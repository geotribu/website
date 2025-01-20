---
title: "Calcul de buffer sous MySQL - 2ème partie : la pratique"
subtitle: MyTamponQL 2
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2012-04-17
description: "Calculer un buffer avec un SGBD sans extension spatiale (MySQL 5). 2ème partie : la pratique"
icon: simple/mysql
legacy:
    - node: 505
tags:
    - buffer
    - latitude
    - longitude
    - MySQL
    - rayon
    - Terre
---

# Calcul de buffer sous MySQL - 2ème partie - la pratique

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![logo MySQL](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/mysql.png){: .img-thumbnail-left }

Pour mettre en application le [premier article](./2012-04-16_calcul_buffer_mysql_partie_1_theorie.md) sur le calcul de buffer dans MySQL, nous allons développer une petite démo. Tout d'abord il nous faudra initialiser une base de données qui contiendra pas mal d'enregistrements, puis nous alimenterons cette base avec des points d'intérêts provenant d'OpenStreetMap et enfin nous développerons une carto avec l'API Google Maps pour tester la formule Haversine.

## La base de données

Créons une base de données sous MySQL :

```sql
CREATE DATABASE IF NOT EXISTS osmtestpoi  
```

Puis ajoutons une table contentant un champ de type `GEOMETRY` :

```sql
CREATE TABLE poi (  
id_poi INT NOT NULL AUTO_INCREMENT,  
name_poi VARCHAR(100),  
geom_poi GEOMETRY,  
PRIMARY KEY (id_poi)  
) ENGINE=INNODB DEFAULT CHARSET=utf8;  
```

## Des POI, des POI, toujours des POI

