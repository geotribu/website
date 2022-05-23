---
title: "13. Ajouter la couche StreetView"
authors:
    - Fabien Goblet
categories:
    - article
date: 2008-11-17 10:20
description: "13. Ajouter la couche StreetView"
image: ''
license: default
robots: index, follow
tags:
    - Google Maps
    - Street View
---

# 13. Ajouter la couche StreetView

:calendar: Date de publication initiale : 17 novembre 2008

----

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-rdp-news-thumb }

L'API Google Maps propose le service Street View qui permet de naviguer virtuellement dans les rues. Avant de voir comment faire dans le prochain tutoriel, nous allons voir ici quelle est l'emprise des images.  

## Initialisation

Reprendre la carte du [tutoriel n°2](/articles/2008/art_2008-08-22_2-enrichir-la-carte-avec-des-boutons-et-des-controles/).  

## Superposition de l'emprise

Construire un overlay de type StreetView :

`var svOverlay = new GStreetviewOverlay();`  

L'ajouter à la carte :

`map.addOverlay(svOverlay);`  

## Code complet

```html
<script type="text/javascript">

var map = null;

function initialize() {
  if (GBrowserIsCompatible()) {
    var map = new GMap2(document.getElementById('map'));
    map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),15);
    map.addControl(new GMapTypeControl());
    map.removeMapType(G\_HYBRID\_MAP);
    map.addMapType(G\_PHYSICAL\_MAP);
    map.setMapType(G\_PHYSICAL\_MAP);
    map.addControl(new GOverviewMapControl());
    map.addControl(new GScaleControl());
    map.addControl(new GLargeMapControl());
    map.enableScrollWheelZoom();
    var svOverlay = new GStreetviewOverlay();
    map.addOverlay(svOverlay);

  }
  else{
    alert('Désolé, mais votre navigateur n\'est pas compatible avec Google Maps');
  }
}
</script>
```

## Démonstration

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto13.html" height="350px" width="100%"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto13.html)

## Remarques

Toujours se référer à l'API Google Maps - [Google Maps API Reference](http://code.google.com/apis/maps/documentation/reference.html) pour les différentes classes, méthodes et options utilisées.
Les photos StreetView ne sont pas disponibles partout sur la Terre.

## Conclusion

Les méthodes relatives à StreetView commencent ici : [http://code.google.com/apis/maps/documentation/reference.html#GStreetviewPanorama](http://code.google.com/apis/maps/documentation/reference.html#GStreetviewPanorama).

----

## Auteur {: data-search-exclude }

--8<-- "content/team/fgob.md"
