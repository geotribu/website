---
title: "Rechercher des images dans le CDN"
subtitle: Trouver l'image ou le logo souhaité pour éviter d'ajouter un doublon
authors:
    - Julien MOURA
categories:
    - article
    - meta
date: 2022-11-26 14:20
description:
icon: material/image-search
image: https://cdn.geotribu.fr/img/internal/contribution/embed_image/geotribu_cdn_tinyfilemanager_search.png
robots: index, follow
tags:
    - cdn
    - images
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

## Faire une recherche via un script

![logo Python](https://cdn.geotribu.fr/img/logos-icones/programmation/python.png "logo Python"){: .img-rdp-news-thumb }

Si l'interface graphique vous semble trop longue ou la recherche assez fine ou que vous n'avez pas les identifiants sous la main, il est possible d'interroger l'index des images stockées généré avec lunr.py toutes les heures et qui est accessible librement.

Pré-requis :

- Python >= 3.9
- une connexion autorisée vers <https://cdn.geotribu.fr>

### Créer un environnement virtuel

Sauf si vous voulez installer [lunr.py](https://lunr.readthedocs.io/) au niveau de votre interpréteur système, mieux vaut faire la tambouille dans un environnement isolé :

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

#### Télécharger l'index du CDN

On cherche à télécharger le fichier `https://cdn.geotribu.fr/img/search-index.json` dans le dossier `.geotribu/search/` qu'on crée si besoin dans l'espace personnel de l'utilisateur courant.

Pour télécharger le fichier de l'index, étant donné qu'on n'a pas de cas particulier (VPN, authentification...) on utilise la bibliothèque standard de Python :

```python
#! python3  # noqa: E265

# import
from pathlib import Path
from urllib.request import Request, urlopen

# variables
index_local_file: Path = Path().home() / ".geotribu/search/cdn_search_index.json"
remote_index_file: str = "https://cdn.geotribu.fr/img/search-index.json"

# -- MAIN --------------------------------------------------------------------

# on s'assure que les dossiers parents existent
index_local_file.parent.mkdir(parents=True, exist_ok=True)

# téléchargement
with urlopen(custom_request) as response:
    with index_local_file.open(mode="wb") as output_file:
        output_file.write(response.read())
```

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"
