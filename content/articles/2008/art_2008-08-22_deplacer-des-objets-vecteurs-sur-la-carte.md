---
authors:
- Arnaud
categories:
- article
date: 2008-08-22 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- OpenLayers
- vecteurs
title: Déplacer des objets vecteurs sur la carte
---

# Déplacer des objets vecteurs sur la carte


:calendar: Date de publication initiale : 22 août 2008


----

### - Introduction -





---


Ce tutorial est la suite logique de "[Ajout d'une barre d'outil dessin à OpenLayers](http://ks356007.kimsufi.com/arno/geotribu/?q=node/26)". En effet, nous allons étudier les différentes interactions possibles avec les objets de type vectors. Il s'appuie en grande partie de ressources disponibles sur le net, et notamment : [OpenLayers Drag Feature](http://www.openlayers.org/dev/examples/drag-feature.html).


### - Déplacer des objets sur la carte -




---


Le déplacement d'objet (feature) sur la carte est pré-programmé. En effet, l'API d'OpenLayers définit une méthode nommée DragFeature auquelle il faut passer en argument la couche qu'il est possible de déplacer.


`function init() {  

var map, vectors, panel, controls, maxExtent;  

// Création du constructeur Map  

map = new OpenLayers.Map( 'map', { controls: [] } );  

// Nouvelle couche layer WMS  

var layer = new OpenLayers.Layer.WMS( "OpenLayers WMS","http://labs.metacarta.com/wms/vmap0? ", {layers: 'basic'});  

// Ajout de la couche WMS à la carte  

map.addLayer(layer);  

// Caractéristiques générales de la carte  

map.setCenter(new OpenLayers.LonLat(0, 0), 2);`


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














----

## Auteur

![Portait de Arnaud](){: .img-rdp-news-thumb }
**Arnaud**

