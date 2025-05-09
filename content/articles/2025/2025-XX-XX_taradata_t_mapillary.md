---
title: "Transformation des features Mapillary avec DBT"
subtitle: "Transformation de données géographiques avec une Modern Data Stack basée sur Data Build Tool (DBT)"
authors:
    - Michaël GALIEN
categories:
    - article
comments: true
date: 2025-XX-XX
description: Transformation avec DBT des features extraites via les API de Mapillary au sein de la Modern Data Stack du Gard.
icon: fontawesome/solid/cubes-stacked
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/taradata_t_mapillary/affiche.png
tags:
    - DBT
    - Jinja
    - Mapillary
    - Modern Data Stack
    - Open Source
    - PostGIS
    - PostgreSQL
    - SQL
    - YAML
---

# Transformation des _features_ Mapillary avec DBT

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![Logo Mapillary](https://cdn.geotribu.fr/img/logos-icones/divers/mapillary.png "Logo Mapillary"){: .img-thumbnail-left }

Salut everybody, tout le monde ! Ça y est, c'est le deuxième article !

Dans le précédent opus, nous avons vu comment [Apache Airflow](https://airflow.apache.org/) nous permet d'extraire et de charger les [_features_ de Mapillary](https://help.mapillary.com/hc/en-us/articles/115002332165-Map-features) à proximité de réseau routier départemental gardois.

Cette fois, nous allons transformer les données pour les rendre exploitables avec [QGIS](https://qgis.org/) car, souviens-toi, nous avions stocker directement les éléments retournés par les API au format JSON.

Pour faire ces transformations, nous allons utiliser Data Build Tool ; [DBT](https://www.getdbt.com/) pour les intimes.

----

## DBT

![Logo DBT](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/dbt.png "Logo DBT"){: .img-thumbnail-left }

DBT est un outil de transformation, et uniquement de transformation, de données. En d'autres termes, il est incapable de faire de l'extraction et du chargement et s'attend à ce que les données à transformer soit déjà dans l'entrepôt sous leur forme brute.

Tout comme Apache Airflow, DBT est un outil "as code" qui mélange [SQL](https://fr.wikipedia.org/wiki/Structured_Query_Language), [Jinja](https://fr.wikipedia.org/wiki/Jinja_(moteur_de_template)) et [YAML](https://fr.wikipedia.org/wiki/YAML). Il va donc te falloir réviser tes `select`, `from` et `where`. Cela dit, peut-on vraiment faire l'impasse sur le SQL quand on fait de la data, qu'elle soit géographique ou non ? Je ne pense pas :innocent:.

L'avantage est que DBT ne vient pas en coupure du moteur de bases de données sous-jacent mais, qu'au contraire, il s'appuie pleinement sur ce dernier. De fait, toute la puissance du moteur est là, entre tes mains. Avoue que c'est vraiment un plus quand on dispose d'un système extensible tel que [PostgreSQL](https://www.postgresql.org/) pour, au hasard, traiter des données géographiques avec [PostGIS](https://postgis.net/). 

Tu es septique, je l'étais aussi ! Histoire d'accroitre un peu plus tes doutes, je dois t'apprendre que pour faire les transformations, tu auras uniquement droit à des `select` ; ni `ìnsert` ni `update` et encore moins de `create` puisque c'est DBT qui prend en charge la partie [DDL (Data Definition Language)](https://fr.wikipedia.org/wiki/Langage_de_d%C3%A9finition_de_donn%C3%A9es).

### Sources

Pour pouvoir faire les transformations, DBT a besoin de savoir où se trouvent les [sources](https://docs.getdbt.com/docs/build/sources) de données dans l'entrepôt. Concrètement, dans le cas de PostgreSQL, cela revient à lui indiquer les schémas et les tables à interroger.

La déclaration des sources se fait via un fichier YAML.

```yml
version: 2

sources: 
  - name: src_hubeau_eaufrance_fr
    tables:
      - name: stations
        tags: ["monthly"]
      - name: observations_tr
        tags: ["every_10min"]
```

Par défaut en PostgreSQL, le nom de la source correspond au nom du schéma, mais il est également possible de préciser le schéma via la clé `schema`.

### Models

Un [modèle](https://docs.getdbt.com/docs/build/models) est la description d'une transformation à faire.

Il est construit avec un couple SQL+Jinja/YAML :

- Le SQL+Jinja va porter la requête `select` de transformation des données.
- Le YAML va quant à lui donner les informations utiles à DBT pour générer la partie DDL en précisant par exemple le schéma et le nom de la table ou de la vue de stockage.

En aucun cas, le SQL ne doit accéder directement à une table ou une vue de l'entrepôt. Les `from` doivent à la place faire référence à une source, via le template Jinja `{{ source("<source_name>", "<table_name>") }}`, ou à un autre modèle, via le template Jinja `{{ ref("<model_name>") }}`.

Voici par exemple un modèle de transformation des observations extraites et chargées dans l'entrepôt au format JSON depuis l'[API Hydrométrie de Hubeau](https://hubeau.eaufrance.fr/page/api-hydrometrie).

```yml
version: 2

models:
  - name: stg_hubeau_eaufrance_fr__observations
    config: 
      alias: observations
      schema: stg_hubeau_eaufrance_fr
```

```sql
with observations as (
    select *
    from {{ source("src_hubeau_eaufrance_fr", "observations_tr")}}
),
details_observations as (
    select
        observations.code_station,
        details_observation
    from observations
    cross join jsonb_array_elements(observations -> 'data') as details_observation
),
selections_typages_renommages as (
    select
        code_station,
        {{ to_utc_timestamp_or_null("details_observation ->> 'date_obs'", '^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$', 'YYYY-MM-DD"T"HH24:MI:SS"Z"') }} as date_heure,
        (details_observation ->> 'resultat_obs')::numeric as resultat,
        details_observation ->> 'grandeur_hydro' as grandeur_hydro
    from details_observations
)
select *
from selections_typages_renommages
```

### Macros

Lorsqu'on souhaite factoriser du code, il est d'usage de créer des procédures stockées. Avec DBT, on utilisera plutôt des [macros](https://docs.getdbt.com/docs/build/jinja-macros#macros).

Les macros sont des blocs de SQL réutilisables. Par exemple, dans la requête de transformation Hubeau qui précède, tu peux voir un appel `to_utc_timestamp_or_null`.

Cette macro, nous l'avons développée pour faciliter les transformations de chaînes en dates et heures tout en s'assurant que la conversion n'entraine pas une erreur par la validation préalable d'une [expression régulière](https://fr.wikipedia.org/wiki/Expression_r%C3%A9guli%C3%A8re).

```sql
{% macro to_utc_timestamp_or_null(column, regexp_check, format) %}
    case when {{ column }} ~ '{{ regexp_check }}' then to_timestamp({{ column }}, '{{ format }}')::timestamp at time zone 'UTC' end
{% endmacro %}
```

### Matérialisation

### Modèles incrémentaux

### Architecture en médaillon

### Lignage

### Documentation

### Ressources

<!-- geotribu:authors-block -->