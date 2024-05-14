---
title: "4. Introduction sur les polylignes"
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-08-22
description: "4. Introduction sur les polylignes"
tags:
    - Google
    - Google Maps
    - maps
    - polylignes
---

# 4. Introduction sur les polylignes

:calendar: Date de publication initiale : 22 août 2008

:warning: L'API Google Maps v2 est dépréciée depuis le 19 mai 2010.

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-thumbnail-left }

De la même manière que le troisième tutoriel sur l'affichage d'un marqueur, il est possible de définir et d'afficher une polyligne sur la carte.

## Initialisation

Pour ce tutoriel, nous partirons de la carte définie dans le second tutoriel et alimenterons la fonction `initialize()`.

## Création de la polyligne

Pour cela, il faut définir une liste de points :

```javascript
var points = [ new GLatLng(43.57776102358721,1.403797022247275),
               new GLatLng(43.57774203677786,1.402996671914309),
               new GLatLng(43.57770841326447,1.402996671901832),
               new GLatLng(43.57769313342543,1.402998782088943),
               new GLatLng(43.57767174734567,1.403007224111022),
               new GLatLng(43.57781081938519,1.402984013893814),
               new GLatLng(43.57776634571197,1.402916553930126),
               new GLatLng(43.57775256036395,1.402897600993683),
               new GLatLng(43.57773724611339,1.402872341766638),
               new GLatLng(43.577723523068,1.402899724384128),
               new GLatLng(43.57772504884841,1.402897617553464),
               new GLatLng(43.57772047329792,1.402906044132763),
               new GLatLng(43.57771286432422,1.402927106716888),
               new GLatLng(43.57769459159984,1.402956602400224),
               new GLatLng(43.57769612259359,1.402958710172129),
               new GLatLng(43.57770981869092,1.402931318866109),
               new GLatLng(43.57767479573649,1.403000892396264)];
```

Et de définir la polyligne grâce à la classe [GPolyline](http://code.google.com/intl/fr/apis/maps/documentation/reference.html#GPolyline) :

```javascript
var poly = new GPolyline(points);
```

## Affichage de la polyligne sur la carte

En utilisant la méthode overlay sur la carte (cf. tutoriel n°3), on affiche la polyligne sur la carte :

```javascript
map.addOverlay(poly);
```

## Code complet

```html
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>
      [Google Maps] 4. Introduction sur les polylignes
    </title>
    <style type="text/css">
      html { overflow:hidden; height:100%; }
      body { height:100%; margin:0; }
      #map { width:100%; height:100%; }
    </style>
    <script src="http://maps.google.com/maps?file=api&v=2.x&key=votre_clé_ici" type="text/javascript"></script>
    <script type="text/javascript">
      function initialize() {
        if (GBrowserIsCompatible()) {
          var map = new GMap2(document.getElementById('map'));
          map.setCenter(new GLatLng(43.57769664771851, 1.402821992034912),16);
          map.addControl(new GMapTypeControl());
          map.removeMapType(G_HYBRID_MAP);
          map.addMapType(G_PHYSICAL_MAP);
          map.setMapType(G_SATELLITE_MAP);
          map.addControl(new GOverviewMapControl());
          map.addControl(new GScaleControl());
          map.addControl(new GLargeMapControl());
          map.enableScrollWheelZoom();
          var points = [ new GLatLng(43.57776102358721,1.403797022247275),
                         new GLatLng(43.57774203677786,1.402996671914309),
                         new GLatLng(43.57770841326447,1.402996671901832),
                         new GLatLng(43.57769313342543,1.402998782088943),
                         new GLatLng(43.57767174734567,1.403007224111022),
                         new GLatLng(43.57781081938519,1.402984013893814),
                         new GLatLng(43.57776634571197,1.402916553930126),
                         new GLatLng(43.57775256036395,1.402897600993683),
                         new GLatLng(43.57773724611339,1.402872341766638),
                         new GLatLng(43.577723523068,1.402899724384128),
                         new GLatLng(43.57772504884841,1.402897617553464),
                         new GLatLng(43.57772047329792,1.402906044132763),
                         new GLatLng(43.57771286432422,1.402927106716888),
                         new GLatLng(43.57769459159984,1.402956602400224),
                         new GLatLng(43.57769612259359,1.402958710172129),
                         new GLatLng(43.57770981869092,1.402931318866109),
                         new GLatLng(43.57767479573649,1.403000892396264)];
          map.addOverlay(new GPolyline(points));
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
    `<iframe src="http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto4.html" height="350px" width="100%"></iframe>`

[Résultat pleine page](http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto4.html)

## Conclusion

L'affichage d'une polyligne sur une carte Google Maps est tout aussi simple que l'affichage d'un simple marqueur. Il est possible de gérer des événements de la même façon que sur les simples marqueurs.

----

<!-- geotribu:authors-block -->
