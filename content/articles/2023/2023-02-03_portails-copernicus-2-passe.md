---
title: "Accès aux données Copernicus/Sentinel partie 2 : portails d'accès saisons 1&2, 'the road so far'"
authors:
    - Nicolas DAVID
categories:
    - article
date: "2023-02-03 10:20"
description: "Historique des portails d'accès aux données Sentinel en Europe et en France et description de leur grandes fonctionnalités"
image: "https://cdn.geotribu.fr/img/logos-icones/copernicus_logo.50f4fc3b.png"
license: default
robots: index, follow
tags:
    - Copernicus
    - Sentinel
    - Open-data
    - Télédétection
---

# Accès aux données Copernicus/Sentinel partie 2 : portails d'accès saisons 1&2, 'the road so far'

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

## Saison 1 : portails open-data européens et nationaux

L'Europe a accompagné le lancement et la mise en production des différents satellites Sentinel par la mise en place de services d'accès aux données diffusées en open data.

Le premier service d'accès aux données a été le Copernicus [Open Access Hub](<https://scihub.copernicus.eu/>) ouvert en 2014 pour la diffusion des données du premier satellite Sentinel-1A. Toutefois ce portail est souvent désigné d'après son url d'accès, "https://scihub.copernicus.eu/", comme SciHub. Et c'est le nom qui sera utilisé dans le reste de cet article.

!!! warning
    Ne pas confondre Scihub site copernicus d'accès aux données Sentinel avec sci-hub le fameux site pirate d'accès aux publications scientifiques.

