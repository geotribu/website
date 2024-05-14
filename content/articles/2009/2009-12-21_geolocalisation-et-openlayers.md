---
title: Géolocalisation et OpenLayers
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2009-12-21
description: Géolocalisation et OpenLayers
tags:
    - géolocalisation
    - HTML 5
---

# Géolocalisation et OpenLayers

:calendar: Date de publication initiale : 21 décembre 2009

## Introduction

Lorsque vous vous connectez à Internet il est dorénavant possible qu'une application tierce puisse connaitre, avec votre autorisation, votre position. Le fonctionnement est expliqué en détail sur le site de [Mozilla](http://fr.www.mozilla.com/fr/firefox/geolocation/). Globalement, lors de votre connexion à un site utilisant la géolocalisation, votre navigateur va rassembler des informations sur les points d'accès sans fil alentour et votre adresse IP. Ces informations seront alors soumises à Google Location Services qui renverra alors une estimation de votre position.

Avant d'aborder le côté technique, je tiens à souligner mon pessimisme quant à l'utilisation de "Google Location Services" en tant que provider. À mon sens, les standards du Web devraient pouvoir être indépendants de tout partenaire commercial ou non. Enfin, c'est un autre débat, reprenons notre tutoriel !

Si vous souhaitez approfondir la notion de Géolocalisation et d'HTML 5, je vous conseille la lecture de [diveintoHTML5](http://diveintohtml5.org/geolocation.html).

## La géolocalisation au coeur de votre navigateur

Nous avons vu globalement comment fonctionne la géolocalisation, mais concrètement qu'est-ce qui se traficote au sein de votre navigateur une fois le résultat retourné? Pour ceux qui en ont le courage, je vous suggère la lecture des [spécifications du W3C](http://dev.w3.org/geo/api/spec-source.html), vous saurez ensuite sur le bout des doigts comment cela fonctionne. Pour les plus fainéants, faisons un rapide résumé.

Premièrement, il est nécessaire de spécifier au navigateur client que nous allons utiliser l'API de géolocalisation. Cela se fait, dans votre script, de la manière suivante :

`navigator.geolocation.getCurrentPosition(function_de_traitement);`

Cette simple instruction aura pour effet d'activer la géolocalisation sur le poste client. Ce dernier aura alors la possibilité d'accepter ou de refuser la connexion. L'image ci-dessous, montre la demande d'activation par Firefox :

![Géolocalisation](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/geoloc.png "Géolocalisation"){: .img-center loading=lazy }

Si celle-ci est autorisée, un objet "position" contenant notamment la longitude, la latitude et l'altitude est alors construit. L'instruction de géolocalisation peut prendre jusqu'à 3 arguments, ceux-ci sont :

* La fonction qui sera lancée en cas de géolocalisation réussie
* La fonction qui sera lancée en cas d'erreur dans la géolocalisation
* Une série d'arguments optionnels (âge maximal, timeout, meilleur precision), regroupés au sein d'un objet json

Reprenons, l'exemple précédent en y ajoutant quelques paramètres :  

```javascript
navigator.geolocation.getCurrentPosition(
                                geoPositionSuccess,
                                geoPositionError,
                                {maximumAge:1,enableHighAccuracy:true});
```

Passons maintenant au traitement de l'objet `position`.

## Affichage de la position grâce à openLayers

L'essentiel de notre traitement se fera dans la fonction passée en premier paramètre. Pour les besoins de notre exemple, nous allons afficher un marqueur ainsi qu'une infobulle en utilisant la position retournée par la géolocalisation.

```javascript
function geoPositionSuccess(position){  
//Feature  
var point = new OpenLayers.Geometry.Point(
                        position.coords.longitude,
                        position.coords.latitude ); //1
var feature = new OpenLayers.Feature.Vector(point, null, style); //2
vectors.addFeatures([feature]); //3
```

Etudions successivement les différentes étapes :

1. Premièrement, je récupère tout simplement ma position potentielle grâce à l'argument "position" de ma fonction `geoPositionSuccess` et je construit mon objet géometrique. L'argument "position" est automatiquement renseigné par la méthode `navigator.geolocation.getCurrentPosition()`.
2. Ceci étant fait, je créé mon objet feature à partir des renseignements précédents.
3. Enfin, j'ajoute mon nouvel objet à ma couche.

Passons maintenant au popup :

```javascript
function geoPositionSuccess(position){  
//Feature  
...
popup = new OpenLayers.Popup.FramedCloud(
    "GeoLoc",
    new OpenLayers.LonLat(point.x, point.y),  
    null,
    "lon : "+ position.coords.longitude +"<br /> lat : " + position.coords.latitude,
    null,
    false,
    null );
map.addPopup(popup);
```

Là encore rien d'exceptionnel, il me suffit d'instancier mon objet `FramedCloud` à partir des renseignements de position. Comme vous pouvez le constater je n'utilise que le basic d'OpenLayers, rien de bien sorcier !

## Exemple

Dans l'[exemple](http://geotribu.net/applications/tutoriaux/openlayers/geolocalisation/index.html) ci-dessous, votre position devrait s'affiche sur un fond OpenStreetMap (OSM). Cela ne fonctionne que si vous avez auparavant accepté l'activation de la géolocalisation. Enfin, du fait des différences de projection entre l'API de géolocalisation et (OSM) une reprojection des coordonnées géographiques a été nécessaire.

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/openlayers/geolocalisation/index.html" height="350px" width="550px"></iframe>`

----

<!-- geotribu:authors-block -->
