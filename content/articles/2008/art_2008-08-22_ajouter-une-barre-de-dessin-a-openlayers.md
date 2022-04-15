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
- EditingToolbar
title: Ajouter une barre de dessin à OpenLayers
---

# Ajouter une barre de dessin à OpenLayers


:calendar: Date de publication initiale : 22 août 2008


----

### - Introduction -




---


Ce tutorial vous permettra d'intégrer une barre d'outil de dessin à votre environnement cartographique offert par OpenLayers. Pour les novices dans ce domaine, je vous conseille auparavant la lecture de cet autre article décrivant de manière détaillée ce qu'est la librairie OpenLayers ainsi que son utilisation. L'exemple présenté ci-dessous s'inspire de Editing Toolbar Example présenté sur les pages d'exemples du site d'OpenLayers.


### - Ajouter un barre d'outil dessin -




---


L'ajout d'une barre d'outil dans l'environnement d'Open Layers n'est pas quelque chose de très dificille. En effet, cette fonctionnalité a été prévue dans le code lui même.


Il s'agit donc d'ajouter un nouvel objet (OpenLayers.Control.EditingToolbar) ainsi qu'une couche éditable ( OpenLayers.Layer.Vector( "Editable" ).


`function init() {  

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

map.addControl(new OpenLayers.Control.EditingToolbar(vlayer));`


}














----

## Auteur

![Portait de Arnaud](){: .img-rdp-news-thumb }
**Arnaud**

