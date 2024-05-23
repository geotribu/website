---
title: 9. Superposer une carte à Google Maps avec génération préalable de tuiles
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-09-07
description: 9. Superposer une carte à Google Maps avec génération préalable de tuiles
tags:
    - Google Maps
    - mapcruncher
    - tuiles
---

# 9. Superposer une carte à Google Maps avec génération préalable de tuiles

:calendar: Date de publication initiale : 07 septembre 2008

:warning: L'API Google Maps v2 est dépréciée depuis le 19 mai 2010.

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-thumbnail-left }

Le but de ce tutoriel est de montrer la possibilité de superposer ses propres fonds cartographiques à la carte Google Maps. Pour ceci, il est d'abord nécessaire de 'construire' les tuiles pour ensuite les afficher sur la carte.  

## Génération des tuiles

Grâce au logiciel [MapCruncher](http://research.microsoft.com/en-us/um/redmond/projects/mapcruncher/) de Microsoft, il est possible de 'découper' une carte scannée selon différents niveaux de zoom.  

L'utilisation de ce logiciel est décrite dans la vidéo suivante :

[Video: 5 Minute Mapcruncher Tutorial](http://video.msn.com/video.aspx?vid=66a1094c-8490-4e30-b353-88332ba2fe47 "5 Minute Mapcruncher Tutorial")

Il convient alors de stocker les tuiles générées dans un répertoire sur votre serveur.  

## Initialisation de la carte

Reprendre la carte du [tutoriel n°2](2008-08-22_2-enrichir-la-carte-avec-des-boutons-et-des-controles.md) pour initialiser la carte.  

## Définition des fonctions

Afin d'afficher les tuiles, il faut définir une fonction qui 'reconstruise' leur URL définie par MapCruncher :  

```javascript
function TileToQuadKey (x, y, zoom){  
  var quad = "";  
  for (var i = zoom; i > 0; i--){  
    var mask = 1 << (i - 1);  
    var cell = 0;  
    if ((x & mask) != 0){  
      cell++;  
    }  
    if ((y & mask) != 0){  
      cell += 2;  
    }  
    quad += cell;  
  }  
  return quad;  
}
```  

Puis une fonction qui aille 'chercher' les noms des tuiles via cette méthode TileToQuadKey(x,y,zoom) :  

```javascript
var topoTiles = function (a,b) {  
var f = "./tile_files/" + TileToQuadKey(a.x,a.y,b) + ".png";  
return f;  
}
```

## Construction du layer

Il faut maintenant déclarer un objet GTileLayer en définissant les niveaux de zoom maxi et mini (correspondant aux niveaux demandés lors de la génération de tuiles avec MapCruncher) :  

```javascript
var topoLayer = new GTileLayer(new GCopyrightCollection(''),9,12);
```  

Puis définir les deux méthodes getTileUrl et isPng de l'objet topoLayer :

```javascript
topoLayer.getTileUrl = topoTiles;  
topoLayer.isPng = function() {return true;};
```  

Et définir un nouveau bouton de sélection de couche :  

```javascript
var topoMap = new GMapType([topoLayer], G_SATELLITE_MAP.getProjection(), "Topo",{errorMessage: "Pas de données ici !"});
```  

## Finalisation

Enfin enlevons les types 'SATELLITE' et 'HYBRID', sélectionnons la carte topo par défaut et ajoutons le bouton 'topo' :  

```javascript
map.addMapType(topoMap);  
map.removeMapType(G_HYBRID_MAP);  
map.removeMapType(G_SATELLITE_MAP);  
map.addControl(new GScaleControl());  
map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),12);  
map.setMapType(topoMap);  
map.enableScrollWheelZoom();
```  

### Code complet

```html
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <title>
    [Google Maps] 9. Superposer une carte à Google Maps
  </title>
  <style type="text/css">
  html { overflow:hidden; height:100%; }
  body { height:100%; margin:0; }
  #map { width:100%; height:100%; }
  </style>
  <link rel="icon" type="image/png" href="./favicon.png"/>
  <script src="http://maps.google.com/maps?file=api&v=2.x&key=votre_clé_ici" type="text/javascript"></script>
  <script type="text/javascript">

  function TileToQuadKey (x, y, zoom){
    var quad = "";
    for (var i = zoom; i > 0; i--){
      var mask = 1 << (i - 1);
      var cell = 0;
      if ((x & mask) != 0){
        cell++;
      }
      if ((y & mask) != 0){
        cell += 2;
      }
      quad += cell;
    }
    return quad;
  }

  function initialize() {
    if (GBrowserIsCompatible()) {
      var map = new GMap2(document.getElementById('map'));

      var topoTiles = function (a,b) {
        var f = "./tile_files/" + TileToQuadKey(a.x,a.y,b) + ".png";
        return f;
      }

      var topoLayer = new GTileLayer(new GCopyrightCollection(''),9,12);
      topoLayer.getTileUrl = topoTiles;
      topoLayer.isPng = function() {return true;};

      var topoMap = new GMapType([topoLayer], G_SATELLITE_MAP.getProjection(), "Topo",{errorMessage: "Pas de données ici !"});

      map.addMapType(topoMap);
      map.removeMapType(G_HYBRID_MAP);
      map.removeMapType(G_SATELLITE_MAP);
      map.addControl(new GScaleControl());
      map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),12);
      map.setMapType(topoMap);
      map.enableScrollWheelZoom();

    }
    else{
      alert('Désolé, mais votre navigateur n\'est pas compatible avec Google Maps');
    }
  }
</script>
</head>
<body onload="initialize()" onunload="GUnload()">
  <div id="map"></div>
</body>
</html>
```

## Démonstration

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="https://web.archive.org/web/20171110114935if_/http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto9.html" height="350px" width="100%">`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto9.html)

## Remarques

Toujours se référer à l'API Google Maps - [Google Maps API Reference](http://code.google.com/apis/maps/documentation/reference.html) pour les différentes classes, méthodes et options utilisées.
La carte est ici 'calée' et 'découpée' en tuiles grâce au logiciel [MapCruncher](http://research.microsoft.com/en-us/um/redmond/projects/mapcruncher/), mais il est possible d'utiliser le module [gdal2tiles](http://www.klokan.cz/projects/gdal2tiles/) des outils [GDAL](http://www.gdal.org/) ou d'utiliser le logiciel [MapTiler](http://www.maptiler.org/) qui sera l'interface graphique de gdal2tiles.

## Conclusion

Ce tutoriel décrit les étapes pour superposer un fond de carte dans Google Maps en générant des tuiles d'une carte préexistante via le logiciel MapCruncher. Celui-ci génère des tuiles selon un certain nombre de niveau de zoom et 'donne' un nom de fichier aux tuiles générées facilement exploitable. La superposition de fonds de carte via la classe GTileLayer peut être utilisée pour des fonds de carte fixe. Pour des données 'dynamiques', il sera alors préférable d'utiliser un serveur cartographique (MapServer ou GeoServer et TileCache). Cette méthode demande un serveur robuste pour répondre aux requêtes. Je me suis fortement inspiré de ce [site](http://www.bdcc.co.uk/GoogleCrunch/Crunch.htm) pour produire ce tutoriel.

----

<!-- geotribu:authors-block -->
