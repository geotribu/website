---
title: DuckDB et les données spatiales
authors:
    - Florent FOUGÈRES
categories:
    - article
comments: true
date: "2023-12-19 14:20"
description: Présentation de DuckDB et surtout de ses fonctions spatiales. Comment les exploiter et les mettre en lien avec des données (géo)parquet.
icon: simple/duckdb
image:
license: default
robots: index, follow
tags:
    - base de données
    - DuckDB
    - geoparquet
    - geos
    - parquet
---

# DuckDB et les données spatiales

:calendar: Date de publication initiale : 19 décembre 2023

## Introduction

![logo DuckDB](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/duckdb.png){: .img-thumbnail-left }

Si depuis quelques semaines, vous voyez passer beaucoup de choses sur des sujets comme DuckDB, les fichiers parquet ou encore les données d’Overture Maps, mais sans trop comprendre de quoi il s’agit, vous êtes au bon endroit !

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## DuckDB c’est quoi ?

[DuckDB](https://duckdb.org/) est un SGBD (système de gestion de base de données) relationnel principalement écrit en C++ et [open source](https://github.com/duckdb/duckdb) publié sous[ licence MIT](https://fr.wikipedia.org/wiki/Licence_MIT). Le projet a débuté en 2018 et vit beaucoup. Il fait l'objet de releases fréquentes (13 300 étoiles sur GitHub le 09/12/23) et en est à la version 0.9.2.

Ce SGBD a la particularité d'être sous forme de fichier portable (comme les bases GeoPackage, File GeoDatabase d'ESRI ou encore Access MDB) ce qui simplifie les échanges. Cette portabilité présente cependant un défaut : la non rétrocompatibilité entre les différentes versions de DuckDB : un fichiers produit avec une version de DuckDB ne peut actuellement pas être lu avec une autre version de DuckDB.

## Les performances

Au niveau des performances, DuckDB est particulièrement adapté au traitement des gros volumes de données. Son architecture diffère d'ailleurs sensiblement de SGBDs comme PostgreSQL ou MySQL qui attaquent majoritairement les données par ligne, car DuckDB traite les données en colonnes. La finalité permise : un grand lot de valeurs est traité en une seule opération rapporte le [le site officiel de DuckDB](https://duckdb.org/why_duckdb.html#duckdbisfast) : on traite seulement les colonnes utiles à la requête et cela optimise et accélère le temps de réponse.



## Comment l’utiliser

