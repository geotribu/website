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
- une connexion internet autorisée vers pypi.org et github.com

## Introduction

2 modes d'installation et d'utilisation au choix détaillés dans cet article :

- tout au clic sur des interfaces graphiques
- tout à la ligne de commande


[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## J'aime le son du clic

![Pour l'amour de la souris](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/conf_qgis_2023_qdt/souris_old_school.gif){: .img-center loading=lazy }




----

## J'aime le bruit des touches

Prérequis complémentaires :

- Python 3.10 ou supérieur - si vous êtes sur Windows, [voir notre article dédié](/articles/2020/2020-06-19_setup_python/)

![Pour l'amour du clavier](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/conf_qgis_2023_qdt/clavier_joie.gif){: .img-center loading=lazy }

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

### Exécuter

=== ":fontawesome-brands-linux: Linux"

    Exemple sur Ubuntu LTS (22.04 à date) :

    ```sh
    qdt --scenario-path https://gitlab.com/Oslandia/qgis/profils_qgis_fr_2022/-/raw/main/qdt_scenarii/scenario.qdt.yml
    ```

=== ":window: Windows"

    ```powershell
    qdt --scenario-path https://gitlab.com/Oslandia/qgis/profils_qgis_fr_2022/-/raw/main/qdt_scenarii/scenario.qdt.yml
    ```

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

{% include "licenses/beerware.md" %}
