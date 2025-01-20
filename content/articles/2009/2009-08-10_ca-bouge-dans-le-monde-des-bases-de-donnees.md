---
title: "Ça bouge dans le monde des bases de données"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-08-10
description: "Ça bouge dans le monde des bases de données"
tags:
    - database
    - licence
    - open source
---

# Ça bouge dans le monde des bases de données

:calendar: Date de publication initiale : 10 août 2009

![icone database](https://cdn.geotribu.fr/img/logos-icones/programmation/database.png "icone database"){: .img-thumbnail-left }

Plus qu'une véritable news, ce billet retrace les différentes évolutions qui ont eu lieu dans le monde des bases de données spatiales ces dernières semaines. En effet, en un laps de temps très court, plusieurs informations majeures ont été annoncées. Nous aborderons succesivement spatialite, la nouvelle version de postgis et enfin Rasdaman.

## SpatiaLite en version 2.3.1

Commençons tout d'abord par spatialite qui permet au moteur [SQLite](http://www.sqlite.org/) de gérer les objets spatiaux (comparable à posgis pour postgresql). Le moteur SQLite, remarquable par sa taille (le code précompilé pèse entre 200 et 600 Ko source : [01netPro](http://pro.01net.com/editorial/372465/sqlite-devient-la-base-de-donnees-standard-du-web-deconnecte/)) l'est également par son mode de fonctionnement. En effet, ce dernier ne se base pas sur l'habituel paradigme client/serveur mais sur une bibliothèque de fonctions directement appelées par l'application (plus d'informations sur [Wikipedia](https://fr.wikipedia.org/wiki/SQLite)). Ses caractéristiques qui en font la base de données idéale pour les applications légères embarquées ont déjà séduit des grands noms de l'informatique tels que Google, Adobe ou encore Mozilla.  
Ainsi, à l'heure du "tout spatial", il était obligatoire pour une bibliothèque de cette qualité de gérer les objets géographiques. Gestion qui, comme nous l'avons vu précédemment, est assurée par Spatialite. Une nouvelle version (2.3.1) est disponible depuis peu. Les modifications portent notamment sur :

* le support de SQLite en version 3.6.16 et GEOS en version 3.1.1
* l'ajout de trois nouvelles fonctions d'administration `spatialite_version()`,`proj4_version()` et `geos_version()`
* l'ajout des fonctions `IsTiffBlob()` et `IsWaveletBlob()` (compatibilité avec RasterLite)
* le support du type 'F' (flottant) pour les .DBF (pour les fichiers Shape)
* la gestion des données raster grâce à RasterLite qui permet notamment le tuilage et la gestion des couches pyramidales
* Corrections de bugs...

Si vous souhaitez en connaitre d'avantage sur SpatiaLite et RasterLite, je vous invite à consulter le [tutoriel](http://www.bostongis.com/PrinterFriendly.aspx?content_name=spatialite_tut01) mis en ligne par [BostonGis](http://www.bostongis.com/) ou encore la [documentation officielle](http://www.gaia-gis.it/spatialite/docs.html).

### PostGis en version 1.4

Si il est une base de données qui n'est plus à présenter c'est bien [Postgresql](http://www.postgresql.org/) et sa cartouche spatiale [PostGis](http://postgis.refractions.net/). Elle est de par sa puissance et ses capacités l'équivalente libre de [Oracle](https://fr.wikipedia.org/wiki/Oracle_Database) et [Oracle Spatial](http://www.oracle.com/technology/products/spatial/index.html). Une nouvelle version de PostGis (1.4) est disponible, celle-ci apporte notamment :

* l'externalisation des librairies "coeur" (auparavant codées directement dans postgis) dans le fichier `liblwgeom`
* une amélioration des performances pour toutes les fonctions d'agrégation
* le support de la prochaine version de postgresql (8.4)
* l'amélioration de nombreuses fonctions telle que `ST_Union()`, `ST_Intersects()`, `ST_Contains()`, `ST_Within()`...
* l'enrichissement et amélioration de la documentation
* des corrections de bugs...

La liste complète des modifications et améliorations apportées est disponible sur le [Blog de PostGis](http://www.postgresonline.com/journal/index.php?/archives/128-PostGIS-1.4-is-finally-out-and-other-news.html).

Passons maintenant à un peu de littérature avec le livre "[PostGis in Action](http://www.manning.com/obe/)" dont la première mouture est prévu pour Fevrier 2010. Pourquoi en parler si tôt? Tout simplement du fait que vous êtes invités à commenter, améliorer les écrits de l'auteur ou encore à suggérer de nouvelles idées sur le [forum](http://www.manning-sandbox.com/forum.jspa?forumID=565) qui lui est dédié. C'est la première fois pour ma part que je rencontre ce concept de communauté poussé aussi loin. Le [premier chapitre](http://www.manning.com/obe/PostGIS_MEAPCH01.pdf) du livre est dors et déjà librement disponible.

J'anticipe également sur le paragraphe suivant en présentant un projet récent (janvier 2009), [WKTRaster](http://trac.osgeo.org/postgis/wiki/WKTRaster) dont le but est de permettre à PostGis de gérer les couches raster. Cette gestion prendra la forme d'un nouvel objet géographique nommé RASTER. En plus d'assurer le stockage de tuiles il sera également possible d'effectuer de multiples opérations (Clip, Reclass, Union, Contains...) aussi bien sur les couches raster elles-mêmes que sur les couches vecteurs. **C'est en tout cas un projet à surveiller de très près**.

### Rasdaman

Conjointement développé depuis plusieurs années par la [Jacobs University Bremen](https://fr.wikipedia.org/wiki/Jacobs_University_Bremen) (Allemagne) et rasdaman GmbH, [Rasdaman](http://www.rasdaman.org/) est désormais disponible en licence [GPL V3](https://fr.wikipedia.org/wiki/Licence_publique_g%C3%A9n%C3%A9rale_GNU) et en licence propriétaire. Celui-ci, tout comme WKTRaster, permet de gérer les objets rasters et il possède également un langage de requêtage.

N'ayant qu'une vision très vague de Rasdaman et WKTraster, il m'est difficile de privilégier l'un ou l'autre. Logiquement Rasdaman, développé depuis plus longtemps, devrait être plus stable et plus avancé technologiquement. Néanmoins, de mes premières lectures du futur WKTraster, j'avoue être passablement séduit par la gestion des raster comme un objet PostGis à part entière.

**Qui des deux survivra?**

Comme je vous le disais en préambule, beaucoup de changements ont eu lieu. Reste maintenant à tester toutes ces nouvelles fonctionnalités !

----

<!-- geotribu:authors-block -->
