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

# Accès aux données Copernicus/Sentinel : partie 1 , données Copernicus et Sentinel

:calendar: Date de publication initiale : 27 janvier 2023

## Introduction

![icône satellite](https://cdn.geotribu.fr/img/logos-icones/divers/satellite.png "icône satellite"){: .img-rdp-news-thumb }

L'europe fait évoluer, en 2023, les possibilités d'accès aux différentes données des satellites de la constellation Sentinel via la création du "Copernicus Data Space Ecosytem".
Il s'agit d'un nouveau portail d'accès aux données qui prendra la suite du portail actuel [scihub.copernicus.eu](https://scihub.copernicus.eu) (données open-data) ainsi que de certains des actuels DIAS (**D**ata **I**nformation and **A**cces **S**ervice) pour l'offre de service payante associée.
La première version de ce portail, [dataspace.copernicus.eu](https://dataspace.copernicus.eu/), a été lancée cette semaine et devrait évoluer vers sa version définitive jusqu'en juin 2023.

Le lancement de ce nouveau portail est donc une bonne occasion de revenir un peu sur l'historique du programme Sentinel ainsi que les différentes possibilités d'accéder aux données open-data Sentinel puis de détailler les fonctionnalités prévues pour ce nouveau service.
En particulier, outre le téléchargement des données Sentinel en Open-data,
leur accès via différents services "free" de plus haut niveaux est au programme, soit : visualisation des données via des flux, accès facilité aux données anciennes, utilisation des technologies dites "cloud ready"  etc.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Programme Copernicus et données Sentinel

[Copernicus (Europe Eyes on Earth)](https://www.copernicus.eu/en/about-copernicus) est le programme européen de suivi et d'observation de la terre.
Il est responsable d'une part de la production de différentes couches de données géographiques et d'autre part de la mise en service et suivi opérationnel d'une constellation de satellites d'observation de la terre appelée Sentinel.

Concernant la production de données géographiques issues de Copernicus on peut
notamment citer [les produits d'occupation du sol](https://land.copernicus.eu) comme [Corinne Land Cover](https://land.copernicus.eu/pan-european/corine-land-cover), produit depuis 1990, [Urban Atlas](https://land.copernicus.eu/local/urban-atlas) ainsi que les couches HRL ([High Resolution Layers](https://land.copernicus.eu/pan-european/high-resolution-layers)).
Ces dernières sont produites de façon semi-automatique et se focalisant chacune sur une des thématiques suivantes: zones imperméables, forêts, prairies et les surfaces d'eaux/zones humides, culture.

Pour les données brutes d'observation de la terre (imagerie spatiale) leur production et mise à disposition est faite par le déploiement des satellites de la constellation Sentinel, qui s'est inspirée du [succès des satellites US Landsat](https://www.usgs.gov/news/featured-story/fifty-years-landsat-sharing-earth-information-benefit-all).

Pour l'aspect observation de la partie surface continentale on peut citer les satellites et capteurs suivants :

* [Sentinel-1](https://esamultimedia.esa.int/docs/S1-Data_Sheet.pdf) : satellites équipés de capteur SAR ([Synthetic Aperture Radar](https://en.wikipedia.org/wiki/Synthetic-aperture_radar)) en bande C avec une revisite de 3 jours. Capteurs : Sentinel-1A (2014- ), Sentinel-1B (04-2016 /06-2022), Sentinel 1C (prévu 04/2023)
* [Sentinel-2](https://esamultimedia.esa.int/docs/S2-Data_Sheet.pdf) : satellites avec capteur optique multispectral à 10/20/60m de résolutions sur 12 bandes spectrales avec une revisite de 5 jours. Les données utilisées sont principalement les données de niveau 2A orthorectifiées et calibrées radiométriquemeent. Capteurs : Sentinel-2A (06/2015- ) , Sentinel-2B (03/2017 - ) , Sentinel-2C (prévu 2024)
* [Sentinel-3](https://esamultimedia.esa.int/docs/S3-Data_Sheet.pdf) : satellites altimétriques et observation océan/atmosphère (notamment température) Capteurs : Sentinel-3A (02/2016- ) , Sentinel-2B (04/2018 - )
* [Sentinel-5](https://esamultimedia.esa.int/docs/S5-prec_Data_Sheet.pdf) : satellites pour le suivi de l'atmosphère

[D'autres satellites Sentinel](https://www.esa.int/ESA_Multimedia/Images/2022/01/Copernicus_Sentinel_Expansion_missions) sont prévus dans le futur pour augmenter encore les capacités d'observation de la constellation avec en particulier en télédétection pour les surfaces continentales :

* Sentinel-12 / ROSE-L : satellites radar en bande L pour le suivi de la forêt et complémentaire de Sentinel-1 (lancement vers 2027). Bande radar utilisée en particulier pour des applications "forestières"
* Sentinel-10 / CHIME : satellites avec capteur optique hyperspectral en complément des capteurs mutlispectraux de Sentinel-2  (lancement vers 2029)
