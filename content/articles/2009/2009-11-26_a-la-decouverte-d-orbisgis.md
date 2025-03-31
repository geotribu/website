---
title: "A la découverte d'OrbisGIS"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-11-26
description: "A la découverte d'OrbisGIS"
tags:
    - open source
    - OrbisGIS
    - SIG
---

# A la découverte d'OrbisGIS

:calendar: Date de publication initiale : 26 novembre 2009

![logo OrbisGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/orbigis.jpg "logo OrbisGIS"){: .img-thumbnail-left}

Après avoir successivement exploré [PuzzleGis](http://geotribu.net/node/117), [OpenJump](http://geotribu.net/node/120), [UDIG](http://geotribu.net/node/126) et enfin [ArqGIS](http://geotribu.net/node/152) nous découvrirons au cours de ce billet [OrbisGis](http://brehat.ec-nantes.fr/orbisgis/doku.php). Ce dernier développé par l'[Institute on Urban Sciences and Technics](http://www.irstv.cnrs.fr/) (CNRS) est l'œuvre de trois géomaticiens Erwan BOCHER, Thomas LEDUC, Fernando GONZALES-CORTES. N'ayant jamais entendu parlé de ce logiciel, je m'attendais à une "petite application maison" sans grande particularité. Cet a priori ne fut que temporaire et j'avoue avoir été très agréablement surpris. De plus OrbisGIS dispose d'une [documentation](http://brehat.ec-nantes.fr/orbisgis/doku.php?id=support:doc) riche et interactive ce qui permet de ne jamais se sentir pris au dépourvu. Découvrons ensemble ce logiciel.

## Téléchargement et installation

Développé en Java, OrbisGis est multiplateforme vous trouverez sur la [page de téléchargement](http://brehat.ec-nantes.fr/orbisgis/doku.php?id=download:index) une version pour Windows (le **M**al) et une autre pour Linux (le **B**ien). L'installation sur Ubuntu (9.10) n'a posé aucun souci et c'est avec plaisir que j'ai pu voir, dans mon gestionnaire d'applications, l'icône d'OrbisGis.

![OrbisGIS - Header](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/header_medium_blue.png "OrbisGIS - Header"){: .img-center loading=lazy }

## Découverte de l'interface

L'interface est complètement modulaire ce qui permet d'ajouter, de supprimer ou de changer la place des éléments. Vous pouvez ainsi construire l'espace de travail qui vous convient le mieux. Concernant la légende, il est possible de grouper les couches afin de faciliter la lecture de l'information. Pour ma part, le seul élément qui manque à l'appel, est une mini-carte globale permettant de se repérer plus facilement

![OrbisGIS - Inteface](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/general.png "OrbisGIS - Inteface"){: .img-center loading=lazy }

## Accès aux données

Même si OrbisGis permet d'accéder à plus d'une dizaine de formats de données, nous sommes tout de même loin des potentialités de ArqGIS. Néanmoins, il est possible d'ouvrir des données au format VRML (3D). Cela s'explique je pense du fait qu'OrbisGIS soit développé dans le but de simuler des phénomènes urbains d'où la nécessité de pouvoir afficher des objets 3D.

![OrbisGIS - Données](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/data.png "OrbisGIS - Données"){: .img-center loading=lazy }

Côté vecteur, vous pourrez notamment afficher des données ShapeFiles, CSV...

Côté raster nous avons la possibilité d'afficher des images JPEG, PNG et TIFF ou encore celles provenant d'un serveur WMS. Pour ce dernier cas, nous avons réalisé quelques tests à partir du serveur [GeoLittoral](http://www.geolittoral.equipement.gouv.fr/). Les résultats sont exposés ci-dessous.

![OrbisGIS - WMS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/WMS.png "OrbisGIS - WMS"){: .img-center loading=lazy }

![OrbisGIS - Carte WMS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/WMS_ocean.png "OrbisGIS - Carte WMS"){: .img-center loading=lazy }

## Modification du style des couches

OrbisGis permet de modifier le style d'une couche et de réaliser/combiner une ou plusieurs analyses thématiques. Chaque couche dispose ainsi d'un panel dans lequel vous ajoutez les styles que vous désirez.

![OrbisGIS - style](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/CLASSIF.png "OrbisGIS - style"){: .img-center loading=lazy }

Dans l'exemple ci-dessous nous avons réalisé une analyse thématique sur l'aire de chaque pays (en aplat de couleur) et sa population totale (en cercle proportionnel). J'entends déjà les médisants dire "Oui mais pourquoi tu n'as pas fait juste une analyse de densité de population ?" Tout simplement car j'avais besoin d'exemple pour illustrer ma présentation et qu'OrbisGis ne permet pas de créer des analyses à partir de plusieurs champs de la table :)

![OrbisGIS - Analyse thématique](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/analyse_thematique.png "OrbisGIS - Analyse thématique"){: .img-center loading=lazy }

## Interrogation des données

L'interrogation des données peut se faire de deux manières. Soit en passant par la table attributaire ou alors en utilisant le champs de requête SQL.

Dans le 1er cas, tout se fait depuis l'interface graphique. Là encore très bonne surprise car l'Interface Homme Machine (IHM) est vraiment bien pensée. En effet, il suffit de faire un click droit sur une cellule pour qu'un menu s'affiche dans lequel il est possible par exemple de préciser que l'on souhaite sélectionner toutes les entités ayant la même valeur.

Le panneau SQL bien que plus difficile à prendre en main il permet par contre une plus grande liberté. Aux requêtes SQL classiques (Group By, Sum...) s'ajoutent plus de 80 requêtes géographiques disponibles depuis le panneau "SQL repository".

![OrbisGIS - Requete](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/requete_Geo.png "OrbisGIS - Requete"){: .img-center loading=lazy }

![OrbisGIS - SQL](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/SQl.png "OrbisGIS - SQL"){: .img-center loading=lazy }

## Édition et modification des objets

OrbisGis permet de modifier aussi bien les attributs que la géométrie des objets. Néanmoins, je n'ai réalisé ce test que sur des données au format Shapefile.

![OrbisGIS - Edition](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/Edition.png "OrbisGIS - Edition"){: .img-center loading=lazy }

## Le petit plus

Vous pouvez sauvegarder vos vues courantes sous la forme de raccourcis géographiques grâce au menu GeoMarks. Cela peut s'avérer fort utile si vous devez souvent vous déplacer vers des zones pré-définies.

![OrbisGIS - GeoMarks](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/GeoMarks.png "OrbisGIS - GeoMarks"){: .img-center loading=lazy }

## Conclusion

Au final, je dois avouer que c'est sur une excellente appréciation que je finis ce billet. OrbisGis m'a totalement séduit. Il ne lui manque que la possibilité d'accéder à un plus grand nombre de formats de données. Mis à part ce détail, c'est un logiciel complet et bien pensé dont les fonctionnalités n'ont rien à envier aux autres "stars" de l'OpenSource. Encore un grand bravo aux personnes qui se cachent derrière le nom OrbisGis.

----

<!-- geotribu:authors-block -->
