---
title: Portails d'accès aux données Sentinel, 'the road so far'
subtitle: Accès aux données Copernicus et Sentinel
authors:
    - Nicolas DAVID
categories:
    - article
comments: true
date: 2023-02-28
description: Historique des portails d'accès aux données Sentinel en Europe et en France et description de leur grandes fonctionnalités
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/copernicus_logo.png
license: beerware
robots: index, follow
tags:
    - open data
    - OSO
    - PEPS
    - satellite
    - Sentinel-2
    - télédétection
    - Theia
---

# Accès aux données Copernicus, partie 2 : portails d'accès aux données Sentinel, 'the road so far'

:calendar: Date de publication initiale : 28 février 2023

## Introduction

![icône satellite](https://cdn.geotribu.fr/img/logos-icones/divers/satellite.png "icône satellite"){: .img-thumbnail-left }

L'Europe fait évoluer, en 2023, les possibilités d'accès aux différentes données des satellites de la constellation Sentinel via la création du "Copernicus Data Space Ecosytem" : [dataspace.copernicus.eu](https://dataspace.copernicus.eu/).
Le lancement de ce nouveau portail est donc une bonne occasion de revenir un peu sur l'historique du programme Sentinel ainsi que les différentes possibilités d'accéder aux données open-data Sentinel puis de détailler les fonctionnalités prévues pour ce nouveau service au cours de trois articles, chacun dédié à une partie pour faciliter la lecture et le "picorage" d'information à ceux qui connaissent déjà le sujet.

Ce nouveau portail doit prendre la suite du portail actuel [scihub.copernicus.eu](https://scihub.copernicus.eu) d'accès aux données open-data Sentinel ainsi que de certains des actuels DIAS (**D**ata **I**nformation and **A**cces **S**ervice) pour l'offre de service payante associée.
Dans ce deuxième article nous revenons donc sur l'historique des différents portails d'accès aux données Sentinel et des fonctionnalités qu'ils ont offertes.

Pour un rappel sur les données Sentinel voir le [premier article](2023-02-21_portails-copernicus-1-donnees.md) et pour les personnes intéressées par le nouveau portail aller directement au [troisième article](2023-03-07_portails-copernicus-3-futur.md).
Série **Accès aux données Copernicus/Sentinel** :

* [Partie 1 : données OCS et Sentinel](2023-02-21_portails-copernicus-1-donnees.md).
* [Partie 3 : évolution de l'accès aux données Copernicus](2023-03-07_portails-copernicus-3-futur.md).

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Saison 1 : portails open-data européens et nationaux

L'Europe a accompagné le lancement et la mise en production des différents satellites Sentinel par la mise en place de services d'accès aux données diffusées en open data.

### Copernicus Open Access Hub : SciHub

Le premier service d'accès aux données a été le Copernicus [Open Access Hub](https://scihub.copernicus.eu/) ouvert en 2014 pour la diffusion des données du premier satellite Sentinel-1A. Toutefois ce portail est souvent désigné d'après son url d'accès, <https://scihub.copernicus.eu/>, comme "SciHub".  
Et c'est le nom qui sera utilisé dans le reste de cet article.

![Portail scihub illustration](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/scihub_copernicus_access_hub_1.jpg "Portail scihub example page - Crédits ESA"){: .img-center loading=lazy }

!!! warning "Attention, risque de confusion"
    Ne pas confondre Scihub site copernicus d'accès aux données Sentinel avec sci-hub le fameux site pirate d'accès aux publications scientifiques.

Le site Scihub offre principalement deux services : recherche de données et téléchargement de données.  
Ces fonctionnalités sont disponibles soit graphiquement via un site internet soit via des [API](https://scihub.copernicus.eu/userguide/APIsOverview).
Ces dernières sont adaptées des API REST de type [OpenSearch](https://www.opensearch.org/) ou [OData (_Open Data Protocol_)](https://www.odata.org/).
L'accès aux données est gratuit pour toute personne mais il existe toutefois une limitation de débit et du nombre de téléchargement en parallèle possible par utilisateur.

Concrètement un appel à l'API OpenSearch pour chercher les images Sentinel-2 disponibles aux alentours de Clermont-Ferrand depuis le début de l'année ressemble alors à :

```sh
URL="https://scihub.copernicus.eu/dhus/search?q="
BBOX="footprint:'Intersects(POLYGON((3.0 47.4, 3.1 47.4,3.1 47.5,3.0 47.5,3.0 47.4)))'"
DATES="beginposition:[2023-01-01T00:00:00.000Z TO 2023-02-14T00:00:00.000Z]"
IMG_TYPE="producttype:S2MSI2A AND cloudcoverpercentage:[0 TO 50]"

QUERY="${URL}${BBOX} AND ${DATES} AND {IMG_TYPE}"

wget --no-check-certificate --user={USERNAME} --password={PASSWORD} ${QUERY}
```

!!! note
    Le code du portail scihub est lui même opensource via le projet **sentineldatahub**. Liens pour la [documentation](https://sentineldatahub.github.io/DataHubSystem/index.html) et le [github](https://github.com/SentinelDataHub/DataHubSystem).

La communauté d'utilisateurs a développé différents outils open-source permettant de faciliter l'utilisation de ces API dans votre langage de programmation préféré.

Ici un exemple d'utilisation en python de l'outil [SentinelSat](https://sentinelsat.readthedocs.io/en/stable/), pour télécharger des données Sentinel-2 du début d'année vers Clermont.

``` py
# imports
from datetime import date
from sentinelsat import SentinelAPI


# connect to the API
api = SentinelAPI('user', 'password', 'https://apihub.copernicus.eu/apihub')

# recherche par polygone, date et type de données
# qq part à Clermont
footprint = "POLYGON((3.0 47.4, 3.1 47.4, 3.1 47.5, 3.0 47.5, 3.0 47.4))"
products = api.query(
    footprint,
    # entre janvier et mi fevrier 2023
    date=('20230101', date(2023, 2, 14)),
    # données sentinel 2
    platformname='Sentinel-2',
    # de niveau L2A (sentinel 2, sensor MSI niveau 2A)
    producttype='S2MSI2A',
    # avec un maximum de 50% de couverture nuageuse
    cloudcoverpercentage=(0, 50))

# download all results from the search
api.download_all(products)
```

Afin de faciliter la diffusion large des données Sentinel, différents portails nationaux (appelés miroirs) sont également venus compléter l'offre de diffusion et d'accès aux données.
On peut citer par exemple [le portail autrichien](https://data.sentinel.zamg.ac.at/dhus/#/home), [le portail australien](https://www.copernicus.gov.au/data-access) et bien sur [PEPS un des portails français](https://peps.cnes.fr/rocket/#/home). Chacun facilitant l'accès aux données couvrant son territoire géographique.

### Portails français PEPS et THEIA

![logo PEPS](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/peps.png "Logo PEPS"){: .img-thumbnail-left }

En France il existe actuellement deux portails nationaux d'accès aux données Sentinel : [PEPS](https://peps.cnes.fr/rocket/#/home) et [THEIA](https://theia.cnes.fr/atdistrib/rocket/#/home).

[PEPS](https://peps.cnes.fr/rocket/#/home) (Plateforme d’Exploitation des Produits Sentinel) est un portail développé et maintenu par le CNES qui offre la recherche et le téléchargement des données Sentinel-1 et Sentinel-2.
Par rapport à l'offre de base Scihub, PEPS permet un accès un peu plus rapide aux données en France (meilleur débit) mais aussi des post-traitements de données supplémentaires comme l'extraction de bande ou l'orthorectification des données SAR Sentinel-1 sur la géométrie "grille" de diffusion des données Sentinel-2 via [S1-tiling](https://gitlab.orfeo-toolbox.org/s1-tiling/s1tiling).

![Portail PEPS CNES](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/PEPS_CNES_captrue_site.png "Portail PEPS CNES - Crédits PEPS"){: .img-center loading=lazy }

![logo Theia](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/theia.jpg "Logo Theia"){: .img-thumbnail-left }

[THEIA](https://theia.cnes.fr/atdistrib/rocket/#/home) est une composante de l'infrastructure de recherche [Data-Terra](https://www.data-terra.org/) centrée sur l'étude des surfaces continentales.
Elle a, en particulier, pour objectif de faciliter l'accès aux données nécessaires pour la recherche et les études pour l'observation de la Terre.
Dans ce cadre le site THEIA permet de rechercher et télécharger un certain nombre de données d'observation de la Terre dont des données Sentinel.
Les fonctionnalités sont disponibles graphiquement via l'interface web ou bien via une API REST.
Par rapport à PEPS ou Scihub, le site THEIA ne fournit pas d'accès aux données SAR Sentinel-1.
Mais par contre il propose des données Sentinel-2 avec une meilleure calibration radiométrique (en utilisant la chaîne de traitement [MAJA](https://www.cesbio.cnrs.fr/outils/maja/)) pour les données de niveau L2A, ainsi que des données de niveau [L3A](https://labo.obs-mip.fr/multitemp/theias-sentinel-2-l3a-monthly-cloud-free-syntheses/) qui sont des synthèses mensuelles des images Sentinel L2A.
Ces dernières sont pratiques pour avoir des images avec moins de nuages et diminuer le volume de données à traiter.
En plus des données Sentinel, THEIA donne aussi accès à des produits dérivés comme la carte d'occupation des sols [OSO](https://www.theia-land.fr/en/ceslist/land-cover-sec/) ou une carte de couverture 'neige' et des images SPOT et Landsat.

![Portail THEIA land](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/theia_land_page.jpg "Portail THEIA Land - Crédits THEIA"){: .img-center loading=lazy }

Certaines infrastructures géographiques régionales proposent également un accès local aux données Copernicus : [mviewer geobretagne](https://geobretagne.fr/pub/dreal_b/mviewer/?config=../apps/teledetection/config.xml)

!!! note
    Les portails PEPS et THEIA utilisent l'outil [RESTO](https://github.com/jjrom/resto) dont le code est aussi disponible sur GitHub.

----

## Saison 2 : here come the dragons, GAFAM et réponse européenne

### Google Earth Engine et Open Data AWS

Assez rapidement après la mise à disposition des données Sentinel-2 en open-data Amazon et Google ont aussi récupéré ces données afin de les intégrer dans leurs plateformes respectives.
Pour Google cela s'est fait via leur mise à disposition dans Google Earth Engine (GEE) qui est accessible de façon gratuite pour les étudiants et chercheurs.
Et du côté d'Amazon, ces données ont été mises à disposition dans un [répertoire de données open-data](https://registry.opendata.aws/sentinel-2/) hebergé sur les services Amazon (bucket S3), cela facilitant entre autre leur exploitation dans l'offre de service Amazon.
Il faut noter que les données Landsat diffusées en open-data avaient déjà ouvert la voie pour ces modes de diffusion de données satellites par les GAFAM.

![Exemple open data AWS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/aws-odr-s2-1024x702.png "Exemple open data AWS - Crédits Elements84"){: .img-center loading=lazy }

### DIAS : Data and Information Access Service

En 2018, un peu en réponse aux GAFAM, l'Europe a lancé un appel à candidature pour la mise en place de plateformes "cloud" proposant un accès simplifié et efficace aux données Sentinel afin d'aider aux développements de nouveaux services.
Quatre DIAS (Data and Information Access Service) ont alors été retenus pour une période de quatre ans.

Par rapport aux plateformes Scihub et PEPS/THEIA l'objectif des DIAS était de fournir des services payants permettant aux entreprises et acteurs publiques de développer plus facilement des applications et services utilisant les données Sentinel.
Le but était par exemple d'éviter qu'un organisme ait à télécharger et stocker l'intégralité des données Sentinel-2 afin de lancer un calcul automatique de carte d'occupation des sols ou autre produit dérivé.
Le volume des données Sentinel pour un an d'acquisition sur un pays en Europe étant de l'ordre d'une dizaine à quelques centaines de To selon la taille du pays, traiter un tel volume nécessite donc, sans DIAS, un temps non négligeable de récupération des données et un coût d'infrastructure de stockage conséquent.
Les DIAS offrent une alternative en hébergeant ces données et en proposant des ressources de calculs (serveurs clouds) ayant un accès rapide à celles-ci. L'accès aux données Sentinel étant gratuit depuis les plateformes DIAS mais l'accès aux ressources de calcul payant.

Pour détailler, un peu plus, on peut considérer un DIAS comme étant composé de :

* une **infrastructure cloud** : soit un accès à des serveurs de calcul et du stockage de données, etc. Donc des services de type OVH/Orange cloud/Google/Amazon.
* **un stockage et un catalogue de données Sentinel**. C'est à dire une gestion d'une solution d'ingestion, sauvegarde et accès aux différentes données Sentinel produites par Copernicus ainsi que des post-traitements "classiques" de données. Cela comprend donc le développement (code) et mise en place d'une architecture cloud appropriée ainsi que la gestion opérationnelle du service.
* Production et **offre d'API d'accès aux données** pour se connecter aux services et accéder aux données. Cela comprend aussi les fonctionnalités de gestion utilisateur centralisé et de facturation des services.
* **une offre de service et applications tierces** sur les données Sentinel du catalogue. Services produits par le consortium (défaut du DIAS) ou par un tiers sur une "place de marché" et via paiement/abonnement au service

![Creodias components](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/creodias_components.jpg "Creodias components - Crédits CREODIAS"){: .img-center loading=lazy }

Les quatre consortiums choisis pour les DIAS étaient :

* [Creodias](https://creodias.eu/) : Consortium avec Creotech Instrument (Lead, gestion projet), CloudFerro (cloud + données Sentinel), Sinergise (accès données) ainsi que WIZIPISI et Geomatys (traitement de données).
* [Mundi](https://mundiwebservices.com/) : Consortium avec T-System pour l'infra (cloud), Atos pour l'opérationnel/management de la plateforme et Sinergise pour l'ajout de service de visualisation et API sur les données. (DLR, e-Geos, EOX, GAF, Sinergise, Spacemetric, Thales Alenia Space and T-Systems, which is led by Atos)
* [Onda](https://www.onda-dias.eu/cms/) : Serco (Lead) OVH (cloud infra), GAEL Sytem (data access solution), Sinergise (web spatial data applications /API)
* [Sobloo](https://sobloo.eu/index.html) : Orange Business Services (cloud), Airbus (data provider)  Capgemini. Lead par Airbus, Capgemini apporte ses logiciels de traitement des données et Orange fournit sa solution cloud grand public Flexible Engine

![Icones DIAS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/DIAS_0.jpg "Icones DIAS - Crédits JRC"){: .img-center loading=lazy }

A ces quatres DIAS s'est ajouté un cinquième, [WEKEO](https://www.wekeo.eu/), qui est plus dédié sur la communauté météo/océanique.
Une étude comparative de ces DIAS est disponible sur le [gitlab IDGEO](https://gitlab.com/idgeo_public/etude-dias).

## Un exemple d'utilisation : le monitoring PAC

Au niveau européen, un cas d'application (clients) de ces offres DIAS a été, entre autre, leur utilisation par les différents organismes de contrôles et paiements associés à la PAC (Politique Agricole Commune) pour la mise en place d'un "monitoring PAC".
En effet l'Europe a souhaité faire évoluer les contrôles terrain ponctuels associés au versement des aides PAC vers un ["monitoring"](https://publications.jrc.ec.europa.eu/repository/handle/JRC112913), exhaustif spatialement, et réalisé de manière semi-automatique via l'exploitation des données Sentinel-1 et 2.
Ces dernières devant permettre entre autre de vérifier la présence ou non d'activités agricoles (présence de culture annuelle, détection de fauche de prairie etc..) sur une parcelle donnée.

Pour cela il peut être en particulier intéressant de calculer et extraire des profils temporels optiques ou radar sur chacune des parcelles agricoles à "monitorer".  Pour les détails techniques voir par exemple les différentes présentations du projet [Sen4CAP](http://esa-sen4cap.org/)

![Profil temporel S2](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/sen4cap_example_profil_s2_b.png "Profil temporel S2] - Crédits SEN4CAP"){: .img-center loading=lazy }

Le JRC diffuse une documentation possible d'une architecture permettant de calculer ces profils et autres opérations utiles au monitoring sur une infrastructure de l'un des DIAS. Voir [DIAS for CAP Checks by Monitoring](https://jrc-cbm.readthedocs.io/en/latest/dias4cbm_intro.html)

![JRC CBM DIAS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/cbm_dias_software.png "JRC CBM DIAS - Crédits JRC"){: .img-center loading=lazy }

----

## Quelques liens supplémentaires

Pour avoir une liste plus exhaustive des différents portails et des outils d'accès associés vous pouvez vous reporter par exemple à la page github : [awesome-sentinel](https://github.com/kr-stn/awesome-sentinel)

Et si vous vous demandez si cela est vraiment bien raisonnable de devoir avoir 42 outils différents de téléchargement de données selon les portails d'accès utilisés alors vous serez sûrement intéressés par l'outil [EODAG](https://eodag.readthedocs.io/en/stable/) développé en open-source par la société [C.S Group](https://www.csgroup.eu/en/).

<!-- geotribu:authors-block -->
