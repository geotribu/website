---
title: "Rechercher des images"
subtitle: "Trouver la bonne image ou le bon logo"
authors:
    - Julien MOURA
categories:
    - article
    - meta
date: 2022-11-26 14:20
description: "Guide pour rechercher dans l'entrepôt d'images de Geotribu (https://cdn.geotribu.fr/), via l'interface graphique de TinyFileManager ou bien via un script pour interroger l'index lunr."
icon: material/image-search
image: https://cdn.geotribu.fr/img/internal/contribution/embed_image/geotribu_cdn_tinyfilemanager_search.png
robots: index, follow
tags:
    - cdn
    - images
    - script
    - Python
---

# Rechercher des images dans le CDN de Geotribu

## Parcourir le CDN via l'interface web

L'accès en lecture à [notre entrepôt d'images](/contribuer/guides/cdn-images-hebergement/) accumulées depuis toutes ces années est ouvert :gift_heart: et c'est même un passage recommandé pour tout contributeur/rice :

- adresse : <https://cdn.geotribu.fr>
- identifiant : `invité`
- mot de passe : `geotribu_bemyguest2020`

En plus de permettre un petit voyage dans le temps, autant que toutes ces ressources servent en plus de notre site :smiley:. Merci de ne pas en abuser en respectant le _fair-use_. Pensez également à créditer les auteur/es.

### Chercher une image

#### Filtrer le dossier courant

La barre de recherche en haut permet de filtrer sur le nom du fichier parmi ceux du répertoire courant. A noter qu'il faut attendre que l'ensemble des fichiers du répertoire soient listés pour que ce la fonctionne.

