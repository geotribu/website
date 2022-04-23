---
title: "1. Introduction à l'API Google Maps"
authors:
    - Fabien Goblet
categories:
    - article
date: 2008-08-22
description: "1. Introduction à l'API Google Maps"
tags:
    - Google Maps
---

# 1. Introduction à l'API Google Maps

:calendar: Date de publication initiale : 22 août 2008

:warning: L'API Google Maps v2 est dépréciée depuis le 19 mai 2010.

## Introduction

L'[API Google Maps](http://code.google.com/intl/fr/apis/maps/) permet d'intégrer une carte semblable à [celle de Google](http://maps.google.fr/maps?hl=fr&tab=wl) dans ses pages Web en utilisant un peu de Javascript.

## Appel à l'API grâce à la clé

Pour utiliser l'API Google Maps, il est nécessaire d'obtenir une clé gratuite à cette adresse (link is external). Et d'écrire cette ligne dans le de la page HTML qui contiendra la carte Google Maps :  

- v=2.x : ici on note la version de l'API utilisée dans notre projet : - 2.x correspond à la dernière version de l'API - 2.s correspond à la dernière version stable de l'API - 2 correspond à la version courante Détail des changements de l'API : [http://mapki.com/wiki/Changelog](http://mapki.com/wiki/Changelog)

NB : Nous utiliserons par la suite toujours la version courante de l'API afin d'éviter les mauvaises surprises.

## Code Javascript de déclaration de la carte

Nous déclarons la fonction initialize() qui sera chargée lors du chargement de la page Web. Cette fonction contient les instructions afin de déclarer la carte Google Maps. La structure conditionnelle 'if then else' permet d'alerter l'utilisateur si son navigateur n'accepte pas le JavaScript grâce à la fonction GBrowserIsCompatible(). Nous déclarons ensuite l'objet map qui sera affiché dans le bloc dont l'identifiant sera 'map_canvas' de la page HTML :

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
<div id="map_canvas"></div>
```

Et il faut appeler la fonction initialize() lors du chargement de la page :   La fonction GUnload() permet de libérer la mémoire lorsque l'on quitte la page Web.

## Code complet

```
```

## Démonstration

<iframe src="http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto1.html" height="350px" width="100%"></iframe>

----

## Auteur {: data-search-exclude }

--8<-- "content/team/fgob.md"
