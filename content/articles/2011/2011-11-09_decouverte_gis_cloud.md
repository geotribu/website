---
title: "A la découverte de GIS Cloud"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2011-11-09
description: "Découverte de GIS Cloud, plateforme de création de contenu web-cartographique dont on entend beaucoup parler ces derniers temps. Bien décidé à voir de quoi il en retourne, je me suis inscrit et j'en ai profité pour faire quelques tests. Je vous livre ci-dessous mes impressions."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/serveur/giscloud/giscloud_interface.png"
tags:
    - GIS Cloud
    - HTML5
---

# A la découverte de GIS Cloud

:calendar: Date de publication initiale : 09 novembre 2011

![logo GIS Cloud](https://cdn.geotribu.fr/img/articles-blog-rdp/serveur/giscloud/giscloud_logo.jpg "logo GIS Cloud"){: .img-thumbnail-left }

Cela faisait plusieurs semaines que ma [timeline twitter](http://twitter.com/#!/geotribu) s'ornait de hashtag [GisCloud](http://www.giscloud.com). C'est vrai que les différentes [démos](http://www.giscloud.com/blog/gis-cloud-starts-html5-mapping-revolution) proposées sont tout de même impressionnantes. J'entends déjà les amoureux de la sémiologie graphique me dire que c'est une hérésie d'afficher 1 million de points sur une carte. Sur ce point, je suis tout à fait d'accord. Néanmoins, la prouesse technique est tout de même bluffante ! Du coup, bien décidé à voir de quoi il en retourne, je me suis inscrit et j'en ai profité pour faire quelques tests.

Je vous livre ci-dessous mes impressions.

## Présentation générale

Tout d'abord, vous vous demandez certainement qu'est-ce que GIS Cloud ? Il s'agit d'une infrastructure permettant :

- d'une part la création et l'hébergement d'applications cartographiques ;
- et d'autre part l'accès à ces applications grâce à une une [API Javascript](http://dev.giscloud.com/JavaScriptApi/) et une [API Rest](http://dev.giscloud.com/RestGuide).

Les [fonctionnalités](http://www.giscloud.com/features/) de GIS Cloud s'orientent en fonction des [six axes majeurs](http://www.giscloud.com/features/) suivants :

- [Outils cartographiques collaboratifs](http://www.giscloud.com/features/collaboration-map-management)
- [Partage et publication de cartes sur Internet](http://www.giscloud.com/features/share-and-publish-on-web)
- [Intégration des plate-formes mobiles](http://www.giscloud.com/features/mobile-data-collection)
- [Cartographies thématiques](http://www.giscloud.com/features/thematic-maps-analysis)
- [Intégration aux systèmes déjà existants](http://www.giscloud.com/features/integrate-with-existing-systems/)
- [Cloud personnel](http://www.giscloud.com/features/personal-cloud/)

La [liste complète](http://www.giscloud.com/full-feature-list/) des fonctionnalités est bien trop exhaustive pour que je vous la cite içi. Néanmoins, n'hésitez pas à y jeter un coup d'œil pour avoir plus d'informations.

Après cette brève présentation, entrons dans le vif du sujet et voyons voir ce qui se cache derrière GIS Cloud.

## Création cartographique

Une fois mon inscription réalisée, je peux maintenant accéder à l'interface de création cartographique. C'est à partir de celle-ci que nous allons importer nos données, spécifier le style désiré, etc. Toutes les possibilités sont expliquées dans la [documentation](http://www.giscloud.com/docs/).

![GIS Cloud - Interface](https://cdn.geotribu.fr/img/articles-blog-rdp/serveur/giscloud/giscloud_interface.png "GIS Cloud - Interface"){: .img-center loading=lazy }

Me voilà maintenant prêt à créer une nouvelle carte. La première étape est bien évidemment d'ajouter les données désirées. Dans un premier temps, je vais commencer par ajouter un fond de carte. Au choix vous avez, Google Maps (maps, satellite, terrain), 3Tier Wind 80m, Bing Maps ou encore Open Street Map. Bien évidemment, mon choix s'est porté sur ce dernier.

![GIS Cloud - Données OSM](https://cdn.geotribu.fr/img/articles-blog-rdp/serveur/giscloud/osm_data.png "GIS Cloud - Données OSM"){: .img-center loading=lazy }

Passons maintenant à nos données vecteurs. La liste des formats qu'il est possible d'importer, sans être exhaustive, est néanmoins suffisante. En effet, GIS Cloud permet l'accès aux fichiers Shapefile, MapInfo, KML, CSV, PNG, etc. Pour les besoins de notre test, j'ai téléchargé les données [OpenStreetMap](https://www.openstreetmap.org/) au [format Shapefile](http://download.geofabrik.de/osm/europe/france/) proposé par [GeoFabrik](http://www.geofabrik.de/). Étant donné le poids de mes fichiers (+ de 200 Mo) l'import prend un peu de temps. Croisez les doigts en espérant que tout se passe bien et au bout d'une heure la liste de vos fichiers apparaît enfin. Vous n'avez plus qu'à sélectionner la couche désirée et à l'ajouter à l'interface. Attention, là encore cela peut prendre pas mal de temps !

![GIS Cloud - Données OSM](https://cdn.geotribu.fr/img/articles-blog-rdp/serveur/giscloud/data_osm_shp.png "GIS Cloud - Données OSM"){: .img-center loading=lazy }

En plus des fichiers classiques, vous pouvez également connecter une base de données PostGis. Néanmoins, c'est une base de données locale. L’intérêt est donc un peu limité. Mais pour le test, j'ai intégré la couche de points des données OSM.

![GIS Cloud - PostGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/serveur/giscloud/postgis_db.png "GIS Cloud - PostGIS"){: .img-center loading=lazy }

Me voici maintenant avec ma carte et mes données. Profitons-en pour modifier la symbologie des couches.

![GIS Cloud - styling](https://cdn.geotribu.fr/img/articles-blog-rdp/serveur/giscloud/styling.png "GIS Cloud - styling"){: .img-center loading=lazy }

Et voilà, tout est correctement paramétré. Il me reste maintenant à publier mon projet pour qu'il soit accessible sur le web.

## Publication du projet

Une fois mon projet configuré comme je le souhaite, il me suffit maintenant de le publier sur le web. Pour cela différentes options sont possibles. Tout d'abord, je peux tout simplement fournir le [lien permanent](http://www.giscloud.com/map/19062/openstreetmappaca). Les utilisateurs auront alors accès à mon projet au travers de l'interface de la plateforme GisCloud. Mais, une intégration plus poussée est également possible. En effet, vous pouvez (par ordre de difficulté) ajouter votre projet à une page web sous la forme d'une iframe, intégrer le flux Web Map Service (WMS) généré, ou alors coder une application grâce à l'API Javascript.

Testons immédiatement l'iframe. Il me suffit donc de spécifier l'URL de GisCloud ainsi que l'ID de mon projet pour voir ma carte s'afficher. Il est également possible d'ajouter un arbre des couches avec l'option layerlist=true, ou une barre d'outils avec l'option `toolbar=true`.

![GIS Cloud - embed](https://cdn.geotribu.fr/img/articles-blog-rdp/serveur/giscloud/gisCloud_embed.png "GIS Cloud - embed"){: .img-center loading=lazy }

Et voilà, en quelques secondes, mon projet est publié :

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="https://app.giscloud.com/rest/1/maps/19062/render.iframe?map=19062&bound=809726.1045104787,5420082.793302087,817035.395340249,5417216.404741392" title="GIS Cloud test" height="500px"></iframe>`

## Flux WMS

Mais, peut-être souhaitez-vous simplement diffuser vos couches sur le net sans pour autant vous embarrasser d'une application cartographique. Dans ce cas, il vous suffira de rendre public le flux WMS généré par GisCloud. J'entre alors l'url du WMS dans QGIS mais j'obtiens une erreur !

Au départ, je pensais que QGIS était en cause mais après avoir tapé un `getCapabilities` du WMS dans mon navigateur, j'ai toujours cette même erreur :

`RuntimeError: failed to initialize projection with:+init=epsg:901023`

Cela proviendrait donc de GisCloud. Je retenterai l'expérience dans quelques jours pour voir cela ne provient pas d'un simple incident technique isolé.

## API Javascript

Dernier moyen d'intégrer une carte GisCloud, son [API Javascript](http://dev.giscloud.com/JavaScriptApi/ApiReference).

En effet, si vous le souhaitez, vous pouvez coder votre propre application cartographique. Pour cela, commencez par lire le [tutoriel](http://dev.giscloud.com/JavaScriptApi/GettingStarted) qui vous guidera dans vos premiers pas et n'hésitez pas non plus à consulter les [différents exemples](https://github.com/giscloud/GIS-Cloud-Examples) disponibles. Celui sur les [markers](http://dev.giscloud.com/examples/markermethods.html) est bien sympathique.

Je me demande si je ne vais pas copier l'idée et essayer de faire quelque chose de similaire pour OpenLayers. Mais bon, là n'est pas le sujet de cet article, revenons à notre API Javascript. Pour cela, nous allons tout simplement afficher notre carte précédemment créée. Une fois ma page correctement configurée, cela se fait en à peine une ligne de code :

```js
simple mapping app example
```

Le résultat obtenu est le suivant :

![GIS Cloud - API](https://cdn.geotribu.fr/img/articles-blog-rdp/serveur/giscloud/api_1.png "GIS Cloud - API"){: .img-center loading=lazy }

Allez, ajoutons maintenant une barre d'outils :

```js
giscloud.ready(function () {
    // create a viewer
    var viewer = new giscloud.Viewer("map", 19062, { slider: true }); // create a toolbar
    var toolbar = new giscloud.ui.Toolbar({
        viewer: viewer,
        container: "toolbar", defaultTools: ["pan", "zoom", "full"]
    });
});
```

Et voilà en image le résultat. Notez, la barre d'outils en haut à gauche :

![GIS Cloud - API](https://cdn.geotribu.fr/img/articles-blog-rdp/serveur/giscloud/api_map2.png "GIS Cloud - API"){: .img-center loading=lazy }

Bien évidemment, ces deux exemples sont insuffisants pour montrer l'étendue de l'API proposée. Mais l'objectif était simplement de présenter les différents modes d'intégration possibles.

## Conclusion

Notre rapide tour de GisCloud est maintenant terminé et vient donc l'heure des conclusions. Je dois avouer que j'ai été agréablement surpris par l'interface de création cartographique. Elle est intuitive et il est facile d'arriver en quelques minutes aux résultats escomptés. Les différents modes d'intégration sont également un point à souligner. Ainsi, l'utilisateur lambda comme le programmeur y trouveront leur bonheur.

Au moment où j'ai effectué mes tests, GisCloud était encore en bêta. Mais, j'ai récemment reçu un mail me signifiant que cette période était terminée tout comme l'usage illimité de ce service. En effet, pour la version gratuite, les conditions d'utilisations seront dorénavant les suivantes :

- Nombre total d'objets sur la carte limité à 1000
- Pas plus de 100mb pour les données rasters
- Un seul service WMS
- Limitations au niveau de l'API
- Limitations également pour la publication et la collaboration

Même si je trouve tout à fait normal que cette entreprise développe son business model, les conditions pour la version gratuite sont tout de même très limitées. C'est dommage car à mon avis, ils auraient gagné à s'ouvrir un peu plus. En effet, cela aurait permis d'attirer plus de personnes et donc potentiellement de nouveaux clients. Il suffit de voir la stratégie de Google à ce sujet qui commence également à monétiser ces services. Quoi qu'il en soit, c'est vraiment un bon produit. Mais cela suffira-t-il pour se démarquer de la concurrence face à des projets similaires tels que [GeoCommons](http://geocommons.com) ? Nous tenterons de répondre à cette question dans un prochain billet.

----

<!-- geotribu:authors-block -->
