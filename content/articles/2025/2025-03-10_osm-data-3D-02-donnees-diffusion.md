---
title: "OSM Data : des données OSM jusqu'au serveur carto, avec une interface d'administration, etc.."
subtitle: OSM Data 2/5
authors:
    - Karl TAYOU
    - Romain LATAPIE
categories:
    - article
comments: true
date: 2025-03-10
description: Cet article présente les mécanisme d'ingestion de données dans OSM DATA jusqu'à leur diffusion en flux WFS/WMS.
icon: material/emoticon-happy-outline
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_2/parcours_des_donnees_avant_visualisation_400.png
license: default
robots: index, follow
tags:
    - 3D
    - Digital twin
    - Giro3D
    - Three.js
    - jumeau numérique
    - OpenStreetMap
    - QGIS
    - QGIS SERVER
    - WFS/WMS
    - Smart City
---

# OSM DATA V2 : Des données à la cartographie

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

Dans l'article précédent, nous avons présenté les différentes possibilités d'ajout de données à OSM DATA. L'objet de cet article est d'expliciter techniquement les mécanismes mis en place pour ajouter les données.

Pour rappel, quatre étapes principales permettent l'affichage des données :

1. La définition puis la validation de la conformité des fichiers / requêtes SQL
2. L'intégration en base de données des données sous forme de table ou de vues dématérialisées
3. La création d'un projet QGIS et la définition de la symbologie associée à chaque couche
4. La création des flux WMS et WFS à l'aide des projets QGIS créé

![Parcours des données avant visualisation](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_1/parcours_des_donnees_avant_visualisation.png){: .img-center loading=lazy }

## Définition et validation de la conformité des fichiers / requêtes SQL

Dans l'article précédent, le module d'ajout des données est brièvement présenté, une fonction (optionnelle) de définition du type de géométrie est aussi incluse. Pour s'assurer d'une intégration dans les meilleures conditions, seul un type de géométrie est considéré pour chaque ajout.

