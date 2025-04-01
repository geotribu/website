---
title: 'PyQGIS Resource Browser : un plugin pour parcourir les icônes de QGIS'
authors:
    - Julien MOURA
categories:
    - article
comments: true
date: 2023-04-23
description: 'Après le tutoriel et le site, voici le plugin QGIS : PyQGIS Resource Browser ! Idéal pour parcourir les icônes et copier la syntaxe d''intégration.'
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/pyqgis_resources_browser/plugin_pyqgis_resource_browser.png
license: beerware
robots: index, follow
tags:
    - icônes
    - interface graphique
    - plugin
    - PyQGIS
    - PyQt5
    - QGIS
---

# PyQGIS Resource Browser : un plugin pour parcourir les icônes de QGIS

:calendar: Date de publication initiale : 23 avril 2023

![logo PyQGIS](https://cdn.geotribu.fr/img/logos-icones/programmation/pyqgis.png){: .img-thumbnail-left }

Le mois dernier, je [publicisais ici un site permettant de lister les ressources graphiques présentes dans QGIS](2023-03-24_pyqgis-icones-cheatsheet-automatisation.md) et réutilisables dans le développement de plugins, comme démontré dans [ce tutoriel de 2021](../2021/2021-01-19_pyqgis_utiliser_icones_integrees.md).

Je disais avoir été contacté par Benjamin Jakimow et avoir proposé de mutualiser nos forces pour faire un plugin dédié :

> Je lui ai donc proposé mon aide pour en faire un plugin dédié indépendant. À suivre !

Eh bien, grâce principalement au travail de Benjamin, voilà, c'est chose faite :

![PyQGIS Resource Browser](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/pyqgis_resources_browser/plugin_pyqgis_resource_browser.png){: .img-center loading=lazy }

Côté fonctionnement, le plugin consiste en une fenêtre qui permet de parcourir, rechercher et filtrer les images listées dans les différents fichiers de ressources. On peut personnaliser les fichiers à afficher, prévisualiser les images ou la version texte quand il s'agit de SVG et copier/coller la syntaxe d'intégration (getThemeIcon, QIcon ou QPixmap) via le menu contextuel du clic droit.

![PyQGIS Resource Browser - Menu contextuel](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/pyqgis_resources_browser/context_menu.webp){: .img-center loading=lazy }

[Dépôt officiel :simple-qgis:](https://plugins.qgis.org/plugins/pyqgis_resource_browser/){: .md-button }
[Code :fontawesome-solid-code:](https://github.com/Guts/qgis-plugin-resource-browser/){: .md-button }
{: align=middle }

C'est beau l'open source et le travail communautaire, n'est-il pas ?

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
