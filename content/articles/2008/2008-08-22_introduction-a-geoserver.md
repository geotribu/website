---
title: "Introduction à GeoServer"
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-08-22
description: "Introduction à GeoServer"
tags:
    - GeoServer
---

# Introduction à GeoServer

:calendar: Date de publication initiale : 22 août 2008

> that through cooperation we can build something greater than any of us could alone ([tiré de la Philosophy de GeoServer](http://docs.codehaus.org/display/GEOSDOC/Introduction))

## Introduction

![logo GeoServer](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/geoserver.png "logo GeoServer"){: .img-thumbnail-left }

Cette introduction sur GeoServer se décompose en 3 parties. Après avoir retracé l'historique de celui-ci, nous nous attacherons à savoir pour qui ce genre d'outil est utile, et quel sont ces possibilités

## Qu'est ce que GeoServer

[GeoServer](http://docs.codehaus.org/display/GEOS/Home) est, comme son nom l'indique, un serveur cartographique (ou moteur cartographique) OpenSource (licence GPL 2.0) spécialisé dans la gestion d'information géographique (comme [MapServer](http://mapserver.gis.umn.edu/)).

Son développement initié par l'association "[The Open Planning Project (TOPP)](http://www.openplans.org/)" avait pour objectif de départ d'offrir une suite d'outils permettant de rendre la gestion de projet urbain plus transparente pour les citoyens. La philosophie principale de ce projet est de l'aveu même des créateurs tournée vers l' "Open Democraty". Terme que je traduirai par démocratie participative, plutôt que démocratie ouverte, car cela implique non seulement une ouverture et une transparence de cette démocratie, mais également une implication des citoyens qui sont les premiers acteurs de ce projet.

GeoServer a ensuite continué à évoluer, notamment en terme de respect des normes en suivant les préconisations de "l'Open Geospatial Consortium (OGC)" (en intégrant par exemple la norme WFS), mais également en ajoutant des modules supplémentaires en se basant sur la librairie [GéoTools](http://geotools.codehaus.org/) permettant ainsi l'intégration de données multi-source (ShapeFiles, Oracle, PostGis ...).

Nous en sommes aujourd'hui à la version 1.6.1, ce qui indique une certaine maturité du projet. Il faut souligner également que la librairie (GeoTools) sur laquelle se base GeoServer est utilisé par de nombreux autres logiciels (uDig, gvSIG...), ce qui permet une complète intégration des diverses facettes du SIG tout en permettant de disposer d'une base technique commune.

## A qui s'adresse cet outil ?

GeoServer s'adresse en particulier aux administrations, services et personnes souhaitant disposer d'un moteur cartographique en vue d'une externalisation de leurs donnés vers une interface de type WebMapping. A la question, pourquoi utiliser GeoServer plutôt que MapServer, je répondrais que c'est beaucoup plus une question d'habitude. Néanmoins, GeoServer dispose de quelques atouts supplémentaires comme une interface de gestion des données (ce qui par rapport au format text du .map de MapServer est plus qu'agréable), un export vers différents type de rendu cartographique (GoogleEarth, OpenLayers...), ou encore l'intégration des normes d'échange de données actuelles (WMS, WFS ...).

Mais comme je le soulignais, le choix de partir vers telle type plutôt qu'un autre est avant tout personelle, les deux solutions se valent et disposent d'une communauté importante et réactive. Et comme deux avis valent mieux qu'un je vous renvoie vers [l'article de Y.Jacolin sur Géorézo](http://georezo.net/geoblog/?q=node/152) portant sur la comparaison de ces deux solutions.

## Que peut on faire avec ?

Si vous avez bien lu les paragraphes précédents la réponse coule de source. Mais comme répéter ne fait pas de mal, nous alllons revenir sur les principales caractéristiques de Geoserver. Ainsi, GeoServer vous permettra de disposer d'un environnement complet pour la publication et l'édition de données géographique tout en utilisant les standarts de l'OSGEO. Les protocoles WMS, WFS-T, WCS sont dors et déjà implémentés, et la publication peut se faire dans les différents formats suivants, JPEG, PNG, SVG, KML/KMZ, GML, PDF, GeoJSON, ShapeFiles...

Pour un aperçu complet des possibilités je vous invite à consulter [cette page de démo](http://geo-s12.leeds.ac.uk:9080/geoserver/mapPreview.do).

----

<!-- geotribu:authors-block -->
