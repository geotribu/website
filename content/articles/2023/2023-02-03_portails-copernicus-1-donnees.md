---
title: "Accès aux données Copernicus/Sentinel partie 1 : données Copernicus et Sentinel"
authors:
    - Nicolas DAVID
categories:
    - article
date: "2023-02-03 10:20"
description: "Introduction et description des données d'observation de la terre produite dans le cadre du progamme européen Copernicus"
image: "https://cdn.geotribu.fr/img/logos-icones/copernicus_logo.50f4fc3b.png"
license: default
robots: index, follow
tags:
    - Copernicus
    - Sentinel
    - Open-data
    - Télédétection
---

# Accès aux données Copernicus/Sentinel, partie 1 : données Copernicus et Sentinel

:calendar: Date de publication initiale : 27 janvier 2023

## Introduction

![icône satellite](https://cdn.geotribu.fr/img/logos-icones/divers/satellite.png "icône satellite"){: .img-rdp-news-thumb }

L'europe fait évoluer, en 2023, les possibilités d'accès aux différentes données des satellites de la constellation Sentinel via la création du "Copernicus Data Space Ecosytem" : [dataspace.copernicus.eu](https://dataspace.copernicus.eu/).
Le lancement de ce nouveau portail est donc une bonne occasion de revenir un peu sur l'historique du programme Sentinel ainsi que les différentes possibilités d'accéder aux données open-data Sentinel puis de détailler les fonctionnalités prévues pour ce nouveau service au cours de trois articles, chacun dédié à une partie pour faciliter la lecture et le "picorage" d'information à ceux qui connaissent déjà le sujet.

* [Accès aux données Copernicus/Sentinel, partie 1 : données Copernicus et Sentinel](2023-02-03_portails-copernicus-1-donnees.md).
* [Accès aux données Copernicus/Sentinel, partie 2 : portails d'accès saisons 1&2, 'the road so far'](2023-02-03_portails-copernicus-2-passe.md).
* [Accès aux données Copernicus/Sentinel, partie 3 : évolution de l'accès aux données Copernicus/Sentinel](2023-02-03_portails-copernicus-3-futur.md).

Dans cette première partie nous revenons sur le programme Copernicus et surtout sur les différentes données produites par celui-ci. Les personnes connaissant déjà les données et l'ecosystème Sentinel / Coperncus peuvent directement aller au troisième et dernier article de la série.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Programme Copernicus et données d'occupation du sol

[Copernicus (Europe Eyes on Earth)](https://www.copernicus.eu/en/about-copernicus) est le programme européen de suivi et d'observation de la terre.
Il est responsable d'une part de la production de différentes couches de données géographiques et d'autre part de la mise en service et suivi opérationnel d'une constellation de satellites d'observation de la terre appelée Sentinel.

Concernant la production de données géographiques issues de Copernicus on peut notamment citer [les produits d'occupation du sol](https://land.copernicus.eu) comme [Corinne Land Cover](https://land.copernicus.eu/pan-european/corine-land-cover), produit depuis 1990 et [Urban Atlas](https://land.copernicus.eu/local/urban-atlas) qui sont par photointerprétation manuelle.
Ci-dessous un exemple de ces deux données sur une zone de Clermont-Ferrand :

![Orthophotographie RVB sur Clermont-Ferrand](copernicus_data/clermont_ferrand_ortho_a.jpg "Orthophotographie RVB sur Clermont-Ferrand - Crédits : IGN"){: .img-center loading=lazy }
![Corinne land Cover sur Clermont-Ferrand](copernicus_data/clermont_ferrand_CLC18_a.jpg "Données Corinne Land Cover 2018 sur Clermont-Ferrand - Crédits : IGN / Copernicus"){: .img-center loading=lazy }
![Urban Atlas sur Clermont-Ferrand](copernicus_data/clermont_ferrand_UA18_a.jpg "Données Urban Atlas 2018 sur Clermont-Ferrand - Crédits : IGN / Copernicus"){: .img-center loading=lazy }

A cela s'ajoute les couches HRL ([High Resolution Layers](https://land.copernicus.eu/pan-european/high-resolution-layers)) produites de façon semi-automatique et se focalisant chacune sur une des thématiques suivantes: zones imperméables, forêts, prairies et les surfaces d'eaux/zones humides, culture.
Par exemple pour les couches *imperviousness* et *tree cover density* sur la même zone que précédement :

![Couche HRL imperviousness sur Clermont-Ferrand](copernicus_data/clermont_ferrand_HRL18_impervious_a.jpg "Données Copernicus HRL imperviousness 2018 sur Clermont-Ferrand - Crédits : IGN / Copernicus"){: .img-center loading=lazy }
![Couche HRL Forest sur Clermont-Ferrand](copernicus_data/clermont_ferrand_HRL18_tree_density_a.jpg "Données Copernicus HRL Tree Cover Density 2018 sur Clermont-Ferrand - Crédits : IGN / Copernicus"){: .img-center loading=lazy }

## Données satellites Sentinel d'observation de la terre

Pour les données brutes d'observation de la terre (imagerie spatiale) leur production et mise à disposition est faite par le déploiement des satellites de la constellation Sentinel, qui s'est inspirée du [succès des satellites US Landsat](https://www.usgs.gov/news/featured-story/fifty-years-landsat-sharing-earth-information-benefit-all).

### Satellites de la constellation Sentinel

![Constellation sentinel 1 slide](copernicus_data/copernicus_sentinel_esa_mission.jpg "Satellites constellation Sentinel une diapo ESA - Crédits : ESA"){: .img-center loading=lazy }

Pour l'aspect observation de la partie surface continentale on peut citer les satellites et capteurs suivants :

* [Sentinel-1](https://esamultimedia.esa.int/docs/S1-Data_Sheet.pdf) : satellites équipés de capteur SAR ([Synthetic Aperture Radar](https://en.wikipedia.org/wiki/Synthetic-aperture_radar)) en bande C avec une revisite de 3 jours. Capteurs : Sentinel-1A (2014- ), Sentinel-1B (04-2016 /06-2022), Sentinel 1C (prévu 04/2023)
* [Sentinel-2](https://esamultimedia.esa.int/docs/S2-Data_Sheet.pdf) : satellites avec capteur optique multispectral à 10/20/60m de résolutions sur 12 bandes spectrales avec une revisite de 5 jours. Les données utilisées sont principalement les données de niveau 2A orthorectifiées et calibrées radiométriquemeent. Capteurs : Sentinel-2A (06/2015- ) , Sentinel-2B (03/2017 - ) , Sentinel-2C (prévu 2024)
* [Sentinel-3](https://esamultimedia.esa.int/docs/S3-Data_Sheet.pdf) : satellites altimétriques et observation océan/atmosphère (notamment température) Capteurs : Sentinel-3A (02/2016- ) , Sentinel-2B (04/2018 - )
* [Sentinel-5](https://esamultimedia.esa.int/docs/S5-prec_Data_Sheet.pdf) : satellites pour le suivi de l'atmosphère

[D'autres satellites Sentinel](https://www.esa.int/ESA_Multimedia/Images/2022/01/Copernicus_Sentinel_Expansion_missions) sont prévus dans le futur pour augmenter encore les capacités d'observation de la constellation avec en particulier en télédétection pour les surfaces continentales :

* Sentinel-12 / ROSE-L : satellites radar en bande L pour le suivi de la forêt et complémentaire de Sentinel-1 (lancement vers 2027). Bande radar utilisée en particulier pour des applications "forestières"
* Sentinel-10 / CHIME : satellites avec capteur optique hyperspectral en complément des capteurs mutlispectraux de Sentinel-2  (lancement vers 2029)

### Données optiques Sentinel 2

![Composition colorée temporelle NDVI Sentinel 2](copernicus_data/composition_ndvi_3dates_nov_jan_avr.png "Composition colorée temporelle NDVI Sentinel 2 - Crédits : IGN"){: .img-center loading=lazy }

### Données radar Sentinel 1

![Cohérence radar Sentinel-1](copernicus_data/sentinel_1_esa.png "Images de cohérence sentinel-1 6 jours - Crédits : ESA"){: .img-center loading=lazy }
