---
title: "Évolution de l'accès aux données Copernicus/Sentinel"
authors:
    - Nicolas DAVID
categories:
    - article
date: "2023-01-27 10:20"
description: "Évolution des portails d'accès aux données europénnes de la constellation satellites Sentinel : des début en 2015 aux évolutions prévues en 2023"
image: "https://cdn.geotribu.fr/img/logos-icones/copernicus_logo.50f4fc3b.png"
license: default
robots: index, follow
tags:
    - Copernicus
    - Sentinel
    - Open-data
    - Télédétection
---

# Accès aux données Copernicus, partie 3 : évolution de l'accès aux données Copernicus

:calendar: Date de publication initiale : 27 janvier 2023

## Introduction

![icône satellite](https://cdn.geotribu.fr/img/logos-icones/divers/satellite.png "icône satellite"){: .img-rdp-news-thumb }

L'europe fait évoluer, en 2023, les possibilités d'accès aux différentes données des satellites de la constellation Sentinel via la création du "Copernicus Data Space Ecosytem" : [dataspace.copernicus.eu](https://dataspace.copernicus.eu/).
Le lancement de ce nouveau portail est donc une bonne occasion de revenir un peu sur l'historique du programme Sentinel ainsi que les différentes possibilités d'accéder aux données open-data Sentinel puis de détailler les fonctionnalités prévues pour ce nouveau service au cours de trois articles, chacun dédié à une partie pour faciliter la lecture et le "picorage" d'information à ceux qui connaissent déjà le sujet.

Ce troisième article se propose de détailler les fonctionnalités prévues pour ce nouveau service.
En particulier, outre le téléchargement des données Sentinel en Open-data, leur accès via différents services "free" de plus haut niveaux est au programme, soit : visualisation des données via des flux, accès facilité aux données anciennes, utilisation des technologies dites "cloud ready"  etc.

Série **Accès aux données Copernicus/Sentinel** :

* [Partie 1 : données OCS et Sentinel](2023-02-03_portails-copernicus-1-donnees.md).
* [Partie 2 : portails d'accès, 'the road so far'](2023-02-03_portails-copernicus-2-passe.md).
* [Partie 3 : évolution de l'accès aux données Copernicus](2023-02-03_portails-copernicus-3-futur.md).

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Accès aux données Sentinel Teaser Saison 3 : "There can be only one"

Après quatre ans de retours d'expérience sur le déploiement et l'exploitation des DIAS, leur contrat arrivant à terme, l'Europe à choisi de faire évoluer son offre de services (gratuite et payante) d'accès aux données Sentinel.

Concrètement l'évolution consiste à selectionner un consortium (décembre 2022) afin d'opérer d'une part une nouvelle version du portail open-data européen Scihub qui offrira des fonctionnalités similaires aux DIAS mais en une version gratuite, avec toutefois une limitation de quota, et d'autre part à offrir une version payante de ce service permettant aux chercheurs, organismes publiques et industriels qui le souhaitent.
Cette version "non free" permet de disposer de ressources de stockage/calcul et d'accès aux services non limités moyennant finance.

Le deploiement de ce nouveau service commencera fin janvier 2023 avec la mise en place de service dans la continuité de ceux offerts par Scihub et s'étoffera progressivement de nouveaux services (plutôt issus des offres DIAS actuelles) jusqu'a juin 2023 où le service devra avoir atteint sa phase opérationnelle complète et date à laquelle l'ancien service Scihub devrait être arrêté.
Le premier contrat d'exploitation de ce nouveau service est d'une durée de six ans avec une extension possible de dix ans, soit possiblement une continuité de service sur seize ans.

Le consortium qui a été retenu est consituté d'industriels participant aux DIAS Mundi et Creodias : T-Systems, CloudFerro, Sinergise, VITO,  DLR, ACRI-ST et RHEA

* T-System : fournisseur de service et infra cloud
* CloudFerro : exploitation de l'infra T-System pour y déployer et mettre en place une solution de stockage et accès aux données Sentinel
* Sinergise : développement d'une offre de service sur l'accès aux données Sentinel (API de téléchargement, visualisation etc..) et d'un portail de visualisation accès aux données.
* VITO : développement d'une offre de service/accès basé sur OpenEo.
* DLR : expertise archivage, traitement de données satellites (SAR / Sentinel 1 en particuluer)
* ACRI-ST : expertise exploitation et traitement de données satellites Sentinel (Sentinel 2 et 3)
* RHEA

A noter que la mise en place de ce portail s'inscrit dans la stratégie européennes concernant [destination earth](https://digital-strategy.ec.europa.eu/en/policies/destination-earth) un projet européens sur la création de "#Digitial Twins"

## Détails de la nouvelle offre d'accès Sentinel

D'un point de vue communication le nom associé à l'offre de service devrait évoluer et être maintenant "Copernicus Data Space Ecosystem" associé à l'url [dataspace.copernicus.eu](https://dataspace.copernicus.eu/).

La nouvelle offre de service va offir une continuité par rapport à l'ancienne et devrait donc conserver les services existants de recherche et téléchargement des données Sentinel.
Mais elle doit aussi proposer plusieurs nouveautés en particulier concernant les interfaces *"machine to machine"*.

### Arrivé de STAC et COG

Une première évolution prévue est une diversification des modes d'accès et téléchargement à ces données.
Aujoud'hui l'accès aux données Sentinel se fait par granules (S1) ou dalles (S2) réprésentant des zones géographiques de plusieurs centaines de kilomètres ([tuiles de type MGRS](https://labo.obs-mip.fr/multitemp/the-sentinel-2-tiles-how-they-work/) de 110k0*110km pour Sentinel-2) dans le format de l'ESA (JPEG 2000).
Le nouveau "dataspace" copernicus offrira en plus un accès aux données selon les protocoles et format "cloud ready" [STAC](https://stacspec.org/en) (catalogue de données) et [COG (cloud optimised geotiff)](https://www.cogeo.org/) et permettra d'accéder seulement à la partie des données souhaitée, que cela soit au niveau des bandes spectrales ou de l'emprises géographiques.
Cela sera probablement effectué via un accès à un bucket S3 comme l'offre actuelle d'Amazon.

### Service de visualisation et accès interactif

Une première nouveauté de service devrait être l'arrivée de la mise à disposition, via les outils de l'entreprise Sinergise, de flux de visualisation de données respectant les normes OCG WMS, WMTS (tuile raster).
Cela sera accompagné à la fois par un portail de visualisation/récupération des données basée sur l'offre [EOBrowser](https://apps.sentinel-hub.com/eo-browser/) de Sinergise (aka geoportail) et par la mise à disposition de service [JupyterLab](https://jupyter.org/) pour l'accès aux données de façon intéractive dans des environnements de codes (plutôt basés python a priori).
On pense ici plutôt à un équivalent google colab et à ce que les DIAS offrent déjà comme service d'exploration de données.

### Offre de données Sentinel

Le nouveau portail devrait offrir un accès à l'ensemble des données Sentinel :
Sentinel-1 SLC et GRD  L2 OCN, Sentinel-2 L1C and L2A, Sentinel-3 and Sentinel-5P L1 et L2.
À cela, doit s'ajouter un accès aux "Copernicus Contributing Missions data".
Un exemple de ce type de données est la couverture satellites de l'Europe pour 2018 ayant servie à la production des données Corinne Land Cover millésime 2018.

Et enfin, de la même façon que le portail PEPS en france, un ensemble de fonctionnalités de post-traitements à la demande devrait être disponible.
En particulier cela devrait couvrir la possibilité d'effectuer des corrections atmosphérique avec le processeur MAJA et la production de produits dérivés Sentinel-1 comme la cohérence entre 2 dates (produit utilisé par exemple dans les algorithmes pour le suivi des cultures)

À noter, qu'a priori, il ne devrait plus y avoir de notions de donnés online/offline dépendant de la date d'acquisition des données.
Les données offline étant les données datant de plus de X mois et donc l'accès se fait en différé avec une demande de désarchivage puis un téléchargement.
Toutes les données produites depuis 2014 devrait donc être accesibles via un accès rapide, cela pour faciliter les traitements demandant un accès à des données sur un interval de temps long.

### Accès aux données via WCS et OpenEO

En plus de l'accès "simple" aux données le nouveaux service devrait aussi offrir deux nouveaux types d'accès permettant des post-traitement à la volé des données.
D'une part, on devrait rerouver une offre d'API selon la norme [WCS](http://opengeospatial.github.io/e-learning/wcs/text/basic-main.html) de
l'OGC (via Sinergise) qui permet par exemple des calculs simples entre bandes raster (de type calculatrice raster, cela permet par exemple de calculer à la volé une couche NDVI (indice de végétation) à partir des bandes spectrales rouge et infrarouge Sentinel-2.  
D'autre part, un service [OpenEO](https://openeo.org/) devrait aussi être déployer (via VITO).
L'API OpenEO propose des fonctionnalités de type Google Earth Engine (GEE) ou datacube mais avec une API normalisée et pouvant être proposée par différents backend/fournisseurs.
Le but étant à la fois de proposer une alternative à GEE mais aussi d'assurer un certain niveau d'intéropérabilité entre fournisseurs de services/données spatiales.

!!! note
    Beaucoup de ces nouveaux services sont en partie issus de travaux
    menés dans différents projets européens lors des dernières années :
    [OPENEO](https://openeo.org/)