Pour la démo, il nous faut un grand nombre d'enregistrements. Au lieu de générer des faux points, autant s'amuser un peu avec les nouveaux [serveurs](https://wiki.openstreetmap.org/wiki/FR:Servers/Hardware#Dell_R610) et services proposés par [OpenStreetMap France](http://openstreetmap.fr/). Parmi les services nous utiliserons ici l'[OverpassAPI](https://wiki.openstreetmap.org/wiki/Overpass_API) qui permet de faire des extractions : il suffit de faire la bonne requête pour extraire ce que nous désirons (par exemple les restaurants dans une France métropolitaine un peu élargie). Nous allons donc utiliser la [boîte de requête](http://api.openstreetmap.fr/query_form.html) en ligne pour extraire les POI :

```xml
<query type="node">
  <bbox-query s="41.29" n="51.28" w="-5.41" e="10.15"/>
  <has-kv k="amenity" v="restaurant"/>
</query>
<print/>
```

Qui nous renverra un fichier d'environ 10 Mo que nous pousserons dans la base de données. L'OverpassAPI fournit un fichier XML OSMifié. Il suffit donc de parser le fichier et d'écrire un petit script pour alimenter la base.

## Un peu de parsing avec PHP

Pour alimenter la base de données, nous utiliserons ici le PHP. N'importe quel autre langage de scripts fait l'affaire. Voici un extrait de l'export d'OverpassAPI :

```xml
<node id="29681754" lat="43.6436341" lon="1.5220926">
  <tag k="amenity" v="restaurant"/>
  <tag k="name" v="La Table de Grand-mere"/>
  <tag k="website" v="http://www.latabledegrandmere.fr/"/>
</node>
```

C'est du XML et PHP sait le lire et le [transformer](http://php.net/manual/fr/function.simplexml-load-file.php) en objet. C'est assez pratique !  

Bon un peu de code :

1. On se connecte à la base de données.
2. On regarde si le fichier existe.
3. Pour chaque node, on récupère le nom si il existe.
4. On fait une petite requête d'insertion dans la table.
5. Et voilà !

```php
<?php

define('HOST', 'localhost');
define('PORT', '5432');
define('DB_USER', 'mylogin');
define('DB_PASS', 'mypass');
define('DB_NAME', 'osmtestpoi');

if (file_exists('./resources/osm/osmrestotoulouse.osm')) {
 $link = mysql_connect(HOST,DB_USER,DB_PASS);
 mysql_select_db(DB_NAME);
 $xml = simplexml_load_file('./resources/osm/osmrestotoulouse.osm');
 foreach ($xml->node as $node) {
  $existname = 0;
  foreach ($node->tag as $tag) {
   if ((string) $tag['k'] == 'name') {
    $name = mysql_real_escape_string($tag['v']);
    $existname = 1;
   } else {
    $name = "";
   }
  }
  switch ($existname) {
   case 0:
    $sql = "INSERT INTO poi (id_poi, geom_poi) VALUES (".$node['id'].",GeomFromText('POINT(".$node['lon']." ".$node['lat'].")'))";
    break;
   case 1:
    $sql = "INSERT INTO poi (id_poi, name_poi, geom_poi) VALUES (".$node['id'].",'".$name."',GeomFromText('POINT(".$node['lon']." ".$node['lat'].")'))";
    break;
  }
  $result = mysql_query($sql);
  if (!$result) {
   echo "Requête invalide : ".mysql_error()."<br/>";
  } else {
   echo $node['id']." => insert<br/>";
  }
 }
 mysql_free_result($result);
 mysql_close($link);
} else {
 exit('gloubs - il est où le fichier :/');
}

?>
```

## Préparons notre carte Google Maps

Ça fait quelques temps que nous n'avons pas développé avec l'API Google Maps ; malgré les désaffections des gros utilisateurs au profit d'OpenStreetMap, ça n'en reste pas moins une très belle librairie.

```html
<!DOCTYPE html>
<html>
<head>
 <title>Calcul de buffer sous MySQL</title>
 <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">
 <meta charset="UTF-8">
 <style type="text/css">
  html, body, #map_canvas {
   margin: 0;
   padding: 0;
   height: 100%;
  }
 </style>
 <script type="text/javascript" src="https://maps.googleapis.com/maps/api/js?sensor=false"></script>
 <script type="text/javascript">
  var map;
  function initialize() {
   var myOptions = {
    zoom: 6,
    center: new google.maps.LatLng(46.89, 2.61),
    mapTypeId: google.maps.MapTypeId.ROADMAP
   };
   map = new google.maps.Map(document.getElementById('map_canvas'), myOptions);
  }
  google.maps.event.addDomListener(window, 'load', initialize);
 </script>
</head>
<body>
 <div id="map_canvas"></div>
</body>
</html>
```

## XMLHttpRequest

Nous avons besoin d'une connexion Ajax vers le script PHP pour "aller chercher" nos marqueurs dans la base de données. Contrairement à l'API v2 qui proposait un connecteur par défaut, dans la v3 il faut le déclarer. Souvent nous n'avons pas besoin de coder cette fonction avec l'usage intensif de jQuery ou autre. Mais c'est pas plus mal de savoir ce que l'on fait :

```javascript
function downloadUrl(url,callback) {
 var request = window.ActiveXObject ? new ActiveXObject('Microsoft.XMLHTTP') : new XMLHttpRequest;
 request.onreadystatechange = function() {
  if (request.readyState == 4) {
   request.onreadystatechange = doNothing;
   callback(request, request.status);
  }
 };
 request.open('GET', url, true);
 request.send(null);
}

function doNothing() {}
```

## Chargeons les marqueurs et affichons-les

Dans le corps de la fonction, on fait un appel vers le script PHP et on parcourt le XML généré pour ajouter les marqueurs sur la carte :

```javascript
downloadUrl("getMarker.php", function(data) {
 var xml = data.responseXML;
 var markers = xml.documentElement.getElementsByTagName("marker");
 for (var i = 0; i < markers.length; i++) {
  var name = markers[i].getAttribute("name");
  var type = markers[i].getAttribute("type");
  var point = new google.maps.LatLng(parseFloat(markers[i].getAttribute("lat")), parseFloat(markers[i].getAttribute("lng")));
  var html = "<b>" + name + "</b> <br/>" + address;
  var marker = new google.maps.Marker({
   map: map,
   position: point
  });
  bindInfoWindow(marker, map, infoWindow, html);
 }
});
```

## Une petite infobulle

Ajoutons l'événement qui ouvre l'infobulle :

```javascript
function bindInfoWindow(marker, map, infoWindow, html) {
 google.maps.event.addListener(marker, 'click', function() {
  infoWindow.setContent(html);
  infoWindow.open(map, marker);
 });
}
```

### Le script qui génère le XML avec les marqueurs

Ici pas trop de souci, nous éditons le XML contenant les marqueurs en manipulant le DOM pour gérer la construction du fichier XML : il s'agit dune simple requête SQL - c'est ce script qu'il faudra changer pour prendre en compte le rayon de recherche et le centre.

```php
<?php header("Content-type: text/xml");

define('HOST', 'localhost');
define('PORT', '5432');
define('DB_USER', 'mylogin');
define('DB_PASS', 'mypass');
define('DB_NAME', 'osmtestpoi');

$link = mysql_connect(HOST,DB_USER,DB_PASS);
mysql_select_db(DB_NAME);

$dom = new DOMDocument("1.0");
$node = $dom->createElement("markers");
$parnode = $dom->appendChild($node);

$query = "SELECT poi.id_poi, poi.name_poi, x(geom_poi) AS X, y(geom_poi) AS Y FROM poi WHERE 1";
$result = mysql_query($query);

while ($row = @mysql_fetch_assoc($result)) {
 $node = $dom->createElement("marker");  
 $newnode = $parnode->appendChild($node);  
 $newnode->setAttribute("name",$row['name_poi']);
 $newnode->setAttribute("lat", $row['Y']);  
 $newnode->setAttribute("lng", $row['X']);  
 $newnode->setAttribute("type", "restaurant");
}

echo $dom->saveXML();

mysql_free_result($result);
mysql_close($link);

?>
```

Exemple sur Toulouse sans buffer - éviter de le faire avec la France - votre navigateur risque de ne pas trop apprécier le chargement ;)

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.142.86/geotribu/blog/buffermysql/index_toulouse_nobuffer.html" width="640" height="480" frameborder="0"></iframe>`

