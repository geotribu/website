---
title: "5. Ajouter un fichier KML"
authors:
    - Fabien Goblet
categories:
    - article
date: 2008-11-02 10:20
description: "5. Ajouter un fichier KML"
image: ''
license: default
robots: index, follow
tags:
    - Google Earth
    - KML
---

# 5. Ajouter un fichier KML

:calendar: Date de publication initiale : 02 novembre 2008

----

## Prérequis

- Tutoriaux :
    - [1. Introduction à l'API Google Earth](/articles/2008/art_2008-11-02_2-ajoutons-quelques-controles/)
    - [2. Ajoutons quelques contrôles](/articles/2008/art_2008-11-02_2-ajoutons-quelques-controles/)
    - [4. Marqueurs et événements](/articles/2008/art_2008-11-02_4-marqueurs-et-evenements/)

- Connaissances :
    - notions de HTML, notions de JavaScript, notions d'algorithmique

- Liens :
    - <http://code.google.com/apis/earth/documentation/reference/index.html>

## Code

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
  <title>[Google Earth] 5. Ajouter un fichier KML</title>
  <script src="http://www.google.com/jsapi?key=ABQIAAAAPo34DyTbdo2RpVUvdvK1qxTVkAM76o12Ue_ZZqmwjROaqOyBLhQVBCYY9lnsLXH3mdZLo-PWW8Z1DQ"></script>
  <style type="text/css">
  html { overflow:hidden; height:100%; }
  body { height:100%; margin:0; }
</style>
<link rel="icon" type="image/png" href="./favicon.png"/>
<script>
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

function finished(object) {
if (!object) {
alert('KML mal formé');
return;
}
ge.getFeatures().appendChild(object);
}

var kmlUrl = 'http://88.191.39.115/fabien/geotribu/kml/route.kml';
google.earth.fetchKml(ge, kmlUrl, finished);

}
</script>
</head>
<body onload='init()' id='body'>
  <div id='map3d_container' style='border: 0px solid silver; height: 100%; width: 100%;'>
    <div id='map3d' style='height: 100%;'></div>
  </div>
</body>
</html>
```

## Processus

1. Reprendre la carte du tutoriel sur les marqueurs et les événements : <http://www.geotribu.net/?q=node/55>
2. Définir une fonction qui vérifie la validité du fichier KML :  

```javascript
function finished(object) {  
  if (!object) {  
    alert('KML mal formé');  
    return;  
  }  
  ge.getFeatures().appendChild(object);  
}
```

3. Définir l'objet géographique KML :  

```javascript
var kmlUrl = 'http://88.191.39.115/fabien/geotribu/kml/route.kml';
```

4. Et l'appliquer sur la carte :  

```javascript
google.earth.fetchKml(ge, kmlUrl, finished);
```

## Résultat

<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto5.html" width="100%" height="700px"></iframe>

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto5.html)

## Remarques

Ajouter un fichier KML est très simple. Il suffit de déclarer le fichier, vérifier qu'il soit bien formé, et l'ajouter à la carte.

## Conclusion

Si le fichier KML est mal formé, la fonction finished() renverra NULL et donc l'API ne chargera pas le fichier.
Cette vérification est nécessaire pour éviter de faire 'planter' la carte.

----

## Auteur {: data-search-exclude }

--8<-- "content/team/fgob.md"
