---
title: "Non, MapServer, GeoServer, TileCache & co ne sont pas toujours nécessaires"
authors:
    - Arnaud VANDECASTEELE
categories:
    - article
comments: true
date: 2014-03-24
description: "Non, MapServer, GeoServer, TileCache & co ne sont pas toujours nécessaires"
tags:
    - webmapping
---

# Non, MapServer, GeoServer, TileCache & co ne sont pas toujours nécessaires

:calendar: Date de publication initiale : 24 mars 2014

Lors d'un récent projet, j'ai été amené à travailler sur une application cartographique dont les fondations avaient déjà été mises en place par le précédent développeur. En background on avait de l'usuel, à savoir [MapServer](http://mapserver.org/) et [TileCache](http://tilecache.org/). Ma première impression fût, bon c'est cool on est sur de l'habituel ça devrait rouler. Après une petite exploration du projet et au regard du mode d'utilisation, je me suis rendu compte qu'en fait ces deux composants étaient complètement inutiles. Sans être gênants, ils étaient surdimensionnés. C'était un peu comme avoir un bazooka pour tuer une mouche... Bon vous avez compris l'idée quoi.

 Après en avoir discuté avec le commanditaire du projet, celui-ci m'a fait part de sa surprise en me soulignant que nos tutoriaux mettaient justement en avant ce type d'architecture. C'est pourquoi il me paraît important de mettre au clair certaines pratiques afin d'éviter des situations similaires. Car oui, en fonction de votre besoin, vous pouvez faire une application cartographique avec comme seule application un serveur web !

----

Attardons-nous rapidement sur ce qui m'a amené à remettre en cause l'utilisation de MapServer & TileCache. Le projet ne contenait que deux cartes rasters, toutes les autres données étant stockées en base. Ces cartes rasters ne changeaient quasiment pas, ou alors une fois par an. Vous voyez où je veux en venir ? En fait, dans ce type de cas, il est bien plus simple de générer au préalable les différentes tuiles et les stocker ensuite sur votre serveur web plutôt que de mettre en place une véritable architecture cartographique.

Bien que l'utilisation de MapServer et de TileCache ne soit pas dans ce cas ni bonne, ni mauvaise, elle entraîne l'installation de différents composants qui sont autant de causes potentielles de dysfonctionnement de votre application ou de votre serveur. De plus, cela entraîne inévitablement une consommation inutile de ressources.

## Pré-génération de tuiles, comment ça fonctionne ?

Bon me direz-vous mais comment je fais alors pour mes données. T'inquiètes paupiette on y arrive. En fait, il existe des solutions très simples s'appuyant sur la pré-génération de tuiles. Ces tuiles correspondent à des morceaux de l'image qui seront automatiquement générés puis stockées dans des répertoires en fonction du niveau de zoom et de la position géographique reportée sur une grille. La dernière partie de cette phrase est importante car même si certains formats (ex: XYZ) laisse à penser qu'ils travaillent avec des coordonnées, en réalité ce n'est pas tout à fait le cas. En fait, l'étendue géographique est semblable à un immense tableau où les longitudes seraient les lignes et les latitudes les colonnes. En fonction du niveau de zoom, l'étendue cartographique est divisée en autant de cellules en fonction de la taille de la tuile (classiquement 256x256). Ainsi, avec ce système de pré-génération afficher une tuile revient au final à trouver la cellule correspondant à l'intersection entre une ligne et une colonne.