Hum : j'ai testé la carte avec toutes les données contenues en base (un peu plus de 47000 restaurants) ; bah le navigateur a un peu de mal, faut vraiment mettre en place ce système de buffer - d'ailleurs on peut remarquer qu'il y a beaucoup plus de restaurants recensés chez nos voisins :

![Trop de POI](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2012/tropdepoi.png "Trop de POI"){: .img-center loading=lazy }

## Code complet côté client

Pour afficher les marqueurs contenus dans un cercle, il faut modifier un peu le code côté client ci-dessus :

- mettre les marqueurs dans un tableau de marqueurs ;
- écrire une fonction qui supprime les marqueurs lorsque l'on bouge le cercle de recherche ;
- ajouter des événements sur le cercle - quand on le bouge et quand on modifie son rayon.

Un peu de CSS :

```css
<style type="text/css">
 html, body {
  margin: 0;
  padding: 0;
  height: 100%;
 }
 #map_canvas {
  float: left;
 }
 #form_canvas {
  float: left;
  margin: 5px;
 }
 #maxbuffer {
  color: red;
  font-size: 10px;
 }
</style>
```

On ajoute jQuery parce que c'est bien pratique :

```html
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7/jquery.min.js"></script>
```

Déclaration des variables et écriture des fonctions :

```javascript
var map;
var markersArray = [];
var buffer;
var circle;
var uri;
var infoWindow;

function clearMarkers() {
 if (markersArray) {
  for (i in markersArray) {
   markersArray[i].setMap(null);
  }
 }
}

function getMarker() {
 downloadUrl(uri, function(data) {
  var xml = data.responseXML;
  var markers = xml.documentElement.getElementsByTagName("marker");
  for (var i = 0; i < markers.length; i++) {
   var name = markers[i].getAttribute("name");
   var type = markers[i].getAttribute("type");
   var point = new google.maps.LatLng(parseFloat(markers[i].getAttribute("lat")), parseFloat(markers[i].getAttribute("lng")));
   var html = "<b>" + name + "</b>";
   var marker = new google.maps.Marker({
    map: map,
    position: point
   });
   markersArray.push(marker);
   bindInfoWindow(marker, map, infoWindow, html);
  }
 });
}
```

Puis initialisons un cercle de recherche et des événements lorsque l'utilisateur modifie celui-ci :

```javascript
infoWindow = new google.maps.InfoWindow;

circle = new google.maps.Circle({
 map: map,
 fillColor: '#ff8922',
 fillOpacity: 0.2,
 strokeWeight: 0,
 clickable: false,
 editable: true,
 center: new google.maps.LatLng(46.83, 2.50),
 radius: 50000
});
buffer = circle.getRadius() / 1000;
uri = "getMarker.php?lat="+circle.getCenter().lat()+"&lng="+circle.getCenter().lng()+"&buffer="+buffer;
getMarker();

google.maps.event.addListener(circle, 'center_changed', function(e) {
 clearMarkers();
 if (circle.getRadius() > 50000) {
  circle.setRadius(50000);
  $("#maxbuffer").show().delay(1000).queue(function(n) {
   $(this).hide(); n();
  });
 }
 buffer = circle.getRadius() / 1000;
 uri = "getMarker.php?lat="+circle.getCenter().lat()+"&lng="+circle.getCenter().lng()+"&buffer="+buffer;
 getMarker();
 $("#lat").val(circle.getCenter().lat());
 $("#lng").val(circle.getCenter().lng());
 $("#rayon").val(Math.round(circle.getRadius()/1000));
});

google.maps.event.addListener(circle, 'radius_changed', function(e) {
 clearMarkers();
 if (circle.getRadius() > 50000) {
  circle.setRadius(50000);
  $("#maxbuffer").show().delay(1000).queue(function(n) {
   $(this).hide(); n();
  });
 }
 buffer = circle.getRadius() / 1000;
 uri = "getMarker.php?lat="+circle.getCenter().lat()+"&lng="+circle.getCenter().lng()+"&buffer="+buffer;
 getMarker();
 $("#lat").val(circle.getCenter().lat());
 $("#lng").val(circle.getCenter().lng());
 $("#rayon").val(Math.round(circle.getRadius()/1000));
});

$("#lat").val(circle.getCenter().lat());
$("#lng").val(circle.getCenter().lng());
$("#rayon").val(Math.round(circle.getRadius()/1000));
```

