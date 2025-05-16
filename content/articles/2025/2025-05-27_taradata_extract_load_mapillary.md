---
title: "Extraction et chargement des features Mapillary avec Apache Airflow"
subtitle: "Un article qui brasse de l'air et des data."
authors:
    - Michaël GALIEN
categories:
    - article
comments: true
date: 2025-05-27
description: Utilisation des API de Mapillary au sein de la Modern Data Stack du Gard pour extraire et charger des objets détectés (features) sur les images.
icon: fontawesome/solid/cubes-stacked
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/taradata_el_mapillary/affiche.png
tags:
    - Apache Airflow
    - Mapillary
    - Modern Data Stack
    - Open Source
    - PostGIS
    - PostgreSQL
    - Python
---

# Extraction et chargement des _features_ Mapillary avec Apache Airflow

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![Logo Mapillary](https://cdn.geotribu.fr/img/logos-icones/divers/mapillary.png "Logo Mapillary"){: .img-thumbnail-left }

Salut à toi chère lectrice/cher lecteur ! Dans son article intitulé ["L'enjeu de la data au département du Gard"](/articles/2025/2025-02-25_stack_data_gard/), [Satya](/team/satya-minguez/) t'explique comment nous avons combiné _Modern Data Stack_ (MDS) et géomatique au sein de notre _stack data_, qui porte le joli petit nom de **Taradata**.

Le but : être en mesure de valoriser le patrimoine de données départemental (rien que ça !) et ainsi offrir aux élus, aux directions et aux services, les informations clés pour la prise de décisions et le suivi de leurs actions.

Conformément aux principes de la MDS, Taradata est construite de façon modulaire avec notamment [PostgreSQL](https://www.postgresql.org/)/[PostGIS](https://postgis.net/) pour l'entreposage des données, [Apache Airflow](https://airflow.apache.org/) pour l'orchestration des traitements et [DBT](https://www.getdbt.com/) pour les transformations.

Les données sont extraites depuis leur source avant d'être chargées dans l'entrepôt pour enfin être transformées. Et oui ! La transformation arrive après le chargement suivant la méthodologie ELT (Extract > Load > Transform) et contrairement à l'ETL.

Dans cet article, je vais t'expliquer comment nous utilisons Apache Airflow et Python pour extraire et charger dans notre entrepôt les [_features_ de Mapillary](https://help.mapillary.com/hc/en-us/articles/115002332165-Map-features). Dans un article à venir, tu pourras voir comment nous transformons cette donnée brute en une information utile à la direction des routes grâce à DBT.

Ces deux articles te rappelleront peut-être [celui de Florian sur ce même sujet](/articles/2022/2022-05-31_donnees_mapillary/). Le script qu'il propose s'appuie sur les tuiles vectorielles. Notre approche quant à elle utilise les API. Deux départements limitrophes, une rivalité, et donc 2 façons de voir le monde ; le Gard ne pouvant pas faire comme l'Hérault (:kissing_heart: Florian). :three:, :two:, :one:, c'est parti !

Ah non ! J'ai failli oublier. Si je tiens la plume AZERTY aujourd'hui, je me dois de remercier [Leo Pironti](https://www.linkedin.com/in/leo-pironti-379557293/) pour son travail sur le sujet. En effet, c'est Leo qui a rédigé la majeure partie du code que je m'apprête à te décrire. Ce travail, il l'a fait dans le cadre de son stage de première année de [BTS SIO à la CCI du Gard](https://lycee.gard.cci.fr/formations/bts-services-informatiques-aux-organisations-sio/). Alors merci Leo et cette fois :three:, :two:, :one:, c'est vraiment parti !!!

----

## Apache Airflow

![Logo Apache Airflow](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/airflow.png "Logo Apache Airflow"){: .img-thumbnail-left }

Apache Airflow est un outil d'orchestration orienté data. Son rôle est de déclencher des traitements lorsque les conditions de lancement sont réunies. Il propose également une interface graphique de suivi d'exécution avec la possibilité, par exemple, de visualiser les logs et de relancer manuellement une tâche en échec.

![Aperçu Apache Airflow](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/taradata_el_mapillary/demo_grid_view_with_task_logs.png "Aperçu Apache Airflow"){: .img-center loading=lazy }

Ce n'est pas le seul outil à proposer cela, on peut par exemple citer [Dagster](https://dagster.io/), [Prefect](https://www.prefect.io/) ou encore le français [Kestra](https://kestra.io/) (Cocorico :flag_fr: !!!). Cependant, après étude, Apache Airflow nous a paru être la meilleure option pour répondre à nos objectifs et contraintes (voir [les commentaires dans l'article de Satya](/articles/2025/2025-02-25_stack_data_gard/#satya-minguez) pour plus de détails).

Avant de rentrer dans le vif du sujet, voyons quelques concepts clés de l'outil.

### _DAG_ et _Task_

Avec Apache Airflow, un traitement est décrit comme un graphe acyclique dirigé ; un _DAG_ en _n'english_. Il s'agit d'un ensemble de tâches à exécuter, celles-ci pouvant être réalisées en séquence ou en parallèle. Un _DAG_ a un début et une fin et il est impossible de boucler d'où le "acyclique dirigé".

Les fans de [FME](https://fme.safe.com/) ou autre ETL graphique risquent d'être bousculés en découvrant que la réalisation d'un _DAG_ se fait grâce à un script Python ; exit donc les glisser-déplacer dans une IHM, Apache Airflow adopte l'approche "as code". Ici, nous utilisons majoritairement [Visual Studio Code](https://fr.wikipedia.org/wiki/Visual_Studio_Code) pour construire nos _DAGs_ mais d'autres options sont possibles.

Si elle peut faire peur, cette approche présente plusieurs avantages. Elle facilite le travail collaboratif et permet le versionning via des outils tels que [Git](https://fr.wikipedia.org/wiki/Git). D'ailleurs, l'approche "as code" est plébiscitée dans d'autres domaines que celui de la data avec par exemple [Terraform](https://developer.hashicorp.com/terraform) pour la gestion des infrastructures.

Apache Airflow propose deux syntaxes pour décrire les tâches. La première s'appuie sur des [_Operators_](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/operators.html) c'est-à-dire des classes Python qu'il suffit d'instancier. Il en existe de nombreux parmi lesquels le `BashOperator` pour lancer une commande bash ou l'`EmailOperator` pour, tu l'as deviné, envoyer un e-mail.

Désormais, la syntaxe [_TaskFlow_](https://airflow.apache.org/docs/apache-airflow/stable/tutorial/taskflow.html) est privilégiée. Avec elle, une tâche est décrite à l'aide d'une simple fonction Python précédée du décorateur `@task`. Cette méthode est plus lisible car plus ["pythonique"](https://fr.wiktionary.org/wiki/pythonique).

Plusieurs options sont également disponibles pour créer un _DAG_ mais avec _TaskFlow_ le principe est identique ; un _DAG_ est une fonction Python décorée d'un `@dag`.

A noter qu'il est possible de mixer, au sein d'un même _DAG_, les deux syntaxes.

Ci-dessous, un exemple de _DAG_ pour récupérer chaque heure la hauteur d'eau du Gardon à Anduze grâce à l'[API Hydrométrie de Hubeau](https://hubeau.eaufrance.fr/page/api-hydrometrie).

``` py
import requests
from airflow.decorators import dag, task
from datetime import datetime

@dag(dag_id = "un_exemple_de_dag",
     start_date = datetime(2025, 1, 1),
     schedule_interval = "@hourly",
     tags = ["extract", "load", "hourly"],
     catchup = False)
def mon_dag():

    @task(task_id = "appel_api_hubeau")
    def ma_premiere_tache():
        response = requests.get(
            "https://hubeau.eaufrance.fr/api/v2/hydrometrie/observations_tr?code_entite=V714401001&size=1&grandeur_hydro=H"
        )
        response.raise_for_status()
        return response.json()

    @task(task_id = "isolation_hauteur_eau")
    def ma_seconde_tache(response):
        hauteur = response.get("data")[0].get("resultat_obs")
        print("Hauteur d'eau :", hauteur)

    ma_seconde_tache(ma_premiere_tache())

mon_dag()
```

Apache Airflow scrute à intervalles réguliers un répertoire dans lequel les fichiers .py des _DAGs_ doivent être déposés. Aussi, il suffit d'enregistrer ce fichier à l'emplacement qui convient pour le voir apparaitre, après un petit délai d'interprétation, dans l'IHM d'Apache Airflow.

!!! info "Airflow 3.0 est sorti"
	Au moment où j'écris ces lignes, la version 3.0 d'Apache Airflow vient de sortir.

	Celle-ci arrive avec de nombreuses nouveautés. Il est désormais possible de spécifier plusieurs emplacements pour les fichiers .py des _DAGs_ via les [_DAG bundles](https://airflow.apache.org/docs/apache-airflow/stable/administration-and-deployment/dag-bundles.html). Il semble même possible de demander à Apache Airflow de charger les _DAGs_ directement depuis un repository Git.

	Pour plus d'informations sur la version 3.0, tu peux consulter le blog d'[Apache Airflow](https://airflow.apache.org/blog/airflow-three-point-oh-is-here/).

### _Scheduler_, _Executor_ et _Workers_

Un _DAG_ correspond donc un ensemble de tâches à réaliser...mais il faut bien que quelqu'un s'occupe de les exécuter ces tâches justement !

La responsabilité de l'exécution des tâches incombe à trois briques d'Apache Airflow :

- Le _Scheduler_ : Il est responsable de la planification des tâches. Il décide quand elles doivent être exécutées en fonction du calendrier de lancement et de leurs dépendances.
- L'_Executor_ : Il gère l'exécution des tâches planifiées par le _Scheduler_. [Plusieurs natures d'_Executor_ sont disponibles](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/index.html) et le type à utiliser est fixé par paramétrage. Par exemple, le [`CeleryExecutor`](https://docs.celeryq.dev/en/stable/getting-started/introduction.html) est capable de distribuer l'exécution sur plusieurs serveurs.
- Les _Workers_ : Ce sont les processus qui exécutent réellement les tâches. Ils reçoivent les tâches à faire du _Scheduler_ via l'_Executor_.

![Architecture d'Apache Airflow](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/taradata_el_mapillary/architecture_apache_airflow.jpg "Architecture d'Apache Airflow"){: .img-center loading=lazy }

### Instances et statuts

Un _DAG_ et ses tâches associées décrivent les traitements à effectuer. Lorsque ceux-ci sont exécutés, on parle respectivement d'instance de _DAG_ et d'instance de tâche.

Les instances de _DAG_ et de tâche ont des statuts qui renseignent sur l'état de leur exécution.

Ainsi une instance de tâche passera de `queued` à `running` lorsqu'un _Worker_ la prendra en charge. Si le traitement se termine sans erreur, l'instance prendra l'état `success`. Dans le cas contraire, elle sera en `failed` ou en `up_for_retry` si plusieurs tentatives ont été paramétrées.

![Les statuts possibles d'une tâche](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/taradata_el_mapillary/task_status.png "Les statuts possibles d'une tâche"){: .img-center loading=lazy }

----

## Extraction et chargement des _features_

![Logo de Python](https://cdn.geotribu.fr/img/logos-icones/programmation/python.png "Logo Python"){: .img-thumbnail-left }

Après cette entrée en matière sur Apache Airflow, voyons maintenant le script Python de notre _DAG_ d'extraction et de chargement des _features_ grâce aux API proposées par Mapillary.

### Tâche 1 – création du schéma

La première tâche de notre _DAG_ consiste en la création du schéma d'accueil dans l'entrepôt PostgreSQL.

``` py
create_schema_task = postgresql_tasks.create_schema(taradata_storage, target_schema)
```

Alors oui, on ne voit pas de décorateur `@task` ici. C'est simplement parce que nous nous sommes créés une boîte à outils de tâches et que, la création d'un schéma étant quelque chose de courant dans nos _DAGs_, nous y avons intégré cette opération.

Regardons donc le code de cette fonction.

``` py
@task(task_id = "créer_schéma")
def create_schema(pg_storage: BasePostgreSQLDataStorage, schema: str):
    """
    Tâche de création d'un schéma dans une base de données PostgreSQL.

    pg_storage : La base de données PostgreSQL.
    schema : Le nom du schéma à créer.
    """
    _execute_sql_statement(pg_storage, f"create schema if not exists {schema}")
```

### Tâche 2 – création de la table de chargement des données

Avec cette seconde tâche, nous créons la table d'accueil des données que nous nous apprêtons à extraire.

``` py
create_table_task = postgresql_tasks.execute_sql_statement.override(task_id = "créer_table_temporaire")(
    taradata_storage,
    """
    drop table if exists tmp_features;

    create table tmp_features(
        geom geometry(polygon, 4326) primary key,
        id_tache integer not null,
        informations jsonb
    );
    """,
    search_path = f"{target_schema},public"
)
```

Toujours pas de décorateur en vue, tout comme pour la création du schéma, le code de cette tâche est disponible dans notre boîte à outils.

Si tu es attentif, tu auras probablement remarqué que nous utilisons le type `jsonb`. Mais pourquoi diable faire cela ?!? La raison est simple, et nous l'avons dit plus haut, c'est parce que nous travaillons suivant un modèle ELT.

En effet, les API de Mapillary retournent les résultats au format JSON. C'est ce résultat que nous allons stocker directement dans l'entrepôt. Après tout, n'en déplaise à [MongoDB](https://www.mongodb.com/), PostgreSQL se débrouille très bien avec le JSON comme nous l'explique [cet autre article de Thomas](/articles/2025/2025-01-21_travailler-avec-JSON-et-PostgreSQL/).

La transformation de ces données JSON en quelque chose d'exploitable, avec [QGIS](https://qgis.org/) par exemple, ne sera réalisée que par la suite avec DBT. Ce sera l'objet du prochain article.

Avant de poursuivre, nous devons chaîner les tâches. En effet, il ne faut pas essayer de créer la table avant d'avoir terminé la création du schéma. Ceci est fait grâce à l'opérateur `>>`.

``` py
create_schema_task >> create_table_task
```

### Tâche 3 – calcul de l’emprise d’extraction et répartition du travail

Bien, passons aux choses sérieuses !

L'API de Mapillary permet de récupérer les _features_ présentes dans une [_bbox_](https://en.wikipedia.org/wiki/Minimum_bounding_rectangle) passée en paramètre d'appel. Cependant, [la documentation](https://www.mapillary.com/developer/api-documentation?locale=fr_FR#map-feature) précise que ce sont au maximum 2000 _features_ qui seront renvoyées sans possibilité d'itérer sur les résultats suivants ; l'API n'étant pas paginée.

Comme seuls les éléments à proximité du réseau routier départemental nous intéressent, nous allons calculer une grille sur l'emprise du référentiel routier et ne conserver que les cellules à proximité immédiate d'un tronçon.

Ceci est fait grâce aux 2 [_CTE_](https://www.postgresql.org/docs/current/queries-with.html) suivantes.

``` sql
with emprise as (
    select ST_Collect(geom) as geom
    from troncons_wgs84
),
cellules as (
    select sg.geom
    from emprise e
    cross join ST_SquareGrid(0.01, e.geom) sg
    where exists (
        select *
        from troncons_wgs84 t
        where ST_DWithin(sg.geom, t.geom, 0.0001)
    )
),
```

À noter que l'API attend des coordonnées en WGS84 pour la _bbox_, les distances sont donc exprimées en degrés. La valeur `0.01` correspond à des cellules d'environ 800 mètres * 1100 mêtres. Parmi elles, seules celles à moins de `0.0001` d'un tronçon (environ 10 mètres) sont conservées grâce à l'appel à `ST_DWithin`. Tout ceci est approximatif et comme Loïc nous l'a démontré dans sa série d'articles, [en SIG il faut être tolérant](/articles/2024/2024-08-08_de-la-tolerance-en-sig-geometrie-04-postgis-oracle-ms-sql-server/).

Au regard du réseau géré par le département du Gard, ce sont ici plus de 4000 cellules qui sont retournées.

Nous aurions tout à fait pu créer 4000 tâches d'extraction des _features_, une par cellule, mais il s'avère que cette approche n'est pas optimale...revenons un peu sur le fonctionnement d'Apache Airflow pour comprendre.

Le _Scheduler_ détermine les tâches à exécuter et charge l'_Executor_ de transmettre le travail à faire aux _Workers_. Or, d'une part le nombre de _Workers_ est limité. Par exemple, sur notre infra nous en avons configurés 3, chacun pouvant exécuter 4 tâches soit un total de 12 tâches en parallèle au maximum. D'autre part, le mécanisme d'attribution des tâches aux _Workers_ prend un peu de temps. Sur des traitements massifs comme celui-ci, il est donc plus optimal de lancer moins de tâches, mais de faire faire à chacune plus de choses.

L'idée est donc de répartir ces 4000 cellules à N tâches. Ainsi, pour une valeur de N à 8, chaque tâche aura à traiter 500 cellules. Le revers de la médaille est que plus la tâche doit faire de choses, plus il y aura de choses à refaire en cas d'échec et de réexécution. Nous verrons plus bas comment nous avons géré cette contrainte.

Ci-dessous, la _CTE_ de répartition des cellules à N tâches.

``` sql
repartition_aleatoire as (
    select geom, ntile(%(nb_taches)s) over(order by random()) as id_tache
    from cellules
)
```

Ne reste plus qu'à insérer cette répartition aléatoire dans notre table de chargement, ce qui donne la requête globale suivante.

``` sql
with emprise as (
    select ST_Collect(geom) as geom
    from troncons_wgs84
),
cellules as (
    select sg.geom
    from emprise e
    cross join ST_SquareGrid(0.01, e.geom) sg
    where exists (
        select *
        from troncons_wgs84 t
        where ST_DWithin(sg.geom, t.geom, 0.0001)
    )
),
repartition_aleatoire as (
    select geom, ntile(%(nb_taches)s) over(order by random()) as id_tache
    from cellules
)
insert into tmp_features (geom, id_tache)
select geom, id_tache
from repartition_aleatoire;
```

Nous pouvons alors afficher le résultat de cette répartition dans QGIS. De l'art cartographique !

![Répartition des cellules à 8 tâches](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/taradata_el_mapillary/repartition_cellules.jpeg "Répartition des cellules à 8 tâches"){: .img-center loading=lazy }

### Tâche 4 – extraction et chargement des _features_

#### Entête et pseudo-code

Tout est prêt pour extraire et charger les données. Histoire de ne pas rentrer directement dans le dur, analysons d'abord l'entête et le pseudo-code de la tâche.

``` py
@task(task_id = "extraire_charger_features", retries = 3)
def extract_load_features(extract_load_task_id: int):
    """
    Tâche d'extraction et de chargement des "features" présentes sur l'emprise de cellules.

    extract_load_task_id : Le numéro de tâche d'extraction et de chargement.
    """
    # récupération de la liste des cellules à extraire/charger
    # tant qu'il y a des cellules à extraire/charger
        # pour chaque cellule :
            # appel de l'API
            # si le résultat contient moins de 2000 éléments (limite de l'API)
                # alors, chargement du résultat dans la base de données
        # division des cellules qui n'ont pas pu être extraites/chargées
        # récupération de la nouvelle liste des cellules à extraire/charger
```

Cette fois, le décorateur `@task` est bien visible. Le paramètre `task_id`, déjà aperçu plus haut, permet d'identifier la tâche. Le `retries` quant à lui, indique à Apache Airflow de retenter l'exécution en cas d'échec. Il est également possible de définir le délai minimal entre deux tentatives via le paramètre `retry_delay`. En son absence, c'est la valeur par défaut qui s'applique soit 300 secondes.

La première étape consiste à récupérer la liste des cellules à extraire et charger. Ceci est fait en tenant compte du paramètre `extract_load_task_id` pour ne lister que les cellules attribuées à la tâche courante.

Ensuite, pour chacune des cellules, nous appelons l'API d'extraction des _features_.

Bien que nous ayons calculé une grille assez fine, il arrive que, sur certaines zones urbaines, 2000 éléments soient retournés. Ceci indique que la limite d'appel est atteinte ; le résultat est alors ignoré.

Si en revanche le nombre de _features_ retournées est en dessous du seuil, alors le JSON retourné est sauvegardé en base de données.

En sortie de boucle `pour chaque`, les cellules qui n'ont pas de JSON associé sont celles pour lesquelles le seuil des 2000 éléments a été atteint. Celles-ci sont alors divisées en plus petites cellules de sorte à diminuer la taille de la _bbox_ d'appel afin de passer en dessous du seuil.

De nouvelles cellules sont donc potentiellement créées à la sortie de la boucle `pour chaque`. Pour cette raison, la boucle `pour chaque` est incluse dans une autre boucle `tant qu'il y a` qui à chaque itération récupère à nouveau la liste des cellules à extraire et charger. Grâce à cela, la tâche ne sera terminée que lorsque les _features_ de toutes les cellules auront été extraites.

#### Récupération de la liste des cellules à traiter

Cette étape consiste simplement à exécuter la requête suivante.

``` sql
select
    geom,
    ST_XMin(geom) as x_min,
    ST_YMin(geom) as y_min,
    ST_XMax(geom) as x_max,
    ST_YMax(geom) as y_max
from tmp_features
where id_tache = %(id_tache)s
and informations is null
```

Le premier critère de la clause `where` permet de limiter la recherche à la tâche courante.

Le second filtre exclut les cellules pour lesquelles les _features_ ont déjà été extraites. Ce critère intervient dans deux cas :

- D'une part, comme vu dans le pseudo-code, plusieurs itérations peuvent être nécessaires lorsque 2000 éléments sont retournés pour certaines cellules. Dans ce cas, seules les nouvelles cellules issues de la division seront retournées pour l'itération suivante.
- D'autre part, si une erreur devait survenir, par exemple en cas d'indisponibilité du réseau au moment de l'appel à l'API, ce filtre permet de ne pas avoir à retraiter la totalité des cellules lors des `retries`. En effet, il serait dommage de refaire tous les appels si 90% de l'emprise a pu être traitée avant l'apparition de l'erreur.

#### Extraction des données

Sur chaque cellule, l'extraction se fait via un appel HTTP à l'API en passant en paramètre les bornes de la _bbox_.

Nous avons encapsulé cet appel dans la fonction ci-dessous.

``` py
def call_map_features_api(cell: dict):
    """
    Appel à l'API d'extraction des "features" au format JSON pour une cellule donnée.

    cell : La cellule pour laquelle les "features" doivent être extraites.
    """
    url = (
        "https://graph.mapillary.com/map_features"
        f"?access_token={mapillary_conn.password}"
        "&fields=id,aligned_direction,first_seen_at,last_seen_at,object_value,object_type,geometry"
        f"&bbox={cell['x_min']},{cell['y_min']},{cell['x_max']},{cell['y_max']}"
    )

    return http_helper.get_json(url, verify = False)
```

L'appel à `http_helper.get_json` fait référence à une fonction présente dans notre boîte à outils. Celle-ci s'appuie sur la bibliothèque Python `requests`.

Par ailleurs, Apache Airflow propose [la gestion de connexions](https://airflow.apache.org/docs/apache-airflow/stable/howto/connection.html) ce qui permet de ne pas avoir à faire apparaitre les secrets (utilisateur, mot de passe, token, ...) dans le code source. Ici, la variable `mapillary_conn` est globale au _DAG_ et a été initialisée grâce à la méthode [`get_connection_from_secrets`](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/models/connection/index.html#airflow.models.connection.Connection.get_connection_from_secrets). Elle contient dans son champ `password` le token qui nous permet d'interroger l'API de Mapillary.

#### Chargement des données

Le chargement des données consiste en la mise à jour du champs `ìnformations` (type `jsonb`) de la table de chargement pour la géometrie correspondante.

``` sql
update tmp_features
set informations = %(informations)s
where ST_Equals(geom, (%(geom)s)::geometry);
```

#### Division des cellules non traitées

Les cellules pour lesquelles 2000 _features_ ont été retournées sont supprimées et remplacées par 4 cellules plus petites.

La suppression et l'ajout sont réalisés en un seul ordre SQL grâce au mot-clé [`returning`](https://www.postgresql.org/docs/current/dml-returning.html) qui permet de récupérer tout ou partie des champs des lignes modifiées.

``` sql
with cellules_a_diviser as (
    delete
    from tmp_features
    where id_tache = %(id_tache)s
    and informations is null
    returning geom
)
insert into tmp_features (geom, id_tache)
select sg.geom, %(id_tache)s
from cellules_a_diviser cad
inner join ST_SquareGrid((ST_XMax(cad.geom)::numeric - ST_XMin(cad.geom)::numeric) / 2, cad.geom) sg
on ST_Intersects(sg.geom, cad.geom) and not ST_Touches(sg.geom, cad.geom)
```

Nous pouvons voir dans l'image ci-dessous que certaines cellules doivent être découpées une à deux fois pour permettre l'extraction de l'ensemble des _features_ de l'emprise.

![Découpage des cellules](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/taradata_el_mapillary/decoupage_cellules.jpeg "Découpage des cellules"){: .img-center loading=lazy }

#### Invocation multiple de la tâche

La tâche 4 est construite de sorte à traiter une sous-partie des quelques 4000 cellules pour lesquelles il faut extraire et charger les _features_.

Il faut donc invoquer autant de fois que souhaité la tâche pour chacune des sous-parties. Pour cela, nous mettons ces invocations dans une liste Python.

```py
extract_load_features_tasks = []
for extract_load_task_id in range(1, extract_load_tasks_count + 1):
    extract_load_features_tasks.append(extract_load_features.override(task_id = f"extraire_charger_features_{extract_load_task_id}")(extract_load_task_id))
```

L'appel à `override` permet de redéfinir les paramètres de la tâche. Nous l'utilisons ici pour mettre un intitulé distinct à chacune.

Il est ensuite possible de chaîner chaque invocation à la tâche qui précède en passant directement la liste Python à l'opérateur `>>`.

```py
compute_cells_task >> extract_load_features_tasks
```

### Tâche 5 – écrasement de la table destination

Après chargement, la table définitive de stockage des données est écrasée avec la table de chargement. Seul le champ `informations` est conservé, les autres champs n'étant utiles que pour la phase d'EL.

```py
replace_table_task = postgresql_tasks.execute_sql_statement.override(task_id = "remplacer_table")(
    taradata_storage,
    """
    begin;

    drop table if exists features cascade;
    create table features as select informations from tmp_features;
    drop table tmp_features;

    commit;
    """,
    search_path = target_schema
)
```

Le passage par la table temporaire `tmp_features` couplé à l'utilisation de la transaction `begin ... commit` nous assure la cohérence de l'entrepôt. En effet, en cas d'échec, la version antérieure des données extraites et chargées reste disponible.

### Planification du @dag et représentation graphique

L'ensemble des tâches est encapsulé dans un _DAG_ planifié de façon mensuelle.

```py
@dag(dag_id = "extraction_et_chargement__mensuel__mapillary_com",
     start_date = datetime(1993, 1, 10),
     schedule_interval = schedule.get_dag_cron(tags.extract_and_load, tags.monthly),
     tags = [tags.extract_and_load, tags.monthly],
     catchup = False,
     doc_md = dag_doc_md)
def dag():
```

La représentation graphique du _DAG_ est alors visible dans l'IHM d'Apache Airflow.

![_DAG_ d'EL des _features_ Mapillary](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/taradata_el_mapillary/extration_et_chargement__mensuel__mapillary_com.png "_DAG_ d'EL des _features_ Mapillary"){: .img-center loading=lazy }

La première tâche `ignorer_si_dag_subséquent_en_cours`, que nous n'avons pas évoquée, permet d'ignorer le lancement du _DAG_ si d'autres _DAGs_ de transformation ou d'export sont en cours. L'objectif est d'assurer la cohérence des données en étant sûr que celles-ci ne soient pas écrasées au moment de leur transformation ou de leur export.

Nous pouvons voir que les 8 tâches d'extraction et de chargement ne sont pas liées entre elles. Apache Airflow aura donc la possibilité de les exécuter en parallèle.

## Résultat

Après exécution, la table `features` est disponible dans le schéma `src_mapillary_com` de l'entrepôt.

Elle est constituée d'une unique colonne de type `jsonb` et contient un peu plus de 4000 lignes ; une par cellule.

![Table résultat de l'extraction et du chargement des _features_](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/taradata_el_mapillary/src_mapillary_com__features.png "Table résultat de l'extraction et du chargement des _features_"){: .img-center loading=lazy }

## Conclusion

Apache Airflow est donc un outil totalement adapté à la mise en oeuvre de processus automatisés de traitement de données, que celles-ci soient géographiques ou non.

Son approche "as code" et le fait qu'il soit construit sur Python permet de profiter des nombreuses bibliothèques du langage. Par ailleurs, la syntaxe _TaskFlow_ fait que le code à rédiger est syntaxiquement proche d'un script Python classique.

Une des forces d'Apache Airflow est qu'il est en mesure d'optimiser l'exploitation de l'infrastructure technique sous-jacente en parallélisant l’exécution des tâches indépendantes. Il est même en mesure de _"scaler"_ les traitements sur plusieurs serveurs via par exemple le `CeleryExecutor`.

Il permet également le traitement de certaines erreurs par le paramétrage de plusieurs tentatives d'exécution des tâches.

Enfin, en cas d'échecs répétés, il donne la possibilité à l'utilisateur de consulter les logs d'exécution et de relancer manuellement les tâches en erreur.

Concernant le déploiement, celui-ci est facilité via les [images Docker disponibles sur DockerHub](https://hub.docker.com/r/apache/airflow).

## Annexe - code complet du _DAG_

``` py
import gard.taradata.airflow.extensions.connection
import gard.taradata.airflow.schedule as schedule
import gard.taradata.airflow.tasks.dags.sensors as dags_sensors
import gard.taradata.airflow.tasks.database.postgresql_tasks as postgresql_tasks
import gard.taradata.constants.tags as tags
import gard.taradata.helpers.web.http_helper as http_helper
import json

from airflow.decorators import dag, task
from airflow.models.connection import Connection
from datetime import datetime
from gard.taradata.airflow.handlers.cursor import fetch_all_dict_handler
from gard.taradata.data.storage.ogr import *

dag_doc_md = """
Extraction et chargement des "features" détectées par l'IA de [Mapillary](https://www.mapillary.com).
Le code s'appuie sur l'[API map feature](https://www.mapillary.com/developer/api-documentation?locale=fr_FR#map-feature).
"""

@dag(dag_id = "extraction_et_chargement__mensuel__mapillary_com",
     start_date = datetime(1993, 1, 10),
     schedule_interval = schedule.get_dag_cron(tags.extract_and_load, tags.monthly),
     tags = [tags.extract_and_load, tags.monthly],
     catchup = False,
     doc_md = dag_doc_md)
def dag():

    mapillary_conn = Connection.get_connection_from_secrets("Mapillary")

    taradata_conn = Connection.get_connection_from_secrets("Taradata")
    taradata_storage = taradata_conn.to_postgresql_data_storage()

    target_schema = "src_mapillary_com"

    extract_load_tasks_count = 8

    # ---------------------------------------------------------------------------------------------
    # Tâche de synchronisation inter-DAGs.
    # ---------------------------------------------------------------------------------------------

    # ignore l'extraction/chargement si un DAG subséquent (transformation, export) est en cours
    skip_if_subsequent_dag_active = dags_sensors.dags_with_tags_inactive.override(
        task_id = "ignorer_si_dag_subséquent_en_cours",
        timeout = 0,
        soft_fail = True
    )({tags.transform, tags.export})

    # ---------------------------------------------------------------------------------------------
    # Tâche de création du schéma.
    # ---------------------------------------------------------------------------------------------

    create_schema_task = postgresql_tasks.create_schema(taradata_storage, target_schema)

    skip_if_subsequent_dag_active >> create_schema_task

    # ---------------------------------------------------------------------------------------------
    # Tâche de création d'une table temporaire de chargement.
    # ---------------------------------------------------------------------------------------------

    create_table_task = postgresql_tasks.execute_sql_statement.override(task_id = "créer_table_temporaire")(
        taradata_storage,
        """
        drop table if exists tmp_features;

        create table tmp_features(
            geom geometry(polygon, 4326) primary key,
            id_tache integer not null,
            informations jsonb
        );
        """,
        search_path = f"{target_schema},public"
    )

    create_schema_task >> create_table_task

    # ---------------------------------------------------------------------------------------------
    # Tâche de détermination des cellules d'extraction des "features".
    # ---------------------------------------------------------------------------------------------

    # calcul des cellules d'extraction au regard du référentiel routier départemental
    # les cellules sont réparties aléatoirement dans n groupes ou n est égal à extract_load_tasks_count
    compute_cells_task = postgresql_tasks.execute_sql_statement.override(task_id = "déterminer_cellules_extraction")(
        taradata_storage,
        """
        begin;

        create temporary table troncons_wgs84 on commit drop as
        select ST_Transform(geom, 4326) as geom
        from troncons
        where not fictif
        and (siren_proprietaire = '223000019' or siren_gestion_courante = '223000019');

        create index on troncons_wgs84 using gist (geom);

        with emprise as (
            select ST_Collect(geom) as geom
            from troncons_wgs84
        ),
        cellules as (
            select sg.geom
            from emprise e
            cross join ST_SquareGrid(0.01, e.geom) sg
            where exists (
                select *
                from troncons_wgs84 t
                where ST_DWithin(sg.geom, t.geom, 0.0001)
            )
        ),
        repartition_aleatoire as (
            select geom, ntile(%(nb_taches)s) over(order by random()) as id_tache
            from cellules
        )
        insert into tmp_features (geom, id_tache)
        select geom, id_tache
        from repartition_aleatoire;

        commit;
        """,
        statement_params = {"nb_taches": extract_load_tasks_count},
        search_path = f"{target_schema},wrh_referentiel_routier,public",
    )

    create_table_task >> compute_cells_task

    # ---------------------------------------------------------------------------------------------
    #  Tâches d'extraction et de chargement des "features" depuis Mapillary.
    # ---------------------------------------------------------------------------------------------

    def get_task_cells(extract_load_task_id: int):
        """
        Récupération de la liste des cellules à extraire et charger par une tâche donnée.

        extract_load_task_id : L'identifiant de la tâche d'extraction et de chargement.
        """
        return postgresql_tasks.execute_sql_statement.function(
            taradata_storage,
            """
            select
                geom,
                ST_XMin(geom) as x_min,
                ST_YMin(geom) as y_min,
                ST_XMax(geom) as x_max,
                ST_YMax(geom) as y_max
            from tmp_features
            where id_tache = %(id_tache)s
            and informations is null
            """,
            statement_params = {"id_tache": extract_load_task_id},
            search_path = f"{target_schema},public",
            handler = fetch_all_dict_handler
        )

    def call_map_features_api(cell: dict):
        """
        Appel à l'API d'extraction des "features" au format JSON pour une cellule donnée.

        cell : La cellule pour laquelle les "features" doivent être extraites.
        """
        url = (
            "https://graph.mapillary.com/map_features"
            f"?access_token={mapillary_conn.password}"
            "&fields=id,aligned_direction,first_seen_at,last_seen_at,object_value,object_type,geometry"
            f"&bbox={cell['x_min']},{cell['y_min']},{cell['x_max']},{cell['y_max']}"
        )

        return http_helper.get_json(url, verify = False)

    def divide_task_cells(extract_load_task_id: int):
        """
        Division des cellules non extraites et chargées en cellules de surface 4 fois inférieures.

        extract_load_task_id : L'identifiant de la tâche d'extraction et de chargement pour laquelle il faut diviser les cellules.
        """
        postgresql_tasks.execute_sql_statement.function(
            taradata_storage,
            """
            with cellules_a_diviser as (
                delete
                from tmp_features
                where id_tache = %(id_tache)s
                and informations is null
                returning geom
            )
            insert into tmp_features (geom, id_tache)
            select sg.geom, %(id_tache)s
            from cellules_a_diviser cad
            inner join ST_SquareGrid((ST_XMax(cad.geom)::numeric - ST_XMin(cad.geom)::numeric) / 2, cad.geom) sg
            on ST_Intersects(sg.geom, cad.geom) and not ST_Touches(sg.geom, cad.geom)
            """,
            statement_params = {"id_tache": extract_load_task_id},
            search_path = f"{target_schema},public",
        )

    @task(task_id = "extraire_charger_features", retries = 3)
    def extract_load_features(extract_load_task_id: int):
        """
        Tâche d'extraction et de chargement des "features" présentes sur l'emprise de cellules.

        extract_load_task_id : Le numéro de tâche d'extraction et de chargement.
        """
        # récupération de la liste des cellules à extraire/charger
        cells = get_task_cells(extract_load_task_id)

        while (cells):

            # pour chaque cellule :
            for cell in cells:

                # appel de l'API
                features = call_map_features_api(cell)

                if (len(features["data"]) < 2000):
                    # si le résultat contient moins de 2000 éléments (limite de l'API)
                    # alors, chargement du résultat dans la base de données  
                    postgresql_tasks.execute_sql_statement.function(
                        taradata_storage,
                        """
                        update tmp_features
                        set informations = %(informations)s
                        where ST_Equals(geom, (%(geom)s)::geometry);
                        """,  
                        statement_params = {
                            "informations": json.dumps(features),
                            "geom": cell["geom"]
                        },
                        search_path = f"{target_schema},public",
                        log_sql = False
                    )

            # division des cellules qui n'ont pas pu être extraites/chargées
            divide_task_cells(extract_load_task_id)

            # et récupération de la nouvelle liste des cellules à extraire/charger
            cells = get_task_cells(extract_load_task_id)

    extract_load_features_tasks = []
    for extract_load_task_id in range(1, extract_load_tasks_count + 1):
        extract_load_features_tasks.append(extract_load_features.override(task_id = f"extraire_charger_features_{extract_load_task_id}")(extract_load_task_id))

    compute_cells_task >> extract_load_features_tasks

    # ---------------------------------------------------------------------------------------------
    # Tâche de remplacement de la table définitive par la table temporaire de chargement.
    # ---------------------------------------------------------------------------------------------

    replace_table_task = postgresql_tasks.execute_sql_statement.override(task_id = "remplacer_table")(
        taradata_storage,
        """
        begin;

        drop table if exists features cascade;
        create table features as select informations from tmp_features;
        drop table tmp_features;

        commit;
        """,
        search_path = target_schema
    )

    extract_load_features_tasks >> replace_table_task

dag()
```

<!-- geotribu:authors-block -->
