---
title: "Hillshading or not ..."
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-11-24
description: "Hillshading or not ..."
tags:
    - Google Maps
    - hillshading
    - OpenStreetMap
    - ombrage
---

# Hillshading or not

:calendar: Date de publication initiale : 24 novembre 2010

![Imagimap Hillshading](https://cdn.geotribu.fr/img/logos-icones/divers/imagimap.png){: .img-thumbnail-left }

Vous reprendrez bien un peu d'ombrage ... Je trouve les rendus OSM ou Google Maps un peu trop lisse à mon goût.  
Par contre, j'aime bien le relief que propose la vue TERRAIN de Google ; alors comment concilier les rendus Mapnik et Google Maps normal avec de l'ombrage ?

Pour cela, nous avons utilisé les bibliothèques [ExtJS](http://www.sencha.com/products/js/), [GeoExt](http://www.geoext.org/) et [OpenLayers](https://openlayers.org/) pour avoir une mise en page sympathique des 4 cartes. Une synchronisation a été mise en place afin d'avoir une vue simultanée sur chacune.  
L'ombrage a quant à lui été ajouté à la carto en utilisant la classe [Layer TMS](http://dev.openlayers.org/releases/OpenLayers-2.10/doc/apidocs/files/OpenLayers/Layer/TMS-js.html) d'OpenLayers et d'une fonction de récupération d'URL :  

```javascript
function osm_getTileURL(bounds) {
 var res = this.map.getResolution();
 var x = Math.round((bounds.left - this.maxExtent.left) / (res * this.tileSize.w));
 var y = Math.round((this.maxExtent.top - bounds.top) / (res * this.tileSize.h));
 var z = this.map.getZoom();
 var limit = Math.pow(2, z);

 if (y < 0 || y >= limit) {
  return OpenLayers.Util.getImagesLocation() + "404.png";
 } else {
  x = ((x % limit) + limit) % limit;
  return this.url + z + "/" + x + "/" + y + "." + this.type;
 }
}
```

Les tuiles nous ont été fournies par [Hike & Bike Map](http://hikebikemap.de/). Merci à [Colin](https://www.openstreetmap.org/user/ColinMarquardt) !

[![Hillshading](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/hillshading_imagimap.png "Hillshading"){: .img-center loading=lazy }](http://geotribu.net/applications/hillshading/)

Cliquez sur l'image pour lancer l'application :-)

----

<!-- geotribu:authors-block -->
