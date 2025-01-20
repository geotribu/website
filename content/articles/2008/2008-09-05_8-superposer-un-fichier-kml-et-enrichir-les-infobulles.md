---
title: 8. Superposer un fichier KML et enrichir les infobulles
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-09-05
description: 8. Superposer un fichier KML et enrichir les infobulles
tags:
    - Google Maps
    - infobulle
    - KML
---

# 8. Superposer un fichier KML et enrichir les infobulles

:calendar: Date de publication initiale : 05 septembre 2008

:warning: L'API Google Maps v2 est dépréciée depuis le 19 mai 2010.

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-thumbnail-left }

L'API Google Maps permet de superposer des fichiers KML sur une carte. Et d'afficher une mini-carte dans une infobulle (ce qui n'a rien à voir avec l'affichage du KML mais qui peut être intéressant).

## Initialisation

Reprendre la carte du [deuxième tutoriel](2008-08-22_2-enrichir-la-carte-avec-des-boutons-et-des-controles.md).

## Appel d'un fichier KML et affichage sur la carte

L'appel à un fichier KML (dans le cas présent un fichier KML bien connu des [SIGMA](http://sigma.ensat.fr)-iens (-ieux, -iois, au choix)) se fait grâce à la classe GGeoXml :  `var kml = new GGeoXml("http://88.191.39.115/fabien/geotribu/kml/route.kml");` Et l'affichage grâce à la méthode addOverlay() déjà utilisée précédemment :  `map.addOverlay(kml);`

## Mini-carte dans une infobulle

Créons tout d'abord un marqueur et ajoutons-le à la carte :  `var marker1 = new GMarker(new GLatLng(43.57769664771851, 1.402821992034912)); map.addOverlay(marker1);`  Puis gérons l'événement lors d'un clic sur celui-ci :  `GEvent.addListener(marker1, 'click', function() { marker1.showMapBlowup({zoomLevel:18,mapType:G_SATELLITE_MAP}); });`

## Code complet

