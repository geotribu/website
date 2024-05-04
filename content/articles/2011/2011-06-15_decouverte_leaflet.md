---
title: "Leaflet, une nouvelle librairie cartographique en Javascript"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2011-06-15
description: "A la découverte de Leaflet, une nouvelle librairie cartographique en Javascript."
image: "https://leafletjs.com/docs/images/logo.png"
tags:
    - API
    - JavaScript
    - Leaflet
    - open source
---

# Leaflet, une nouvelle librairie cartographique en Javascript

:calendar: Date de publication initiale : 15 juin 2011

![logo leafletjs](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/leaflet.png "logo Leaflet"){: .img-thumbnail-left }

[Annoncé](http://blog.cloudmade.com/2011/05/13/announcing-leaflet-a-modern-open-source-javascript-library-for-interactive-maps/) il y a quelques semaines, [Leaflet](http://leaflet.cloudmade.com/) est la nouvelle API cartographique en JavaScript de [Cloud Made](http://blog.cloudmade.com). Les conditions d'utilisations sont très souples puisqu'elle a été publiée sous [licence BSD](https://fr.wikipedia.org/wiki/Licence_BSD). Néanmoins, que vaut-elle par rapport aux autres alternatives existantes ? Partons dans ce tutoriel à la découverte de celle-ci.

## Téléchargement

Commençons tout d'abord par [télécharger](http://github.com/CloudMade/Leaflet/zipball/master) la librairie. Premier constat, celle-ci est particulièrement légère, à peine plus d'une cinquantaine de kilo octets pour la version compressée. Quelques [exemples d'applications](http://leaflet.cloudmade.com/examples.html) sont déjà disponibles, mais regardons ce qu'elle permet de faire.

## Contenu de l'API

Composé d'une dizaine de classes, [l'API de leaflet](http://leaflet.cloudmade.com/reference.html) contient les éléments habituels nécessaires à la construction d'une application cartographique. Nous retrouvons ainsi la [classe map](http://leaflet.cloudmade.com/reference.html#map-usage), la classe [Rasters Layer](http://leaflet.cloudmade.com/reference.html#tilelayer) ou encore [la classe control](http://leaflet.cloudmade.com/reference.html#control-zoom). Les habitués d'OpenLayers ou de Google Maps ne se sentiront pas dépaysés. Néanmoins, à première vue les possibilités sont tout de même plus limitées. Par exemple, pour le moment les seuls contrôles disponibles sont celui du zoom et des attributions.

## Afficher une carte

### Squelette de la page

Bon, passons aux choses sérieuses et commençons à étudier un peu le code. Nous allons pour les besoins de ce tutoriel créer une carte sur laquelle s'affichera un marqueur.  
Commençons par le squelette de notre page HTML.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Leaflet Quick Start Guide Example</title>
    <meta charset="utf-8" />

    <link rel="stylesheet" href="./CloudMade-Leaflet/dist/leaflet.css" />
    <script src="./CloudMade-Leaflet/dist/leaflet.js"></script>
    <script>
      function init() {
        //Leaflet code
      }
    </script>
  </head>
  <body onLoad="init()">
    <div id="map" style="width: 600px; height: 400px"></div>
  </body>
</html>
```

Rien de très sorcier. Nous allons simplement appeler la fonctiont "init()" au chargement de la page. C'est à l'intérieur de cette fonction que nous allons construire notre carte.

### L'objet Map

Passons maintenant à l'objet map. Celui-ci prend en paramètre l'id d'un div de votre dom. Dans notre cas l'id est 'map'. Ensuite nous pouvons ajouter des [arguments supplémentaires](http://leaflet.cloudmade.com/reference.html#map-options) comme le zoom initial, la position de la carte, les actions autorisées (zoom, déplacement, etc), ou encore l'activation ou non d'animations lors des transitions. Festival de Cannes oblige, zoomons sur la croisette :

```javascript
function init() {
  var map = new L.Map("map", {
    center: new L.LatLng(43.55, 7.02),
    zoom: 14,
  });
}
```

### Les couches de données

Notre objet map créé, nous allons lui ajouter maintenant une couche de données. Les trois types disponibles sont une couche de type TileLayer, de type WMS ou une image. Pour le moment, utilisons le service de tuile de Cloud Made. Mais, pour cela une [inscription](http://cloudmade.com/signin) est nécessaire afin de disposer d'une clé d'authentification. Cette dernière sera à spécifier lors de l'appel des tuiles. Par exemple :

```javascript
function init(){
    [...]
    var cloudmadeUrl = 'http://{s}.tile.cloudmade.com/Your-API-Key/997/256/{z}/{x}/{y}.png';
    var cloudmade = new L.TileLayer(cloudmadeUrl, {maxZoom: 18});
    map.addLayer(cloudmade);
}
```

Le petit côté sympa de cloud made, c'est la possibilité de changer le style de votre carte. Pour cela, il suffit de modifier le chiffre (997) par un nouvel identifiant d'un des nombreux styles disponibles via [l'interface d'édition](http://maps.cloudmade.com/editor). Par exemple, modifions 997 par 999 pour lui donner un petit air plus sombre !  
Et voilà, il nous suffit maintenant d'ajouter cette couche à la carte grâce à la méthode [map.addLayer()](http://leaflet.cloudmade.com/reference.html#map-stuff-methods).  
Si vous rechargez votre page, vous devriez maintenant disposer d'une carte avec cannes affichée en noir et blanc.

### Les marqueurs

Voyons comment ajouter un [marqueur](http://leaflet.cloudmade.com/reference.html#marker). Cela se fait en à peine trois lignes de code :

```javascript
function init(){  
    [...]  
    var latlng = new L.LatLng(43.55, 7.018); // 1  
    var marker = new L.Marker(latlng); // 2  
    map.addLayer(marker); // 3
}
```

Premièrement nous spécifions les coordonnées du marqueur avec l'objet [Latlng](http://leaflet.cloudmade.com/reference.html#latlng) que nous passons ensuite en argument à notre objet marqueur. Enfin, il suffit d'ajouter celui-ci à la carte.  
Bien que l'icône du marqueur soit déjà très sympathique voyons tout de même comment changer celle-ci. Pour cela, nous allons étendre les propriétés initiales de l'objet Icon. Cela se fait de la manière suivante :

```javascript
function init(){  

    var icon = L.Icon.extend({  
        iconUrl: './icone.png',  
        iconSize: new L.Point(32, 32),  
        shadowSize: new L.Point(0, 0)  
    });  
    var cannesIcon = new icon();  
    var latlng = new L.LatLng(43.55, 7.018);  
    var marker = new L.Marker(latlng, {icon: cannesIcon});  
    map.addLayer(marker);  
}
```

Il ne manque plus qu'à ajouter une jolie infobulle.

### Les infobulles

L'affichage d'une infobulle est vraiment très simple. Une seule ligne suffit :

```javascript
function init(){  
    [...]
    marker.bindPopup('Vive le festival de Cannes');  
}
```

### Code et application

Voici le code complet utilisé pour ce tutoriel ainsi que le rendu final

```javascript
function init(){  
// initialize the map on the "map" div with a given center and zoom  
    var map = new L.Map('map', {  
        center: new L.LatLng(43.55, 7.02),  
        zoom: 14  
    });

    // create a CloudMade tile layer  
    var cloudmadeUrl = 'http://{s}.tile.cloudmade.com/5c3066fdbca745adb52e3efb943995c5/999/256/{z}/{x}/{y}.png';

    var cloudmade = new L.TileLayer(cloudmadeUrl, {maxZoom: 18});

    // add the CloudMade layer to the map  
    map.addLayer(cloudmade);

    // Change the default icon style  
    var icon = L.Icon.extend({  
        iconUrl: './icone.png',  
        iconSize: new L.Point(32, 32),  
        shadowSize: new L.Point(0, 0)  
    });  
    var cannesIcon = new icon();  
    var latlng = new L.LatLng(43.55, 7.018);  
    var marker = new L.Marker(latlng, {icon: cannesIcon});  
    map.addLayer(marker);

    // Add a popup  
    marker.bindPopup('Vive le festival de Cannes');  
}
```

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://geotribu.net/applications/leaflet/leaflet.html" width="650px" height="450px" frameborder="0" align=""></iframe>`

## Conclusion

Leaflet est une librairie Javascript bien sympathique dont la prise en main est rapide et l'API assez intuitive. Néanmoins, même si [Rodolphe Quiédeville](http://blog.rodolphe.quiedeville.org/index.php?post/2011/05/Leaflet-la-sobre-OpenLayers-la-gourmande) met en avant son poids et la rapidité d'affichage, je reste pour le moment fidèle à OpenLayers. En effet, celle-ci n'apporte pas de fonctionnalités supplémentaires mis à part le plaisir de coder avec une nouvelle librairie.

----

<!-- geotribu:authors-block -->
