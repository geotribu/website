---
title: 2. Ajoutons quelques contrôles
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-11-02
description: 2. Ajoutons quelques contrôles
image: ''
license: default
robots: index, follow
tags:
    - contrôles
    - Google Earth
---

# 2. Ajoutons quelques contrôles

:calendar: Date de publication initiale : 02 novembre 2008

## Introduction

![logo Google Earth](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/googleearth.png "logo Google Earth"){: .img-thumbnail-left }

Ce deuxième tutoriel reprend le globe défini dans le [premier tutoriel](2008-10-28_1-introduction-a-l-api-google-earth.md) en lui ajoutant des éléments de contrôle.  

## Initialisation

Reprendre le globe défini dans le [premier tutoriel](2008-10-28_1-introduction-a-l-api-google-earth.md).  

## Processus

Ajouter quelques contrôles à la carte - navigation à la souris, contrôles de zoom et de directions, grille, carte générale et légende :  

```javascript
ge.getOptions().setMouseNavigationEnabled(true);  
ge.getNavigationControl().setVisibility(ge.VISIBILITY_SHOW);  
ge.getOptions().setGridVisibility(true);  
ge.getOptions().setStatusBarVisibility(true);  
ge.getOptions().setOverviewMapVisibility(true);  
ge.getOptions().setScaleLegendVisibility(true);
```  

## Code complet

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html>
<head>
  <title>[Google Earth] 2. Ajoutons quelques contrôles</title>
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
  ge.getOptions().setGridVisibility(true);
  ge.getOptions().setStatusBarVisibility(true);
  ge.getOptions().setOverviewMapVisibility(true);
  ge.getOptions().setScaleLegendVisibility(true);
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
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto2.html" width="100%" height="700px"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto2.html)

## Remarques

L'ajout de contrôle et d'informations sur la carte se fait de manière très simple en utilisant les méthodes de l'API.
L'API est disponible à cette adresse : <http://code.google.com/apis/earth/documentation/reference/index.html>

## Conclusion

Ajouter quelques options à la carte est très simple.
Maintenant que les options de contrôle et de navigation sont ajoutées à la carte, nous verrons par la suite comment ajouter des informations sur la carte.
L'utilisation des boutons de navigation est exactement la même que le logiciel Google Earth - vous ne serez pas perdu.

----

<!-- geotribu:authors-block -->
