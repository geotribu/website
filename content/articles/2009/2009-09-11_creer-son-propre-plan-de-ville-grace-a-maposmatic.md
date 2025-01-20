---
title: "Créer son propre plan de ville grace à MapOSMatic"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-09-11
description: "Créer son propre plan de ville grace à MapOSMatic"
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/openstreetmap/maposmatic.png"
license: default
robots: index, follow
tags:
    - carte
    - MapOSMatic
    - open source
    - OpenStreetMap
---

# Créer son propre plan de ville grace à MapOSMatic

:calendar: Date de publication initiale : 11 septembre 2009

![logo OpenStreetMap](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/Openstreetmap.png "logo OpenStreetMap"){: .img-thumbnail-left }

Il existe de nombreuses manières d'exploiter les données d'OSM! Si [les exemples les plus courants](https://wiki.openstreetmap.org/wiki/Featured_image_proposals) se font sous la forme d'interfaces cartographiques Web, il existe néanmoins d'autres initiatives qui se démarquent par leur originalité et leur utilité.

C'est le cas de l'application [MapOSMatic](http://maposmatic.org/) imaginée par Gilles Lamiral. Son but est de permettre, à partir d'une zone sélectionnée, de générer un plan quadrillé et ordonné qui servira à faire le lien avec l'index des noms de rues qui lui est associé.  
La philosopie du site tient en une simple phrase : "**Vos cartes de ville libres !**".

Côté architecture technique, l'orientation est résolument pro python (Django, Mapnik...) avec une bonne dose également de Postgresql/PostGIS pour la base de données.

![MapOSMatic](https://cdn.geotribu.fr/img/articles-blog-rdp/openstreetmap/maposmatic.png "MapOSMatic"){: .img-center loading=lazy }

La génération du plan se décompose en trois étapes :

1. Sélection de la zone désirée
1. Validation de la zone. Le plan à générer est alors mis à la suite des autres demandes en attente. L'état d'avancement est consultable depuis l'onglet "Rendus" (Jobs)
1. Une fois la demande traitée, celle-ci est disponible depuis l'onglet "Cartes" (Maps). Le plan ainsi que son index des rues peuvent être alors librement téléchargés (format PDF, SVG, PNG...).

![MapOSMatic - Carte](https://cdn.geotribu.fr/img/articles-blog-rdp/openstreetmap/maposmatic_cartes.png "MapOSMatic - Carte"){: .img-center loading=lazy }

Cet outil, en plus d'être simple d'utilisation, offre un service des plus utiles tout en gardant un rendu cartographique de qualité. Il est possible également d'imaginer des évolutions futures, en créant par exemples des plans de villes touristiques (avec affichage de POIs remarquables) ou sportifs...

!!! info
    Le projet MapOSMatic semble s'être éteint depuis 2017. Un fork, renommé MyOSMatic, reste actif et accessible sur : <https://print.get-map.org/>. Pour plus d'informations, voir [le wiki OSM](https://wiki.openstreetmap.org/wiki/FR:MapOSMatic).

----

<!-- geotribu:authors-block -->
