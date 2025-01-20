---
title: 6. Afficher un objet en 3D
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-12-01
description: ''
image: ''
license: default
robots: index, follow
tags:
    - Google Earth
    - 3D
    - API
    - Sketchup
---

# 6. Afficher un objet en 3D

:calendar: Date de publication initiale : 01 décembre 2008

## Introduction

![logo Google Earth](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/googleearth.png "logo Google Earth"){: .img-thumbnail-left }

L'API Google Earth propose d'afficher dans son globe des objets en 3D provenant notamment de [Sketchup](http://sketchup.google.com/intl/fr/).  

## Initialisation

Reprendre la carte du tutoriel sur les marqueurs et les événements : [Tutoriel n°4](2008-11-02_4-marqueurs-et-evenements.md)

## Processus

Définir une fonction qui vérifie la validité du fichier KML :  

```javascript
function finished(object) {  
  if (!object) {  
    alert('KML mal formé');  
    return;  
  }  
  ge.getFeatures().appendChild(object);  
}
```

Définir l'objet géographique KML :  

```javascript
var kmlUrl = 'url du KML';
```

Et l'appliquer sur la carte :  

```javascript
google.earth.fetchKml(ge, kmlUrl, finished);
```

## Code complet

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
  <head>
    <title>[Google Earth] 6. Afficher un objet en 3D</title>
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

       var camera = ge.createLookAt('');
       camera.set(43.6,1.44949866510018,2860,ge.ALTITUDE_RELATIVE_TO_GROUND,190,75,10000);
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

### Démonstration

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto6.html" width="100%" height="700px"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto6.html)

## Remarques

L'affichage d'un objet 3D provenant de Sketchup se fait de la même façon qu'un fichier KML.

## Conclusion

Sketchup est un logiciel de création d'objets 3D, voir le [site officiel](http://sketchup.google.com/intl/fr/) pour plus d'informations.

**Merci à Jean-Hugues Puech pour son musée de Portet-sur-Garonne.**

----

<!-- geotribu:authors-block -->
