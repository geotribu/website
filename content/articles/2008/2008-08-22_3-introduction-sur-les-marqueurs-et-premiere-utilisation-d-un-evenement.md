---
title: "3. Introduction sur les marqueurs et première utilisation d'un événement"
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-08-22
description: "3. Introduction sur les marqueurs et première utilisation d'un événement"
tags:
    - événement
    - Google Maps
    - marqueurs
---

# 3. Introduction sur les marqueurs et première utilisation d'un événement

:calendar: Date de publication initiale : 22 août 2008

:warning: L'API Google Maps v2 est dépréciée depuis le 19 mai 2010.

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-thumbnail-left }

Les deux premiers tutoriaux - 1 et 2 - nous ont permis d'afficher une carte Google Maps sur une page Web.

Ce tutoriel explique comment ajouter un marqueur sur la carte et comment ouvrir une infobulle lors d'un clic sur ce marqueur.

## Initialisation

Pour ce tutoriel, nous partirons de la carte définie dans le second tutoriel et alimenterons la fonction `initialize()`.

## Création du marqueur

Un marqueur se crée de la manière suivante en utilisant la classe [GMarker](http://code.google.com/intl/fr/apis/maps/documentation/reference.html#GMarker) de l'API.

Le première ligne est la création du marqueur.

La seconde ajoute le marqueur sur la carte.

```javascript
var marker1 = new GMarker(new GLatLng(43.57726664771851, 1.402251992034912));
map.addOverlay(marker1);
```

## Gestion de l'événement 'click' sur le marqueur

La classe [GEvent](http://code.google.com/intl/fr/apis/maps/documentation/reference.html#GEvent) permet de gérer de nombreux événements sur la carte et tous ses éléments contenus.
Il suffit juste de définir un événement lors d'un clic sur le marqueur précédemment défini :

```javascript
GEvent.addListener(marker1, 'click', function() {
  marker1.openInfoWindowHtml(html);
});
```

Ici un 'clic' sur le marqueur ouvrira une infobulle contenant du HTML :

```javascript
var html = "Ici vous pouvez insérer des images, du flash, des vidéos ou tout simplement du texte.";
```

## Code complet

```html
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>
    [Google Maps] 3. Introduction sur les marqueurs et première utilisation d'un événement
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
      var marker1 = new GMarker(new GLatLng(43.57769664771851, 1.402821992034912));
      map.addOverlay(marker1);
      var html = ;
      GEvent.addListener(marker1, 'click', function() {
        marker1.openInfoWindowHtml(html);
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
    `<iframe src="http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto3.html" height="350px" width="100%"></iframe>`

[Résultat pleine page](http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto3.html)

## Remarque

Nous verrons par la suite comment ajouter des marqueurs stockés en base de données. Cependant, la méthode sera la même. Il est également possible d'ajouter des marqueurs en appelant un fichier KML ou GeoRSS - nous verrons ceci prochainement.

## Conclusion

La création d'un marqueur est tout aussi facile que l'initialisation de la carte. Il est également possible de personnaliser les icônes des marqueurs grâce à la classe GIcon ([http://code.google.com/intl/fr/apis/maps/documentation/reference.html#GIcon](http://code.google.com/intl/fr/apis/maps/documentation/reference.html#GIcon)).

----

<!-- geotribu:authors-block -->
