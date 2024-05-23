---
title: "GeoServer bientôt en version 2.0"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-06-04
description: "GeoServer bientôt en version 2.0"
tags:
    - GeoServer
    - open source
---

# GeoServer bientôt en version 2.0

:calendar: Date de publication initiale : 04 juin 2009

![logo GeoServer](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/geoserver.png "logo GeoServer"){: .img-thumbnail-left }

GeoServer est, comme son nom l'indique, un serveur cartographique OpenSource sous licence GPL 2.0. Son développement initié par l'association " The Open Planning Project (TOPP)" avait au départ pour objectif d'offrir une suite d'outils permettant de rendre la gestion de projets urbain plus transparente pour les citoyens. La philosophie principale étant de l'aveu même des créateurs de s'orienter vers une "Open Democraty".

GeoServer a par la suite continué à évoluer en intégrant notamment, les normes définies par l' "Open Geospatial Consortium (OGC)" ainsi que des modules supplémentaires permettant l'intégration de données multi-sources (ShapeFiles, Oracle, PostGis...).

La version 2.0 est disponible depuis peu en [version bêta](http://blog.geoserver.org/2009/06/03/geoserver-20-now-in-beta/). Au-delà des nombreuses [corrections et améliorations](http://jira.codehaus.org/browse/GEOS/fixforversion/15082) le changement le plus marquant et aussi le plus visible est sa [nouvelle interface](http://blog.geoserver.org/2009/04/20/see-the-new-ui/) se basant sur le [framework wicket](http://wicket.apache.org/). A cela s'ajoute également une modification du workflow de configuration des couches. En effet le processus qui se décomposait auparavant en 3 étapes (Submit -> Apply -> Save ) a été simplifié et il suffit maintenant de simplement sauvegarder ses modifications.

* Ancienne interface

![Configuration](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/configuration.jpg "Configuration"){: .img-center loading=lazy }

* Nouvelle interface

![Board](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/board_geoserver.png "Board"){: .img-center loading=lazy }

Personnellement je trouve que ce changement est des plus réussi. Du coup, l'interface est beaucoup plus claire et accessible.

* Groupement des couches

![Layer group](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/grouing_layer.png "Layer group"){: .img-center loading=lazy }

* Choix de l'ESPG

![EPSG](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/EPSG.png "EPSG"){: .img-center loading=lazy }

* Définition du SLD

![Style](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/style.png "Style"){: .img-center loading=lazy }

Au final, avec cette nouvelle version toute l'équipe de GeoServer nous offre un produit bien abouti. Les lourdeurs présentes auparavant ont été corrigées et le fait d'avoir, au contraire de MapServer, interface d'administration est vraiment très agréable.

----

<!-- geotribu:authors-block -->
