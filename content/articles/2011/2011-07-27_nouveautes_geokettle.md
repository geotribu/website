---
title: "Les nouveautés apportées par la version 2.0 de GeoKettle"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2011-07-27
description: "Les nouveautés apportées par la version 2.0 de GeoKettle"
tags:
    - ETL
    - GeoBI
    - GeoKettle
    - open source
---

# Les nouveautés apportées par la version 2.0 de GeoKettle

:calendar: Date de publication initiale : 27 juillet 2011

## Introduction

Les outils d'Extraction, de Transformation et de Chargement, plus connu sous l'acronyme anglais ETL (Extract, Transform and Load), sont utilisés pour gérer les flux informationnels générés par les organismes. Bien que conçus au départ pour l'univers décisionnel, il est désormais possible de les intégrer à votre architecture de données géographiques. Cela se fait grâce à l'utilisation d'ETL capables de gérer la dimension spatiale.

![GeoKettle - ETL](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/ORG_Figure_ETLen.png "GeoKettle - ETL"){: .img-center loading=lazy }

> Source : [Spatialytics](http://www.spatialytics.org/projects/geokettle/)

Historiquement, le premier produit capable de gérer la dimension spatiale était le fameux logiciel [FME](http://www.safe.com/fme/fme-technology/fme-desktop/) développé par la société [Safe](http://www.safe.com/). Mais, plus récemment, deux alternatives Open Source sont désormais disponibles. Toutes deux s'appuient sur des ETL (non spatiaux) déjà existants et y ajoutent la capacité de traiter des données géographiques. La première alternative, nommée [Spatial Data Integrator](http://talendforge.org/wiki/doku.php?id=sdi:mainpage&s%5B%5D=spatial&s%5B%5D=data&s%5B%5D=integrator) (SDI) se base sur [Talend Open Studio](http://fr.talend.com/products-data-integration/talend-open-studio.php) (TOS), la seconde nommée [GeoKettle](http://www.spatialytics.org/projects/geokettle/) se base elle sur [Pentaho data Integration](http://kettle.pentaho.com/) (PDI mais plus connu sous le nom de kettle).

Attardons-nous sur cette dernière. En effet, une nouvelle version de Geokettle est disponible depuis la semaine dernière. Attendue depuis longtemps, celle-ci intègre un grand nombre de [nouvelles fonctionnalités](http://wiki.spatialytics.org/doku.php?id=projects:geokettle:documentation:what_is_new_in_version_2.0) grâce notamment à l'intégration de nombreuses librairies Open Source à savoir, [OGR](http://www.gdal.org/ogr), [Sextante](http://sextante.forge.osor.eu/), [JTS](http://www.vividsolutions.com/jts/main.htm), [GeoTools](http://geotools.org/) et [deegree](http://www.deegree.org/). Découvrons ensemble ce que cette nouvelle version apporte.

![GeoKettle](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/geokettle.png "GeoKettle"){: .img-center loading=lazy }

## Intégration de nouveaux formats de données

Grâce à l'intégration de la librairie OGR, il est désormais possible d'accéder à une soixantaine de formats de formats de données en lecture et/ou en écriture. A cela s'ajoutent également de nouveaux composants permettant le traitement des données GML et KML ainsi que l'intégration des normes OGC Sensor Observation Service (SOS) et Catalog Web Service (CSW)

![GeoKettle - OGR](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/ogr_geokettle.png "GeoKettle - OGR"){: .img-center loading=lazy }

## Analyse spatiale

Grâce à l'intégration des librairies JTS et sextante, Geokettle s'est enrichi d'un grand nombre de fonctions spatiales. Ces fonctions sont dépendantes du type de géométrie comme cela est illustré par les deux images ci-dessous.

![GeoKettle - sextante](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/sextante_1.png "GeoKettle - sextante"){: .img-center loading=lazy }

![GeoKettle - sextante](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/sextante_2.png "GeoKettle - sextante"){: .img-center loading=lazy }

La réalisation d'opérations géométriques sur les entités est également possible :

![GeoKettle - analyse spatiale](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/spatial_analyse.png "GeoKettle - analyse spatiale"){: .img-center loading=lazy }

Ainsi que des calculs géométriques :

![GeoKettle - calcul](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/calcul.png "GeoKettle - calcul"){: .img-center loading=lazy }

## Enrichissement de l'interface

Enfin, concluons cette liste non exhaustive par l'ajout d'un module cartographique permettant de pré-visualiser les résultats des opérations. Cela représente à mon sens, l'une des fonctionnalités majeures de cette nouvelle version.

![GeoKettle - Carto](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/carto.png "GeoKettle - Carto"){: .img-center loading=lazy }

## Remarques & Conclusion

Comme le souligne Cedric Darbon d'[atolCd](http://blog.atolcd.com/?p=864), Geokettle entre dans le cour des grands avec cette nouvelle version. De nombreuses fonctionnalités ont été ajoutées et ce logiciel mérite largement sa place dans un système d'information géographique.

Mais, quelques détails mériteraient d'être améliorés. Ces remarques sont très subjectives car résultantes de ma seule opinion. Néanmoins, voici les quelques points que je soulignerai :

- **difficulté à localiser les extensions spatiales** : Pentaho Data Integration dispose d'origine d'un grand nombre de modules. Pour un utilisateur novice il peut être difficile et déroutant de ne pas réussir à identifier facilement ceux utiles aux SIG. Il serait peut-être intéressant de n'afficher que les modules spatiaux quand une recherche portant sur les mots "geo" ou "spatial" est effectuée.
- **Regroupement des fonctionnalités** : Il pourrait également être intéressant de regrouper les modules en fonction de leurs objectifs par exemple analyses spatiales, modification/création de géométries, etc. Cela permettrait d'identifier plus rapidement l'étape nécessaire.
- **Release early, release often** : Enfin, entre cette version et la précédente près de deux ans s'étaient écoulés. A l'avenir, espérons que les futures release seront plus régulières. Mais peut-être est-ce prévu dans cette version 2 ?

## Ressources complémentaires

Pour plus d'informations, n'hésitez pas à consulter :

- l'annonce officielle en [anglais](http://wiki.spatialytics.org/doku.php?id=projects:geokettle:documentation:what_is_new_in_version_2.0) et en [français](http://www.spatialytics.org/fr/blogue/geokettle-2-0%C2%A0-spatialytics-annonce-la-disponibilite-dune-nouvelle-version-de-letl-spatial-open-source/)
- l'article d'[osbi](http://www.osbi.fr/?p=2679)
- et celui d'[atolcd](http://blog.atolcd.com/?p=864)

----

<!-- geotribu:authors-block -->
