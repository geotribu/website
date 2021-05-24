---
title: "Un rendu carte topo QGIS basé sur la BD TOPO®"
authors: ["Florian Boret"]
categories: ["article", "tutoriel"]
date: "2021-06-25 15:00"
description: "Un rendu carte topographique avec QGIS et la BD TOPO®"
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_carte_topo_bdtopo/export_carte_topo_saussines.png"
tags: "carte topographique,QGIS,BD TOPO®,Scan25,IGN"
---

# Un rendu carte topo QGIS basé sur la BD TOPO®"

:calendar: Date de publication initiale : 25 Juin 2021

**Mots-clés :** Carte topographique | QGIS | BD TOPO® | Scan25 | IGN 

Pré-requis :

- Avoir une BD TOPO® en version 3
- Maîtriser [QGIS](https://qgis.org/)

## Introduction

Il y a maintenant deux ans sur la base des données [osm2igeo](https://github.com/igeofr/osm2igeo) que je produisais, j'avais lancé un second projet qui s'appelait [osm2igeotopo](https://github.com/igeofr/osm2igeotopo) et qui avait pour objectif de générer des tuiles raster sur la base d'un rendu carte topo inspiré notamment par [le travail de Romain Lacroix](https://github.com/rxlacroix/CarteTopo).

Mais voilà avec l'[ouverture des données de la BD TOPO®](https://geoservices.ign.fr/documentation/diffusion/telechargement-donnees-libres.html), j'ai décidé de travailler sur un rendu carte topo QGIS basé sur la BD TOPO® et qui vient compléter le projet [TOPen25](https://osm.cquest.org/topen25/#15/48.4018/2.7945) réalisé par [C. Quest](https://twitter.com/cq94).

## Le projet QGIS 

[Accéder au projet QGIS :world_map:](){: .md-button }
{: align=middle }

Le projet QGIS est composé des différentes couches de la BD TOPO® et il doit se placer dans le répertoire : BDT_3-0_SHP_LAMB93_D0...

![Localisation du projet](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_carte_topo_bdtopo/localisation_qgs.png "Localisation du projet"){: loading=lazy .img-center }

Le projet QGIS a été paramétré pour un rendu optimum au 1/25 000 mais libre à chacun de l'adapter à sa guise.

![Le projet QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_carte_topo_bdtopo/qgis_bdtopo_carte_topo.png "Le projet QGIS"){: loading=lazy .img-center }

Voici un exemple d'export réalisé et comme vous pouvez le constater, en plus des données de la BD TOPO® j'ai également ajouté des courbes de niveaux pour améliorer le rendu. Pour les territoires avec plus de relief, il serait également possible de jouer avec les ombrages du MNT pour marquer les pentes.

![Exemple d'export](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_carte_topo_bdtopo/export_carte_topo_saussines.png "Exemple d'export"){: loading=lazy .img-center }

## Conclusion

Ce projet QGIS est une proposition de rendu qui pourrait vous rendre service mais n'hésitez pas à l'adapter et à nous faire part de vos améliorations en commentaire.

----

## Auteur

--8<-- "content/team/fbor.md"