Le site Scihub offre principalement deux services : recherche de données et téléchargement de données.
Ces fonctionnalités sont disponibles soit graphiquement via un site internet soit via des [API](https://scihub.copernicus.eu/userguide/APIsOverview).
Ces dernières sont adaptées des API REST de type [OpenSearch](https://www.opensearch.org/) ou [OData,(Open Data Protocol)](https://www.odata.org/).
L'accès aux données est gratuit pour toute personne mais il existe toutefois une limitation de débit et du nombre de téléchargement en parallèle possible par utilisateur.
La communauté d'utilisateur a développé différents outils open-source permettant de faciliter l'utilisation des ces API dans votre langage de programmation préféré, par exemple en python l'outil [SentinelSat](https://sentinelsat.readthedocs.io/en/stable/).

!!! note
    Le code du portail scihub est lui même opensource via le projet **sentineldatahub**. Liens pour la [documentation](https://sentineldatahub.github.io/DataHubSystem/index.html) et le [github](https://github.com/SentinelDataHub/DataHubSystem)

Afin de faciliter la diffusion large des données Sentinel, différents portails nationaux (appelés miroirs) sont également venus compléter l'offre de diffusion et accès aux données.
On peut citer par exemple [le portail autrichien](https://data.sentinel.zamg.ac.at/dhus/#/home), [le portail australien](https://www.copernicus.gov.au/data-access) et bien sur [PEPS un des portails français](https://peps.cnes.fr/rocket/#/home).

En France il existe actuellement deux portails nationaux d'accès aux données Sentinel : [PEPS](https://peps.cnes.fr/rocket/#/home) et [THEIA](https://theia.cnes.fr/atdistrib/rocket/#/home).

### PEPS

![logo PEPS](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/peps.png "Logo PEPS"){: .img-rdp-news-thumb }

[PEPS](https://peps.cnes.fr/rocket/#/home) (Plateforme d’Exploitation des Produits Sentinels) est un portail développé et maintenu par le CNES qui offre la recherche et le téléchargement des données Sentinel-1 et Sentinel-2.
Par rapport à l'offre de base Scihub, PEPS permet un accès un peu plus rapide aux données en France (meilleur débit) mais aussi des post-traitements de données supplémentaires comme l'extraction de bande ou l'orthorectification des données SAR Sentinel-1 sur la géométrie "grille" de diffusion des données Sentinel-2 via [S1-tiling](https://gitlab.orfeo-toolbox.org/s1-tiling/s1tiling).

### THEIA

![logo Theia](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/theia.jpg "Logo Theia"){: .img-rdp-news-thumb }

[THEIA](https://theia.cnes.fr/atdistrib/rocket/#/home) est une composante de l'infrastructure de recherche [Data-Terra](https://www.data-terra.org/) centrée sur l'étude des surfaces continentales.
Elle a, en particulier, pour objectif de faciliter l'accès aux données nécessaires pour la recherche et les études pour l'observation de la terre.
Dans ce cadre le site THEIA permet de rechercher et télécharger un certain nombre de données d'observation de la terre dont des données Sentinel.
Les fonctionnalités sont disponibles graphiquement via l'interface web ou bien via une API REST.
Par rapport à PEPS ou scihub, le site THEIA ne fournit pas d'accès aux données SAR Sentinel-1.
Mais par contre il propose des données Sentinel-2 avec une meilleure calibration radiométrique (en utilisant la chaine de traitement [MAJA](https://www.cesbio.cnrs.fr/outils/maja/)) pour les données de niveau L2A, ainsi que des données de niveau [L3A](https://labo.obs-mip.fr/multitemp/theias-sentinel-2-l3a-monthly-cloud-free-syntheses/) qui sont des synthèses mensuelles des images Sentinel L2A.
Ces dernières sont pratiques pour avoir des images avec moins de nuages et diminuer le volume de données à traiter.
En plus des données Sentinel, THEIA donne aussi accès à des produits dérivés comme la carte d'occupation des sol [OSO](https://www.theia-land.fr/en/ceslist/land-cover-sec/) ou une carte de couverture 'neige' et des images SPOT et Landsat.

Certaines infrastructures géographiques régionales proposent également un accès local aux données Copernicus : [mviewer geobretagne](https://geobretagne.fr/pub/dreal_b/mviewer/?config=../apps/teledetection/config.xml)

## Saison 2 : here comme the dragons, GAFAM et réponse européene

Assez rapidement après la mise à disposition des données Sentinel-2 en open-data Amazon et Google ont aussi récupéré ces donnés afin de les intégrer dans leurs plateformes respectives.
Pour Google cela s'est fait via leur mise à disposition dans Google Earth Engine (GEE) qui est accessible de façon gratuite pour les étudiants et chercheurs.
Et du côté d'Amazon, ces données ont été mises à disposition dans un [répertoire de données open-data](https://registry.opendata.aws/sentinel-2/) hebergé sur les services Amazon (bucket S3), cela facilitant entre autre leur exploitation dans l'offre de service Amazon.
Il faut noter que les données Landsat diffusées en open-data avaient déjà ouvert la voie pour ces modes de diffusion de données satellites par les GAFAM.

En 2018, un peu en réponse aux GAFAM, l'Europe a lancé un appel à candidature pour la mise en place de plateformes "cloud" proposant un accès simplifié et efficace aux données Sentinel afin d'aider aux développements de nouveaux services.
Quatre DIAS (Data and Information Access Service) ont alors été retenus pour une période de quatre ans.

Par rapport aux plateformes Scihub et PEPS/THEIA l'objectif des DIAS était de fournir des services payants permettant aux entreprises et acteurs publiques de développer plus facilement des applications et services utilisant les données Sentinel.
Le but était par exemple d'éviter qu'un organisme ait à télécharger et stocker l'intégralité des données Sentinel-2 afin de lancer un calcul automatique de carte d'occupation des sols ou autres produit dérivé.
Le volume des données Sentinel pour un an d'acquisition sur un pays en Europe étant de l'ordre d'une dizaine à quelques centaines de To selon la taille du pays, traiter un tel volume nécessite donc, sans DIAS, un temps non négligeable de récupération des données et un coût d'infrastructure de stockage conséquent.
Les DIAS offrent une alternative en hébergeant ces données et en proposant des ressources de calculs (serveurs clouds) ayant un accès rapide à celles-ci. L'accès aux données Sentinel étant gratuit depuis les plateformes DIAS mais l'accès aux ressources de calcul payant.

Pour détailler, un peu plus, on peut considérer un DIAS comme étant composé de :

* une **infrastructure cloud** : soit un accès à des serveurs de calcul et du stockage de données, etc. Donc des services de type OVH/Orange cloud/Google/Amazon.
* **un stockage et un catalogue de données Sentinel**. C'est à dire une gestion d'une solution d'ingestion, sauvegarde et accès aux différentes données Sentinel produites par Copernicus ainsi que des post-traitement "classiques" de données. Cela comprend donc le développement (code) et mise en place d'une architecture cloud appropriée ainsi que la gestion opérationnelle du service.
* Production et **offre d'API d'accès aux données** pour se connecter aux services et accéder aux données. Cela comprend aussi les fonctionnalités de gestion utilisateur centralisé et de facturation des services.
* **une offre de service et applications tierces** sur les données Sentinel du catalogue. Services produits par le consortium (défaut du DIAS) ou par un tier sur une "place de marché" et via paiement/abonnement au service

Les quatre consortiums choisis pour les DIAS étaient :

* [Creodias](https://creodias.eu/) : Consortium avec Creotech Instrument (Lead, gestion projet), CloudFerro (cloud + données Sentinel), Sinergise (accès données) ainsi que WIZIPISI et Geomatys (traitement de données).
* [Mundi](https://mundiwebservices.com/) : Consortium avec T-System pour l'infra (cloud), Atos pour l'opérationnel/management de la plateforme et Sinergise pour l'ajout de service de visualisation et API sur les données. (DLR, e-Geos, EOX, GAF, Sinergise, Spacemetric, Thales Alenia Space and T-Systems, which is led by Atos)
* [Onda](https://www.onda-dias.eu/cms/) : Serco (Lead) OVH (cloud infra), GAEL Sytem (data access solution), Sinergise (web spatial data applications /API)
* [Sobloo](https://sobloo.eu/index.html) : Orange Business Services (cloud), Airbus (data provider)  Capgemini. Lead par Airbus, Capgemini apporte ses logiciels de traitement des données et Orange fournit sa solution cloud grand public Flexible Engine

A ces quatres DIAS s'est ajouté un cinquième, [WEKEO](https://www.wekeo.eu/), qui est plus dédié sur la communauté météo/océanique.
Une étude comparative de ces DIAS est disponible sur le [gitlab IDGEO](https://gitlab.com/idgeo_public/etude-dias).

Au niveau européen, un cas d'application (clients) de ces offres DIAS a été, entre autre, leur utilisation par les différents organismes de contrôles et paiements associés à la PAC (Politique Agricole Commune) pour la mise en place d'un "monitoring CAP".
En effet l'Europe a souhaité faire évoluer les contrôles terrain ponctuels associés aux versemment des aides PAC vers un ["monitoring"](https://publications.jrc.ec.europa.eu/repository/handle/JRC112913) exhaustif spatiallement et réalisé de manière semi-automatique par l'exploitation des données Sentinel-1 et 2.
Ces dernières devant permettre entre autre de vérifier la présence ou non d'activité agricoles (présence de culture annuelle, détection de fauche de prairie etc..) sur une parcelle donnée.
