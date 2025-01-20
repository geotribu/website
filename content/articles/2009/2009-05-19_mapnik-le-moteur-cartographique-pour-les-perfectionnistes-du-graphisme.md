---
title: "Mapnik, le moteur cartographique pour les perfectionnistes du graphisme"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-05-19
description: "Mapnik, le moteur cartographique pour les perfectionnistes du graphisme"
tags:
    - Mapnik
    - TileCache
---

# Mapnik, le moteur cartographique pour les perfectionnistes du graphisme

:calendar: Date de publication initiale : 19 mai 2009

![logo Mapnik](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/mapnik.png "logo Mapnik"){: .img-thumbnail-left }

J'avoue avoir été longtemps frustré par la piètre qualité des images générées par [MapServer](http://mapserver.org/). Difficile de laisser parler sa créativité cartographique quand le rendu n'est pas à la hauteur de ses espérances. C'est pourquoi je me suis récemment tourné vers [Mapnik](http://mapnik.org/). Ce dernier doit la qualité de ses graphiques à l'utilisation de la librairie [AGG](http://antigrain.com/). Même si Mapnik a été le premier à tirer partie des potentialités de cette librairie, celle-ci est dorénavant implémentée par MapServer et [MapGuide](http://mapguide.osgeo.org/).

Les sources de Mapnik étant disponibles dans les dépôts Fedora et Ubuntu je n'ai rencontré aucune difficulté à l'installation. Néanmoins, une fois cette étape réalisée, j'avoue avoir passé quelques heures sur les [tutoriaux](http://mapnik.org/documentation/) avant de comprendre sa logique de fonctionnement. Vous pouvez en effet l'utiliser à partir d'un [script python](http://trac.mapnik.org/wiki/GettingStarted) ([API](http://svn.mapnik.org/tags/release-0.6.0/docs/api_docs/python/index.html)), de l'utilitaire [nik2img](http://code.google.com/p/mapnik-utils/wiki/Nik2Img) ou encore sous la forme d'un [serveur WMS](http://trac.mapnik.org/wiki/OgcServer).

Une fois le traditionnel "[hello world](http://trac.mapnik.org/wiki/GettingStarted)" et sa jolie carte réalisée j'ai voulu immédiatement être en mesure de produire des tuiles pour une consultation par internet.  
C'est à ce niveau qu'entre en jeu [TileCache](http://tilecache.org/) qui possède la particularité de pouvoir directement interroger et générer les images selon le niveau de zoom désiré.

J'ai donc commencé à paramétrer mon fichier XML, équivalent du MapFile de MapServer, et au bout de quelques jours et presque un millier de lignes je suis arrivé à un résultat satisfaisant. Les deux images présentées ci-dessous sont une vue de La Réunion où est mis en évidence le réseau routier. Les données sont celles de [RDTronic](http://www.rdtronic.com/) entreprise pour laquelle je travaille :

* Vue générale de La Réunion

[![Mapnik](https://cdn.geotribu.fr/img/Blog/Mapnik/mapnik_general_.png "Mapnik"){: .img-center loading=lazy }]

* Zoom sur Saint-Denis

[![Zoom_batiment](https://cdn.geotribu.fr/img/Blog/Mapnik/zoom_baitment.png "Zoom_batiment"){: .img-center loading=lazy }]

La qualité graphique est vraiment exceptionnelle, le trait est net même lorsque sa taille est inférieur à 1 pixel. Le moteur de placement des labels est particulièrement abouti, j'aime également la possibilité d'ajouter des [écussons](http://trac.mapnik.org/wiki/ShieldSymbolizer) à la manière des cartes routières ou ses propres images afin de représnter des POI. Enfin, il est possible de réaliser une[fausse 3D](http://trac.mapnik.org/wiki/BuildingSymbolizer) sur les bâtiments. Il est dommage que pour cette dernière la taille des objets soit fixe et non paramétrable en fonction d'un champ attributaire des données.

En conclusion, j'estime que les quelques jours passés à la compréhension de cet outil valent largement le résultat final. Quel bonheur de pouvoir paramétrer sa sortie graphique au pixel près ! Si vous souhaitez approfondir cette courte introduction à Mapnik je vous conseillerai la visite des liens ci-dessous :

* [+ de démo](http://mapnik.org/demo/)
* [+ d'utilitaires](http://code.google.com/p/mapnik-utils/)
* [+ d'exemples de code](http://mapnik-utils.googlecode.com/svn/example_code/)

----

<!-- geotribu:authors-block -->
