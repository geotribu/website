---
authors:
- Fabien Goblet
categories:
- article
date: 2008-11-17 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- Google Maps
- Google Bar
title: 15. Ajouter la GoogleBar
---

# 15. Ajouter la GoogleBar


:calendar: Date de publication initiale : 17 novembre 2008


----





### Introduction




---


L'API Google Maps permet de définir une barre de géolocalisation et d'afficher le résultat sur la carte.  



### Ajout de la Google Bar




---


`map.enableGoogleBar();`  



### Code complet




---


`-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">  







[Google Maps] 15. Ajouter la GoogleBar  



html { overflow:hidden; height:100%; }
body { height:100%; margin:0; }
#map { width:100%; height:100%; }



var map = null;

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

map.enableGoogleBar();

}
else{
alert('Désolé, mais votre navigateur n\'est pas compatible avec Google Maps');
}
}`  



### Démonstration




---






[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto15.html)


### Remarques




---


Toujours se référer à l'API Google Maps - [Google Maps API Reference](http://code.google.com/apis/maps/documentation/reference.html) pour les différentes classes, méthodes et options utilisées.
Lorsque l'on fait une recherche grâce à cette GoogleBar, l'API place automatiquement un marqueur géocodé sur la carte.


### Conclusion




---


Petit tutorial pour savoir déclarer le service GoogleBar.
Cette méthode est identique au tutoriel - [11.


**Auteur : Fabien - fabien.goblet [ at ] gmail.com**](http://geotribu.net/node/39)


----

## Auteur

--8<-- "content/team/fgob.md"
