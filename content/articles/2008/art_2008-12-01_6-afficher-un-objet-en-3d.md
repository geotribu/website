---
authors:
    - Fabien Goblet
categories:
    - article
date: 2008-12-01 10:20
description: ""
image: ''
license: default
robots: index, follow
tags:
- Google Earth
- 3D
- API
- Sketchup
title: 6. Afficher un objet en 3D
---

# 6. Afficher un objet en 3D

:calendar: Date de publication initiale : 01 décembre 2008

----

### Introduction

---

L'API Google Earth propose d'afficher dans son globe des objets en 3D provenant notamment de [Sketchup](http://sketchup.google.com/intl/fr/).  

### Initialisation

---

Reprendre la carte du tutoriel sur les marqueurs et les événements : <http://www.geotribu.net/?q=node/55>  

### Processus

---

Définir une fonction qui vérifie la validité du fichier KML :  

`function finished(object) {  

if (!object) {  

alert('KML mal formé');  

return;  

}  

ge.getFeatures().appendChild(object);  

}`  

Définir l'objet géographique KML :  

`var kmlUrl = 'url du KML';`  

Et l'appliquer sur la carte :  

`google.earth.fetchKml(ge, kmlUrl, finished);`  

### Code complet

---

`[Google Earth] 6. Afficher un objet en 3D

html { overflow:hidden; height:100%; }
body { height:100%; margin:0; }

google.load("earth", "1");
var ge = null;

function init() {
google.earth.createInstance("map3d", initCallback);
}

function initCallback(object) {
ge = object;
ge.getWindow().setVisibility(true);
ge.getOptions().setMouseNavigationEnabled(true);
ge.getNavigationControl().setVisibility(ge.VISIBILITY\_SHOW);

var camera = ge.createLookAt('');
camera.set(43.6,1.44949866510018,2860,ge.ALTITUDE\_RELATIVE\_TO\_GROUND,190,75,10000);
ge.getView().setAbstractView(camera);
map = ge.createStyleMap('styleMap');

function finished(object) {
if (!object) {
alert('KML mal formé');
return;
}
ge.getFeatures().appendChild(object);
}

var kmlUrl = 'url du KML';
google.earth.fetchKml(ge, kmlUrl, finished);

}`  

### Démonstration

---

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto6.html)

### Remarques

---

L'affichage d'un objet 3D provenant de Sketchup se fait de la même façon qu'un fichier KML.

### Conclusion

---

Sketchup est un logiciel de création d'objets 3D, voir le [site officiel](http://sketchup.google.com/intl/fr/) pour plus d'informations.

**Merci à Jean-Hugues Puech pour son musée de Portet-sur-Garonne.**

**Auteur : Fabien - fabien.goblet [ at ] gmail.com**

----

## Auteur

--8<-- "content/team/fgob.md"
