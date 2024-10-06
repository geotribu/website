---
title: Testez QGIS 4
subtitle:
authors:
    - Julien MOURA
categories:
    - article
comments: true
date: 2024-11-09
description: "Description de 160 caractères maximum qui résume l'article qui est présente dans le flux RSS, la newsletter, les moteurs de recherche, en page d'accueil... "
icon: material/crystal-ball
image: "Image d'illustration de l'article qui sert ensuite dans la mise en avant : réseaux sociaux, flux RSS... 400x800 en PNG"
license: default
robots: index, follow
tags:
    - QGIS
    - Qt
    - OSGeo4W
---

# QGIS 4

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Architecture de QGIS

```mermaid
flowchart TD
    A{QGIS} -->|Dépend de| B(Qt)
    A -->|Dépend de| C(API géospatiales)
    B:::blocimportant --> S{"Système exploitation<br/>(et donc toutes les API système)"}
    C --->|dépend de| D[/GDAL\]
    D --> E
    D --> G
    D --> F
    D --> Z@{ shape: docs, label: "Environ 73% des <br/>bibliothèques de drivers <br/>de formats de données <br/>géo-quelque-chose"}
    C -->|dépend de| E[GEOS]
    C -->|dépend de| F[PROJ]
    C --->|dépend de| G[("Clients BDD<br/>liboci, libpq, <br/>libspatialite...")]

    classDef blocimportant fill:#ff0000
```

Actuellement, c'est la version 5 de Qt qui est utilisée dans QGIS 3. Il se trouve qu'elle est arrivée en fin de vie en... mai 2025 selon [la documentation officielle](https://doc.qt.io/qt-6/supported-platforms.html#supported-qt-versions).

![Planning des versions de Qt](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qgis_4_qt6/qt_versions_planning.webp){: .img-center loading=lazy }

----

## Sur Windows

### Niveau : Arche Perdue

[le workflow Windows Qt6](https://github.com/qgis/QGIS/actions/workflows/windows-qt6.yml?query=is%3Asuccess)

Sinon, en mars dernier, OPENGIS.ch, en tête de pont sur le packaging Windows avec vcpkg diffusait un lien de téléchargement sur leurs réseaux sociaux.  <https://download.opengis.ch/qgis-qt6.zip>

!!! note "Dans l'ombre de la DSI"
    Notez que cette version téléchargeable et autoporteuse est idéale pour les environnements où les droits d'installation sont limités.
    Si on vous demande d'où ça sort, dites que vous avez lu ça sur [arcOrama](https://www.arcorama.fr/) :zipper_mouth:.

### Avec l'OSGeo4W

[Télécharger l'installateur OSGeo4W](https://download.osgeo.org/osgeo4w/v2/osgeo4w-setup.exe){: .md-button }
{: align=middle }

Lancer en mode administrateur puis suivre les étapes :

1. _Advanced Install_
1. Install from Internet
1. All Users

    Choisir un dossier convenable pour l'installation car on n'est pas des bêtes quand même. Par exemple, soyons civilisés et mettons cela dans `%PROGRAMFILES%/QGIS/OSGeo4W`

1. Tant pis pour l'avertissement. Si en 2024 on doit encore s'embêter avec des espaces dans les cehmins de fichiers, c'est qu'on a un souci d'anachronisme. Ignorons et continuons donc.
1. Laissons les valeurs par défaut
1. Dans le champ Search, taper `qt6-dev-full`
1. Dérouler `Desktop`
1. Cliquer sur `Skip` en regard de `qgis-qt6-dev-full` jusqu'à obtenir un numéro de version (probablement impair et supérieur d'un chiffre à la version courante.)
1. suivant, suivant
1. cocher les licences (ERDAS, MrSID, ORacle, SZIP...). Notez qu'il est aussi possible de les imprimer de façon à les étudier en détail.
1. :coffee:
1. Il y aura peut-être des erreurs mais qu'importe, vous êtes arrivés jusqu'ici car vous vouliez un goût d'aventure dans la bouche ? Il n'est plus temps de reculer pour si peu.

### Titre 3

On lance, on prend le temps d'essayer de reconnaître des têtes connues sur le splash screen de dév

et hop !

Alors, qu'est-ce que ça change ?

- le thème de l'interface s'aligne automatiquement sur les paramètres du système (sombre ou clair)
- on peut choisir des couleurs en CMJN
- peu de plugins sont compatibles et on ne peut pas filtrer dessus donc c'est assez compliqué de savoir
- on peut voter sur un plugin directement depuis l'interface
- on a une sensation de vitesse à l'utilisation mais c'est peut-être lié au fait qu'il n'y a aucun plugin d'installé
- il y a parfois des messages d'erreur
- sur Linux, le support de Wayland

----

## Sur Linux

Comment vous dire...

----

## Sur MacOS

!!! example ""
    Compte-tenu des coûts associés pour l'obtention d'un Mac M4, cette section est réservée aux abonnés premium de Geotribu.

:face_with_hand_over_mouth:

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
