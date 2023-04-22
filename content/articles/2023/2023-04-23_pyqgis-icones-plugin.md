---
title: "PyQGIS Resource Browser : un plugin pour parcourir les icônes de QGIS"
subtitle: "Et tout totomatique svp !"
authors:
    - Julien MOURA
categories:
    - article
date: "2023-04-23 18:20"
description: "Pour faciliter le travail d'intégration des icônes de QGIS par les développeurs de plugins, j'ai automatisé la génération et la mise à jour d'un site web : PyQGIS Icons Cheatsheet."
mage: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/pyqgis_resources_browser/plugin_pyqgis_resource_browser.png
license: beerware index, f
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

![logo PyQGIS](https://cdn.geotribu.fr/img/logos-icones/programmation/pyqgis.png){: .img-rdp-news-thumb }

Le mois dernier, je [publicisais ici un site permettant de lister les ressources graphiques présentes dans QGIS](/articles/2023/2023-03-24_pyqgis-icones-cheatsheet-automatisation/) et réutilisables dans le développement de plugins, comme démontré dans [ce tutoriel de 2021](/articles/2021/2021-01-19_pyqgis_utiliser_icones_integrees/).

Je disai avoir été contacté par Benjamin Jakimow et avoir proposé de mutualiser nos forces pour faire un plugin dédié :

> Je lui ai donc proposé mon aide pour en faire un plugin dédié indépendant. À suivre !

Eh bien, voilà, c'est chose faite :

![PyQGIS Icons Cheatsheet](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/pyqgis_resources_browser/plugin_pyqgis_resource_browser.png){: .img-center loading=lazy }

[Sur le dépôt officiel :fontawesome-solid-comments:](https://plugins.qgis.org/plugins/pyqgis_resource_browser/){: .md-button }
[Code :fontawesome-solid-comments:](https://github.com/Guts/qgis-plugin-resource-browser/){: .md-button }
{: align=middle }

C'est beau l'open source et le travail communautaire, n'est-il pas ?

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

{% include "licenses/beerware.md" %}
