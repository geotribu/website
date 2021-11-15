---
title: "Le traitement des données OSM chez Geovelo"
authors:
  - Samuel Deschamps-Berger
categories:
  - article
date: 2021-11-20 08:00
description: "Etat des lieux des traitements OSM de geovelo"
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_en_relief_des_ecrins/0-head.jpg"
license: default
tags:
  - osm
  - geovelo
---

# Le traitement des données OSM chez Geovelo

:calendar: Date de publication initiale : 20 novembre 2021

## Présentation
Geovelo est une application gratuite qui permet de **trouver facilement l'itinéraire à vélo le plus adapté** selon plusieurs critères. Plusieurs options sont proposées, de la plus rapide à la plus sécurisée. En complément, l'application intègre aussi d'autres fonctionnalités telles que le **suivi de ses statistiques**, l'accès à des **itinéraires touristiques** ou encore un **outil de contributions cartographiques**.

Geovelo accompagne les collectivités dans le but de **favoriser la pratique du vélo**. Cela passe par une meilleure compréhension de l'utilisation du réseau cyclable (via des statistiques anonymisées issues des utilisateurs), et des axes d'amélioration pour le développer.

## Geovelo & OpenStreetMap
Les données cyclables d’OSM sont l’un des fondements de l’activité même de Geovelo. Elles alimentent non seulement nos calculateurs d’itinéraires pour construire le réseau cyclable, mais servent également de référentiel pour de multiples traitements, des statistiques d’aménagements jusqu’aux informations de déplacements.
La validité, la qualité, la cohérence et la complétude de ces données sont donc des rouages essentiels de la valeur ajoutée des produits Geovelo.  


----


### Enrichissement des données OSM

Pour s’assurer d’avoir les meilleures données cyclables possibles, Geovelo participe quotidiennement à l’amélioration des données. Nous sommes 4 (1 à temps plein et 3 “connaisseurs”) à commiter régulièrement des changements, qui sont basés sur :  

![Suivi OSM chez Geovelo](https://wpformation.com/wp-content/uploads/2014/03/todo1.jpg "Suivi OSM chez Geovelo"){: loading=lazy align=right}

- des **enquêtes sur le terrain**, avec import des images sur Mapillary,
- des bases Open Data, ou documents assimilés, fournis par les collectivités partenaires pour intégration,
- des **retours utilisateurs**, via notre système intégré de contributions carto sur les apps,  
- des indices remontés par des erreurs de calculs d’itinéraires.

### Processus de traitement des contributions
Geovelo intègre un outil de contribution à son site web et ses applications, permettant aux utilisateurs de contribuer sur 8 thématiques différentes:

> Erreur de cartographie, Aménagement Cyclable manquant, parking Vélo Manquant, A faire à voir, Points noirs, Travaux, Route bloquée, Nid de Poule

Seules les catégories “Erreur de cartographie”, “Aménagement Cyclable manquant”, et “Parking vélo manquant”, créent une note sur OpenStreetMap et entraînent un traitement de notre équipe de cartographes. L’ensemble des commentaires effectués sur une note géovélo lié à une note OpenStreetMap et l’ensemble des commentaires effectués sur cette note sont synchronisés de sorte à pouvoir suivre indépendamment du côté de Geovelo ou d’OpenStreetMap ces signalements. Cela permet aussi une totale transparence avec la communauté OpenStreetMap.

*L’outil de signalement interne à l’application incite l’utilisateur à nous joindre une photo et une description du problème.*

Les contributions sont ensuite traitées manuellement par nos soins :
- Si les informations sont pertinentes, les données OpenStreetMap sont modifiées.
- Si nous manquons d’informations, nous demandons des détails au contributeur initial. Tout les commentaire sur note, qu’il est été effectué coté OpenStreetMap ou coté Geovelo, sont transmis par mail au créateur de la note.
  - Si l’usager nous répond uniquement par mail, nous recevons ses précisions et nous traitons la demande, mais sa réponse ne s’affiche pas sur la note.
  - Si l’usager nous répond en utilisant amenagements-cyclables.fr, sa réponse s'affiche sur la note OpenStreetMap
- Si la note comprend des informations personnelles ou semble trop fantaisiste, nous supprimons la contribution.

Nous modifions alors les données OpenStreetMap, et clôturons la contribution sur amenagements-cyclables.fr, clôturant ainsi la note OpenStreetMap en même temps.

De nombreuses notes restent ouvertes (la plupart en attente de précisions d’un contributeur).
Ces notes sont parfois traitées par un contributeur local, qui aura connaissance du sujet traité.
>Sans réponse ou retour de la part de l’utilisateur initial, nous clôturons la note 2 mois après sa création.


### Vérification de la qualité de nos imports
Notre base de données OpenStreetMap “monde” est maintenue et mise à jour quotidiennement. A partir de cette base nous créons des extraits spécialisés en fonction des usages. Ils possèdent donc leurs propres spécificités, aussi bien dans la couverture géographique que dans le filtrage des données OpenStreetMap et des champs calculés.
Cela nous permet d’optimiser la taille et les performances de chaque base de données pour un usage précis. (peut être dans un 2ème article ? )

Nous utilisons les données OpenStreetMap pour différents usages, par exemple :
- Calculateur d’itinéraires,
- Calculs de statistiques d’aménagements cyclables, disponibles sur aménagements-cyclables.fr,
- Extraction dans des formats standardisés ou personnalisés de la données OpenStreetMap. Nous publions également l’extraction des aménagements cyclables de france métropolitaine pour la [Base Nationale des Aménagements Cyclables (BNAC)](https://www.data.gouv.fr/fr/datasets/amenagements-cyclables-france-metropolitaine/) sur data.gouv.fr
- Serveur de tuiles raster et vecteur


----
## Nos outils pratiques
Pour l'intégration et le traitement des notes :

- **QGIS** (*une évidence...*) avec le plug-in QuickOSM (utilisation du remote controler vers JOSM, merci [3Liz](https://www.3liz.com/en/news/quickosm-2-0.html) :heart_eyes:)
- **JOSM**, notamment avec une couche de style aux petits oignons signée [CartoCité](https://github.com/Cartocite/MapCSS-JOSM-Bicycle)

Pour les traitements de réutilisation, on est sur du classique libre :
>Postgis, Osmosis, Osm2pgsql, GDAL

---

Bonus ! La station de travail de [Simon](https://twitter.com/c_geovelo), notre cartographe:  
![station_simon](https://wpformation.com/wp-content/uploads/2014/03/todo1.jpg "La station de travail du cartographe"){: loading=lazy align=right}

## Auteur

--8<-- "content/team/sdesb.md"

<!-- Intègre le glossaire centralisé -->
--8<-- "content/toc_nav_ignored/snippets/glossaire.md"
