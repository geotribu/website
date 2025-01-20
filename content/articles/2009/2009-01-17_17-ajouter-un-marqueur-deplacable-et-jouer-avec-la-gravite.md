---
title: 17. Ajouter un marqueur déplaçable et jouer avec la gravité
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2009-01-17
description: 17. Ajouter un marqueur déplaçable et jouer avec la gravité
tags:
    - Google Maps
    - marqueur
---

# 17. Ajouter un marqueur déplaçable et jouer avec la gravité

:calendar: Date de publication initiale : 17 janvier 2009

## Introduction

![logo Google Maps](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google_maps.png "logo Google Maps"){: .img-thumbnail-left}

Il est possible grâce à l'API Google Maps de créer des marqueurs déplaçables. Nous verrons ici comment l'implémenter.  

## Ajout des marqueurs

Définir une fonction de création des marqueurs - en définissant les options clickable, draggable, bouncy, bouncyGravity et title, et en ajoutant nu événement lors de la fin du déplacement du marqueur :  

```javascript
function createMarker(point){
  marker = new GMarker(point,{clickable: false, draggable: true, bouncy: true, bounceGravity: 0.2, title: 'marqueur déplaçable'});
  map.addOverlay(marker);
  GEvent.addListener(marker, "dragend", function() {
    marker.openInfoWindowHtml("Il est possible de modifier la gravité du rebond !");
  });
}
```  

Créer un événement lorsqu'on clique sur la carte - ici on ajoute un marqueur :  

```javascript
GEvent.addListener(map,"click", function(overlay,latlng){
  if (latlng){
    var point = new GLatLng(latlng.y,latlng.x);
    createMarker(point);
  }
});
```  

## Code complet

```html
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>
      [Google Maps] 17. Ajouter un marqueur déplaçable et jouer avec la gravité
    </title>
    <style type="text/css">
      html { overflow:hidden; height:100%; }
      body { height:100%; margin:0; }
      #map { width:100%; height:100%; }
    </style>
    <link rel="icon" type="image/png" href="./favicon.png"/>
    <script src="http://maps.google.com/maps?file=api&v=2&key=votre_cle_ici" type="text/javascript"></script>
    <script type="text/javascript">

      var map;
      var marker;
      var latlng;

      function createMarker(point){
        marker = new GMarker(point,{clickable: false, draggable: true, bouncy: true, bounceGravity: 0.2, title: 'marqueur déplaçable'});
        map.addOverlay(marker);
        GEvent.addListener(marker, "dragend", function() {
          marker.openInfoWindowHtml("Il est possible de modifier la gravité du rebond !");
        });
      }

      function initialize() {

        map = new GMap2(document.getElementById("map"));
        map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),15);
        map.addControl(new GSmallMapControl());
        map.addControl(new GMapTypeControl());

        GEvent.addListener(map,"click", function(overlay,latlng){
          if (latlng){
            var point = new GLatLng(latlng.y,latlng.x);
            createMarker(point);
          }
        });

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
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto17.html" height="500px" width="500px"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto17.html)

## Remarques

Toujours se référer à l'API Google Maps - [Google Maps API Reference](http://code.google.com/apis/maps/documentation/reference.html) pour les différentes classes, méthodes et options utilisées.
Il existe beaucoup d'événements sur les objets - carte et marqueur - dans l'API Google Maps, à vous de les découvrir.

## Conclusion

- Ce tutoriel explique comment ajouter un marqueur sur la carte à la position où l'on clique.
- Il explique aussi comment faire pour que ce marqueur soit déplaçable.
- On peut imaginer des interactions avec une base de données pour enregistrer les marqueurs et beaucoup d'autres choses encore.

----

<!-- geotribu:authors-block -->
