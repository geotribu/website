---
title: 3. La Tour Eiffel en 3D
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-11-02
description: 3. La Tour Eiffel en 3D
image: ''
license: default
robots: index, follow
tags:
    - 3D
    - Google Earth
    - tour eiffel
---

# 3. La Tour Eiffel en 3D

:calendar: Date de publication initiale : 02 novembre 2008

## Introduction

![logo Google Earth](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/googleearth.png "logo Google Earth"){: .img-thumbnail-left }

Il est possible d'afficher les couches 'bâtiments' présentes dans Google Earth dans l'API et donc dans sa propre page Internet.  

Nous verrons ici comment afficher la tour Eiffel et comment définir par défaut les paramètres de vue.  

## Initialisation

Reprendre le globe du [tutoriel n°2](2008-11-02_2-ajoutons-quelques-controles.md).  

## Processus

Ajouter le contrôle de la navigation - en mode automatique :  

```javascript
ge.getNavigationControl().setVisibility(ge.VISIBILITY_AUTO);
```

Créer une vue :  

```javascript
var eiffel = ge.createLookAt('');
```

Puis paramétrer cette vue - latitude, longitude, altitude de la caméra, comment l'altitude est gérée (ici 50 mètres au-dessus du niveau du sol), l'angle de la caméra par rapport au nord, l'inclinaison de la caméra et la distance de la caméra :  

```javascript
eiffel.set(48.858521049096, 2.29425080771864, 50, ge.ALTITUDE_RELATIVE_TO_GROUND, 250, 75, 1100);
```  

Positionnons la caméra dans la carte en 3D :  

```javascript
ge.getView().setAbstractView(eiffel);
```  

Et activons le mode 'Bâtiments en 3D' - les mêmes que dans e logiciel Google Earth :  

```javascript
ge.getLayerRoot().enableLayerById(ge.LAYER_BUILDINGS, true);
```

## Code complet

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN""http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
  <head>
    <title>[Google Earth] 2. Ajoutons quelques contr&ocirc;les</title>
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
        ge.getNavigationControl().setVisibility(ge.VISIBILITY_AUTO);
        var eiffel = ge.createLookAt('');
  eiffel.set(48.858521049096, 2.29425080771864, 50, ge.ALTITUDE_RELATIVE_TO_GROUND, 250, 75, 1100);
  ge.getView().setAbstractView(eiffel);

        ge.getLayerRoot().enableLayerById(ge.LAYER_BUILDINGS, true);
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
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto3.html" width="100%" height="700px"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto3.html)

## Remarques

Les bâtiments en France sont encore peu nombreux, mais il y a en aura de plus en plus.
L'API - <http://code.google.com/apis/earth/documentation/reference/index.html> - est à mettre en relation avec les informations de référence des objets KML - <http://code.google.com/apis/kml/documentation/kmlreference.html> .

## Conclusion

Il est possible d'afficher les couches présentes dans Google Earth.
On peut déclarer une caméra, et agir dessus.

----

<!-- geotribu:authors-block -->
