---
title: "Bientôt une nouvelle fonctionnalité pour OpenStreetMap, la création de cartes statiques"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-07-21
description: "Bientôt une nouvelle fonctionnalité pour OpenStreetMap, la création de cartes statiques"
tags:
    - open source
    - OpenStreetMap
---

# Bientôt une nouvelle fonctionnalité pour OpenStreetMap, la création de cartes statiques

:calendar: Date de publication initiale : 21 juillet 2009

![logo OpenStreetMap](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/Openstreetmap.png "logo OpenStreetMap"){: .img-thumbnail-left }

Le [Google Summer of Code](https://fr.wikipedia.org/wiki/Google_Summer_of_Code) (GSoC) est un programme annuel, fondé sur une logique de mécénat, visant à promouvoir le développement du logiciel libre. Pour cela différents projets sont sélectionnés par Google afin d'être développés durant la période estivale.

La possibilité de créer, **à partir d'une URL**, une **carte statique** des données d'OpenStreetMap fait partie des projets retenus pour le [GSoc de 2009](http://socghop.appspot.com/student_project/show/google/gsoc2009/openstreetmap/t124023144019) (plus d'informations également sur le [wiki](https://wiki.openstreetmap.org/wiki/GSoC_Applications_2009#Static_Maps_API)).

L'[API](http://dev.openstreetmap.org/~pafciu17/) de cette nouvelle fonctionnalité est depuis peu en ligne, le but étant pour les développeurs de recueillir les avis des utilisateurs afin d'enrichir ou de modifier celle-ci. Vous pouvez faire remonter vos remarques en utilisant l'adresse suivante : `osm.static.maps.api(at)gmail.com`.

Concrètement comment cela se passe ? Pour ceux qui ont débuté le WebMapping avec le CGI de MapServer, c'est exactement la même chose. En effet, au moyen d'une **URL standardisée** et de paramètres définis vous interrogez le serveur distant qui vous retourne alors l'image correspondante :

<http://dev.openstreetmap.org/~pafciu17?module=map&center=55.027084,24.999439&zoom=10&type=mapnik&width=400&height=200>  

> A l'heure où j'écris ce billet la carte qui est retournée peut être construite à partir :

* d'un point central, d'une hauteur, d'une largeur et d'un niveau de zoom :  
[http://dev.openstreetmap.org/~pafciu17/?module=map&center=0,51&zoom=7&wi...](http://dev.openstreetmap.org/~pafciu17/?module=map&center=0,51&zoom=7&width=400&height=400)
* d'une extension géographique (bouding box) et d'un niveau de zoom :  
<http://dev.openstreetmap.org/~pafciu17/?module=map&bbox=0,70,40,50&zoom=4>
* d'une extension géographique, et d'une hauteur ou d'une largeur :  
[http://dev.openstreetmap.org/~pafciu17/?module=map&bbox=0,70,40,50&width...](http://dev.openstreetmap.org/~pafciu17/?module=map&bbox=0,70,40,50&width=300)  
[http://dev.openstreetmap.org/~pafciu17/?module=map&bbox=0,70,40,50&heigh...](http://dev.openstreetmap.org/~pafciu17/?module=map&bbox=0,70,40,50&height=300)  
[http://dev.openstreetmap.org/~pafciu17/?module=map&bbox=0,70,40,50&width...](http://dev.openstreetmap.org/~pafciu17/?module=map&bbox=0,70,40,50&width=300&height=400)

> Les attributs qui peuvent être ajoutés à l'URL sont :

* **type** - filtre les données selon le type désiré (mapnik, cycle, osmrender).  
[http://dev.openstreetmap.org/~pafciu17/?module=map&type=mapnik&bbox=0,70...](http://dev.openstreetmap.org/~pafciu17/?module=map&type=mapnik&bbox=0,70,40,50&width=300&height=300)
* **imgType** - spécifie le format de sortie (png, gif, jpg).  
[http://dev.openstreetmap.org/~pafciu17/?module=map&imgType=gif&type=mapn...](http://dev.openstreetmap.org/~pafciu17/?module=map&imgType=gif&type=mapnik&bbox=-30,30,0,0&width=300&height=300)
* **center** - coordonnées (longitude/latitude) du point central de la carte :  
[http://dev.openstreetmap.org/~pafciu17/?module=map&center=180,20&zoom=2&...](http://dev.openstreetmap.org/~pafciu17/?module=map&center=180,20&zoom=2&width=1200&height=1200)
* **lon** et **lat** - une seconde manière de spécifier les coordonnées centrale de la carte :  
[http://dev.openstreetmap.org/~pafciu17/?module=map&lon=180&lat=20&zoom=2...](http://dev.openstreetmap.org/~pafciu17/?module=map&lon=180&lat=20&zoom=2&width=1200&height=1200)
* **zoom** - niveau de zoom de la carte
* **bbox** - spécifie l'extension géographique de la carte. Celle-ci est définie par les coordonnées géographiques des coins haut/gauche, haut/droit, bas/gauche et bas/droit :  
[http://dev.openstreetmap.org/~pafciu17/?module=map&bbox=-80,50,-50,10&wi...](http://dev.openstreetmap.org/~pafciu17/?module=map&bbox=-80,50,-50,10&width=300)
* **width** et **height** - hauteur et largeur de la carte :
* **points** - Coordonnées du/des points qui seront ajoutés, sous forme graphique, à la carte. Chaque point est constitué d'une longitude et d'une latitude :  
[http://dev.openstreetmap.org/~pafciu17/?module=map&points=-74,40.34,-82....](http://dev.openstreetmap.org/~pafciu17/?module=map&points=-74,40.34,-82.3,23.1&bbox=-80,50,-67,15&width=500)
* **paths** - Coordonnées du/des tracés qui seront ajoutés, sous forme graphique, à la carte. Les différents tracés sont séparés par un point-virgule (voir image ci-dessous) :  
[http://dev.openstreetmap.org/~pafciu17/?module=map&paths=-74,40.43,-82.3...](http://dev.openstreetmap.org/~pafciu17/?module=map&paths=-74,40.43,-82.3,23.1,-85,35,-87.2,32.12;-90,40,-80,40&bbox=-100,45,-67,5&width=600)
* **color** - Couleur des graphiques qui seront ajoutés à la carte :  
[http://dev.openstreetmap.org/~pafciu17/?module=map&points=-74,40.34,-82....](http://dev.openstreetmap.org/~pafciu17/?module=map&points=-74,40.34,-82.3,23.1&color=150,0,0&bbox=-80,50,-67,15&width=500)
* **reload** - force le rechargement des tuiles depuis le serveur plutôt que d'utiliser le cache :
* **logoPos** - spécifie la position du logo d'OSM. Quatre valeurs sont possibles (leftUpCorner, leftDownCorne, rightUpCorner, rightDownCorner):  
[http://dev.openstreetmap.org/~pafciu17?module=map&logoPos=leftUpCorner&c...](http://dev.openstreetmap.org/~pafciu17?module=map&logoPos=leftUpCorner&center=-120,50&zoom=5&width=300&height=300)

**Exemple d'utilisation de l'API static d'OSM avec génération d'un tracé :**

![Carte statique OSM](http://dev.openstreetmap.org/~pafciu17/?module=map&paths=-74,40.43,-82.3,23.1,-85,35,-87.2,32.12;-90,40,-80,40&bbox=-100,45,-67,5&width=600 "Carte statique OSM"){: .img-center loading=lazy }

Même si un service similaire existe déjà chez Google depuis quelque temps ([Google Map Static](http://code.google.com/apis/maps/documentation/staticmaps/)), le travail réalisé par ces étudiants ouvre de nouvelles voies quant à l'utilisation des données d'Open Street Map notamment pour la mise en place d'application mobile web.

----

Autre ressource :

[mapperz blogspot](http://mapperz.blogspot.com/2009/07/open-street-map-static-api-development.html)

----

<!-- geotribu:authors-block -->
