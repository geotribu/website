---
title: "GeoExt en version 0.5"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-06-24
description: "GeoExt en version 0.5"
tags:
    - GeoExt
    - JavaScript
    - open source
---

# GeoExt en version 0.5

:calendar: Date de publication initiale : 24 juin 2009

![logo GeoExt](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/geoext.png "logo GeoExt"){: .img-thumbnail-left }

Décidément, cela bouge dans le petit monde du GeoWeb. Après la sortie d'[OpenLayers en version 2.8](http://geotribu.net/node/129) c'est au tour de [GeoExt](http://www.geoext.org/) de nous offrir une nouvelle release. Quelques bugs ont été corrigés mais c'est surtout plus d'une quarantaine de nouvelles fonctionnalités qui ont été ajoutées. Une liste complète des modifications est disponible sur la page des [notes de version](http://www.geoext.org/trac/geoext/wiki/Release/0.5/Notes).

Cette librairie dispose globalement de deux grandes classes. L'une nommée **data**, l'autre **widget**. La première est chargée de formater les données et flux dans un format utilisable par Ext. La seconde est la partie visuelle de GeoExt, c'est à partir de celle-ci que nous allons construire notre interface. Un exemple des widgets disponibles ?

* [MapPanel](http://dev.geoext.org/trunk/geoext/examples/mappanel-window.html) : C'est l'un des widgets essentiels de GeoExt. Il créé une fenêtre qui contient la carte d'OpenLayers
* [FeatureGrid](http://dev.geoext.org/trunk/geoext/examples/feature-grid.html) : Affiche dans un tableau les données provenant d'une couche vecteur (GML, KML...)
* [PopUp](http://dev.geoext.org/trunk/geoext/examples/popup.html) : Affiche un Popup
* [ZoomChooser](http://dev.geoext.org/trunk/geoext/examples/zoom-chooser.html) : Liste déroulante permettant de définir l'échelle souhaitée
* [ZoomSlider](http://dev.geoext.org/trunk/geoext/examples/zoomslider.html) : Remplace l'outil de zoom habituel par un nouveau contrôle permettant par exemple d'afficher des infobulles en fonction du niveau de zoom
* [LegendWMS](http://dev.geoext.org/trunk/geoext/examples/legendpanel.html) : Construit une légende en fonction des couches WMS affichées

Ces nouvelles versions sont une preuve supplémentaire de la maturité du monde de l'OpenSource GeoWeb. GeoExt permet réellement d'imaginer la mise en place de RIA et ainsi de réaliser de véritables outils. Vivement que je puisse libérer un peu de temps pour tester ces nouvelles fonctionnalités.

----

<!-- geotribu:authors-block -->
