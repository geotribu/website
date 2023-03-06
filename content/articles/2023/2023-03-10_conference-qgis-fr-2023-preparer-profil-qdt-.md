---
title: "Préparez la conférence QGIS FR avec le profil QGIS"
authors:
    - Julien MOURA
categories:
    - article
date: "2023-03-10 10:20"
description: "Description pour le SEO."
image: "Image d'illustration de l'article qui sert ensuite dans la mise en avant : réseaux sociaux, flux RSS..."
license: beerware
robots: index, follow
tags:
    - OSGeo FR
    - QDT
    - QGIS Deployment Toolbelt
    - QGIS
---

# La conférence QGIS FR approche : préparez votre environnement avec QDT !

:calendar: Date de publication initiale : 10 mars 2023

Prérequis :

- QGIS
- une connexion internet autorisée vers pypi.org et gitlab.com

## Introduction

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## J'aime le son du clic

----

## J'aime le bruit des touches

Prérequis :

- Python 3.10 ou supérieur

### Installer

<!-- markdownlint-disable MD046 -->
=== ":fontawesome-brands-linux: Linux"

    Exemple sur Ubuntu LTS (22.04 à date) :

    ```sh
    python3 -m pip install --user --upgrade qgis-deployment-toolbelt
    ```

=== ":window: Windows"

    ```powershell
    py -3 -m pip install --user --upgrade qgis-deployment-toolbelt
    ```

<!-- markdownlint-enable MD046 -->

### Exécuter

```sh
qdt --scenario-path https://gitlab.com/Oslandia/qgis/profils_qgis_fr_2022/-/raw/main/qdt_scenarii/scenario.qdt.yml
```

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

{% include "licenses/beerware.md" %}
