---
title: 11. Géocoder une adresse
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-08-22
description: 11. Géocoder une adresse
tags:
    - géocodage
    - Google Maps
---

# 11. Géocoder une adresse

:calendar: Date de publication initiale : 07 septembre 2008

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-thumbnail-left }

L'API Google Maps possède des fonctions de géocodage à l'adresse qui permettent d'obtenir la longitude et la latitude à partir d'une adresse.  

Nous allons voir dans ce tutoriel comment utiliser cette fonctionnalité et comment ajouter un champ de saisie sur la carte.  

## Initialisation

Reprendre la carte du [tutoriel n°2](2008-08-22_2-enrichir-la-carte-avec-des-boutons-et-des-controles.md).  

## Géocodage

Définir la fonction `showAddress` qui géocode l'adresse saisie et créé un marqueur cliquable :  

```javascript
function showAddress(address) {  
  if (geocoder) {  
    geocoder.getLatLng(address,function(point) {  
      if (!point) {  
        alert(address + " not found");  
      }  
      else {  
        map.setCenter(point);  
        var marker = new GMarker(point);  
        map.addOverlay(marker);  
        var html = '![](./logos/logo_geotribu.png)';  
        GEvent.addListener(marker, 'click', function() {  
          marker.openInfoWindowHtml(html);  
        });  
      }  
    });  
  }  
}
```

Définir un géocodeur grâce à la classe GClientGeocoder : `geocoder = new GClientGeocoder();`  

Définir un container qui appelle le formulaire de saisie :  

```javascript
var address = new GControlPosition(G_ANCHOR_TOP_LEFT, new GSize(60, 10));  
address.apply(document.getElementById("address"));  
map.getContainer().appendChild(document.getElementById("address"));
```  

Et éditer le formulaire en HTML :  

!!! info
    Le serveur hébergeant le formulaire n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée est désactivée.

## Code complet

```javascript
<script type="text/javascript">

var map = null;
var geocoder = null;

function showAddress(address) {
  if (geocoder) {
    geocoder.getLatLng(address,function(point) {
      if (!point) {
        alert(address + " not found");
      }
      else {
        map.setCenter(point);
        var marker = new GMarker(point);
        map.addOverlay(marker);
        var html = '<img src="./logos/logo_geotribu.png">';
        GEvent.addListener(marker, 'click', function() {
          marker.openInfoWindowHtml(html);
        });
      }
    });
  }
}

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

    geocoder = new GClientGeocoder();

    var address = new GControlPosition(G_ANCHOR_TOP_LEFT, new GSize(60, 10));
    address.apply(document.getElementById("address"));
    map.getContainer().appendChild(document.getElementById("address"));

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
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto11.html" height="350px" width="100%"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto11.html)
Evidemment le résultat est plus joli en pleine page :-)

## Remarques

Toujours se référer à l'API Google Maps - [Google Maps API Reference](http://code.google.com/apis/maps/documentation/reference.html) pour les différentes classes, méthodes et options utilisées.
Le nombre de géocodage est limité à 15000 par jour et par adresse IP.
La requête de géocodage renvoie deux codes : le premier est le statut (savoir si la requête a réussi, si le nombre de requêtes autorisés est dépassé, etc) et le second le niveau de précision du géocodage (de 1 à 8).

## Conclusion

Le géocodage à l'adresse est très simple à mettre en place grâce à l'API Google Maps. Cette fonctionnalité enrichie de belle manière une interface cartographique.

----

<!-- geotribu:authors-block -->
