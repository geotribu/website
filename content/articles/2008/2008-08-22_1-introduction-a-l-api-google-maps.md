---
title: "1. Introduction à l'API Google Maps"
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-08-22
description: "1. Introduction à l'API Google Maps"
tags:
    - Google Maps
---

# 1. Introduction à l'API Google Maps

:calendar: Date de publication initiale : 22 août 2008

:warning: L'API Google Maps v2 est dépréciée depuis le 19 mai 2010.

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-thumbnail-left }

L'[API Google Maps](http://code.google.com/intl/fr/apis/maps/) permet d'intégrer une carte semblable à [celle de Google](http://maps.google.fr/maps?hl=fr&tab=wl) dans ses pages Web en utilisant un peu de Javascript.

## Appel à l'API grâce à la clé

Pour utiliser l'API Google Maps, il est nécessaire d'obtenir une clé gratuite à cette [adresse](http://code.google.com/intl/fr/apis/maps/signup.html). Et d'écrire cette ligne dans le de la page HTML qui contiendra la carte Google Maps :  

- v=2.x : ici on note la version de l'API utilisée dans notre projet :
    - 2.x correspond à la dernière version de l'API
    - 2.s correspond à la dernière version stable de l'API
    - 2 correspond à la version courante Détail des changements de l'API : [http://mapki.com/wiki/Changelog](http://mapki.com/wiki/Changelog)

NB : Nous utiliserons par la suite toujours la version courante de l'API afin d'éviter les mauvaises surprises.

## Code Javascript de déclaration de la carte

Nous déclarons la fonction `initialize()` qui sera chargée lors du chargement de la page Web. Cette fonction contient les instructions afin de déclarer la carte Google Maps. La structure conditionnelle 'if then else' permet d'alerter l'utilisateur si son navigateur n'accepte pas le JavaScript grâce à la fonction `GBrowserIsCompatible()`. Nous déclarons ensuite l'objet map qui sera affiché dans le bloc dont l'identifiant sera 'map_canvas' de la page HTML :

```javascript
var map = new GMap2(document.getElementById('map'));
```

et définissons un centre et un niveau de zoom pour cet objet.

```javascript
map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),15);
```

## Code HTML

Afin d'afficher la carte, il est nécessaire de déclarer un bloc div qui contiendra la carte :

```html
<div id="map"></div>
```

Et il faut appeler la fonction `initialize()` lors du chargement de la page :

```html
<body onload="initialize()" onunload="GUnload()">
```

La fonction `GUnload()` permet de libérer la mémoire lorsque l'on quitte la page Web.

## Code complet

```html
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>
     [Google Maps] 1. Introduction à Google Maps
    </title>
 <style type="text/css">
   html { overflow:hidden; height:100%; }
   body { height:100%; margin:0; }
   #map { width:100%; height:100%; }
 </style>
    <script src="http://maps.google.com/maps?file=api&v=2.x&key=votre_clé_ici" type="text/javascript"></script>
    <script type="text/javascript">
      function initialize() {
        if (GBrowserIsCompatible()) {
          var map = new GMap2(document.getElementById('map'));
          map.setCenter(new GLatLng(43.57769664771851, 1.402821992034912),16);
        }
        else{
          alert('Désolé, mais votre navigateur n\'est pas compatible avec Google Maps');
        }
      }
    </script>
  </head>
  <body onload="initialize()" onunload="GUnload()">
    <div id="map"</div>
  </body>
</html>
```

## Démonstration

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto1.html" height="350px" width="100%"></iframe>`

[Résultat pleine page](http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto1.html)

----

<!-- geotribu:authors-block -->
