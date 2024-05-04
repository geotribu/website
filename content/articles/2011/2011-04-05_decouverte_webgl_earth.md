---
title: "A la découverte de WebGL Earth"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2011-04-05
description: "A la découverte de WebGL Earth"
tags:
    - JavaScript
    - open source
    - WebGL
---

# A la découverte de WebGL Earth

:calendar: Date de publication initiale : 05 avril 2011

![icône globe](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "icône globe"){: .img-thumbnail-left }

Depuis quelques mois déjà nos billets font de plus en plus référence à l'utilisation de la 3D au sein de l'univers du Web. L'intégration de la librairie [WebGL](https://fr.wikipedia.org/wiki/WebGL), par les navigateurs les plus récents, montre bien que cette composante fera partie intégrante de nos prochaines façons de surfer. Profitant de la sortie récente de firefox 4, je me suis penché sur WebGl Earth. Ce projet initié par la société [klokantech](http://www.klokantech.com/) vise à remplacer nos interfaces cartographiques planes par un véritable globe directement dans votre navigateur. Bien évidemment, vous pourriez me dire que Google Earth est disponible depuis longtemps sur le Web via son [API](http://code.google.com/apis/earth/), mais cela nécessite l'installation d'un plugin spécifique. Tout l’avantage de se baser sur WebGL c'est que tout l'environnement est déjà intégré à votre navigateur. D'ailleurs, on pourrait même se demander si un scenario similaire à la [Google Gears](http://pro.01net.com/editorial/509349/google-delaisse-gears-au-profit-d-html-5/) ne serait pas en gestation chez Google ? Néanmoins revenons à nos moutons et à WebGl Earth.

!!! warning
    Juste un rappel au cas où vous ne l'auriez pas remarqué, ce tutoriel nécessite un navigateur (très) récent (Firefox 4, Chrome 9 etc.).

## Hello World

N'ayez pas peur, vous n'aurez pas besoin de connaissances spécifiques en 3D ! Juste quelques notions de JavaScript seront nécessaires. Surtout cela sera l'occasion de voir que vous pouvez avec juste quelques lignes de codes construire votre propre application. Allé commençons avec l'habituel "[Hello World](http://www.webglearth.org/api)" :

```html
<!DOCTYPE HTML>
<html>
<head>
<script src="http://www.webglearth.com/api.js"></script>
<script>
  function initialize() {
    var options = { zoom: 3.0, center: [47.19537,8.524404] };
    var earth = new WebGLEarth('earth_div', options);
  }
</script>
</head>
<body onload="initialize()">
  <h1>WebGL Earth API: Hello World</h1>
  <div id="earth_div" style="width:600px;height:400px;border:1px solid gray;"></div>
</body>
</html>
```

Ce qui nous donne donc l'application suivante :

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://webglearth.googlecode.com/svn/trunk/api/examples/helloworld.html" width="700px" height="500px"></iframe>`

Les habitués d'OpenLayers ou de Google Maps ne seront pas surpris par le code affiché. Rien de bien sorcier. En effet, dans un premier temps nous définissons quelques options et ensuite nous instançons l'objet WebGLEarth. Celui-ci prend en paramètre l'identifiant de la balise div qui contiendra le globe ainsi que les options que nous avons définies auparavant. Vous voyez, je ne vous avais pas menti, 2 lignes de code pour réaliser. Amusez-vous à changer les paramètres définis en entrée pour par exemple centrer votre carte sur Paris : `center: [48.8594, 2.3482]`.

## Changer la couche par défaut

Par défaut, la couche qui s'affiche est celle de [MapQuest](http://www.mapquest.fr/mq/home.do) (basée sur les données d'[OpenStreetMap](https://www.openstreetmap.org/)). Mais vous pouvez personaliser votre application avec l'une des trois autres sources disponibles (OSM, Bing, Custom).

Imaginons que nous souhaitions afficher la couche OpenStreetMap, deux solutions sont alors possibles. Soit instancier la couche en même temps que notre objet WebGLEarth via la propriété map. Bizarre d'ailleurs le choix du nom de cette propriété, pourquoi ne pas l'avoir appelé layer ? Mais bon passons :

```html
<script>
  function initialize() {
    var options = {
      zoom: 3.0,
      center: [48.8594, 2.3482],
      map: WebGLEarth.Maps.OSM,
    };
    var earth = new WebGLEarth("earth_div", options);
  }
</script>
```

Ou alors, il est toujours possible de le faire par la suite :

```javascript
<script>
  function initialize() {
    var options = { zoom: 3.0, center: [48.8594, 2.3482] };
    var earth = new WebGLEarth('earth_div', options);
    earth.initMap(WebGLEarth.Maps.BING, ['Road', 'your_bing_code']);
    earth.setMap(WebGLEarth.Maps.BING, 'Road');
  }
</script>
```

Pour ce dernier exemple, nous avons dû utiliser une couche de type Bing. En effet, sauf erreur de ma part, il semblerait que la méthode setMap ne fonctionne pas pour OSM.

## Conclusion

WebGL Earth est un projet récent. Cela explique notamment le peu de fonctionnalités disponibles dans l'API. En effet, il n'est pas possible pour le moment de faire plus qu'afficher un fond cartographique. Difficile alors de réaliser une application un peu sérieuse. Espérons maintenant que les développeurs enrichiront cette prometteuse librairie et même pourquoi pas imaginer un rapprochement des communautés OpenLayers et WebGL Earth.

## Ressources

- [WebGL Earth API](http://www.webglearth.org/api)  
- [WebGL Earth Examples](http://webglearth.googlecode.com/svn/trunk/api/examples/)  
- [Code Source](http://code.google.com/p/webglearth/)

----

<!-- geotribu:authors-block -->
