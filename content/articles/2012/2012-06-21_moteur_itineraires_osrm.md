---
title: "Créer votre moteur d'itinéraires Open Source avec OSRM"
authors:
    - Arnaud VANDECASTEELE
categories:
    - article
    - tutoriel
comments: true
date: 2012-06-21
description: "Le calcul d'itinéraires est un enjeu courant dans les métiers ed l'information géographique. Découvrez comment créer un moteur de calcul d'itinéraires avec Open Source Routing Machine (OSRM)."
tags:
    - open source
    - OpenStreetMap
    - OSRM
---

# Créer votre moteur d'itinéraires Open Source avec OSRM

:calendar: Date de publication initiale : 21 juin 2012

## Introduction

![logo OSRM](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/osrm.png "logo OSRM"){: .img-thumbnail-left loading=lazy }

Souvent, quand je parle d'OpenStreetMap (OSM), on me répond : "ah oui c'est un peu comme Google Maps mais en libre". Bien que cela ne soit pas totalement faux, c'est réduire le projet OSM à sa simple utilisation comme fond de carte. Or les possibilités et les potentialités de celui-ci sont bien plus grandes. Mais, et je trouve cela dommage, il existe encore trop peu d'applications permettant une exploitation de ces données Open Source. Néanmoins, trop peu ne veut pas dire aucune. Preuve en est, je vous présenterai dans ce billet [Open Source Routing Machine](http://project-osrm.org/), un moteur d'itinéraire Open Source. Fini le simple affichage de données sur un fond de carte, nous allons maintenant exploiter le plein potentiel de celles-ci !

----

## Open Source Routing Machine

