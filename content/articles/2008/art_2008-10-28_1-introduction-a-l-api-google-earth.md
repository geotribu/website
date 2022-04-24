---
authors:
    - Fabien Goblet
categories:
    - article
date: 2008-10-28 10:20
description: ""
image: ''
license: default
robots: index, follow
tags:
- tutoriel
- Google Earth
title: 1. Introduction à l'API Google Earth
---

# 1. Introduction à l'API Google Earth

:calendar: Date de publication initiale : 28 octobre 2008

----

### Introduction

---

A l'instar de l'API Google Maps, Google propose également une API pour manipuler Google Earth dans une page Internet.  

### Processus

---

Pour afficher la carte, il est nécessaire de fournir l'url de l'API Google Earth - la même que pour l'API Google Maps :  

Il faut déclarer dans le corps de la page deux blocs div imbriqués où sera placée la carte, on définit les attributs de style pour que la carte prenne toute la taille de la page :  

Et il faut déclarer l'appel à la fonction de construction de la carte dans la déclaration de la balise :  

Nous déclarons ensuite le code Javascript qui permet de construire le globe :  

`google.load("earth", "1");
var ge = null;

function init() {
google.earth.createInstance("map3d", initCallback);
}

function initCallback(object) {
ge = object;
ge.getWindow().setVisibility(true);
}`  

La fonction init() crée l'instance Google Earth.  

La fonction initCallback(object) crée l'objet carte et définit ses options.  

### Code complet

---

`[Google Earth] 1. Introduction à l'API Google Earth

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
}`  

### Démonstration

---

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto1.html)

### Remarques

---

L'intégration de Google Earth se fait de manière très simple à l'intérieur d'un navigateur.
Je vous encourage vivement à visiter le site officiel de l'API Google Earth pour de plus amples imformations - <http://code.google.com/apis/earth/>

### Conclusion

---

La création d'une simple carte en 3D et l'intégration de celle-ci dans une page Internet est très facile.
Cependant dans celle-ci, la navigation n'est pas aisée.
Nous verrons par la suite comment enrichir l'interface pour pouvoir naviguer dans la carte et comment ajouter des informations sur cette dernière.
Il est nécessaire de télécharger un plugin pour faire fonctionner cette API - elle n'est disponible que pour Firefox, IE6 et IE7, et uniquement sous Windows.

**Auteur : Fabien - fabien.goblet [ at ] gmail.com**

----

## Auteur

--8<-- "content/team/fgob.md"
