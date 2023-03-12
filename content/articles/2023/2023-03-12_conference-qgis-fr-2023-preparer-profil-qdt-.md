---
title: "Préparez la conférence QGIS FR avec QDT"
subtitle: Venez avec votre meilleur profil
authors:
    - Julien MOURA
categories:
    - article
date: "2023-03-12 18:20"
description: "Afin de suivre au mieux les rencontres 2023 des utilisateurs francophones de QGIS, on vous propose de déployer facilement un profil QGIS avec tout ce qu'il faut dedans pour suivre les ateliers et présentations. Bonne conférence !"
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/conf_qgis_2023_qdt/qgis_ecran_demarrage_conf_qgis_fr_2023.png
license: beerware
robots: index, follow
tags:
    - OSGeo-fr
    - QDT
    - QGIS Deployment Toolbelt
    - QGIS
---

# La conférence QGIS FR approche : préparez votre environnement avec QDT !

:calendar: Date de publication initiale : 12 mars 2023

Prérequis :

- QGIS
- une connexion internet autorisée vers <https://github.com>

## Introduction

![logo conf QGIS FR 2023](https://cdn.geotribu.fr/img/external/salons_conferences/qgis_fr/qgis_journees_francophones_2023_logo.svg){: .img-rdp-news-thumb }

2 modes d'installation et d'utilisation au choix dans cet article :

- [tout au clic sur des interfaces graphiques](#jaime-le-son-du-clic)
- [tout à la ligne de commande](#jaime-le-bruit-des-touches)

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## J'aime le son du clic

![Pour l'amour de la souris](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/conf_qgis_2023_qdt/souris_old_school.gif){: .img-center loading=lazy }

1. [Télécharger l'exécutable de QDT pour votre système d'exploitation depuis la page de documentation](https://guts.github.io/qgis-deployment-cli/usage/installation.html)
1. S'assurer qu'il soit autorisé à s'exécuter
1. Télécharger le fichier du scénario dans le même dossier que l'exécutable
1. Double-cliquer sur l'exécutable

----

## J'aime le bruit des touches

Prérequis complémentaires :

- Python 3.10 ou supérieur - si vous êtes sur Windows, [voir notre article dédié](/articles/2020/2020-06-19_setup_python/)
- une connexion internet autorisée vers <https://pypi.org>

![Pour l'amour du clavier](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/conf_qgis_2023_qdt/clavier_joie.gif){: .img-center loading=lazy }

### Installer

<!-- markdownlint-disable MD046 -->
=== ":fontawesome-brands-linux: Linux et assimilés"

    Exemple sur Ubuntu LTS (22.04 à date) :

    ```sh
    python3 -m pip install --user --upgrade qgis-deployment-toolbelt
    ```

=== ":window: Windows"

    ```powershell
    py -3 -m pip install --user --upgrade qgis-deployment-toolbelt
    ```

### Configurer

<!-- markdownlint-disable MD046 -->
=== ":fontawesome-brands-linux: Linux et assimilés"

    Si QGIS est installé "normalement" avec les paquets officiels ([voir cet article](/articles/2023/2023-01-05_installer-qgis-sur-ubuntu/)) et donc accessible sur `/usr/bin/qgis`, il n'y a rien à faire.  

    Sinon, par exemple dans le cas où plusieurs versions de QGIS sont installées sur la machine, il est possible de spécifier le chemin vers l'exécutable de la version à utiliser :

    ```sh
    export QDT_QGIS_EXE_PATH=/path/to/bin/qgis-custom
    ```

=== ":window: Windows"

    Si QGIS 3.28.4 est installé avec l'installateur officiel sans personnalisation du chemin d'installation (ne pas [voir cet article](/articles/2020/2020-07-03_deploy_qgis_windows/ "Installer QGIS avec PowerShell et l'OSGeo4W")) et donc accessible sur `C:\Program Files\QGIS 3.28.4\bin\qgis-ltr-bin.exe`, il n'y a rien à faire.

    ```powershell
    $env:QDT_QGIS_EXE_PATH="C:\\path\\to\\qgis-ltr-bin.exe"
    ```

### Exécuter

=== ":fontawesome-brands-linux: Linux et assimilés"

    Exemple sur Ubuntu LTS (22.04 à date) :

    ```sh
    qdt --scenario-path https://github.com/geotribu/profils-qgis/raw/main/qdt/scenario.qdt.yml
    ```

=== ":window: Windows"

    ```powershell
    qdt --scenario-path https://github.com/geotribu/profils-qgis/raw/main/qdt/scenario.qdt.yml
    ```

----

## Résulat

![Ecran de démarrage du profil conf QGIS FR 2023](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/conf_qgis_2023_qdt/qgis_ecran_demarrage_conf_qgis_fr_2023.png){: .img-center loading=lazy }

----

## Crédits

- le logo du profil est réalisé par Sylvain Beorchia pour l'OSGeo-FR avec l'accord du projet QGIS
- l'image utilisée pour le splash screen réutilise la montgolfière avec l'accord de son auter (Sylvain Beorchia) et une carte libre de droits de la cartothèque de la BNF

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

{% include "licenses/beerware.md" %}