![Ajout d'un jeu de données](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_2/creation_nouvelle_source.png){: .img-center loading=lazy }

### A partir d'un fichier SIG

Pour l'ajout de fichiers SIG avec Geopandas, la première étape est de créer un `GeoDataFrame` à partir des données :

```python title="Import d'un fichier SIG avec GeoPandas"
# Importation du fichier SIG
import geopandas
gpdSource: geopandas.GeoDataFrame = geopandas.read_file(self.file)
```

Une fois le fichier interprété avec succès et le `GeoDataFrame` créé, deux étapes de validation sont réalisées :

- Présence d'un seul type de géométrie :

    ```python title="Vérification du nombre de types de géométries"
    # Vérification du nombre de types de géométries
    if len(gpdSource.geom_type.unique()) > 1 :
        raise Exception("Votre fichier contient plusieurs types de géométries :(")
    ```

Dans le cadre d'une mise à jour du jeu de données, on vérifie également la conformité du type de géométrie entre les données sources et les données de mise à jour. Si ce n'est pas le cas, le jeu de données de mise à jour est considéré invalide (sa définition/symbologie dans QGIS dépendant du type de géométrie du jeu de données source).

- Présence d'entités au sein du fichier  :

    ```python title="Vérification que le fichier n'est pas vide"
    # Vérification que le fichier n'est pas vide
    if len(gpdSource.empty is False :
        raise Exception("Votre fichier ne contient aucune donnée :(")
    ```

Une fois ces vérification effectuées, on prépare la connexion à la base de données avec `SQLAlchemy` :

```python title="Connection à la base de données avec SQLAlchemy"
# Connexion à la base de données
from sqlalchemy import create_engine
engine = create_engine("postgresql://{db_user}:{db_password}@{db_host}{db_port}/{db_name}")
```

Enfin, l'importation en base de données est réalisé à l'aide de la commande `to_postgis` :

```python title="Intégration d'un GeoDataFrame en base de données"
# Intégration en base de données
gpdSource.to_postgis(
            name="nom_de_notre_table",
            con=engine,
            index=True,
            index_label="id",
)
```

La couche est insérée en base de données ! :fireworks:

### A partir d'une requête SQL

En ce qui concerne l'ajout d'un jeu de données à partir d'une requête QSL, on considère qu'une base de données est fournie avec des données d'OpenStreetMap par le biais d' OSM2PGSQL, un article détaille la procédure [ici](https://geotribu.fr/articles/2022/2022-06-28_import-donnees-osm-postgresql-osm2pgsql-osmium/).

On possède donc les trois principales tables de données d'OpenStreetMap à savoir `planet_osm_point`, `planet_osm_line` et `planet_osm_polygon`.

La définition d'une requête SQL sur les données OpenStreetMap est simplifiée : seule la clause de restriction (`WHERE`) de la requête peut être définie. Ainsi, un utilisateur qui ne maitrise pas le SQL ou le schéma de la base d'OSM peut s'appuyer uniquement sur le [Wiki d'OpenStreetMap (exemple des stations de métro)](https://wiki.openstreetmap.org/wiki/Tag:station%3Dsubway) pour définir de nouvelles couches. La majorité des 350 couches présentes aujourd'hui a été créée à l'aide de cette fonctionnalité.

L'utilisateur peut aussi éditer la clause de projection (`SELECT`), ci-dessous un exemple de sélection des métros dans la base de données OSM. Pour cette clause et en complément de ce qui a été défini par l'utilisateur, sont rajoutés d'autres champs `geom`, `osm_id`, `name` et `tags` contenant toutes les autres attributs sous forme de `hstore`.

![Requête SQL pour les métros](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_2/requete_sql_metro.png){: .img-center loading=lazy }

La clause source (`FROM`) dépend elle du type de géométrie défini lors de la création du jeu de données :

- Pour les géométrie de type `Point`, la sélection est réalisée sur l'union des tables `planet_osm_point` et les centroides issus de la table `planet_osm_polygon`.
- Pour les géométrie de type `Polyline`, seule la table `planet_osm_line` est considérée.
- Pour les géométrie de type `Polygon`, seule la table `planet_osm_polygon` est considérée.

Une fois les clauses définies, un assemblage de celles-ci permet de former la requête entière. Pour l' exemple des métros :

```sql type="Requête entière pour les métros"
SELECT
    A.osm_id,
    A.name,
    hstore_to_json(A.tags),
    ST_TRANSFORM(A.way,4326) as geom,
    tags->'wheelchair' = 'yes' as "has_wheelchair"
FROM planet_osm_point as A
WHERE ( A.railway='station' AND A.tags->'station'='subway' )
UNION ALL
SELECT
    B.osm_id,
    B.name,
    hstore_to_json(B.tags),
    ST_TRANSFORM(st_centroid(B.way),4326) as geom,
    tags->'wheelchair' = 'yes' as "has_wheelchair"
FROM planet_osm_polygon as B
WHERE ( B.railway='station' AND B.tags->'station'='subway' )
```

Pour valider la requête SQL, il suffit de vérifier que son exécution ne génère pas d'erreurs ! Pour rapidement connaitre la conformité de la requête, son exécution n'est pas effectuée sur toute la base de données, on limite son exécution à une seule entité par l'ajout de la contrainte `LIMIT 1` en fin de script. La requête de validation est donc :

```sql title="Validation d'une requête SQL"
SELECT
    A.osm_id,
    A.name,
    hstore_to_json(A.tags),
    ST_TRANSFORM(A.way,4326) as geom,
    tags->'wheelchair' = 'yes' as "has_wheelchair"
FROM planet_osm_point as A
WHERE ( A.railway='station' AND A.tags->'station'='subway' )
UNION ALL
SELECT
    B.osm_id,
    B.name,
    hstore_to_json(B.tags),
    ST_TRANSFORM(st_centroid(B.way),4326) as geom,
    tags->'wheelchair' = 'yes' as "has_wheelchair"
FROM planet_osm_polygon as B
WHERE ( B.railway='station' AND B.tags->'station'='subway' )
LIMIT 1
```

En l'absence d'erreurs, une vue matérialisée dans PostgreSQL est créée. Les données d'une vue sont toujours à jour, car elles sont directement dérivées des tables sources chaque fois qu'on y accède. Les vues matérialisées offrent un mécanisme puissant pour améliorer les performances des requêtes en pré-calculant et en stockant le jeu de résultats d'une requête sous forme de table physique

Pour OSM DATA, les requêtes peuvent faire appel à des milliers d'entités, résultant de plusieurs tables sous-jacentes, des conditions sur des champs indexés (ou non) et qui sont mises à jour une seule fois par jour. Pour toutes ces raisons, les vues matérialisées semblent être l'option la plus approriée pour notre solution.

A l'aide de la requête d'assemblage créée, la vue matérialisée est créée de la manière suivante :

```sql title="Création de la vue matérialisée"

CREATE MATERIALIZED VIEW {NOM_DE_LA_VUE} AS ({REQUETE_SQL_ENTIERE})
```

Pour information, l'utilisateur PostgreSQL exécutant la requête SQL détient uniquement des droits de création de tables ou de vues dans certains schémas de la base de données afin d'éviter les mauvaises surprises.

La couche est insérée en base de données ! :fireworks:

## Création d'un projet QGIS et de la symbologie associée au jeu de données

### Création d'un projet

La création d'un projet QGIS permet, à partir des données stockées dans la base de données PostgreSQL et de QGIS Server, de créer les flux WMS/WFS nécessaires à la visualisation des couches sur le web.

 **Pourquoi QGIS et QGIS Server ? Pourquoi ne pas avoir utilisé Mapserver ou Geoserver ? En deux mots : interopérabilité et efficacité**. QGIS :heart: dispose d'un moteur de style puissant et dont les capacités ne cessent de s'étoffer. Couplé à QGIS Server, la visualisation avec symbologie synchronisée *desktop*/*web* permet de créer rapidement et interactivement des symbologies, [Mathieu Rajerison](https://x.com/datagistips?s=21) a par exemple mis en place différents styles :

- Les lampadaires sont discriminés en fonction de leur type de mât, du nombre de sources lumineuses, de leurs intensités...

![Exemple Lampadaires](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_2/osm_lampadaires.png){: .img-center loading=lazy }

- Les fontaines à eau sont représentées dépendammant du caractère potable ou non de l'eau

![Exemple Fontaines](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_2/osm_data_style_fontaine.png){: .img-center loading=lazy }

Techniquement, c'est beau, très beau, trop beau... et vous n'êtes certainement pas amoureux de [Brad Pitt](https://www.marieclaire.fr/anne-escroquee-par-un-faux-brad-pitt-un-porte-parole-de-l-acteur-s-exprime-apres-l-arnaque-de-830-000-euros,1487356.asp) donc oui il y a quelques contraintes !

QGIS est avant tout un logiciel *desktop* donc en l'ouvrant , il initialise par défaut son environnement avec l'ensemble des dépendances qu'il juge nécessaires à une utilisation *desktop*. Compte tenu de notre utilisation, certaines contraintes sont soient superflues, soient limitantes en termes de performance, il est donc nécessaire de paramétrer les variables d'environnement afin de désactiver le lancement de certaines fonctionnalités (voir ci-dessous *Diffusion des flux OGC WMS/WFS)*).

Aussi, si on considère le lancement d'un projet ne contenant qu'une couche, l'initialisation peut être rapide, lorsque le projet dispose de 350 couches, c'est moins évident.

![Perceval](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_2/pas_faux.gif){: .img-center loading=lazy }

Pour ces raisons et sans avoir encore eu l'occasion de faire une analyse de l'outil [PerfSuite](https://github.com/qgis/QGIS-Server-PerfSuite/tree/master?tab=readme-ov-file), il a été décidé de répartir les couches entre plusieurs projets QGIS avec un maximum de 5 couches par projet. Sur OSM DATA, il y a actuellement 139 projets répertoriés :

```sh
# Décompte des projets QGIS d'OSM DATA
debian@osm_data:provider/qgis/project$ ls | grep '\.qgs$' | wc -l
139
# Liste des projets QGIS d'OSM DATA
debian@osm_data:provider/qgis/project$ ls | grep '\.qgs$'
projet_0.qgs
projet_1.qgs
projet_10.qgs
projet_100.qgs
...
```

Pour créer un projet QGIS relié à un jeu de données, il est donc nécessaire d'établir une nomenclature structurée dépendante de la contrainte de "5 jeux de données maximum par projet". Ainsi, pour lancer la création d'un projet associé à un nouveau jeu de données, voici le script utilisé :

```python title="Création d'un projet QGIS avec PyQGIS"
from qgis.core import QgsProject

# Nomenclature du projet QGIS
path_to_qgis_project = "projet" + "_" + str(int({nombre_total_de_couches_existantes} / 5)) + ".qgs"

# Création du projet QGIS
project = QgsProject()
project.read(path_to_qgis_project)
project.write()

```

Si le projet existe déja il est utilisé, et s'il n'existe pas, le projet est créé.

Une fois le projet QGIS sélectionné/créé, on ajoute le nouveau jeu de données avec pour source la table ou la vue matérialisée précédement créée :

```python title="Création d'une couche dans un projet QGIS"
from qgis.core import QgsProject, QgsDataSourceUri

# Création de la connexion à la base de données
uri = QgsDataSourceUri()
uri.setConnection(host, port, database, user, password)

# Création de la source de données avec le nom de la table ou la vue, le schéma, le champ de géométrie et celui de la clé primaire
uri.setDataSource({schema_de_la_table_ou_vue}, {table_ou_la_vue}, {champ_de_geometrie}, "", {cle_primaire})

# Création d'une couche de type vecteur avec la source définie
vector_layer = QgsVectorLayer(uri.uri(False), {layer_name}, "postgres")

# Validation d'accès à la table / vue et ajout de la couche au projet
if vector_layer.isValid():
    project.addMapLayer(vector_layer)

# Pour que la couche soit disponible en WFS, ajout de celle-ci dans la balise WFSLayers.
project.writeEntry("WFSLayers", "", [vector_layer.id()])
project.writeEntry("WMSAddWktGeometry", "", "true")

# Sauvegarde du projet
project.write()
```

Une fois le projet QGIS créé, les données peuvent déjà être diffusées sous forme de flux WMS/WFS avec QGIS Server ! Cependant, afin d'améliorer leur visualisation, le style doit être défini.

### Définition et application du style par l'utilisateur

Dans la fenêtre de définition d'une couche sur OSM DATA, un onglet Styles permet de définir une ou plusieurs symbologies pour chaque jeu de données :

![Fenêtre de définition d'une couche](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_2/osm_data_gestion_style.png){: .img-center loading=lazy }

Cette caractéristique multi-styles découle de la fonctionnalité déjà présente au sein de QGIS. Les différentes manières de définir un style dans OSM DATA permettent de faciliter l'administration des jeux de données depuis l'interface, deux options sont disponibles :

- A l'aide d'un fichier QML directement préparé à partir de QGIS

![Fonction d'import d'un fichier QML](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_2/ajout_style_qml.png){: .img-center loading=lazy }

- A l'aide du moteur de style intégré d'OSM DATA :
    - Sous la forme d'un icone ponctuel :  L'utilisateur fournit un icône (raster ou vecteur), un style est créé avec [`QgsSingleSymbolRenderer`](https://api.qgis.org/api/classQgsSingleSymbolRenderer.html) et PyQGIS pour l'appliquer au jeu de données. Le détail de l'implémentation est disponible sur le [GitHub](https://github.com/data-osm/geosm-backend/blob/master/provider/qgis/customStyle/point_icon_simple.py#L24) du projet.
    - Sous la forme d'un regroupement de point (*cluster*) : L'utilisateur fournit un icône, un style est créé avec [`QgsPointClusterRenderer`](https://api.qgis.org/api/classQgsPointClusterRenderer.html) pour l'appliquer au jeu de données. Le détail de l'implémentation est disponible sur le [GitHub](https://github.com/data-osm/geosm-backend/blob/master/provider/qgis/customStyle/point_icon_simple.py#L24) du projet.

![Fonction de création de style sous forme de *clusters*](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_2/ajout_style_cluster.png){: .img-center loading=lazy }

Au besoin, un dernier article peut compléter cette série pour expliciter davantage la création de styles avec PyQGIS.

## Diffusion des flux OGC WMS/WFS

Pour utiliser QGIS Server, rien de plus simple ! Il suffit d'enregistrer le projet QGIS dans un dossier et cet [article](https://geotribu.fr/articles/2010/2010-09-03_creer_diffuser_services_wms_avec_qgis/#test-du-service-wms) détaille les étapes d'exploitation de ce dossier pour créer les flux OGC.

Cependant, nous avons évoqué plus haut qu'à ce jour 139 projets QGIS sont présents. Une seule instance QGIS ne peut pas gérer l'ensemble de ces données de manière efficace. Pour cela, [py-qgis-server](https://github.com/3liz/py-qgis-server) est utilisé, il permet de définir plusieurs instances sur plusieurs *workers*, améliorant ainsi les performances. De plus certaines variables d'environnement QGIS sont directement exposées, voici celles qui sont actuellement activées sur OSM DATA lors de l'initialisation d'un projet :

- Ignorance des composeurs d'impression du projet
- Ignorance de la validité des couches

Après avoir exploré le mécanisme d’ingestion et de diffusion des données par OSM DATA, nous pouvons désormais nous intéresser à ses fonctionnalités récentes, notamment la visualisation des données en 3D. Ce sera l’objectif du prochain article.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
