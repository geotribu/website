---
title: "A la découverte de Puzzle GIS"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-05-24
description: "A la découverte de Puzzle GIS"
tags:
    - Java
    - open source
    - Puzzle GIS
    - SIG
---

# A la découverte de Puzzle GIS

:calendar: Date de publication initiale : 24 mai 2009

## introduction

![logo Puzzle GIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/puzzle_gis.gif "logo Puzzle GIS"){: .img-thumbnail-left }

D'habitude j'utilise principalement QGis, sa souplesse d'utilisation et ses fonctionnalités me conviennent parfaitement. Mais voilà, il y a quelques semaines, suite à une mise à jour de Fedora je me suis retrouvé avec un message d'erreur : "Segmentation Fault" au lancement de mon application.  

J'ai donc commencé à chercher d'autres logiciels pouvant répondre à mes attentes. Ce billet est le premier d'une série de 4 présentations au cours desquelles nous introduirons successivement [Puzzle GIS](http://puzzle-gis.codehaus.org/index.html), [GvSIG](http://www.gvsig.gva.es/), [Udig](http://udig.refractions.net/) et [Qgis](http://www.qgis.org/) pour enfin finir sur une comparaison générale.

Développé principalement par Johann Sorel, Puzzle GIS est une application 100% Java utilisant la plateforme de développement [NetBeans](http://www.netbeans.org/). Ce projet a débuté sous la forme d'un simple projet tutoré qui a par la suite évolué devenant ainsi Alter-sig puis aujourd'hui Puzzle GIS.

![Démarrage puzzleGis](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/demarrage_puzzleGis.png "Démarrage puzzleGis"){: .img-center loading=lazy }

## Téléchargement et installation

Premier point positif, l'installation est facile et rapide. En effet, après avoir [téléchargé](http://puzzle-gis.codehaus.org/download.html) l'application je n'ai eu qu'à lancer un `sh puzzle` pour que tout fonctionne. L'interface est claire et agréable, les icônes explicites, de suite on se sent à l'aise ce qui me conforte dans mon idée de continuer à explorer ce logiciel, je me décide donc à créer mon premier projet.

![PuzzleGis Board](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/puzzleGis-Board.png "PuzzleGis Board"){: .img-center loading=lazy }

## Découverte de l'interface

Je configure ensuite ma première carte et ajoute ma couche. Le glissé-déposé et le système d'onglets fonctionnent bien et apportent une véritable souplesse d'utilisation. Néanmoins, j'ai du jouer un peu avant de comprendre la logique de *maps* et *sources*. Mais au final ce fonctionnement s'avère très utile. Vous pouvez en effet, au sein d'un même projet créer plusieurs cartes contenant ou non des sources de données communes. Nous pouvons imaginer par exemple créer un projet général par zones géographiques et autant de cartes ensuite que de thématiques.

Les outils de navigation sont intuitifs et le globe à la Google-Earth apporte un petit plus. Même si le choix ne se limite qu'à un seul modèle la carte peut être enrichie par une barre d'échelle et une flèche du nord. Même si les icônes parlent d'elles-mêmes il est dommage qu'une petite infobulle descriptive ne s'affiche pas au passage de la souris.

![Board map](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/board_map.png "Board map"){: .img-center loading=lazy }

## Accès aux données

En dehors du format shapefile il est également possible d'ajouter des données provenant de PostGis et de serveurs WMS. Le fait de ne pouvoir accéder directement à différentes sources de données vecteurs et/ou raster est assez limitant, heureusement que le plugin Puzzle Shell (ancien alter-conv) permet le passage d'un format à l'autre.

![Plugins](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/plugins.png "Plugins"){: .img-center loading=lazy }

## Modification du style des couches

Il est possible de changer le style des couches et ainsi d'adapter la sémiologie à sa convenance. J'avoue avoir été un peu déçu car pour que le changement de style s'opère il faut pour cela recharger la vue, un petit point en moins...

## Interrogation des données

La consultation des données attributaires est également possible. Le tri par colonne apporte un plus à l'utilisation mais l'utilisation de filtre s'avère laborieuse.

![Attributs](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/attributs.png "Attributs"){: .img-center loading=lazy }

En conclusion, je classerai Puzzle-GIS dans la catégorie viewer. Les fonctionnalités de base (navigation, consultation des attributs...) d'un SIG sont disponibles. L'interface est vraiment des plus agréables du coup l'utilisation en est facilité. A mon sens un seul point négatif vient ternir ce tableau, l'impossibilité d'ouvrir des formats autres que le shapefile. Cela reste en tout cas un projet à surveiller et qui au vu de l'enthousiasme de son développeur devrait continuer à évoluer.

----

<!-- geotribu:authors-block -->
