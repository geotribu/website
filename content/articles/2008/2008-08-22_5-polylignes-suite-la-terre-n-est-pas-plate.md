---
title: "5. Polylignes (suite) - La Terre n'est pas plate ..."
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-08-22
description: "5. Polylignes (suite) - La Terre n'est pas plate ..."
tags:
    - Google Maps
    - polylignes
---

# 5. Polylignes (suite) - La Terre n'est pas plate

:calendar: Date de publication initiale : 22 août 2008

:warning: L'API Google Maps v2 est dépréciée depuis le 19 mai 2010.

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-thumbnail-left }

Les options sont parfois nécessaires pour personnaliser les affichages. Ici nous verrons comment ajouter des options aux polylignes pour simuler les vols d'une compagnie aérienne.

## Initialisation

Pour ce tutoriel, nous partirons de la carte définie dans le second tutoriel et alimenterons la fonction `initialize()`.

## Création des points

Tout d'abord, définissons les villes :

```javascript
var paris = new GLatLng(48.83993649400669,2.394869685885226);
```

Puis les icônes - une image est définie par son pictogramme ainsi que par son ombre et un placement en pixel par rapport à sa taille :

```javascript
var icon1 = new GIcon();
icon1.image = "http://localhost/geotribu/icons/marker/green-dot.png";
icon1.shadow = "http://localhost/geotribu/icons/marker/shadow-dot.png";
icon1.iconSize = new GSize(32,32);
icon1.shadowSize = new GSize(49,32);
icon1.iconAnchor = new GPoint(16,32);
icon1.infoWindowAnchor = new GPoint(16,16);
```

Puis les marqueurs :

```javascript
var marker2 = new GMarker(paris,icon1);
```

## Création des vols

Pour créer les polylignes, il faut définir le vol :

```javascript
var vol1 = [paris,new_york];
```

puis les options des polylignes - notamment l'option 'geodesic' pour suivre la courbure de la Terre :

```javascript
var polyOptions = {geodesic: true};
```

et enfin les polylignes - couleur en héxadécimal #RRGGBB, largeur en pixel, opacité entre 0 et 1 - pour les options :

```javascript
var poly1 = new GPolyline(vol1, "#ff0000", 2.5, 0.5, polyOptions);
```

## Affichage des marqueurs et des polylignes

Enfin nous affichons les marqueurs et les polylignes sur la carte grâce à la méthode addOverlay :

```javascript
map.addOverlay(poly1);
map.addOverlay(marker1)
```

## Code complet

