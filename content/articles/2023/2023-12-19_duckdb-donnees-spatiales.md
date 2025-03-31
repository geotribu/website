---
title: DuckDB et les données spatiales
subtitle: Spatial laqué
authors:
    - Florent FOUGÈRES
categories:
    - article
comments: true
date: 2023-12-19
description: Présentation de DuckDB et surtout de ses fonctions spatiales. Comment les exploiter et les mettre en lien avec des données (géo)parquet.
icon: simple/duckdb
image:
license: default
robots: index, follow
tags:
    - base de données
    - DuckDB
    - GeoParquet
    - GEOS
    - Parquet
---

# DuckDB et les données spatiales

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

![logo DuckDB](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/duckdb.png){: .img-thumbnail-left }

Si depuis quelques semaines, vous voyez passer beaucoup de choses sur des sujets comme DuckDB, les fichiers Parquet ou encore les données d’Overture Maps, mais sans trop comprendre de quoi il s’agit, vous êtes au bon endroit !

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## DuckDB c’est quoi ?

[DuckDB](https://duckdb.org/) est un SGBD (système de gestion de base de données) relationnel principalement écrit en C++ et [open source](https://github.com/duckdb/duckdb) publié sous [licence MIT](https://fr.wikipedia.org/wiki/Licence_MIT). Le projet a débuté en 2018 et vit beaucoup. Il fait l'objet de releases fréquentes (13 300 étoiles sur GitHub le 09/12/23) et en est à la version 0.9.2.

Ce SGBD a la particularité d'être sous forme de fichier portable (comme les bases GeoPackage, File GeoDatabase d'ESRI ou encore Access MDB) ce qui simplifie les échanges. Cette portabilité présente cependant un défaut : la non rétrocompatibilité entre les différentes versions de DuckDB. Un fichiers produit avec une version de DuckDB ne peut actuellement pas être lu avec une autre version de DuckDB.

## Les performances

Au niveau des performances, DuckDB est particulièrement adapté au traitement des gros volumes de données. Son architecture diffère d'ailleurs sensiblement de SGBDs comme PostgreSQL ou MySQL qui attaquent majoritairement les données par ligne, car DuckDB traite les données en colonnes. La finalité permise : un grand lot de valeurs est traité en une seule opération rapporte le [le site officiel de DuckDB](https://duckdb.org/why_duckdb.html#duckdbisfast) : on traite seulement les colonnes utiles à la requête et cela optimise et accélère le temps de réponse. Alors qu'avec une architecture plus traditionnelle, on va venir traiter l'intégralité des données de chaque ligne pour éxécuter la requête.

## Comment l’utiliser

