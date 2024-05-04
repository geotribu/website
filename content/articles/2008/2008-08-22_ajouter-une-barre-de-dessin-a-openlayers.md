---
title: "Ajouter une barre de dessin à OpenLayers"
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-08-22
description: "Ajouter une barre de dessin à OpenLayers"
tags:
    - EditingToolbar
    - OpenLayers
---

# Ajouter une barre de dessin à OpenLayers

:calendar: Date de publication initiale : 22 août 2008

## Introduction

![Logo OpenLayers](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/openlayers.png){: .img-thumbnail-left }

Ce tutorial vous permettra d'intégrer une barre d'outil de dessin à votre environnement cartographique offert par OpenLayers. Pour les novices dans ce domaine, je vous conseille auparavant la lecture de cet autre article décrivant de manière détaillée ce qu'est la librairie OpenLayers ainsi que son utilisation. L'exemple présenté ci-dessous s'inspire de Editing Toolbar Example présenté sur les pages d'exemples du site d'OpenLayers.

## Ajouter un barre d'outil dessin

L'ajout d'une barre d'outil dans l'environnement d'Open Layers n'est pas quelque chose de très dificille. En effet, cette fonctionnalité a été prévue dans le code lui même.

Il s'agit donc d'ajouter un nouvel objet (OpenLayers.Control.EditingToolbar) ainsi qu'une couche éditable ( OpenLayers.Layer.Vector( "Editable" ).

```html
<html>
  <head>
    <script>
      function init() {
            var map, layer;
          // Création du constructeur Map
           map = new OpenLayers.Map( 'map', { controls: [] } );
          // Nouvelle couche layer WMS
                 var layer = new OpenLayers.Layer.WMS( "OpenLayers WMS","http://labs.metacarta.com/wms/vmap0?", {layers: 'basic'});
          // Ajout de la couche WMS à la carte
                   map.addLayer(layer);
          // Caractéristiques générales de la carte
                   map.setCenter(new OpenLayers.LonLat(0, 0), 2);
                 map.addControl(new OpenLayers.Control.LayerSwitcher());
           //Création du layer Editable de type vecteur
            vlayer = new OpenLayers.Layer.Vector( "Editable" );
           //Ajout du layer à la carte
            map.addLayer(vlayer);
          // Ajout de la barre d'outil de dessin
           map.addControl(new OpenLayers.Control.EditingToolbar(vlayer));

       }
    </script>
  </head>
  <body onload="init()" >
    <div id="map"</div>
  </body>
</html>
```

L'exemple correspondant au code ci-dessus est présenté sur cette page : Ajout d'une barre de dessin à OpenLayers

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://geotribu.net/applications/tutoriaux/openlayers/toolbar/toolbar.htm" height="420px" width="100%"></iframe>`

## Placer la barre d'outils en dehors de la carte

Par rapport au code précédent il y a peu de changements à effectuer pour placer la barre d'outils en dehors de la carte. En effet, la méthode openLayers.Control.EditingToolbar() peut prendre en argument optionnel le nom du DIV dans lequel sera placé la barre de dessin.

```html
<html>
  <head>
    <script>
    function init() {
          var map, layer;
        // Création du constructeur Map
         map = new OpenLayers.Map( 'map', { controls: [] } );
        // Nouvelle couche layer WMS
               var layer = new OpenLayers.Layer.WMS( "OpenLayers WMS","http://labs.metacarta.com/wms/vmap0?", {layers: 'basic'});
        // Ajout de la couche WMS à la carte
                 map.addLayer(layer);
        // Caractéristiques générales de la carte
                 map.setCenter(new OpenLayers.LonLat(0, 0), 2);
               map.addControl(new OpenLayers.Control.LayerSwitcher());
         //Création du layer Editable de type vecteur
          vlayer = new OpenLayers.Layer.Vector( "Editable" );
         // Ajour de la barre d'outil
          var divDessin = document.getElementById("barreDessin");
          var panel = new OpenLayers.Control.EditingToolbar(vlayer, {div: divDessin});  
         map.addControl(panel);
         //Ajout du layer à la carte
          map.addLayer(vlayer);

     }
    </script>
  </head>
  <body onload="init()" >
    <div id="map"></div>
    <div id="panel" class="olControlEditingToolbar"></div>
  </body>
</html>
```

----

<!-- geotribu:authors-block -->
