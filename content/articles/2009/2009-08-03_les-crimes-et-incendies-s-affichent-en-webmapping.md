---
title: "Les crimes et incendies s'affichent en WebMapping"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-08-03
description: "Les crimes et incendies s'affichent en WebMapping"
tags:
    - webmapping
---

# Les crimes et incendies s'affichent en WebMapping

:calendar: Date de publication initiale : 03 août 2009

![icône globe world](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "icône globe générique"){: .img-thumbnail-left }

J'ai récemment découvert deux applications cartographiques qui m'ont interpellées tant par leur contenu que par le choix de leur architecture. Ainsi, au-delà de la découverte de chacune d'entre elles, j'effectuerai un rapide comparatif en privilégiant une approche technique..

La première, [cartocrime](http://www.cartocrime.net/webigeoagsdb/index.jsf), fait suite à l'initiative de l'Observatoire National de la Délinquance de démocratiser l'accès aux statistiques de délinquance. D'abord sous forme de bulletins mensuels, leur stratégie de communication s'est progressivement orientée vers une représentation cartographique des données.

Néanmoins, je dois avouer avoir été déçu par la qualité de l'application proposée. En effet, l'interface mériterait largement un coup de jeune! J'ai l'impression de repartir trois ou quatre ans en arrières lors des balbutiements du webmapping.

Côté architecture, nous sommes là aussi sur des choix qui mériteraient d'être discutés. La partie moteur est constituée du trio TomCat/Apache/ArcGis Server, la partie base de données étant assurée par postgres. Étant un fervent défenseur des technologies OpenSource, j'aurais pour ma part choisi une architecture beaucoup plus souple. Pourquoi ne pas remplacer ArcGis Server par GeoServer (complémentarité avec tomCat - techno Java) et quitte à utiliser postgres autant y coupler sa cartouche spatiale PostGis.

Dernière petite remarque, même si je ne suis pas expert en sémiologie graphique, il me semble néanmoins que la représentation cartographique de valeurs quantitatives se fait par symboles proportionnels et non par plages de couleur.

![Cartocrime](https://cdn.geotribu.fr/img/Blog/divers/cartocrime.png "Cartocrime"){: .img-center loading=lazy }

Passons maintenant à la seconde application réalisée par l'European Forest Fire Information System ([EFFIS](http://effis.jrc.ec.europa.eu/)). Celle-ci a pour objectif de fournir des informations actualisées (quotidiennement) et fiables de la situation des feux de végétation en Europe.

Grâce aux icônes, immédiatement reconnaissables, il est facile de deviner que derrière l'interface cartographique se cache [OpenLayers](https://openlayers.org/). De plus, au regard des URLs qui transitent dans mon navigateur, on reste sur des standards OGC avec des tuiles servies au format WMS. Enfin, des rares informations que j'ai pu trouver, il semble que l'architecture est constituée de MapServer comme serveur cartographique et Oracle comme base de données.

Inutile de vous préciser que l'éventail des fonctionnalités est beaucoup plus riche que sur cartocrime. Il en est de même pour la facilité et la compréhension de l'accès à l'information. D'ailleurs, le mode de représentation des données est cette fois adéquate puisque les valeurs sont d'ordre qualitatif !

![Feu](https://cdn.geotribu.fr/img/Blog/divers/feu.png "Feu"){: .img-center loading=lazy }

Au final, la découverte de ces deux applications à quelques jours d'intervalles m'amène à réfléchir sur les capacités réelles des éditeurs de logiciels propriétaires à pouvoir évoluer suffisamment rapidement dans un domaine en mouvement continuel. Le choix de cartocrime de privilégier une solution aussi lourde est discutable, peut-être que la facilité de gestion et d'administration a été un facteur important dans leur décision. Néanmoins, le comparatif avec ce que propose l'EFFIS est sans appel ! Il est clair que cette dernière est nettement plus agréable.

----

<!-- geotribu:authors-block -->
