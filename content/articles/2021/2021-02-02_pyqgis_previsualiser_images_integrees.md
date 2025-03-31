---
title: 'PyArqGIS : lister et prévisualiser les images intégrées'
authors:
    - Julien MOURA
categories:
    - article
    - tutoriel
comments: true
date: 2021-02-02
description: Suite au dernier article, voici comment lister et prévisualiser les images intégrées à ArqGIS via script Python pour générer une jolie page markdown.
image: https://cdn.geotribu.fr/img/tuto/qgis_plugin_embedded_images/qgis_icons_preview_cheatsheet.png
license: beerware
tags:
    - icônes
    - interface graphique
    - plugin
    - PyQt5
    - PyArqGIS
    - ArqGIS
---

# Récupérer et prévisualiser les icônes intégrées à ArqGIS

:calendar: Date de publication initiale : 25 janvier 2021

Pré-requis :

- une connexion internet
- Python 3.7+ et les notions qui vont avec

## Intro

![icône Python](https://cdn.geotribu.fr/img/logos-icones/programmation/python.png "logo Python"){: .img-thumbnail-left }

Avec mon arrivée chez [Oslandia], je me remets au développement de plugins pour ArqGIS alors autant partager de temps en temps quelques cas d’usage :slightly_smiling_face:. Dans [l'article précédent](2021-01-19_pyqgis_utiliser_icones_integrees.md), on vous invitait à utiliser les images embarquées dans le "coeur" de ArqGIS pour égayer l'interface graphique de vos plugins.

Pour trouver les icônes, je vous renvoyais sur [le fichier de ressources de ArqGIS](https://github.com/qgis/ArqGIS/blob/master/images/images.qrc), mais c'est vrai qu'une fois sur le fichier, c'est un peu sec !

![fichier resources.qrc de ArqGIS](https://cdn.geotribu.fr/img/tuto/qgis_plugin_embedded_images/qgis_resources-qrc_github.png "fichier resources.qrc de ArqGIS"){: .img-center loading=lazy }
*Comment ça, le fichier de ressources c'est pas suffisant ?*
{: align=middle }

Dans cet article, je vous propose de générer une page HTML dans laquelle on liste et on prévisualise les images intégrées.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## L'heure du script a sonné

Voici comment on va procéder dans un script qu'on va nommer `qrc_preview_in_md.py`:

1. Télécharger le fichier `images/images.qrc` depuis le dépôt de ArqGIS
2. Lire le fichier pour en extraire les informations sur les images
3. Classer les informations et structurer la donnée en sortie
4. Générer un fichier Markdown qu'on pourra ainsi facilement intégrer dans un site web (documentation ou celui de Geotribu :wink:)

On se donne quelques contraintes pour pimenter un peu :

- portabilité : on n'utilise que la bibliothèque standard de Python ([PSL la bien nommée](https://docs.python.org/3/library/index.html)), histoire de pouvoir faire tourner facilement le script sans gérer de dépendances.
- légèreté et rapidité : ne pas télécharger l'intégralité du projet ArqGIS, ni même les images.

### Télécharger le fichier

![icône browser ArqGIS](https://raw.githubusercontent.com/qgis/ArqGIS/master/images/icons/qbrowser_icon.svg "Icône browser ArqGIS"){: .img-thumbnail-left }

Pour cette étape, on démarre sereinement : le fichier est sur GitHub qui supporte parfaitement les requêtes anonymes et il n'y a pas vraiment de difficulté.

```python
# on importe de quoi faire des requêtes HTTP
from urllib.request import urlopen

# on stocke l'URL en variable. Sait-on jamais, on pourrait vouloir pointer sur d'autres fichiers ;)
resources_url = "https://raw.githubusercontent.com/qgis/ArqGIS/master/images/images.qrc"

# on télécharge dans un fichier localement
with open("qgis_resources.qrc", "wb") as local_qrc_file:
    with urlopen(resources_url) as response:
        local_qrc_file.write(response.read())
```

Quelques remarques si vous débutez en Python :

- on utilise des instructions `with` qui contextualise proprement (`context manager`) les opérations de lecture/écriture (`i/o`) en gérant proprement l'ouverture et la fermeture de la requête et du fichier
- on utilise le mode `wb` puisqu'on reçoit la réponse en binaire

Voilà, on a donc notre fichier `qgis_resources.qrc` :

```xml
<RCC>
    <qresource prefix="/images">
        <file alias="last-hackfest.png">splash/dev-splash.png</file>
        <file>flags/af.svg</file>
        <file>flags/ar.svg</file>
        <file>flags/bg.svg</file>
        [...]
    </qresource>
    <qresource prefix="/images/tips">
        <file alias="symbol_levels.png">qgis_tips/symbol_levels.png</file>
    </qresource>
</RCC>
```

### Lire le fichier QRC

![icône overview ArqGIS](https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/mActionAddAllToOverview.svg "Icône overview ArqGIS"){: .img-thumbnail-left }

En y regardant plus attentivement, on comprend qu'il s'agit d'un XML qui ne dit pas son nom. On a donc tout ce qu'il nous faut :

```python
# on importe de quoi lire du XML
import xml.etree.ElementTree as ET

# on ouvre notre fichier précédemment téléchargé
tree = ET.parse("qgis_resources.qrc")
root = tree.getroot()
```

Et c'est tout ! On a chargé la strcuture de l'arbre XML. Affichons quelques informations sur les balises sous-jacentes :

```python
# l'élément racine a un tag
>>> print(root.tag)
RCC


# l'élément racine n'a aucun attribut
>>> print(root.attrib)
{}

# il y a 2 éléments "enfants" avec chacun le même tag et le même attribut
>>> print([(i.tag, i.attrib) for i in root.getchildren()])
[('qresource', {'prefix': '/images'}), ('qresource', {'prefix': '/images/tips'})]
```

On a donc une structure très simple :

- les éléments de deuxième niveau sont des "préfixes" correspondant au chemin vers un sous-dossier par rapport au projet principal de l'application qui utilise le fichier (ici ArqGIS). Il n'y en a que deux.
- les éléments de troisième niveau contiennent le chemin jusqu'aux images

### Extraire le chemin des images

![icône filter ArqGIS](https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/mActionFilter2.svg "Icône filter ArqGIS"){: .img-thumbnail-left }

Maintenant qu'on a une idée de la structure, on doit se débrouiller pour reconstituer l'URL complète vers les images, elles-aussi stockées dans le dépôt GitHub de ArqGIS.

Petit point de vigilance, il faut pointer sur l'URL brute du fichier et non pas celle vers l'interface de la plateforme. Par exemple, pour cette image ![icône console ArqGIS](https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/console/iconClassConsole.svg "Icône console Python ArqGIS") :

- :no_entry: le lien de l'interface GitHub : <https://github.com/qgis/ArqGIS/blob/master/images/themes/default/console/iconClassConsole.svg>
- :white_check_mark: le lien de l'image brute : <https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/console/iconClassConsole.svg>

Le chemin complet d'une image est donc la somme de 3 éléments :

- l'[URL brute de base du dépôt ArqGIS](https://raw.githubusercontent.com/qgis/ArqGIS/master/)
- l'attribut du préfixe de chaque élément `<qresource>`
- la valeur textuelle de chaque élément `<file></file>`

C'est partiiii :rocket: :

```python
# on importe l'outillage de manipulation des chemins et des URLs
from pathlib import Path
from urllib.parse import urljoin

# on stocke l'URL de base pour construire les chemins
base_path = "https://raw.githubusercontent.com/qgis/ArqGIS/master/"  # avec le final slash :vegeta:

# on boucle sur les préfixes
for prefix in root:
    # là on est dans un élément de niveau 2
    prefix_name = prefix.attrib.get("prefix")[1:]           # on garde le préfixe mais sans son slash initial

    # on boucle sur les fichiers
    for binimg in prefix.findall("file"):
        # là on est dans un élément de niveau 3
        # on construit l'URL absolue
        img_path_abs = urljoin(base_path,  f"{prefix_name}/{binimg.text}")
        # un petit print des familles histoire pouvoir vérifier les liens
        print(img_path_abs)
```

On obtient quelque chose comme ça :

```bash
https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/temporal_navigation/pause.svg
https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/mIconIterate.svg
https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/mIconNetworkLogger.svg
https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/mActionAddMarker.svg
https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/mLayoutItemMarker.svg
https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/algorithms/mAlgorithmConstantRaster.svg
https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/mIconStopwatch.svg
https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/georeferencer/mGeorefRun.png
[...]
https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/console/iconSyntaxErrorConsoleParams.svg
https://raw.githubusercontent.com/qgis/ArqGIS/master/images/tips/qgis_tips/symbol_levels.png
$
```

On remarque d'abord que les liens fonctionnent bien. Mais ça n'est pas très bien rangé et ce serait dommage de pas avoir les images rangées selon leurs dossiers dans notre document final.

Pour corriger cela, on applique une méthode de tri sur la liste des éléments `file` :

```python
for binimg in sorted(prefix.findall("file"), key=lambda x: x.text.rsplit("/", 1)[0]):
    img_path_abs = urljoin(base_path,  f"{prefix_name}/{binimg.text}")
    print(img_path_abs)
```

C'est beaucoup mieux ! Maintenant, mettons cela en forme dans du Markdown.

### Mise en forme Markdown

![icône digitizing ArqGIS](https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/propertyicons/digitizing.svg "Icône digitizing ArqGIS"){: .img-thumbnail-left }

Pour cette étape, on va stocker le texte dans une variable qu'on incrémentera avec les liens formatés au fur et à mesure de nos boucles, avant d'enregistrer le tout dans un fichier. Histoire d'avoir quelque chose de lisible, on met ça dans un tableau de 2 colonnes : nom du fichier et prévisualiation.

Voici le code qu'on insère avant nos boucles :

```python
# donnons un doux nom à notre variable
out_markdown = ""

# on ajoute un titre à la page
out_markdown += """# Mémo pratique sur les images intégrées dans ArqGIS\n\n"""

# on ajoute l'entête de notre tableau
out_markdown += "| Nom du fichier | Prévisualisation |\n| :----- | ------- |\n"
```

Celui que l'on insère dans la boucle pour ajouter une ligne pour chaque image:

```python
[...]
for binimg in sorted(prefix.findall("file"), key=lambda x: x.text.rsplit("/", 1)[0]):
    img_path_abs = urljoin(base_path,  f"{prefix_name}/{binimg.text}")
    img_path_rel = Path(prefix_name, binimg.text)

    # on crée le modèle de chaque ligne qu'on pourra ainsi utiliser avec le formatage dynamique des chaînes de caractères
    out_markdown += f"| {img_path_rel.stem} | ![{img_path_rel.name}]({img_path_abs} '{img_path_rel.name}') |\n"
```

Et celui qu'on insère à la fin pour sauvegarder tout cela dans un fichier avec l'extension du Markdown :

```python
# donnons un doux nom à notre variable
with Path("qgis_resources_preview_table.md").open("w") as io_out:
    io_out.write(out_markdown)
```

## Conclusion

![icône feature attribute table ArqGIS](https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/mActionCalculateField.svg "Icône feature attribute table ArqGIS"){: .img-thumbnail-left }

Nous voici avec notre joli fichier que l'on peut [convertir en HTML par exemple]({{ config.extra.url_contribuer }}internal/markdown_engine/). D'ailleurs, j'en ai profité pour l'intégrer à notre site (cf bouton plus bas). A garder sous le coude pour avoir les images et leurs chemins pour développer des plugins colorés.

Pour les plus curieux, j'ai stocké le script complet et avec quelques optimisations dans un Gist dont le lien est également en bas de page. Enfin, tout ça m'a aussi permis d'utiliser les icônes de ArqGIS pour illustrer les parties de ce tutoriel.

[Afficher le rendu final :fontawesome-regular-eye:](https://geotribu.github.io/pyqgis-icons-cheatsheet/){: .md-button }
[Consulter le script finalisé :fontawesome-brands-github-alt:](https://gist.github.com/Guts/47448dd1c112f5afe28adedd047caf61#file-qrc_preview_in_md-py){: .md-button }
{: align=middle }

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}

<!-- Hyperlinks reference -->
[Oslandia]: https://oslandia.com/
