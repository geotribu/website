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
- Open Source
title: Introduction à OpenLayers
---

# Introduction à OpenLayers


:calendar: Date de publication initiale : 22 août 2008


----

Ce tutorial est un aperçu rapide des possibilités d'OpenLayers. Il vous permettra de comprendre globalement le fonctionnement de cette bibliothèque Javascript OpenSource tournée vers la cartographie.


- Intégration d'OpenLayers  

- Afficher une carte  

- Enrichir l'interface  

- Ajouter des marqueurs


### - Intégration d'OpenLayers -




---


La dernière version d'OpenLayers est librement téléchargeable à l'adresse suivante : [OpenLayers](http://trac.openlayers.org/wiki/HowToDownload).


Une fois dézippé, placer le répertoire OpenLayers dans votre environnement de développement Web (ex: le localhost d'apache). Pour l'instant rien de bien sorcier. Il faut maintenant créer une page internet (de type htm par ex) dans laquelle sera spécifiée à l'intérieur du header la localisation du répertoire d'OpenLayers. Cela se fait de la manière suivante :


`OpenLayers exemples`








### - Afficher une carte -




---


Nous allons aborder ici une partie un peu longue et compliquée. Pour comprendre ce qui va suivre, des connaissances en Javascript sont nécessaires.


L'une des premières étapes est de créer un nouvel objet map grâce au constructeur OpenLayers.Map (1), il prend comme paramètre l'id de la balise qui contiendra la carte. C'est à partir de ce dernier que nous pourrons manipuler les éléments relatifs à la carte. Ensuite, nous allons utiliser ce qui fait un des nombreux atouts d'OpenLayers qu'est la possibilité d'interroger des serveurs cartographique grâce au protocole wms(2). Pour finir nous allons afficher la carte désirée (3).


Le résultat est visible sur cette page : exemple 1.




<script type="text/javascript">
function init() {
var map, ol\_wms; // (1) instanciation du constructeur
map = new OpenLayers.Map('map');
// (2) Choix des couches
var ol\_wms = new OpenLayers.Layer.WMS( "OpenLayers WMS","http://labs.metacarta.com/wms/vmap0?", {layers: 'basic'});
// (3) ajout des couches a la carte
map.addLayers([ol\_wms]);
//On zoom au max
map.zoomToMaxExtent();;
}












----

## Auteur

![Portait de Arnaud](){: .img-rdp-news-thumb }
**Arnaud**
