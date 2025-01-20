---
title: "GeoExt en version 0.6"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-10-16
description: "GeoExt en version 0.6"
tags:
    - GeoExt
    - JavaScript
    - open source
---

# GeoExt en version 0.6

:calendar: Date de publication initiale : 16 octobre 2009

![logo GeoExt](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/geoext.png "logo GeoExt"){: .img-thumbnail-left }

Ca y'est, la [version 0.6](http://geoext.blogspot.com/2009/10/geoext-06-released.html) de [GeoExt](http://geoext.blogspot.com/) est officiellement sortie. Cette dernière conclue 4 mois de travail qui ont permis la fermeture de 51 tickets dont 34 apportant de nouvelles fonctionnalités.

Pour rappel, GeoExt est une librairie cartographique, écrite en javascript (JS), permettant de réaliser rapidement et efficacement des interfaces web cartographiques intuitives. Pour cela elle s'appuie sur deux librairies JS, GeoExt pour la partie Interface Homme Machine et OpenLayers pour la cartographie.

Les améliorations portent notamment sur :

* l'ajout de [LayerParamNode](http://dev.geoext.org/trunk/geoext/examples/tree.html) permettant de configurer l'arbre des couches afin qu'il affiche un noeud pour chaque couche listée dans une requête WMS
* l'ajout de [FeatureSelectionModel](http://dev.geoext.org/trunk/geoext/examples/feature-grid.html) qui gère l'interaction entre le tableau de données et les couches affichées lors d'une sélection
* Un [nouveau slider](http://dev.geoext.org/trunk/geoext/examples/layeropacityslider.html) pour ajuster la transparence des couches
* Le widget LayerContainer a subi de nombreuses modifications afin d'améliorer la gestion du drag and drop et offrir plus de souplesse quant à la configuration des couches
* Dans l'arbre des couches, il est dorénavant possible d'utiliser des boutons radios plutôt que des checkbox
* De nombreuses améliorations ont été apportées au widget [LegendPanel](http://dev.geoext.org/trunk/geoext/examples/legendpanel.html). Avec par exemple la prise en compte des changements de symbologie d'une couche ou encore l'ajout d'un filtre pour limiter les couches affichées ...
* Les popups peuvent maintenant être déplacés en dehors du viewport
* ...

Cette nouvelle version est d'ores et déjà [librement téléchargeable](http://geoext.org/downloads.html) tout en sachant qu'elle ne devrait poser aucun problème de compatibilité ascendante.

----

<!-- geotribu:authors-block -->