Le support est multi-plateforme (Windows, Linux et MacOS) et DuckDB est utilisable de plusieurs façons via [des installations bien documentées](https://duckdb.org/docs/installation/). Il y a un CLI si vous êtes un adepte du terminal et de nombreux langages peuvent l'utiliser (parmi lesquels Python, C++, R, Node.js ou encore Rust). Si vous êtes plus à l’aise avec les gestionnaires de base de données avec interface graphique, [DBeaver](https://dbeaver.io/) ou [DataGrip](https://www.jetbrains.com/fr-fr/datagrip/) proposent eux aussi le [support](https://duckdb.org/docs/guides/sql_editors/dbeaver.html) des bases de données DuckDB.

Enfin, indépendamment du client de votre choix, DuckDB fonctionne en SQL. Dans la suite de cet article, mes exemples reposeront sur des commandes en utilisant le CLI ou le paquet Python.

## Les fonctions spatiales

Les fonctions spatiales de DuckDB sont rassemblées dans une [extension](https://duckdb.org/docs/extensions/spatial.html) et sont pour la plupart issues de la librairie [GEOS](https://libgeos.org/). Néanmoins, toutes ne sont pas implémentées nativement dans le cœur de DuckDB. Si vous êtes un habitué des fonctions spatiales de PostGIS vous ne serez pas dépaysé en utilisant les fonctions spatiales du canard : la syntaxe et le nom des fonctions sont extrêmement proches.

On retrouve ainsi une bonne soixantaine de fonctions dont la star de la jointure spatiale `ST_Intersects(GEOMETRY, GEOMETRY)`.

Ces fonctions ne sont donc pas natives mais s'implémentent avec un simple `INSTALL spatial`, qui équivaut (coucou les géomaticien.ne.s) à un `CREATE EXTENSION postgis` pour obtenir l’extension spatiale PostGIS dans PostgreSQL. À chaque utilisation, cette extension s'appelle par la commande `LOAD spatial`.

## Les formats de données spatiales pris en charge

Au niveau des formats de données spatiales, beaucoup de choix également. Une cinquantaine sont supportés en lecture ou import dont les classiques Shapefile, GeoJSON, GPX ou encore KML, ainsi que des formats de base de données spatiales comme Spatialite ou GeoPackage. Enfin, pour les OSM addicts, en mode expérimental, DuckDB est capable de lire et intégrer des fichiers [PBF](https://wiki.openstreetmap.org/wiki/PBF_Format) (.osm.pbf) via une fonction nommée `ST_ReadOSM()`.

## Les colonnes de géométries et la non prise en charge des projections

Une des particularités des colonnes de géométrie sur DuckDB spatial est l'absence de définition du type de géométrie (contrairement à PostGIS par exemple). Une même colonne de géométrie contiendra aussi bien des points, des lignes, des polygones, etc.

Il y a quand même un hic dans tout ça : une colonne de géométrie n'a pas de système de projection dans sa définition ! Conséquences, il n'y a :

- pas de définition de projection comme contrainte pour une colonne
- pas d'attribution d'une projection lors d'un export

Il est bien possible de projeter une géométrie (fonction `ST_Transform`) mais cela nécessite de connaître l'EPSG de la géométrie source, celle-ci ne sera pas détectée automatiquement et l'information n'est pas portée dans la définition de la colonne.

Il faut définir manuellement (et avec rigueur) vos projections en dehors de DuckDB car il ne les différencie pas. Si cette réflexion tombe sous le sens du point de vue "administrateur de données", les utilisateurs moins avertis peuvent avoir quelques surprises en mélangeant des projections.

## Les fichiers Parquet, c'est quoi ?

![logo Parquet](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/parquet.png){: .img-thumbnail-left }

[Parquet](https://parquet.apache.org/) est un format de fichier open source poussé par la fondation Apache depuis 2013, qui a la particularité de stocker des données avec efficacité... via une architecture en colonne 😉. Il est notamment utilisé pour le big data. À la base, ces « parquet files » étaient utilisés pour l'échange de données et non pour travailler dessus mais les schémas de compression et de codage de données qu'ils mobilisent les rendent très performants pour la gestion massive de données complexes.

## Pour aller plus loin

Sur ce [répertoire Github](https://github.com/davidgasquez/awesome-duckdb) est maintenue une liste de projets, outils, ou ressources développés autour de DuckDB. Petit coup de :heart: pour [Harlequin](https://harlequin.sh/), qui est un IDE pour terminal destiné à l’utilisation de DuckDB et simple d'installation.

![Screenshot Harlequin DuckDB](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/duckdb_spatial/harlequin.png){: .img-center loading=lazy }

## Ailleurs sur DuckDB et le spatial

La série d'articles de Éric Mauvière sur le même sujet : [Interroger des fichiers distants](https://www.icem7.fr/outils/3-explorations-bluffantes-avec-duckdb-1-interroger-des-fichiers-distants/) et  [Butiner des API JSON](https://www.icem7.fr/pedagogie/3-explorations-bluffantes-avec-duckdb-butiner-des-api-json-2-3/).

Mark Litwintschik utilise DuckDB et ses fonctions spatiales dans ces articles, on peut en trouver un sur l'exploration du [suivi des vols à l'échelle mondiale](https://tech.marksblogg.com/global-flight-tracking-adsb.html) ou encore les données de [Natural Earth](https://tech.marksblogg.com/natural-earth-free-gis-data.html).

Enfin un [article](https://dev.to/savo/spatial-data-analysis-with-duckdb-40j9) sur le même thème que l'exemple pratique qui va suivre, l'exploration des données de Overture Maps Foundation avec DuckDB.

----

## Exemple pratique

### Pré requis

Pour suivre la suite de ce tutoriel, il vous faut donc avoir installé DucKDB. Deux possibilités :

- :snake: Soit un environnement Python intégrant le [paquet duckdb](https://pypi.org/project/duckdb/). DuckDB utilisant de nombreuses dépendances, il est fortement conseillé d’utiliser un environnement virtuel pour éviter les conflits de dépendances.

<!-- markdownlint-disable MD040 -->
<!-- termynal -->

```sh
$ pip install duckdb
---> 100%
Installing collected packages: duckdb
Successfully installed duckdb-0.10.1
```

<!-- markdownlint-enable MD040 -->

ou

- :material-console: Soit l’exécutable DuckDB pour utiliser l'interface en ligne de commande (CLI) dont l'invite change pour un `D` (que nous ignorerons dans les blocs de code suivants) :

<!-- markdownlint-disable MD040 -->
<!-- termynal -->

```sh
v0.10.1 3c695d7ba9
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
D
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
    .open overture_maps-transportation.db
    ```

### Installer puis charger l’extension spatiale

=== ":snake: Python"

    ```python
    con.sql("INSTALL spatial; LOAD spatial; INSTALL httpfs; LOAD httpfs;")
    ```

=== ":material-console: CLI"

    ```sh
    INSTALL spatial ;
    LOAD spatial ;
    INSTALL httpfs ;
    LOAD httpfs ;
    ```

### Importer un CSV et créer la géométrie

La fonction `read_csv_auto` nous permet de pouvoir importer un CSV sans avoir à créer la table au préalable. Cette fonction détecte automatiquement la structure du CSV.

=== ":snake: Python"

    ```python
    con.sql("CREATE TABLE airports AS FROM read_csv_auto('https://davidmegginson.github.io/ourairports-data/airports.csv', HEADER=True, DELIM=',') ;")
    con.sql("ALTER TABLE airports ADD COLUMN the_geom GEOMETRY ;")
    con.sql("UPDATE airports SET the_geom = ST_POINT(longitude_deg, latitude_deg) ;")
    ```

    Avec `DESCRIBE` il est facile d'afficher la structure de la table :

    ```python
    print(con.sql("DESCRIBE airports;"))
    ┌───────────────────┬─────────────┬─────────┬─────────┬─────────┬─────────┐
    │    column_name    │ column_type │  null   │   key   │ default │  extra  │
    │      varchar      │   varchar   │ varchar │ varchar │ varchar │ varchar │
    ├───────────────────┼─────────────┼─────────┼─────────┼─────────┼─────────┤
    │ id                │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
    │ ident             │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ type              │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ name              │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ latitude_deg      │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
    │ longitude_deg     │ DOUBLE      │ YES     │ NULL    │ NULL    │ NULL    │
    │ elevation_ft      │ BIGINT      │ YES     │ NULL    │ NULL    │ NULL    │
    │ continent         │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ iso_country       │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ iso_region        │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ municipality      │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ scheduled_service │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ gps_code          │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ iata_code         │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ local_code        │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ home_link         │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ wikipedia_link    │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ keywords          │ VARCHAR     │ YES     │ NULL    │ NULL    │ NULL    │
    │ the_geom          │ GEOMETRY    │ YES     │ NULL    │ NULL    │ NULL    │
    ├───────────────────┴─────────────┴─────────┴─────────┴─────────┴─────────┤
    │ 19 rows                                                       6 columns │
    └─────────────────────────────────────────────────────────────────────────┘

    # et on n'oublie pas de fermer proprement la connexion
    con.close()
    ```

=== ":material-console: CLI"

    ```sh
    CREATE TABLE airports AS FROM read_csv_auto('https://davidmegginson.github.io/ourairports-data/airports.csv', HEADER=True, DELIM=',') ;
    ALTER TABLE airports ADD COLUMN the_geom GEOMETRY ;
    UPDATE airports SET the_geom = ST_POINT(longitude_deg, latitude_deg) ;
    ```

    Avec `DESCRIBE` il est facile d'afficher la structure de la table :

    ```sh
    DESCRIBE airports;
    ┌───────────────────┬─────────────┬─────────┬─────────┬─────────┬─────────┐
    │    column_name    │ column_type │  null   │   key   │ default │  extra  │
    │      varchar      │   varchar   │ varchar │ varchar │ varchar │ varchar │
    ├───────────────────┼─────────────┼─────────┼─────────┼─────────┼─────────┤
    │ id                │ BIGINT      │ YES     │         │         │         │
    │ ident             │ VARCHAR     │ YES     │         │         │         │
    │ type              │ VARCHAR     │ YES     │         │         │         │
    │ name              │ VARCHAR     │ YES     │         │         │         │
    │ latitude_deg      │ DOUBLE      │ YES     │         │         │         │
    │ longitude_deg     │ DOUBLE      │ YES     │         │         │         │
    │ elevation_ft      │ BIGINT      │ YES     │         │         │         │
    │ continent         │ VARCHAR     │ YES     │         │         │         │
    │ iso_country       │ VARCHAR     │ YES     │         │         │         │
    │ iso_region        │ VARCHAR     │ YES     │         │         │         │
    │ municipality      │ VARCHAR     │ YES     │         │         │         │
    │ scheduled_service │ VARCHAR     │ YES     │         │         │         │
    │ gps_code          │ VARCHAR     │ YES     │         │         │         │
    │ iata_code         │ VARCHAR     │ YES     │         │         │         │
    │ local_code        │ VARCHAR     │ YES     │         │         │         │
    │ home_link         │ VARCHAR     │ YES     │         │         │         │
    │ wikipedia_link    │ VARCHAR     │ YES     │         │         │         │
    │ keywords          │ VARCHAR     │ YES     │         │         │         │
    │ the_geom          │ GEOMETRY    │ YES     │         │         │         │
    ├───────────────────┴─────────────┴─────────┴─────────┴─────────┴─────────┤
    │ 19 rows                                                       6 columns │
    └─────────────────────────────────────────────────────────────────────────┘
    ```

### Traiter des données parquet d'Overture Maps avec DuckDB

Les données d’Overture Maps sont fournies sous forme de fichier Parquet ([décrites ici](https://docs.overturemaps.org/overview/feature-model/)), nous allons donc importer ces données dans une base pour les consulter.

#### Importer les données dans la base

Dans cet exemple, on récupère 100 bâtiments aléatoirement ; environ une minute de traitement chez moi.

=== ":snake: Python"

    ```python
    query_buildings = ("create table buildings as ( SELECT"
        "type,"
        "version,"
        "height,"
        "level,"
        "class,"
        "JSON(names) as names,"
        "JSON(sources) as sources,"
        "ST_GeomFromWKB(geometry) as geometry"
        "FROM"
        "read_parquet('s3://overturemaps-us-west-2/release/2024-04-16-beta.0/theme=buildings/type=*/*', hive_partitioning=1)"
        "LIMIT 100);"
    )

    con.sql(query_buildings)
    ```

=== ":material-console: CLI"

    ```sh
    create table buildings as ( SELECT
    type,
    version,
    height,
    level,
    class,
    JSON(names) as names,
    JSON(sources) as sources,
    ST_GeomFromWKB(geometry) as geometry
    FROM
    read_parquet('s3://overturemaps-us-west-2/release/2024-04-16-beta.0/theme=buildings/type=*/*', hive_partitioning=1)
    LIMIT 100);
    ```

Dans cet autre exemple, on récupère les bâtiments d’une partie de la ville de Laval en indiquant les coordonnées d’un rectangle (attention requête assez longue)

=== ":snake: Python"

    ```python
    query_buildings = ("create table laval_buildings as ( SELECT "
    "type,"
    "version,"
    "height,"
    "level,"
    "class,"
    "JSON(names) as names,"
    "JSON(sources) as sources,"
    "ST_GeomFromWKB(geometry) as geometry"
    "FROM"
    "read_parquet('s3://overturemaps-us-west-2/release/2024-04-16-beta.0/theme=buildings/type=*/*', hive_partitioning=1)"
    "WHERE bbox.xmin > -0.7948129589175504"
    "AND bbox.xmax < -0.7472280816538276"
    "AND bbox.ymin > 48.069335046027035"
    "AND bbox.ymax < 48.073450034830316 );")

    con.sql(query_admins)
    ```

=== ":material-console: CLI"

    ```sh
    create table laval_buildings as ( SELECT
    type,
    version,
    height,
    level,
    JSON(names) as names,
    JSON(sources) as sources,
    ST_GeomFromWKB(geometry) as geometry
    FROM
    read_parquet('s3://overturemaps-us-west-2/release/2024-04-16-beta.0/theme=buildings/type=*/*', hive_partitioning=1)
    WHERE bbox.xmin > -0.7948129589175504
    AND bbox.xmax < -0.7472280816538276
    AND bbox.ymin > 48.069335046027035
    AND bbox.ymax < 48.073450034830316);
    ```

#### Visualiser les données dans ArqGIS

Pour cela, installer le plugin ArqGIS [QDuckDB](https://oslandia.gitlab.io/qgis/qduckdb/), en cochant la case `Afficher les extensions expérimentales` dans l'onglet `Paramètres` du gestionnaire d'extensions.

![qduckdb](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/duckdb_spatial/qduckdb.png){: .img-center loading=lazy }

Puis charger la couche avec le plugin.

![qgis](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/duckdb_spatial/overtures_maps.png){: .img-center loading=lazy }

!!! info "Transparence"
    Attention, cette extension est encore expérimentale (je suis bien placé pour le savoir puisque j'en suis l'un des principaux développeurs :wink:). N'hésitez pas à la tester et à nous faire des retours !  
    J'en profite pour préciser que cet article est une initiative personnelle de ma part. En aucun cas cet article est rédigé ou financé dans le cadre de mes activités chez Oslandia en tant que développeur du plugin.

#### Convertir les données en un GeoJSON en utilisant DuckDB

Un des atouts de DuckDB est qu'en plus d’intégrer des données pour les traiter en base, il peut servir d’outil de conversion pour des données Parquet. Exemple : si on me donne des données en Parquet et je souhaite des GeoJSON, DuckDB peut les convertir sans créer de table ni de base !

=== ":snake: Python"

    ```python
    query_export_buildings = ("COPY ( "  
    "SELECT "
    "type,"
    "version,"
    "height,"
    "level,"
    "class,"
    "JSON(names) as names,"
    "JSON(sources) as sources,"
    "ST_GeomFromWKB(geometry) as geometry"
    "FROM"
    "read_parquet('s3://overturemaps-us-west-2/release/2024-04-16-beta.0/theme=buildings/type=*/*', hive_partitioning=1)"
    "WHERE bbox.xmin > -0.7948129589175504"
    "AND bbox.xmax < -0.7472280816538276"
    "AND bbox.ymin > 48.069335046027035"
    "AND bbox.ymax < 48.0842516213572821)  "
    "TO 'laval_buildings.geojson' "
    " WITH (FORMAT GDAL, DRIVER 'GeoJSON', SRS 'EPSG:4326'); ")

    con.sql(query_export_buildings)
    ```

=== ":material-console: CLI"

    ```sh
    COPY (
    SELECT
    type,
    version,
    height,
    level,
    JSON(names) as names,
    JSON(sources) as sources,
    ST_GeomFromWKB(geometry) as geometry
    FROM
    read_parquet('s3://overturemaps-us-west-2/release/2024-04-16-beta.0/theme=buildings/type=*/*', hive_partitioning=1)
    WHERE bbox.xmin > -0.7948129589175504
    AND bbox.xmax < -0.7472280816538276
    AND bbox.ymin > 48.069335046027035
    AND bbox.ymax < 48.073450034830316)
    TO 'laval_buildings.geojson'
    WITH (FORMAT GDAL, DRIVER 'GeoJSON', SRS 'EPSG:4326');
    ```

    :bulb: Il est également possible d'exporter en Shapefile, pour cela, il faut remplacer les deux dernières lignes par celles-ci :

    ```sql
    TO 'laval_buildings.shp'
    WITH (FORMAT GDAL, DRIVER 'ESRI Shapefile', SRS 'EPSG:4326');
    ```

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}

<!-- Abbreviations -->
*[CLI]: pour "Command-Line Interface", une interface en ligne de commande, c'est-à-dire qu'on utilise le terminal (ou la console) pour interagir avec un logiciel.