```html
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>
     [Google Maps] 8. Superposer un fichier .kml et enrichir les info-bulles
   </title>
   <style type="text/css">
     html { overflow:hidden; height:100%; }
     body { height:100%; margin:0; }
     #map { width:100%; height:100%; }
   </style>
   <link rel="icon" type="image/png" href="./favicon.png"/>
   <script src="http://maps.google.com/maps?file=api&v=2.x&key=votre_clé_ici" type="text/javascript"></script>
   <script type="text/javascript">

     function initialize() {
       if (GBrowserIsCompatible()) {
       var map = new GMap2(document.getElementById('map'));

       function ZoomControl() {}
         ZoomControl.prototype = new GControl();
         ZoomControl.prototype.initialize = function(map) {
         var container = document.createElement("div");

         var zoomInDiv = document.createElement("div");
         this.setButtonStyle_(zoomInDiv);
         container.appendChild(zoomInDiv);
         zoomInDiv.appendChild(document.createTextNode("Zoom In"));
         zoomInDiv.innerHTML = '<img src="./icons/32x32/1.png">';
         GEvent.addDomListener(zoomInDiv, "click", function() {
           map.zoomIn();
         });

         var zoomOutDiv = document.createElement("div");
         this.setButtonStyle_(zoomOutDiv);
         container.appendChild(zoomOutDiv);
         zoomOutDiv.innerHTML = '<img src="./icons/32x32/2.png">';
         GEvent.addDomListener(zoomOutDiv, "click", function() {
           map.zoomOut();
         });

         map.getContainer().appendChild(container);
         return container;
       }

       ZoomControl.prototype.getDefaultPosition = function() {
         return new GControlPosition(G_ANCHOR_TOP_LEFT, new GSize(5, 5));
       }

       ZoomControl.prototype.setButtonStyle_ = function(button) {
         button.style.cursor = "pointer";
       }

       function PanUpControl() {}
         PanUpControl.prototype = new GControl();
         PanUpControl.prototype.initialize = function(map) {
         var container = document.createElement("div");

         var panUp = document.createElement("div");
         this.setButtonStyle_(panUp);
         container.appendChild(panUp);
         panUp.innerHTML = '<img src="./icons/32x32/9.png">';
         GEvent.addDomListener(panUp, "click", function() {
           map.panDirection(0,1);
         });

         map.getContainer().appendChild(container);
        return container;
       }

       PanUpControl.prototype.getDefaultPosition = function() {
         return new GControlPosition(G_ANCHOR_TOP_RIGHT, new GSize(map.getSize().width/2-16, 0));
       }

       PanUpControl.prototype.setButtonStyle_ = function(button) {
         button.style.cursor = "pointer";
       }

       function PanDownControl() {}
       PanDownControl.prototype = new GControl();
       PanDownControl.prototype.initialize = function(map) {
         var container = document.createElement("div");

         var panDown = document.createElement("div");
         this.setButtonStyle_(panDown);
         container.appendChild(panDown);
         panDown.innerHTML = '<img src="./icons/32x32/10.png">';
         GEvent.addDomListener(panDown, "click", function() {
           map.panDirection(0,-1);
         });

         map.getContainer().appendChild(container);
         return container;
       }

       PanDownControl.prototype.getDefaultPosition = function() {
         return new GControlPosition(G_ANCHOR_BOTTOM_RIGHT, new GSize(map.getSize().width/2-16, 0));
       }

       PanDownControl.prototype.setButtonStyle_ = function(button) {
         button.style.cursor = "pointer";
       }

       function PanRightControl() {}
       PanRightControl.prototype = new GControl();
       PanRightControl.prototype.initialize = function(map) {
         var container = document.createElement("div");

         var panRight = document.createElement("div");
         this.setButtonStyle_(panRight);
         container.appendChild(panRight);
         panRight.innerHTML = '<img src="./icons/32x32/7.png">';
         GEvent.addDomListener(panRight, "click", function() {
           map.panDirection(-1,0);
         });

         map.getContainer().appendChild(container);
         return container;
       }

       PanRightControl.prototype.getDefaultPosition = function() {
         return new GControlPosition(G_ANCHOR_TOP_RIGHT, new GSize(0, map.getSize().height/2-16));
       }

       PanRightControl.prototype.setButtonStyle_ = function(button) {
         button.style.cursor = "pointer";
       }

       function PanLeftControl() {}
         PanLeftControl.prototype = new GControl();
         PanLeftControl.prototype.initialize = function(map) {
         var container = document.createElement("div");

         var panLeft = document.createElement("div");
         this.setButtonStyle_(panLeft);
         container.appendChild(panLeft);
         panLeft.innerHTML = '<img src="./icons/32x32/8.png">';
         GEvent.addDomListener(panLeft, "click", function() {
           map.panDirection(1,0);
         });

         map.getContainer().appendChild(container);
         return container;
       }

       PanLeftControl.prototype.getDefaultPosition = function() {
         return new GControlPosition(G_ANCHOR_TOP_LEFT, new GSize(0, map.getSize().height/2-16));
       }

       PanLeftControl.prototype.setButtonStyle_ = function(button) {
         button.style.cursor = "pointer";
       }

       function CustomMapControl() {}
       CustomMapControl.prototype = new GControl();
       CustomMapControl.prototype.initialize = function(map) {
         var container = document.createElement("div");

         var CustomMapPlan = document.createElement("div");
         this.setButtonStyle_(CustomMapPlan);
         container.appendChild(CustomMapPlan);
         CustomMapPlan.innerHTML = '<img src="./buttons/plan_orange_75.png">';
         GEvent.addDomListener(CustomMapPlan, "click", function() {
           map.setMapType(G_NORMAL_MAP);
         });

         var CustomMapSatellite = document.createElement("div");
         this.setButtonStyle_(CustomMapSatellite);
         container.appendChild(CustomMapSatellite);
         CustomMapSatellite.innerHTML = '<img src="./buttons/satellite_orange_75.png">';
         GEvent.addDomListener(CustomMapSatellite, "click", function() {
           map.setMapType(G_SATELLITE_MAP);
         });

         var CustomMapRelief = document.createElement("div");
         this.setButtonStyle_(CustomMapRelief);
         container.appendChild(CustomMapRelief);
         CustomMapRelief.innerHTML = '<img src="./buttons/relief_orange_75.png">';
         GEvent.addDomListener(CustomMapRelief, "click", function() {
           map.setMapType(G_PHYSICAL_MAP);
         });

         map.getContainer().appendChild(container);
         return container;
       }

       CustomMapControl.prototype.getDefaultPosition = function() {
         return new GControlPosition(G_ANCHOR_TOP_RIGHT, new GSize(15, 15));
       }

       CustomMapControl.prototype.setButtonStyle_ = function(button) {
         button.style.marginBottom = "8px";
         button.style.cursor = "pointer";
       }

       function LogoControl() {}
       LogoControl.prototype = new GControl();
       LogoControl.prototype.initialize = function(map) {
       var container = document.createElement("div");

       var Logo = document.createElement("div");
       container.appendChild(Logo);
       Logo.innerHTML = '<img src="./logos/logo_geotribu.png">';

       map.getContainer().appendChild(container);
         return container;
       }

       LogoControl.prototype.getDefaultPosition = function() {
         return new GControlPosition(G_ANCHOR_BOTTOM_LEFT, new GSize(map.getSize().width/7, 0));
       }

       map.addControl(new ZoomControl());
       map.addControl(new PanUpControl());
       map.addControl(new PanDownControl());
       map.addControl(new PanRightControl());
       map.addControl(new PanLeftControl());
       map.addControl(new CustomMapControl());
       map.addControl(new LogoControl());
       map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),13);
       map.enableScrollWheelZoom();
       map.enableContinuousZoom();

       var kml = new GGeoXml("http://88.191.39.115/fabien/geotribu/kml/route.kml");
       map.addOverlay(kml);

       var marker1 = new GMarker(new GLatLng(43.57769664771851, 1.402821992034912));
       map.addOverlay(marker1);
       GEvent.addListener(marker1, 'click', function() {
         marker1.showMapBlowup({zoomLevel:18,mapType:G_SATELLITE_MAP});
       });

       var marker2 = new GMarker(new GLatLng(43.53507914503071, 1.493223511978854));
       map.addOverlay(marker2);
       GEvent.addListener(marker2, 'click', function() {
         marker2.showMapBlowup({zoomLevel:18,mapType:G_SATELLITE_MAP});
       });
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

## Démonstration

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto8.html" height="350px" width="100%"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto8.html)

## Remarques

Toujours se référer à l'API Google Maps - [Google Maps API Reference](http://code.google.com/apis/maps/documentation/reference.html) pour les différentes classes, méthodes et options utilisées. Le fichier XML doit toujours être une URL accessible. Consulter cette [page](http://code.google.com/apis/kml/documentation/kmlreference.html) pour les spécifications des fichiers KML.

## Conclusion

Ce tutoriel décrit les étapes pour ajouter un fichier KML à la carte et pour afficher une mini-carte dans une infobulle. Les possiblités d'utilisation de superposition d'un fichier sont nombreuses - exemple [le projet Inde à vélo](http://www.sigma2008.org/projects).

----

<!-- geotribu:authors-block -->
