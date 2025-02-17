---
title: Les Open Buildings, des données bâtiments pour le Sud
subtitle: Les pros du bâtiment
authors:
    - Michel-Francis KISWESO
    - Guilhem ALLAMAN
categories:
    - article
comments: true
date: 2025-02-19
description: Présentation, guide d'import et d'extraction des Open Buildings, un jeu de données de bâti couvrant les pays du Sud et généré par Google
icon: fontawesome/solid/building
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/open_buildings/carte_telechargement_open_buildings.png
license: beerware
robots: index, follow
tags:
    - CSV
    - Google
    - OpenBuildings
    - QGIS
---

# Extraction des Open Buildings, un jeu de données de bâtiments pour le Sud

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

Les [Open Buildings](https://sites.research.google/gr/open-buildings/) sont un jeu de données, disponible [sous licence ODbL](https://fr.wikipedia.org/wiki/Open_Database_License), qui caractérise les empreintes des bâtiments dans les pays du Sud.

Ces bâtiments sont dérivés d’images satellites haute résolution, issus d'un traitement effectué par une équipe de recherche de Google au Ghana. Ils sont au nombre d'environ 1,8 milliard, sur une zone de 58 millions de km² et sur plusieurs continents : en Afrique, en Asie du Sud et du Sud-Est, en Amérique du Sud et Centrale, dans les Caraïbes...

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Description des données Open Buildings

La version actuelle de ce jeu de données est la troisième (v3), publiée en mai 2023. Geotribu abordait d'ailleurs la première version du dataset, qui couvrait l'Afrique uniquement, [lors d'une GeoRDP en 2021](../../rdp/2021/rdp_2021-08-27.md#cartographie-des-batiments-dafrique).

![Carte de densité de bâtiments en Afrique dans le dataset Google Open Buildings première version](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/google_oepn_buildings_building-density.png){: .img-center loading=lazy }

Chaque bâtiment, dans ce jeu de données, est représenté par :

- un polygone décrivant son empreinte au sol
- sa superficie en m²
- un score de confiance indiquant la probabilité qu’il s’agisse d’un bâtiment
- un [code Plus](https://fr.wikipedia.org/wiki/Open_Location_Code) correspondant au centre du bâtiment

Le type de bâtiment n'est pas renseigné, contrairement [aux données OpenStreetMap par exemple](https://wiki.openstreetmap.org/wiki/Key:building), seulement la géométrie et donc un score de confiance dont le seuil minimal de filtrage est fixé à 65%, ce qui peut parfois s'avérer assez bas (dis "camion!" :truck:).

Et la méthode de détection de la v2 [est décrite ici](https://arxiv.org/abs/2107.12283v2), qui explique notamment que c'est basé sur des images satellites de résolution 50cm.

## Importer les Open Buildings dans QGIS

Il existe des manières très _fancy_ de récupérer les OpenBuildings v3, qui feraient sensation lors d'une soirée mondaine. Via [Earth Engine en JavaScript notamment](https://developers.google.com/earth-engine/datasets/catalog/GOOGLE_Research_open-buildings_v3_polygons). Ou bien via [gsutil](https://cloud.google.com/storage/docs/gsutil_install), un outil [CLI](https://en.wikipedia.org/wiki/Command-line_interface) de _Gogole Claude Storage_.

Ici on va préférer le [KISS](https://en.wikipedia.org/wiki/KISS_principle) :kissing_smiling_eyes:, et le bon vieux CSV des familles : les Open Buildings sont regroupés en tuiles carrées, pour lesquelles il est possible de télécharger tous les bâtiments situés à l'intérieur de chaque tuile, [sur la carte du site officiel](https://sites.research.google/gr/open-buildings/#open-buildings-download), dans la partie `Download` :

![Carte de téléchargement des tuiles Open Buildings](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/open_buildings/carte_telechargement_open_buildings.png){: .img-center loading=lazy }

Le format fourni est donc du CSV. Pour cet exemple, nous téléchargerons [ce zip](https://storage.googleapis.com/open-buildings-data/v3/polygons_s2_level_4_gzip/0fd_buildings.csv.gz) qui couvre le Ghana et la partie Est de la Côte d'Ivoire, pour une taille de 1.5 GO (3.4 GO une fois dézippé), et presque 15 millions de bâtiments.

Pour ajouter le jeu de données Open Buildings dans QGIS, il suffit de l'importer au format CSV :

- Aller dans le menu `Couche` puis `Ajouter une couche` et `Ajouter une couche de texte délimité`

![Écran d'import d'une tuile de données Open Buildings en format CSV dans QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/open_buildings/import_open_buildings_csv_qgis.webp){: .img-center loading=lazy }

- Choisir l’emplacement du fichier CSV et le sélectionner
- Au niveau des géométries, sélectionner `WKT` (pour [Well-known text](https://fr.wikipedia.org/wiki/Well-known_text), un standard de représentation de géométries utile pour les échanges, en CSV notamment)
- Choisir le SCR `EPSG:4326`
- Cliquer sur `Ajouter` pour intégrer le jeu de données à QGIS

Tada :tada:, le CSV est importé !

[Et là, c'est le drame.](https://www.arteradio.com/son/61658634/et_la_c_est_le_drame)

![gif d'une personne qui a l'air pressée, en train de pointer sa montre du doigt](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/open_buildings/gif_waiting.gif){: .img-center loading=lazy }

## Convertir un CSV en geopackage, un format plus commode

Le nombre important de bâtiments, chargé via CSV en plus, peut rendre l'usage dans QGIS pas forcément fluide. Pour cela, on préférera utiliser un `gpkg`, qu'il est possible d'exporter depuis la couche CSV via un export classique.

Ou alors via un peu de magie [GDAL/OGR](https://gdal.org/en/stable/drivers/raster/gpkg.html), en créant d'abord un fichier `.vrt`, qu'on nomme `0fd_buildings.vrt` en écho au CSV initial appelé `0fd_buildings.csv` :

```xml title="Contenu du fichier 0fd_buildings.vrt"
<OGRVRTDataSource>
    <OGRVRTLayer name="0fd_buildings">
        <SrcDataSource>0fd_buildings.csv</SrcDataSource>
        <GeometryType>wkbPolygon</GeometryType>
        <LayerSRS>WGS84</LayerSRS>
        <GeometryField encoding="WKT" field="geometry"/>
    </OGRVRTLayer>
</OGRVRTDataSource>
```

Puis on convertit ce [VRT](https://gdal.org/en/stable/drivers/raster/vrt.html) en geopackage, grâce à la commande suivante :

```sh
ogr2ogr -f GPKG 0fd_buildings.gpkg 0fd_buildings.vrt -t_srs EPSG:4326 -nlt Polygon -nln footprints -progress
```

En sortie, on se retrouve avec le geopackage `0fd_buildings.gpkg`, ce qui est pratique pour une utilisation plus fluide dans QGIS.

Également pour un import éventuel en base PostGIS, qu'on peut effectuer là aussi avec `GDAL/OGR` :

```sh
ogr2ogr -f "PostgreSQL" \
    PG:"host=HOST port=PORT user=USER dbname=DBNAME password=PASSWORD" \
    -select geom -nln NOM_TABLE_PG \
    -s_srs epsg:4326 -t_srs PROJECTION_BD -progress \
    0fd_buildings.gpkg
```

## Conclusion

Nous avons vu comment télécharger puis convertir dans un format plus commode des données de bâtiments Open Buildings.

L’objectif est de fournir une méthode efficace pour obtenir des informations géospatiales précises sur les bâtiments, qui peuvent être utilisés pour diverses applications, telles que :

- La cartographie des populations, notamment pour les recensements et l’estimation de la densité
- L’évaluation des pertes et la planification des interventions lors de catastrophes naturelles
- Les secteurs de l’environnement, de la santé, du foncier, le développement économique...

Qu'on se le dise : les Open Buildings pallient un manque de services publics et de données disponibles dans les pays couverts par ce jeu de données, où le niveau de complétion des bâtiments OpenStreetMap n'est pas toujours haut. Tout le monde n'a pas la chance d'avoir [l'IGN](https://www.ign.fr/) et sa [BD TOPO](https://geoservices.ign.fr/bdtopo)...

Même si ça commence à bouger ces derniers temps, citons notamment [le projet SIGFU en Côte d'Ivoire](https://sigfu.gouv.ci/accueil) : 50% SIG 50% Kung-Fu, il s'agit du _Système Intégré de Gestion du Foncier Urbain_, initié par le _Ministère en charge de la Construction du Logement et de l’Urbanisme_. Ou [le service d'adressage et de parcelles numériques et uniques de la Poste au Ghana](https://www.ghanapostgps.com/map/).

Il peut également arriver parfois que la pertinence de certains bâtiments laisse à désirer. Bon, comme c'est une équipe de Google qui a généré le jeu de données, on pourrait s'attendre à ce qu'il soit synchro avec les tuiles satellites fournies par big G (qu'il est d'ailleurs possible de configurer dans QGIS, [en suivant ce tuto et l'ajout via tuiles XYZ](https://geossc.ma/ajouter-les-couches-de-google-sur-qgis-3-x/)). Or ces tuiles satellites sont rafraîchies plus souvent que le jeu de données OpenBuildings, comme il est possible de le voir, par exemple, ici à [Luanda](https://fr.wikipedia.org/wiki/Luanda):

![Delta temporel entre tuile Google sat et Open Buildings - Luanda](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/open_buildings/openbuilding_delta_temporel_sat_luanda.webp){: .img-center loading=lazy }

Et parfois, il y a des décalages entre imagerie satellitaire et bâtiments, comme par exemple ici à [Yaoundé](https://fr.wikipedia.org/wiki/Yaound%C3%A9) :

![Décalage de quelques mètres entre image satellite Google et bâtiment OpenBuildings - Yaoundé](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/open_buildings/openbuilding_yaounde_decalage_googlesat.png){: .img-center loading=lazy }

Toutefois, notons au travers de cette interview toute fraîche d'Abdoulaye Diack, le responsable du lab qui génère les Open Buildings, qu'en réalité ce sont les images de Sentinel-2 qui sont utilisées pour générer les emprises de bâtiments :

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/9VtoKJWZ5os?si=ohH3v4u14sEvjmcX" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

De toutes les manières, nous encourageons les organisations et les individus à utiliser ce jeu de données Open Buildings, pour des applications vertueuses et en faveur du développement et de la résilience des pays du Sud.

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
