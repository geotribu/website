---
title: 14. Se promener place du Capitole
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-11-17
description: 14. Se promener place du Capitole
image: ''
tags:
    - Google Maps
    - Street View
---

# 14. Se promener place du Capitole

:calendar: Date de publication initiale : 17 novembre 2008

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-thumbnail-left }

Il est possible grâce à l'API Google Maps de naviguer virtuellement dans les rues, nous verrons ici comment implanter cette fonctionnalité.  

## Créer un panorama

Construire un panorama en lui indiquant son emplacement :  

```javascript
var myPano = new GStreetviewPanorama(document.getElementById("pano"));
```

Définir une destination :  

```javascript
var capitole = new GLatLng(43.60436298129637, 1.442950341024869);
```

Définir les attributs de la caméra - yaw pour la direction en degré de l'angle de vue et pitch l'inclinaison de la caméra :  

```javascript
var myPOV = {yaw:370.64659986187695,pitch:0};
```

Initialiser le panorama sur la destination et avec les paramètres de caméra :  

```javascript
myPano.setLocationAndPOV(capitole, myPOV);
```

Ajouter un événement (une alerte simple) si le navigateur ne supporte pas le Flash. :  

```javascript
GEvent.addListener(myPano, "error", handleNoFlash);
```

Définir l'événement :  

```javascript
function handleNoFlash(errorCode) {
  if (errorCode == 603) {
    alert("Flash n'est pas supporté par votre navigateur !");
    return;
  }
}
```

Définir l'emplacement de la carte :  

```html
<div name="pano" id="pano"></div>
```

## Code complet

```html
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>
     [Google Maps] 14. Se promener place du Capitole
   </title>
   <style type="text/css">
     html { overflow:hidden; height:100%; }
     body { height:100%; margin:0; }
     #pano { width:100%; height:100%; }
   </style>
   <link rel="icon" type="image/png" href="./favicon.png"/>
   <script src="http://maps.google.com/maps?file=api&v=2&key=votre_clé_ici" type="text/javascript"></script>
   <script type="text/javascript">

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
     }
  </script>
  </head>
  <body onload="initialize()" onunload="GUnload()">
    <div name="pano" id="pano"></div>
   </body>
</html>
```

## Démonstration

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto14.html" height="350px" width="100%"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto14.html)

## Remarques

Un panorama StreetView est une image cliquable, 'zoomable' et avec lequel on peut se diriger vers les images mitoyennes.
L'application est en Flash, ce qui permet la navigation 'demi-sphérique' dans la photographie.

## Conclusion

Les panoramas de StreetView sont facilement exploitables grâce à l'API.
Il faut maintenant coupler la couche des photos sur la carte - <http://geotribu.net/node/65> - et les photographies.

----

<!-- geotribu:authors-block -->
