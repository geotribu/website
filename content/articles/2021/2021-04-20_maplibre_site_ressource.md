---
title: Faire de la cartographie thématique sur le Web avec MapLibreGL
authors:
    - Boris MERICSKAY
categories:
    - article
comments: true
date: 2021-04-20
description: Fork open source de MapboxGL, MapLibreGL représente l’une des solutions actuelles de cartographie en ligne les plus intéressantes. Afin de documenter et de partager une série d’expérimentations autour de la cartographie thématique sur le Web, la mise en place d’un site Web apparait comme une bonne solution pour donner à voir les possibilités de cartographie thématiques permises par MapLibreGL.
icon: simple/maplibre
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/accueil_site.png
tags:
    - MapLibre
    - MapboxGL
    - ressource
    - sémiologie
    - webmapping
---

# Faire de la cartographie thématique sur le Web avec MapLibreGL

:calendar: Date de publication initiale : 20 Avril 2021

Fork open source de MapboxGL, **MapLibreGL** représente l'une des solutions actuelles de cartographie en ligne les plus intéressantes. Bénéficiant d'une communuaté active de plus de 300 contributeurs, la bibliotèque JavaScript [MapLibreGL.js](https://github.com/maplibre/maplibre-gl-js) permet de mettre en place très rapidement des cartes en lignes basées sur les **tuiles vectorielles** et le **WebGL**.

![maplibre](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/maplibre.JPG "Maplibre"){: .img-center loading=lazy }

Cette bibliothèque de cartographie en ligne (côté client) repose sur la logique et la syntaxe de [MapboxGL.js](https://docs.mapbox.com/mapbox-gl-js/api/) (version 1.13). Au-delà de produire des cartes en ligne, elle offre de multiples possibilités pour la **cartographie thématique**, autement dit pour représenter sur une carte des données statistiques sous différentes formes.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Cartographie thématique <en ligne /\>

Côté francophone, on parle beaucoup de **sémiologie graphique** pour désigner l’ensemble des règles permettant l’utilisation d’un système graphique de signes pour la transmission via une carte d’une information correcte et accessible à un lecteur.

La cartographie est un langage qui repose sur :

- Un **alphabet** : l'implantation sous forme de point, de ligne ou de surface
- Un **vocabulaire** : les variables visuelles
- Une **syntaxe** : qui définie par les règles de la perception visuelle

Ce langage doit être :

- Visuel : obéir aux règles générales de la perception
- Universel : compréhensible par tous
- Clair et cohérent : éviter l’excès de redondance, la surcharge…

Pour aller plus loin :

- [Introduction à la cartographie thématique par Laurent Jégou](https://www.geotests.net/cours/qgis/fr/d-la-mse-en-forme/cartographie-thematique)
- [Billet du blog NEOCARTO sur la sémiologie graphique](https://neocarto.hypotheses.org/3940)
- [Cours de M1 SIGAT sur la sémiologie graphique](https://www.sites.univ-rennes2.fr/mastersigat/Cours/CM%20-%20SEMIOLOGIE%20GRAPHIQUEUNIV.pdf)

![semiologie graphique](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/semio_graphique.png "Sémiologie graphique"){: .img-center loading=lazy }

Sur le Web, il est davantage question d'une **cartographie guidée par les données (_data driven style_)**, autrement dit basée sur la nature des données (donc des variables), comme le mettent en avant des éditeurs comme [Mapbox](https://docs.mapbox.com/help/getting-started/map-design/#data-driven-styles) ou [Microsoft](https://docs.microsoft.com/fr-fr/azure/azure-maps/data-driven-style-expressions-web-sdk). Au final la logique est exactement la même que celle de la sémiologie graphique de Jacques Bertin, à savoir adapter les modes de représentation cartographique à la nature des données...

Le développement de la cartographie sur le web ne **marque pas véritablement de rupture avec les approches "classiques"**. Elle s’appuie simplement sur une **réinterprétation de règles et de principes établis** il y a plus de cinquante ans, mais réinvestis dans un contexte socio-technique différent où les pratiques, les utilisateurs comme les outils ont largement évolué.

![regles semiologie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/regles_semio.png "Règle de sémiologie"){: .img-center loading=lazy }

Pour en savoir plus, vous pouvez [vous référer à cet article](http://lecfc.fr/new/articles/229-article-6.pdf).

----

## Un site pour présenter les potentialités de cartographie thématique de MapLibreGL

Afin de **documenter** et de **partager** une série d'expérimentations autour de la cartographie thématique sur le Web, [la mise en place d'un **site Web**](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL) apparait comme une bonne solution pour donner à voir les possibilités de cartographie thématiques permises par MapLibreGL.

Ce site Web se positionne à la fois comme un **agrégateur de cartes, d'extraits de code (_snippets_) et une vitrine** des potentialités de cartographie thématique de MaplibreGL.

[![accueil site](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/accueil_site.JPG "Accueil site ressources MapLibre"){: .img-center loading=lazy }](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL)

----

## Un GitLab pour centraliser les syntaxes HMTL/CSS/Javascript

En complément au site Web, un [**projet GitLab**](https://gitlab.huma-num.fr/bmericskay/maplibre) permet de son côté de **centraliser les syntaxes HMTL/CSS/Javascript** de toutes les cartes dans un espace commun, ouvert et collaboratif.

[![projet gitlab](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/projet_gitlab.JPG "Projet GitLab"){: .img-center loading=lazy }](https://gitlab.huma-num.fr/bmericskay/maplibre)

----

## Un espace Github pour héberger les données spatiales

Afin d'éviter de dépendre d'un service commercial (payant) d'hébergement et surtout de s'affranchir de toute clé d'accès, l'ensemble des données spatiales des cartes présentées ici sont stockées sur [**un espace Github dédié**](https://github.com/mastersigat/data). Les données disponibles en _open data_ (IGN, INSEE, Ville de Paris...) sont toutes téléchargeables.

![github data](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/gihubdata.JPG "Github Data"){: .img-center loading=lazy }

Les données qui doivent être stockées en ligne sous format **GeoJSON** en **WGS84** ([EPSG:4326](https://epsg.io/4326)) sont directement appelées dans les codes des cartes.

```js
map.addSource("Nomdelasource", {
  type: "geojson",
  data: "URLduGeoJSON",
});
```

Pour en savoir plus sur le principe voir ce [tutoriel introductif sur MapLibreGL](2021-02-23_carte_ligne_libre.md) réalisé en février 2021 sur Géotribu :wink:.

----

## Cartes de bases

Une [première section](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/#basic) présente deux modèles de cartes "basiques". Il n'est pas question ici de cartographie thématique mais plutôt de revenir sur **les bases syntaxiques d'une carte basée sur MapLibreGL** (appel de la carte, fond de carte, paramètres de la vue, marqueurs, outils de contrôle, échelle...).

### Une carte de base avec un marqueur interactif

![carte base marqueur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/carte_base_marqueur.JPG "Carte de base avec un marqueur"){: .img-center loading=lazy }

[**Ouvrir la carte en plein écran**](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/Basicmap.html) // [_Voir le code sur GitLab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/Basicmap.html)

### Une carte avec un menu pour changer le style des fonds de carte

![carte menu style](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/carte_menu_style.JPG "Carte avec menu pour changer le style"){: .img-center loading=lazy }

[**Ouvrir la carte en plein écran**](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/Basemapsmenu.html) // [_Voir le code dans GitLab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/Basemapsmenu.html)

Ici **l'appel des différents fonds de carte** en tuiles vectorielles (avec les URL des .json) s'effectue en HTML, dans une DIV dédiée.

```html
<div id="menu"><b>Choose your Basemap Style</b> <hr>
  <input id="https://api.maptiler.com/maps/voyager/style.json?key=rrASqj6frF6l2rrOFR4A" type="radio" name="rtoggle" value="Voyager" checked />Voyager
  <input id="https://api.maptiler.com/maps/streets/style.json?key=rrASqj6frF6l2rrOFR4A" type="radio" name="rtoggle" value="Streets" />Streets
  <input id="https://api.maptiler.com/maps/toner/style.json?key=rrASqj6frF6l2rrOFR4A" type="radio" name="rtoggle" value="Toner" />Toner
  <input id="https://geoserveis.icgc.cat/contextmaps/hibrid.json" type="radio" name="rtoggle" value="Hibrid" />Hibrid
  <input id="https://geoserveis.icgc.cat/contextmaps/osm-bright.json" type="radio" name="rtoggle" value="OSMbright"/>OSM-Bright
  <input id="https://geoserveis.icgc.cat/contextmaps/icgc.json" type="radio" name="rtoggle" value="ICGC" />ICGC
  <input id="https://geoserveis.icgc.cat/contextmaps/positron.json" type="radio" name="rtoggle" value="Positron" />Positron
  <input id="https://geoserveis.icgc.cat/contextmaps/fulldark.json" type="radio" name="rtoggle" value="Fulldark" />Fulldark
  <input id="https://geoserveis.icgc.cat/contextmaps/night.json" type="radio" name="rtoggle" value="Night" />Night
</div>
```

Le **changement des fonds de cartes** est paramétré dans la partie script.

```js
var layerList = document.getElementById("menu");
var inputs = layerList.getElementsByTagName("input");

function switchLayer(layer) {
  var layerId = layer.target.id;
  map.setStyle(layerId);
};

for (var i = 0; i < inputs.length; i++) {
  inputs[i].onclick = switchLayer;
};
```

----

## Carte en points (Dot Map)

Une carte de points est un type de carte thématique qui utilise un signe ponctuel, souvent de taille uniforme, pour visualiser la distribution géographique d'un phénomène. Bien adapatées à la représentation de jeux de données géographiques volumineux, les cartes en points peuvent s'avérer très efficaces.

![carte en points](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/carte_points.JPG "Carte en points (Dot Map)"){: .img-center loading=lazy }

[**Ouvrir la carte en plein écran**](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/Dotmap.html) // [_Voir le code sur GitLab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/Dotmap.html)

La mise en forme des points s'appuie ici sur une syntaxe simple, on **définit la variable à catégoriser** `match,['get', 'variable']` et les **correspondances entre les modalités de la variables et les couleurs** désirées via `circle_color`.

Dans cet exemple, `circle-radius` est mobilisé pour proposer une symbologie de la **taille des points adaptative** au niveau de zoom (on définit un niveau de zoom et la taille désirée à plusieurs échelles).

```javascript
map.addLayer({
  id: "Stations",
  type: "circle",
  source: "Stations",
  paint: {
    "circle-radius": {
      base: 0.6,
      stops: [
        [12, 1.5],
        [14, 2],
        [20, 4],
      ],
    },
    "circle-color": [
      "match",
      ["get", "type"],
      "A",
      "#fbb03b",
      "B",
      "#0074D9",
      "C",
      "#2ECC40",
      /* other */ "#ccc",
    ],
  },
});
```

----

## Carte choroplèthe

Une carte choroplèthe est une carte thématique où les régions sont colorées pour montrer une mesure statistique (densité de population, revenu moyen...). Ce type de carte facilite la comparaison d'une variable statistique d'une entité spatiale à l'autre et montre la variabilité de celle-ci pour une région donnée.

![carte choroplete](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/carte_choroplete.JPG "Carte choroplète"){: .img-center loading=lazy }

[**Ouvrir la carte en plein écran**](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/ChoroplethMap.html) // [_Voir le code sur GitLab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/ChoroplethMap.html)

La syntaxe de mise en forme renvoie à trois éléments :

1. le **choix de la variable** à représenter `property : 'variable'`
2. la **discrétisation** de la variable (les bornes des classes) `stops`
3. les **couleurs** associées à chaque classes `fill-color`

```js
map.addLayer({
  id: "Municipalities",
  type: "fill",
  source: "Municipalities",
  layout: { visibility: "visible" },
  paint: {
    "fill-outline-color": "#000000",
    "fill-color": {
      property: "density",
      stops: [
        [20, "#4d9221"],
        [50, "#a1d76a"],
        [100, "#e6f5d0"],
        [200, "#fde0ef"],
        [500, "#e9a3c9"],
        [1000, "#c51b7d"],
      ],
    },
    "fill-opacity": 0.9,
  },
});
```

----

## Carte en symboles proportionnels

Une carte en symboles proportionnels représente par un cercle (ou éventuellement une autre forme géométrique simple, voire un pictogramme) une variable dont la surface est proportionnelle à la valeur représentée.

### Carte en symboles proportionnels "simples"

![carte symboles proportionnels](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/carte_symboles_proportionnels.JPG "Carte en symboles proportionnels"){: .img-center loading=lazy }

[**Ouvrir la carte en plein écran**](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/GraduatedCircles.html) // [_Voir le code sur GitLab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/GraduatedCircles.html)

La syntaxe de mise en forme `circle-radius`renvoie à deux éléments :

1. le **choix de la variable** à représenter `property : 'variable'`
2. la **taille des points en fonction de la valeur de la variable** `stops: [[0, 0], [95, 20]]`

```js
map.addLayer({
  id: "Stations",
  type: "circle",
  source: "Stations",
  paint: {
    "circle-stroke-color": "white",
    "circle-stroke-width": 1,
    "circle-radius": {
      property: "capacity",
      type: "exponential",
      stops: [
        [0, 0],
        [95, 20],
      ],
    },
    "circle-color": "#0074D9",
  },
});
```

### Carte en symboles proportionnels avec graduation de couleur

Ici on combine **deux variables visuelles, la taille et la couleur**. Dans notre cas, on procède à une redondance visuelle de l'information relative aux nombres de vélibs par station qui sont mis en forme à travers la taille des points et leur couleur.

![carte symboles proportionnels graduation](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/carte_symboles_proportionnels_graduation.JPG "Carte en symboles proportionnels avec graduation de couleur"){: .img-center loading=lazy }

[**Ouvrir la carte en plein écran**](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/GraduatedCirclesColor.html) // [_Voir le code sur GitLab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/GraduatedCirclesColor.html)

La syntaxe de mise en forme renvoie à trois éléments :

1. le **choix de la variable** à représenter
2. la **taille des points** en fonction de la valeur la variable `circle-radius`
3. la **graduation de couleurs** (discrétisation) `circle-color`

```js
map.addLayer({
  id: "Stations",
  type: "circle",
  source: "Stations",
  paint: {
    "circle-stroke-color": "#ffffff",
    "circle-stroke-width": 0.6,
    "circle-radius": {
      property: "capacity",
      type: "exponential",
      stops: [
        [0, 0],
        [100, 20],
      ],
    },
    "circle-color": {
      property: "capacity",
      stops: [
        [20, "#2c7bb6"],
        [30, "#abd9e9"],
        [40, "#ffffbf"],
        [50, "#fdae61"],
        [60, "#d7191c"],
      ],
    },
    "circle-opacity": 0.9,
  },
});
```

----

## Carte de chaleur (heatmap)

Une carte de chaleur (_heatmap_) propose une représentation continue d’un ensemble de données ponctuelles par l’estimation des densités de noyau. Les heatmaps permettent d’identifier en un coup d'œil les zones à forte densité (les points chauds), la distribution ainsi que l’organisation spatiale des concentrations d'un ensemble de données ponctuelles.

![carte chaleur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/carte_chaleur.JPG "Carte de chaleur"){: .img-center loading=lazy }

[**Ouvrir la carte en plein écran**](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/Heatmap.html) // [_Voir le code sur GitLab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/Heatmap.html)

La syntaxe de mise en forme est assez complexe. Elle s'appuie sur quatre éléments qu'il convient de paramétrer avec soin :

1. L'**intensité en fonction du niveau de zoom** `heatmap-intensity`
2. La **variation des couleurs** `heatmap-color`
3. Le **rayon d'interpolation** en fonction du niveau de zoom `heatmap-radius`
4. L'**opacité** en fonction du niveau de zoom `heatmap-opacity`

Pour aller plus loin voir la [documentation de Mapbox](https://docs.mapbox.com/mapbox-gl-js/style-spec/layers/#heatmap).

```js
map.addLayer({
  id: "horodateurs",
  type: "heatmap",
  source: "DMR",

  paint: {
    "heatmap-intensity": ["interpolate", ["linear"], ["zoom"], 1, 0, 16, 3],

    "heatmap-color": [
      "interpolate",
      ["linear"],
      ["heatmap-density"],
      0,
      "rgba(33,102,172,0)",
      0.2,
      "rgb(103,169,207)",
      0.4,
      "rgb(209,229,240)",
      0.6,
      "rgb(253,219,199)",
      0.8,
      "rgb(239,138,98)",
      1,
      "rgb(178,24,43)",
    ],

    "heatmap-radius": [
      "interpolate",
      ["linear"],
      ["zoom"],
      0,
      0,
      12,
      3,
      15,
      15,
    ],

    "heatmap-opacity": ["interpolate", ["linear"], ["zoom"], 12, 1, 15, 0.7],
  },
});
```

----

## Carte en cluster

Les carte basées sur le regroupement spatial de marqueurs sous forme de clusters, tiennent une place importante dans la cartographie sur le Web. Cette approche, appuyée sur l’analyse des distances et des densités d’un ensemble de points, permet de rendre plus lisible une carte saturée de points par leur regroupement en grappes homogènes et l’affichage de leur nombre.

## Carte en clusters classiques

![carte clusters classiques](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/carte_clusters.JPG "Carte en clusters classiques"){: .img-center loading=lazy }

[**Ouvrir la carte en plein écran**](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/Cluster.html) // [_Voir le code sur GitLab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/Cluster.html)

La syntaxe de paramètrage et de mise en forme est **assez complexe**. Elle s'appuie sur quatre éléments qu'il convient de paramétrer avec soin :

1. Le **niveau de zoom maximal** du clustering `clusterMaxZoom`
2. Le **rayon de regroupement** `clusterRadius`
3. La **graduation de couleur** des clusters `circle-color`
4. La **taille des clusters** `circle-color`

> La configuration des étiquettes du dénombrement des points dans chaque cluster n'est pas réellement à paramétrer, hormis la taille ou la police.

```js
map.addSource("DMR", {
  type: "geojson",
  data: "https://raw.githubusercontent.com/mastersigat/data/main/DMR.geojson",
  cluster: true,
  clusterMaxZoom: 14,
  clusterRadius: 50,
});

map.addLayer({
  id: "clusters",
  type: "circle",
  source: "DMR",
  filter: ["has", "point_count"],
  paint: {
    "circle-color": [
      "step",
      ["get", "point_count"],
      "#51bbd6",
      400,
      "#f1f075",
      600,
      "#F012BE",
      1000,
      "#FF4136",
    ],
    "circle-radius": [
      "step",
      ["get", "point_count"],
      5,
      200,
      10,
      400,
      15,
      600,
      20,
      1000,
      40,
    ],
  },
});

map.addLayer({
  id: "cluster-count-label",
  type: "symbol",
  source: "DMR",
  filter: ["has", "point_count"],
  layout: {
    "text-field": "{point_count_abbreviated}",
    "text-font": ["DIN Offc Pro Medium", "Arial Unicode MS Bold"],
    "text-size": 12,
  },
});
```

## Carte en clusters thématiques

![carte clusters thematiques](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/carte_clusters_thematiques.JPG "Carte en clusters thématiques"){: .img-center loading=lazy }

[**Ouvrir la carte en plein écran**](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/Clusterthematic.html) // [_Voir le code sur GitLab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/Clusterthematic.html)

La syntaxe de paramètrage et de mise en forme de cluster thématiques est **complexe**.

> Pour vraiment prendre en main ce mode de représentation de données géographiques, voir ce [tutoriel de Mapbox](https://blog.mapbox.com/clustering-properties-with-mapbox-and-html-markers-bb353c8662ba) et cet [exemple de Mapbox](https://docs.mapbox.com/mapbox-gl-js/example/cluster-html/)

En gros, la syntaxe s'appuie sur plusieurs élements comme :

- Définir en amont chacune des modalités qui seront prises en compte dans le clustering et leur associer une couleur

> Dans mon exemple la variable (nom du champ) se nomme **_type_** et renvoie à trois modalités dans le geojson (_A_, _B_ et _C_) > [voir le GeoJSON](https://raw.githubusercontent.com/mastersigat/data/main/DMR.geojson)

```js
var mag1 = ["match", ["get", "type"], ["A"], false, true];

var mag2 = ["match", ["get", "type"], ["B"], false, true];

var mag3 = ["match", ["get", "type"], ["C"], false, true];

var colors = ["#fbb03b", "#0074D9", "#2ECC40"];
```

- Spécifier les modalités dans `clusterProperties`

```js
map.addSource("earthquakes", {
  type: "geojson",
  data: "https://raw.githubusercontent.com/mastersigat/data/main/DMR.geojson",
  cluster: true,
  clusterMaxZoom: 16,
  clusterRadius: 50,
  clusterProperties: {
    // keep separate counts for each magnitude category in a cluster
    mag1: ["+", ["case", mag1, 1, 0]],
    mag2: ["+", ["case", mag2, 1, 0]],
    mag3: ["+", ["case", mag3, 1, 0]],
  },
});
```

- Spécifier les modalités au niveau de la création du `DonutChart`

```js
function createDonutChart(props) {
  var offsets = [];
  var counts = [props.mag1, props.mag2, props.mag3];
};
```

- Enfin, configurer à la fois la **taille des étiquettes** des clusters `var fontSize` et la **taille des clusters** `var r`

```js
var fontSize = total >= 1000 ? 15 : total >= 100 ? 12 : total >= 6 ? 10 : 5;
var r =
  total >= 20000
    ? 50
    : total >= 10000
    ? 40
    : total >= 5000
    ? 30
    : total >= 100
    ? 20
    : 15;
```

## Cartes en 3D

Avec le WebGL, il est désormais assez simple d'intégrer de la 3D dans les cartes en ligne. Cette perspective est particulièrement intéressante en cartographie thématique pour représenter autrement certaines variables et surtout combiner plusieurs variables visuelles (comme la taille et la couleur) au sein d'une même carte.

### Carte en 3D basée sur un carroyage de population

Dans cette première carte, on travaille avec deux variables visuelles, une **variable de couleur** et une **variable de taille** qui renvoient à la même donnée, la population de chaque carreau.

![carte 3d carroyage](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/carte_3d_carroyage.JPG "Carte 3D sur un carroyage de population"){: .img-center loading=lazy }

[**Ouvrir la carte en plein écran**](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/3Dmap.html) // [_Voir le code sur GitLab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/3Dmap.html)

La syntaxe de paramètrage et de mise en forme repose sur deux principaux élements relatifs au `fill-extrusion`:

1. La **couleur** des entités extrudées en 3D `fill-extrusion-color`
2. La **hauteur** des entités extrudées en 3D `fill-extrusion-height`

```js
map.addLayer({
  id: "extrude",
  type: "fill-extrusion",
  source: "Carro",
  layout: {
    visibility: "visible",
  },
  paint: {
    "fill-extrusion-color": {
      property: "ind_c",
      stops: [
        [1, "#1a9850"],
        [20, "#91cf60"],
        [50, "#d9ef8b"],
        [100, "#ffffbf"],
        [200, "#fee08b"],
        [300, "#fc8d59"],
        [500, "#d73027"],
      ],
    },
    "fill-extrusion-height": {
      property: "ind_c",
      stops: [
        [1, 0],
        [10, 100],
        [1000, 5000],
      ],
    },
    "fill-extrusion-opacity": 0.95,
    "fill-extrusion-base": 0,
  },
});
```

### Carte en 3D basée sur deux variables statistiques

Dans cette autre carte, on travaille aussi avec deux variables visuelles, une **variable de couleur** et une **variable de taille**, mais qui renvoient ici à deux variables statistiques, la **population** (qui sert à l'extrusion) et la **densité de population** (qui sert à l'applat de couleurs) de chacune des communes bretonnes.

![carte 3d bivariee](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/carte_3d_bivariee.JPG "Carte 3D bivariée"){: .img-center loading=lazy }

[**Ouvrir la carte en plein écran**](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/Choropleth3DMap.html) // [_Voir le code sur GitLab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/Choropleth3DMap.html)

La syntaxe de paramètrage et de mise en forme repose sur deux principaux élements relatif au `fill-extrusion`:

1. La **couleur** des entités extrudées en 3D `fill-extrusion-color`
2. La **hauteur** des entités extrudées en 3D `fill-extrusion-height`

```js
map.addLayer({
  id: "Municipalities",
  type: "fill-extrusion",
  source: "Municipalities",
  layout: { visibility: "visible" },
  paint: {
    "fill-extrusion-color": {
      property: "density",
      stops: [
        [20, "#4d9221"],
        [50, "#a1d76a"],
        [100, "#e6f5d0"],
        [200, "#fde0ef"],
        [500, "#e9a3c9"],
        [1000, "#c51b7d"],
      ],
    },
    "fill-extrusion-height": {
      property: "POPULATION",
      stops: [
        [100, 10],
        [100, 100],
        [200000, 70000],
      ],
    },
    "fill-extrusion-opacity": 0.95,
    "fill-extrusion-base": 0,
  },
});
```

### Carte en 3D basée les hauteurs de bâtiments

Avec le WebGL, il est simple d’extruder la hauteur des bâtiments pour représenter de manière plus réaliste les volumétries des villes. Dans cette dernière carte, il s'agit d'appliquer la même logique que précédamment, en extrudant en 3D les bâtiments (BDTOPO de l'IGN) selon leur hauteur et en appliquant une graduation de couleur selon la hauteur.

![carte 3d hauteurs](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/carte_3d_hauteurs.JPG "Carte 3D hauteurs de bâtiments"){: .img-center loading=lazy }

[**Ouvrir la carte en plein écran**](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/Buildingmaps.html) // [_Voir le code sur GitLab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/Buildingmaps.html)

La syntaxe de paramètrage et de mise en forme repose sur deux principaux élements relatifs au `fill-extrusion`:

1. La **couleur** des entités extrudées en 3D `fill-extrusion-color`
2. La **hauteur** des entités extrudées en 3D `fill-extrusion-height` mais dans ce cas, pas besoin de préciser des bornes, car il est attendu une extrusion calquée sur la hauteur des bâtiments

```js
map.addLayer({
  id: "Batiments",
  type: "fill-extrusion",
  source: "Batiments",
  paint: {
    "fill-extrusion-height": { type: "identity", property: "HAUTEUR" },
    "fill-extrusion-color": {
      property: "HAUTEUR",
      stops: [
        [5, "#1a9850"],
        [7, "#91cf60"],
        [9, "#d9ef8b"],
        [12, "#ffffbf"],
        [16, "#fee08b"],
        [20, "#fc8d59"],
        [30, "#d73027"],
      ],
    },
    "fill-extrusion-opacity": 0.7,
    "fill-extrusion-base": 0,
  },
});
```

----

## En bonus

Petit bonus pour terminer ce tour d'horizon des potentialités de MapLibreGL en termes de cartographie thématique, trois autres syntaxes fonctionnelles de cartes en ligne qui peuvent servir dans certains contexte !

- la **[carte glissante](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/Swipemap.html)** (_swipe map_) pour visualiser deux fonds de carte ! [_Code Gitlab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/Swipemap.html)
- la **[carte animée](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/Animation.html)** qui bouge toute seule ! [_Code Gitlab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/Animation.html)
- la carte où tu peux même intégrer des **[services WMS](https://sites-formations.univ-rennes2.fr/mastersigat/MaplibreGL/maps/WMSmap.html)** dans du MapLibreGL ! [_Code Gitlab_](https://gitlab.huma-num.fr/bmericskay/maplibre/-/blob/master/WMSmap.html)

Bref, MapLibre c'est une super solution, assez simple de prise en main, donc plus aucune raison de ne pas opérer sa conversion à la cartographie en ligne en mode libre et avec qualité !

![meme maplibre](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/maplibre_site_ressource/meme_maplibre.jpg "Meme MapLibre"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-sa.md" %}
