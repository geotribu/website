---
title: "Évolution de l'accès aux données Copernicus/Sentinel"
authors:
    - Nicolas DAVID
categories:
    - article
date: "2023-01-27 10:20"
description: "Évolution des portails d'accès aux données europénnes de la constellation satellites Sentinel : des début en 2015 aux évolutions prévues en 2023"
image: "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.copernicus.eu%2Fen&psig=AOvVaw15niRUcSg8Zs1jzufbxn2h&ust=1674806243021000&source=images&cd=vfe&ved=0CBAQjRxqFwoTCKCorMvh5PwCFQAAAAAdAAAAABAE"
license: default
robots: index, follow
tags:
    - Copernicus
    - Sentinel
    - Open-data
    - Télédétection
---

# Evolution de l'accès aux données Copernicus/Sentinel

:calendar: Date de publication initiale : 27 janvier 2023

## Introduction

L'europe fait évoluer, en 2023, les possibilités d'accès aux différentes données
des satellites de la constellation Sentinel via la création du "Copernicus
Data Space Ecosytem".
Il s'agit d'un nouveau portail d'accès aux données qui prendra la suite du portail actuel [scihub.copernicus.eu](https://scihub.copernicus.eu) (données open-data) et prendra la suite de certains
des actuels DIAS (**D**ata **I**nformation and **A**cces **S**ervice) pour l'offre de service payante associée.
La première version de ce portail, [dataspace.copernicus.eu](https://dataspace.copernicus.eu/), a été lancée cette semaine et devrait évoluer vers sa version définitive jusqu'en juin 2023.

Le lancement de ce nouveau portail est donc une bonne occasion de revenir un peu
sur l'historique du programme sentinel ainsi que les différentes possibilités
d'accéder aux données open-data sentinel puis de détailler les fonctionnalités
prévues pour ce nouveau service.
En particulier, outre le téléchargement des données Sentinel en Open-data,
leur accès via différents services "free" de plus haut niveaux est au programme,
soit : visualisation des données via des flux, accès facilité aux données
anciennes, utilisation des techno "cloud ready"  etc.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Programme Copernicus et données Sentinel

[Copernicus (Europe Eyes on Earth)](https://www.copernicus.eu/en/about-copernicus) est le programme européen de suivi et
d'observation de la terre. Il est responsable d'une part de la production
de différentes couches de données géographiques et d'autre part de la mise en
service et suivi opérationnel d'une constellation de satellites d'observation
de la terre appelée Sentinel.

Concernant la production de données géographiques issues de Copernicus on peut
notamment citer [les produits d'occupation du sol](https://land.copernicus.eu) comme [Corinne Land Cover](https://land.copernicus.eu/pan-european/corine-land-cover), produit depuis 1990,
[Urban Atlas](https://land.copernicus.eu/local/urban-atlas) ainsi que les couches HRL ([High Resolution Layers](https://land.copernicus.eu/pan-european/high-resolution-layers)). Ces dernières sont produites de façon semi-automatique et se focalisant chacune sur une des thématiques suivantes: zones imperméables, forêts, prairies et les surfaces d'eaux/zones humides, culture.
Pour les données brutes d'observation de la terre (imagerie spatiale) leur
production et mise à disposition est faite par le déploiement des satellites de
la constellation Sentinel, qui s'est inspirée du [succès des satellites US Landsat](https://www.usgs.gov/news/featured-story/fifty-years-landsat-sharing-earth-information-benefit-all).

Pour l'aspect observation de la partie surface continentale on peut citer les
satellites et capteurs suivants :

* [Sentinel-1](https://esamultimedia.esa.int/docs/S1-Data_Sheet.pdf) :
  satellites équipés de capteur SAR (bande C) avec une revisite de 3 jours.
  Capteurs : Sentinel-1A (2014- ), Sentinel-1B (04-2016 /06-2022), Sentinel 1C (prévue
  04/2023)
* [Sentinel-2](https://esamultimedia.esa.int/docs/S2-Data_Sheet.pdf) :
  satellites avec capteur optique multispectrale à 10/20/60m
  de résolutions sur 12 bandes spectrales. revisite de 5 jours. Les données
  utilisées sont principalement les données de niveau 2A orthorectifiées et
  calibrées radiométriquemeent.
  Capteurs : Sentinel-2A (06/2015- ) , Sentinel-2B (03/2017 - ) , Sentinel-2C (prévu 2024)
* [Sentinel-3](https://esamultimedia.esa.int/docs/S3-Data_Sheet.pdf) :
  satellites altimétriques et observation océan/atmosphère (
  notamment température)
  Capteurs : Sentinel-3A (02/2016- ) , Sentinel-2B (04/2018 - )
* [Sentinel-5](https://esamultimedia.esa.int/docs/S5-prec_Data_Sheet.pdf) :
  satellites pour le suivi de l'atmosphère

[D'autres satellites Sentinel](https://www.esa.int/ESA_Multimedia/Images/2022/01/Copernicus_Sentinel_Expansion_missions) sont prévus dans le futur pour augmenter encore les capacités
d'observation de la constellation avec en particulier en télédétection pour les
surfaces continentales :

* Sentinel-12 / ROSE-L : satellites radar en bande L pour le suivi de la forêt
  et complémentaire de Sentinel-1 (lancement vers 2027). Bande radar utilisée en particulier pour des applications "forestières"
* Sentinel-10 / CHIME : satellites avec capteur optique hyperspectrale en complément des capteurs mutlispectraux de sentinel-2  (lancement vers 2029)

## Accès aux données Sentinel, "the road so far"

### Saison 1 : portails open-data européens et nationaux

L'europe a accompagné le lancement et la mise en production des différents
satellites sentinel par la mise en place de services d'accès aux données
diffusées en open data.

Le premier service d'accès aux données a été le Copernicus [Open Access Hub] (<https://scihub.copernicus.eu/>) ouvert en 2014 pour la diffusion des données du premier satellite Sentinel-1A. Toutefois ce portail est souvent désigné d'après son url d'accès, "https://scihub.copernicus.eu/", comme SciHub. Et c'est le nom qui sera utilisé dans le reste de cet article.

!!! warning
    à noter de ne pas confondre Scihub site copernicus d'accès aux données
    sentinel avec sci-hub le fameux site pirate d'accès aux publications
    scientifiques.

Le site Scihub offre principalement deux services : recherche de données et téléchargement de données.
Ces fonctionnalités sont disponibles soit graphiquement via un site internet
soit via des [API](https://scihub.copernicus.eu/userguide/APIsOverview). Ces dernières sont adaptées des API REST de type [OpenSearch](https://www.opensearch.org/) ou [OData,(Open Data Protocol)](https://www.odata.org/)
L'accès aux données est gratuit pour toute personne mais il existe toutefois une
limitation de débit et du nombre de téléchargement en parallèle possible par utilisateur.
La communauté d'utilisateur a développé différents outils open-source permettant
de faciliter l'utilisation des ces API dans votre langage de programmation
préféré, par exemple en python l'outil [SentinelSat](https://sentinelsat.readthedocs.io/en/stable/)

!!! note
    le code du portail scihub est lui même opensource via le projet **sentineldatahub**. Liens pour la [documentation](https://sentineldatahub.github.io/DataHubSystem/index.html) et le [github](https://github.com/SentinelDataHub/DataHubSystem)

Afin de faciliter la diffusion large des données Sentinel, différents portails
nationaux (appelés miroirs) sont également venus compléter l'offre de diffusion
et accès aux données. On peut citer par exemple [le portail autrichien](https://data.sentinel.zamg.ac.at/dhus/#/home), [le portail australien](https://www.copernicus.gov.au/data-access) et bien sur [PEPS un des portails français](https://peps.cnes.fr/rocket/#/home).

En france il existe actuellement deux portails nationaux d'accès aux données Sentinel :
[PEPS](https://peps.cnes.fr/rocket/#/home) et [THEIA](https://theia.cnes.fr/atdistrib/rocket/#/home).

#### PEPS

[PEPS](https://peps.cnes.fr/rocket/#/home) (Plateforme d’Exploitation des Produits Sentinels) est un portail développé
et maintenu par le CNES qui offre la recherche et le téléchargement des données
Sentinel-1 et Sentinel-2. Par rapport à l'offre de base Scihub, PEPS permet un
accès un peu plus rapide aux données en France (meilleur débit) mais aussi des
post-traitements de données supplémentaires comme l'extraction de bande ou
l'orthorectification des données SAR Sentinel-1 sur la géométrie "grille" de
diffusion des données Sentinel-2 via [S1-tiling](https://gitlab.orfeo-toolbox.org/s1-tiling/s1tiling)

#### THEIA

[THEIA](https://theia.cnes.fr/atdistrib/rocket/#/home) est une composante de l'infrastructure de recherche [Data-Terra](https://www.data-terra.org/) centrée sur l'étude des surfaces continentales.
Elle a, en particulier, pour objectif de faciliter l'accès aux données nécessaires pour la recherche et les études pour l'observation de la terre.
Dans ce cadre le site THEIA permet de rechercher et
télécharger un certain nombre de données d'observation de la terre dont des
données Sentinel.
Les fonctionnalités sont disponibles graphiquement via l'interface web ou bien via une API REST.
Par rapport à PEPS ou scihub, le site THEIA ne fournit pas d'accès aux données SAR Sentinel-1.
Mais par contre il propose des données Sentinel-2 avec une meilleure calibration radiométrique (en utilisant la chaine de traitement [MAJA](https://www.cesbio.cnrs.fr/outils/maja/)) pour les données de niveau L2A, ainsi que des données de niveau [L3A](https://labo.obs-mip.fr/multitemp/theias-sentinel-2-l3a-monthly-cloud-free-syntheses/) qui sont des synthèses mensuelles des images sentinel L2A.
Ces dernières sont pratiques pour avoir des images avec moins de nuages et diminuer le volume de données à traiter.
En plus des données Sentinel, THEIA donne aussi accès à des produits
dérivés comme la carte d'occupation des sol [OSO](https://www.theia-land.fr/en/ceslist/land-cover-sec/) ou une carte de couverture
'neige' et des images SPOT et Landsat.

Certaines infrastructures geo régionales proposent également un accès local aux données Copernicus : [mviewer geobretagne](https://geobretagne.fr/pub/dreal_b/mviewer/?config=../apps/teledetection/config.xml)

### Saison 2 : here comme the dragons, GAFAM et réponse européene

Assez rapidement après la mise à disposition des données Sentinel-2 en open-data
Amazon et Google ont aussi récupéré ces donnés afin de les intégrer dans leurs
plateformes respectives.
Pour Google cela s'est fait via leur mise à disposition
dans Google Earth Engine (GEE) qui est accessible de façon gratuite pour les étudiants et chercheurs.
Et du côté d'Amazon, ces données ont été mises à disposition dans
un [répertoire de données open-data](https://registry.opendata.aws/sentinel-2/) hebergé sur les services Amazon (bucket S3),
cela facilitant entre autre leur exploitation dans l'offre de service Amazon.
Il faut noter que les données Landsat diffusées en open-data avaient déjà ouvert
la voie pour ces modes de diffusion de données satellites par les GAFAM.

En 2018, un peu en réponse aux GAFAM, l'europe a lancé un appel à candidature
pour la mise en place de plateformes "cloud" proposant un accès simplifié et
efficace aux données Sentinel afin d'aider aux développements de nouveaux
services. Quatre DIAS (Data and Information Access Service) ont alors été retenus
pour une période 4 ans.
Par rapport aux plateformes Scihub et PEPS/THEIA l'objectif des DIAS était de
fournir des services payants permettant aux entreprises et acteurs publiques de
développer plus facilement des applications et services utilisant les données Sentinel.
Le but était par exemple d'éviter qu'un organisme ait à télécharger et stocker l'intégralité des données Sentinel-2 afin de lancer un calcul automatique de carte d'occupation des sols ou autres produit dérivé.
Le volume des données Sentinel pour un an d'acquisition sur un
pays en Europe étant de l'ordre d'une dizaine à quelques centaines de To selon
la taille du pays, traiter un tel volume nécessite donc, sans DIAS, un temps non
négligeable de récupération des données et un coût d'infrastructure de stockage
conséquent. Les DIAS offrent une alternative en proposant d'herberger ces données
et en proposant des ressources de calculs (serveurs clouds) ayant un accès rapide
à celles-ci. L'accès aux données sentinel étant gratuit depuis les plateformes DIAS
mais l'accès aux ressources de calcul payant.

Pour détailler, un peu plus, on peut considérer un DIAS comme étant composé de :

* une **infrastructure cloud** : soit un accès à des serveurs de calcul et du stockage de données, etc.. . Donc des services de type OVH/Orange cloud/... ou Google/Amazon.
* **un stockage et un catalogue de données sentinel**. C'est à dire une gestion d'une
  solution d'ingestion, sauvegarde et accès aux différentes données Sentinel
  produites par Copernicus ainsi que de post-traitement "classiques" de données.
  Cela comprend donc le développement (code) et mise en place d'une architecture
  cloud appropriée ainsi que la gestion opérationnelle du service.
* Production et **offre d'API pour se connecter aux services et accéder aux données**. Cela comprend aussi les fonctionnalités de gestion utilisateur centralisé et de facturation des services.
* **une offre de service et applications tierces** sur les données sentinel du catalogue.
  Services produits par le consortium (défaut du DIAS) ou par un tier sur une
  "place de marché" et via paiement/abonnement au service

Les quatre consortiums choisis pour les DIAS étaient :

* [Creodias](https://creodias.eu/) : Consortium avec Creotech Instrument (Lead, gestion projet), CloudFerro (cloud + données sentinel), Sinergise (accès données) ainsi que WIZIPISI et Geomatys (traitement de données).
* [Mundi](https://mundiwebservices.com/) : Consortium avec T-System pour l'infra (cloud), Atos pour
  l'opérationnel/management de la plateforme et Sinergise pour l'ajout de
  service de visualisation et API sur les données.
  (DLR, e-Geos, EOX, GAF, Sinergise, Spacemetric, Thales Alenia Space and T-Systems, which is led by Atos)
* [Onda](https://www.onda-dias.eu/cms/) : Serco (Lead) OVH (cloud infra), GAEL Sytem (data access solution)
  Sinergise (web spatial data applications /API)
* [Sobloo](https://sobloo.eu/index.html) : Orange Business Services (cloud), Airbus (data provider)  Capgemini
  Lead par Airbus, Capgemini apporte ses logiciels de traitement des données
  et Orange fournit sa solution cloud grand public Flexible Engine

A ces quatres DIAS s'est ajouté un cinquième, [WEKEO](https://www.wekeo.eu/), qui est plus dédié sur la communauté météo/océanique.
Une étude comparative de ces DIAS est disponible sur le [gitlab IDGEO](https://gitlab.com/idgeo_public/etude-dias)

Au niveau européen, un cas d'application (clients) de ces offres DIAS a été, entre
autre, leur utilisation par les différents organismes de contrôles et paiements
associés à la PAC (Politique Agricole Communes) pour la mise en place d'un
"monitoring CAP". En effet l'EU a souhaité faire évoluer les contrôles terrain
ponctuels associés aux versemment des aides PAC vers un ["monitoring"](https://publications.jrc.ec.europa.eu/repository/handle/JRC112913) exhaustif
spatiallement et semi-automatique par l'exploitation dees données Sentinel-1
et 2. Ces dernières devant permettre entre autre de vérifier la présence
ou non d'activité agricoles (présence de culture annuel, détection de fauche de
prairie etc..) sur une parcelle donnée.

## Accès aux données sentinel Teaser Saison 3 : "There can be only one"

Après quatre ans de retours d'expérience sur le déploiement et l'exploitation des DIAS, leur contrat arrivant à terme, l'Europe à choisi de
faire évoluer son offre de services (gratuite et payante) d'accès aux données
Sentinel.

Concrètement l'évolution consiste à selectionner un consortium (décembre 2022)
afin d'opérer d'une part une nouvelle version du portail open-data européen
scihub qui offrira des fonctionnalités similaires aux DIAS mais en une version
gratuite, avec toutefois une limitation de quota, et d'autre part à offrir une
version payante de ce service permettant aux chercheurs, organismes publiques et
industriels qui le souhaitent. Cette version "non free" permet de disposer de ressources de stockage/calcul et d'accès aux services non limités moyennant finance.

Le deploiement de ce nouveau service commencera fin janvier 2023 avec la mise
en place de service dans la continuité de ceux offerts par scihub et s'étoffera
progressivement de nouveaux services (plutôt issus des offres DIAS actuelles)
jusqu'a juin 2023 où le service devra avoir atteint sa phase opérationnelle
complète et date à laquelle l'ancien service scihub devrait être arrêté.
Le premier contrat d'exploitation de ce nouveau service est d'une durée de
six ans avec une extension possible de dix ans, soit possiblement une continuité de service sur seize ans.

Le consortium qui a été retenu est consituté d'industriels participant aux DIAS
Mundi et Creodias : T-Systems, CloudFerro, Sinergise, VITO,  DLR, ACRI-ST et RHEA

* T-System : fournisseur de service et infra cloud
* CloudFerro : exploitation de l'infra T-System pour y déployer et mettre en
  place une solution de stockage et accès aux données Sentinel
* Sinergise : développement d'une offre de service sur l'accès aux données
  sentinel (API de téléchargement, visualisation etc..) et d'un portail de
  visualisation accès aux données.
* VITO : développement d'une offre de service/accès basé sur OpenEo.
* DLR : expertise archivage, traitement de données satellites (SAR / Sentinel 1
  en particuluer)
* ACRI-ST : expertise exploitation et traitement de données satellites sentinel
  (sentinel 2 et 3)
* RHEA

A noter que la mise en place de ce portail s'inscrit dans la stratégie européennes concernant
[destination earth](https://digital-strategy.ec.europa.eu/en/policies/destination-earth) un projet européens sur la création de "#Digitial Twins"

## Détails de la nouvelle offre d'accès Sentinel

D'un point de vue communication le nom associé à l'offre de service devrait
évoluer et être maintenant "Copernicus Data Space Ecosystem" associé à l'url dataspace.copernicus.eu.

La nouvelle offre de service va offir une continuité par rapport à l'ancienne
et devrait donc conserver les services existants de recherche et téléchargement
des données Sentinel. Mais elle doit aussi proposer plusieurs nouveautés
en particulier concernant les interfaces "machine to machine".

### Arrivé de STAC et COG

Une première évolution prévue est une diversification des modes d'accès et
téléchargement à ces données. Aujoud'hui l'accès aux données Sentinel se fait
par granules (S1) ou dalles (S2) réprésentant des zones géographiques de plusieurs
centaines de kilomètres ([tuiles de type MGRS](https://labo.obs-mip.fr/multitemp/the-sentinel-2-tiles-how-they-work/) de 110k0*110km pour sentinel-2) dans
le format de l'ESA (JPEG 2000). Le nouveau "dataspace" copernicus offrira en
plus un accès aux données selon les protocoles et format "cloud ready" [STAC](https://stacspec.org/en)
(catalogue de données) et [COG (cloud optimised geotiff)](https://www.cogeo.org/) et permettra d'accéder
seulement à la partie des données souhaitée, que cela soit au niveau des bandes
spectrales ou de l'emprises géographiques. Cela sera probablement effectué via
un accès à un bucket S3 comme l'offre actuelle d'Amazon.

### Service de visualisation et accès interactif

Une première nouveauté de service devrait être l'arrivée de la mise à disposition,
via les outils de l'entreprise Sinergise, de flux de visualisation de données
respectant les normes OCG WMS, WMTS (tuile raster).
Cela sera accompagné à la fois par un portail de visualisation/récupération
des données basée sur l'offre [EOBrowser](https://apps.sentinel-hub.com/eo-browser/) de Sinergise (aka geoportail) et par
la mise à disposition de service [JupyterLab](https://jupyter.org/) pour l'accès aux données de façon
intéractive dans des environnements de codes (python a priori). On pense ici
plutôt à un équivalent google colab et à ce que les DIAS offrent déjà comme service d'exploration de données.

### Offre de données Sentinel

Le nouveau portail devrait offrir un accès à l'ensemble des données Sentinel :
Sentinel-1 SLC et GRD  L2 OCN, Sentinel-2 L1C and L2A, Sentinel-3 and
Sentinel-5P L1 et L2.
À cela, doit s'ajouter un accès aux "Copernicus Contributing Missions data". Un exemple de ce type de données est la couverture satellites de l'Europe pour 2018 ayant servie à la production des données Corinne Land Cover millésime 2018.
Et enfin, de la même façon que le portail PEPS en france, un ensemble de
fonctionnalités de post-traitements à la demande devrait être disponible. En
particulier cela devrait couvrir la possibilité d'effectuer des corrections
atmosphérique avec le processeur MAJA et la production de produits dérivés
Sentinel-1 comme la cohérence entre 2 dates (produit utilisé par exemple dans les algorithmes pour le suivi des cultures)
À noter qu'a priori il ne devrait plus y avoir de notions de donnés online/offline
dépendant de la date d'acquisition des données. Les données offline étant les données datant de plus de X mois et donc l'accès se fait en différé avec une demande de désarchivage puis un téléchargement. Toutes les données produites
depuis 2014 devrait donc être accesibles via un accès rapide, cela pour faciliter
les traitements demandant un accès à des données sur un interval de temps long.

### Accès aux données via WCS et OpenEO

En plus de l'accès "simple" aux données le nouveaux service devrait aussi
offrir deux nouveau types d'accès permettant des post-traitement à la volé des
données.
D'une part, on devrait rerouver une offre d'API selon la norme [WCS](http://opengeospatial.github.io/e-learning/wcs/text/basic-main.html) de
l'OGC (via Sinergise) qui permet par exemple des calculs simples entre bandes
raster (de type calculatrice raster, cela permet par exemple de calculer à la
volé un couche NDVI (indice de végétation) à partir des bandes rouges et
infrarouges Sentinel-2.  
D'autre part, un service [OpenEO](https://openeo.org/) devrait aussi être déployer (via VITO). L'API
OpenEO propose des fonctionnalités de type Google Earth Engine (GEE) ou
datacube mais avec une API normalisée et pouvant être proposée par différents
backend/fournisseurs. Le but étant à la fois de proposer une alternative à GEE
mais aussi d'assurer un certain niveau d'intéropérabilité entre fournisseurs de
services/données spatiales.

!!! note
    Beaucoup de ces nouveaux services sont en partie issus de travaux
    menés dans différents projets européens lors des dernières années :
    [OPENEO](https://openeo.org/)

## Auteur {: data-search-exclude }

--8<-- "content/team/ndavid.md"

{% include "licenses/default.md" %}
