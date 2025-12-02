---
title: "Introduction à OpenLayers"
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-08-22
description: "Introduction à OpenLayers"
tags:
    - OpenLayers
---

# Introduction à OpenLayers

:calendar: Date de publication initiale : 22 août 2008

## Introduction

![Logo OpenLayers](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/openlayers.png){: .img-thumbnail-left }

Ce tutorial est un aperçu rapide des possibilités d'OpenLayers. Il vous permettra de comprendre globalement le fonctionnement de cette bibliothèque Javascript OpenSource tournée vers la cartographie.

- Intégration d'OpenLayers
- Afficher une carte
- Enrichir l'interface
- Ajouter des marqueurs

## Intégration d'OpenLayers

La dernière version d'OpenLayers est librement téléchargeable à l'adresse suivante : OpenLayers (link is external).

Une fois dézippé, placer le répertoire OpenLayers dans votre environnement de développement Web (ex: le localhost d'apache). Pour l'instant rien de bien sorcier. Il faut maintenant créer une page internet (de type htm par ex) dans laquelle sera spécifiée à l'intérieur du header la localisation du répertoire d'OpenLayers. Cela se fait de la manière suivante :

```html
<DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
   <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
   <title>OpenLayers exemplestitle>
   <script src="./js/OpenLayers/OpenLayers.js" type="text/javascript">
   </script>
</head>
```

## Afficher une carte

Nous allons aborder ici une partie un peu longue et compliquée. Pour comprendre ce qui va suivre, des connaissances en Javascript sont nécessaires.

L'une des premières étapes est de créer un nouvel objet map grâce au constructeur OpenLayers.Map (1), il prend comme paramètre l'id de la balise qui contiendra la carte. C'est à partir de ce dernier que nous pourrons manipuler les éléments relatifs à la carte. Ensuite, nous allons utiliser ce qui fait un des nombreux atouts d'OpenLayers qu'est la possibilité d'interroger des serveurs cartographique grâce au protocole wms(2). Pour finir nous allons afficher la carte désirée (3).

Le résultat est visible sur cette page : exemple 1.

```html
</head>
   <script src="./js/OpenLayers/OpenLayers.js" type="text/javascript">
   <script type="text/javascript">
    function init() {
      var map, ol_wms;     // (1) instanciation du constructeur
     map = new OpenLayers.Map('map');
         // (2) Choix des couches
           var ol_wms = new OpenLayers.Layer.WMS( "OpenLayers WMS","http://labs.metacarta.com/wms/vmap0?", {layers: 'basic'});
         // (3) ajout des couches a la carte
          map.addLayers([ol_wms]);
     //On zoom au max
     map.zoomToMaxExtent();;
   }
  </script>
</head>
  <body onload="init()" >
    <div id="map"></div>
  </body>
</html>
```

## Enrichir l'interface

Comme vous avez pu le constater dans l'exemple 1, OpenLayers dispose d'une interface par défaut. Mais il est possible de rajouter un certain nombre d'options de configuration grâce à la classe controls. Comme par exemple une barre pour ajuster le seuil de zoom, l'affichage des coordonnées...

Dans la liste ci-dessous sont définies les boutons de contrôles les plus courants (une liste complète est néanmoins disponible ici) :

| Classe | Description |
| :----- | :---------- |
| PanZoomBar | Affiche une barre de zoom (par défaut c'est panZoom qui est utilisé). |
| Scale | Affiche l'échelle courante. |
| LayerSwitcher | Affiche un sélecteur permettant de choisir la couche désirée. |
| EditingToolbar | Affiche la barre d'édition des objets géographiques. |
| MousePosition | Affiche la position du curseur. |
| OverviewMap | Ajoute une carte de référence. |

Il existe deux manières pour modifier l'apparence général de la carte :

- En indiquant les options au constructeur :

```javascript
new OpenLayers.Map('map', {controls:[new OpenLayers.Control.OverviewMap()]});
```

- En utilisant la méthode addcontrol() :

```javascript
map.addControl(new OpenLayers.Control.PanZoomBar());
```

L'exemple ci-dessous (visible sur cette page : exemple 2) explique comment changer l'apparence de la carte en utilisant successivement les deux méthodes exposées précédemment. Ainsi dans un premier temps nous annulons la configuration par défaut d'OpenLayers grâce à MouseDefaults, puis nous ajoutons une barre de zoom et la carte d'aperçu.

```html
<html>
  <head>
     <script src="./js/OpenLayers/OpenLayers.js" type="text/javascript">
     <script type="text/javascript">
      function init() {
        var map, ol_wms;     //instanciation du constructeur
       map = new OpenLayers.Map('map', { controls:
       [new OpenLayers.Control.MouseDefaults()]});
           //Ajout des options graph, zoom + apercu
       map.addControl(new OpenLayers.Control.PanZoomBar());
       map.addControl(new OpenLayers.Control.OverviewMap());
           //Choix des couches
             var ol_wms = new OpenLayers.Layer.WMS( "OpenLayers WMS", "http://labs.metacarta.com/wms/vmap0?", {layers: 'basic'});
           //ajout des couches a la carte
            map.addLayers([ol_wms]);
       //On zoom au max
       map.zoomToMaxExtent();
     }
    </script>
  </head>
  <body onload="init()" >
    <div id="map"></div>
  </body>
</html>
```

## Ajouter des marqueurs

Les marqueurs sont des indicateurs de position, ils vont permettre de localiser un objet géographique sur la carte.

La création d'un marqueur se fait grâce au constructeur "OpenLayers. Marker". Il suffit ensuite d'ajouter celui-ci à la carte par l'intermédiaire de la méthode markers.addMarker.

Il existe différents types de marqueurs mais pour des raisons de simplicité nous n'en verrons ici qu'un seul. L'objectif du code ci-dessous est tout d'abord d'afficher un marqueur à une position géographique définie. Ensuite, nous allons ajouter un peu d'interactivité en spécifiant qu'au click de l'utilisateur sur le marqueur une fenêtre d'information doit s'afficher. Le résultat du code ci-dessous est visible ici : exemple 3.

```html
<html>
  <head>
    <script src="./js/OpenLayers/OpenLayers.js" type="text/javascript">
    <script type="text/javascript">
      function init() {
        var map, layer;  
        map = new OpenLayers.Map('map', {controls:[new OpenLayers.Control.MouseDefaults()]});
       //Caracteristiques de la carte
        var ol_wms = new OpenLayers.Layer.WMS( "OpenLayers WMS","http://labs.metacarta.com/wms/vmap0?", {layers: 'basic'});
       map.addLayer();
       map.setCenter(new OpenLayers.LonLat(0, 0), 2);
       map.addControl(new OpenLayers.Control.LayerSwitcher());
       //Creation du layer Marker
       markers = new OpenLayers.Layer.Markers("Marker");
       map.addLayer(markers);
      //Creation du Marker
       feature = new OpenLayers.Feature(ol_wms, new OpenLayers.LonLat(0,45));
       marker = feature.createMarker();
       markers.addMarker(marker);
       marker.events.register("mousedown", marker, mousedown);
      //Gestion des evenements
       function mousedown(evt) {
         popup = feature.createPopup(true);
            popup.setContentHTML("Exemple de PopUp sur un marqueur");
              popup.setBackgroundColor("yellow");
            popup.setOpacity(0.6);
         markers.map.addPopup(popup);
       }
     }
    </script>
  </head>
  <body onload="init()" >
    <div id="map"></div>
  </body>
</html>
```

----

<!-- geotribu:authors-block -->
