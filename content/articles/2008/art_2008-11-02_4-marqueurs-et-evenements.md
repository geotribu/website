---
authors:
- Fabien Goblet
categories:
- article
date: 2008-11-02 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- Google Earth
- marqueurs
title: 4. Marqueurs et événements
---

# 4. Marqueurs et événements


:calendar: Date de publication initiale : 02 novembre 2008


----





### Introduction




---


Il est possible à l'instar de l'API Google Maps de créer des marqueurs sur la carte et gérer des événements avec cette API.  



### Initialisation




---


Reprendre le globe du [deuxième tutoriel](http://www.geotribu.net/node/53).  



### Processus




---


Ajouter le contrôle de la navigation - en mode automatique :  

`ge.getNavigationControl().setVisibility(ge.VISIBILITY_AUTO);`  

Créer et paramétrer une vue :  

`var camera = ge.createLookAt('');  

camera.set(43.6,1.44949866510018,2860,ge.ALTITUDE_RELATIVE_TO_GROUND,190,75,10000);  

ge.getView().setAbstractView(camera);`  

Définir des icônes personnalisées - par défaut et au survol de la souris - pour les marqueurs :  

`map = ge.createStyleMap('styleMap');
normal = ge.createIcon('');  

normal.setHref('http://maps.google.com/mapfiles/kml/shapes/triangle.png');  

iconNormal = ge.createStyle('styleIconNormal');  

iconNormal.getIconStyle().setIcon(normal);


highlight = ge.createIcon('');  

highlight.setHref('http://maps.google.com/mapfiles/kml/shapes/square.png');  

iconHighlight = ge.createStyle('styleIconHighlight');  

iconHighlight.getIconStyle().setIcon(highlight);


map.setNormalStyleUrl('#styleIconNormal');  

map.setHighlightStyleUrl('#styleIconHighlight');`  

Définir les marqueurs :  

`var mirail = ge.createPlacemark('');
var mirail\_point = ge.createPoint('');  

mirail\_point.setLatitude(43.57825178577821);  

mirail\_point.setLongitude(1.40247810866353);  

mirail.setName('Université Toulouse Le Mirail');  

mirail.setGeometry(mirail\_point);`  

Affecter les icônes personnalisées aux marqueurs :  

`mirail.setStyleSelector(null);  

mirail.setStyleUrl('#styleMap');`  

Créer un événement lors d'un clic sur un marqueur - ici l'ouverture d'une infobulle contenant une image cliquable :  

`google.earth.addEventListener(mirail, "click", function(event) {  

event.preventDefault();  

var balloon = ge.createHtmlDivBalloon('');  

balloon.setFeature(mirail);  

var div = document.createElement('DIV');  

div.innerHTML = '![](http://www.univ-tlse2.fr/images/utm/bandeau_011.jpg)';  

balloon.setContentDiv(div);  

ge.setBalloon(balloon);  

});`  



### Code complet




---


`[Google Earth] 4. Marqueurs et événements

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

map = ge.createStyleMap('styleMap');

normal = ge.createIcon('');
normal.setHref('http://maps.google.com/mapfiles/kml/shapes/triangle.png');
iconNormal = ge.createStyle('styleIconNormal');
iconNormal.getIconStyle().setIcon(normal);

highlight = ge.createIcon('');
highlight.setHref('http://maps.google.com/mapfiles/kml/shapes/square.png');
iconHighlight = ge.createStyle('styleIconHighlight');
iconHighlight.getIconStyle().setIcon(highlight);

map.setNormalStyleUrl('#styleIconNormal');
map.setHighlightStyleUrl('#styleIconHighlight');

var mirail = ge.createPlacemark('');

var mirail\_point = ge.createPoint('');
mirail\_point.setLatitude(43.57825178577821);
mirail\_point.setLongitude(1.40247810866353);
mirail.setName('Université Toulouse Le Mirail');
mirail.setGeometry(mirail\_point);

mirail.setStyleSelector(null);
mirail.setStyleUrl('#styleMap');

google.earth.addEventListener(mirail, "click", function(event) {
event.preventDefault(); 
var balloon = ge.createHtmlDivBalloon('');
balloon.setFeature(mirail);
var div = document.createElement('DIV');
div.innerHTML = '<img src="http://www.univ-tlse2.fr/images/utm/bandeau\_011.jpg" onclick="window.open(\'http://www.univ-tlse2.fr\')">';
balloon.setContentDiv(div);
ge.setBalloon(balloon);
});

var ensat = ge.createPlacemark('');
var ensat\_point = ge.createPoint('');
ensat\_point.setLatitude(43.53511064424029);
ensat\_point.setLongitude(1.493182079733259);
ensat.setName('ENSAT');
ensat.setGeometry(ensat\_point);

ensat.setStyleSelector(null);
ensat.setStyleUrl('#styleMap');

google.earth.addEventListener(ensat, "click", function(event) {
event.preventDefault(); 
var balloon = ge.createHtmlDivBalloon('');
balloon.setFeature(ensat);
var div = document.createElement('DIV');
div.innerHTML = '<img src="http://www.ensat.fr/images/ensat\_r2\_c3.jpg" onclick="window.open(\'http://www.ensat.fr\')">';
balloon.setContentDiv(div);
ge.setBalloon(balloon);
});

ge.getFeatures().appendChild(mirail);
ge.getFeatures().appendChild(ensat);

var camera = ge.createLookAt('');
camera.set(43.6,1.44949866510018,2860,ge.ALTITUDE\_RELATIVE\_TO\_GROUND,190,75,10000);
ge.getView().setAbstractView(camera);
}`  



### Démonstration




---






[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto4.html)


### Remarques




---


La méthode event.preventDefault(); permet de s'affranchir des événements proposés par défaut par l'API. Ici la création d'un marqueur et de la définition de son nom - object.setName('nom') - instanciait déjà une ouverture d'infobulle lors d'un clic sur le marqueur. On surcharge donc cette propriété.
Il est possible d'utiliser la classe GEHtmlStringBalloon à la place de la classe GEHtmlDivBalloon utilisée ici.


### Conclusion




---


De la même manière que l'API Google Maps, il est possible de créer des marqueurs, de modifier leurs icônes et de créer des événements lors d'un clic à la souris.
La gallerie de démonstration - <http://code.google.com/apis/earth/documentation/demogallery.html> - et l'API Reference - <http://code.google.com/apis/earth/documentation/reference/> - sont nécessaires pour bien comprendre les éléments mis en jeu.


**Auteur : Fabien - fabien.goblet [ at ] gmail.com**




----

## Auteur

--8<-- "content/team/fgob.md"
