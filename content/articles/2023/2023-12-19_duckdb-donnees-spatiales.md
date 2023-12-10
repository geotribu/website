---
title: "DuckDB et les données spatiales"
authors:
    - Florent FOUGÈRES
categories:
    - article
comments: true
date: "2023-12-19 14:20"
description: "Présentation de DuckDB et surtout de ses fonctions spatiales. Comment les exploiter et les mettres en liens avec des données parquet."
image:
license: default
robots: index, follow
tags:
    - database
    - duckdb
    - geoparquet
    - geos
    - parquet
    - spatial
---

# DuckDB et les données spatiales

:calendar: Date de publication initiale : 19 décembre 2023

## Introduction

![logo DuckDB](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/duckdb_spatial/DuckDB_Logo.png){: .img-thumbnail-left }

Si depuis quelques semaines, vous voyez passer beaucoup de choses sur des sujets comme DuckDB, les fichiers parquet ou encore les données d’Ouverture Maps, mais sans trop comprendre de quoi il s’agit, vous êtes au bon endroit !

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## DuckDB c’est quoi ?

[DuckDB](https://duckdb.org/) est un SGBD (système de gestion de base de données) relationnel principalement écrit en C++ et [open source](https://github.com/duckdb/duckdb) publiée sous licence MIT. Le projet est assez récent, il a débuté en 2018, mais le projet vit beaucoup et les releases sont fréquentes, notamment grâce à une communauté très active (12 800 étoiles sur Github). Actuellement le projet est en version 0.9.1.

La particularité de ce système de base de données est qu'à l’instar des bases SQLite ou GeoPackage, les bases de données sont des fichiers portables. Ce qui permet un échange simplifié. Cependant, un des inconvénients à ce jour est le non-support de la rétrocompatibilité des bases entre les versions de DuckDB. Exemple, si quelqu’un me donne une base construite avec DuckDB 0.8.0 et que je dispose des outils de la dernière version, à savoir 0.9.1, je ne pourrais pas lire et utiliser cette base de données.

## Les performances

Au niveau des performances, DuckDB est particulièrement adapté pour traiter avec une grande efficacité les gros volumes de données. La ou DuckDB se démarque, c’est que contrairement au système de base de données connu comme PostgreSQL ou MySQL qui ont un système de traitement par ligne, DuckDB utilise un système d’architecture en colonne et donc selon [le site officiel de DuckDB](https://duckdb.org/why_duckdb.html#duckdbisfast) :

> “Un grand lot de valeurs est traité en une seule opération”

Concrètement, cela permet donc de traiter uniquement les colonnes utiles à la requête et donc d’accélérer le temps de réponse.

## Comment l’utiliser

Tout d’abord le support est mufti plateforme, ce que je vais dire est valable pour Windows, Linux et MacOS. DuckDB est utilisable de plusieurs façons et [les installations sont bien documentées](https://duckdb.org/docs/installation/). Il y a tout d’abord un CLI si vous êtes un adepte du terminal. Mais également de nombreux langages parmi lesquelles Python, C++, R, Node.js ou encore Rust. Si vous n’êtes pas très familier avec ces environnements et que vous êtes plus à l’aise avec les gestionnaires de base de données avec interface graphique, [DBeaver](https://dbeaver.io/) propose le [support](https://duckdb.org/docs/guides/sql_editors/dbeaver.html) des bases de données DuckDB.

Bien sûr, au-delà de la manière donc vous utilisez DuckDB, le langage pour utiliser DuckDB est le SQL. Dans la suite dans cet article, lors des exemples pratiques, je détaillerais les commandes en utilisant le CLI ou bien le paquet Python.

## Les fonctions spatiales

Les fonctions spatiales de DuckDB sont une [extension](https://duckdb.org/docs/extensions/spatial.html). La plupart des fonctions spatiales sont issus de la librairie [GEOS](https://libgeos.org/). Seulement certaines sont implémentées nativement dans le cœur de DuckDB. Si vous êtes un habitué des fonctions spatiales de PostGIS vous ne serez pas dépaysé en utilisant les fonctions spatiales du canard, la syntaxe et le nom des fonctions est extrêmement proche.

Une bonne soixantaine de fonctions spatiales sont disponibles parmi par exemple la star de la jointure spatiale `ST_Intersects(GEOMETRY, GEOMETRY)`

Ces fonctions spatiales ne sont donc pas nativement présente. Il faut donc la première fois faire un `INSTALL spatial` pour installer cette extension. Pour faire une analogie assez connue du monde de la géomatique (ou des sigistes à votre guise) c’est un peu l’équivalent d’un `CREATE EXTENSION postgis`dans PostgreSQL pour obtenir l’extension spatial PostGIS.

Puis lors de chaque utilisation sur une base de données, il faut charger cette extension via un `LOAD spatial`

## Les formats de données spatiales pris en charge

Au niveau des formats, là aussi, il y a du choix. Une cinquantaine de formats sont supportés pour lire ou importer des données spatiales. On trouve par exemples les classiques Shapefile, GeoJSON, GPX ou encore KML. Mais aussi des formats de base de données spatiales comme Spatialite ou GeoPackage. Pour finir sur les formats, si vous êtes un OSM addict, le support est encore en mode expérimental, mais DuckDB est capable de lire et intégré des fichiers [PBF](https://wiki.openstreetmap.org/wiki/PBF_Format) (`.osm.pbf`) via une fonction nommée `ST_ReadOSM()`.

## Les colonnes de géométries

Une des particularités de colonne de géométrie sur DuckDB spatial, est qu’une colonne n’a pas de type de géométrie défini (comme sur PostGIS par exemple). Une même colonne de géométrie peut contenir aussi bien des points, des lignes, des polygones etc..

Il y a quand même un hic à tout ça, à l’heure où j’écris ces lignes (peut-être que cela sera prochainement implémenté), une colonne de géométrie ne porte pas de système de projection. Il n’y a donc pas de fonction de reprojection. Et lors de l’export d’une couche géographique, cette couche ne portera pas de projection. Lors d’une lecture dans un SIG, QGIS par exemple, il faudra définir manuellement la projection de votre couche.

## Les fichiers parquet, c'est quoi ?

[Parquet](https://parquet.apache.org/) est un format de fichier open source poussé par la fondation Apache créé en juillet 2013. Et qui a la particularité de pouvoir stocker avec une grande efficacité des données en utilisant une architecture en colonne (tiens tiens cette histoire de colonne, ça ne vous dit pas quelque chose ?). Il est notamment utilisé pour des données “big data” … Les “parquet file” comme ils sont souvent nommés sur la toile ne sont que des fichiers utilisés pour s’échanger des données, ce n’est pas sûr lequel on va travailler.

De nombreux outils existent pour traiter et requêter ce type de fichier, parmi un est particulièrement performant, et devinez quoi, il s’agit de DuckDB (quelle surprise hein ?)

## Pour aller plus loin

Sur ce [répertoire Github](https://github.com/davidgasquez/awesome-duckdb) est maintenu une liste de projets, outils, ou ressource développée autour de DuckDB. Petit coup de ❤️ pour [Harlequin](https://harlequin.sh/), qui est un IDE pour terminal destiné à l’utilisation de DuckDB et simple d'installation.

![screenshort harlequin](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/duckdb_spatial/harlequin.png){: .img-center }

## Exemple pratique

### Pré requis

- L’exécutable DuckDB pour utiliser le CLI

<!-- markdownlint-disable MD040 -->
<!-- termynal -->

```sh
v0.9.2 3c695d7ba9
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D
```

<!-- markdownlint-enable MD040 -->
ou

- Un environnement Python avec le [paquet duckdb](https://pypi.org/project/duckdb/) d’installer (DuckDB utilise de nombreuses dépendances, il est donc conseiller d’utiliser un environnement virtuel pour éviter les conflits de dépendances)

<!-- markdownlint-disable MD040 -->
<!-- termynal -->

```sh
$ pip install duckdb
---> 100%
Installing collected packages: duckdb
Successfully installed duckdb-0.9.2
```

<!-- markdownlint-enable MD040 -->

### Création d’une de données (ou l’ouvrir si elle existe déjà)

<!-- markdownlint-disable MD046 -->

=== ":snake: Python”

```python
import duckdb

con = duckdb.connect("./ouverture_maps-transportation.db")
```

=== "▶️ CLI”

```bash
D .open ouverture_maps-transportation.db
```

### Installer puis charger l’extension spatiale

=== ":snake: Python”

```python
con.sql("INSTALL spatial; LOAD spatial ; LOAD httpfs ;")
```

=== "▶️ CLI”

```bash
D INSTALL spatial ;
D LOAD spatial ;
D LOAD httpfs ;
```

### Importer un CSV et créer la géométrie

La fonction `read_csv_auto` nous permet de pouvoir importer un CSV sans avoir à créer la table au préalable, cette fonction détecte automatiquement la structure du CSV.

=== ":snake: Python”

```python
con.sql("CREATE TABLE airports AS FROM read_csv_auto('[https://davidmegginson.github.io/ourairports-data/airports.csv](https://davidmegginson.github.io/ourairports-data/airports.csv)', HEADER=True, DELIM=',') ;")
con.sql("ALTER TABLE airports ADD COLUMN the_geom GEOMETRY ;")
con.sql("UPDATE airports SET the_geom = ST_POINT(longitude_deg, latitude_deg) ;")
```

=== "▶ CLI”

```bash
D CREATE TABLE airports AS FROM read_csv_auto('[https://davidmegginson.github.io/ourairports-data/airports.csv](https://davidmegginson.github.io/ourairports-data/airports.csv)', HEADER=True, DELIM=',') ;
D ALTER TABLE airports ADD COLUMN the_geom GEOMETRY ;
D UPDATE airports SET the_geom = ST_POINT(longitude_deg, latitude_deg) ;
```

### Traiter des données parquet d'Ouverture Maps avec DuckDB

Les données d’Ouverture Maps sont fournies sous forme de fichier parquet ([décrites ici](https://github.com/OvertureMaps/data#data-release-feedback)), nous allons donc importer ces données dans une base pour les consulter.

#### Importer les données dans la base

Dans cet exemple on récupère 100 bâtiments aléatoirement (environ 1 minute de traitement chez moi)

=== ":snake: Python”

```python
query_buildings = ("CREATE TABLE buildings AS ( "  
"SELECT type, version, CAST(updatetime as varchar) as updateTime, "
"height, numfloors as numFloors, level, class, "
"ST_GeomFromWKB(geometry) as geometry "
"FROM read_parquet('s3://overturemaps-us-west-2/release/2023-11-14-alpha.0/theme=buildings/type=*/*', hive_partitioning=1) "
"LIMIT 1 ); ")

con.sql(query_admins)
```

=== "▶️ CLI”

```bash
D. CREATE TABLE buildings AS (  
 SELECT type, version, CAST(updatetime as varchar) as updateTime,
 height, numfloors as numFloors, level, class,
 ST_GeomFromWKB(geometry) as geometry
 FROM read_parquet('s3://overturemaps-us-west-2/release/2023-11-14-alpha.0/theme=buildings/type=*/*', hive_partitioning=1)
 LIMIT 1 );
```

Dans cet autre exemple, on récupère les bâtiments d’une partie de Manhattan en indiquant les coordonnées d’un rectangle (attention requête assez longue)

=== ":snake: Python”

```python
query_buildings = ("CREATE TABLE buildings AS ( "  
"SELECT type, version, CAST(updatetime as varchar) as updateTime, "
"height, numfloors as numFloors, level, class, "
"ST_GeomFromWKB(geometry) as geometry "
"FROM read_parquet('s3://overturemaps-us-west-2/release/2023-11-14-alpha.0/theme=buildings/type=*/*', hive_partitioning=1) "
"WHERE bbox.minx > -73.9967900 "
"AND bbox.maxx < -73.9967900 "
"AND bbox.miny > 40.7373325 "
"AND bbox.maxy < 40.7373325 ); ")

con.sql(query_admins)
```

=== "▶️ CLI”

```bash
D. CREATE TABLE buildings AS (  
 SELECT type, version, CAST(updatetime as varchar) as updateTime,
 height, numfloors as numFloors, level, class,
 ST_GeomFromWKB(geometry) as geometry
 FROM read_parquet('s3://overturemaps-us-west-2/release/2023-11-14-alpha.0/theme=buildings/type=*/*', hive_partitioning=1)
 WHERE bbox.minx > -73.9967900
 AND bbox.maxx < -73.9967900
 AND bbox.miny > 40.7373325
 AND bbox.maxy < 40.7373325 );
```

#### Visualiser les données dans QGIS

Pour cela, installer le plugin QGIS [QDuckDB](https://oslandia.gitlab.io/qgis/qduckdb/).
:warning: Attention, cette extension est encore expérimentale, il faut donc bien cocher ce paramètre dans le gestionnaire des extensions de QGIS.

![qduckdb](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/duckdb_spatial/qduckdb.png)

#### Convertir les données en un GeoJSON en utilisant DuckDB

Un des atouts de DuckDB n'est pas seulement d’intégrer des données pour les traiter dans la base. Mais cela peut servir d’outils de conversion pour des données parquets. Exemple, on me donne des données en parquet, mais je souhaite les avoirs en GeoJSON, on peut les convertir sans créer de table ni de base.

=== ":snake: Python”

```python
query_export_buildings = ("COPY ( "  
"SELECT type, version, CAST(updatetime as varchar) as updateTime, "
"height, numfloors as numFloors, level, class, "
"ST_GeomFromWKB(geometry) as geometry "
"FROM read_parquet('s3://overturemaps-us-west-2/release/2023-11-14-alpha.0/theme=buildings/type=*/*', hive_partitioning=1) "
"WHERE bbox.minx > -73.9967900 "
"AND bbox.maxx < -73.9967900 "
"AND bbox.miny > 40.7373325 "
"AND bbox.maxy < 40.7373325 )  "
"TO 'new_york_buildings.geojson' "
" WITH (FORMAT GDAL, DRIVER 'GeoJSON', SRS 'EPSG:4326'); ")

con.sql(query_export_buildings)
```

=== "▶️ CLI”

```bash
D. COPY (
 SELECT type, version, CAST(updatetime as varchar) as updateTime,
 height, numfloors as numFloors, level, class,
 ST_GeomFromWKB(geometry) as geometry
 FROM read_parquet('s3://overturemaps-us-west-2/release/2023-11-14-alpha.0/theme=buildings/type=*/*', hive_partitioning=1)
 WHERE bbox.minx > -73.9967900
 AND bbox.maxx < -73.9967900
 AND bbox.miny > 40.7373325
 AND bbox.maxy < 40.7373325 )  
 TO 'new_york_buildings.geojson'
 WITH (FORMAT GDAL, DRIVER 'GeoJSON', SRS 'EPSG:4326');
```

:bulb: Également possible d'exporter en Shapefile, pour cela, il faut remplacer les deux dernières lignes par celles-ci :

```sql
 ) TO 'new_york_buildings.shp'
WITH (FORMAT GDAL, DRIVER 'ESRI Shapefile');
```

----

## Auteur {: data-search-exclude }

--8<-- "content/team/ffou.md"

{% include "licenses/default.md" %}
