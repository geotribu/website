---
title: "DicoGIS : le dictionnaire de données SIG"
authors: Julien Moura
category: article
date: 2014-09-25
description: "DicoGIS, utilitaire pour générer automatiquement un dictionnaire de métadonnées sur une base SIG."
hero: "DicoGIS, Le Petit Robert des données SIG"
tags: DicoGIS,GDAL,OGR,Python,métadonnées
---

# DicoGIS : le dictionnaire de données SIG

:calendar: Date de publication initiale : 25 septembre 2014

**Mots-clés :** DicoGIS | GDAL | OGR | Python | métadonnées

Ou comment se créer un Petit Robert de l’information géographique en 5 minutes et 3 clics.  
Je vous présente un petit utilitaire sans prétention sinon d'être bien pratique pour la gestion de données.

![DicoGIS - Animated demonstration](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/DicoGIS/DicoGIS_demo_w8.gif)

----

## Présentation de l’outil

[DicoGIS](https://github.com/Guts/DicoGIS) est un petit utilitaire qui produit un dictionnaire de données au format Excel 2003 (.xls). Disponible sous forme d’exécutable Windows (.exe) sans installation ou sous forme de script (voir les pré-requis) il peut donc s’utiliser directement sur une clé USB par exemple.

![DicoGIS - Logo](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/DicoGIS/DicoGIS_logo.png){: .img-rdp-news-thumb }

Il est particulièrement utile dans certains cas de figure :

* on vous refile une base de données fichiers ou PostGIS dans laquelle vous aimeriez savoir ce qu’il peut bien y avoir dedans ;
* dans le cadre de votre travail ou d’un projet, vous souhaitez fournir facilement un dictionnaire des données fournies, que ce soit à vos collègues, partenaires ou clients.
J’ai commencé à le développer en complément de [Metadator](http://www.portailsig.org/content/metadator-creation-automatisee-de-metadonnees) et je m’en sers aujourd’hui régulièrement, notamment pour réaliser un rapide audit des données et un support utile pour la conception des thésaurus internes dans la phase d’accompagnement des projets avec [Isogeo](http://www.isogeo.com/).

## Caractéristiques techniques

### Côté développement

* développé en [Python 2.7.8](https://www.python.org/) ;
* librairie [GDAL](http://geotribu.net/taxonomy/term/255)/[OGR](http://geotribu.net/taxonomy/term/136) 1.11.0-2 ;
* librairie [python-excel/xlwt](https://github.com/python-excel/xlwt) pour écrire les fichiers Excel 2003 (.xls) ;
* librairie [Tkinter / ttk](https://docs.python.org/2/library/tkinter.html) pour l'interface graphique (par défaut avec Python sur Windows mais non incluse par défaut dans les distributions Debian) ;
* librairie [py2exe](http://www.py2exe.org/) pour générer facilement l'exécutable Windows.

Le code est disponible sur GitHub en [licence GPL 3](https://github.com/Guts/DicoGIS/blob/master/LICENSE), c’est-à-dire que chacun est tout à fait libre de réutiliser ou modifier le code.

### Côté utilisation

Les formats pris en compte sont potentiellement tous ceux de [GDAL](http://www.gdal.org/formats_list.html) et [OGR](http://www.gdal.org/ogr_formats.html) mais pour l'instant voici ceux qui sont implémentés :

* vecteurs : shapefile, tables MapInfo, GeoJSON, GML, KML
* rasters : ECW, GeoTIFF, JPEG
* bases de données "plates" (fichiers) : Esri File GDB
* CAO : DXF (+ listing des DWG)
* Documents cartos : Geospatial PDF

En mode script Python, c'est (a priori...) multiplateformes et a été testé sur:

* Ubuntu 12/14.04
* Windows 7/8.1
* Mac OS X (merci à [GIS Blog Fr](https://twitter.com/gisblogfr/status/515068147901407232))

DicoGIS est disponible en [3 langues (Français, Anglais et Espagnol)](https://github.com/Guts/DicoGIS/tree/master/data/locale) mais il est facile de personnaliser et/ou d'ajouter les traductions.

En ce qui concerne les performances, cela dépend surtout de la machine sur laquelle DicoGIS est lancé. De mon côté, le traitement met environ 30 secondes pour :

* une quarantaine de vecteurs,
* une dizaine de rasters (qui pèsent environ 90 Mo au total),
* 7 FileGDB contenant une soixantaine de vecteurs
* et quelques DXF.

## Utilisation

### Téléchargement et premier lancement

1. Télécharger la dernière version :

* soit de [l’exécutable Windows](https://github.com/Guts/DicoGIS/releases),
* soit du [code source](https://github.com/Guts/DicoGIS/archive/master.zip).

2. Dézipper et lancer DicoGIS.exe / le script DicoGIS.py

![DicoGIS - Launch](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/DicoGIS/00a_DicoGIS_Win32exe.PNG)

3. Changer la langue au besoin

![DicoGIS - Switch language](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/DicoGIS/99_DicoGIS_SwitchLanguage.gif)

### Scan de données organisées en fichiers

1. Choisir le dossier parent : l’exploration commence et la barre de progression tourne jusqu’à la fin du listing
2. Choisir les formats désirés

![DicoGIS- Listing](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/DicoGIS/02_DicoGIS_Listing.gif)

### Scan d'une base PostGIS

Pour des données stockées dans une base PostgreSQL / PostGIS, c'est le même principe sauf qu'il faut entrer les paramètres de connexion :

![DicoGIS - Processing PostGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/DicoGIS/06_DicoGIS_PostGIS.gif)

### Traitement

Lancer et attendre la fin du traitement : sauvegarder le fichier Excel généré.

![DicoGIS - Processing files](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/DicoGIS/05_DicoGIS_Processing.gif)  

Consulter le fichier en sortie et le fichier `DicoGIS.log` (dans lequel il y a un paquet d'informations ^^).

## Et au final, quelles informations sur quels formats

En sortie, vous obtenez un fichier Excel (2003 = .xls) dans lequel les métadonnées sont organisées en différents onglets correspondant au type de donnée. J'ai fait une [matrice des informations disponibles selon le format](https://github.com/Guts/DicoGIS/blob/master/doc/InfosByFormats_matrix.md).

## A venir (ou pas)

Voici les quelques évolutions que j'envisage, mais vu que je ne suis pas mère Thérésa, que j'ai pas non plus beaucoup de temps disponible et que j'ai la flemme :), il ne faut pas y voir un quelconque engagement :

* prendre en compte de nouveaux formats : DGN, Spatialite, MXD, QGS, Geoconcept
* ajouter un onglet de statistiques globales avec de jolis graphiques ;
* basculer de python-xlwt vers xlsxwriter.
* un jour sur Python 3.x mais il faudrait déjà que py2exe soit stable de ce côté-là.
* travailler sur les performances en basculant les traitements en multiprocessing (mais je crois que ça coince avec py2exe).

----

## Auteur

![Portait de Julien Moura](https://cdn.geotribu.fr/images/internal/contributeurs/jmou.jpg){: .img-rdp-news-thumb }
**Julien Moura**

Géographe qui s'est laissé gagner peu à peu par le côté géomatique de la Force. Intéressé par de nombreuses thématiques liées à l'urbain (ségrégation, environnement, risque et vulnérabilité, etc), j'aime bien l'idée de formaliser les pensées en les modélisant et en les automatisant au possible. A ce jeu là, les outils informatiques s'avèrent indispensables, en particulier Python et Javascript.