Le support est multi-plateforme (Windows, Linux et MacOS) et DuckDB est utilisable de plusieurs façons via [des installations bien documentées](https://duckdb.org/docs/installation/). Il y a un CLI si vous êtes un adepte du terminal, et de nombreux langages peuvent l'utiliser (parmi lesquels Python, C++, R, Node.js ou encore Rust). Si vous êtes plus à l’aise avec les gestionnaires de base de données avec interface graphique, [DBeaver](https://dbeaver.io/) propose lui aussi le [support](https://duckdb.org/docs/guides/sql_editors/dbeaver.html) des bases de données DuckDB.

Enfin, indépendamment du client de votre choix, DuckDB fonctionne en SQL. Dans la suite de cet article, mes exemples reposeront sur des commandes en utilisant le CLI ou le paquet Python.

## Les fonctions spatiales

Les fonctions spatiales de DuckDB sont rassemblées dans une [extension](https://duckdb.org/docs/extensions/spatial.html), et sont pour la plupart issues de la librairie [GEOS](https://libgeos.org/). Néanmoins, toutes ne sont pas implémentées nativement dans le cœur de DuckDB. Si vous êtes un habitué des fonctions spatiales de PostGIS vous ne serez pas dépaysé en utilisant les fonctions spatiales du canard, la syntaxe et le nom des fonctions est extrêmement proche.

On retrouve ainsi une bonne soixantaine de fonctions dont la star de la jointure spatiale ST_Intersects(GEOMETRY, GEOMETRY)

Ces fonctions ne sont donc pas natives mais s'implémentent avec un simple INSTALL spatial, qui équivaut (coucou les géomaticien.ne.s) à un CREATE EXTENSION postgis pour obtenir l’extension spatial PostGIS dans PostgreSQL. À chaque utilisation, cette extension s'appelle par la commande LOAD spatial.


## Les formats de données spatiales pris en charge

Au niveau des formats de données spatiales, beaucoup de choix également. Une cinquantaine sont supportés en lecture ou import dont les classiques Shapefile, GeoJSON, GPX ou encore KML, ainsi quedes formats de base de données spatiales comme Spatialite ou GeoPackage. Enfin, pour les OSM addicts, en mode expérimental, DuckDB est capable de lire et intégrer des fichiers [PBF](https://wiki.openstreetmap.org/wiki/PBF_Format) (.osm.pbf) via une fonction nommée ST_ReadOSM().

## Les colonnes de géométries et la non prise en charge des projections

Une des particularités des colonnes de géométrie sur DuckDB spatial est l'absence de définition du type de géométrie (contrairement à PostGIS par exemple). Une même colonne de géométrie contiendra aussi bien des points, des lignes, des polygones, etc.

Il y a quand même un hic dans tout ça : les projections ne sont pas gérables dans la version actuelle de DuckDB, donc : 
- pas de définition de projection comme contrainte pour une colonne 
- pas de fonction de reprojection 
- pas d'attribution d'une projection lors d'un export

Il faut définir manuellement (et avec rigueur) vos projections en dehors de DuckDB car il ne les différencie pas. Si cette réflexion tombe sous le sens du point de vue "administrateur de données", les utilisateurs moins avertis peuvent avoir quelques surprises en mélangeant des projections.

## Les fichiers parquet, c'est quoi ?

[Parquet](https://parquet.apache.org/) est un format de fichier open source poussé par la fondation Apache, créé en juillet 2013, qui a la particularité de pouvoir stocker avec une grande efficacité des données. Il utilise… une architecture en colonne. Tiens, tiens, cette histoire de colonne, ça ne vous dit pas quelque chose ? Il est notamment utilisé pour des données « big data »… Les « parquet files », comme ils sont souvent nommés sur la toile, sont uniquement des fichiers utilisés pour s’échanger des données et non pour travailler dessus.


## Pour aller plus loin

Sur ce [répertoire Github](https://github.com/davidgasquez/awesome-duckdb) est maintenue une liste de projets, outils, ou ressource développée autour de DuckDB. Petit coup de :heart: pour [Harlequin](https://harlequin.sh/), qui est un IDE pour terminal destiné à l’utilisation de DuckDB et simple d'installation.

![Screenshot Harlequin DuckDB](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/duckdb_spatial/harlequin.png){: .img-center loading=lazy }

----

## Exemple pratique

### Pré requis

- L’exécutable DuckDB pour utiliser la CLI :

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

- Un environnement Python intégrant le [paquet duckdb](https://pypi.org/project/duckdb/). DuckDB utilisant de nombreuses dépendances, il est fortement conseillé d’utiliser un environnement virtuel pour éviter les conflits de dépendances.

<!-- markdownlint-disable MD040 -->
<!-- termynal -->

```sh
$ pip install duckdb
---> 100%
Installing collected packages: duckdb
Successfully installed duckdb-0.9.2
```

<!-- markdownlint-enable MD040 -->

### Création d’une base de données, ou l’ouvrir si elle existe déjà

<!-- markdownlint-disable MD046 -->

=== ":snake: Python"

    ```python
    import duckdb

    con = duckdb.connect("./overture_maps-transportation.db")
    ```

=== ":material-console: CLI"

    ```sh
    D .open overture_maps-transportation.db
    ```

### Installer puis charger l’extension spatiale

=== ":snake: Python"

    ```python
    con.sql("INSTALL spatial; LOAD spatial ; LOAD httpfs ;")
    ```

=== ":material-console: CLI"

    ```sh
    D INSTALL spatial ;
    D LOAD spatial ;
    D LOAD httpfs ;
    ```

### Importer un CSV et créer la géométrie

La fonction `read_csv_auto` nous permet de pouvoir importer un CSV sans avoir à créer la table au préalable. Cette fonction détecte automatiquement la structure du CSV.

=== ":snake: Python"

    ```python
    con.sql("CREATE TABLE airports AS FROM read_csv_auto('[https://davidmegginson.github.io/ourairports-data/airports.csv](https://davidmegginson.github.io/ourairports-data/airports.csv)', HEADER=True, DELIM=',') ;")
    con.sql("ALTER TABLE airports ADD COLUMN the_geom GEOMETRY ;")
    con.sql("UPDATE airports SET the_geom = ST_POINT(longitude_deg, latitude_deg) ;")
    ```

=== ":material-console: CLI"

    ```sh
    D CREATE TABLE airports AS FROM read_csv_auto('[https://davidmegginson.github.io/ourairports-data/airports.csv](https://davidmegginson.github.io/ourairports-data/airports.csv)', HEADER=True, DELIM=',') ;
    D ALTER TABLE airports ADD COLUMN the_geom GEOMETRY ;
    D UPDATE airports SET the_geom = ST_POINT(longitude_deg, latitude_deg) ;
    ```

### Traiter des données parquet d'Overture Maps avec DuckDB

Les données d’Overture Maps sont fournies sous forme de fichier parquet ([décrites ici](https://github.com/OvertureMaps/data#data-release-feedback)), nous allons donc importer ces données dans une base pour les consulter.

#### Importer les données dans la base

Dans cet exemple, on récupère 100 bâtiments aléatoirement ; environ une minute de traitement chez moi.

=== ":snake: Python"

    ```python
    query_buildings = ("CREATE TABLE buildings AS ( "  
    "SELECT type, version, CAST(updatetime as varchar) as updateTime, "
    "height, numfloors as numFloors, level, class, "
    "ST_GeomFromWKB(geometry) as geometry "
    "FROM read_parquet('s3://overturemaps-us-west-2/release/2023-11-14-alpha.0/theme=buildings/type=*/*', hive_partitioning=1) "
    "LIMIT 1 ); ")

    con.sql(query_admins)
    ```

=== ":material-console: CLI"

    ```sh
    D. CREATE TABLE buildings AS (  
        SELECT type, version, CAST(updatetime as varchar) as updateTime,
        height, numfloors as numFloors, level, class,
        ST_GeomFromWKB(geometry) as geometry
        FROM read_parquet('s3://overturemaps-us-west-2/release/2023-11-14-alpha.0/theme=buildings/type=*/*', hive_partitioning=1)
        LIMIT 1
    );
    ```

Dans cet autre exemple, on récupère les bâtiments d’une partie de Manhattan en indiquant les coordonnées d’un rectangle (attention requête assez longue)

=== ":snake: Python"

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

=== ":material-console: CLI"

    ```sh
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

![qduckdb](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/duckdb_spatial/qduckdb.png){: .img-center loading=lazy }

#### Convertir les données en un GeoJSON en utilisant DuckDB

Un des atouts de DuckDB est qu'en plus d’intégrer des données pour les traiter en base, il peut servir d’outil de conversion pour des données parquets. Exemple : Si on me donne des données en parquet et je souhaite des GeoJSON, DuckDB peut les convertir sans créer de table ni de base !

=== ":snake: Python"

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

=== ":material-console: CLI"

    ```sh
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
