---
title: "1er experience d'OpenStreetMap"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-09-02
description: "1er experience d'OpenStreetMap"
tags:
    - data
    - open source
    - OpenStreetMap
---

# 1er experience d'OpenStreetMap

:calendar: Date de publication initiale : 02 septembre 2009

![logo OpenStreetMap](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/Openstreetmap.png "logo OpenStreetMap"){: .img-thumbnail-left }

Cela faisait longtemps que l'envie de m'impliquer dans le projet **O**pen**S**treet**M**ap (OSM) me titillait. Profitant donc de mes congés, j'ai pu faire mes 1ers pas de "mappeur de la route". Sur les aspects théoriques, le fait que je vienne du monde de la géomatique ainsi que mon expérience dans les bases de données routières a grandement facilité mon initiation. Il ne me restait alors qu'a régler les problèmes d'ordres techniques, c'est à dire le GPS, le logiciel qui me permettrait d'extraire mes données GPS et enfin comprendre JOSM l'une des applications permettant de travailler sur les données d'OSM tout en prenant en compte le fait que je travaille sur Ubuntu.

## Le GPS

![logo Holux](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/holux_GPSport.jpg "logo Holux"){: .img-thumbnail-left }

Première difficulté trouver un GPS "tracker". Après avoir consulté [la liste](https://wiki.openstreetmap.org/wiki/GPS_Reviews) des GPS déjà testés par les équipes d'OSM, je me suis orienté vers le modèle GPSport 245 d'Holux.

Après quelques petits ratés réglages, notamment le rythme d'acquisition des données (temps ou distance) que j'ai spécifié à 3M, me voilà fin prêt à partir à la conquête de mon espace immédiat.

J'enregistre donc mes premières traces et me félicite d'avoir su anticiper mes besoins en mettant muni d'un carnet et de quoi noter quelques indications (nom des rues, plans...). Je me rends compte que cet accessoire devient rapidement aussi essentiel que mon GPS. Sans lui, je ne pourrais pas renseigner les informations attributaires.

![Carnet OSM](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/carnet_OSM.jpg "Carnet OSM"){: .img-center loading=lazy }

Néanmoins, si comme moi vous enregistrez vos données en voiture la présence d'un coéquipier s'occupant de la conduite ou des croquis est obligatoire. J'ai eu la chance de voir ma compagne se prendre au jeu et c'est donc elle qui s'est chargée de réaliser tous les jolis dessins et annotations diverses.

## Extraire les données GPS

Mes 1res données enregistrées, je n'avais qu'une hâte celle de les voir s'afficher sur mon écran. Premier problème, le driver fourni pour mon GPS ne fonctionne que sur Windows or, je suis sur Ubuntu et il est hors de question pour moi de basculer vers l'OS de Bill.

Mon GPS n'étant pas automatiquement reconnu comme périphérique de stockage de masse par Ubuntu, j'essaye alors de l'atteindre en ligne de commande. Mais bon, étant tout de même géographe de formation j'arrive vite à mes limites sur mon pauvre terminal qui doit se demander qu'est ce que je désire faire.

Je me tourne alors vers la panoplie des applications disponibles. Une retient alors particulièrement mon attention, [BT747](http://bt747.free.fr/content/).

La prise en main n'est pas instantanée et je reste bien quelques minutes à me demander comment cela fonctionne. A force de tâtonner et parcourir la documentation j'arrive enfin à extraire mon premier fichier .GPX.

![BT747](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/BT747.png "BT747"){: .img-center loading=lazy }

Une fois habitué ce logiciel se révèle être un véritable couteau suisse de la cartographie. En effet en plus d'être capable de se connecter à mon GPS et d'en extraire les données, il permet de convertir ces dernières dans 6 formats (GPX, KML, KMZ, CSV, HTML, NMEA) ou encore de les afficher directement sur un fond cartographique utilisant comme source de données devinez quoi? Ben, OpenStreetMap évidemment !

![BT747 - Carte](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/BT747_map.png "BT747 - Carte"){: .img-center loading=lazy }

Bon, me voilà muni de mon fichier GPX contenant mes traces. J'ai vérifié rapidement leur cohérence en les visualisant sur [ArqGIS](https://www.qgis.org/). Passons maintenant au coeur de notre projet, mettre à jour les données d'OSM.

## Réaliser la mise à jour

Pour mettre à jour les données j'ai besoin pour cela d'un éditeur cartographique. J'aurais pu pour cela utiliser [Potlach](https://wiki.openstreetmap.org/wiki/FR:Potlatch) l'éditeur en ligne, mais celui-ci montre vite ses limites lors de grosses MAJ. En effet, l'ergonomie n'est pas forcément adaptée et il ne bénéficie pas non plus d'aide à la saisie pour les balises. Il est donc avant tout à réserver pour de petits travaux. Bien évidemment, d'autres éditeurs existent et le choix de l'un ou l'autre dépend avant tout de vos affinités. Matt Amos, sur l'un de ces [posts](http://www.asklater.com/matt/wordpress/2009/08/editor-popularity/), a d'ailleurs joliment illustré la répartition de ces éditeurs par pays.

![OSM Editors](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/created_by_20090826.png "OSM Editors"){: .img-center loading=lazy }

Je m'oriente donc vers [JOSM](https://wiki.openstreetmap.org/wiki/FR:JOSM) qui au vu des copies d'écrans à l'air plutôt sympa. Je regarde dans mon dépôt s'il existe une version spécifique pour Ubuntu. Celle proposée bien que fonctionnelle est largement dépassée. Je [télécharge](http://josm.openstreetmap.de/josm-tested.jar) donc la dernière version stable, que je lance ensuite par un simple "java -jar josm-tested.jar".

![JOSM](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/JOSM.png "JOSM"){: .img-center loading=lazy }

Je télécharge alors directement depuis JOSM, les données d'OSM correspondant à ma zone de MAJ et ajoute également mon fichier GPX correspondant à mes données.

![JOSM - Téléchargement](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/JOSM_OSM.png "JOSM - Téléchargement"){: .img-center loading=lazy }

Je tâtonne un peu avant de comprendre le fonctionnement de JOSM notamment au niveau des options de topologies. Mais la prise en main est beaucoup plus facile que je l'espérais. Un mois avant j'avais dû réaliser un travail similaire sur MapInfo et je dois dire que celui-ci est loin d'atteindre le niveau de JOSM.

Tout est fait pour faciliter le travail de digitalisation. Il est par exemple très facile de créer automatiquement un rond-point, d'aligner automatiquement les noeuds d'un segment, de séparer une rue en deux segments ou au contraire de les fusionner pour ne former qu'un seul élément. Je créé donc rapidement mes premières formes géométriques et grâce à l'aide à la saisie je spécifie les informations attributaires nécessaires (type de route, revêtement...).

![JOSM - Tag](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/tag.png "JOSM - Tag"){: .img-center loading=lazy }

Bon, tout me semble correct, je décide alors de valider mon travail en l'exportant sur OSM.

## Valider la mise à jour

Aie ! Moi qui pensais que tout était bon, voilà que JOSM m'annonce fièrement qu'il a détecté plusieurs erreurs. Celles-ci sont aussi bien d'ordres géométriques, qu'attributaires. Heureusement pour certaines d'entre elles il arrive à les corriger automatiquement et je m'occupe donc de modifier celles restantes.

![JOSM - Erreurs](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/errors_OSM.png "JOSM - Erreurs"){: .img-center loading=lazy }

Je valide à nouveau mes données et les envoie sur le serveur d'OSM. Après quelques heures, c'est avec joie que je vois que celles-ci ont été prises en compte.

![JOSM - Carte](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/OSM_carto.png "JOSM - Carte"){: .img-center loading=lazy }

Et voilà, j'ai à mon tour participé à ce formidable projet en apportant mes quelques mètres de bitumes virtuels. Le plus drôle, c'est que l'on se prend très vite au jeu et je ne me dépasse plus sans mon GPS. Il m'arrive même de prendre volontairement d'autres itinéraires que ceux que j'utilise habituellement dans le seul but d'enregistrer de nouvelles traces.

Je profite de ce post pour vous annoncer que je quitterai bientôt mon île pour une nouvelle aventure en métropole. Je jette un coup d'œil sur OSM afin de voir l'état d'avancement de collecte des données. A mon grand regret, mais tant mieux pour OSM, une très grosse partie à l'air déjà enregistrée. Une fois sur place je regarderai en détail ce que je peux faire. En attendant saurez-vous trouver grâce à l'image ci-dessous où je me rends?

![JOSM - Ville](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/new_ville.png "JOSM - Ville"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->
