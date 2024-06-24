---
title: "Déplacer des objets vecteurs sur la carte"
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-08-22
description: "Déplacer des objets vecteurs sur la carte"
tags:
    - OpenLayers
    - vecteurs
---

# Déplacer des objets vecteurs sur la carte

:calendar: Date de publication initiale : 22 août 2008

## Introduction

![Logo OpenLayers](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/openlayers.png){: .img-thumbnail-left }

Ce tutorial est la suite logique de "[Ajout d'une barre d'outil dessin à OpenLayers](2008-08-22_ajouter-une-barre-de-dessin-a-openlayers.md)". En effet, nous allons étudier les différentes interactions possibles avec les objets de type vectors. Il s'appuie en grande partie de ressources disponibles sur le net, et notamment : [OpenLayers Drag Feature](http://www.openlayers.org/dev/examples/drag-feature.html).

## Déplacer des objets sur la carte

Le déplacement d'objet (feature) sur la carte est pré-programmé. En effet, l'API d'OpenLayers définit une méthode nommée DragFeature auquelle il faut passer en argument la couche qu'il est possible de déplacer.

```html
<html>
<head>
<script>
function init() {
      var map, vectors, panel, controls, maxExtent;
    // Création du constructeur Map
     map = new OpenLayers.Map( 'map', { controls: [] } );
    // Nouvelle couche layer WMS
           var layer = new OpenLayers.Layer.WMS( "OpenLayers WMS","http://labs.metacarta.com/wms/vmap0? ", {layers: 'basic'});
    // Ajout de la couche WMS à la carte
             map.addLayer(layer);
    // Caractéristiques générales de la carte
             map.setCenter(new OpenLayers.LonLat(0, 0), 2);

     //Création du layer Editable de type vecteur
      vlayer = new OpenLayers.Layer.Vector( "Editable" );
     //Création du l'objet Panel
      panel = new OpenLayers.Control.Panel(
        {'displayClass': 'olControlEditingToolbar'});
     //Création des outils
     controls = {
        move : new OpenLayers.Control.Navigation(),
        point: new OpenLayers.Control.DrawFeature(vectors,
             OpenLayers.Handler.Point,
            {'displayClass': 'olControlDrawFeaturePoint'}),
        line: new OpenLayers.Control.DrawFeature(vectors,
            OpenLayers.Handler.Path,
            {'displayClass': 'olControlDrawFeaturePath'}),
        polygon: new OpenLayers.Control.DrawFeature(vectors,
             OpenLayers.Handler.Polygon,
            {'displayClass': 'olControlDrawFeaturePolygon'}),
        drag: new OpenLayers.Control.DragFeature(vectors,
             {'displayClass':'olControlDraggFeature'})
     //Ajout des outils à la barre
      for(var key in controls) {
         panel.addControls([controls[key]]);
      }
     //Ajout de la barre à la carte
      map.addControl(panel);
    // Ajout de la barre d'outil de dessin à la carte
     panel.activateControl(controls.point)

 }
 }
</script>
</head>
</body onload="init()" >
    <div id="map" </div>
</body>
<html>
```

## Définir un style pour l'icône de déplacement

Il suffit ensuite de définir un style à à notre nouvelle outil DragFeature que nous avons défini comme appartenant à la classe : olControlDraggFeature . Il y a cependant une petite subtilité.

En effet en fonction que l'outil soit actif ou inactif, OpenLayers ajoute ItemInactive ou ItemActive , ce qui donne :

```html
<style type="text/css">
#map {
  width: 512px;
  height: 350px;
  border: 1px solid gray;
}

.olControlDraggFeatureItemActive {
  background-image:url("Chemin_vers_Image/drag_on.png");
  background-repeat: no-repeat;
}
.olControlDraggFeatureItemInactive {
  background-image:url("Chemin_vers_Image/drag_off.png");
  background-repeat: no-repeat;
}
</style>
```

Les deux blocs de code présentés ci-dessus sont visibles sur l'exemple suivant :

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://geotribu.net/applications/tutoriaux/openlayers/toolbar/vector_move.htm" height="450px" width="100%"></iframe>`

----

<!-- geotribu:authors-block -->
