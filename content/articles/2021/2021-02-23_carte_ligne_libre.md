---
title: Faire une carte en ligne (tuiles vectorielles + WebGL) 100% libre
authors:
    - Boris MERICSKAY
categories:
    - article
    - tutoriel
comments: true
date: 2021-02-23
description: 'En réaction au changement de licence de MapBox, de nombreuses initiatives ont émergé, dont une très intéressante : MapLibre. Voici un tutoriel complet pour l''utiliser pour créer une carte web interactive 100% libre, en continuant à utiliser les fonctionnalités de MapboxGL sans dépendance aux jetons d''accès.'
icon: simple/maplibre
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/finalisation.JPG
tags:
    - MapBox
    - MapLibre
    - tuiles vectorielles
    - WebGL
    - webmapping
---

# Faire une carte en ligne (tuiles vectorielles + WebGL) 100% libre

:calendar: Date de publication initiale : 23 février 2021

## Introduction

Le recent passage de la bibliothèque Javascript MapboxGL à une [nouvelle licence d'utilisation moins ouverte](https://github.com/mapbox/mapbox-gl-js/issues/10162), et disons le fermée, pousse à repenser la dépendance des cartographes du Web à cet ecosystème innovant, fonctionnel et très efficace.

En réaction à ce changement, de nombreuses initiatives ont émergé, dont une très intéressante, [MapLibre](https://github.com/maplibre), un fork open source de la version 1.x de MapboxGL.JS. Déjà très actif avec plus de 300 contributeurs, ce fork constitue une bonne alternative pour continuer à utiliser les fonctionnalités de MapboxGL sans dépendance aux jetons d'accès (_access token_) de MapBox et en s'affranchissant donc des limites de l'éditeur et surtout de la monétisation.

![maplibre gl](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/maplibre_pres.JPG "Maplibre GL"){: .img-center loading=lazy }

Ce projet est très intéressant car MapLibre conserve la syntaxe de [MapboxGL.JS](https://docs.mapbox.com/mapbox-gl-js/api/), et permet de mobiliser des services de **tuiles vectorielles** et des affichages 3D en **WebGL**. Du coup pas besoin de réapprendre une nouvelle syntaxte et se replonger dans une énième documentation !

Nous proposons dans ce billet de **construire étape par étape une [carte Web 100% libre](https://bl.ocks.org/mastersigat/30898810b41783ffde93330b7edb3124) en mobilisant une série de services ouverts** pour construire rapidement une petite carte Web basée sur les tuiles vectorielles et le WebGL.

![carte presentation](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/carte_presentation.JPG "Carte de presentation"){: .img-center loading=lazy }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## 1. Mobiliser simplement l'API de MapLibre

L'entreprise [Maptiler](https://support.maptiler.com/i849-how-to-use-maplibre) propose depuis peu une URL pour accéder rapidement et sans restriction à l'API de MapLibre.

```html
<script src="https://cdn.maptiler.com/maplibre-gl-js/v1.13.0-rc.4/mapbox-gl.js"></script>
<link
  href="https://cdn.maptiler.com/maplibre-gl-js/v1.13.0-rc.4/mapbox-gl.css"
  rel="stylesheet"
/>
```

Si vous avez déjà développé avec MapboxGL.JS, il suffit de remplacer les anciennes URL fournies par Mapbox par celles-ci, tout simplement ! A partir de là, finis les AccessToken et bonjour la liberté :smile:

Sinon, voici la **structure globale pour une carte basique**

![carte ba](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/carte_basique.JPG "Carte basique"){: .img-center loading=lazy }

```html
<html>
  <head>
    <meta
      name="viewport"
      content="initial-scale=1,maximum-scale=1,user-scalable=no"
    />
    <script src="https://cdn.maptiler.com/maplibre-gl-js/v1.13.0-rc.4/mapbox-gl.js"></script>
    <link
      href="https://cdn.maptiler.com/maplibre-gl-js/v1.13.0-rc.4/mapbox-gl.css"
      rel="stylesheet"
    />

    <style>
      #map {
        position: absolute;
        top: 0;
        right: 0;
        bottom: 0;
        left: 0;
      }
    </style>
  </head>

  <body>
    <div id="map"></div>

    <script>
      //Appel et configuration de la carte

      var map = new mapboxgl.Map({
        container: "map",
        style:
          "https://openmaptiles.geo.data.gouv.fr/styles/osm-bright/style.json", //Fond de carte
        zoom: 15.3, // Zoom
        center: [-1.68, 48.106], // Centrage
        pitch: 60, // Inclinaison
        bearing: -50, // Rotation
        minZoom: 14.5, // Zoom min
      });
    </script>
  </body>
</html>
```

----

## 2. Mobiliser des fonds de cartes vectoriels libres

Précurseurs dans la conception et l'hébergement de fond de carte en tuiles vectorielles, des entreprises comme [Mapbox](https://www.mapbox.com/), [Maptiler](https://www.maptiler.com/) ou [Jawg](https://www.jawg.io/fr/) proposent une pléthore de styles de fond de carte et des fonctionnalités de personnalisation. Pour bénéficier de ces services il faut toutefois payer le "prix" _via_ des abonnements ou en respectant les quotas imposés par ces fournisseurs.

Dans la même logique que précédemment, l'idée est ici de pouvoir mobiliser des fonds de carte en tuiles vectorielles mais sans restrictions (sans clé d'accès) afin de ne dépendre de personne !

**Il existe de plus en plus de flux de tuiles vectorielles accessibles gratuitement sans aucune restriction.**

Cette petite [interface cartographique](https://bl.ocks.org/mastersigat/dd2e0c913391f75f9c2a0796f66cb042) permet de visualiser à la volée différents styles librement accessibles.

Pour changer le **style** du fond de carte, il suffit tout simplement de renseigner **l'URL du .json**

```javascript
style: "URLdufonddecarte";
```

----

### Etalab

[Etalab](https://www.etalab.gouv.fr/) propose plusieurs [flux de tuiles vectorielles](https://openmaptiles.geo.data.gouv.fr/) basées sur les données OSM pour les fonds de carte comme des flux de données spatiales dédiés (cadastre, limites administrative,...).

#### Fond de carte (Style)

```javascript
https://openmaptiles.geo.data.gouv.fr/styles/osm-bright/style.json
```

![style etalab](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/etalab.JPG "Style Etalab"){: .img-center loading=lazy }

#### Flux de données thématiques (données OSM, contours administratifs et cadastre)

```javascript
https://openmaptiles.geo.data.gouv.fr/data/france-vector.json
https://openmaptiles.geo.data.gouv.fr/data/decoupage-administratif.json
https://openmaptiles.geo.data.gouv.fr/data/cadastre.json
```

----

### IGN

L'IGN met à disposition sans restriction un [flux de tuiles vectorielles de fond carte](https://geoservices.ign.fr/documentation/services_betas/vecteur-tuile.html) basé sur ses propres données ce qui peux contituer une alternative intéressante aux données OSM dans certains cas.

<!-- markdownlint-disable MD024 -->
#### Fond de carte (Style)

```javascript
https://vectortiles.ign.fr/demonstrateur/styles/planign.json
```

![style ign](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/ign.JPG "Style IGN"){: .img-center loading=lazy }

----

### Institut Cartogràfic i Geològic de Catalunya

L'[institut cartographique et géologique de la Catalogne](https://www.icgc.cat/en/) propose de son côté [plusieurs styles de fond de carte](https://openicgc.github.io/) en tuiles vectorielles (basés sur les données OSM), **disponibles sans restriction à l'échelle du monde**.

#### Style ICGC

```javascript
https://geoserveis.icgc.cat/contextmaps/icgc.json
```

![style icgc](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/icgc.JPG "Stye ICGC"){: .img-center loading=lazy }

#### Style FullDark

```javascript
https://geoserveis.icgc.cat/contextmaps/fulldark.json
```

![style fulldark](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/full_dark.JPG "Style FullDark"){: .img-center loading=lazy }

#### Style Night

```javascript
https://geoserveis.icgc.cat/contextmaps/night.json
```

![style night](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/night.JPG "Style Night"){: .img-center loading=lazy }

#### Style Positron (CARTO)

```javascript
https://geoserveis.icgc.cat/contextmaps/positron.json
```

![style positron](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/positron.JPG "Style Positron"){: .img-center loading=lazy }

----

## 3. Héberger ses données spatiales sans passer par Mapbox Studio

Une fois sa carte configurée avec MapLibre et un fond de carte, il est temps d'afficher ses propres données. Plusieurs options d'hébergement de GeoJSON sont possibles, comme un hébergement sur un serveur FTP, toutefois le mécanisme [Cross-origin resource sharing (CORS)](https://fr.wikipedia.org/wiki/Cross-origin_resource_sharing) qui permet d'intégrer à sa carte Web des ressources externes peux s'avérer très capricieux, surtout si on n'est pas connaisseur...

L'une des alternatives les plus simples consiste à héberger ses GeoJSON sur GitHub.

![hebergement github](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/github.JPG "Hébergement Github"){: .img-center loading=lazy }

Une fois les GeoJSON hébergés il suffit de récupérer l'URL.

![github raw](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/github_raw.JPG "Github raw"){: .img-center loading=lazy }

----

Pour afficher un GeoJSON (hébergé sur GitHub) dans sa carte Web il suffit de **paramétrer la commande `map.addSource`**, concernant le `map.addLayer` (pour la mise en forme), la syntaxe de MapboxGL reste identique.

```javascript
map.addSource("Nomdelasource", {
  type: "geojson",
  data: "URLduGeojson",
});
```

### Appel du GeoJSON des stations de métro

```javascript
// Ajout stations de metros

map.addSource("StationsGIT", {
  type: "geojson",
  data:
    "https://raw.githubusercontent.com/mastersigat/data/main/metro-du-reseau-star-localisation-des-stations.geojson",
});

map.addLayer({
  id: "Stations",
  type: "circle",
  source: "StationsGIT",
  paint: {
    "circle-stroke-color": "white",
    "circle-stroke-width": 3,
    "circle-radius": 6,
    "circle-color": "#0074D9",
  },
});
```

### Appel du GeoJSON des lignes de métro

```javascript
// Ajout lignes de metros

map.addSource("lignesGIT", {
  type: "geojson",
  data:
    "https://raw.githubusercontent.com/mastersigat/data/main/metro-du-reseau-star-traces-de-laxe-des-lignes.geojson",
});

map.addLayer({
  id: "Lignes",
  type: "line",
  source: "lignesGIT",
  paint: { "line-opacity": 0.7, "line-width": 7, "line-color": "#0074D9" },
});
```

![ajout geojson](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/map_addsource.JPG "Ajout des GeoJSON"){: .img-center loading=lazy }

----

## 4. Activer la 3D !

Pour appuyer cette petite démonstration, il est important d'illustrer que le fait de passer à des environnements 100% libres ne vient pas forcément altérer les capacités de rendus graphiques des cartes en ligne.

Nous allons ici extruder en 3D les bâtiments de la BDTOPO de l'IGN en se basant sur le champ `HAUTEUR` présent dans la couche (`fill-extrusion-height`). Pour accentuer le rendu visuel, nous allons également appliquer une graduation de couleur en se basant sur la même colonne (`fill-extrusion-color`).

```javascript
//BATIMENTS EN 3D

map.addSource("Batiments", {
  type: "geojson",
  data:
    "https://raw.githubusercontent.com/mastersigat/data/main/BatiRennes.geojson",
});

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

![ajout 3D](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/3d.JPG "Ajout de la 3D"){: .img-center loading=lazy }

----

## 5 Ajouter de l'interactivité à la carte

Nous allons ici ajouter deux fonctionnalités d'interaction avec les données :

- une popup
- un menu de gestion des couches

### Configurer la Popup (hover)

Nous voulons ajouter une Popup (fenêtre d'informations) pour afficher le nom des stations de métro qui apparaitra au survol (_hover_) des stations de métro. Il est aussi possible de configurer la popup avec une interaction au clic (sur l'objet spatial).

On ajoute en premier lieu quelques **paramètres de style dans le CSS** pour que la popup soit jolie.

```CSS
.Mypopup .mapboxgl-popup-content {
      background-color: black;
      color : white;
      opacity : 0.7;
}
```

On ajoute ensuite dans le **script la fonction de popup en mode hover**. En gros, ici, seul l'appel de la couche et le (ou les) champ(s) à afficher dans la popup sont à modifier pour une autre utilisation.

```javascript
//Interactivité HOVER

var popup = new mapboxgl.Popup({
  className: "Mypopup",
  closeButton: false,
  closeOnClick: false,
});

map.on("mousemove", function (e) {
  var features = map.queryRenderedFeatures(e.point, { layers: ["Stations"] });
  // Change the cursor style as a UI indicator.
  map.getCanvas().style.cursor = features.length ? "pointer" : "";

  if (!features.length) {
    popup.remove();
    return;
  }

  var feature = features[0];
  popup
    .setLngLat(feature.geometry.coordinates)
    .setHTML("<b>" + feature.properties.nom + "</b>")
    .addTo(map);
});
```

![popup](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/popup.JPG "Ajout du popup"){: .img-center loading=lazy }

----

### Ajout d'un menu de gestion des couches

Etape la plus "compliquée", pour rendre sa carte encore plus interactive, quoi de mieux qu'un menu pour controler l'affichage des couches.

On commence par **configurer le style du menu dans le CSS**.

```css
.menu {
  position: absolute;
  top: 10px;
  left: 30px;
  width: 180px;
  background-color: #ffffff;
  opacity: 0.89;
  color: #000000;
  font: 13px/20px "Helvetica Neue", Arial, Helvetica, sans-serif;
  padding: 10;
}
```

On **paramètre ensuite le menu au niveau des div**. Cette approche est bien plus simple car on **configure sa structure directement en HTML**. Les plus aguerris en développement Web préférerons le CSS :wink:

```html
<div class="menu">
  <hr />
  <label class="categoryLabel"><b>Données Réferentielles</b></label>
  <br />
  <input
    type="checkbox"
    id="Batiments"
    value="Batiments"
    onchange="switchlayer('Batiments')"
    checked
  />
  <label for="Batiments">Batiments</label>
  <hr />
  <label class="categoryLabel"><b>Données TC</b></label>
  <br />
  <input
    type="checkbox"
    id="Stations"
    value="Stations"
    onchange="switchlayer('Stations')"
    checked
  />
  <label for="Stations">Stations de métro</label>
  <br />
  <input
    type="checkbox"
    id="Lignes"
    value="Lignes"
    onchange="switchlayer('Lignes')"
    checked
  />
  <label for="Lignes">Lignes de métro</label>
  <hr />
</div>
```

Enfin, il suffit d'ajouter dans le script (à la suite) la commande qui va gérer l'affichage à la demande des couches.

```javascript
// Configuration affichage menu couches

switchlayer = function (lname) {
  if (document.getElementById(lname).checked) {
    map.setLayoutProperty(lname, "visibility", "visible");
  } else {
    map.setLayoutProperty(lname, "visibility", "none");
  }
};
```

Voilà vous avez un menu simple mais fonctionnel :smile: !

![menu](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/menu.JPG "Menu"){: .img-center loading=lazy }

## 6. Finaliser l'habillage de la carte

Dernière étape, habiller la carte avec un **controleur de navigation** et une **échelle**. Il suffit d'ajouter ces commandes à la fin du script.

```javascript
// Ajout controle de navigation et echelle

map.addControl(new mapboxgl.NavigationControl({ position: "top-left" }));

map.addControl(new mapboxgl.ScaleControl({ position: "bottom-right" }));
```

Votre carte en ligne en tuiles vectorielles et WebGL 100% libre est terminée !

![carte finale](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte-ligne-libre/finalisation.JPG "Carte finale"){: .img-center loading=lazy }

Le code complet [se trouve ici](https://bl.ocks.org/mastersigat/30898810b41783ffde93330b7edb3124).

----

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-sa.md" %}
