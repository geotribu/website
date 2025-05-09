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

L'avantage de DBT est qu'il ne vient pas en coupure du moteur de bases de données sous-jacent mais, qu'au contraire, il s'appuie pleinement sur ce dernier. De fait, toute la puissance du moteur est là, entre tes mains. Avoue que c'est vraiment un plus quand on dispose d'un système extensible tel que [PostgreSQL](https://www.postgresql.org/) pour, au hasard, traiter des données géographiques avec [PostGIS](https://postgis.net/). 

Tu es septique, je l'étais aussi ! Histoire d'accroitre un peu plus tes doutes, je dois t'apprendre que pour faire les transformations, tu auras uniquement droit à des `select` ; ni `ìnsert` ni `update` et encore moins de `create` puisque c'est DBT qui prend en charge la partie [DDL (Data Definition Language)](https://fr.wikipedia.org/wiki/Langage_de_d%C3%A9finition_de_donn%C3%A9es).

Difficile, impossible même, pour moi de faire de toi un expert DBT en seulement quelques lignes. Voyons quand-même les notions essentielles et si tu souhaites aller plus loin, je te conseille [comme Satya a déjà pu le faire dans son article](https://geotribu.fr/articles/2025/2025-02-25_stack_data_gard/) de visionner [la playlist DBT de Michael Kahan](https://www.youtube.com/playlist?list=PLy4OcwImJzBLJzLYxpxaPUmCWp8j1esvT). 

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

Il est construit avec un couple SQL+Jinja / YAML :

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

Lorsqu'on souhaite factoriser du code, il est d'usage en bases de données de créer des procédures stockées. Avec DBT, on utilisera plutôt des [macros](https://docs.getdbt.com/docs/build/jinja-macros#macros).

Les macros sont des blocs de SQL réutilisables. Par exemple, dans la requête de transformation Hubeau qui précède, tu peux voir un appel à `to_utc_timestamp_or_null`.

Cette macro, nous l'avons développée pour faciliter les transformations de chaînes de caractères en dates et heures tout en s'assurant que la conversion n'entraine pas une erreur par la validation préalable d'une [expression régulière](https://fr.wikipedia.org/wiki/Expression_r%C3%A9guli%C3%A8re).

```sql
{% macro to_utc_timestamp_or_null(column, regexp_check, format) %}
    case when {{ column }} ~ '{{ regexp_check }}' then to_timestamp({{ column }}, '{{ format }}')::timestamp at time zone 'UTC' end
{% endmacro %}
```

### Architecture en médaillon

L'architecture en médaillon n'est pas propre à DBT. Il s'agit d'un modèle de structuration des données en 3 couches :

- La couche _Bronze_ : Cette couche correspond aux données non transformées telles qu'extraites depuis leur source.
- La couche _Silver_ : Dans cette couche, les données sont nettoyées, validées et transformées. Il peut notamment être question de [normalisation](https://fr.wikipedia.org/wiki/Forme_normale_(bases_de_donn%C3%A9es_relationnelles)) et d'enrichissement via le croisement et l'association de données provenant de sources distinctes.
- La couche _Gold_ : Cette couche contient les données hautement transformées et agrégées, prêtes pour l'analyse et la consommation par les utilisateurs finaux. Les données sont en général dénormalisées pour en faciliter l'analyse ; [modèles en étoile](https://fr.wikipedia.org/wiki/%C3%89toile_(mod%C3%A8le_de_donn%C3%A9es)) ou [_"one big table"_](https://dataengineering.wiki/Concepts/Data+Modeling/One+Big+Table).

L'objectif est de garantir l’atomicité et la cohérence des traitements en isolant les différentes étapes de transformation dans des couches spécifiques.

![Architecture en médaillon](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/taradata_t_mapillary/medallion_architecture.png "Architecture en médaillon"){: .img-center loading=lazy }

Cette approche présente des similitudes avec l'architecture logicielle en 3 couches où chaque strate (et même chaque classe en programmation orientée objet) a une [responsabilité unique](https://fr.wikipedia.org/wiki/Principe_de_responsabilit%C3%A9_unique) ; la couche d'accès aux données, la couche métier et la couche de présentation.

### Matérialisation

La [matérialisation](https://docs.getdbt.com/docs/build/materializations) détermine la façon dont DBT stocke le résultat des transformations, c'est à dire le résultat d'exécution des modèles, dans l'entrepôt.

Concrètement, et dans la mesure où DBT se charge du DDL, il est question de lui dire s'il doit créer une table ou une vue dans la base de données.

En règle générale, les modèles sont organisés en couches suivant l'architecture en médaillon. Le mode de matérialisation est alors fixé au niveau du projet, dans le fichier [_dbt_project.yml_](https://docs.getdbt.com/reference/dbt_project.yml), pour l'ensemble des modèles d'une même couche.

```yml
models:
  taradata:
    2_staging:
        +materialized: view

    3_warehouses:
        +materialized: table

    4_marts:
        +materialized: table
```

Il reste possible de redéfinir cette matérialisation par défaut sur un modèle spécifique grâce à la clé `materialized` de la section `config` du YAML.

### Modèles incrémentaux

Lorsque les matérialisations `table` ou `view` sont retenues, DBT va recréer à chaque lancement la structure de données et donc exécuter l'ordre `create table as select...` ou `create view as select...` correspondant.

Cette approche a plusieurs avantages. D'une part, elle est résiliente car la suppression malencontreuse de la structure peut être corrigée en rejouant le modèle. Par ailleurs, comme toutes les données sont retraitées, il n'est pas utile d'identifier de façon chirurgicale les lignes ayant évoluées, ce qui rend la rédaction du modèle de transformation simple.

Cependant, les matérialisations `table` et `view` trouvent leurs limites quand le volume de données est important ou lorsque le but est de conserver l'historique des données alors même que la source ne le propose pas.

DBT propose pour cela le mode [`incremental`](https://docs.getdbt.com/docs/build/incremental-models). Avec lui, une table est créée à la première exécution du modèle. Les exécutions suivantes se chargent ensuite de mettre à jour et/ou d'insérer les nouvelles données en fonction du paramétrage défini pour le modèle.

### Lignage et parallélisation

C'est probablement le point fort de DBT ; sa capacité à déterminer le lignage des modèles.

Imagine, tu récupères le tout dernier millésime de la [BD TOPO®](https://geoservices.ign.fr/bdtopo) et tu dois reconstruire toutes les données qui dépendent du thème commune. _"Quels sont les processus que je dois relancer ? Est-ce que je dois faire celui-là avant celui-ci ? Peut-être que je peux lancer ces deux transformations en même temps pour aller plus vite, mais peut-être pas."_. Bref, la galère !

Grâce à DBT, plus besoin de se faire des noeuds au cerveau grâce au graphe de dépendances des modèles. 

![Lignage des données](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/taradata_t_mapillary/lignage.png "Lignage des données"){: .img-center loading=lazy }

Cette fonctionnalité ne se limite pas à un rendu graphique. Il est aussi possible de demander la reconstruction des modèles descendants grâce à la commande suivante :

`dbt run --select source:src_ign_bdtopo.commune+` 

Ce lignage permet non seulement à DBT de savoir l'ordre dans lequel il doit faire les transformations, mais il est aussi capable d'identifier les modèles indépendants qu'il est possible d'exécuter en parallèle.

### Documentation des modèles


----

## Transformation des _features_

<!-- geotribu:authors-block -->