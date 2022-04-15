---
authors:
- Fabien Goblet
categories:
- article
date: 2008-09-07 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- Google Maps
- géocodage
title: 11. Géocoder une adresse
---

# 11. Géocoder une adresse


:calendar: Date de publication initiale : 07 septembre 2008


----





### Introduction




---


L'API Google Maps possède des fonctions de géocodage à l'adresse qui permettent d'obtenir la longitude et la latitude à partir d'une adresse.  

Nous allons voir dans ce tutoriel comment utiliser cette fonctionnalité et comment ajouter un champ de saisie sur la carte.  



### Initialisation




---


Reprendre la carte du  [tutoriel n°2](http://www.geotribu.net/node/13).  



### Géocodage




---


Définir la fonction showAddress qui géocode l'adresse saisie et créé un marqueur cliquable :  

`function showAddress(address) {  

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

}`  

Définir un géocodeur grâce à la classe GClientGeocoder :  

`geocoder = new GClientGeocoder();`  

Définir un container qui appelle le formulaire de saisie :  

`var address = new GControlPosition(G_ANCHOR_TOP_LEFT, new GSize(60, 10));  

address.apply(document.getElementById("address"));  

map.getContainer().appendChild(document.getElementById("address"));`  

Et éditer le formulaire en HTML :  





### Code complet




---


`-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">  







[Google Maps] 11. Géocoder une adresse  



html { overflow:hidden; height:100%; }
body { height:100%; margin:0; }
#map { width:100%; height:100%; }



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
var html = '<img src="./logos/logo\_geotribu.png">';
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
map.removeMapType(G\_HYBRID\_MAP);
map.addMapType(G\_PHYSICAL\_MAP);
map.setMapType(G\_PHYSICAL\_MAP);
map.addControl(new GOverviewMapControl());
map.addControl(new GScaleControl());
map.addControl(new GLargeMapControl());
map.enableScrollWheelZoom();

geocoder = new GClientGeocoder();

var address = new GControlPosition(G\_ANCHOR\_TOP\_LEFT, new GSize(60, 10));
address.apply(document.getElementById("address"));
map.getContainer().appendChild(document.getElementById("address"));

}
else{
alert('Désolé, mais votre navigateur n\'est pas compatible avec Google Maps');
}
}









![](./logos/logo_geotribu.png)`  



### Démonstration




---






[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto11.html)
Evidemment le résultat est plus joli en pleine page :-)


### Remarques




---


Toujours se référer à l'API Google Maps - [Google Maps API Reference](http://code.google.com/apis/maps/documentation/reference.html) pour les différentes classes, méthodes et options utilisées.
Le nombre de géocodage est limité à 15000 par jour et par adresse IP.
La requête de géocodage renvoie deux codes : le premier est le statut (savoir si la requête a réussi, si le nombre de requêtes autorisés est dépassé, etc) et le second le niveau de précision du géocodage (de 1 à 8).


### Conclusion




---


Le géocodage à l'adresse est très simple à mettre en place grâce à l'API Google Maps.
Cette fonctionnalité enrichie de belle manière une interface cartographique.


**Auteur : Fabien - fabien.goblet [ at ] gmail.com**




----

## Auteur

--8<-- "content/team/fgob.md"