Ajoutons un petit bloc d'informations :

```html
<div id="map_canvas" style="float: left; width: 640px; height: 480px;"></div>
<div id="form_canvas">
 <form>
  <fieldset>
   <legend align="top">Centre et buffer</legend>
   latitude : <input readonly id="lat" type="text" name="lat"/><br/>
   longitude : <input readonly id="lng" type="text" name="lng"/><br/>
   rayon : <input readonly id="rayon" type="text" name="rayon"/>
  </fieldset>
 </form>
 <span id="maxbuffer" style="display:none;">* Buffer 50 km maximum</span>
</div>
```

## Et côté serveur

On cherche dans la base de données les enregistrements qui sont dans la bounding box calculée dans le premier article et qui sont à une distance inférieure au buffer :

```php
<?php header("Content-type: text/xml");

define('HOST', 'localhost');
define('PORT', '5432');
define('DB_USER', 'mylogin');
define('DB_PASS', 'mypass');
define('DB_NAME', 'osmtestpoi');

$link = mysql_connect(HOST,DB_USER,DB_PASS);
mysql_select_db(DB_NAME);

$dom = new DOMDocument("1.0");
$node = $dom->createElement("markers");
$parnode = $dom->appendChild($node);

$query = "SELECT poifrance.id_poi, poifrance.name_poi, y(poifrance.geom_poi) AS Y,
x(poifrance.geom_poi) AS X,
6371 * 2 * asin(sqrt(power(sin((".$_GET['lat']." - abs(y(poifrance.geom_poi))) * pi() / 180 / 2), 2)
+ cos(".$_GET['lat']." * pi() / 180) * cos(abs(y(poifrance.geom_poi)) * pi() / 180)
* power(sin((".$_GET['lng']." - x(poifrance.geom_poi)) * pi() / 180 / 2), 2) )) AS distance
FROM poifrance WHERE 1 = 1 ";
if (isset($_GET['lat']) && isset($_GET['lng']) && isset($_GET['buffer'])) {
 $deglat = 111.195;
 $lat = $_GET['lat'];
 $lng = $_GET['lng'];
 $buffer = $_GET['buffer'];
 $query .= " AND y(poifrance.geom_poi) BETWEEN ".$lat." - (".$buffer." / ".$deglat.")
AND ".$lat." + (".$buffer." / ".$deglat.") ";
 $query .= " AND x(poifrance.geom_poi) BETWEEN ".$lng." - ".$buffer." / ABS(COS(RADIANS(".$lat.")) * ".$deglat.")
AND ".$lng." + ".$buffer." / ABS(COS(RADIANS(".$lat.")) * ".$deglat.")";
 $query .= " HAVING distance < ".$_GET['buffer'];
}
$result = mysql_query($query);

while ($row = @mysql_fetch_assoc($result)) {
 $node = $dom->createElement("marker");  
 $newnode = $parnode->appendChild($node);  
 $newnode->setAttribute("name",$row['name_poi']);
 $newnode->setAttribute("lat", $row['Y']);  
 $newnode->setAttribute("lng", $row['X']);  
 $newnode->setAttribute("type", "restaurant");
}

echo $dom->saveXML();

mysql_free_result($result);
mysql_close($link);

?>
```

Ce qui donne :) Attention le rayon maximum de recherche est de 50 km.

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.142.86/geotribu/blog/buffermysql/index.html" width="800" height="600" frameborder="0"></iframe>`

## Conclusion

Ces deux billets nous ont montré comment mettre en place un système de buffer avec une base de données MySQL. En fait ce n'est pas si compliqué que ça, il convient juste de bien cerner le problème : limiter la recherche à une bounding box calculée avec la formule Haversine. Après, les appels à la base de données et l'affichage sont maintenant des choses bien connues.  
Si vous avez des remarques et / ou des suggestions, vous pouvez sans problème les soumettre dans les commentaires ou dans le ForumSIG.

----

<!-- geotribu:authors-block -->
