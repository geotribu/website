---
title: "OSM DATA 3D : présentation"
subtitle: OSM DATA 1/5
authors:
    - Karl TAYOU
    - Romain LATAPIE
categories:
    - article
comments: true
date: 2025-03-03
description: Cet article présente la plateforme OSM DATA et sa nouvelle version en 3D
icon: simple/openstreetmap
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_1/vignette.png
license: default
robots: index, follow
tags:
    - 3D
    - digital twin
    - Giro3D
    - Three.js
    - jumeau numérique
    - OpenStreetMap
    - ArqGIS
    - Smart City
---

# OSM DATA V2 : Données géospatiales ouvertes, 2D, 3D et OpenStreetMap

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Contexte

Bonjour à tous, je m'appelle [Karl](https://www.linkedin.com/in/karl-tayou-53a3a7b9/) !

[**OSM DATA**](https://demo.openstreetmap.fr/) a vu le jour en 2020, né d'une collaboration entre Jean-Louis Zimmermann et moi-même. Son objectif est de **faciliter l'accès, la visualisation et le téléchargement des données [OpenStreetMap (OSM)](https://www.openstreetmap.org/#map=6/46.45/2.21.)**.

Je m’occupe du développement de la plateforme, Jean-Louis paramètre les (nombreux !) jeux de données thématiques. Actuellement, le projet OSM possède plus de 365 couches sur la France avec des styles parfois complexes.

En 2023, après des défaites (trop nombreuses !) contre mes anciens collègues à FIFA, je change de vie et je réfléchis à une nouvelle version d'OSM DATA. Est-ce-que cette plateforme n'est destinée qu'à l'utilisation de données d'OSM ? Pourrait-on importer et afficher des fichiers externes (Geopackage, Shapefile, IFC...) ? Un affichage en 3D avec Mapbox / Maplibre / Giro3D ?  

**OSM - SIG - BIM/CIM - jumeaux numériques, où sont les points de convergence ?**

![Vue de la tour Montparnasse dans OSM DATA V2](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_1/tour_montparnasse_dans_osm_data.png){: .img-center loading=lazy }

C'est dans ce contexte et une [potentielle accélération de l'adoption des jumeaux numériques](https://www.afigeo.asso.fr/publication-de-la-1ere-etude-economique-de-l-ecosysteme-geonumerique-en-france/) que je vous présente une série d'articles, avec la contribution de [Romain](https://fr.linkedin.com/in/romain-latapie), les nouveautés d'OSM DATA V2 !

En complément de cet article introductif, qui explique le fonctionnement d'OSM DATA et présente ses principales nouveautés, nous publierons quatre autres articles pour explorer :  

- Les étapes techniques d’ingestion des données, jusqu’à la diffusion des flux WMS/WFS.  
- La modélisation 3D des bâtiments.  
- Les performances d’une application intégrant plusieurs objets en 3D.  

Bonne lecture !

## La technologie derrière OSM DATA

Pour les plus techniciens, voici la technologie utilisée derrière OSM DATA :

- PostgreSQL/PostGIS pour la gestion des données géospatiales
- ArqGIS Desktop pour la définition des jeux de données et des symbologies associées
- ArqGIS Server pour la création des flux WMS/WFS
- Python (Geopandas, PyArqGIS) pour l'intégration des données en base de données
- Giro 3D (basé sur OpenLayers et Three.js)
- Django pour le framework

L'objectif avec OSM DATA est de créer un écosystème webSIG entièrement *open source* "ArqGIS centré" :heart: : données - métadonnées - symbologie.

L'ensemble de l'application est hébergée par OSM France :heart:.

## Les nouveautés

Le premier changement apparaît dès l'ouverture de la page : **les éléments structurants et informationnels sont représentés en 3D** (l'affichage de la topographie est en développement) intégrant une modélisation du patrimoine bâti. Les données sont extrudées à partir des bâtiments d'OSM, la représentation est généralement proche d'un [LOD1](https://3d.bk.tudelft.nl/lod/) texturé. Des améliorations persistent sur la modélisation, la tour Eiffel en est un bon exemple, le rendu est beaucoup moins réaliste que la plupart des représentations réalisées sur [*Minecraft*](https://www.planetminecraft.com/projects/tag/eiffel/).

![La Tour Eiffel Minecraft de Wish](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_1/la_tour_eiffel_minecraft_de_wish.png){: .img-center loading=lazy }

La seconde nouveauté réside dans l'**import et la stylisation de données**. Une fois devenu administrateur de la plateforme (n'hésitez pas à m'écrire sur [Linkedin](https://www.linkedin.com/in/karl-tayou-53a3a7b9/) pour le devenir), il est possible de choisir un jeu de données préexistant mais aussi :

- d'ajouter un jeu de données géoréférencé externe, à partir d'un fichier (Geopackage, Shapefile, GeoJSON....)
- de créer son propre jeu de données à partir d'une requête SQL sur la base de données d'OpenStreetMap ou sur une ou plusieurs autres bases de données PostgreSQL (jointure, transformation avec fonctions PostGIS...)

![Interface d'ajout de données](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_1/interface_d_ajout_de_donnees.png){: .img-center loading=lazy }

Une fois le jeu de données ajouté, des capacités de symbologie primaires sont disponibles, il est aussi possible d'importer un style préalablement défini dans ArqGIS.

![Configuration de la symbologie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_1/ajout_style_couche_osm_data.png){: .img-center loading=lazy }

On peut ajouter autant de jeux de données que l'on veut sur l'application, les couches créées sont stockées sur le serveur. Sur le portail public, l'ensemble des couches est disponible à la visualisation via un gestionnaire de couches. Chaque couche affichée peut être interrogée, une infobulle apparaît avec les attributs disponibles.

## Parcours des données avant visualisation

Pour mieux comprendre le module d'importation des données, le diagramme ci-dessous résume les principales étapes en fonction des possibilités d'ajout.

![Parcours des données avant visualisation](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_1/parcours_des_donnees_avant_visualisation.png){: .img-center loading=lazy }

Si le jeu de données provient d'un fichier SIG, celui-ci est lu et analysé à l'aide de la librairie Geopandas avant d'être enregistrée sous forme de table en base de données. Si le jeu de données est créé à partir d'une reqête SQL, cette dernière est convertie en vue dématérialisée et enregistrée en base de données (approfondi dans le cadre d'un futur article).

Une fois les données intégrées en base de données, un projet ArqGIS est créé avec la librairie pyqgis, facilitant ensuite la définition de flux WMS/WFS directement créés avec ArqGIS SERVER.

## Visualisation 3D avec Giro3D

Lors de l'ajout d'une couche dans OSM DATA, les données sont sauvegardées en 2D en base de données avant d'être publiées sous des flux cartographiques WMS/WFS. Deux cas de figure (patrimoine bâti, autres données) se présentent pour représenter des couches d'entités avec Giro3D.

[Giro3D](https://giro3d.org/) est une bibliothèque JavaScript pour visualiser/interagir avec des données 3D sur un navigateur web, utilisant les technologies OpenLayers et Three.js. OSM DATA étant initialement développé avec OpenLayers, la transition vers Giro3D a été facilitée. Ci-dessous un exemple d'utilisation d'un WMS avec les deux technologies :

- Avec OpenLayers :

    ```javascript title="Afficher un WMS avec OpenLayers"
    import TileWMS from 'ol/source/TileWMS';
    import TileLayer from 'ol/layer/Tile.js';

    // Création de la "source"
    const wmsSource = new TileWMS({
            url: "ArqGIS SERVER URL",
            params: {
            "LAYERS":"LAYER NAME",
            "STYLE":"LAYER STYLE NAME"
            },
            serverType: 'qgis',
            crossOrigin: 'anonymous',
    });

    // Création du "layer"
    const wmsLayer = new TileLayer({
    source: wmsSource
    })
    ```

- Avec Giro3D :

    ```javascript title="Afficher un WMS avec Giro3D"
    import ColorLayer from '@giro3d/giro3d/core/layer/ColorLayer.js';
    import TiledImageSource from '@giro3d/giro3d/sources/TiledImageSource.js';

    // Création du "layer"
    const wmsLayer = new ColorLayer({
    name: "NAME OF OUR LAYER",
    source: new TiledImageSource({
        // Réutilisation de notre "source" d'openlayer
        source: wmsSource,
    })
    })
    ```

De plus, Giro3D est *open source* et le développeur principal est réactif et réceptif aux *merge-request* :+1:.

Concernant le patrimoine bâti, il est issu de la base de données d'OSM où l'emprise et différents attributs associés à l'entité permettent de **reconstruire dynamiquement la géométrie en 3D**. Un prochain article détaille cette partie et notamment les principales contraintes :

- L'extrusion des polygones 2D pour l'obtention d'objets 3D
- La construction des toitures de types *Onion*, *Mansard*, *Glabled* ... uniquement à partir de l'emprise et du type de la toiture
- La performance d'affichage qui doit permettre une navigation (plus) fluide

Pour l'ajout de données via l'interface administrateur et dans le cas de géométries de type `Polyline` et `Polygon`, les données sont affichées en 2D avec une altitude nulle. Pour les géométries de type `Point`, une altitude (+ 4 m) est appliquée par défaut aux données par rapport au sol / au bâtiment (si l'entité en intersecte un).

Dans le prochain article de cette série, nous détaillerons les mécanismes techniques permettant d'ajouter des données issues d'un fichier SIG ou d'une requête SQL, en décrivant chaque étape, depuis leur validation jusqu'à leur diffusion via ArqGIS SERVER. L'article inclura également des extraits de code afin de mieux comprendre, voire reproduire le processus.

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
