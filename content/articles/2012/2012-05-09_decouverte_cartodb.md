---
title: "A la découverte de CartoDB"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2012-05-09
description: "A la découverte de CartoDB"
tags:
    - database
    - CartoDB
    - open source
    - PostGIS
---

# A la découverte de CartoDB

:calendar: Date de publication initiale : 09 mai 2012

## Introduction

![logo CartoDB](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/cartodb.png "logo CartoDB"){: .img-thumbnail-left loading=lazy }

Il y a plusieurs semaines, j'avais reçu mon précieux sésame me permettant d'accéder au service [CartoDB](http://cartodb.com/). Malheureusement, le manque de temps ne m'a pas permis de vous faire un retour immédiat. Je profite donc de ce Week-End pour revenir sur ce service créé par [Vizzuality](http://vizzuality.com/) qui vous permet :

1. de stocker vos données dans une base [Postgis](http://postgis.refractions.net/),
2. d'y accéder ensuite via une [API](https://developers.cartodb.com/api/) SQL ou cartographique.

En fonction de vos besoins, [quatre modes d’adhésion](http://cartodb.com/pricing) sont proposés dont un totalement gratuit. C'est ce dernier que nous utiliserons pour nos tests. Découvrons ensemble immédiatement les potentialités de ce projet qui en plus est [OpenSource](https://github.com/Vizzuality/cartodb).

----

## Import des données

La première étape consiste à importer ou structurer les données que nous allons utiliser. Pour cela cartoDB propose une interface d'administration que je trouve assez bien conçue. Trois options sont proposées :

- la création d'une table vide
- l'import de données stockées sur votre ordinateur
- l'import de données accessibles sur le net

Pour ces deux dernières options, les formats autorisés sont notamment le CSV, GeoJSOn ou encore le Shapefile. Dans le cas d'un fichier ne contenant pas d'entités géographiques (ex : CSV) vous pourrez par la suite réaliser une opération de géocodage en fonction des informations dont vous disposez (ex : champs longitude/latitude).

![Create Table](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2012/2_createTable.png "Create Table"){: .img-center loading=lazy }

L'opération est relativement intuitive et ne demande pas de connaissances particulières. Une fois les données importées, vous pouvez les consulter sous la forme d'une table attributaire ou alors d'une carte interactive.

### Paramétrages des données

#### Table attributaire

La table attributaire permet de consulter ou modifier les données enregistrées. Vous pouvez également, si vous le souhaitez, effectuer une requête SQL afin de filtrer les résultats, effectuer une opération d’agrégation, ou même encore supprimer des données.

![Table](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2012/table_shp.png "Table"){: .img-center loading=lazy }

#### Personnalisation des données

Maintenant que nous avons vérifié nos données attributaires, passons au paramétrage de la carte. En fonction du type d'informations, différentes représentations cartographiques sont disponibles. Dans notre cas, nous avons choisi de représenter la population totale sous la forme d'un aplat de couleur (carte choroplèthe). Bien évidemment, les puristes me diront qu'une valeur absolue ne peut être affichée qu'avec des symboles proportionnels. Malheureusement, c'est pour le moment le seul mode de représentation disponible.

Dans le monde du GeoWeb, ce n'est pas encore aujourd'hui que nous arriverons à saisir tous les préceptes et les subtilités de [M. Bertin](https://fr.wikipedia.org/wiki/Jacques_Bertin_%28cartographe%29) (si ce nom vous est inconnu (*honte à vous*), n'hésitez pas à jeter un œil à cet [article](http://cybergeo.revues.org/554?id=554&lang=en&lang=fr)).

![Carte choroplèthe](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2012/choropleth_map.png "Carte choroplèthe"){: .img-center loading=lazy }

La gamme de couleurs proposée par défaut ne vous convient pas ? Sachez qu'il est facile de modifier le style de votre carte en utilisant une syntaxe similaire au [CSS](https://fr.wikipedia.org/wiki/Feuilles_de_style_en_cascade). Dans l'exemple ci-dessous, j'ai spécifié que tous les pays dont la population est supérieure à 1312978855 doivent apparaître en noir.

![Style](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2012/style_css.png "Style"){: .img-center loading=lazy }

Comme vous pouvez le constater, l'interface intuitive permet une prise en main rapide. Mais bon, s'amuser avec une carte dans l'administration c'est bien, mais l'objectif est tout de même de publier nos données. Voyons voir immédiatement comment réaliser cela.

### Publier vos données

Pour publier vos données, CartoDB a la particularité de proposer trois interfaces de programmation (API).

La première n'est pas vraiment une API mais plutôt une iframe [HTML](http://developers.cartodb.com/documentation/using-cartodb.html#sharing_map). En effet, il vous suffit d'une simple URL pour afficher vos données.

La seconde est une [API SQL](http://developers.cartodb.com/documentation/cartodb-apis.html#sql_api).

Enfin, la dernière est une API [cartographique](http://developers.cartodb.com/documentation/cartodb-apis.html#maps_api). Étudions chacune d’entre-elles

#### iFrame HTML

C'est la manière la plus simple de publier vos données. Pas de programmation, juste une URL. Celle-ci se présente de la manière suivante :

```http
https://{account}.cartodb.com/tables/{table_name}/embed_map
```

Par exemple, j'ai créé une table nommée world qui contient les pays du monde. Si je souhaite maintenant en faire une carte il me suffit d'écrire l'URL suivante :

```http
https://geotribu.cartodb.com/tables/world/embed_map
```

Pour le moment la carte apparaît comme je l'ai pré-paramétrée dans mon interface d'administration. Néanmoins, si je le souhaite, rien ne m'empêche de demander à ne voir que ceux dont la population est supérieure à 10 millions. J'aurais donc l'URL suivante :

```http
https://geotribu.cartodb.com/tables/world/embed_map?sql=SELECT * FROM world WHERE pop2005>10000000
```

Ce qui me donne visuellement la carte suivante :

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="https://geotribu.cartodb.com/tables/world/embed_map?sql=SELECT * FROM world WHERE pop2005&gt;10000000" width="500" height="500"></iframe>`

#### API SQL

Bon, cette carte déjà toute pré-paramétrée c'est très bien, mais comment faire si nous souhaitons accéder à directement à nos données ? C'est là qu'intervient [l'API SQL](http://developers.cartodb.com/documentation/cartodb-apis.html#sql_api). Grâce à celle-ci, vous pourrez directement interroger vos données en base au moyen d'un simple appel html. Pour cela, il vous suffit de suivre le modèle ci-dessous :

```http
<http://{account}.cartodb.com/api/v2/sql?q={SQL> statement}
```

Si vous vous y connaissez un peu en SQL, cela ne devrait pas être sorcier. Imaginons que je souhaite récupérer les attributs de la France. Cela se fait de la manière suivante :

```http
https://geotribu.cartodb.com/api/v2/sql?q=SELECT * FROM world WHERE name like 'France'
{ "time":0.007, "total_rows":1,
  "rows": [{
     "fips":"FR",
     "iso2":"FR",
     "iso3":"FRA",
     "un":250,
     "name":"France",
     "area":55010,"pop2005":60990544,
     "region":150,
     "subregion":155,
     "lon":2.55,
     "lat":46.565,
     "the_geom":"010600 [...] 515941"
   }]
}
```

Bon et maintenant, comment faire si je souhaite que toute la réponse soit au format GeoJSON et non pas juste la géométrie ? Il vous suffit simplement de spécifier dans votre appel html le paramètre 'format=geojson' :

```rest
https://geotribu.cartodb.com/api/v2/sql?q=SELECT * FROM world WHERE name like 'France'&format=geojson
{ "type":"FeatureCollection",
  "features":[{
     "type":"Feature",
     "properties": { "fips":"FR",
     "iso2":"FR",
     "iso3":"FRA",
     "un":250,
     "name":"France",
     "area":55010,
     "pop2005":60990544,
     "region":150,
     "subregion":155,
     "lon":2.55,
     "lat":46.565,
     "cartodb_id":65,
     "created_at":"2012-01-15T16:00:16.637Z",
     "updated_at":"2012-02-21T08:04:31.354Z"},
     "geometry":{
         "type":"MultiPolygon",
         "coordinates":[[[[9.48583200000013,42.615273000000116], [...], [2.541667000000132,51.09111000000007]]]]
      }
  }]
}
```

Et maintenant, comment faire si nous souhaitons afficher cela ? Rien de plus facile, quelques petites lignes de code et le tour est joué. Pour cela nous utiliserons l'API [OpenLayers](https://openlayers.org/) :

```js
var map = new OpenLayers.Map(
    {
        div: "map",
        layers: [
            //Ajout d'un fond de carte osm
            new OpenLayers.Layer.OSM(),
            //Ajout de notre couche vecteur
            new OpenLayers.Layer.Vector(
                "Vectors", {
                projection: new OpenLayers.Projection("EPSG:4326"), strategies: [new OpenLayers.Strategy.Fixed()], protocol: new OpenLayers.Protocol.Script({
                    //URL du service CartoDB
                    url: "http://geotribu.cartodb.com/api/v2/sql", params: { q: "select * from world where name like 'France'", format: "geojson" }, format: new OpenLayers.Format.GeoJSON({ ignoreExtraDims: true }), callbackKey: "callback"
                }),
                //Quand toutes les données ont été ajoutées, on zoom sur l'extent
                eventListeners: { "featuresadded": function () { this.map.zoomToExtent(this.getDataExtent()); } }
            })]
    });
```

Et maintenant la carte :

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://geotribu.net/applications/cartodb/index_ol.html" width="640" height="480" frameborder="0"></iframe>`

Comme vous pouvez le constater, l'API SQL vous permet avec quelques connaissances SQL d'accéder facilement à vos données. Mais pour le moment, toutes les données que nous avons récupérées sont au format vectoriel. Bien que cela soit pratique pour l’interactivité, ce n'est néanmoins pas la meilleure solution lorsqu'il y a de gros volumes de données. Pour y remédier, voyons comment utiliser l'API cartographique.

#### API Cartographique

Tout comme l'API SQL, [l'API cartographique](http://developers.cartodb.com/documentation/cartodb-apis.html#maps_api) vous permet d'accéder à vos données mais cette fois sous la forme d'une carte ou plus précisément, sous la forme de tuiles. C'est à vous ensuite de "construire" la partie cartographique grâce à l'une des API existantes (Google Maps, Leaflet, OpenLayers, etc.).

Même si vous ne devriez pas avoir à manipuler directement les tuiles, il est toujours bon de savoir comment cela fonctionne. Tout comme les précédents exemples, un simple appel HTML est suffisant :

`http://{account}.cartodb.com/tiles/{table_name}/{z}/{x}/{y}.png`

[![Tuiles](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2012/poster-coordinates.gif "Tuiles"){: .img-center loading=lazy }](http://www.maptiler.org/google-maps-coordinates-tile-bounds-projection/)

Le début de l'appel ne vous est pas inconnu. Mais à quoi correspondent les {z}, {x}, {y} ? En fait, cela permet tout simplement d'indiquer l'image à récupérer car derrière se "cache" un système de pyramide de tuiles. Les paramètres x et y indiquent la cellule exacte de la grille et z le niveau de zoom.

Bon assez de théorie et passons à la pratique. En réalité, vous n'avez pas à vous soucier de ce système de tuiles. C'est la librairie que vous utiliserez qui s'en chargera. La plupart des API existantes disposent d'une classe implémentant déjà les protocoles nécessaires à la gestion des données tuilées. Prenez par exemple la [classe XYZ](http://dev.openlayers.org/docs/files/OpenLayers/Layer/XYZ-js.html) d'OpenLayers ou encore la [classe TileLayer](http://leaflet.cloudmade.com/reference.html#tilelayer) de LeafLet.

#### Intégration avec Leaflet

[Leaflet](http://leaflet.cloudmade.com) est une API cartographique OpenSource initiée par la société [CloudMade](http://cloudmade.com/). D'un mon point de vue elle possède moins de fonctionnalités que son homologue [OpenLayers](https://openlayers.org/) mais elle est aussi justement plus simple à prendre en main. C'est pourquoi nous l'utiliserons dans le cadre de ce billet.

L'intégration de CartoDB et de Leaflet semble assez simple puisque vous disposez d'une [classe déjà pré-paramétrée](https://github.com/Vizzuality/cartodb-leaflet/). Avant de faire votre première carte, nous aurons besoin de télécharger quelques librairies à savoir : [leaflet](http://leaflet.cloudmade.com) (bien évidemment) et [wax](http://mapbox.com/wax/) (tiens je ne la connaissais pas celle-là !). Ensuite, quelques lignes de code et le tour est joué :

```js
function init() {
    var map = new L.Map('map_canvas').setView(new L.LatLng(20, 0), 3);
    var cloudmadeUrl = 'http://{s}.tile.cloudmade.com/BC9A493B41014CAABB98F0471D759707/997/256/{z}/{x}/{y}.png', cloudmadeAttrib = 'Map data © 2011 OpenStreetMap contributors, Imagery © 2011 CloudMade', cloudmade = new L.TileLayer(cloudmadeUrl, { maxZoom: 18, attribution: cloudmadeAttrib });
    map.addLayer(cloudmade);
    var cartodb_leaflet = new L.CartoDBLayer({ map_canvas: 'map_canvas', map: map, user_name: 'geotribu', table_name: 'world', query: "SELECT * FROM {{table_name}}", auto_bound: false });
}
```

Si vous avez tout suivi correctement, vous devriez alors avoir une [application similaire](http://geotribu.net/applications/cartodb/index.html) à celle ci-dessous :

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://geotribu.net/applications/cartodb/index.html" width="640" height="480" frameborder="0"></iframe>`

En vous couplant à des API cartographiques, vous pourrez bien évidemment créer des applications bien plus élaborées. Il ne tient qu'à vous de réaliser ce que vous souhaitez !

## Conclusion

Nous arrivons au terme de notre découverte de CartoDB. Je dois avouer que j'ai été agréablement surpris par ce service. L'interface est bien pensée tout comme les différents modes d'intégration. Ca se voit que les mecs qui sont derrière ont bossé dessus !

Concernant les tarifs, lors de nos tests nous avons utilisé la version gratuite. Néanmoins, cette offre est limitée à 5 tables en accès public et à 5 MB de données. Bizarrement sur mon interface, j'ai droit à 100 MB peut être est-ce dû au fait que je me suis inscrit dès la bêta. Mais, pour une petite utilisation, cela est largement suffisamment. Rien ne vous empêche ensuite de basculer vers une des [offres contractuelles](http://cartodb.com/pricing) proposées. En terme de prix, je trouve cela très correct. En effet, vous pouvez opter pour une 1ère formule à 30€ par mois sinon basculer vers des offres plus pro à 150€ par mois.

Au-delà de notre "petit" test, lecteur de géotribu, avez-vous déjà essayé cette solution ? Quelles ont été vos impressions ? N'hésitez pas à nous le faire partager grâce aux commentaires.

----

<!-- geotribu:authors-block -->
