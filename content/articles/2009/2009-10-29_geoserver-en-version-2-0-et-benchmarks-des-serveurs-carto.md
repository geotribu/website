---
title: "GeoServer en version 2.0 et Benchmarks des serveurs carto"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-10-29
description: "GeoServer en version 2.0 et Benchmarks des serveurs carto"
tags:
    - GeoServer
    - open source
    - serveur cartographique
---

# GeoServer en version 2.0 et Benchmarks des serveurs carto

:calendar: Date de publication initiale : 29 octobre 2009

![logo GeoServer](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/geoserver.png "logo GeoServer"){: .img-thumbnail-left }

Lors d'un précédent [billet](http://geotribu.net/node/122) nous avions déjà annoncé la disponibilité de GeoServer 2.0, néanmoins à l'époque cette version n'était encore qu'une release candidate. Depuis, plusieurs mois sont passés mais c'était le temps nécessaire aux développeurs pour corriger les derniers bugs et de nous offrir une version stable.  
Plusieurs modifications importantes dont les plus visibles portent sur l'interface utilisateur et administrateur ont été apportées ce qui fait de l'aveu même de l'équipe de GeoServer, une version majeure (pour plus de détails consultez ce [billet](http://blog.geoserver.org/2009/10/26/geoserver-2-0-released/)). GeoServer 2.0 est donc disponible en [téléchargement](http://geoserver.org/display/GEOS/GeoServer+2.0.0) depuis quelques jours, pour les personnes que les fichiers mapfile rebutent je vous conseille fortement ce moteur cartographique très user friendly.

Toujours dans le domaine des moteurs cartographiques, le dernier [FOSS4G](http://2009.foss4g.org/) a vu l'[affrontement](http://wiki.osgeo.org/wiki/Benchmarking_2009) pacifique et amical des deux poids lourds de l'OpenSource. Dans le coin droit MapServer, dans le coin gauche GeoServer. Il faut néanmoins noter l'[absence d'Esri](http://lists.osgeo.org/pipermail/benchmarking/2009-October/000353.html) (et [ici](http://fuzzytolerance.info/2009/10/esri-withdraws-from-foss4g-wms-shootout/)) qui avait au départ prévu de participer. C'est dommage, cela aurait permis d'étoffer la compétition et offrir de plus amples comparaisons.

L'objectif de ce comparatif portait sur les performances WMS de chacun des deux serveurs. Le but étant de comparer le temps de génération d'une image en utilisant des sources de données aussi bien vectorielles que matricielles ou même stockées en base (shapefile, geotiff, ECW, PostgreSQL/PostGIS, Oracle Spatial...). L'essentiel des caractéristiques du Benchmark est expliqué sur le [wiki](http://wiki.osgeo.org/wiki/Benchmarking_2009), je vous invite donc à le consulter si vous souhaitez en connaitre davantage.

Les conclusions de ce Benchmarks, disponibles en [ligne](https://www.slideshare.net/gatewaygeomatics.com/wms-performance-shootout), montrent que si MapServer l'emporte d'une courte tête, les deux serveurs cartographiques sont, en terme de performance, au coude à coude. Néanmoins ce test aura permis de confirmer, si besoin est, les très bons résultats de ces serveurs aussi bien en terme de vitesse qu'en tenue de charge. J'ai hate de voir ce quelle nouvelle surprise nous réserve le prochain [FOSS4G 2010](http://2010.foss4g.org/)

----

<!-- geotribu:authors-block -->
