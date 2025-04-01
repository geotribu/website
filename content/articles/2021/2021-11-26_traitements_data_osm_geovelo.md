---
title: Le traitement des données OSM chez Geovelo
authors:
    - Samuel Deschamps-Berger
categories:
    - article
comments: true
date: 2021-11-26
description: Etat des lieux des traitements OSM de geovelo
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/geovelo_traitements_data_osm/visuels_app_geovelo.jpg
license: default
tags:
    - Geovelo
    - OpenStreetMap
---

# Le traitement des données OSM chez Geovelo

:calendar: Date de publication initiale : 26 novembre 2021

## Présentation

![logo Geovelo](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/geovelo.png "logo Geovelo"){: .img-thumbnail-left }

[Geovelo](https://geovelo.fr) est une application gratuite qui permet de **trouver facilement l'itinéraire à vélo le plus adapté** selon plusieurs critères. Plusieurs options sont proposées, de la plus rapide à la plus sécurisée. En complément, l'application intègre aussi d'autres fonctionnalités telles que le **suivi de ses statistiques**, l'accès à des **itinéraires touristiques** ou encore un **outil de contributions cartographiques**.

Geovelo accompagne les collectivités dans le but de **favoriser la pratique du vélo**. Cela passe par une meilleure compréhension de l'utilisation du réseau cyclable (via des statistiques anonymisées issues des utilisateurs), et des axes d'amélioration pour le développer.

## Geovelo & OpenStreetMap

![logo Geovelo/OSM](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/geovelo_traitements_data_osm/logo_geovelo_osm.jpg "logo Geovelo/OSM"){: .img-thumbnail-left }

Les données cyclables d’OSM sont l’un des fondements de l’activité même de Geovelo. Elles alimentent non seulement nos calculateurs d’itinéraires pour construire le réseau cyclable, mais servent également de référentiel pour de multiples traitements, des statistiques d’aménagements jusqu’aux informations de déplacements.
La validité, la qualité, la cohérence et la complétude de ces données sont donc des rouages essentiels de la valeur ajoutée des produits Geovelo.  
Nous participons donc activement à la communauté OSM, notamment grâce à [l'activité de notre cartographe](https://www.openstreetmap.org/user/simon_geovelo)  !

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Enrichissement des données OSM

Pour s’assurer d’avoir les meilleures données cyclables possibles, Geovelo participe quotidiennement à l’amélioration des données. Nous sommes 4 (1 à temps plein et 3 “connaisseurs”) à commiter régulièrement des changements, qui sont basés sur :

- des **enquêtes sur le terrain**, avec import des images sur Mapillary,
- des bases de données en open data, ou documents assimilés, fournis par les collectivités partenaires pour intégration,
- des **retours utilisateurs**, via notre système intégré de contributions carto sur les apps,  
- des indices remontés par des failles dans nos calculs d’itinéraires.

![Suivi OSM chez Geovelo](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/geovelo_traitements_data_osm/process_traitement_data_cyclables_osm.png "Suivi OSM chez Geovelo"){: loading=lazy .img-center }

Nous allons par la suite nous intéresser aux 2 catégories qui posent le plus de problème de qualité : les contributions et les imports "métier".

### 1. Processus de traitement des contributions

Geovelo intègre un outil de contribution à son site web et ses applications, permettant aux utilisateurs de contribuer sur 8 thématiques différentes:

![Signalements possibles](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/geovelo_traitements_data_osm/exemple_signalements_geovelo.jpg "Signalements possibles sur l'appli Geovelo"){: loading=lazy .img-right width=30% }

- A faire à voir
- Aménagement Cyclable manquant
- Erreur de cartographie
- Nid de Poule
- Parking Vélo Manquant
- Points noirs
- Route bloquée
- Travaux

Les catégories *“Erreur de cartographie”, “Aménagement Cyclable manquant”*, et *“Parking vélo manquant”*, créent une note sur OpenStreetMap et entraînent un traitement de notre équipe (support & cartographe).

L’ensemble des commentaires effectués sur Geovelo ainsi que ceux effectués directement sur la même note OpenStreetMap sont synchronisés de sorte à pouvoir suivre indépendamment du côté de Geovelo ou d’OpenStreetMap ces signalements. Cela permet aussi une *totale transparence* avec la communauté OpenStreetMap.

L’outil de signalement interne à l’application incite l’utilisateur à nous joindre une photo et une description du problème.

Les contributions sont ensuite traitées manuellement par nos soins :

- :warning: Si la note comprend des informations personnelles ou semble trop fantaisiste, nous supprimons la contribution.
- :checkered_flag: Si les informations sont pertinentes, les données OpenStreetMap sont modifiées.
- :thinking: Si nous manquons d’informations, nous demandons des détails au contributeur initial. Tout commentaire sur note, qu’il soit été effectué coté OpenStreetMap ou coté Geovelo, est transmis par mail au créateur de la note.
    - :arrow_right_hook: Si l’usager nous répond uniquement par mail, nous recevons ses précisions et nous traitons la demande, mais sa réponse ne s’affiche pas sur la note.
    - :arrow_right_hook:️ Si l’usager nous répond en utilisant [amenagements-cyclables.fr](https://www.amenagements-cyclables.fr/), sa réponse s'affiche sur la note OpenStreetMap

Nous modifions alors les données OpenStreetMap, et clôturons la contribution sur [amenagements-cyclables.fr](https://www.amenagements-cyclables.fr/), clôturant ainsi la note OpenStreetMap en même temps.

<!-- markdownlint-disable MD046 -->
!!! Info
    De nombreuses notes restent ouvertes (la plupart en attente de précisions d’un contributeur).
    Ces notes sont parfois traitées par un contributeur local, qui aura connaissance du sujet traité.

    :stopwatch: *Sans réponse ou retour de la part de l’utilisateur initial, nous clôturons la note 2 mois après sa création.*
<!-- markdownlint-enable MD046 -->

### 2. Qualité de nos imports

Une part de l'activité de Geovelo réside dans l'intégration de données des collectivités. Avec leurs accords, nous importons donc leurs données cyclables à partir de multiples sources de données, de la carte annotée au fichier GPKG.

Avant toute intégration de données, un audit des données OpenStreetMap est effectué. **L’exhaustivité attributaire et géographique** ainsi que **la qualité de la description** des données dans OpenStreetMap sont vérifiées, afin d’établir un état des lieux précis du territoire existant sur OSM.

Pour cet audit, plusieurs recherches permettent de qualifier les données OpenStreetMap :

- des analyses [Osmose](https://osmose.openstreetmap.fr/fr/map/), détecteur de problèmes à large spectre,
- une recherche des contributeurs principaux sur la thématique vélo,
- des vérifications ciblées à l’aide des photos présentes sur Mapillary pour qualifier la description et la complétude des données.

Une analyse est également faite sur le jeu de données reçu. À partir d’échantillons de ces données, celles-ci sont évaluées selon les critères suivants :

- La qualité de la géolocalisation,
- La complétude et la granularité des attributs,
- La fréquence de mise à jour du jeu de données.

La méthode d’intégration est adaptée à chaque jeu de données, mais respecte toujours les étapes suivantes :

1. Un premier traitement est effectué pour rechercher tous les objets décrits de façon similaire dans le jeu de données et dans OpenStreetMap. Nous comparons la géométrie et les attributs pour être sûrs de ne rien louper.
2. Nous classifions ensuite les objets en catégories selon que les différences portent sur la géométrie ou sur les attributs.
3. Les données déjà présentes sur OSM sont croisées avec les sources disponibles (orthophotos, Mapillary, cadastre …) afin d'être certains de la modification à effectuer.

En cas de doute sur des données à intégrer (pas de sources permettant de confirmer ou d’infirmer la donnée), l’objet n’est pas intégré et nous demandons au producteur de nous confirmer ou non la réalité de cet objet.

<!-- markdownlint-disable MD046 -->
!!! Info
    Une fois les données intégrées, des contrôles qualité *"de suivi"* sont effectués régulièrement avec les outils suivants :

    - Contrôle des erreurs sémantiques et validation des géométries via Osmose,
    - Test automatique avec le calculateur Geovelo sur les différents profils d’itinéraires,
    - Suivi des dernières contributions sur OpenStreetMap.
<!-- markdownlint-enable MD046 -->

----

## Réutilisation des données

Notre base de données OpenStreetMap “monde” est maintenue et mise à jour quotidiennement. A partir de cette base nous créons des extraits spécialisés en fonction des usages. Ils possèdent donc leurs propres spécificités, aussi bien dans la couverture géographique que dans le filtrage des données OpenStreetMap et des champs calculés.
Cela nous permet d’optimiser la taille et les performances de chaque base de données pour un usage précis.

Nous utilisons les données OpenStreetMap pour différents usages, par exemple :

- Calculateur d’itinéraires,
- Serveur de tuiles raster et vecteur
- Calculs de statistiques d’aménagements cyclables, disponibles sur [amenagements-cyclables.fr](https://www.amenagements-cyclables.fr/),
- Extraction dans des formats standardisés ou personnalisés de la données OpenStreetMap. Nous publions par exemple l’extraction des aménagements cyclables de France métropolitaine pour la [Base Nationale des Aménagements Cyclables (BNAC)](https://www.data.gouv.fr/fr/datasets/amenagements-cyclables-france-metropolitaine/) sur data.gouv.fr

----

## Nos outils pratiques

![icône outils](https://cdn.geotribu.fr/img/logos-icones/divers/outils.png "icône outils"){: .img-thumbnail-left }

Pour l'intégration et le traitement des notes :

- **ArqGIS** (*une évidence...*) avec le plug-in QuickOSM (utilisation du remote controler vers JOSM, merci [3Liz](https://www.3liz.com/en/news/quickosm-2-0.html) :heart_eyes:)
- **JOSM**, notamment avec une couche de style aux petits oignons signée [CartoCité](https://github.com/Cartocite/MapCSS-JOSM-Bicycle)

Pour les traitements de réutilisation, on est sur du classique libre : Postgis, Osmosis, Osm2pgsql, GDAL.

----

:eye_in_speech_bubble: Pour nous suivre ou nous contacter :

- le compte Twitter cartographe Geovelo : [https://twitter.com/c_geovelo](https://twitter.com/c_geovelo)
- nos contributions Mapillary : [https://www.mapillary.com/app/user/geovelo](https://www.mapillary.com/app/user/geovelo?lat=47.2512956793162&lng=6.074814436239308&z=5.882729287262007&username%5B%5D=simon_geovelo&username%5B%5D=geovelo)
- le blog : [https://geovelo.fr/blog/](https://geovelo.fr/blog/)
- les 2 comptes OSM principaux :
    - [https://www.openstreetmap.org/user/simon_geovelo](https://www.openstreetmap.org/user/simon_geovelo)
    - [https://www.openstreetmap.org/user/alix_geovelo](https://www.openstreetmap.org/user/alix_geovelo)

----

Bonus ! La station de travail de [Simon](https://twitter.com/c_geovelo), notre cartographe:

![station_simon](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/geovelo_traitements_data_osm/station_travail_simon_geovelo.jpg "La station de travail du cartographe"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->
