---
authors:
- Fabien Goblet
categories:
- article
date: 2009-01-17 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- Google Earth
- Google Maps
- 3D
title: 16 / 7. Intégrer la vue 3D de l'API Google Earth dans Google Maps
---

# 16 / 7. Intégrer la vue 3D de l'API Google Earth dans Google Maps


:calendar: Date de publication initiale : 17 janvier 2009


----





### Introduction




---


L'API Google Maps peut se coupler également avec l'API Google Earth Plugin (cf. les [tutoriaux](http://www.geotribu.net/node/23)) en ajoutant un bouton permettant de switcher entre les deux vues 2D et 3D.  



### Ajout de la 3D




---


`map.addMapType(G_SATELLITE_3D_MAP);`  



### Code complet




---


`-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">  







[Google Maps / Google Earth] 16 / 7. Intégrer la vue 3D de l'API Google Earth dans Google Maps  



html { overflow:hidden; height:100%; }
body { height:100%; margin:0; }
#map { width:100%; height:100%; }



function initialize() {

var map = new GMap2(document.getElementById("map"));
map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),15);
map.addControl(new GMapTypeControl());
map.removeMapType(G\_HYBRID\_MAP);
map.removeMapType(G\_SATELLITE\_MAP);
map.addMapType(G\_PHYSICAL\_MAP);

map.addMapType(G\_SATELLITE\_3D\_MAP);

}`  



### Démonstration




---






[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto16.html)


### Remarques




---


Toujours se référer à l'API Google Maps - [Google Maps API Reference](http://code.google.com/apis/maps/documentation/reference.html) pour les différentes classes, méthodes et options utilisées.
Lorsque l'on fait une recherche grâce à cette GoogleBar, l'API place automatiquement un marqueur géocodé sur la carte.


### Conclusion




---


Petit tutoriel pour intégrer la vue 3D fournie par l'API Google Earth dans une carte Google Maps.
Rien de bien compliqué ici.


**Auteur : Fabien - fabien.goblet [ at ] gmail.com**




----

## Auteur

--8<-- "content/team/fgob.md"