Créé par [Dennis Luxen](http://algo2.iti.kit.edu/luxen.php) de l'Institut Technologique de Karlsruhe, [Open Source Routing Machine](http://project-osrm.org/) (OSRM) est un moteur d'itinéraire Open Source utilisant les données d'[OpenStreetMap](https://www.openstreetmap.org/). Écrit en C++, il est utilisable sur différentes plateformes (Linux, FreeBSD, Windows, Mac). Contrairement aux autres moteurs existants qui sont pour la plupart basés sur un algorithme de type A*, celui-ci implémente l’approche de contraction de hiérarchies de Geisberger [^1]. Je serai bien incapable de vous parler en détail de cet algorithme, mais si cela vous intéresse sachez que vous pouvez consulter la thèse de Gräbener dont l'un des paragraphes porte sur ce sujet [^2].

Bon c'est bien beau d'implémenter un autre algorithme, mais est-ce pour autant que celui-ci est plus rapide. En tout état de cause OUI ! La comparaison effectuée par [Pascal Neis](http://neis-one.org/) est sans équivoque. En effet, OSRM est 4 à 7 fois plus rapide que les moteur d'itinéraires de MapQuest et de CloudMade. Mieux encore, il se place même devant celui de Google, c'est vous dire.

![Routing - Comparaison](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/osrm/comparison_routing_times.png "Routing - Comparaison"){: .img-center loading=lazy }

> Source : [Neis One](https://neis-one.org/2011/07/comparison-routing/)

Enfin, pour alimenter un moteur d'itinéraires il vous faut des données. Là encore, les concepteurs du projet ont pensé à tout car OSRM est capable de lire directement les fichiers [OpenStreetMap](https://www.openstreetmap.org/). Petit rappel si cela était nécessaire, mais OSM est un projet de cartographie libre vous permettant à la fois de contribuer mais aussi d'exploiter les données produites. C'est d'ailleurs ce que nous allons faire dans le cadre de ce billet. Passons donc à la partie technique et mettons en place notre propre serveur OSRM.

### Installation d'OSRM

La meilleure source d'informations est bien évidemment le [Wiki du projet](https://github.com/DennisOSRM/Project-OSRM/wiki). Dans le cadre de ce billet, nous relaterons les différentes étapes par lesquelles nous sommes passées afin d'illustrer plus concrètement la démarche. Cela vous permettra en tout cas de voir avec quelle simplicité cela a été réalisé.

La première étape consiste à télécharger les [sources du projet](https://github.com/DennisOSRM/Project-OSRM). Pour cela, un simple `git clone` est suffisant. Maintenant, voyons voir les prérequis. En effet, OSRM s'appuie sur un certain nombre de bibliothèques. Lors de notre première installation sur une Ubtuntu 11.04, nous avions du compiler les librairies protobuf et boost pour des raisons de versions trop anciennes dans les dépôts. Depuis, une nouvelle installation sur une Ubtuntu 12.04 a résolu tout cela et il suffit simplement de faire un apt-get install en spécifiant les bibliothèques ci-dessous :

```bash
sudo apt-get install build-essential git scons libprotoc-dev libprotobuf7 protobuf-compiler libprotobuf-dev libpng-dev libbz2-dev sudo apt-get install libstxxl-dev libstxxl-doc libstxxl1 libxml2-dev libzip-dev libboost-thread-dev libboost-system-dev libboost-regex-dev
```

Afin de permettre un certain confort de lecture, nous avons séparé le téléchargement des bibliothèques en deux lignes. Mais vous pouvez bien évidemment spécifier le tout avec un seul `apt-get`. On laisse un peu le temps à la machine de tout télécharger et installer et nous avons quasiment terminé. En effet, il vous suffit maintenant de lancer la commande `scons` dans le répertoire d'OSRM et le projet se compilera automatiquement. Si vous fonctionnez sur un Debian ou une Ubuntu, il se peut, comme cela a été le cas pour nous, que la compilation retourne un message d'erreur. Pas de panique, c'est un [problème connu](https://github.com/DennisOSRM/Project-OSRM/issues/177) et il suffit simplement de relancer la commande une seconde fois pour que tout fonctionne.

Voilà, tout est quasiment terminé. Il reste maintenant à passer à la configuration et nous serons prêts à nous amuser.

### Préparation des données

Avant d'aborder concrètement la configuration d'OSRM il y a encore une petite chose à faire, la préparation des données. En effet, OSRM précalcule les itinéraires afin de proposer des performances optimales. Pour cela, deux étapes sont nécessaires.

#### Extraire

Tout d'abord, toujours dans le dossier contenant les sources d'OSRM, il faut lancer la commande `osrm-extract` avec en argument le chemin vers le fichier OSM. Sachez que OSRM est également capable de directement lire les fichiers au format bz2 ou pbf. mais revenons à notre extraction des données :

```bash
./osrm-extract MonFichier.osm
```

Une fois réalisé, vous obtiendrez alors trois autres fichiers dont l'extension est : `MonFichier.osrm` `MonFichier.osrm.names` et `MonFichier.osrm.restrictions`.

#### Créer la hiérarchie

Nous utiliserons deux d’entre eux lors de l'étape de création de la hiérarchie. Celle-ci permet au moteur de précalculer les itinéraires potentiels. Par défaut une configuration (ram, disk, etc.) est déjà pré-paramétrée. Néanmoins, en fonction de votre architecture informatique vous pouvez affiner ces paramètres. Pour le moment, faisons simple et gardons celle déjà proposée. Lançons donc la commande `osrm-prepare` en spécifiant cette fois en argument `MonFichier.osrm` et `MonFichier.osrm.restrictions` :

```bash
./osrm-prepare MonFichier.osrm MonFichier.osrm.restrictions
```

Vous devriez maintenant disposer de 5 nouveaux fichiers : `MonFichier.osrm.nodes`, `MonFichier.osrm.edges`, `MonFichier.osrm.ramIndex`, `MonFichier.osrm.fileIndex` et `MonFichier.osrm.hsgr`.

### Configuration d'OSRM

Allez, encore quelques secondes et tout est quasiment terminé. Dernière étape, la configuration d'OSRM. Pour cela, tout se fait à partir du fichier `server.ini`. La structure de celui-ci est la suivante :

```ini
Threads = 8
IP = 00.00.00.00
Port = 5000
hsgrData=MonFichier.osrm.hsgr
nodesData=MonFichier.osrm.nodes
edgesData=MonFichier.osrm.edges
ramIndex=MonFichier.osrm.ramIndex
fileIndex=MonFichier.osrm.fileIndex
namesData=MonFichier.osrm.names
timestamp=MonFichier.osrm.timestamp
```

Là encore, rien d'insurmontable. Le seul paramètre qui n'est pas renseigné dans le wiki est le timestamp. Je n'ai pas compris à quoi il servait et aucun fichier de ce type n'est créé par OSRM. Néanmoins, j'ai ajouté la même information que les lignes précédentes et cela fonctionne. Ce fichier n'a pas l'air primordial !

Maintenant que tout est configuré, lançons notre moteur d'itinéraires. Cela se fait grâce à la commande osrm-routed. Si tout est correct, les lignes suivantes devraient s'afficher :

```bash
./osrm-routed [server] starting up engines, saved at Sat Jun 16 10:30:46 2012 [server] http 1.1 compression handled by zlib version 1.2.3.4 [info Server/DataStructures/QueryObjectsStorage.cpp:26] loading graph data [info Server/DataStructures/QueryObjectsStorage.cpp:33] Data checksum is 358366287 [info Server/DataStructures/QueryObjectsStorage.cpp:39] Loading Timestamp [info Server/DataStructures/QueryObjectsStorage.cpp:49] Loading auxiliary information [info Server/DataStructures/QueryObjectsStorage.cpp:57] Loading names index [info Server/DataStructures/QueryObjectsStorage.cpp:74] All query data structures loaded [handler] registering plugin hello [handler] registering plugin locate [handler] registering plugin nearest [handler] registering plugin timestamp [handler] registering plugin viaroute [server] running and waiting for requests
```

Tadam :party_face: ! Votre serveur est prêt et il n'attend plus que vos requêtes. Pour cela, tout se fait par le biais d'appels HTTP formatés. Différentes requêtes sont disponibles (locate, nearest et viaroute) et pour plus de détails je vous laisse le soin de consulter l'[API](https://github.com/DennisOSRM/Project-OSRM/wiki/Server-api) ainsi que le billet écrit par Rodolphe Quiédeville.

#### Visualisation des itinéraires

Par défaut, vous trouverez dans le fichier `Docs/WebFrontend` d'OSRM une interface basée sur OpenLayers [développée par Pascal Neis](http://neis-one.org/2011/05/gui-osrm/). Bien que parfaitement fonctionnelle notre coup de coeur va sur celle développée par Dennis Schiefer dont les [sources](https://github.com/DennisOSRM/Project-OSRM-Web) sont sur GitHub. Pourquoi celle-là ? Tout simplement parce que l'ergonomie est bien meilleure et qu'elle possède un plus grand nombre de fonctionnalités.

Une fois les sources téléchargées et le dossier placé dans un endroit accessible par internet il suffit de configurer le projet. Pour cela, tout est centralisé dans le fichier `OSRM.config.js`. Le paramètre principal est `HOST_ROUTING_URL` qui indique l'adresse de votre serveur d'itinéraires. Ensuite, à vous de tout customiser comme vous le souhaitez.

Bon visuellement qu'est-ce que cela donne ? Le plus simple pour cela est de faire un tour sur la [démo](http://map.project-osrm.org/) disponible en ligne. Amusez-vous à calculer quelques itinéraires, vous verrez comme cela est rapide. En plus, OSRM est même capable de prendre en compte les lignes de ferry (cf [exemple](http://map.project-osrm.org/Gr)).

Chez Géotribu nous avons également notre projet OSRM Home Made ! Tout d'abord parce que nous avions envie d'essayer et aussi car sur la zone qui nous intéressait (La Réunion) les données proposées dans la démo précédente sont assez vieilles (quoi que depuis, il semblerait qu'une mise jour a été réalisée). Quoi qu'il en soit, voilà le premier moteur d'itinéraires Open Source pour l'Ile de La Réunion :

[![OSRM 974](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/osrm/OSRM974.png "OSRM 974"){: .img-center loading=lazy }](http://geotribu.net/applications/OSRM_leaflet_974/main.html)

----

## Conclusion

Nous arrivons au terme de cette courte introduction à OSRM. Au départ, ce projet nous avait immédiatement plu par la rapidité des calculs ainsi que par son utilisation d'OpenStreetMap. Ce sentiment s'est confirmé par la suite tant son installation ainsi que sa configuration sont simples. Bien qu'encore assez jeune, il pourrait néanmoins devenir une référence dans le domaine. A voir maintenant si de futurs développements sont programmés et surtout si les créateurs du projet arrivent à fédérer une communauté. En tout cas, c'est un beau boulot.

Félicitations à toute l'équipe de l'Institut Technologique de Karlsruhe !

----

<!-- geotribu:authors-block -->

<!-- Footnotes -->
[^1]: Geisberger, R., Sanders, P., Schultes, D. and Delling, D. (2008). Contraction hierarchies : Faster and simpler hierarchical routing in road networks. Experimental Algorithms, pp. 319–333. (<http://algo2.iti.kit.edu/schultes/hwy/contract.pdf>)
[^2]: Gräbener, T. (2010) [Calcul d'itinéraire multimodal et multiobjectif en milieu urbain, pp. 94](http://dl.demotera.com/these_graebener.pdf)
