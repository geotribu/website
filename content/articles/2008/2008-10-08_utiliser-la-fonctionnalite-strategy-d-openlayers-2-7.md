---
title: Utiliser la fonctionnalité Strategy d'OpenLayers 2.7
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-10-08
description: Utiliser la fonctionnalité Strategy d'OpenLayers 2.7
tags:
    - OpenLayers
    - strategy
---

# Utiliser la fonctionnalité Strategy d'OpenLayers 2.7

:calendar: Date de publication initiale : 08 octobre 2008

## Introduction

L'une des grandes nouveautés d'OpenLayers 2.7 est la possibilité de définir un comportement particulier pour une couche vecteur (WFS, GML...) lors de la réception du flux de données. Cela se passe au moyen de la class "[strategy](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Strategy-js.html "obj strategy")". Celle-ci doit être utilisée conjointement à l'une des quatres sous"-classes" suivantes :

- [BBOX](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Strategy/BBOX-js.html) - Seuls les objets vecteur contenus dans l'extention géographique de la vue sont affichés
- [Cluster](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Strategy/Cluster-js.html) - Les objets vecteur spatialement proche sont regroupés afin d'apporter une meilleure visibilité
- [Fixed](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Strategy/Fixed-js.htm) - La requête éffectuée vers le serveur ne se fait qu'une seule fois. Il n'y a pas de rechargement de la couche après, par exemple, un déplacement, zoom...
- [Paging](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Strategy/Paging-js.html) - Les objets vecteur ne sont pas tous affichés mais disponible sous la forme d'un slideshow.

Comme à son habitude, les créateurs de cette librairie ont pensé à tout et ont également fourni un certains nombes d'exemples :

- [Cluster strategy](http://openlayers.org/dev/examples/strategy-cluster.html)
- [Paging strategy](http://openlayers.org/dev/examples/strategy-paging.html)
- [BBOX stategy](http://openlayers.org/dev/examples/strategy-bbox.html)
- [Fixed strategy](http://openlayers.org/dev/examples/behavior-fixed-http-gml.html)

Ce tutoriel est une mise en application de cette classe strategy. Nous utiliserons pour cela deux flux de données, un GML et l'autre WFS.

## Mise en application de strategy.Cluster pour une couche GML

L'exemple ci-dessous s'appuit sur un fichier de points générés aléatoireement puis exporter au format GML et SHP depuis GRASS. Nous allons à partir de là, utiliser la classe strategy.Cluster pour automatiquement regrouper les points adjacents et former un cercle de rayon plus important.

Bien entendu nous allons nous appuyer sur la classe strategy.Cluster pour y arriver, mais l'astuce, pour faire varier la taille des cercles, consiste à utiliser l'attibut **pointRadius** de la classe [Style](http://dev.openlayers.org/releases/OpenLayers-2.6/doc/apidocs/files/OpenLayers/Style-js.html). Dans le cas ci-dessous nous allons simplement utiliser un fichier GML qui contient l'ensemble de nos points :

```javascript
var GMLstyle = new OpenLayers.Style({  
  pointRadius: "${radius}",  
  fillColor: "#ffcc66",  
  fillOpacity: 0.8,  
  strokeColor: "#ff0000",  
  strokeWidth: 2,  
  strokeOpacity: 0.3  
}, {  
  context: {  
    radius: function(feature) {  
      return Math.min(feature.attributes.count,7) + 4;  
    }  
  }  
});

GML = new OpenLayers.Layer.Vector("GML",  
{  
  strategies:[  
    new OpenLayers.Strategy.Fixed(),  
    new OpenLayers.Strategy.Cluster()  
  ],  
  protocol: new OpenLayers.Protocol.HTTP({  
    url: "../data/poi_random/gml/random_poi.gml",  
    format: new OpenLayers.Format.GML()  
  }),  
  styleMap:new OpenLayers.StyleMap({  
    "default": GMLstyle, // Utilisation du style GMLstyle  
    "select": { // Style particulier lors de la selection  
      fillColor: "#8aeeef",  
      strokeColor: "#32a8a9"  
    }  
  })  
}  
);  
```

Et voilà, sous vos yeux ébahis devrait alors s'afficher vos points automatiquement regroupés en fonction de leur distance (en pixel) avec les points voisins. Vous pouvez, évidemment, faire varier la distance maximale de recherche de points voisins (par défaut 20 px). Cela se passe grace à la propriété [distance](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Strategy/Cluster-js.html#OpenLayers.Strategy.Cluster.distance) :

```javascript
strategyCluster = new OpenLayers.Strategy.Cluster();  
strategyCluster.distance = 50;
```

## Mise en application de strategy.Cluster pour une couche WFS

Je pensais au départ pouvoir utiliser strategy.Cluster directement depuis la classe standards layers [WFS](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Layer/WFS-js.html) d'Openlayers qui hérite pourtant de la classe layer [vector](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Layer/Vector-js.html). Malheureusement cela semble impossible. Il faut pour cela "redescendre d'un niveau" et utiliser directement la classe layer vector en spécifiant le protocole corrspondant. Cela se fait de la manière suivante :

```javascript
var WFSstyle = new OpenLayers.Style({  
  pointRadius: "${radius}",  
  fillColor: "#71FF00",  
  fillOpacity: 0.5,  
  strokeColor: "#000",  
  strokeWidth: 2,  
  strokeOpacity: 0.3  
}, {  
  context: {  
    radius: function(feature) {  
      return Math.min(feature.attributes.count,7) + 4;  
    }  
  }  
});

wfs = new OpenLayers.Layer.Vector("WFS",  
{  
  strategies: [  
    new OpenLayers.Strategy.Fixed(),  
    new OpenLayers.Strategy.Cluster()  
  ],  
  protocol: new OpenLayers.Protocol.HTTP({  
    url: "http://localhost/cgi-bin/mapserv?map=/var/www/html/data/random_poi.map",  
    params: {  
      format: "WFS",  
      service: "WFS",  
      request: "GetFeature",  
      srs: "EPSG:4326",  
      VERSION : "1.0.0",  
      typename : 'Random_POI'  
    },  
    format: new OpenLayers.Format.GML()  
  }),  
  styleMap:new OpenLayers.StyleMap({  
    "default": WFSstyle,  
    "select": {  
      fillColor: "#8aeeef",  
      strokeColor: "#32a8a9"  
    }  
  })  
  ,  
  {  
    extractAttributes:true,  
    displayInLayerSwitcher: true  
  });  
```

Voici un exemple concret de ce qu'il est possible de réaliser :

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/openlayers/random_poi/random_poi.html" width="100%" height="700px"></iframe>`

----

<!-- geotribu:authors-block -->