Il faut savoir que ce système fonctionne de manière pyramidale avec un nombre croissant de tuiles en fonction du niveau de zoom. Ce nombre est exponentiel, au début vous aurez assez peu de variation, mais le nombre de niveaux de zoom augmentant le nombre de tuiles va rapidement devenir très important. Pour un exemple concret, je vous propose de consulter [cet exemple](http://www.maptiler.org/google-maps-coordinates-tile-bounds-projection/). A chaque zoom, vous verrez les valeurs (x, y et z) changer.

![Pyramide de tuiles](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/TilePyramid.jpg "Pyramide de tuiles"){: .img-center loading=lazy }

Source de l'image : [Web Map Tile Services for Spatial Data Infrastructures: Management and Optimization](http://www.intechopen.com/books/cartography-a-tool-for-spatial-analysis/web-map-tile-services-for-spatial-data-infrastructures-management-and-optimization#F1)

|zoom | nombre de tuiles |
| :---------------: |:---------------:|
|0 | 1 tuile qui recouvre la terre entière |
|1 | 4 tuiles |
|2 | 16 tuiles |
|n | 2^2n  tuiles |
|12 | 16 777 216 tuiles |
|16 | 2^32 = 4 294 967 296 tuiles |
|17 | 17 179 869 184 tuiles |
|18 | 68 719 476 736 tuiles |
|19 | 274 877 906 944 tuiles |

Source du tableau : le [Wiki d'OSM](https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames#Zoom_levels)

### Tile Map Service

Cette manière de faire a été notamment popularisée par la spécification [Tile Map Service (TMS)](http://wiki.osgeo.org/wiki/Tile_Map_Service_Specification) définie par l'OSGEO. Par la suite, de nombreuses applications se sont appuyés sur cette spécification à l'exemple de [TileCache](http://tilecache.org/) ou encore [GeoWebache](http://geowebcache.org/). Si vous pré-générez vos tuiles avec un logiciel implémentant le standard TMS, vous obtiendrez en sortie une architecture de répertoires en 3 niveaux (z, x, y) dont la numérotation correspond à :

- Répertoire 1 = Zoom
    - Répertoir 1.1 = X (Longitude)
        - Répertoire 1.1.1 = Y (Latitude)

[![TMS Specification](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2014/Tms.png "TMS Specification"){: .img-center loading=lazy }](http://wiki.osgeo.org/wiki/Tile_Map_Service_Specification)

### XYZ

Si vous êtes un familier du GeoWeb, vous devez certainement vous dire que cette manière de faire ressemble étrangement à [l'approche XYZ](https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames) proposée notamment par Google, OpenStreetMap et compagnie. Et vous aurez raison, en fait il n'y a aucune réelle différence mise à l'origine de Y qui change. Avec TMS cette origine est calculée à partir du coin inférieur droit alors que celle-ci est calculée à partir du coin supérieur droit pour XYZ. Est-ce que ça fait une différence ? Honnêtement je n'en ai aucune idée !

![TMS/XYZ origine](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/tms_xyz_origine.png "TMS/XYZ origine"){: .img-center loading=lazy }

### Web Map Tile Service

Deux manières d'arriver au même résultat, mais avec une approche différente... Il n'en fallait pas plus pour qu'un besoin de standardisation se fasse sentir. L'[Open GeoSpatial Consortium](http://www.opengeospatial.org/) (OGC) a donc proposé un nouveau standard nommé [Web Map Tile Service](http://www.opengeospatial.org/standards/wmts) similaire dans son approche au [Web Map Service](http://www.opengeospatial.org/standards/wms). Pour plus d'info je vous suggère la lecture de [ce billet](http://georezo.net/wiki/main/standards/wmts) paru sur le site GeoRezo.

Bien que le standard WMTS soit une bonne chose du point de vue de la standardisation, on s'éloigne un peu de l'objectif initial de ce billet. En effet, offrir du WMTS nécessitera au préalable de disposer d'un serveur cartographique. Or, nous souhaitions disposer d'une architecture souple et surtout simple. C'est pourquoi la suite de ce billet sera consacrée aux formats TMS et XYZ.

## Pré-génération de tuiles, comment faire ?

Bon, arrêtons la théorie et passons à la pratique. Comment allons-nous faire pour pré-générer nos tuiles. Bien que différentes solutions existent, mon habitude de la ligne de commande et de Gdal me pousse naturellement vers le script [gdal2tiles](http://www.gdal.org/gdal2tiles.html). Dans sa forme la plus simple, il suffit d'appeler la commande avec en paramètre le fichier raster que l'on souhaite tuiler. Ce qui donne donc:

```bash
gdal2tiles monFichier.tif
```

Un nouveau répertoire du même nom que votre fichier sera alors automatiquement créé avec les tuiles pré-générées pour différents niveaux de zoom. Comme les choses sont bien faites, vous avez également un viewer s'appuyant sur Google Maps ou OpenLayers à votre disposition. Bien évidemment tout cela est paramétrable en ajoutant à votre ligne de commande différents paramètres. Je vous laisse pour cela le soin de [consulter la page du projet](http://www.gdal.org/gdal2tiles.html).

Bon j'entends déjà certains râler du fait que la ligne de commande c'est bien, mais bon... ça tombe mal j'ai rasé ma barbe aujourd'hui et je n'ai pas une collection de stickers sur mon ordi portable ! Ok, ok je vous vois venir. Si un bel écran noir vous rebute, sachez que vous pouvez également disposer d'une interface graphique. Pour cela il vous faudra télécharger et installer le logiciel [MapTiler](http://www.maptiler.org/) disponible sur Linux, Mac et Windows (vous remarquerez le classement par ordre d'importance :D). Les étapes sont simples et en quelques clics de souris vous disposerez de votre fichier de tuiles.

Au-delà de l'interface graphique, l'intérêt de MapTiler est également de vous laisser le choix entre le format XYZ et TMS. Sauf erreur de ma part, seul le format TMS est disponible avec gdal2tiles.

![MapTiler](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/MapTiler_2_0.jpg "MapTiler"){: .img-center loading=lazy }

### Afficher les tuiles générées sur une carte

Du fait de sa simplicité, l'utilisation de ce format s'est rapidement généralisée et de nombreuses bibliothèques cartographiques implémentent les méthodes nécessaires à l'affichage de tuiles. Pour illustrer cela, prenons l'exemple de Leaflet et d'OpenLayers.

Pour leaflet, [la classe](http://leafletjs.com/reference.html#tilelayer) permettant d'afficher une couche au format XYZ est :

```javascript
L.tileLayer('http://monURL/{z}/{x}/{y}.png', {  
    maxZoom: 18
}).addTo(map);
```

Pour info, il est également possible avec le même appel d'afficher une couche au format TMS. Mais l'option `tms=true` devra être alors spécifiée dans els paramètres de la couche.

OpenLayers dispose quant à elle d'une classe spécifique pour chaque format ([classe TMS](http://dev.openlayers.org/releases/OpenLayers-2.13.1/doc/apidocs/files/OpenLayers/Layer/TMS-js.html), [classe XYZ](http://dev.openlayers.org/releases/OpenLayers-2.13.1/doc/apidocs/files/OpenLayers/Layer/XYZ-js.html) et même au besoin la [classe WMTS](http://dev.openlayers.org/releases/OpenLayers-2.13.1/doc/apidocs/files/OpenLayers/Layer/WMTS-js.html)). Par exemple, l'appel d'un service TMS avec OpenLayers se fait de la manière suivante:

```javascript
var layer = new OpenLayers.Layer.TMS(
      "Ma couche TMS", // name for display in LayerSwitcher
      "http://monURL/",
      {layername: "leNomDeMaCouche", type: "png"}
);
```

## En conclusion

Voilà comment au final vous pouvez créer votre application cartographique sans pour autant avoir besoin d'installer de nombreuses librairies ou d'investir dans un serveur dédié. Bien évidemment, cela ne fonctionne que si vos données sont au format raster et surtout qu'elles sont statiques. Pour des données vecteurs il est toujours possible d'utiliser d'autres approches (ex : [TileMill](https://www.mapbox.com/tilemill/)) mais bon c'est une autre histoire.

----

<!-- geotribu:authors-block -->
