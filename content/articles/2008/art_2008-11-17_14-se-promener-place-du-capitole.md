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
- Street View
title: 14. Se promener place du Capitole
---

# 14. Se promener place du Capitole

:calendar: Date de publication initiale : 17 novembre 2008

----

### Introduction

---

Il est possible grâce à l'API Google Maps de naviguer virtuellement dans les rues, nous verrons ici comment implanter cette fonctionnalité.  

### Créer un panorama

---

Construire un panorama en lui indiquant son emplacement :  

`var myPano = new GStreetviewPanorama(document.getElementById("pano"));`  

Définir une destination :  

`var capitole = new GLatLng(43.60436298129637, 1.442950341024869);`  

Définir les attributs de la caméra - yaw pour la direction en degré de l'angle de vue et pitch l'inclinaison de la caméra :  

`var myPOV = {yaw:370.64659986187695,pitch:0};`  

Initialiser le panorama sur la destination et avec les paramètres de caméra :  

`myPano.setLocationAndPOV(capitole, myPOV);`  

Ajouter un événement (une alerte simple) si le navigateur ne supporte pas le Flash. :  

`GEvent.addListener(myPano, "error", handleNoFlash);`  

Définir l'événement :  

`function handleNoFlash(errorCode) {  

if (errorCode == 603) {  

alert("Flash n'est pas supporté par votre navigateur !");  

return;  

}  

}`  

Définir l'emplacement de la carte :  

### Code complet

---

`-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">  

[Google Maps] 14. Se promener place du Capitole  

html { overflow:hidden; height:100%; }
body { height:100%; margin:0; }
# pano { width:100%; height:100%; }

function initialize() {
if (GBrowserIsCompatible()) {
var myPano = new GStreetviewPanorama(document.getElementById("pano"));
var capitole = new GLatLng(43.60436298129637, 1.442950341024869);
var myPOV = {yaw:370.64659986187695,pitch:0};
myPano.setLocationAndPOV(capitole, myPOV);
GEvent.addListener(myPano, "error", handleNoFlash);
}
else{
alert('Désolé, mais votre navigateur n\'est pas compatible avec Google Maps');
}
}

function handleNoFlash(errorCode) {
if (errorCode == 603) {
alert("Error: Flash doesn't appear to be supported by your browser");
return;
}
}`  

### Démonstration

---

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto14.html)

### Remarques

---

Un panorama StreetView est une image cliquable, 'zoomable' et avec lequel on peut se diriger vers les images mitoyennes.
L'application est en Flash, ce qui permet la navigation 'demi-sphérique' dans la photographie.

### Conclusion

---

Les panoramas de StreetView sont facilement exploitables grâce à l'API.
Il faut maintenant coupler la couche des photos sur la carte - <http://geotribu.net/node/65> - et les photographies.

**Auteur : Fabien - fabien.goblet [ at ] gmail.com**

----

## Auteur

--8<-- "content/team/fgob.md"
