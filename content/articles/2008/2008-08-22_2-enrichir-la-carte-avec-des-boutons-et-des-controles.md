---
title: "2. Enrichir la carte avec des boutons et des contrôles"
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-08-22
description: "2. Enrichir la carte avec des boutons et des contrôles"
tags:
    - Google Maps
    - contrôles
---

# 2. Enrichir la carte avec des boutons et des contrôles

:calendar: Date de publication initiale : 22 août 2008

:warning: L'API Google Maps v2 est dépréciée depuis le 19 mai 2010.

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-thumbnail-left }

Suite au [tutoriel d'introduction](2008-08-22_1-introduction-a-l-api-google-maps.md) sur l'API Google Maps, il devient nécessaire d'enrichir un peu la carte de boutons de contrôle et de sélecteurs de vue. Nous verrons ici comment utiliser les méthodes de l'API Google Maps pour étoffer la carte.

## Initialisation

Nous utiliserons la carte définie dans le tutoriel d'introduction à l'API Google Maps pour l'enrichir.
Les méthodes ajoutées se feront donc dans la fonction `initialize()` précédemment définie, le reste de la page HTML n'étant pas modifié.

## Control Classes

Il existe de nombreuses fonctionnalités dans l'API Google Maps pour définir les contrôles de la carte.

- Ajouter le contrôle des types de vue

```javascript
map.addControl(new GMapTypeControl());
```

- Enlever le type de carte G_HYBRID_MAP

```javascript
map.removeMapType(G_HYBRID_MAP);
```

- Ajouter le type "Relief"

```javascript
map.addMapType(G_PHYSICAL_MAP);
```

- Définir par défaut le type de carte "Relief"

```javascript
map.setMapType(G_PHYSICAL_MAP);
```

- ajouter la carte de navigation globale

```javascript
map.addControl(new GOverviewMapControl());
```

- Ajouter l'échelle

```javascript
map.addControl(new GScaleControl());
```

- Ajouter les boutons de zoom et de navigation

```javascript
map.addControl(new GLargeMapControl());
```

- Ajouter la possibilité de zoomer grâce à la molette de la souris

```javascript
map.enableScrollWheelZoom();
```

## Code complet

```html
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>
      [Google Maps] 2. Introduction sur les contrôles
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
          map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),15);
          map.addControl(new GMapTypeControl());
          map.removeMapType(G_HYBRID_MAP);
          map.addMapType(G_PHYSICAL_MAP);
          map.setMapType(G_PHYSICAL_MAP);
          map.addControl(new GOverviewMapControl());
          map.addControl(new GScaleControl());
          map.addControl(new GLargeMapControl());
          map.enableScrollWheelZoom();
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
    `<iframe src="http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto2.html" height="350px" width="100%"></iframe>`

[Résultat pleine page](http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto2.html)

## Remarques

Il existe de nombreux autres types de contrôles - [API Google Maps](http://code.google.com/apis/maps/documentation/reference.html) - à vous de les tester

- [GControl](http://code.google.com/apis/maps/documentation/reference.html#GControlImpl)
- [GMapTypeControl](http://code.google.com/apis/maps/documentation/reference.html#GMapTypeControl)
- [GMenuMapTypeControl](http://code.google.com/apis/maps/documentation/reference.html#GMenuMapTypeControl)
- [GHierarchicalMapTypeControl](http://code.google.com/apis/maps/documentation/reference.html#GHierarchicalMapTypeControl)

## Conclusion

L'ajout de contrôle sur une carte Google Maps est très simple tout comme la création d'une simple carte. Il est cependant nécessaire de parcourir l'API pour voir les différentes classes et méthodes qu'il est possible d'utiliser. Il existe de nombreux types de vue différents :

- G_NORMAL_MAP : carte simple - par défaut
- G_SATELLITE_MAP : vue satellite
- G_HYBRID_MAP : couplage vue satellite et carte simple
- G_PHYSICAL_MAP : carte relief
- G_MOON_ELEVATION_MAP : vue relief de la Lune ...
- G_MOON_VISIBLE_MAP : vue aérienne de la Lune ...
- G_MARS_ELEVATION_MAP : vue relief de Mars ...
- G_MARS_VISIBLE_MAP : vue 'mode visible' de Mars ..
- G_MARS_INFRARED_MAP : vue 'infrarouge' de Mars ...
- G_SKY_VISIBLE_MAP : vue du 'ciel' ...
- G_SATELLITE_3D_MAP : vue 3D Google Earth - que nous verrons par la suite dans un prochain tutoriel sur l'utilisation de l'API Google Earth et du plugin

----

<!-- geotribu:authors-block -->
