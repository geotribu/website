---
title: Afficher le nombre d'éléments dans un Cluster Strategy
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2009-02-07
description: Afficher le nombre d'éléments dans un Cluster Strategy
tags:
    - cluster
    - OpenLayers
    - strategy
---

# Afficher le nombre d'éléments dans un Cluster Strategy

:calendar: Date de publication initiale : 07 février 2009

## Introduction

![logo OpenLayers](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/openlayers.png "logo OpenLayers"){: .img-thumbnail-left }

Une des grandes améliorations de la version 2.7 d'OpenLayers était la possibilité de pouvoir "jouer" avec les données vecteurs avant même leur affichage. Cette fonctionnalité nommée Strategy propose 4 types d'actions : BBOX, Cluster, Fixed, pagging. Pour un aperçu rapide vous pouvez consulter ce [précédent tutoriel](http://geotribu.net/node/47) dont les bases sont d'ailleurs reprises dans celui-ci.

Nous allons nous attarder sur la méthode [Strategy.Cluster](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Strategy/Cluster-js.html), qui permet avant même leur chargement de regrouper les données en fonction de l'échelle en cours. Dans le tutoriel cité précédemment nous avons joué sur la taille des cercles afin de définir le nombre d'entité regroupé. Nous allons maintenant ajouter grâce à la [librairie PHP GD](http://fr.php.net/gd) le nombre d'entité regroupé à l'intérieur de ces cercles.

## Afficher le nombre d'entités agglomérées

La logique de fonctionnement est simple, en effet la classe [Layer.Vector](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Layer/Vector-js.html) propose un attribut [style](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Feature/Vector-js.html#OpenLayers.Feature.Vector.style) dans lequel il est possible de définir l'URL de l'image à utiliser. Dans notre cas, cela ne sera pas une image simple mais un script PHP qui renvoie une image.

Concrètement en javaScript cela se passe de la manière suivante, la propriété `externalGraphic` a pour valeur une fonction pointant vers un fichier PHP nommé `custom_cluster.php` Dans ce dernier nous passons deux paramètres : `numCluster` et `size` :

```javascript
var GMLstyle = new OpenLayers.Style({
 pointRadius: "${radius}",
 fillColor: "#ffcc66",
 fillOpacity: 0.8,
 strokeColor: "#ff0000",
 strokeWidth: 2,
 strokeOpacity: 0.3,
 externalGraphic: "${getChartURL}"  
      }, {
 context: {
   radius: function(feature) {  
     var minV = 1;
     var maxV = 10;
     var minR =  5;
     var maxR = 50;
     surf = Math.round(
               minR+((maxR-minR)*((feature.attributes.count-minV)/(maxV-minV)))
            );  
            return surf;
 },
          //Fonction qui interroge le script PHP
   getChartURL: function(feature) {
     var charturl = 'http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/openlayers/
                       cluster_count/custom_cluster.php?numCluster='+feature.attributes.count+'&size='+surf;
     return charturl;
 } // End of function getChartURL
      }
});

GML = new OpenLayers.Layer.Vector(
 "GML", {
 strategies:[
  new OpenLayers.Strategy.Fixed(),
  new OpenLayers.Strategy.Cluster()
 ],
 protocol: new OpenLayers.Protocol.HTTP({
  url: "../random_poi/poi_random/gml/random_poi.gml",
  format: new OpenLayers.Format.GML()
 }),
 styleMap:new OpenLayers.StyleMap({
  "default": GMLstyle,
  "select": {
     fillColor: "red",
     strokeColor: "red"
  }
        })
});
```

Le code PHP utilise la librairie GD pour générer une image en fonction des paramètres que nous avons passé dans l'URL :

```javascript
//Get Paramz
 $getNumCluster = $_GET["numCluster"];
 $getSize  = $_GET["size"]*3;
 // create Obj image
 $image = imagecreatetruecolor($getSize,$getSize);
 // allocate some solors
 $white  = imagecolorallocate($image, 255, 255, 255);
 $red    = imagecolorallocate($image, 0, 0, 0);
 $orange = imagecolorallocate($image, 241, 90, 36);
 $orangeDark = imagecolorallocate($image, 178, 56, 18);
 $black  = imagecolorallocate($image, 0, 0, 0);
 //Border of the Circle
 imagefilledarc($image, $getSize/2, $getSize/2, $getSize-3, $getSize-3, 0, 360 , $orangeDark, IMG_ARC_PIE);
 //Fill Circle
 imagefilledarc($image, $getSize/2, $getSize/2, $getSize-8, $getSize-8, 0, 360 , $orange, IMG_ARC_PIE);
 //Text in the circle
 if($getNumCluster>1){
  //We must Calculate the BBOX of the text to align it with the img
  $bbox = imagettfbbox($getSize/2, 0, './arialbi.ttf', $getNumCluster);
  $x = $bbox[2]+$bbox[0];
  $y = $bbox[7]-$bbox[1];
  //Final Center position
  $xPos = imagesx($image)/2-$x/2;
  $yPos = imagesy($image)/2-$y/2;
  //Obj Text
  imagettftext($image,$getSize/2,0,$xPos,$yPos,$white,'./arialbi.ttf',$getNumCluster);
 }
 imagecolortransparent($image, $black);
 // flush image
 header('Content-type: image/png');
 imagepng($image);
 imagedestroy($image);
```

Et voilà, rien de plus compliqué. Le résultat de ces deux scripts est visible ci-dessous.

## Exemple

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/openlayers/cluster_count/clusterCount.html" height="600px" width="600px"></iframe>`

----

<!-- geotribu:authors-block -->
