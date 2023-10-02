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
license: beerware
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
- :broken_heart: n'aime pas les NFT ou tout autre technologie purement vénalé sans considération pour l'environnement. Merci de respecter ses valeurs.

Il y a déjà de nombreuses ressources et posts ([notamment sur LinkedIn](https://www.linkedin.com/search/results/content/?keywords=prettymaps&origin=FACETED_SEARCH&sid=jXj&sortBy=%22date_posted%22)) sur [prettymaps](https://github.com/marceloprates/prettymaps/) mais je n'ai rien trouvé en français ni rien qui ne détaille vraiment le fonctionnement. Alors c'est parti !

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Prérequis logiciels

- Python 3.9+, correctement configuré dans le `PATH`. Pour Windows, voir cet article.
- une connexion internet
- un terminal. Sur Windows, privilégier [Windows Terminal](https://aka.ms/terminal)

----

## Installation

![logo Python](https://cdn.geotribu.fr/img/logos-icones/programmation/python.png "logo Python"){: .img-rdp-news-thumb }

Dans ses premières versions, le projet était difficilement installable à cause d'un packaging foireux (dépendances non déclarées ou non épinglées, police d'écriture manquante...). Depuis, Marcelo a clairement corrigé le tir et le plus simple est d'utiliser le gestionnaire de paquets Python (`pip`) depuis un terminal, de préférence dans un environnement virtuel en lançant la commande adaptée à votre système.

<!-- markdownlint-disable MD040 -->
<!-- termynal -->

```
$ pip install prettymaps
---> 100%
Installing collected packages: prettymaps
Successfully installed prettymaps-1.0.0
```

<!-- markdownlint-enable MD040 -->

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

    Si un message d'avertissement s'affiche, allez lire [cet article](../2020/2020-06-19_setup_python.md#ajouter-python-au-path) :wink: !
<!-- markdownlint-enable MD046 -->

----

## Une simple adresse suffit

C'est l'un des éléments qui a rendu prettymaps aussi populaire : la simplicité d'utilisation. On sent que l'auteur a fait des efforts pour rendre la vie plus facile à l'utilisateur final que nous sommes, du moins au début :

- une adresse suffit. A noter qu'on peut aussi passer une paire de coordonnées bien sûr ou encore un objet [GeoDataFrame.boundary](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.boundary.html)
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

----

## Jouer avec les préréglages par défaut

Si le rendu par défaut est déjà sympa, la richesse de _prettymaps_ se trouve dans sa capacité à personnaliser les styles des différents objets issus d'OpenStreetMap. L'auteur a intégré dans la bibliothèque des préréglages de styles (_preset_) que l'on peut obtenir avec une simple commande :

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

On exécute de nouveau le script et voilà les 7 résultats (le style `barcelona-plotter` génère une erreur chez moi) :

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

----

## Let's script again : jouer avec les paramètres

![logo OpenStreetMap Python](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/osm_python.png){: .img-rdp-news-thumb }

Maintenant qu'on a bien joué avec les préréglages par défaut, creusons un peu plus loin car prettymaps permet de paramétrer plutôt finement la façon dont les objets OpenStreetMap sont stylisés ainsi que comment la figure (au sens de Matplotlib) est construite :

- `layers` permet de spécifier les objets à récupérer depuis OpenStreetMap, en fait les requêtes à l'API Overpass
- `style` permet de régler le mode de représentation des objets dans Maplotlib : la couleur de fond (`fc`), de bordure (`ec`), la largeur de celle-ci (`lw`), le motif (`hatch`), etc.

Prenons un lieu qui se prête bien à l'exercice : Saint-Malo.

```python linenums="1" title="tuto_prettymaps.py"
# adresse (on peut aussi passer une paire de coordonnées)
adresse = "Saint-Malo, France"

# paramètres appliqués à la carte
plot: prettymaps.draw.Plot = prettymaps.plot(
    query=adresse,
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

```

----

## Sous le capot

```mermaid

```

----

## prettymapp : l'alternative web optimisée

![icône souris clic gauche](https://cdn.geotribu.fr/img/logos-icones/divers/souris_mouse_left-click.webp){: .img-rdp-news-thumb }

Bon, ok, j'aurais pu vous en parler plus tôt mais si j'avais commencé par là, vous n'auriez pas mis les mains dans le cambouis, ni ressenti ce soulagement à l'idée de pouvoir cliquer sur une interface web pour faire les réglages de style :smile:.

L'énorme succès de _prettymaps_ a inspiré de nombreux dérivés, certains comme le méprisable [Aeterna Civitas](https://magiceden.io/marketplace/aeterna_civitas) allant à l'encontre du souhait de l'auteur, le poussant à ne plus publier ses outils en open source... Et d'autres plus heureux comme [_prettymapp_](https://github.com/chrieke/prettymapp/) (oui sans `s` mais avec 2 `p`), le projet de [Christoph Rieke](https://chrieke.com/) qui facilite l'utilisation en proposant une interface graphique pour les principaux paramètres, le tout dans une application web dont l'instance de démo est publique :

[:frame_photo: Utiliser prettymapp](https://prettymapp.streamlit.app/){: .md-button .md-button--primary }
{: align=middle }

![prettymapp - démo](https://github.com/chrieke/prettymapp/raw/main/streamlit-prettymapp/example_prints/demo.gif){: .img-center loading=lazy }

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

{% include "licenses/beerware.md" %}