![Filtrer le dossier courant dans TinyFileManager](https://cdn.geotribu.fr/img/internal/contribution/embed_image/geotribu_cdn_tinyfilemanager_filter.png){: .img-center loading=lazy }

#### Recherche avancée

Il est également possible d'effectuer une recherche dans l'arborescence en cliquant sur le menu descendant à droite de la barre de filtre et de sélectionner "Recherche avancée" :

![Recherche avancée dans TinyFileManager](https://cdn.geotribu.fr/img/internal/contribution/embed_image/geotribu_cdn_tinyfilemanager_search.png){: .img-center loading=lazy }

----

## Faire une recherche en requêtant l'index lunr

![logo Python](https://cdn.geotribu.fr/img/logos-icones/programmation/python.png "logo Python"){: .img-rdp-news-thumb }

Si l'interface graphique vous semble trop longue ou la recherche assez fine ou que vous n'avez pas les identifiants sous la main, il est possible d'interroger [l'index des images stockées](https://cdn.geotribu.fr/img/search-index.json) généré avec [lunr.py] toutes les heures et qui est accessible librement.

Pré-requis :

- Python >= 3.9
- une connexion autorisée vers <https://cdn.geotribu.fr>

### Créer un environnement virtuel

Sauf si vous voulez installer [lunr.py] au niveau de votre interpréteur système, mieux vaut faire la tambouille dans un environnement isolé :

1. Créer un dossier pour le script et s'y déplacer :

    ```sh
    mkdir -p ~/Geotribu/ && cd ~/Geotribu
    ```

1. Créer l'environnement virtuel :

    ```sh
    python3 -m venv .venv
    ```

1. Activer l'environnement virtuel :

    ```sh
    source .venv/bin/activate
    ```

### Installer ou mettre à jour les dépendances

Une fois l'environnement virtuel activé, on met à jour pip et les paquets de base :

```sh
python -m pip install -U pip
python -m pip install -U setuptools wheel
```

Puis on installe les dépendances :

```sh
python -m pip install -U "lunr>=0.6,<1"
```

### Let's script again

Avec notre script, on va :

1. télécharger localement le fichier d'index depuis le CDN
1. le charger et regarder un peu à quoi il ressemble
1. faire une recherche
1. enrichir les résultats

#### Télécharger l'index du CDN

On cherche donc à télécharger le fichier `https://cdn.geotribu.fr/img/search-index.json` dans un sous-dossier `.geotribu/search/` qu'on crée si besoin dans le dossier personnel de l'utilisateur courant : `/home/nom_utilisateur/` sur Linux ou `C:\Users\nom_utilisateur\` sur Windows, généralement accessible avec l'alias `~`.

Pour télécharger le fichier de l'index, étant donné qu'on n'a pas de cas particulier (VPN, authentification...) on utilise la bibliothèque standard de Python :

```python title="Téléchargement du fichier JSON distant avec _urllib_"
#! python3  # noqa: E265

# import
from pathlib import Path
from urllib.request import Request, urlopen

# variables
index_local_file: Path = Path().home() / ".geotribu/search/cdn_search_index.json"
remote_index_file: str = "https://cdn.geotribu.fr/img/search-index.json"

# on s'assure que les dossiers parents existent
index_local_file.parent.mkdir(parents=True, exist_ok=True)

# téléchargement
with urlopen(remote_index_file) as response:
    with index_local_file.open(mode="wb") as output_file:
        output_file.write(response.read())
```

Normalement, à ce stade, on a donc un fichier dans notre dossier personnel :

![Fichier index téléchargé localement](https://cdn.geotribu.fr/img/internal/contribution/embed_image/index_cdn_geotribu_local.webp){: .img-center loading=lazy }

#### Charger et ausculter le fichier

S'agissant d'un fichier JSON, on ajoute l'import du package en haut de notre script :

```python hl_lines="3"
[...]
# import
import json
from pathlib import Path
[...]
```

Puis on charge le fichier à la suite de notre script :

```python
with index_local_file.open("r") as fd:
    local_index_data = json.loads(fd.read())
```

Comme toujours avec des données distantes, on prend le temps de regarde run peu la structure :

```python
print(type(local_index_data))
#  <class 'dict'>
print(local_index_data.keys())
# dict_keys(['images', 'index'])
print(
    type(local_index_data.get("images")),
    len(local_index_data.get("images")),
    list(local_index_data.get("images").items())[:2],
)
# <class 'dict'> 3934 [('18bitmap.png', [100, 100]), ('3typomap.png', [100, 100])]
print(
    type(local_index_data.get("index")),
    len(local_index_data.get("index")),
    local_index_data.get("index").keys(),
)
# <class 'dict'> 5 dict_keys(['fieldVectors', 'fields', 'invertedIndex', 'pipeline', 'version'])
```

On voit donc qu'on a :

- un dictionnaire en contenant 2 autres dont les clés sont : `images` et `index`
- le dictionnaire `images` contient 3 934 entrées, chacune correspondant à une image du CDN dont la clé est le chemin et la valeur est une liste contenant 2 entiers. En se référant au [script qui génère l'index](https://github.com/geotribu/infra/blob/master/ansible/roles/cdn-indexer/files/search_indexer.py#L113), on comprend qu'il s'agit de la largeur et la longueur en pixels de l'image.
- le dictionnaire `index` correspond à la structure d'index de lunr

#### Faire une recherche

Pour la recherche, on utilise [lunr.py].  
On commence par importer le module depuis le package en haut de fichier. On en profite pour ajouter aussi [`pprint`](https://docs.python.org/fr/3/library/pprint.html) qui nous permettra d'y voir plus clair dans les résultats :

```python hl_lines="2 6"
[...]
from pprint import pprint
from urllib.request import Request, urlopen

# 3rd party
from lunr.index import Index

# variables
[...]
```

On charge l'index :

```python
idx = Index.load(local_index_data.get("index"))
```

Et on peut alors faire une recherche :

```python
search_results = idx.search("satellite")
pprint(search_results)
# [{'match_data': <MatchData "satellit">,
#   'ref': 'logos-icones/divers/satellite.png',
#   'score': 79.718},
#  {'match_data': <MatchData "satellit">,
#   'ref': 'articles-blog-rdp/capture-ecran/reupload/matching-satellite.png',
#   'score': 58.613}]
```

##### Recherche avancée

Il est aussi possible de passer des paramètres de recherche plus avancés. Par exemple :

- rechercher la correspondance seulement dans le nom du fichier :

```python
>>> pprint(len(idx.search("qgis")))
34
>>> pprint(len(idx.search("name:qgis")))
12
```

- quand il y a 2 termes, c'est la clause `OR` qui s'applique. Exemple, les images qui correspondent à `openstreetmap` **ou** `logo` :

```python
pprint(idx.search("openstreetmap logo"))
```

- rechercher les images qui correspondent à `openstreetmap` **et** `logo` :

```python
pprint(idx.search("+openstreetmap +logo"))
# [{'match_data': <MatchData "logo,openstreetmap">,
#   'ref': 'logos-icones/OpenStreetMap/Openstreetmap.png',
#   'score': 61.5621305836632}]
```

- rechercher les images qui contiennent `logo` dans le chemin **et** `qgis` dans le nom du fichier

```python
pprint(idx.search("+path:logo +name:qgis"))
# [{'match_data': <MatchData "logo,qgi">,
#   'ref': 'logos-icones/logiciels_librairies/qgis.png',
#   'score': 52.797999999999995},
#  {'match_data': <MatchData "logo,qgi">,
#   'ref': 'logos-icones/entreprises_association/qgis-ch.png',
#   'score': 39.056000000000004}]
```

#### Enrichir la recherche

C'est déjà pas mal mais on aimerait croiser avec les métadonnées qui sont dans le dictionnaire `images` d'à-côté.
En regardant de plus près la structure de nos résultats de recherche, on voit qu'il s'agit là d'un dictionnaire contenant 3 clés/valeurs :

- `match_data` donne les termes de correspondance entre la requête et les résultats
- `ref` contient le chemin du fichier relatif à l'URL de base du CDN
- `score` donne le score de correspondance

Il y a donc matière à faire une jointure entre les deux dictionnaires sur le chemin du fichier : `ref` d'un côté, clé de l'autre.

On itère donc sur les résultats et on étend chaque résultat avec les métadonnées :

```python title="Croisement résultat de recherche et métadonnées"
# on stocke la recherche et le dictionnaire des métadonnées des images dans des variables
search_results = idx.search("+path:logo +name:qgis")
images_dict = local_index_data.get("images")

for search_result in search_results:
    mapped_img = images_dict.get(search_result.get("ref"))
    search_result.update(
        {
            "width": mapped_img[0],
            "height": mapped_img[1],
            "full_url": f"https://cdn.geotribu.fr/img/{search_result.get('ref')}",
        }
    )
pprint(search_result)

# [{'full_url': 'https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png',
#   'height': 339,
#   'match_data': <MatchData "logo,qgi">,
#   'ref': 'logos-icones/logiciels_librairies/qgis.png',
#   'score': 52.797999999999995,
#   'width': 360},
#  {'full_url': 'https://cdn.geotribu.fr/img/logos-icones/entreprises_association/qgis-ch.png',
#   'height': 74,
#   'match_data': <MatchData "logo,qgi">,
#   'ref': 'logos-icones/entreprises_association/qgis-ch.png',
#   'score': 39.056000000000004,
#   'width': 74}]
```

### Aller plus loin

Il s'agit ici d'un exemple rapide de script rapide.  
Si vous utilisez régulièrement la recherche dans l'index, je vous recommande d'utiliser notre script `search_playground.py` qui intègre :

- la gestion des erreurs HTTP
- le téléchargement du fichier d'index seulement selon un temps de rotation (24h par défaut)

[Consulter le script complet :fontawesome-regular-file-code:](https://github.com/geotribu/infra/blob/master/search-index/search_playground.py){: .md-button }
{: align=middle }

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

<!-- Liens de référence -->
[lunr.py]: https://lunr.readthedocs.io/
