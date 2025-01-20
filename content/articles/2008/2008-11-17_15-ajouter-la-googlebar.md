---
title: 15. Ajouter la GoogleBar
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-11-17
description: 15. Ajouter la GoogleBar
image: ''
tags:
    - Google Maps
    - Google Bar
---

# 15. Ajouter la GoogleBar

:calendar: Date de publication initiale : 17 novembre 2008

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-thumbnail-left }

L'API Google Maps permet de définir une barre de géolocalisation et d'afficher le résultat sur la carte.  

## Ajout de la Google Bar

```javascript
map.enableGoogleBar();
```

## Code complet

```html
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>
     [Google Maps] 15. Ajouter la GoogleBar
   </title>
   <style type="text/css">
     html { overflow:hidden; height:100%; }
     body { height:100%; margin:0; }
     #map { width:100%; height:100%; }
   </style>
   <link rel="icon" type="image/png" href="./favicon.png"/>
   <script src="http://maps.google.com/maps?file=api&v=2&key=votre_clé_ici" type="text/javascript"></script>
   <script type="text/javascript">

     var map = null;

     function initialize() {
       if (GBrowserIsCompatible()) {
       map = new GMap2(document.getElementById('map'));
       map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),15);
       map.addControl(new GMapTypeControl());
       map.removeMapType(G_HYBRID_MAP);
       map.addMapType(G_PHYSICAL_MAP);
       map.setMapType(G_PHYSICAL_MAP);
       map.addControl(new GOverviewMapControl());
       map.addControl(new GScaleControl());
       map.addControl(new GLargeMapControl());
       map.enableScrollWheelZoom();

       map.enableGoogleBar();

      }
      else{
       alert('Désolé, mais votre navigateur n\'est pas compatible avec Google Maps');
      }
    }
  </script>
  </head>
  <body onload="initialize()" onunload="GUnload()">
    <div id="map"></div>
   </body>
</html>
```  

### Démonstration

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto15.html" height="350px" width="100%"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto15.html)

## Remarques

Toujours se référer à l'API Google Maps - [Google Maps API Reference](http://code.google.com/apis/maps/documentation/reference.html) pour les différentes classes, méthodes et options utilisées.
Lorsque l'on fait une recherche grâce à cette GoogleBar, l'API place automatiquement un marqueur géocodé sur la carte.

## Conclusion

Petit tutorial pour savoir déclarer le service GoogleBar.
Cette méthode est identique au tutoriel - [11](2008-09-07_11-geocoder-une-adresse.md).

----

<!-- geotribu:authors-block -->
