---
title: "Allégez votre librairie OpenLayers avec openlayerer"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-09-30
description: "Allégez votre librairie OpenLayers avec openlayerer"
tags:
    - JavaScript
    - open source
    - OpenLayers
---

# Allégez votre librairie OpenLayers avec openlayerer

:calendar: Date de publication initiale : 30 septembre 2010

![Logo OpenLayers](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/openlayers.png "Logo OpenLayers"){: .img-thumbnail-left }

Bien qu'[OpenLayers](https://openlayers.org/) ne fasse pas partie des librairies les plus lourdes, ce n'est pas une raison pour ne pas faire la chasse au kilos octets ! N'oubliez pas que tout le monde ne dispose pas encore forcément d'une bande passante suffisante. C'est pourquoi, il est préférable de ne charger que les fichiers nécessaires. Lors d'un [précédent tutoriel](http://geotribu.net/node/52), nous avions expliqué comment utiliser l'outil builder.py fourni avec OpenLayers. Ce dernier vous permet de créer votre propre librairie en spécifiant les classes que vous utiliserez. Néanmoins, bien que son utilisation soit très simple, une interface graphique serait tout de même plus agréable non ? Si vous partagez cet avis, je vous propose de vous rendre sur le site [openlayerer](http://openlayerer.appspot.com/)

Grâce à celui-ci, vous pourrez sélectionner les différentes classes que vous jugez nécessaires puis générer le fichier JavaScript correspondant. Notez qu'il existe une version spécifique à OpenStreetMap ne contenant que le strict minimum. A titre de comparaison, on passe tout de même d'un fichier initial pesant 13 575 ko à un fichier de 315ko (pour la version OpenStreetMap)... Je vous laisse le soin d'en tirer les conclusions qui s'imposent. Néanmoins, cet outil n'est pas disponible pour la dernière version d'OpenLayers (2.10) seule la 2.9.1 est prise en compte.

[![OpenLayerer](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/openlayerer.png "OpenLayerer"){: .img-center loading=lazy }](http://openlayerer.appspot.com/)

----

<!-- geotribu:authors-block -->
