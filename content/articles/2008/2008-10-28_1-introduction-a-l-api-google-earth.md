---
title: 1. Introduction à l'API Google Earth
authors:
    - Fabien Goblet
categories:
    - article
    - tutoriel
comments: true
date: 2008-10-28
description: 1. Introduction à l'API Google Earth
image: ''
license: default
robots: index, follow
tags:
    - Google Earth
---

# 1. Introduction à l'API Google Earth

:calendar: Date de publication initiale : 28 octobre 2008

## Introduction

![logo Google Earth](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/googleearth.png "logo Google Earth"){: .img-thumbnail-left }

A l'instar de l'API Google Maps, Google propose également une API pour manipuler Google Earth dans une page Internet.  

## Processus

Pour afficher la carte, il est nécessaire de fournir l'url de l'API Google Earth - la même que pour l'API Google Maps :  

```html
<script src="http://www.google.com/jsapi?key=ABQIAAAAPo34DyTbdo2RpVUvdvK1qxTVkAM76o12Ue_ZZqmwjROaqOyBLhQVBCYY9lnsLXH3mdZLo-PWW8Z1DQ"></script>
```

Il faut déclarer dans le corps de la page deux blocs `div` imbriqués où sera placée la carte, on définit les attributs de style pour que la carte prenne toute la taille de la page :  

```html
<div id='map3d_container' style='border: 0px solid silver; height: 100%; width: 100%;'>
  div id='map3d' style='height: 100%;'div>
</div>
```

Et il faut déclarer l'appel à la fonction de construction de la carte dans la déclaration de la balise :  

```html
<body onload='init()' id='body'>
```

Nous déclarons ensuite le code Javascript qui permet de construire le globe :  

```javascript
google.load("earth", "1");
var ge = null;

function init() {
  google.earth.createInstance("map3d", initCallback);
}

function initCallback(object) {
  ge = object;
  ge.getWindow().setVisibility(true);
}
```

La fonction `init()` crée l'instance Google Earth.  

La fonction `initCallback(object)` crée l'objet carte et définit ses options.  

## Code complet

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
  <title>[Google Earth] 1. Introduction à l'API Google Earth</title>
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
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto1.html" width="100%" height="700px"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto1.html)

## Remarques

L'intégration de Google Earth se fait de manière très simple à l'intérieur d'un navigateur.
Je vous encourage vivement à visiter le site officiel de l'API Google Earth pour de plus amples imformations - [http://code.google.com/apis/earth/](http://code.google.com/apis/earth/)

## Conclusion

La création d'une simple carte en 3D et l'intégration de celle-ci dans une page Internet est très facile.
Cependant dans celle-ci, la navigation n'est pas aisée.
Nous verrons par la suite comment enrichir l'interface pour pouvoir naviguer dans la carte et comment ajouter des informations sur cette dernière.
Il est nécessaire de télécharger un plugin pour faire fonctionner cette API - elle n'est disponible que pour Firefox, IE6 et IE7, et uniquement sous Windows.

----

<!-- geotribu:authors-block -->
