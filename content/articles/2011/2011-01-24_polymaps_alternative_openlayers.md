---
title: "PolyMaps une alternative à OpenLayers"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2011-01-24
description: "PolyMaps une alternative à OpenLayers"
tags:
    - JavaScript
    - maps
    - Polymaps
---

# PolyMaps une alternative à OpenLayers

:calendar: Date de publication initiale : 24 janvier 2011

![logo polymaps](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/polymaps.png){: .img-thumbnail-left }

Cela faisait longtemps que j'avais l'onglet du site de [PolyMaps](http://polymaps.org/) ouvert dans mon navigateur. Par manque de temps, je n'avais pas encore eu l'occasion d'explorer cette récente bibliothèque cartographique. Développant principalement sur l'API Google Maps et [OpenLayers](https://openlayers.org/), j'avais envie de tester la capacité de cette bibliothèque et de juger si celle-ci pouvait à terme devenir une réelle alternative.  

Après avoir jeté un rapide coup d'œil aux différents exemples (ex [PolyMaps](http://polymaps.org/ex/)), passons concrètement à notre exploration.

Développé en collaboration par [SimpleGeo](http://simplegeo.com/) et [Stamen Design](http://stamen.com/), PolyMaps est une librairie cartographique développée en JavaScript. Le rendu des différents éléments utilise le format [SVG](https://fr.wikipedia.org/wiki/Scalable_Vector_Graphics).

## Téléchargement

Pour cela, se rendre sur la page [ah-hoc](http://polymaps.org/download.html) et télécharger le zip de la dernière version - la 2.4 pour ce mois de janvier 2011.  
Et décompresser cette archive quelque part sur votre serveur.

```bash
unzip simplegeo-polymaps-v2.4.0-0-g42b145f.zip
```

## Initialisation

Si vous êtes un peu familier du développement sous [OpenLayers](http://www.openlayers.org/) ou [Google Maps](http://code.google.com/intl/fr-FR/apis/maps/index.html), vous n'allez pas être trop dépaysé. Et en plus si vous avez déjà tâté du [jQuery](http://jquery.com/), vous ne serez pas surpris par le chaînage - c'est-à-dire le fait d'aligner les fonctions sur un même objet (puisqu'une fonction retourne toujours l'objet sur lequel elle a été appliquée).  

Attaquons directement en codant un petit exemple que nous allons détailler. Avec Polymaps, pas trop de surprise, il faut appeler l'API Javascript et construire notre carte : tout comme Google Maps ou OpenLayers.

```css
@import url("lib/js/examples/example.css");
body { margin: 0px; padding: 0px; }
#map { width: 100%; height: 100%; }  
```

Je ne détaille pas le fichier de style example.css, mais celui-ci regroupe notamment les styles des boutons de zoom + et - .  

## JavaScript

Maintenant le JavaScript - le fichier test1.js - de construction de la carte :

```js
var po = org.polymaps;

var map = po.map()  
.container(document.getElementById("map").appendChild(po.svg("svg")))  
.add(po.interact())  
.add(po.hash());

map.add(po.image()  
.url(po.url("http://{S}tile.cloudmade.com"  
+ "/25e1c714473b482e9414c63afee96b22" // ici mettre votre clé Cloudmade  
+ "/998/256/{Z}/{X}/{Y}.png")  
.hosts(["a.", "b.", "c.", ""])));

map.add(po.compass()  
.pan("none"));  
```

L'exemple ci-dessus affiche une carte glissante provenant de chez [Cloudmade](http://cloudmade.com/).  

Tout d'abord l'initialisation :

```js
var po = org.polymaps;  
```

Il s'agit juste d'un raccourci pour éviter à avoir à re-saisir org.polymaps à chaque fois. Nous voyons qu'ici à la différence de Google Maps, Polymaps n'utilise pas le mot clé *new* pour construire les objets mais utilise une méthode [différente](https://fr.wikipedia.org/wiki/Fabrique_(patron_de_conception)).  

Ensuite la construction de la carte :

```js
var map = po.map()  
.container(document.getElementById("map").appendChild(po.svg("svg")))  
.add(po.interact());  
```

Nous voyons bien le chaînage mis en place :

* `po.map` : constructeur ;
* `container(...)` : ajout de la carte dans le conteneur défini dans le HTML, ce conteneur doit être un SVG, on ajoute donc la méthode `appendChild(po.svg("svg"))` qui est une méthode équivalente à celle-ci : `document.createElementNS("<http://www.w3.org/2000/svg>") ;`
* `add(po.interact())` : ajout des contrôles de carte - déplacement, double-clic, zoom à la molette et 'pilotage' avec les flèches.

Ajoutons ensuite une URL vers une carto jolie :

```js
map.add(po.image()  
.url(po.url("http://{S}tile.cloudmade.com"  
+ "/25e1c714473b482e9414c63afee96b22" // ici votre clé Cloudmade  
+ "/998/256/{Z}/{X}/{Y}.png")  
.hosts(["a.", "b.", "c.", ""])));  
```

Dans l'ordre :

* `map.add(po.image()` : ajout d'une *couche* ;
* `.url(po.url( ... )` : qui possède cette URL Cloudmade ;
* `.hosts(["a.", "b.", "c.", ""])` : là aucune idée, si vous avez des pistes ...

Et ensuite ajoutons le contrôle de zoom in et out :

```js
map.add(po.compass()  
.pan("none"));  
```

Centrons la carte sur Saint-Malo et choisissons un niveau de zoom :

```js
map.center({lat: 48.6356, lon: -2.0448});  
map.zoom(12.0);  
```

Et ajoutons les copyright :wink: :

```txt
© 2010  
[CloudMade](http://www.cloudmade.com/),  
[OpenStreetMap](https://www.openstreetmap.org/) contributors,  
[CCBYSA](http://creativecommons.org/licenses/by-sa/2.0/).  
```

## Première conclusion

Pour une entrée en matière, j'ai trouvé cette bibliothèque plutôt réussie - ça tourne parfaitement - et facile à utiliser : avec les quelques exemples en ligne, il est facile de commencer une première carte. Et ça permet de mettre un joli fond de carte provenant de CloudMade. Pour le moment, rien à dire, c'est bien fait. Evidemment, cette bibliothèque ne peut pas être comparée à OpenLayers - beaucoup plus complète.  
Mais nous n'avons pas testé le SVG qui fait sa spécificité. Nous essaierons dans un prochain article de faire une carte choroplèthe.

----

<!-- geotribu:authors-block -->
