---
authors:
- GeoTribu
categories:
- article
date: 2009-09-11 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- data
- OpenStreetMap
- Open Source
title: Créer son propre plan de ville grace à MapOSMatic
---

# Créer son propre plan de ville grace à MapOSMatic


:calendar: Date de publication initiale : 11 septembre 2009


----

![OSM_logo.png](http://geotribu.net/sites/default/files/Tuto/img/Blog/OSM/OSM_logo.png) Il existe de nombreuses manières d'exploiter les données d'OSM! Si [les exemples les plus courants](http://wiki.openstreetmap.org/wiki/Featured_image_proposals) se font sous la forme d'interfaces cartographiques Web, il existe néanmoins d'autres initiatives qui se démarquent par leur originalité et leur utilité.


C'est le cas de l'application [MapOSMatic](http://maposmatic.org/) imaginée par Gilles Lamiral. Son but est de permettre, à partir d'une zone sélectionnée, de générer un plan quadrillé et ordonné qui servira à faire le lien avec l'index des noms de rues qui lui est associé. La philosopie du site tient en une simple phrase : "**Vos cartes de ville libres !**". Côté architecture technique, l'orientation est résolument pro python (Django, Mapnik...) avec une bonne dose également de Postgresql/PostGis pour la base de données.


[![maposmatic.png](/sites/default/files/Tuto/img/OSM/maposmatic.png)](http://maposmatic.org/)


La génération du plan se décompose en trois étapes :


1. Sélection de la zone désirée
2. Validation de la zone. Le plan à générer est alors mis à la suite des autres demandes en attente. L'état d'avancement est consultable depuis l'onglet "Rendus" (Jobs)
3. Une fois la demande traitée, celle-ci est disponible depuis l'onglet "Cartes" (Maps). Le plan ainsi que son index des rues peuvent être alors librement téléchargés (format PDF, SVG, PNG...).


![cartes.png](/sites/default/files/Tuto/img/OSM/cartes.png)


Cet outil, en plus d'être simple d'utilisation, offre un service des plus utiles tout en gardant un rendu cartographique de qualité. Il est possible également d'imaginer des évolutions futures, en créant par exemples des plans de villes touristiques (avec affichage de POIs remarquables) ou sportifs...




----

## Auteur

--8<-- "content/toc_nav_ignored/snippets/authors/geotribu.md"
