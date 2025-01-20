---
title: "L'API du GéoPortail passe en version 1.0"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-03-17
description: "L'API du GéoPortail passe en version 1.0"
tags:
    - API
    - JavaScript
    - webmapping
---

# L'API du GéoPortail passe en version 1.0

:calendar: Date de publication initiale : 17 mars 2010

![logo IGN](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/ign_old.png "logo IGN"){: .img-thumbnail-left }

L'API cartographique de l'Institut Géographique National (IGN) passe du statut de bêta au statut de release officielle. La version 1.0 a en effet été [annoncée](https://api.ign.fr/geoportail/document.do?doc=6133116) aujourd'hui (16 Mars 2010).

De nouvelles fonctionnalités ont été apportées avec notamment :

- un moteur de recherche par adresse et par lieu-dit
- une visualisation facilitée des traces GPX ou des fichiers KML
- une couverture étendue hors de nos frontières, grâce à une compatibilité accrue avec d’autres données (OpenStreetMap, …) (YES ! ^^)

Afin de fournir une meilleure compatibilité avec OpenLayers un travail de réecriture du code à également été réalisé permettant ainsi une plus grande souplesse d'utilisation. En effet, la classe Geoportal.Map est devenue une sous-classe de OpenLayers.Map. De plus, si vous le souhaitez, vous pouvez simplement importer les éléments essentiels de la librairie (includeEngine=false) afin de construire votre application personnalisée.

Vous trouverez tous les renseignements nécessaires en consultant [l'annonce officielle](https://api.ign.fr/geoportail/document.do?doc=6133116). Après quelques tests de cette nouvelle API, vous devriez probablement voir sur GéoTribu de nouveaux tutoriels orientés IGN.

----

<!-- geotribu:authors-block -->
