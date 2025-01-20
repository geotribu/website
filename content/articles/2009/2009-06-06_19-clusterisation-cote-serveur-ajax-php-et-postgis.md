---
title: 19. Clusterisation côté serveur - Ajax, PHP et PostGIS
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2009-06-06
description: 19. Clusterisation côté serveur - Ajax, PHP et PostGIS
tags:
    - Ajax
    - cluster
    - clusterisation
    - Google Maps
    - PHP
    - PostGIS
    - serveur
---

# 19. Clusterisation côté serveur - Ajax, PHP et PostGIS

:calendar: Date de publication initiale : 06 juin 2009

## Introduction

Les solutions de clusterisation pour afficher un grand nombre d'objets sont peu nombreuses et parfois même payantes :

* <http://maps.forum.nu/server_side_clusterer/>
* <http://googlemapsapi.martinpearman.co.uk/infusions/google_maps_api/google_maps_api.php>
* <http://www.geocubes.com/>
* <http://www.maptimize.com/>

Nous allons voir dans ce tutoriel comment produire notre propre solution de clusterisation.

## Comment faire ?

Avant de se lancer dans le développement, je vais essayer de vous expliquer le processus mis en oeuvre afin de clusteriser des éléments stockés en base de données.

### Découpage de la carte

Pour clusteriser les données, nous allons découper la carte visible à l'écran (plus un petit peu sur les côtés) en un certain nombre de 'petites' cartes - la carte centrale correspond à la partie visible (le navigateur de l'internaute n'affichera que cette partie centrale).  

Le but étant de charger les marqueurs qui sont proches des bords de la carte, afin de fluidifier l'application.

![Découpage de la carte](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/cluster_1.png "Découpage de la carte"){: .img-center loading=lazy }

### Processus

Le but est de calculer pour chaque 'petite' carte le nombre de marqueurs qu'elle comporte.  

