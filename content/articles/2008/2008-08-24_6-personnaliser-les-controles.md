---
title: "6. Personnaliser les contrôles"
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-08-24
description: "6. Personnaliser les contrôles"
tags:
    - Google Maps
---

# 6. Personnaliser les contrôles

:calendar: Date de publication initiale : 24 août 2008

:warning: L'API Google Maps v2 est dépréciée depuis le 19 mai 2010.

----

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-thumbnail-left }

Il est parfois frustrant lorsqu'on utilise des API de ne pas pouvoir personnaliser complètement les contrôles et les événements. L'API Google Maps permet cette fonctionnalité. Nous verrons ici comment personnaliser ses propres contrôles de zoom, de déplacement et de sélection de couches.  

### Initialisation

Reprendre la carte du [tutoriel n°1](2008-08-22_1-introduction-a-l-api-google-maps.md).  

### Création de la fonction zoom

La création de ses propres contrôles passe par la déclaration d'une fonction et de la déclaration d'un objet 'prototype' comme une instance de l'objet `GControl()` :  

```javascript
ZoomControl.prototype = new GControl();  
```

Puis par la création du 'container', des boutons et des événements :  

```javascript
function ZoomControl() {}  
  ZoomControl.prototype = new GControl();  
  ZoomControl.prototype.initialize = function(map) {  

  var container = document.createElement("div");
  var zoomInDiv = document.createElement("div");  
  this.setButtonStyle_(zoomInDiv);  
  container.appendChild(zoomInDiv);  
  zoomInDiv.appendChild(document.createTextNode("Zoom In"));  
  zoomInDiv.innerHTML = '![](./icons/32x32/1.png)';  
  GEvent.addDomListener(zoomInDiv, "click", function() {  
    map.zoomIn();  
  });
  map.getContainer().appendChild(container);  
  return container;  
}
```

## Positionnement du container

Il faut ensuite positionner le container par rapport aux bords de la carte :  

```javascript
ZoomControl.prototype.getDefaultPosition = function() {  
  return new GControlPosition(G_ANCHOR_TOP_LEFT, new GSize(5, 5));  
}
```

## Ajout du contrôle

Il est maintenant nécessaire d'appeler cette fonction de zoom personnalisée :  

```javascript
map.addControl(new ZoomControl());
```

## Paramétrage par défaut de la carte

La dernière étape est de définir un centre, un niveau de zoom et une couche par défaut à la carte :  

```javascript
map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),15);  
map.setMapType(G_SATELLITE_MAP);
```

## Code complet

```html
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>
      [Google Maps] 6. Personnaliser les contrôles
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
          return new GControlPosition(G_ANCHOR_TOP_RIGHT, new GSize(getWindowWidth()/2-16, 0));
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
          return new GControlPosition(G_ANCHOR_BOTTOM_RIGHT, new GSize(getWindowWidth()/2-16, 0));
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
          return new GControlPosition(G_ANCHOR_TOP_RIGHT, new GSize(0, getWindowHeight()/2-16));
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
          return new GControlPosition(G_ANCHOR_TOP_LEFT, new GSize(0, getWindowHeight()/2-16));
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
          return new GControlPosition(G_ANCHOR_BOTTOM_LEFT, new GSize(getWindowWidth()/7, 0));
        }

        map.addControl(new ZoomControl());
        map.addControl(new PanUpControl());
        map.addControl(new PanDownControl());
        map.addControl(new PanRightControl());
        map.addControl(new PanLeftControl());
        map.addControl(new CustomMapControl());
        map.addControl(new LogoControl());
        map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),15);
        map.enableScrollWheelZoom();
        map.enableContinuousZoom();
        map.setMapType(G_SATELLITE_MAP);
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
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto6.html" height="350px" width="100%"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto6.html)

## Remarques

Je n'ai décrit ici que la personnalisation de la fonction de zoom, les fonctions de déplacement fonctionnent exactement sous le même mécanisme.
Pour bien appréhender l'objet GControl(), il est nécessaire de se référer à l'API Google Maps - [http://code.google.com/apis/maps/documentation/reference.html#GControlImpl](http://code.google.com/apis/maps/documentation/reference.html#GControlImpl) - et aux articles Google Maps officiels - [http://code.google.com/apis/maps/documentation/controls.html#Custom_Controls](http://code.google.com/apis/maps/documentation/controls.html#Custom_Controls).
Les constantes G_ANCHOR_x_y correspondent aux coins de la carte.

## Conclusion

Ce tutoriel décrit les étapes pour ajouter des contrôles à la carte.
La réutilisation de ce code nécessite de bonnes notions d'algorithmique et de Javascript.
Il est nécessaire de se plonger en détail dans l'API pour comprendre tous les mécanismes mis en jeu.

----

<!-- geotribu:authors-block -->
