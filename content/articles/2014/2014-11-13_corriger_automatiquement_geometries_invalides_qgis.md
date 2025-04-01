---
title: "Corriger automatiquement des géométries topologiquement invalides avec QGIS"
authors:
    - Arnaud VANDECASTEELE
categories:
    - article
    - tutoriel
comments: true
date: 2014-11-13
description: "Vous avez reçu des données dont les géométries ne sont pas valides ? Pas de panique, voici comment les corriger en utilisant les traitements GRASS intégrées à QGIS."
image: "https://cdn.geotribu.fr/img/tuto/qgis_fix_geometry/qgis_check_geom_validity_start.png"
tags:
    - GIS
    - géométrie
    - GRASS GIS
    - QGIS
    - topologie
---

# Corriger automatiquement des géométries topologiquement invalides avec QGIS

:calendar: Date de publication initiale : 13 novembre 2014

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-thumbnail-left }

Il arrive que, pour différentes raisons, vous receviez une couche de données qui est topologiquement invalide (polygones dont certains arcs se croisent, etc.). Avant d'entrer dans le vif du sujet et si le mot topologie ne vous est pas familier, je vous conseille la lecture de [l'excellent article](http://www.portailsig.org/content/grass-gis-geometries-topologies-et-consequences-pratiques-vecteurs-rasters-volumes) de Martin Laloux paru sur le Portail SIG.

Bon revenons à nos moutons et à ma couche de données. Donc j'ai reçu des données prises depuis un GPS puis directement exportées au format Shapefiles. En raison de l'imprécision du GPS et du trajet effectué par la personne en charge de l'acquisition des données, la géométrie finale n'était pas toujours topologiquement valide. Ainsi, mes données s'affichaient correctement sur QGIS mais pour autant il m'était impossible de les analyser ou encore de les importer dans PostGIS. En effet, lors de l'import la librairie GEOS se plaignait à juste titre des nombreuses erreurs de topologie.

Une approche aurait pu être de simplifier la géométrie des objets afin d'éliminer les erreurs potentielles. Bien que simple, cette démarche entraine également une modification initiale de la géométrie initiale de l'objet. De plus, même si cela élimine un grand nombre d'erreurs il en restait tout de même.

De ce fait, je me suis tourné vers des outils dédiés me permettant de complètement corriger mes géométries. La démarche suivie est expliquée dans les paragraphes ci-dessous.

----

## Logiciel utilisé

Le logiciel SIG [QGIS](https://www.qgis.org) ainsi que son plugin GRASS ont été utilisés pour corriger la topologie des objets. L’avantage d’utiliser GRASS est que contrairement à la plupart des logiciels SIG existants celui-ci s’appuie nativement sur une représentation topologique (arc, nœuds) des objets géographiques.

Le plugin GRASS permet de bénéficier des nombreuses fonctionnalités du logiciel GRASS directement dans QGIS. Celui-ci est accessible depuis la boite à outils de QGIS. Si cette boite à outils n’est pas disponible, il suffit de l’activer à partir du menu : vue ->panneaux -> boite à outils.

Cette boite à outils regroupe un ensemble de « géotraitements », mais seul le module vclean de Grass sera utilisé. Ce module dispose de différentes options dont deux qui seront utilisées pour notre démarche à savoir break et rmarea.

![QGIS Processing Toolbox GRASS vclean](https://cdn.geotribu.fr/img/tuto/qgis_fix_geometry/qgis_processing_toolbox_2-4.png "QGIS Processing Toolbox GRASS vclean"){: .img-center loading=lazy }

## Démarche

Comme précisé en introduction, la couche de données en entrée possède des entités dont la géométrie est invalide. L'outil de vérification de QGIS révèle d'ailleurs un grand nombre d'erreurs.

![QGIS GRASS vclean](https://cdn.geotribu.fr/img/tuto/qgis_fix_geometry/qgis_check_geom_validity_start.png "QGIS GRASS vclean"){: .img-center loading=lazy }

La démarche proposée pour corriger ces erreurs s’appuie sur 4 principales étapes.

### Découpage des intersections

Tout d’abord en utilisant l’option `break` la géométrie initiale de l’objet est découpée lorsqu’une intersection est détectée. Le seuil (*threshold*) peut varier en fonction de vos données. Quelques tests doivent être effectués afin d’obtenir le plus approprié. Dans notre cas, un seuil à 10 était celui donnant les meilleurs résultats.  

![vclean - Formulaire break](https://cdn.geotribu.fr/img/tuto/qgis_fix_geometry/qgis_geom_step_break_form.png "vclean - Formulaire break"){: .img-center loading=lazy }

À la fin de processus, les polygones ayant des intersections sont alors découpés en deux.  

![vclean - Résultat break](https://cdn.geotribu.fr/img/tuto/qgis_fix_geometry/qgis_geom_step_break_result.png "vclean - Résultat break"){: .img-center loading=lazy }

### Suppression des reliquats

Une fois, le découpage des intersections réalisé, il faut maintenant supprimer les reliquats de géométrie. Pour cela l’option `rmarea` est utilisée. Celle-ci supprime les géométries dont l’aire est inférieure à un seuil défini. Comme précédemment, ce seuil peut varier est doit être adapté en fonction des données initiales.  

![vclean - Résultat rmarea break](https://cdn.geotribu.fr/img/tuto/qgis_fix_geometry/qgis_geom_step_rmarea_result.png "vclean - Résultat rmarea break"){: .img-center loading=lazy }

Une ultime vérification me confirme que ma couche est dorénavant topologiquement valide.

![vclean - Vérification des géométries](https://cdn.geotribu.fr/img/tuto/qgis_fix_geometry/qgis_check_geom_validity_end.png "vclean - Vérification des géométries"){: .img-center loading=lazy }

Et voilà, j'ai maintenant ma couche qui est géométriquement valide. Je peux alors l'importer dans PostGIS ou effectuer les traitements que je souhaite.

----

## Conclusion

La démarche proposée est essentiellement manuelle. Bien évidemment rien ne vous empêche d'utiliser le model builder de QGIS pour automatiser tout cela ! A vous de jouer.

----

<!-- geotribu:authors-block -->
