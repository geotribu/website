---
title: Évolution de l'accès aux données Copernicus
subtitle: Accès aux données Copernicus et Sentinel
authors:
    - Nicolas DAVID
categories:
    - article
comments: true
date: 2023-03-07
description: Évolution des portails d'accès aux données europénnes de la constellation satellites Sentinel en 2023
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/copernicus_logo.png
license: beerware
robots: index, follow
tags:
    - COG
    - open data
    - satellite
    - Sentinel-2
    - télédétection
    - WMS
---

# Accès aux données Copernicus, partie 3 : évolution de l'accès aux données Copernicus

:calendar: Date de publication initiale : 7 mars 2023

## Introduction

![icône satellite](https://cdn.geotribu.fr/img/logos-icones/divers/satellite.png "icône satellite"){: .img-thumbnail-left }

L'Europe fait évoluer, en 2023, les possibilités d'accès aux différentes données des satellites de la constellation Sentinel via la création du "Copernicus Data Space Ecosytem" : [dataspace.copernicus.eu](https://dataspace.copernicus.eu/).
Le lancement de ce nouveau portail est donc une bonne occasion de revenir un peu sur l'historique du programme Sentinel ainsi que les différentes possibilités d'accéder aux données open-data Sentinel puis de détailler les fonctionnalités prévues pour ce nouveau service au cours de trois articles, chacun dédié à une partie pour faciliter la lecture et le "picorage" d'information à ceux qui connaissent déjà le sujet.

Ce troisième article se propose de détailler les fonctionnalités prévues pour ce nouveau service.
En particulier, outre le téléchargement des données Sentinel en Open-data, leur accès via différents services "free" de plus hauts niveaux est au programme, soit : visualisation des données via des flux, accès facilité aux données anciennes, utilisation des technologies dites "cloud ready", etc.

Série **Accès aux données Copernicus/Sentinel** :

* [Partie 1 : données OCS et Sentinel](2023-02-21_portails-copernicus-1-donnees.md).
* [Partie 2 : portails d'accès, 'the road so far'](2023-02-28_portails-copernicus-2-passe.md).

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Accès aux données Sentinel Teaser Saison 3 : "There can be only one"

Après quatre ans de retours d'expériences sur le déploiement et l'exploitation des DIAS, leur contrat arrivant à terme, l'Europe à choisi de faire évoluer son offre de services (gratuite et payante) d'accès aux données Sentinel.

![Portail dataspace](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/dataspace_accueil.png "Portail dataspace - Crédits ESA"){: .img-center loading=lazy }

Concrètement l'évolution consiste à sélectionner un consortium (décembre 2022) afin d'opérer d'une part une nouvelle version du portail open-data européen Scihub qui offrira des fonctionnalités similaires aux DIAS mais en une version gratuite, avec toutefois une limitation de quota, et d'autre part à offrir une version payante de ce service aux chercheurs, organismes publiques et industriels qui le souhaitent.
Cette version "non free" doit permettre de disposer de ressources de stockage/calcul et d'accès aux services non limités moyennant finance.

Le déploiement de ce nouveau service a commencé depuis fin janvier 2023 avec la mise en place de service dans la continuité de ceux offerts par Scihub et s'étoffera progressivement de nouveaux services (plutôt issus des offres DIAS actuelles) jusqu'à juin 2023 où le service devra avoir atteint sa phase opérationnelle complète, et date à laquelle l'ancien service Scihub devrait être arrêté.

![Portail dataspace service](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/dataspace_service_description.png "Portail dataspace service- Crédits ESA"){: .img-center loading=lazy }

Le premier contrat d'exploitation de ce nouveau service est d'une durée de six ans avec une extension possible de dix ans, soit possiblement une continuité de service sur seize ans.  
Le consortium qui a été retenu est constitué d'industriels participants aux DIAS Mundi et Creodias : T-Systems, CloudFerro, Sinergise, VITO,  DLR, ACRI-ST et RHEA

* [T-System](https://www.telekom.com/en/media/media-information/archive/copernicus-data-space-1024098) : fournisseur de service et infra cloud.
* [CloudFerro](https://cloudferro.com/en/news/cloudferro-and-its-partners-are-building-copernicus-data-access-service/) : exploitation de l'infra T-System pour y déployer et mettre en place une solution de stockage et accès aux données Sentinel.
* [Sinergise](https://sinergise.com/en/news/copernicus-data-access-service-delivers-first-results) : développement d'une offre de service sur l'accès aux données Sentinel (API de téléchargement, visualisation etc..) et d'un portail de visualisation et d'accès aux données.
* [VITO](https://remotesensing.vito.be/new-copernicus-data-access-service-kicked) : développement d'une offre de service/accès basé sur OpenEo.
* [DLR](https://www.dlr.de/content/en/articles/news/2023/01/20230124_new-data-platform-to-host-copernicus-earth-observation-data.html) : expertise archivage, traitement de données satellites (SAR / Sentinel 1 en particulier).
* [ACRI-ST](https://www.acri-st.fr/fr/portfolio) : expertise exploitation et traitement de données satellites Sentinel (Sentinel 2 et 3).
* [RHEA](https://www.rheagroup.com/fr/rhea-accompagne-le-deploiement-du-nouvel-ecosysteme-de-donnees-spatiales-copernicus/) apport et traitement des données des "mission contributives" Copernicus (CCM) ainsi que le contrôle de leur accès. Ces données n'étant pas toutes open-data/open-access.

A noter que la mise en place de ce portail s'inscrit dans la stratégie européenne concernant [destination earth](https://digital-strategy.ec.europa.eu/en/policies/destination-earth) un projet européen sur la création de "#Digitial Twins".

----

## Détails de la nouvelle offre d'accès Sentinel

D'un point de vue communication le nom associé à l'offre de service européenne a donc évolué et est devenu "Copernicus Data Space Ecosystem" associé à l'url [dataspace.copernicus.eu](https://dataspace.copernicus.eu/).

La nouvelle offre de service offrira une continuité par rapport à l'ancienne et devrait conserver les services existants de recherche et téléchargement des données Sentinel.
Mais elle doit aussi proposer plusieurs nouveautés en particulier concernant les interfaces *"machine to machine"*. Une première description de ces services est [disponible](https://documentation.dataspace.copernicus.eu/_docs/CDSE-SDE-TSY_Service%20Description%20and%20Evolution.pdf).

![dataspace roadmap](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/dataspace_RoadmapSummary.png "dataspace roadmap - Crédits ESA"){: .img-center loading=lazy }

### Service de visualisation et accès interactif

Une première nouveauté de service devrait être l'arrivée de la mise à disposition, via les outils de l'entreprise Sinergise, de flux de visualisation de données respectant les normes OCG WMS, WMTS (tuile raster).
Cela sera accompagné d'un portail de visualisation/récupération des données basé sur l'offre [EOBrowser](https://apps.sentinel-hub.com/eo-browser/) de Sinergise.

Une illustration de ce visualisateur pour des données Sentinel-2 récentes en fausse couleur infrarouge sur Clermont-Ferrand :

![dataspace browser clermont](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/dataspace_browser_clermont_ir.png "dataspace browser clermont - Crédits IGN"){: .img-center loading=lazy }

De plus une mise à disposition de service [JupyterLab](https://jupyter.org/) est prévue pour faciliter l'accès aux données de façon interactive dans des environnements de codes (plutôt basés python a priori).
On pense ici plutôt à un équivalent google colab et à ce que les DIAS offrent déjà comme service d'exploration de données.

![creodias jupyterhub](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/creodias_jupyterlab.jpg "creodias jupyterhub - Crédits ESA"){: .img-center loading=lazy }

### Arrivée de STAC et COG

![logo COG](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/COG_logo.png "Logo COG"){: .img-thumbnail-left }

Une première évolution prévue est une diversification des modes d'accès et téléchargement à ces données.
Aujourd'hui l'accès aux données Sentinel se fait par granules (S1) ou dalles (S2) représentant des zones géographiques de plusieurs centaines de kilomètres ([tuiles de type MGRS](https://labo.obs-mip.fr/multitemp/the-sentinel-2-tiles-how-they-work/) de 110km*110km pour Sentinel-2) dans le format de l'ESA (JPEG 2000).
Le nouveau "dataspace" Copernicus offrira en plus un accès aux données selon les protocoles et formats "cloud ready" [STAC](https://stacspec.org/en) (catalogue de données) et [COG (cloud optimised geotiff)](https://www.cogeo.org/) et permettra d'accéder seulement à la partie des données souhaitée, que cela soit au niveau des bandes spectrales ou de l'emprise géographiques.

Cela sera probablement effectué via un accès à un bucket S3 comme l'offre actuelle d'Amazon et une utilisation de ces services dans un script python devrait ressembler à :

``` py
# recherche de données sur catalogues STAC
import satsearch
import rasterio

bbox = [35.48, -3.24, 35.58, -3.14] # (min lon, min lat, max lon, max lat)
dates = '2020-07-01/2020-08-15'

URL='https://earth-search.aws.element84.com/v0' # changer par url officielle dataspace
results = satsearch.Search.search(
    url=URL,
    collections=['sentinel-s2-l2a-cogs'], # note collection='sentinel-s2-l2a-cogs' fictive
    datetime=dates,
    bbox=bbox,  
    sort=['<datetime'])

# lecture des données COG directement à partir de l'url
# eventuellement lecture d'une sous partie de l'image
window = rasterio.windows.Window(1024, 1024, 1280, 2560)
band = 1

with rasterio.open(fp) as src:
    subset = src.read(band, window=window)

```

### Offre de données Sentinel

Le nouveau portail devrait offrir un accès à l'ensemble des données Sentinel :
Sentinel-1 SLC et GRD  L2 OCN, Sentinel-2 L1C and L2A, Sentinel-3 and Sentinel-5P L1 et L2.
À cela, doit s'ajouter un accès aux "Copernicus Contributing Missions data".
Un exemple de ce type de données est la [couverture satellite de l'Europe pour 2018](https://land.copernicus.eu/imagery-in-situ/european-image-mosaics/very-high-resolution/very-high-resolution-image-mosaic-2018-true-colour-2m) ayant servi à la production des données Corinne Land Cover millésime 2018.

![VHR_IMAGES_2018 COPERNICUS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/VHR_IMAGES_2018_COPERNICUS.png "VHR_IMAGES_2018 COPERNICUS - Crédits ESA"){: .img-center loading=lazy }

!!! note
    Par contre les données d'apprentissage utilisées pour la production semi-automatique des couches HRL ne semblent pas au programme. Donc on ne peut pas encore considérer ces couches comme étant très reproductibles et suivant les principes F.A.I.R.

Et enfin, de la même façon que le portail PEPS en France, un ensemble de fonctionnalités de post-traitements à la demande devrait être disponible.
Entre autre cela devrait couvrir la possibilité d'effectuer des corrections atmosphériques avec le processeur MAJA et la production de produits dérivés Sentinel-1 comme la cohérence entre 2 dates (produit utilisé par exemple dans les algorithmes pour le suivi des cultures).  
Ces offres de traitements de données devraient aussi suivre les recommandations pour les produits CARD4L, [CEOS Analysis Ready Data for Land](https://ceos.org/ard/)

À noter, qu'a priori, il ne devrait plus y avoir de notions de données online/offline dépendant de la date d'acquisition des données.
Les données offline étant les données datant de plus de X mois et donc l'accès se fait en différé avec une demande de désarchivage puis un téléchargement.
Toutes les données produites depuis 2014 devraient donc être accessibles via un accès rapide, cela pour faciliter les traitements demandant un accès à des données sur un intervalle de temps long.

### Accès aux données via WCS et OpenEO

En plus de l'accès "simple" aux données le nouveau service devrait aussi offrir deux nouveaux types d'accès permettant des post-traitements à la volée des données.

![illustration WCS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/200px-OGC_WCS,_trim_and_slice_operations.png "illustration WCS - Crédits Wikipedia"){align=right }
D'une part, on devrait retrouver une offre d'API selon la norme [WCS](http://opengeospatial.github.io/e-learning/wcs/text/basic-main.html) de
l'OGC (via Sinergise) qui permet d'affiner la récupération des données Sentinel au strict nécessaire.
Cela est utile notamment pour des calculs simples, à la volée, entre bandes raster (de type calculatrice raster), un exemple possible étant le calcul d'une couche NDVI (indice de végétation) à partir des bandes spectrales rouge et infrarouge Sentinel-2 et donc de ne récupérer que deux bandes spectrales en WCS sur les treize bandes possibles.  

![logo OPENEO](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/openeo_logo.png "Logo OPENEO"){: .img-thumbnail-left }

D'autre part, un service [OpenEO](https://openeo.org/) devrait aussi être déployé (via VITO).
L'API OpenEO propose des fonctionnalités de type Google Earth Engine (GEE) ou datacube mais avec une API normalisée et pouvant être proposée par différents backend/fournisseurs.

![schema openeo](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/openeo_schema.png "schema openeo - Crédits OPENEO"){: .img-center loading=lazy }

Le but étant à la fois de proposer une alternative à GEE mais aussi d'assurer un certain niveau d'interopérabilité entre fournisseurs de services/données spatiales.

Pour illustrer voici un exemple d'utilisation avec un client javascript (pour changer des exemples python) tiré de la [documentation officielle](https://openeo.org/documentation/1.0/javascript/#full-example)

``` js
// Make the client available to the Node.js script
// Also include the Formula library for simple math expressions
const { OpenEO, Formula } = require('@openeo/js-client');

async function example() {
  // Connect to the back-end
  var con = await OpenEO.connect("https://earthengine.openeo.org");
  // Authenticate ourselves via Basic authentication
  await con.authenticateBasic("group11", "test123");
  // Create a process builder
  var builder = await con.buildProcess();
  // We are now loading the Sentinel-1 data over the Area of Interest
  var datacube = builder.load_collection(
    "COPERNICUS/S1_GRD",
    {west: 16.06, south: 48.06, east: 16.65, north: 48.35},
    ["2017-03-01", "2017-06-01"],
    ["VV"]
  );

  // Since we are creating a monthly RGB composite, we need three separated time ranges (March aas R, April as G and May as G).
  // Therefore, we split the datacube into three datacubes using a temporal filter.
  var march = builder.filter_temporal(datacube, ["2017-03-01", "2017-04-01"]);
  var april = builder.filter_temporal(datacube, ["2017-04-01", "2017-05-01"]);
  var may = builder.filter_temporal(datacube, ["2017-05-01", "2017-06-01"]);

  // We aggregate the timeseries values into a single image by reducing the time dimension using a mean reducer.
  var mean = function(data) {
    return this.mean(data);
  };
  march = builder.reduce_dimension(march, mean, "t");
  april = builder.reduce_dimension(april, mean, "t");
  may = builder.reduce_dimension(may, mean, "t");

  // Now the three images will be combined into the temporal composite.
  // We rename the bands to R, G and B as otherwise the bands are overlapping and the merge process would fail.
  march = builder.rename_labels(march, "bands", ["R"], ["VV"]);
  april = builder.rename_labels(april, "bands", ["G"], ["VV"]);
  may = builder.rename_labels(may, "bands", ["B"], ["VV"]);

  datacube = builder.merge_cubes(march, april);
  datacube = builder.merge_cubes(datacube, may);

  // To make the values match the RGB values from 0 to 255 in a PNG file, we need to scale them.
  // We can simplify expressing math formulas using the openEO Formula parser.
  datacube = builder.apply(datacube, new Formula("linear_scale_range(x, -20, -5, 0, 255)"));

  // Finally, save the result as PNG file.
  // In the options we specify which band should be used for "red", "green" and "blue" color.
  datacube = builder.save_result(datacube, "PNG", {
    red: "R",
    green: "G",
    blue: "B"
  });

  // Now send the processing instructions to the back-end for (synchronous) execution and save the file as result.png
  await con.downloadResult(datacube, "result.png");
}

// Run the example, write errors to the console.
example().catch(error => console.error(error));
```

Ce code devant permettre d'arriver à l'image ci-dessous :
![resultat exemple openeo js](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/openeo-getting-started-result-example-7820ee84.jpg "resultat exemple openeo js- Crédits OPENEO"){: .img-center loading=lazy }

!!! note
    Beaucoup de ces nouveaux services sont en partie issus de travaux
    menés dans différents projets européens lors des dernières années :
    [OPENEO](https://openeo.org/)

## Conclusion

J'espère que cette série d'articles vous aura plu et donné l'envie d'utiliser les données du programme Copernicus, qui offrent déjà de très belles opportunités pour l'observation des territoires et promettent d'en offrir encore plus dans l'avenir, que cela soit au niveau de données disponibles ou bien des différents outils de l'écosystème Copernicus.  
Pour commencer à prendre en main ces données et comme je trouve que juste leur visualisation est déjà jolie je ne peux que vous conseiller d'aller jouer un peu avec le nouvel outil de génération de "timelaps animation" disponible sur le nouveau [visualisateur du dataspace copernicus](https://dataspace.copernicus.eu/browser). Voir quelques exemples et un [petit tutoriel](https://medium.com/sentinel-hub/timelapse-in-eo-browser-962a78e3ee53) sur le blog sentinel-hub.

Et bien sûr, n'hésitez pas à revenir partager ici vos exemples d'utilisation ou vos plus jolies visualisations de données !

<!-- geotribu:authors-block -->
