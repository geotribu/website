---
title: QTribu, le plugin QGIS inutile donc forcément indispensable
authors:
    - Julien MOURA
categories:
    - article
comments: true
date: 2021-04-01
description: "Présentation du plugin de Geotribu pour QGIS : QTribu. Inutile donc forcément indispensable."
icon: material/puzzle-heart-outline
image: https://cdn.geotribu.fr/img/projets-geotribu/plugin_qtribu/qtribu_article_displayed.png
license: default
tags:
    - plugin
    - Geotribu
    - QGIS
    - QTribu
---

# QTribu, le plugin Geotribu pour QGIS

:calendar: Date de publication initiale : 1er avril 2021

## Un plugin sérieux pour ne pas se prendre au sérieux

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-thumbnail-left }

Au détour d'un travail sur la négociation de contenu pour un plugin QGIS dans le cadre de mes fonctions à [Oslandia](https://oslandia.com/fr/), je me suis dit :

- Tiens, et si c'était possible de lire un flux RSS dans QGIS, on pourrait faire un plugin pour Geotribu ?
- Mais pourquoi faire ?
- Pourquoi pas ?

Et voilà ! :smile:

Pour l'instant, le plugin permet de consulter Geotribu sans quitter QGIS. D'autres fonctionnalités arriveront probablement par la suite.

![QTribu - Dernier article dans le navigateur intégré de QGIS](https://cdn.geotribu.fr/img/projets-geotribu/plugin_qtribu/qtribu_article_displayed.png "QTribu - Dernier article dans le navigateur intégré de QGIS"){: .img-center loading=lazy }

C'est surtout un projet "modèle" dont je me sers pour tester ou donner un exemple concret de ce que je considère comme étant de bonnes pratiques et que je présente en partie sur ce site : le [raccourci vers l'aide en ligne](2021-03-09_pyqgis_astuce_aide_plugin.md), l'utilisation des [icônes intégrées de QGIS](2021-01-19_pyqgis_utiliser_icones_integrees.md), l'intégration des options du plugin dans le menu des préférences de QGIS, la gestion centralisée des logs et messages à l'utilisateur/ice final/e, etc.

[Documentation du plugin :fontawesome-solid-book:](https://geotribu.github.io/qtribu/){: .md-button }
[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Installer le plugin

![QGIS icône plugins](https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/propertyicons/plugins.svg "QGIS icône plugins"){: .img-thumbnail-left }

!!!note
    Compte-tenu du périmètre fonctionnel particulier de ce plugin et pour ne pas ajouter du bruit supplémentaire au dépôt officiel des extensions de QGIS, QTribu est uniquement disponible en ajoutant un dépôt personnalisé.

1. Menu `Extensions` > `Installer/Gérer des extensions`
2. Onglet `Paramètres`
3. Sous la liste des dépôts, cliquer sur `Ajouter...` et renseigner :
    - Nom : QTribu
    - URL : `https://github.com/geotribu/qtribu/releases/latest/download/plugins.xml`

    ![QTribu - Dépôt](https://cdn.geotribu.fr/img/tuto/qgis_plugins_repository/qgis_plugins_repository_qtribu.png "QTribu - Dépôt"){: loading=lazy }

4. Une fois le dépôt ajouté, l'extension devrait apparaître dans l'onglet `Non installées`. Cliquer sur `Installer` :

    ![QTribu - Non installée](https://cdn.geotribu.fr/img/tuto/qgis_plugins_repository/qgis_plugins_available_qtribu.png "QTribu - Non installée"){: loading=lazy }

!!!warning
    Selon votre configuration, redémarrer QGIS peut être nécessaire, le gestionnaire d'extensions ayant des comportement parfois capricieux par rapport aux dépôts tiers.

----

## Intégration dans QGIS

Une fois installé, le plugin s'intègre :

- dans le menu `Internet` :

![Menu QTribu](https://cdn.geotribu.fr/img/projets-geotribu/plugin_qtribu/qtribu_menu_plugin.png "Menu QTribu"){: loading=lazy }
{: align=middle }

- dans la barre d'outils sous forme d'une simple icône :

![Toolbar QTribu](https://cdn.geotribu.fr/img/projets-geotribu/plugin_qtribu/qtribu_toolbar.png "Toolbar QTribu"){: loading=lazy }
{: align=middle }

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
