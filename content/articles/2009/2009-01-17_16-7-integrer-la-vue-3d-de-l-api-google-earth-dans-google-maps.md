---
title: 7. Intégrer la vue 3D de l'API Google Earth dans Google Maps
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2009-01-17
description: 7. Intégrer la vue 3D de l'API Google Earth dans Google Maps
tags:
    - Google Earth
    - Google Maps
    - 3D
---

# 7. Intégrer la vue 3D de l'API Google Earth dans Google Maps

:calendar: Date de publication initiale : 17 janvier 2009

## Introduction

![logo Google Maps](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google_maps.png "logo Google Maps"){: .img-thumbnail-left}

L'API Google Maps peut se coupler également avec l'API Google Earth Plugin (cf. les [tutoriaux](http://www.geotribu.net/node/23)) en ajoutant un bouton permettant de switcher entre les deux vues 2D et 3D.  

## Ajout de la 3D

`map.addMapType(G_SATELLITE_3D_MAP);`  

## Code complet

```html
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>
     [Google Maps / Google Earth] 16 /|> 7. Intégrer la vue 3D de l'API Google Earth dans Google Maps
    </title>
    <style type="text/css">
      html { overflow:hidden; height:100%; }
      body { height:100%; margin:0; }
      #map { width:100%; height:100%; }
    </style>
    <link rel="icon" type="image/png" href="./favicon.png"/>
    <script src="http://maps.google.com/maps?file=api&v=2&key=votre_cle_ici" type="text/javascript"></script>
    <script type="text/javascript">

      function initialize() {

        var map = new GMap2(document.getElementById("map"));
        map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),15);
        map.addControl(new GMapTypeControl());
        map.removeMapType(G_HYBRID_MAP);
        map.removeMapType(G_SATELLITE_MAP);
        map.addMapType(G_PHYSICAL_MAP);

        map.addMapType(G_SATELLITE_3D_MAP);

}

    </script>
  </head>
  <body onload="initialize()" onunload="GUnload()">
    <div id="map"></div>
  </body>
</html>
```

## Démonstration

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto16.html" height="500px" width="500px"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto16.html)

## Remarques

Toujours se référer à l'API Google Maps - [Google Maps API Reference](http://code.google.com/apis/maps/documentation/reference.html) pour les différentes classes, méthodes et options utilisées.
Lorsque l'on fait une recherche grâce à cette GoogleBar, l'API place automatiquement un marqueur géocodé sur la carte.

## Conclusion

Petit tutoriel pour intégrer la vue 3D fournie par l'API Google Earth dans une carte Google Maps.
Rien de bien compliqué ici.

----

<!-- geotribu:authors-block -->
