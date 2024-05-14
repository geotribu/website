---
title: 4. Marqueurs et événements
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-11-02
description: 4. Marqueurs et événements
image: ''
license: default
robots: index, follow
tags:
    - Google Earth
    - marqueurs
---

# 4. Marqueurs et événements

:calendar: Date de publication initiale : 02 novembre 2008

## Introduction

![logo Google Earth](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/googleearth.png "logo Google Earth"){: .img-thumbnail-left }

Il est possible à l'instar de l'API Google Maps de créer des marqueurs sur la carte et gérer des événements avec cette API.  

## Initialisation

Reprendre le globe du [deuxième tutoriel](2008-11-02_2-ajoutons-quelques-controles.md).  

## Processus

Ajouter le contrôle de la navigation - en mode automatique :  

```javascript
ge.getNavigationControl().setVisibility(ge.VISIBILITY_AUTO);
```  

Créer et paramétrer une vue :  

```javascript
var camera = ge.createLookAt('');
camera.set(43.6,1.44949866510018,2860,ge.ALTITUDE_RELATIVE_TO_GROUND,190,75,10000);
ge.getView().setAbstractView(camera);
```  

Définir des icônes personnalisées - par défaut et au survol de la souris - pour les marqueurs :  

```javascript
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
```  

Définir les marqueurs :  

```javascript
var mirail = ge.createPlacemark('');

var mirail_point = ge.createPoint('');
mirail_point.setLatitude(43.57825178577821);
mirail_point.setLongitude(1.40247810866353);
mirail.setName('Université Toulouse Le Mirail');
mirail.setGeometry(mirail_point);
```

Affecter les icônes personnalisées aux marqueurs :  

```javascript
mirail.setStyleSelector(null);
mirail.setStyleUrl('#styleMap');
```

Créer un événement lors d'un clic sur un marqueur - ici l'ouverture d'une infobulle contenant une image cliquable :  

```javascript
google.earth.addEventListener(mirail, "click", function(event) {
  event.preventDefault();
  var balloon = ge.createHtmlDivBalloon('');
  balloon.setFeature(mirail);
  var div = document.createElement('DIV');
  div.innerHTML = '<img src="http://www.univ-tlse2.fr/images/utm/bandeau_011.jpg" onclick="window.open(\'http://www.univ-tlse2.fr\')">';
  balloon.setContentDiv(div);
  ge.setBalloon(balloon);
});
```  

## Code complet

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
  <head>
    <title>[Google Earth] 4. Marqueurs et événements</title>
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
        ge.getNavigationControl().setVisibility(ge.VISIBILITY_SHOW);

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

        var mirail_point = ge.createPoint('');
        mirail_point.setLatitude(43.57825178577821);
        mirail_point.setLongitude(1.40247810866353);
        mirail.setName('Université Toulouse Le Mirail');
        mirail.setGeometry(mirail_point);

        mirail.setStyleSelector(null);
        mirail.setStyleUrl('#styleMap');

        google.earth.addEventListener(mirail, "click", function(event) {
          event.preventDefault();
          var balloon = ge.createHtmlDivBalloon('');
          balloon.setFeature(mirail);
          var div = document.createElement('DIV');
          div.innerHTML = '<img src="http://www.univ-tlse2.fr/images/utm/bandeau_011.jpg" onclick="window.open(\'http://www.univ-tlse2.fr\')">';
          balloon.setContentDiv(div);
          ge.setBalloon(balloon);
       });

       var ensat = ge.createPlacemark('');
       var ensat_point = ge.createPoint('');
       ensat_point.setLatitude(43.53511064424029);
       ensat_point.setLongitude(1.493182079733259);
       ensat.setName('ENSAT');
       ensat.setGeometry(ensat_point);

       ensat.setStyleSelector(null);
       ensat.setStyleUrl('#styleMap');

       google.earth.addEventListener(ensat, "click", function(event) {
         event.preventDefault();
         var balloon = ge.createHtmlDivBalloon('');
         balloon.setFeature(ensat);
         var div = document.createElement('DIV');
         div.innerHTML = '<img src="http://www.ensat.fr/images/ensat_r2_c3.jpg" onclick="window.open(\'http://www.ensat.fr\')">';
         balloon.setContentDiv(div);
         ge.setBalloon(balloon);
       });

       ge.getFeatures().appendChild(mirail);
       ge.getFeatures().appendChild(ensat);

       var camera = ge.createLookAt('');
       camera.set(43.6,1.44949866510018,2860,ge.ALTITUDE_RELATIVE_TO_GROUND,190,75,10000);
       ge.getView().setAbstractView(camera);
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

## Démonstration

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="https://web.archive.org/web/20120113071734/http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto4.html" width="100%" height="700px"></iframe>`

[Résultat pleine page](https://web.archive.org/web/20120113071734/http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto4.html)

## Remarques

La méthode event.preventDefault(); permet de s'affranchir des événements proposés par défaut par l'API. Ici la création d'un marqueur et de la définition de son nom - object.setName('nom') - instanciait déjà une ouverture d'infobulle lors d'un clic sur le marqueur. On surcharge donc cette propriété.
Il est possible d'utiliser la classe GEHtmlStringBalloon à la place de la classe GEHtmlDivBalloon utilisée ici.

----

## Conclusion

De la même manière que l'API Google Maps, il est possible de créer des marqueurs, de modifier leurs icônes et de créer des événements lors d'un clic à la souris.
La gallerie de démonstration - [http://code.google.com/apis/earth/documentation/demogallery.html](http://code.google.com/apis/earth/documentation/demogallery.html) - et l'API Reference - [http://code.google.com/apis/earth/documentation/reference/](http://code.google.com/apis/earth/documentation/reference/) - sont nécessaires pour bien comprendre les éléments mis en jeu.

----

<!-- geotribu:authors-block -->
