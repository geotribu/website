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
- marqueurs
- événement
title: 3. Introduction sur les marqueurs et première utilisation d'un événement
---

# 3. Introduction sur les marqueurs et première utilisation d'un événement


:calendar: Date de publication initiale : 22 août 2008


----





![attention_light.jpg](/sites/default/files/Tuto/img/attention_light.jpg)**L'API Google Maps v2 est dépréciée depuis le 19 mai 2010.**


### Introduction




---


Les deux premiers tutoriaux - [1](http://www.geotribu.net/node/12) et [2](http://www.geotribu.net/node/13) - nous ont permis d'afficher une carte Google Maps sur une page Web.  

Ce tutoriel explique comment ajouter un marqueur sur la carte et comment ouvrir une infobulle lors d'un clic sur ce marqueur.  



### Initialisation




---


Pour ce tutoriel, nous partirons de la carte définie dans le [second tutoriel](http://www.geotribu.net/node/13) et alimenterons la fonction initialize().  



### Création du marqueur




---


Un marqueur se crée de la manière suivante en utilisant la classe [GMarker](http://code.google.com/intl/fr/apis/maps/documentation/reference.html#GMarker) de l'API.  

Le première ligne est la création du marqueur.  

La seconde ajoute le marqueur sur la carte.  

`var marker1 = new GMarker(new GLatLng(43.57726664771851, 1.402251992034912));  

map.addOverlay(marker1);`  



### Gestion de l'événement 'click' sur le marqueur




---


La classe [GEvent](http://code.google.com/intl/fr/apis/maps/documentation/reference.html#GEvent) permet de gérer de nombreux événements sur la carte et tous ses éléments contenus.  

Il suffit juste de définir un événement lors d'un clic sur le marqueur précédemment défini :  

`GEvent.addListener(marker1, 'click', function() {  

marker1.openInfoWindowHtml(html);  

});`  

Ici un 'clic' sur le marqueur ouvrira une infobulle contenant du HTML :  

`var html = "Ici vous pouvez insérer des images, du flash, des vidéos ou tout simplement du texte.";`  



### Code complet




---


`-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">  







[Google Maps] 3. Introduction sur les marqueurs et première utilisation d'un événement  



html { overflow:hidden; height:100%; }
body { height:100%; margin:0; }
#map { width:100%; height:100%; }

function initialize() {
if (GBrowserIsCompatible()) {
var map = new GMap2(document.getElementById('map'));
map.setCenter(new GLatLng(43.57769664771851, 1.402821992034912),16);
map.addControl(new GMapTypeControl());
map.removeMapType(G\_HYBRID\_MAP);
map.addMapType(G\_PHYSICAL\_MAP);
map.setMapType(G\_SATELLITE\_MAP);
map.addControl(new GOverviewMapControl());
map.addControl(new GScaleControl());
map.addControl(new GLargeMapControl());
map.enableScrollWheelZoom();
var marker1 = new GMarker(new GLatLng(43.57769664771851, 1.402821992034912));
map.addOverlay(marker1);
var html = "<img src='http://maps.google.fr/intl/fr\_fr/images/maps\_logo\_small.png' alt='Google Maps'></img><br><br>Dans cette
infobulle, le langage HTML est interprété.";
GEvent.addListener(marker1, 'click', function() {
marker1.openInfoWindowHtml(html);
});
}
else{
alert('Désolé, mais votre navigateur n\'est pas compatible avec Google Maps');
}
}`  



### Démonstration




---






[Résultat pleine page](http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto3.html)


### Remarques




---


Nous verrons par la suite comment ajouter des marqueurs stockés en base de données. Cependant, la méthode sera la même.
Il est également possible d'ajouter des marqueurs en appelant un fichier KML ou GeoRSS - nous verrons ceci prochainement.


### Conclusion




---


La création d'un marqueur est tout aussi facile que l'initialisation de la carte. Il est également possible de personnaliser les icônes des marqueurs grâce à la classe [GIcon](http://code.google.com/intl/fr/apis/maps/documentation/reference.html#GIcon).


**Auteur : Fabien - fabien.goblet [ at ] gmail.com**




----

## Auteur

--8<-- "content/team/fgob.md"
