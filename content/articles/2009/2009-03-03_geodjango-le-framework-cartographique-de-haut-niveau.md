---
title: "GéoDjango LE framework cartographique de haut niveau"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-03-03
description: "GéoDjango LE framework cartographique de haut niveau"
tags:
    - GeoDjango
---

# GéoDjango LE framework cartographique de haut niveau

:calendar: Date de publication initiale : 03 mars 2009

![logo GeoDjango](https://cdn.geotribu.fr/img/logos-icones/programmation/geodjango.png){: .img-thumbnail-left }

Cette année et après avoir été bluffé par la quantité de programmes développés en **Python** je me suis décidé à apprendre ce langage. Naturellement, au lieu de ré-inventer la roue j'ai regardé les [frameworks](https://fr.wikipedia.org/wiki/Framework) existants. Je pense que je suis tombé sur LE FRAMEWORK, la killer application qui va me faire veiller tard durant ces prochains jours, [GeoDjango](http://geodjango.org/).

Basé sur [Django](http://www.django-fr.org/), un **framework python** permettant le développement rapide de site internet, GeoDjango apporte un niveau d'abstraction supplémentaire en autorisant une **gestion complète de toutes les composantes spatiales** d'un projet Cartogaphique Web. Vous pourrez ainsi facilement depuis l'interface d'administration (qui se base entre autre sur la librairie OGR/GDAL) :

* manipuler, consulter ou encore importer des données spatiales
* Dialoguer dans les standards du Web Géogaphique (KML, GML, WKT, WKB, GeoRSS, and GeoJSON)
* Reprojection, correction géométrique...

![description_geodjango.png](https://cdn.geotribu.fr/img/articles-blog-rdp/database/Django/description_geodjango.png){: .img-center loading=lazy }

Pas encore convaincu? Sachez alors que GeoDjango possède également un **module de geo-syndication** publiant automatiquement vos données au format (GeoRSS, Atom Feeds ou KML), qu'il devrait prochainement **intégrer directement un moteur cartogaphique** (MapServer ou manik) ou encore qu'il est Multi-plateforme (Linux, Windows, Mac OS X) et multi-database (PostGIS, Oracle, and MySQL). Je vais arrêter là car une page entière ne serait pas suffisante pour lister toutes ses fonctionnalités, néanmoins dans la partie [documentation](http://geodjango.org/presentations/) vous trouverez toutes les informations nécessaires.

Voici quelques exemples de sites réalisés avec Django :

![image_site.png](https://cdn.geotribu.fr/img/articles-blog-rdp/database/Django/image_site.png){: .img-center loading=lazy }

## Liens utiles

* [Site internet GeoDjango](http://geodjango.org/)  
* [Documentation de GeoDjango](http://geodjango.org/docs/)  
* [Présentation de GeoDjango](http://www.geowebguru.com/articles/99-overview-geodjango)  
* [On en parle sur NeoGeo Online](http://www.neogeo-online.net/blog/archives/tag/geodjango/)  
* [Et également sur GeoInWeb](http://www.geoinweb.com/2008/07/10/geodjangon-un-framework-web-gographique-session-de-la-confrence-where-20-2008-slection-n4/)

----

<!-- geotribu:authors-block -->
