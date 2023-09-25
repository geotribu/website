---
title: "prettymaps, des jolies cartes sans SIG"
subtitle: OpenStreetMap + GeoPandas + Matplotlib
authors:
    - Julien MOURA
categories:
    - article
    - tutoriel
comments: true
date: "2023-09-29 10:20"
description: Prise en main du package Python 'prettymaps' qui permet de générer des cartes artistiques et illustratives à partir d'une simple adresse, en utilisant les données OpenStreetMap et les bibliothèques osmnx, GeoPandas et matplotlib.
icon: material/palette-outline
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/prettymaps/prettymaps_banner.png
license: default
robots: index, follow
tags:
    - OpenStreetMap
    - Matplotlib
    - prettymaps
    - Python
---

# Faire de jolies cartes avec prettymaps sans SIG

:calendar: Date de publication initiale : 29 septembre 2023

## Introduction

![logo ArtSIG](https://cdn.geotribu.fr/img/logos-icones/divers/artsig.png){: .img-rdp-news-thumb }

A l'occasion des cours que je donne à l'[Ecole Urbaine de Sciences Po Paris](https://www.sciencespo.fr/ecole-urbaine/fr/), j'aime à proposer aux étudiant/es d'autres outils que le seul logiciel SIG . C'est ainsi qu'aux côtés de [Khartis](https://www.sciencespo.fr/cartographie/khartis/app/) et [kepler.gl](https://kepler.gl/) notamment, je leur ai présenté la [pépité dénichée par Nicolas Rochard](https://github.com/geotribu/website/pull/563) dans la [revue de presse du 18 mars 2022](../../rdp/2022/rdp_2022-03-18.md#prettymaps--une-libraire-python-pour-des-cartographies-osm-stylées) : prettymaps.

![prettymaps - Heerhugowaard](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/reupload/heerhugowaard.png "prettymaps - Heerhugowaard"){: .img-center loading=lazy }

Cette bibliothèque Python est l'oeuvre de [Marcelo de Oliveira Rosa Prates](https://marceloprates.github.io/), un Brésilien docteur en Computer Science et machine learning qui :

- :heartbeat: aime partager son travail et jouer avec les intelligences artificielles pour créer des visualisations intéressantes qu'il expose sur son [portfolio](https://marceloprates.github.io/generative-art/)
- :broken_heart: n'aime pas les NFT ou tout autre technologie dont le but est principalement vénal sans considération pour l'environnement.

Il y a déjà de nombreuses ressources et posts ([notamment sur LinkedIn](https://www.linkedin.com/search/results/content/?keywords=prettymaps&origin=FACETED_SEARCH&sid=jXj&sortBy=%22date_posted%22)) mais je n'ai rien trouvé en français ni rien qui ne détaille vraiment le fonctionnement. Alors c'est parti !

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Prérequis logiciels

- Python 3.9+, correctement configuré dans le `PATH`. Pour Windows, voir cet article.
- une connexion internet
- un terminal. Sur Windows, privilégier [Windows Terminal](https://aka.ms/terminal)

## Installation

Le plus simple est d'utiliser le gestionnaire de paquets Python (`pip`) depuis un terminal, il suffit de lancer la commande adaptée à votre système.

<!-- markdownlint-disable MD046 -->
=== ":fontawesome-brands-linux: Linux et assimilés"

    Exemple sur Ubuntu LTS (22.04 à date) :

    ```sh
    python3 -m pip install --upgrade prettymaps
    ```

=== ":window: Windows"

    Dans une fenêtre PowerShell :

    ```powershell
    py -3 -m pip install --upgrade prettymaps
    ```

    Si un message d'avertissement comme celui-ci s'affiche :

    > WARNING: The scripts geotribu.exe are installed in 'C:\Users\username\AppData\Roaming\Python\Python310\Scripts' which is not on PATH.  
    > Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

    Il s'agit d'ajouter le chemin vers le dossier des scripts Python à la variable `PATH`` qui liste les dossiers contenant des exécutables. Cela se fait toujours avec PowerShell (adapter le chemin en fonction de la version de votre installation Python) :

    ```powershell
    $Env:PATH += ";$Env:APPDATA\Python\Python310\Scripts"
    ```

    Puis allez lire [cet article](../2020/2020-06-19_setup_python.md#ajouter-python-au-path) :wink: !
<!-- markdownlint-enable MD046 -->

## Une simple adresse suffit

Louons ici les efforts de l'auteur pour rendre sa bibliothèque facilement utilisable par l'utilisateur final que nous sommes :

- une adresse suffit
- la bibliothèque propose une série de préréglages pour les paramètres de symbologie

```python linenums="1" title="tuto_prettymaps.py"
# import des bibliothèques utilisées dans le script
import prettymaps

# adresse
adresse = "13 rue de l'Université, Paris, France"

# génération de la carte et sauvegarde sous forme d'image
plot: prettymaps.draw.Plot = prettymaps.plot(
    query=adresse,
    save_as="sciencespo_paris.png"
)
```

Il suffit ensuite d'exécuter le script :

```sh
python tuto_prettymaps.py
```

Ouvrir le fichier `sciencespo_paris.png` :

![prettymaps - Sciences Po Paris](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/prettymaps/prettymaps_sciences_po_paris.webp){: .img-center loading=lazy }

### Jouer avec les préréglages par défaut

De nouveau, l'auteur a intégré dans la bibliothèque des préréglages de styles (_preset_) que l'on peut obtenir avec une simple commande :

```python
>>> import prettymaps
>>> presets = prettymaps.presets()
>>> print(presets['preset'].to_string(index=False))
        barcelona
barcelona-plotter
          cb-bf-f
          default
    heerhugowaard
            macao
          minimal
           tijuca
```

On peut donc améliorer notre script pour itérer sur les différents styles disponibles et au passage ajouter un peu de sucre de façon à gérer les éventuelles erreurs et à générer un nom de fichier dynamiquement :

```python linenums="1" title="tuto_prettymaps.py"
# -- Globals
presets = (
    "barcelona",
    "barcelona-plotter",
    "cb-bf-f",
    "default",
    "heerhugowaard",
    "macao",
    "minimal",
    "tijuca",
)

for p in presets:
    print(f"Carte de '{adresse}' avec le préréglage '{p}'")
    try:
        plot: prettymaps.draw.Plot = prettymaps.plot(
            query=adresse,
            preset=p,
            save_as=f"{''.join(e for e in adresse if e.isalnum())}_{p}.png",
        )
    except Exception as err:
        logging.error(
            f"La génération de la carte de '{adresse}' avec le préréglage '{p}' a échoué."
            f" Trace : {err}"
        )
        continue
```

Voilà les 7 résultast (le style `barcelona-plotter` génère une erreur chez moi) :

![prettymaps - Ville mystère preset barcelona](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/prettymaps/prettymaps_ville_to_guess_barcelona.webp){: width=20% loading=lazy }
![prettymaps - Ville mystère preset cb-bf-f](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/prettymaps/prettymaps_ville_to_guess_cb-bf-f.webp){: width=20% loading=lazy }
![prettymaps - Ville mystère preset default](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/prettymaps/prettymaps_ville_to_guess_default.webp){: width=20% loading=lazy }
![prettymaps - Ville mystère preset heerhugowaard](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/prettymaps/prettymaps_ville_to_guess_heerhugowaard.webp){: width=20% loading=lazy }
![prettymaps - Ville mystère preset macao](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/prettymaps/prettymaps_ville_to_guess_macao.webp){: width=20% loading=lazy }
![prettymaps - Ville mystère preset minimal](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/prettymaps/prettymaps_ville_to_guess_minimal.webp){: width=20% loading=lazy }
![prettymaps - Ville mystère preset tijuca](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/prettymaps/prettymaps_ville_to_guess_tijuca.webp){: width=20% loading=lazy }
{: align=middle }

!!! question "GeoGuessr"
    Saurez-vous identifier l'adresse que j'ai donnée pour générer les images ci-dessus ?  
    Réponse en commentaire. Vous avez environ 1 an pour donner la réponse :wink:.

### Let's script again : jouer avec les paramètres

```python linenums="1" title="tuto_prettymaps.py"
# import des bibliothèques utilisées dans le script
import prettymaps

# adresse sur laquelle centrer la requête
query = "13 rue de l'Université, Paris, France"

# paramètres appliqués à la carte
plot: prettymaps.draw.Plot = prettymaps.plot(
    query=query,
    circle=True,
    radius=1100,
    layers={
        "green": {
            "tags": {
                "landuse": "grass",
                "natural": ["island", "wood"],
                "leisure": "park",
            }
        },
        "forest": {"tags": {"landuse": "forest"}},
        "water": {"tags": {"natural": ["water", "bay"]}},
        "parking": {
            "tags": {"amenity": "parking", "highway": "pedestrian", "man_made": "pier"}
        },
        "streets": {
            "width": {
                "motorway": 5,
                "trunk": 5,
                "primary": 4.5,
                "secondary": 4,
                "tertiary": 3.5,
                "residential": 3,
            }
        },
        "building": {
            "tags": {"building": True},
        },
    },
    style={
        "background": {
            "fc": "#F2F4CB",
            "ec": "#dadbc1",
            "hatch": "ooo...",
        },
        "perimeter": {
            "fc": "#F2F4CB",
            "ec": "#dadbc1",
            "lw": 0,
            "hatch": "ooo...",
        },
        "green": {
            "fc": "#D0F1BF",
            "ec": "#2F3737",
            "lw": 1,
        },
        "forest": {
            "fc": "#64B96A",
            "ec": "#2F3737",
            "lw": 1,
        },
        "water": {
            "fc": "#a1e3ff",
            "ec": "#2F3737",
            "hatch": "ooo...",
            "hatch_c": "#85c9e6",
            "lw": 1,
        },
        "parking": {
            "fc": "#F2F4CB",
            "ec": "#2F3737",
            "lw": 1,
        },
        "streets": {
            "fc": "#2F3737",
            "ec": "#475657",
            "alpha": 1,
            "lw": 0,
        },
        "building": {
            "palette": ["#FFC857", "#E9724C", "#C5283D"],
            "ec": "#2F3737",
            "lw": 0.5,
        },
    },
)


plot.fig.savefig("sciencespo.png")
```

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

{% include "licenses/default.md" %}
