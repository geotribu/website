---
title: Un rendu carte topo QGIS basé sur la BD TOPO®
authors:
    - Florian BORET
categories:
    - article
    - tutoriel
comments: true
date: 2021-05-28
description: Un rendu carte topographique avec QGIS et la BD TOPO®
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_carte_topo_bdtopo/export_carte_topo_saussines.png
tags:
    - carte topographique
    - BD TOPO
    - IGN
    - QGIS
    - Scan25
---

# Un rendu carte topo QGIS basé sur la BD TOPO®

:calendar: Date de publication initiale : 28 Mai 2021

Pré-requis :

- Avoir une BD TOPO® en version 3
- Gestion des styles [QGIS](https://qgis.org/)

## Introduction

![Scan25](https://cdn.geotribu.fr/img/logos-icones/divers/scan25.jpg "Icône Scan25"){: .img-thumbnail-left }

Il y a maintenant deux ans, en travaillant sur la base des données [osm2igeo](https://github.com/igeofr/osm2igeo/) que je produisais, je me lançais dans un second projet [osm2igeotopo](https://github.com/igeofr/osm2igeotopo/) avec pour objectif de générer des tuiles raster sur la base d'un rendu carte topo inspiré notamment par [le travail de R. Lacroix](https://github.com/rxlacroix/CarteTopo/).

Mais voilà, avec l'[ouverture des données de la BD TOPO®](https://geoservices.ign.fr/documentation/diffusion/telechargement-donnees-libres.html), j'ai décidé de remettre le pied à l'étrier pour proposer un rendu QGIS de la carte topo en m'appuyant sur la [BD TOPO®](https://geoservices.ign.fr/documentation/diffusion/telechargement-donnees-libres.html#bd-topo).

A noter que ce projet vient en complément du projet [TOPen25](https://osm.cquest.org/topen25/#15/48.4018/2.7945) de [C. Quest](https://twitter.com/cq94).

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Le projet QGIS

![logo qgis](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "Logo QGIS"){: .img-thumbnail-left }

Le projet QGIS est composé des différentes couches de la BD TOPO® et il doit se placer dans le répertoire `BDT_3-0_SHP_LAMB93_D0...`.

[Accéder au projet QGIS :world_map:](https://github.com/igeofr/qgis3/blob/master/qgs/Projet_Carto_BDT_3-0_FXX_CARTE_TOPO.qgs){: .md-button }
{: align=middle }

![Localisation du projet](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_carte_topo_bdtopo/localisation_qgs.png "Localisation du projet"){: loading=lazy .img-center }

Le projet QGIS est paramétré pour un rendu au 1/25 000 mais libre à chacun de l'adapter à sa guise pour d'autres échelles.

![Le projet QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_carte_topo_bdtopo/qgis_bdtopo_carte_topo.png "Le projet QGIS"){: loading=lazy .img-center }

Voici un exemple d'export réalisé et comme vous pouvez le constater, en plus des données de la BD TOPO® j'ai également ajouté des courbes de niveaux pour améliorer le rendu. Pour les territoires avec plus de relief, il serait également pertinent de jouer avec les ombrages du MNT pour marquer les pentes.

![Exemple d'export](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_carte_topo_bdtopo/export_carte_topo_saussines.png "Exemple d'export"){: loading=lazy .img-center }

## Conclusion

Ce projet QGIS est une première proposition de rendu mais n'hésitez pas à l'adapter en fonction de vos besoins et à nous faire part de vos améliorations en commentaire.

## Présentation aux Rencontres des Utilisateurs Francophones de QGIS 2022

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/PjeoqxC9Zy8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

----

<!-- geotribu:authors-block -->
