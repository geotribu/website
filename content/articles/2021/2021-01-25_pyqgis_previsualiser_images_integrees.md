---
title: "QGIS : lister et prévisualiser les images intégrées"
authors: ["Julien MOURA"]
categories: ["article", "tutoriel"]
date: "2020-01-25 10:20"
description: "Suite au dernier article, voici les images intégrées à QGIS et le script qui va avec pour générer une jolie page markdown."
image: "https://cdn.geotribu.fr/img/tuto/qgis_plugin_embedded_images/qgis_icons_file-explorer.png"
tags: "geotribu,QGIS,plugin,PyQt5,icônes,interface graphique"
---

# Récupérer et prévisualiser les icônes intégrées à QGIS

:calendar: Date de publication initiale : 25 janvier 2021

**Mots-clés :** Python | QGIS | développement | plugin | interface graphique | script | Markdown

Pré-requis :

- une connexion internet
- des notions en Python

## Intro

![icône Python](https://cdn.geotribu.fr/img/logos-icones/programmation/python.png "logo Python"){: .img-rdp-news-thumb }

Avec mon arrivée chez [Oslandia], je me remets au développement de plugins pour QGIS alors autant partager de temps en temps quelques cas d’usage :slightly_smiling_face:. Dans [l'article précédent](/articles/2021/2021-01-19_pyqgis_utiliser_icones_integrees.md), on vous invitait à utiliser les images embarquées dans le "coeur" de QGIS pour égayer l'interface graphique de vos plugins.

Pour trouver les icônes, je vous renvoyais sur [le fichier de ressources de QGIS](https://github.com/qgis/QGIS/blob/master/images/images.qrc), mais c'est vrai qu'une fois sur le fichier, c'est un peu sec !

![fichier resources.qrc de QGIS](https://cdn.geotribu.fr/img/tuto/qgis_plugin_embedded_images/qgis_resources-qrc_github.png "Le fichier resources.qrc de QGIS"){: .img-center }
*Comment ça, le fichier de ressources c'est pas suffisant ?*
{: align=middle }

Dans cet article, je vous propose de générer une page HTML dans laquelle on liste et on prévisualise les images intégrées.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## L'heure du script a sonné

Voici comment on va procéder :

1. Télécharger le fichier `images/images.qrc` depuis le dépôt de QGIS
2. Lire le fichier pour en extraire les informations sur les images
3. Classer les informations et structurer la donnée en sortie
4. Générer un fichier Markdown qu'on pourra ainsi facilement intégrer dans un site web (documentation ou celui de Geotribu :wink:)

On se donne quelques contraintes pour pimenter un peu :

- portabilité : on n'utilise que la bibliothèque standard de Python ([PSL la bien nommée](https://docs.python.org/3/library/index.html)), histoire de pouvoir faire tourner facilement le script sans gérer de dépendances.
- légèreté et rapidité : ne pas télécharger l'intégralité du projet QGIS, ni même les images.

### Télécharger le fichier

Pour cette étape, on démarre sereinement : le fichier est sur GitHub qui supporte parfairement les requêtes anonymes et il n'y a pas vraiment de difficulté.

```python
# on importe de quoi faire des requêtes HTTP
from urllib.request import urlopen

# on stocke l'URL en variable. Sait-on jamais, on pourrait vouloir pointer sur d'autres fichiers ;)
resources_url = "https://raw.githubusercontent.com/qgis/QGIS/master/images/images.qrc"

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

- les éléments de second niveau sont des "préfixes" correspondant au chemin vers un sous-dossier par rapport au projet principal de l'application qui utilise le fichier (ici QGIS). Il n'y en a que deux.
- les éléments de troisième niveau contiennent le chemin jusqu'aux images

### Extraction



```python
# on importe de quoi lire du XML
import xml.etree.ElementTree as ET

# on ouvre notre fichier précédemment téléchargé
tree = ET.parse("qgis_resources.qrc")
root = tree.getroot()
```

for prefix in root:
    if prefix.tag == "qresource" and "prefix" in prefix.attrib:
        # set prefix (= level 2 in markdown)
        prefix_name = prefix.attrib.get("prefix")[1:]
        prefix_path = Path(prefix.attrib.get("prefix")[1:])
        out_markdown += "\n## {}\n".format(prefix_name)

> TO WRITE

### Mise en forme Markdown

> TO WRITE

## Conclusion

> TO DOC

[Afficher le rendu final :fontawesome-regular-eye:](/toc_nav_ignored/qgis_resources_preview_table/){: .md-button }
{: align=middle }

----

## Auteur

--8<--
content/team/jmou.md
--8<--

<!-- Hyperlinks reference -->
[Oslandia]: https://oslandia.com/