```html
<!DOCTYPE html "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>
     [Google Maps] 5. Polylignes (suite) - La Terre n'est pas plate ...
    </title>
    <style type="text/css">
      html { overflow:hidden; height:100%; }
      body { height:100%; margin:0; }
      #map { width:100%; height:100%; }
    </style>
    <script src="http://maps.google.com/maps?file=api&v=2.x&key=votre_clé_ici" type="text/javascript"></script>
    <script type="text/javascript">
      function initialize() {
        if (GBrowserIsCompatible()) {

        var map = new GMap2(document.getElementById('map'));
        map.setCenter(new GLatLng(25,25),3);
        map.addControl(new GMapTypeControl());
        map.removeMapType(G_HYBRID_MAP);
        map.addMapType(G_PHYSICAL_MAP);
        map.setMapType(G_PHYSICAL_MAP);
        map.addControl(new GOverviewMapControl());
        map.addControl(new GScaleControl());
        map.addControl(new GLargeMapControl());
        map.enableScrollWheelZoom();

        var paris = new GLatLng(48.83993649400669,2.394869685885226);
        var new_york = new GLatLng(40.75693702400098,-73.91742736554059);
        var los_angeles = new GLatLng(34.17323498103654,-118.0456432876794);
        var caracas = new GLatLng(10.94798332552648,-66.99024049901435);
        var rio_de_janeiro = new GLatLng(-23.20937441010468,-43.26000741240553);
        var le_cap = new GLatLng(-34.04665291730734,18.47867929466687);
        var dar_es_salam = new GLatLng(-6.382733932167927,40.04620692951011);
        var moscou = new GLatLng(54.37791252704001,38.60045811883745);
        var pekin = new GLatLng(39.61254910089286,115.8052418816071);
        var mumbay = new GLatLng(18.75725955119518,73.74377388950595);
        var singapour = new GLatLng(0.7880273829689369,103.8933421772066);
        var sidney = new GLatLng(-33.7027086456762,151.0772458659653);
        var tokyo = new GLatLng(35.56859494331316,139.9253242874379);

        var icon1 = new GIcon();
        icon1.image = "http://localhost/geotribu/icons/marker/green-dot.png";
        icon1.shadow = "http://localhost/geotribu/icons/marker/shadow-dot.png";
        icon1.iconSize = new GSize(32,32);
        icon1.shadowSize = new GSize(49,32);
        icon1.iconAnchor = new GPoint(16,32);
        icon1.infoWindowAnchor = new GPoint(16,16);

        var icon2 = new GIcon();
        icon2.image = "http://localhost/geotribu/icons/marker/red-dot.png";
        icon2.shadow = "http://localhost/geotribu/icons/marker/shadow-dot.png";
        icon2.iconSize = new GSize(32,32);
        icon2.shadowSize = new GSize(49,32);
        icon2.iconAnchor = new GPoint(16,32);
        icon2.infoWindowAnchor = new GPoint(16,16);

        var marker1 = new GMarker(paris,icon1);
        var marker2 = new GMarker(new_york,icon2);
        var marker3 = new GMarker(los_angeles,icon2);
        var marker4 = new GMarker(caracas,icon2);
        var marker5 = new GMarker(rio_de_janeiro,icon2);
        var marker6 = new GMarker(le_cap,icon2);
        var marker7 = new GMarker(dar_es_salam,icon2);
        var marker8 = new GMarker(moscou,icon2);
        var marker9 = new GMarker(pekin,icon2);
        var marker10 = new GMarker(mumbay,icon2);
        var marker11 = new GMarker(singapour,icon2);
        var marker12 = new GMarker(sidney,icon2);
        var marker13 = new GMarker(tokyo,icon2);

        var vol1 = [paris,new_york];
        var vol2 = [paris,los_angeles];
        var vol3 = [paris,caracas];
        var vol4 = [paris,rio_de_janeiro];
        var vol5 = [paris,le_cap];
        var vol6 = [paris,dar_es_salam];
        var vol7 = [paris,moscou];
        var vol8 = [paris,pekin];
        var vol9 = [paris,mumbay];
        var vol10 = [paris,singapour];
        var vol11 = [paris,sidney];
        var vol12 = [paris,tokyo];

        var polyOptions = {geodesic:true};
        map.addOverlay(new GPolyline(vol1, "#ff0000", 2.5, 0.5, polyOptions));
        map.addOverlay(new GPolyline(vol2, "#ff0000", 2.5, 0.5, polyOptions));
        map.addOverlay(new GPolyline(vol3, "#ff0000", 2.5, 0.5, polyOptions));
        map.addOverlay(new GPolyline(vol4, "#ff0000", 2.5, 0.5, polyOptions));
        map.addOverlay(new GPolyline(vol5, "#ff0000", 2.5, 0.5, polyOptions));
        map.addOverlay(new GPolyline(vol6, "#ff0000", 2.5, 0.5, polyOptions));
        map.addOverlay(new GPolyline(vol7, "#ff0000", 2.5, 0.5, polyOptions));
        map.addOverlay(new GPolyline(vol8, "#ff0000", 2.5, 0.5, polyOptions));
        map.addOverlay(new GPolyline(vol9, "#ff0000", 2.5, 0.5, polyOptions));
        map.addOverlay(new GPolyline(vol10, "#ff0000", 2.5, 0.5, polyOptions));
        map.addOverlay(new GPolyline(vol11, "#ff0000", 2.5, 0.5, polyOptions));
        map.addOverlay(new GPolyline(vol12, "#ff0000", 2.5, 0.5, polyOptions));

        map.addOverlay(marker1);
        map.addOverlay(marker2);
        map.addOverlay(marker3);
        map.addOverlay(marker4);
        map.addOverlay(marker5);
        map.addOverlay(marker6);
        map.addOverlay(marker7);
        map.addOverlay(marker8);
        map.addOverlay(marker9);
        map.addOverlay(marker10);
        map.addOverlay(marker11);
        map.addOverlay(marker12);
        map.addOverlay(marker13);

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
    `<iframe src="http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto5.html" height="350px" width="100%"></iframe>`

[Résultat pleine page](http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto5.html)

## Remarques

Il est possible de générer l'ombre de l'icône du marqueur en ligne à cette adresse : [Google Maps API Icon Shadowmaker](https://web.archive.org/web/20140626090845/http://www.cycloloco.com/shadowmaker/). L'option 'geodesic' permet de visualiser une polyligne en suivant la courbure de la Terre.

## Conclusion

Il existe de nombreuses options sur les marqueurs et les polylignes - ici comment simuler la courbure de la Terre et afficher le plus court chemin entre deux points par une simple option. Toutes les options des 'overlay' sont disponibles à cette adresse - [http://code.google.com/intl/fr/apis/maps/documentation/reference.html](http://code.google.com/intl/fr/apis/maps/documentation/reference.html).

----

<!-- geotribu:authors-block -->
