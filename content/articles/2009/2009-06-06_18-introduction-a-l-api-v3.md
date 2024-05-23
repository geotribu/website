---
title: 18. Introduction à l'API v3
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2009-06-06
description: 18. Introduction à l'API v3
tags:
    - API
    - Google Maps
---

# 18. Introduction à l'API v3

:calendar: Date de publication initiale : 06 juin 2009

## Introduction

![logo Google Maps](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google_maps.png "logo Google Maps"){: .img-thumbnail-left}

La nouvelle API de Google Maps est sensiblement identique à la version 2. Pour les développeurs connaissant l'API v2, ce ne devrait pas être trop déroutant, juste un peu plus simple et logique - selon moi.  

## Initialisation

Afin de garantir l'utilisation de la carte sur tous les supports Internet, il est nécessaire de définir dans les méta que la carte sera affichée pleine page et que l'utilisateur ne pourra pas modifier la taille de cette dernière.  

`<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />`

L'appel à l'API se fait maintenant sans avoir besoin de clé - quel est le devenir de l'[API Google Maps Premier](http://www.google.fr/enterprise/maps/) ?  

`<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>`

Ici nous ne travaillerons pas à le 'sensor' de l'utilisateur.  

## Construction de l'objet 'map'

Une des nouveautés de cette API est le fait qu'il faille initialiser les paramètres de position et de zoom du centre, et les paramètres de type de couche avant de construire l'objet carte, dans un souci de performance, ces options seront des objets 'non construits' et donc littéraux :  

```javascript
var latlng = new google.maps.LatLng(48.856667, 2.350987);
    var myOptions = {
      zoom: 13,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
```

Et enfin nous initialisons la carte avec le nouveau appel typique à cette nouvelle version : google.maps à la place de GMaps2 :  

`var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);`  

## Corps de la page HTML

Toujours dans le souci d'affichage sur les mobiles nouvelle génération, nous définissons la taille de la carte sur tout l'espace disponible du navigateur.  

```html
<body style="margin:0px; padding:0px;" onload="initialize()">
  <div id="map_canvas" style="width:100%; height:100%"></div>
</body>
```

## Code complet

```html
<html>
<head>
<meta name="viewport" content="initial-scale=1.0, user-scalable=no" />
<script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>
<script type="text/javascript">
  function initialize() {
    var latlng = new google.maps.LatLng(48.856667, 2.350987);
    var myOptions = {
      zoom: 13,
      center: latlng,
      mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);
  }
</script>
</head>
<body style="margin:0px; padding:0px;" onload="initialize()">
  <div id="map_canvas" style="width:100%; height:100%"></div>
</body>
</html>
```

## Démonstration

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto18.html" height="350px" width="550px"></iframe>`

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto18.html)

## Remarques

La documentation de l'API v3 se trouve cette à cette adresse : <http://code.google.com/intl/fr/apis/maps/documentation/v3/>

## Conclusion

Bien qu'encore à l'état bêta, il est tout à fait possible de créer une simple carte - sans se soucier des contrôles - accessible rapidement par les ordinateurs de bureau et les smartphones 3G. Le reste des fonctions et services disponibles sur la version 2 de l'API seront progressivement adaptés sur la version 3. Nous les essayerons au fur et à mesure de leur sortie.

----

<!-- geotribu:authors-block -->