Il est nécessaire de définir un nombre à partir duquel nous afficherons un marqueur qui invitera à zoomer (et indiquera le nombre d'éléments contenu dans la 'petite' carte). Si il y a moins de marqueur que ce nombre prédéfini, alors nous pourrons afficher l'ensemble des marqueurs de ce 'petit' bout de carte.

### Gestion des événements

A chaque zoom ou chaque déplacement - supérieur à la distance du bord de la carte centrale au bord de l'extension, un appel Ajax demandera au serveur de recalculer les nouveaux éléments.  

Le calcul des éléments sur les bords de la carte permet de pré-charger les POI et d'anticiper le déplacement de l'internaute afin de fluidifier l'application.

### Passage de paramètres

A chaque événement, il faudra donc envoyer au serveur les coordonnées des bords de la carte afin que celui-ci puisse calculer les POI et les marqueurs et puisse renvoyer le XML correspondant.  

## Côté client

### Création et affichage des marqueurs

Tout d'abord il faut créer une fonction de création de marqueurs. Celle-ci différencie les marqueurs 'simples' des marqueurs 'cluster' avec une affichage différent et un événement spécifique à chacun.  

```javascript
function createMarker(lat,lng,title,icon,cluster){
  var point = new GLatLng(lat,lng);
  if (!cluster){
   icon.image = "./icon/marker/pic.png";
   icon.shadow = "./icon/marker/shadow.png";
   var mark = new GMarker(point,{icon: icon, title: title});
   var infowindow = title;
   GEvent.addListener(mark, 'click', function() {
    mark.openInfoWindowHtml(infowindow);
   });
   map.addOverlay(mark);
  }
  else{
   icon.image = "./icon/marker/cluster_marker.png";
   icon.shadow = "./icon/marker/shadow.png";
   var mark = new GMarker(point,{icon: icon, title: title});
   var infowindow = "";
   GEvent.addListener(mark, 'click', function() {
    map.setCenter(mark.getLatLng(),map.getZoom()+1);
   });
   map.addOverlay(mark);
  }
 }
```

### Récupération des marqueurs via Ajax

L'API Google Maps permet d'utiliser la méthode XmlHttpRequest pour faire des appels à un serveur - il s'agit de la méthode GDownloadUrl déjà utilisée dans le [tutoriel n°10](http://www.geotribu.net/node/38).

Il faut commencer par supprimer les overlays présents sur la carte :  

`map.clearOverlays();`  

Puis récupérer les bords de la carte et le niveau de zoom que nous allons passer en paramètre lors de l'appel au serveur :  

```javascript
var maxY = map.getBounds().getNorthEast().lat();  
var minY = map.getBounds().getSouthWest().lat();  
var maxX = map.getBounds().getNorthEast().lng();  
var minX = map.getBounds().getSouthWest().lng();
```  

Les paramètres sont définis dans l'url :  

`var urlstr = "./function/getObj.php?maxY="+maxY+"&minY="+minY+"&maxX="+maxX+"&minX="+minX+"&zoomLevel="+zoomLevel;`  

Enfin la méthode GDownloadUrl qui récupère le XML construit côté serveur en fonction des paramètres et qui appelle la fonction de création de marqueurs ci-dessus.  

```javascript
GDownloadUrl(urlstr, function(data, responseCode){
 if (responseCode == 200){
  var xmlDoc = GXml.parse(data);
  var markers = xmlDoc.documentElement.getElementsByTagName("marker");

  var icon = new GIcon();
  icon.iconSize = new GSize(24.0,38.0);
  icon.shadowSize = new GSize(44.0,38.0);
  icon.iconAnchor = new GPoint(12.0,38.0);
  icon.infoWindowAnchor = new GPoint(12.0,19.0);

  for (i=0;i<markers.length;i++){
   var latMarker = parseFloat(markers[i].getAttribute("lat_object"));
   var lngMarker = parseFloat(markers[i].getAttribute("lng_object"));
   if (markers[i].getAttribute("cluster") == 0){
    var title = markers[i].getAttribute("title_object");
    createMarker(latMarker,lngMarker,title,icon,false);
   }
   else{
    var title = markers[i].getAttribute("nb_marker")+' items - zoom to view (click on marker)';
    createMarker(latMarker,lngMarker,title,icon,true);
   }
  }
 }
});
```

### Initialisation de la carte et création des événements

Nous remarquerons qu'après la déclaration des options, nous appelons la méthode getMarker() afin d'afficher les marqueurs pour le niveau de zoom et l'extend par défaut.  

Le but de ce tutoriel étant la clusterisation, il est nécessaire de déclarer un événement qui appelle la fonction getMarker() chaque fois que l'utilisateur modifie le zoom de la carte :  

```javascript
GEvent.addListener(map, 'zoomend', function() {
 getMarker();
});
```

Il faut ensuite définir une méthode pour faire une requête au serveur chaque fois que l'utilisateur se déplace sur la carte en dépassant les limites de la 'grande' carte (cf. Comment faire ?).  

Pour cela, il faut voir à chaque fin de déplacement (moveend) si la distance entre le nouveau centre et l'ancien centre et supérieure au pourcentage de carte défini - cf. la 'grande' carte et la carte du centre.  

Si c'est le cas, alors nous réinitialisons les coordonnées des extend et nous appelons la fonction `getMarker()`.  

```javascript
var centerLat = map.getCenter().lat();
var centerLng = map.getCenter().lng();
var north = map.getBounds().getNorthEast().lat();
var south = map.getBounds().getSouthWest().lat();
var west = map.getBounds().getNorthEast().lng();
var east = map.getBounds().getSouthWest().lng();

GEvent.addListener(map, 'moveend', function() {
 var north = map.getBounds().getNorthEast().lat();
 var south = map.getBounds().getSouthWest().lat();
 var west = map.getBounds().getNorthEast().lng();
 var east = map.getBounds().getSouthWest().lng();

 var centerMoveLat = map.getCenter().lat();
 var centerMoveLng = map.getCenter().lng();

 var extendY = Math.abs(north - south)*extendPercent;
 var extendX = Math.abs(west - east)*extendPercent;

 if ((centerMoveLng > (centerLng + extendX)) || (centerMoveLng < (centerLng - extendX))){
  centerLat = map.getCenter().lat();
  centerLng = map.getCenter().lng();
  north = map.getBounds().getNorthEast().lat();
  south = map.getBounds().getSouthWest().lat();
  west = map.getBounds().getNorthEast().lng();
  east = map.getBounds().getSouthWest().lng();
  getMarker();
 }

 if ((centerMoveLat > (centerLat + extendY)) || (centerMoveLat < (centerLat - extendY))){
  centerLat = map.getCenter().lat();
  centerLng = map.getCenter().lng();
  north = map.getBounds().getNorthEast().lat();
  south = map.getBounds().getSouthWest().lat();
  west = map.getBounds().getNorthEast().lng();
  east = map.getBounds().getSouthWest().lng();
  getMarker();
 }
});
```

La variable extendPercent est le pourcentage qui définit les bornes de la 'grande' carte :  

`var extendPercent = 50 / 100;`  

Il faudra veiller à ce que ce pourcentage soit le même côté serveur.  

## Côté serveur

### Initialisation des variables

Avant de commencer à aller chercher les éléments en base de données, il convient de préparer le terrain à la construction du fichier XML.  

Tout d'abord, définir le pas, l'extend de la carte (cf. côté client) et le nombre max d'objets par cellule à partir duquel on affiche un marqueur clusterisé :  

```javascript
$extendPercent = 50 / 100;
$cluster_number = 5;  
$pas = 10;
```

Notons que nous avons défini également l'extend de carte supplémentaire dans le côté client afin de gérer l'événement sur le déplacement à la souris.

Puis vient le tour des paramètres passés via la fonction GDownloadUrl côté client - les bords de la carte - et profitons-en pour calculer l'extend réel :  

```javascript
$addExtendY = ($_GET['maxY'] - $_GET['minY']) * $extendPercent;  
$addExtendX = ($_GET['maxX'] - $_GET['minX']) * $extendPercent;
```  

Reste la partie un peu délicate de calcul des bornes de la 'grande' carte - tout en faisant attention aux coordonnées parfois négatives :  

```javascript
($_GET['maxY'] > 0 ) ? ((($_GET['maxY'] + $addExtendY) > 90) ? $maxY = 90 : $maxY = $_GET['maxY'] + $addExtendY ) : $maxY = $_GET['maxY'] - $addExtendY ;
($_GET['maxX'] > 0 ) ? ((($_GET['maxX'] + $addExtendX) > 180) ? $maxX = 180 : $maxX = $_GET['maxX'] + $addExtendX ) : $maxX = $_GET['maxX'] - $addExtendX ;
($_GET['minY'] > 0 ) ? $minY = $_GET['minY'] - $addExtendY : ((($_GET['minY'] - $addExtendY) < -90) ? $minY = -90 : $minY = $_GET['minY'] - $addExtendY) ;
($_GET['minX'] > 0 ) ? $minX = $_GET['minX'] - $addExtendX : ((($_GET['minX'] - $addExtendX) < -180) ? $minX = -180 : $minX = $_GET['minX'] - $addExtendX) ;
```  

Ainsi nous avons les bornes de la 'grande' carte dans les variables $maxY, $minX, etc.  

La syntaxe un peu particulière - ? : - est juste un opérateur ternaire qui évite de faire des longs if then else - <http://www.phpsources.org/tutoriel-conditionnel-if-else.htm#part_2>. Ici il y en a deux imbriqués.

Enfin il reste à calculer le pas en X et en Y - c'est-à-dire la taille d'une petite cellule :  

```javascript
$pas_largeur = $largeur / $pas;
$pas_hauteur = $hauteur / $pas;
```

Et l'initialisation du XML via les fonctions du dom :  

```javascript
$dom = new DomDocument('1.0', 'iso-8859-1');  
$node = $dom->createElement("markers");  
$parnode = $dom->appendChild($node);
```

### Construction du XML

Une fois toutes les étapes précédentes effectuées, il ne reste plus qu'à éditer le fichier XML correspondant à la requête passée côté client.  

Le processus est simple : pour chaque cellule - dont nous avons maintenant les bornes - calculer le nombre d'éléments qu'elle contient puis ajouter des marqueurs dans le XML - soit un cluster calculé au centroïde des points de la cellule ou les marqueurs si le nombre de marqueurs dans la cellule est inférieur à la variable définie un peu plus haut.  

Parcourons toutes les cellules :  

```javascript
for ($i=0;$i<$pas;$i++){
  for ($j=0;$j<$pas;$j++){
```

Paramétrons la requête spatiale (ici avec PostGIS) pour ne récupérer que les éléments dans la cellule :  

```jaavscript
$temp1 = $minY + $pas_hauteur * $i;
$temp2 = $minX + $pas_largeur * $j;
$temp3 = $minY + $pas_hauteur * ($i + 1);
$temp4 = $minX + $pas_largeur * ($j + 1);
$coord1 = strval($temp2)." ".strval($temp1);
$coord2 = strval($temp4)." ".strval($temp1);
$coord3 = strval($temp4)." ".strval($temp3);
$coord4 = strval($temp2)." ".strval($temp3);

$sql = "SELECT x(geom_object) as x, y(geom_object) as y, title_object FROM object WHERE ";
$sql .= "Contains (GeometryFromText('POLYGON(($coord1,$coord2,$coord3,$coord4,$coord1))',4326),object.geom_object)";
```

Là j'avoue n'avoir pas été super efficace : je calcule 4 chaînes de caractères qui définissent les coordonnées de la cellule pour PostGIS. C'est pas la meilleure solution : il y a moyen de se passer du GeometryFromText.

Puis construisons enfin le XML - on différencie le cas où le nombre d'objets par cellule est supérieur à la variable (où on construit un marqueur 'cluster' qui invitera à zoomer dans la partie cliente) :  

```javascript
$res = pg_query($sql) or die(pg_last_error());
$nb_object = pg_num_rows($res);

if ($nb_object <> 0){
  if ($nb_object > $cluster_number){
    $node = $dom->createElement("marker");
    $newnode = $parnode->appendChild($node);

    $polygone = "POLYGON((";
    $a = 0;
    while ($result = pg_fetch_array($res)){
      if ($a == 0){
        $firstPoint = $result['x']." ".$result['y'];
      }
      $polygone .= $result['x']." ".$result['y'].",";
      $a++;
    }
    $polygone .= $firstPoint;
    $polygone .= "))";

    $sql2 = "select x(Centroid(GeometryFromText('".$polygone."',4326))) as x, y(Centroid(GeometryFromText('".$polygone."',4326))) as y";
    $res2 = pg_query($sql2) or die(pg_last_error());
    $result2 = pg_fetch_array($res2);

    $lat = $result2['y'];
    $lng = $result2['x'];

    $newnode->setAttribute("lat_object", $lat);
    $newnode->setAttribute("lng_object", $lng);
    $newnode->setAttribute("nb_marker", $nb_object);
    $newnode->setAttribute("cluster", 1);
  }
  else{
    while($result = pg_fetch_array($res)){
      $node = $dom->createElement("marker");
      $newnode = $parnode->appendChild($node);
      $newnode->setAttribute("lat_object", $result['y']);
      $newnode->setAttribute("lng_object", $result['x']);
      $newnode->setAttribute("title_object", stripslashes($result['title_object']));
      $newnode->setAttribute("cluster", 0);
    }
  }
}
```

Pour la construction du XML se reporter au [tutoriel n°10](http://www.geotribu.net/node/38).

Il suffit pour conclure de fermer le XML et de l'écrire :  

```javascript
$xmlfile = $dom->saveXML();
echo $xmlfile;
```

## Code complet

```html
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>
     [Google Maps] 19. Clusterisation côté serveur
   </title>
   <style type="text/css">
     html { overflow:hidden; height:100%; }
     body { height:100%; margin:0; }
     #map { width:100%; height:100%; }
   </style>
   <link rel="icon" type="image/png" href="./favicon.png"/>
   <script src="http://maps.google.com/maps?file=api&v=2&key=votre_clé_ici" type="text/javascript"></script>
   <script type="text/javascript">

 var map;
 var extendPercent = 50 / 100;

 function createMarker(lat,lng,title,icon,cluster){
  var point = new GLatLng(lat,lng);
  if (!cluster){
   icon.image = "./icon/marker/pic.png";
   icon.shadow = "./icon/marker/shadow.png";
   var mark = new GMarker(point,{icon: icon, title: title});
   var infowindow = title;
   GEvent.addListener(mark, 'click', function() {
    mark.openInfoWindowHtml(infowindow);
   });
   map.addOverlay(mark);
  }
  else{
   icon.image = "./icon/marker/cluster_marker.png";
   icon.shadow = "./icon/marker/shadow.png";
   var mark = new GMarker(point,{icon: icon, title: title});
   var infowindow = "";
   GEvent.addListener(mark, 'click', function() {
    map.setCenter(mark.getLatLng(),map.getZoom()+1);
   });
   map.addOverlay(mark);
  }
 }

 function getMarker(){
  map.clearOverlays();
  var maxY = map.getBounds().getNorthEast().lat();
  var minY = map.getBounds().getSouthWest().lat();
  var maxX = map.getBounds().getNorthEast().lng();
  var minX = map.getBounds().getSouthWest().lng();
  var zoomLevel = map.getZoom();
  var urlstr = "./function/getObj.php?maxY="+maxY+"&minY="+minY+"&maxX="+maxX+"&minX="+minX+"&zoomLevel="+zoomLevel;
  GDownloadUrl(urlstr, function(data, responseCode){
   if (responseCode == 200){
    var xmlDoc = GXml.parse(data);
    var markers = xmlDoc.documentElement.getElementsByTagName("marker");

    var icon = new GIcon();
    icon.iconSize = new GSize(24.0,38.0);
    icon.shadowSize = new GSize(44.0,38.0);
    icon.iconAnchor = new GPoint(12.0,38.0);
    icon.infoWindowAnchor = new GPoint(12.0,19.0);

    for (i=0;i<markers.length;i++){
     var latMarker = parseFloat(markers[i].getAttribute("lat_object"));
     var lngMarker = parseFloat(markers[i].getAttribute("lng_object"));
     if (markers[i].getAttribute("cluster") == 0){
      var title = markers[i].getAttribute("title_object");
      createMarker(latMarker,lngMarker,title,icon,false);
     }
     else{
      var title = markers[i].getAttribute("nb_marker")+' items - zoom to view (click on marker)';
      createMarker(latMarker,lngMarker,title,icon,true);
     }
    }
   }
  });
 }

 function initialize() {
  if (GBrowserIsCompatible()) {
   map = new GMap2(document.getElementById('map'));
   map.setCenter(new GLatLng(42.57691664771851, 0.402451992034912),9);
   map.addControl(new GMapTypeControl());
   map.removeMapType(G_HYBRID_MAP);
   map.addMapType(G_PHYSICAL_MAP);
   map.setMapType(G_PHYSICAL_MAP);
   map.addControl(new GOverviewMapControl());
   map.addControl(new GScaleControl());
   map.addControl(new GLargeMapControl());
   map.enableScrollWheelZoom();
   getMarker();

   var centerLat = map.getCenter().lat();
   var centerLng = map.getCenter().lng();
   var north = map.getBounds().getNorthEast().lat();
   var south = map.getBounds().getSouthWest().lat();
   var west = map.getBounds().getNorthEast().lng();
   var east = map.getBounds().getSouthWest().lng();

   GEvent.addListener(map, 'moveend', function() {
    var north = map.getBounds().getNorthEast().lat();
    var south = map.getBounds().getSouthWest().lat();
    var west = map.getBounds().getNorthEast().lng();
    var east = map.getBounds().getSouthWest().lng();

    var centerMoveLat = map.getCenter().lat();
    var centerMoveLng = map.getCenter().lng();

    var extendY = Math.abs(north - south)*extendPercent;
    var extendX = Math.abs(west - east)*extendPercent;

    if ((centerMoveLng > (centerLng + extendX)) || (centerMoveLng < (centerLng - extendX))){
     centerLat = map.getCenter().lat();
     centerLng = map.getCenter().lng();
     north = map.getBounds().getNorthEast().lat();
     south = map.getBounds().getSouthWest().lat();
     west = map.getBounds().getNorthEast().lng();
     east = map.getBounds().getSouthWest().lng();
     getMarker();
    }

    if ((centerMoveLat > (centerLat + extendY)) || (centerMoveLat < (centerLat - extendY))){
     centerLat = map.getCenter().lat();
     centerLng = map.getCenter().lng();
     north = map.getBounds().getNorthEast().lat();
     south = map.getBounds().getSouthWest().lat();
     west = map.getBounds().getNorthEast().lng();
     east = map.getBounds().getSouthWest().lng();
     getMarker();
    }
   });

   GEvent.addListener(map, 'zoomend', function() {
    getMarker();
   });
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

```php
<?php

 pg_connect("host=localhost dbname=****** user=****** password=******");

 $extendPercent = 50 / 100;
        $cluster_number = 5;
        $pas = 10;

 $addExtendY = ($_GET['maxY'] - $_GET['minY']) * $extendPercent;
 $addExtendX = ($_GET['maxX'] - $_GET['minX']) * $extendPercent;

 ($_GET['maxY'] > 0 ) ? ((($_GET['maxY'] + $addExtendY) > 90) ? $maxY = 90 : $maxY = $_GET['maxY'] + $addExtendY ) : $maxY = $_GET['maxY'] - $addExtendY ;
 ($_GET['maxX'] > 0 ) ? ((($_GET['maxX'] + $addExtendX) > 180) ? $maxX = 180 : $maxX = $_GET['maxX'] + $addExtendX ) : $maxX = $_GET['maxX'] - $addExtendX ;
 ($_GET['minY'] > 0 ) ? $minY = $_GET['minY'] - $addExtendY : ((($_GET['minY'] - $addExtendY) < -90) ? $minY = -90 : $minY = $_GET['minY'] - $addExtendY) ;
 ($_GET['minX'] > 0 ) ? $minX = $_GET['minX'] - $addExtendX : ((($_GET['minX'] - $addExtendX) < -180) ? $minX = -180 : $minX = $_GET['minX'] - $addExtendX) ;

 $dom = new DomDocument('1.0', 'iso-8859-1');
 $node = $dom->createElement("markers");
 $parnode = $dom->appendChild($node);

 $largeur = $maxX - $minX;
 $hauteur = $maxY - $minY;

 $pas_largeur = $largeur / $pas;
 $pas_hauteur = $hauteur / $pas;

 for ($i=0;$i<$pas;$i++){
  for ($j=0;$j<$pas;$j++){
   $temp1 = $minY + $pas_hauteur * $i;
   $temp2 = $minX + $pas_largeur * $j;
   $temp3 = $minY + $pas_hauteur * ($i + 1);
   $temp4 = $minX + $pas_largeur * ($j + 1);
   $coord1 = strval($temp2)." ".strval($temp1);
   $coord2 = strval($temp4)." ".strval($temp1);
   $coord3 = strval($temp4)." ".strval($temp3);
   $coord4 = strval($temp2)." ".strval($temp3);

   $sql = "SELECT x(geom_object) as x, y(geom_object) as y, title_object FROM object WHERE ";
                        $sql .= "Contains (GeometryFromText('POLYGON(($coord1,$coord2,$coord3,$coord4,$coord1))',4326),object.geom_object)";

   $res = pg_query($sql) or die(pg_last_error());
   $nb_object = pg_num_rows($res);

   if ($nb_object <> 0){
    if ($nb_object > $cluster_number){
     $node = $dom->createElement("marker");
     $newnode = $parnode->appendChild($node);

     $polygone = "POLYGON((";
     $a = 0;
     while ($result = pg_fetch_array($res)){
      if ($a == 0){
       $firstPoint = $result['x']." ".$result['y'];
      }
      $polygone .= $result['x']." ".$result['y'].",";
      $a++;
     }
     $polygone .= $firstPoint;
     $polygone .= "))";

     $sql2 = "select x(Centroid(GeometryFromText('".$polygone."',4326))) as x, y(Centroid(GeometryFromText('".$polygone."',4326))) as y";
     $res2 = pg_query($sql2) or die(pg_last_error());
     $result2 = pg_fetch_array($res2);

     $lat = $result2['y'];
     $lng = $result2['x'];

     $newnode->setAttribute("lat_object", $lat);
     $newnode->setAttribute("lng_object", $lng);
     $newnode->setAttribute("nb_marker", $nb_object);
     $newnode->setAttribute("cluster", 1);
    }
    else{
     while($result = pg_fetch_array($res)){
      $node = $dom->createElement("marker");
      $newnode = $parnode->appendChild($node);
      $newnode->setAttribute("lat_object", $result['y']);
      $newnode->setAttribute("lng_object", $result['x']);
      $newnode->setAttribute("title_object", stripslashes($result['title_object']));
      $newnode->setAttribute("cluster", 0);
     }
    }
   }
  }
 }

 $xmlfile = $dom->saveXML();
 echo $xmlfile;
?>
```

## Démonstration

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://geotribu.net/applications/cluster/%5Bgeotribu%5D_Google_Maps_tuto19.html" height="350px" width="550px"></iframe>`

[Résultat pleine page](http://geotribu.net/applications/cluster/%5Bgeotribu%5D_Google_Maps_tuto19.html)

Evidemment le résultat est plus joli en pleine page :-)

## Remarques

Ce tutoriel utilise une base de données spatiale sous PostgreSQL et sa composante PostGIS. Ce couple permet de faire des requêtes spatiales - ici inclusion et calcul de centroïde.
Le calcul du centroïde dans le cas d'une cellule contenant beaucoup d'objets ralentit un peu l'application, il aurait été plus rapide (mais moins joli :-) ) de placer le marqueur cluster simplement au milieu de la cellule.

## Conclusion

Ce tutoriel montre qu'il est possible en peu de lignes de code, d'afficher intelligemment des données stockées en base. En effet, il est communément admis qu'à partir d'une centaine d'objets construits et affichés, les interfaces d'affichage cartographique Javascript (Google Maps ici, mais c'est sensiblement pareil pour OpenLayers) n'arrivent plus à être performantes.
Il faut donc 'jouer' avec le nombre d'objets à afficher au maximum - ici en adaptant les paramètres d'extent, de pas et le nombre d'objets par cellule.
Ce tutoriel n'est qu'une méthode parmi d'autres et ne se veut pas la plus optimale possible - notamment côté serveur ou les requêtes ne sont pas les plus efficaces.

----

<!-- geotribu:authors-block -->
