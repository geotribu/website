---
title: 12. Calculer un itinéraire
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-09-07
description: 12. Calculer un itinéraire
tags:
    - Google Maps
    - itinéraire
---

# 12. Calculer un itinéraire

:calendar: Date de publication initiale : 07 septembre 2008

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-thumbnail-left }

De la même manière que le géocodage à l'adresse, l'API Google Maps permet de calculer un itinéraire en utilisant la classe [GDirections](http://code.google.com/intl/fr/apis/maps/documentation/reference.html#GDirections).  

## Initialisation

Reprendre la carte du [tutoriel n°2](2008-08-22_2-enrichir-la-carte-avec-des-boutons-et-des-controles.md).

## Calcul de l'itinéraire

Définir la fonction setDirections(fromAddress, toAddress) qui calcule l'itinéraire entre deux adresses :  

```javascript
function setDirections(fromAddress, toAddress) {  

gdir.load("from: " + fromAddress + " to: " + toAddress,{ "locale": "fr" });  

}
```

Définir un objet GDirections : `gdir = new GDirections(map);`  

Calculer un itinéraire lors de l'appel de la carte :

`setDirections("Allée Machado, Toulouse, fr", "Avenue de l'agrobiopole, Auzeville-Tolosane, fr", "fr");`

Et éditer le formulaire en HTML :  

!!! info
    Le serveur hébergeant le formulaire n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée est désactivée.

### Code complet

```javascript
var map = null;
var gdir;

function setDirections(fromAddress, toAddress) {
  gdir.load("from: " + fromAddress + " to: " + toAddress,{ "locale": "fr" });
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

    gdir = new GDirections(map);
    setDirections("Allée Machado, Toulouse, fr", "Avenue de l'agrobiopole, Auzeville-Tolosane, fr", "fr");

    var iti = new GControlPosition(G_ANCHOR_TOP_LEFT, new GSize(60, 10));
    iti.apply(document.getElementById("iti"));
    map.getContainer().appendChild(document.getElementById("iti"));

  }
  else{
    alert('Désolé, mais votre navigateur n\'est pas compatible avec Google Maps');
  }
}
```

## Démonstration

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto12.html" height="350px" width="100%"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto12.html)

Evidemment le résultat est plus joli en pleine page :-)

## Remarques

Toujours se référer à l'API Google Maps - [Google Maps API Reference](http://code.google.com/apis/maps/documentation/reference.html) pour les différentes classes, méthodes et options utilisées. Le nombre de requêtes est limité à 15000 par jour et par adresse IP (idem que le géocodage). Il est possible d'afficher l'itinéraire sous forme de texte en définissant un panel dans le constructeur `GDirections`.

## Conclusion

De la même manière que le géocodage, le calcul d'un itinéraire se fait de façon très simple grâce à l'API Google Maps. L'affichage de l'itinéraire ainsi que le niveau de zoom approprié est fait de façon automatique par la méthode `load()` de la classe `GDirections`.

----

<!-- geotribu:authors-block -->
