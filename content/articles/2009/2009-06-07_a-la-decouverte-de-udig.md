---
title: "A la découverte d'uDig"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-06-07
description: "A la découverte d'uDig"
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/udig/udig_splash_screen.png"
tags:
    - open source
    - SIG
    - uDig
---

# A la découverte d'uDig

:calendar: Date de publication initiale : 07 juin 2009

![udig_logo.png](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/uDig.png){: .img-thumbnail-left }

Nous continuons notre tour d'horizon des logiciels SIG OpenSource en abordant cette fois-ci UDIG. Développé par [Refraction research](http://www.refractions.net/), il est basé sur l'IDE [Eclipse](http://www.eclipse.org/). Ce dernier, bien que principalement utilisé dans le monde de la programmation a été habilement détourné pour offrir une plateforme SIG complète.

## Téléchargement et installation

Une fois [UDIG téléchargé](http://udig.refractions.net/download/) il vous suffira simplement de lancer "l'exécutable". Sur Fedora, en raison d'un problème avec XulRunner, j'ai eu quelques soucis à l'installation. Néanmoins, le bug n'est pas lié directement à uDig et il peut être facilement résolu en suivant les [indications](http://udig.refractions.net/confluence/display/EN/Running+uDig#RunninguDig-Fedora10XULRunnerLibraryConflict) disponibles sur le site.

![uDig Splash Screen](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/udig/udig_splash_screen.png "uDig Splash Screen"){: .img-center loading=lazy }

## Découverte de l'interface

Même si l'interface n'est pas aussi agréable que [Puzzle Gis](http://geotribu.net/node/117) on trouve néanmoins rapidement ses repères, les icônes parlent d'elles-mêmes et au bout de quelques manipulations cela devient instinctif. Bien évidemment les personnes utilisant Eclipse ne seront pas dépaysées. Chacun des éléments de l'interface peut se détacher, vous pouvez ainsi facilement avoir d'un côté votre carte de l'autre la table attributaire.

![uDig - Interface](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/udig/dash_board.png "uDig - Interface"){: .img-center loading=lazy }

## Accès aux données

Dans sa configuration initiale, uDig autorise uniquement la lecture des données vecteurs au format ShapeFile. Le choix est par contre beaucoup plus vaste pour celles stockées dans un SGBD. Les bases interrogeables sont : [ArcSDE](https://en.wikipedia.org/wiki/ArcSDE), [DB2](https://fr.wikipedia.org/wiki/DB2), [MySQL](https://fr.wikipedia.org/wiki/MySQL), [Oracle Spatial](https://en.wikipedia.org/wiki/Oracle_Spatial)et [PostGis](https://fr.wikipedia.org/wiki/PostGIS). Les normes OGC ne sont pas non plus oubliées avec l'accès aux normes [WFS](https://fr.wikipedia.org/wiki/Web_Feature_Service) et [WMS](https://fr.wikipedia.org/wiki/Web_Map_Service).

![uDig - Sources de données](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/udig/layer.png "uDig - Sources de données"){: .img-center loading=lazy }

## Modification du style des couches

Il est possible de modifier le style des couches ou d'effectuer une analyse thématique. L'interface est simple tout en restant fonctionnelle.

* Modification du style

![uDig - symbologie](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/udig/style.png "uDig - symbologie"){: .img-center loading=lazy }

* Analyse thématique

![uDig - analyse thématique](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/udig/style2.png "uDig - analyse thématique"){: .img-center loading=lazy }

Néanmoins, les possibilités de personnalisation des styles sont tout de même moins riches qu'avec [OpenJump](http://geotribu.net/node/120).

## Interrogation des données

Il est possible d'accéder aux données soit de manière individuelle en cliquant chacune d'entre elles ou alors en effectuant une sélection globale. Dans le deuxième cas, les objets sont alors mis en évidence dans la table attributaire. Si la sélection se fait depuis la table, il est également possible de zoomer directement sur les entités.

![uDig - Interrogation des données](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/udig/select.png "uDig - Interrogation des données"){: .img-center loading=lazy }

## Édition et modification des objets

Il est possible de modifier aussi bien les attributs que la géométrie des objets. Plusieurs options sont disponibles (ajout de noeuds, modification des noeuds...). Il est dommage que l'outil d'édition soit considéré comme un "simple" outil associé à la carte et non à la couche. En effet, imaginons que je modifie mon entité, et que je souhaite zoomer sur une zone particulière. Le fait de zoomer désactive alors l'outil de zoom.

![uDig - Edition](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/udig/Modify_geom.png "uDig - Edition"){: .img-center loading=lazy }

## Fonctions Spatiales

Dans sa configuration d'origine uDig ne permet pas de réaliser de requêtes ou d'opérations spatiales.  
C'est pourquoi je vous conseille vivement l'installation des plugins disponibles. Vous y trouverez par exemple l'excellente librairie [sextante](http://forge.osor.eu/plugins/wiki/index.php?id=13&type=g) ou encore le portage des fonctionnalités liées à l'hydrologie de Grass avec le plugin [JGRASS](http://udig.refractions.net/gallery/jgrass/). une fois l'ensemble des plugins installé, vous disposez alors d'une boite à outils des plus conséquente.

![uDig - Opérations spatiales](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/udig/spatial_operations.png "uDig - Opérations spatiales"){: .img-center loading=lazy }

![uDig - Sextante](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/udig/sextante_plugin.png "uDig - Sextante"){: .img-center loading=lazy }

## Conclusion

Du fait du nombre important de bases de données auquel il est possible d'accéder, UDIG est l'outil idéal pour toutes les personnes ayant un profil WEB/SIG. Les géomaticien plus traditionalistes se sentiront surement quelque peu dépaysés.

Pour le moment, je dois avouer que c'est UDIG qui me convient le plus. Seul point noir et décidément ils ont tous ce défaut, c'est la pauvreté des formats vecteurs qu'il est possible d'ouvrir. Pour le moment sur ce point, aucun n'a égalé mon fidèle QGIS. Néanmoins, à part cela je trouve UDIG vraiment exceptionnel il mérite en tous cas à être connu et plus "médiatisé".

----

<!-- geotribu:authors-block -->
