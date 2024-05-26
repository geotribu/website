---
title: "OpenStreetMap ce n'est pas (qu') une carte"
authors:
    - Arnaud VANDECASTEELE
categories:
    - article
comments: true
date: 2015-01-11
description: "Lorsque je discute d'OpenStreetMap, pour beaucoup c'est une carte, rien de plus. Alors qu'en réalité OSM est un projet collaboratif dont le coeur est la base de données géographiques. La carte résultante n’étant qu'un des nombreux dérivés de cette base."
icon: material/database-marker
tags:
    - OpenStreetMap
---

# OpenStreetMap ce n'est pas (qu') une carte

:calendar: Date de publication initiale : 11 janvier 2015

![Logo Openstreetmap](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/Openstreetmap.png "Openstreetmap"){: .img-thumbnail-left }

Lorsque je discute d'OpenStreetMap, je me rends souvent compte qu'il y a une méconnaissance de l'étendue réelle de ce projet. En effet, pour beaucoup de personnes, OpenStreetMap (OSM) se résume à une carte. Il est vrai que c'est souvent la première illustration concrète de ce projet !

Mais en réalité OSM est un projet collaboratif dont le coeur est la base de données géographiques. La carte résultante n’étant qu'un des nombreux dérivés de cette base.

C'est pourquoi l'objectif de ce billet est de clarifier l'architecture générale d'OSM et d'en identifier les principaux composants.

![OSM - Structural Iceberg](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/Structural-Iceberg.png "OSM - Structural Iceberg"){: .img-center loading=lazy }

----

## Ceci n'est pas une pipe

Quel titre étrange pour commencer ce billet non ? En réalité, celui-ci traduit parfaitement ce que je souhaite vous exposer. En effet, quand au début des années 80 René Magritte peint son fameux tableau intitulé "La Trahison des images", il souhaite montrer qu'une image, même peinte de la manière la plus réaliste qui soit, reste une image.

![René Magritte - La Trahison des images](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/margritte.jpg "René Magritte - La Trahison des images"){: .img-center loading=lazy }

De la même manière, la carte d'OpenStreetMap que (presque) tout le monde connait n'est pas OpenStreetMap. Ce n'est en réalité qu'un fragment de ce projet. Un des fragments les plus visibles certes, mais un fragment tout de même !

## Architecture d'OpenStreetMap

Comme je vous le disais en introduction, OpenStreetMap c'est un système complet tourné vers et pour la contribution de données géographiques. Ce système peut être divisé en 5 grands composants (figure ci-dessous) :

- En premier lieu, les données (qui apparaissent en gris) qui vont alimenter la base de données ou aider à la digitalisation (ex fond ortho de Bing Maps)
- Viennent ensuite les fonctionnalités d'édition. La plupart du temps cela se fait via des logiciels dédiés (ex JOSM) qui offrent une interface pour ma création, la modification ou la suppression des données OSM. Dépendamment des fonctionnalités de ces logiciels, il peut être possible d'afficher des orthophographies (ex Bing Maps) ou encore des données dans divers formats (ex Shapefile). Pour l'import de gros volumes de données, ces logiciels d'édition peuvent ne pas être les plus adaptés. C'est pourquoi que des bibliothèques existent dans différents langages (python, java, etc.) permettant de dialoguer directement avec l'API d'OSM.
- Une fois les données correctement formatées, il est alors temps de les insérer en base (en vert sur le schéma). De cette base de données sont régulièrement extrait [les différentiels](https://wiki.openstreetmap.org/wiki/Planet.osm/diffs) (minutes, hours, etc.) permettant de mettre à jour les autres réplication de la base OSM. Ces données sont ensuite utilisées par de nombreuses applications pour proposer de nouveaux services. C'est le cas notamment de [Nominatim](https://nominatim.openstreetmap.org/) (outil de recherche) ou encore [OSRM](http://map.project-osrm.org/) (calcul d'itinéraires).
- Ces données sont également utilisées les cartes, où plutôt devrais-je dire les tuiles, que vous voyez sur les sites utilisant OSM. Il n'y a pas une seule carte mais autant de cartes qu'il existe de style. Ainsi, ne soyez pas surpris si la carte d'[OpenMapQuest](http://open.mapquest.co.uk/) ne ressemble en rien à celle par défaut d'[OSM](https://www.openstreetmap.org/).
- Enfin, tout en haut, ce sont les logiciels et bibliothèque permettant de visualiser les tuiles dont nous parlions dans le paragraphe précédent.

![Architecture d'OpenStreetMap](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/OSM_Components.png "Architecture d'OpenStreetMap"){: .img-center loading=lazy }

## En conclusion

J'espère avoir réussi à clarifier ce qu'est OpenStreetMap sans pour autant trop vous embrouiller. Mais c'est un projet complexe dont l'étendue ne cesse de s'agrandir. Ne voir que sa simple composante cartographique est très réducteur et cela serait oublier toutes les autres fonctionnalités !

<!-- geotribu:authors-block -->
