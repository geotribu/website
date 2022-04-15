---
authors:
- Fabien Goblet
categories:
- article
date: 2008-08-22 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- Google Maps
- contrôles
title: 2. Enrichir la carte avec des boutons et des contrôles
---

# 2. Enrichir la carte avec des boutons et des contrôles


:calendar: Date de publication initiale : 22 août 2008


----





![attention_light.jpg](/sites/default/files/Tuto/img/attention_light.jpg)**L'API Google Maps v2 est dépréciée depuis le 19 mai 2010.**


### Introduction




---


Suite au [tutoriel d'introduction](http://www.geotribu.net/node/12/) sur l'API Google Maps, il devient nécessaire d'enrichir un peu la carte de boutons de contrôle et de sélecteurs de vue. Nous verrons ici comment utiliser les méthodes de l'API Google Maps pour étoffer la carte.  



### Initialisation




---


Nous utiliserons la carte définie dans le tutoriel d'introduction à l'API Google Maps pour l'enrichir.  

Les méthodes ajoutées se feront donc dans la fonction initialize() précédemment définie, le reste de la page HTML n'étant pas modifié.  



### Control Classes




---


Il existe de nombreuses fonctionnalités dans l'API Google Maps pour définir les contrôles de la carte.
* Ajouter le contrôle des types de vue  

`map.addControl(new GMapTypeControl());`
* Enlever le type de carte G\_HYBRID\_MAP  

`map.removeMapType(G_HYBRID_MAP);`
* Ajouter le type "Relief"  

`map.addMapType(G_PHYSICAL_MAP);`
* Définir par défaut le type de carte "Relief"  

`map.setMapType(G_PHYSICAL_MAP);`
* ajouter la carte de navigation globale  

`map.addControl(new GOverviewMapControl());`
* Ajouter l'échelle  

`map.addControl(new GScaleControl());`
* Ajouter les boutons de zoom et de navigation  

`map.addControl(new GLargeMapControl());`
* Ajouter la possibilité de zoomer grâce à la molette de la souris  

`map.enableScrollWheelZoom();`






### Code complet




---


`-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">  







[Google Maps] 2. Introduction sur les contrôles  



html { overflow:hidden; height:100%; } 
body { height:100%; margin:0; }
#map { width:100%; height:100%; }

function initialize() {
if (GBrowserIsCompatible()) {
var map = new GMap2(document.getElementById('map'));
map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),15);
map.addControl(new GMapTypeControl());
map.removeMapType(G\_HYBRID\_MAP);
map.addMapType(G\_PHYSICAL\_MAP);
map.setMapType(G\_PHYSICAL\_MAP);
map.addControl(new GOverviewMapControl());
map.addControl(new GScaleControl());
map.addControl(new GLargeMapControl());
map.enableScrollWheelZoom();
}
else{
alert('Désolé, mais votre navigateur n\'est pas compatible avec Google Maps');
}
}`  



### Démonstration




---






[Résultat pleine page](http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto2.html)


### Remarques




---


Il existe de nombreux autres types de contrôles - [API Google Maps](http://code.google.com/apis/maps/documentation/reference.html) - à vous de les tester
* [GControl](http://code.google.com/apis/maps/documentation/reference.html#GControlImpl)
* [GMapTypeControl](http://code.google.com/apis/maps/documentation/reference.html#GMapTypeControl)
* [GMenuMapTypeControl](http://code.google.com/apis/maps/documentation/reference.html#GMenuMapTypeControl)
* [GHierarchicalMapTypeControl](http://code.google.com/apis/maps/documentation/reference.html#GHierarchicalMapTypeControl)




### Conclusion




---


L'ajout de contrôle sur une carte Google Maps est très simple tout comme la création d'une simple carte. Il est cependant nécessaire de parcourir l'API pour voir les différentes classes et méthodes qu'il est possible d'utiliser.

Il existe de nombreux types de vue différents :
* G\_NORMAL\_MAP : carte simple - par défaut
* G\_SATELLITE\_MAP : vue satellite
* G\_HYBRID\_MAP : couplage vue satellite et carte simple
* G\_PHYSICAL\_MAP : carte relief
* G\_MOON\_ELEVATION\_MAP : vue relief de la Lune ...
* G\_MOON\_VISIBLE\_MAP : vue aérienne de la Lune ...
* G\_MARS\_ELEVATION\_MAP : vue relief de Mars ...
* G\_MARS\_VISIBLE\_MAP : vue 'mode visible' de Mars ..
* G\_MARS\_INFRARED\_MAP : vue 'infrarouge' de Mars ...
* G\_SKY\_VISIBLE\_MAP : vue du 'ciel' ...
* G\_SATELLITE\_3D\_MAP : vue 3D Google Earth - que nous verrons par la suite dans un prochain tutoriel sur l'utilisation de l'API Google Earth et du plugin




**Auteur : Fabien - fabien.goblet [ at ] gmail.com**




----

## Auteur

--8<-- "content/team/fgob.md"
