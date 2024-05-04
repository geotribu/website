---
title: Afficher les infos d'une couche WFS dans un popup
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2009-01-24
description: Afficher les infos d'une couche WFS dans un popup
tags:
    - OpenLayers
    - WFS
    - popup
---

# Afficher les infos d'une couche WFS dans un popup

:calendar: Date de publication initiale : 24 janvier 2009

## Introduction

![logo OpenLayers](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/openlayers.png "logo OpenLayers"){: .img-thumbnail-left }

L'API d'OpenLayers permet d'afficher une couche WFS ainsi que les données attributaires qui lui sont rattachées. Même si cela n'est pas très compliqué à réaliser il existe certaines subtilités.

## La couche WFS

L'affichage d'une couche [WFS depuis OpenLayers](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Layer/WFS-js.html "API OpenLayers WFS") se fait comme n'importe qu'elle autre couche à ceci prêt que nous allons, pour les besoins de ce tutoriel, spécifier un attribut supplémentaire qu'est `extractAttributes`. Celui-ci est optionnel mais il permet de parser le flux WFS afin d'extraire les données attributaires. A noter que cela ralentit le traitement cartographique.

```javascript
var africaWFS = new OpenLayers.Layer.WFS(
   "Africa WFS",
   "http://pathToMapServ/mapserv?map=/pathToYourMapFile/africa.map&",
   {typename: 'Africa'},
   {style: fStyle, extractAttributes: true}
 );
```

Bien entendu il est nécessaire que votre moteur cartographique soit configuré pour envoyer des données attributaires. Dans le cas de MapServer n'oubliez pas de définir pour vos couches les paramètres `DUMP` et `gml_include_items` (voir [MapServer WFS](http://mapserver.org/ogc/wfs_server.html "MapServer WFS"))

```conf
LAYER
 NAME Africa
 STATUS ON
 METADATA
  ### WMS
  "wms_title"    "Africa"
  ### WFS
  "wfs_title"    "Africa"
      "gml_featureid" "NAME"
      "gml_include_items" "all"
 END
 PROJECTION
  "init=epsg:4326"
 END
 DUMP TRUE
 TYPE POLYGON
 STATUS ON
 DATA africa
 CLASS
  COLOR 217 217 217
  OUTLINECOLOR 0 0 0
 END
```

## Extraire les données attributaires

Pour accéder aux données d'une couche WFS vous devez spécifier la propriété `attributes` suivi du nom de la balise XML que vous souhaitez afficher (qui est égal à son nom dans la table attributaire mais en majuscule). Par exemple si dans votre flux il existe une valeur "NAME" pour l'afficher vous devrez faire `monObjetWFS.attributes.NAME`

Enfin, en toute logique votre PopUp se déclenchera sur une action (cf [selectFeature](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Control/SelectFeature-js.html)). Dans ce cas, la fonction à laquelle renvoie le listener inclut directement l'objet WFS. C'est un peu confus à expliquer mais vous comprendrez mieux dans l'exemple ci-dessous :

```javascript
function init() {
    /*
     * Some code before
     */
    // Instanciation du control selectFeature
    options = {  
         hover: false,
         // Fait reference a la fonction popUp
         onSelect: popUP,
         selectStyle :feature_style
    };  
    sf = new OpenLayers.Control.SelectFeature(africaWFS, options)
    map.addControl(sf);
    sf.activate();
}

function popUP(e) {
   // Je verifie qu'aucun popup n'existe deja
   if(typeof popup!='undefined'){
         popup.destroy();
    }
    //je definis les params de mon popup
    var htmlContent = "<b>Pays : "+e.attributes.NAME+"</b><br /> <b><i>Region : "+e.attributes.REGION+"</b></i>";  
    var size = new OpenLayers.Size(20,34);
    var offset = new OpenLayers.Pixel(-(size.w/2), -size.h);
    //j'instancie mon popup
    popup = new OpenLayers.Popup.FramedCloud(
         e.fid,
         e.geometry.getBounds().getCenterLonLat(),
         null,
         htmlContent,
         null,
         false,
          null
    );
    //Je l'ajoute a la carte
    map.addPopup(popup);  
}  
```

## Exemple

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/openlayers/popup/popup_wfs.htm" height="600px" width="600px"></iframe>`

----

<!-- geotribu:authors-block -->
