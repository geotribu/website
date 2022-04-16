---
authors:
- GeoTribu
categories:
- article
date: 2009-08-28 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- Open Source
- SIG
- QGIS
title: A la découverte de QGIS
---

# A la découverte de QGIS


:calendar: Date de publication initiale : 28 août 2009


----

![qgis.png](http://geotribu.net/sites/default/files/Tuto/img/Blog/qgis/qgis.png)Après avoir successivement découvert [PuzzleGis](http://geotribu.net/node/117), [OpenJump](http://geotribu.net/node/120) et [UDIG](http://geotribu.net/node/126) nous allons nous attaquer à un des poids lourds du monde de la géomatique OpenSource, [QGIS](http://www.qgis.org/). Son histoire commence en 2002 sous l'impulsion de Gary Sherman qui souhaitait pouvoir disposer d'un viewer SIG sur Linux. Cinq ans plus tard, ce projet désormais soutenu par l'[OSGEO](http://www.osgeo.org/qgis) a considérablement évolué et propose des fonctionnalités proches des SIG commerciaux tout en étant utilisable sur la grande majorité des plates-formes (Windows, Mac, Linux...).


### Téléchargement et installation


Conçu au départ pour Linux, QGIS est disponible dans la plupart des dépôts. De plus, sur la page de [téléchargement](http://www.qgis.org/en/download/binaries.html) vous pourrez trouver la version Windows et Mac OS X. Pour ma part je n'ai rencontré aucune difficulté lors de l'installation, un simple "apt-get" a suffi.


![qgis_logo_kore.jpg](/sites/default/files/Tuto/img/qgis/qgis_logo_kore.jpg)


### Découverte de l'interface


L'interface de QGIS, complètement **francisée**, est basée sur un concept de modularité. En effet, chacun des éléments peut être déplacé, détaché, agrandi, rétréci ou même caché. Cela permet ainsi de construire l'interface que l'on désire.


![qgis_interface.png](http://geotribu.net/sites/default/files/Tuto/img/qgis/qgis_interface.png)


De plus il est possible de changer facilement le thème des icônes. L'image ci-dessous utilise le thème gis :


![theme_gis.png](/sites/default/files/Tuto/img/qgis/theme_gis.png)


### Accès aux données


Bien que conçu au départ comme un simple viewer pour PostGis, QGIS a su s'appuyer sur la librairie [GDAL-OGR](http://www.gdal.org/) afin d'étoffer considérablement la liste des formats de données accessibles en lecture et/ou écriture.


Au niveau des [vecteurs](http://www.gdal.org/ogr/ogr_formats.html) cette liste compte près d'une trentaine de formats dont notamment : ESRI Shapefile, FMEObjects Gateway, Mapinfo File, Oracle Spatial, PostgreSQL, SQLite, WFS...


Au niveau des [rasters](http://www.gdal.org/formats_list.html) la liste est bien plus longue puisqu'elle compte plus d'une cinquantaine de formats dont notamment : Arc/Info ASCII Grid, ECW, TIFF, GeoTIFF,OGC WCS et WMS, USGS SDTS DEM ...


À ma connaissance et comparativement aux logiciels précédemment testés, QGIS est le seul permettant l'accès à une telle quantité de sources de données. À l'utilisation, cette souplesse est vraiment agréable car il n'est plus nécessaire de devoir convertir des données dans tel ou tel format avant de pouvoir les consulter.


Cette souplesse se retrouve également au niveau de l'export des données. Il est en effet possible de convertir ces dernières en utilisant l'outil mis à disposition par QGIS.


![convertisseur.png](/sites/default/files/Tuto/img/qgis/convertisseur.png)


### Modification du style des couches


Le style des couches peut être facilement modifié (couleur de fond ou des bords, la taille des lignes...) il est même possible de réaliser des analyses thématiques et de jouer sur la transparence. Les styles créés peuvent être également sauvegardés en vue d'une utilisation ultérieure.


![style_layer.png](/sites/default/files/Tuto/img/qgis/style_layer.png)


### Interrogation des données


Si dans les dernières versions les possibilités de requêtes spatiales étaient très limitées, le plugin [ftools](http://www.ftools.ca/) et GeoProcessing permettent de combler ce manque. Les fonctionnalités spatiales restent néanmoins très limitées.


![select_spatial.png](/sites/default/files/Tuto/img/qgis/select_spatial.png)


Par contre, la sélection attributaire fonctionne parfaitement. QGIS propose pour cela deux modes de fonctionnement. Soit une recherche rapide directement depuis la table attributaire ou alors un éditeur facilitant la création des requêtes. J'aime particulièrement le fait qu'il soit possible d'afficher un échantillon des valeurs contenues dans la table. Néanmoins, le fait de devoir à chaque fois ouvrir la table attributaire pour effectuer une requête devient très vite agaçant surtout si celle-ci contient un gros volume de données. C'est pourquoi je vous conseille d'installer le plugin **FindByAttributes** qui ajoute un menu de recherche à l'interface.


![select_attr.png](/sites/default/files/Tuto/img/qgis/select_attr.png)


Pour réaliser des sélections en dessinant directement sur la carte, je vous conseille le plugin **SelectPlus**. Celui-ci permet d'effectuer des recherches en dessinant à main levée, en créant un cercle ou un polygone ou encore d'inverser une sélection.


Si QGIS dispose d'un éventail de fonctionnalités permettant la sélection d'objets il reste tout de même à améliorer la partie spatiale. Je n'ai en effet pas trouvé de fonctions spatiales telles que le proposent les éditeurs de logiciels propriétaires ou encore OpenJump. Il est néanmoins possible de passer par PostGis ou Grass pour cela, mais cela nécessite de convertir nos données au format adéquat.


### Édition et modification des objets


QGIS autorise aussi bien la modification de la géométrie que celle des attributs des objets géographiques. L'outil de mise à jour géométrique bien qu'un peu moins riche que celui d'OpenJump reste tout de même très fonctionnel.  

Il est ainsi possible de créer des îles, de déplacer ou supprimer des sommets ou encore de couper des objets. Les options de digitalisation peuvent être modifiées afin de définir par exemple le mode d'accrochage par défaut. Seul petit bémol si à grande échelle l'affichage des sommets se justifie il en est tout autrement lorsque la vue est globale. Cela contribue à alourdir et ralentir l'application.


![edition.png](/sites/default/files/Tuto/img/qgis/edition.png)


### Les petits plus de QGIS


En comparaison à OpenJump ou UDig les fonctionnalités de QGIS semblent moins riches au premier abord. Mais, une fois certains plugins clés installés, ces fonctionnalités s'étoffent considérablement. Cet aspect est l'un des points forts de QGIS qui propose depuis la version 1.0 une API permettant à tout un chacun de développer les améliorations qui l'intéresse.


![plugin.png](/sites/default/files/Tuto/img/qgis/plugin.png)


La liste des plugins est longue, certains sont inclus directement dans QGIS d'autres téléchargeables à partir du gestionnaire d'extension. Ces plugins permettent par exemple d'utiliser une grande partie des fonctions de Grass (image ci-dessous), de modifier la structure (titre des colonnes, suppression des colonnes...) d'une table shapefile ou encore d'exporter la carte courante au format mapfile (mapserver).


![grass_0.png](/sites/default/files/Tuto/img/qgis/grass_0.png)


### Conclusion


Bien qu'un peu moins riche en fonctionnalités que UDIG ou OpenJump, QGIS garde ma préférence. J'aime la possibilité qu'il offre de pouvoir lire facilement autant de formats vecteurs et/ou rasters ainsi que son interface claire et modulable. Enfin, la version 1.0 avec la publication d'une API stable a permis d'agrandir considérablement la communauté de développeur offrant ainsi une large gamme de plugins a intégrer selon ses besoins.




----

## Auteur

--8<-- "content/toc_nav_ignored/snippets/authors/geotribu.md"
