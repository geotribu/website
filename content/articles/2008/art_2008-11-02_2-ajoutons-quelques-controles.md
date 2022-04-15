---
authors:
- Fabien Goblet
categories:
- article
date: 2008-11-02 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- Google Earth
- contrôles
title: 2. Ajoutons quelques contrôles
---

# 2. Ajoutons quelques contrôles


:calendar: Date de publication initiale : 02 novembre 2008


----





### Introduction




---


Ce deuxième tutoriel reprend le globe défini dans le [premier tutoriel](http://www.geotribu.net/node/49) en lui ajoutant des éléments de contrôle.  



### Initialisation




---


Reprendre le globe défini dans le [premier tutoriel](http://www.geotribu.net/node/49).  



### Processus




---


Ajouter quelques contrôles à la carte - navigation à la souris, contrôles de zoom et de directions, grille, carte générale et légende :  

`ge.getOptions().setMouseNavigationEnabled(true);  

ge.getNavigationControl().setVisibility(ge.VISIBILITY_SHOW);  

ge.getOptions().setGridVisibility(true);  

ge.getOptions().setStatusBarVisibility(true);  

ge.getOptions().setOverviewMapVisibility(true);  

ge.getOptions().setScaleLegendVisibility(true);`  



### Code complet




---


`[Google Earth] 2. Ajoutons quelques contrôles

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
ge.getOptions().setMouseNavigationEnabled(true);
ge.getNavigationControl().setVisibility(ge.VISIBILITY\_SHOW);
ge.getOptions().setGridVisibility(true);
ge.getOptions().setStatusBarVisibility(true);
ge.getOptions().setOverviewMapVisibility(true);
ge.getOptions().setScaleLegendVisibility(true);
}`  



### Démonstration




---






[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto2.html)


### Remarques




---


L'ajout de contrôle et d'informations sur la carte se fait de manière très simple en utilisant les méthodes de l'API.
L'API est disponible à cette adresse : <http://code.google.com/apis/earth/documentation/reference/index.html>


### Conclusion




---


Ajouter quelques options à la carte est très simple.
Maintenant que les options de contrôle et de navigation sont ajoutées à la carte, nous verrons par la suite comment ajouter des informations sur la carte.
L'utilisation des boutons de navigation est exactement la même que le logiciel Google Earth - vous ne serez pas perdu.


**Auteur : Fabien - fabien.goblet [ at ] gmail.com**




----

## Auteur

--8<-- "content/team/fgob.md"
