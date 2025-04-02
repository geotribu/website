---
title: "OSM Data : visualisation des données 3D"
subtitle: OSM Data 5/5
authors:
    - Karl TAYOU
    - Romain LATAPIE
categories:
    - article
comments: true
date: 2025-03-31
description: "OSM DATA : visualisation des données avec Giro3D, avec suivi des performances"
icon: material/video-3d
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_5/miniature.png
license: default
robots: index, follow
tags:
    - WebGL
    - Three.js
    - Giro3D
    - OpenLayers
    - Modélisation 3D
---

# OSM DATA V2 : La visualisation en 3D d'OpenStreetMap

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

Dans les articles précédents, nous avons présenté les étapes de modélisation architecturale 3D à partir des données d'OpenStreetMap. Ce dernier article présente la méthode de visualisation des données 3D sur le web à l'aide de [Giro3D](https://giro3d.org/giro3d.html).

![logo Giro3D](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/giro3d_rectangle.svg){: .img-center loading=lazy }

Pourquoi Giro3D ? Giro3D est un *framework* permettant de visualiser tout type de données géospatiales, en 2D, 2.5D ou 3D. Le moteur cartographique 2D est basé sur [OpenLayers](https://openlayers.org/), le moteur 3D repose sur [Three.js](https://threejs.org/), le projet est *opensource* et se veut *communautaire*, même s'il est actuellement principalement maintenu par [Oslandia](https://oslandia.com/). C'est pour le caractère *opensource*, la complémentarité avec OpenLayers, le développement régulier du produit et la réactivité du support qu'on a choisi cette technologie pour OSM DATA.

Comment représenter des milliers de données 3D avec des textures sur un navigateur web avec Giro3D afin que cela soit le plus fluide possible ? Comment mesurer la performance d'une telle application et identifier les différentes étapes consommatrices de ressources ? Quelle(s) méthode(s) utiliser pour permettre une navigation fluide ?

## Suivi et optimisation des performances de visualisation

Pour évoquer les performances de la solution, la notion de *frame* est importante. Dans le secteur multimédia, le terme *frame* représente une image, l’enchaînement d'images permet de créer une vidéo et le nombre d'images présentées successivement en une seconde représente le taux de rafraîchissement exprimé soit en Hertz, soit en nombre d'images par secondes (*frames per second*). Cette notion de *frame* est importante pour la suite car elle permet d'estimer les performances de la solution mise en en place.

En visualisation 3D, on estime qu'un taux de rafraîchissement performant doit être de 60 *frames per second (fps)*. Par exemple, la Playstation 4 *Slim* permet un affichage à 30 fps alors que la Playstation 4 *pro* permet un affichage à 60 fps : expérience vécue dans FIFA, une frappe reçue de [Tammy Abraham](https://cdn.futwiz.com/assets/img/fc24/social/cards/604_pos.png?v=225516.png) dans la lucarne de Steve Mandanda est deux fois plus fluide sur la Playstation 4 *Pro* que sur la Playstation 4 *Slim*.

Plus sérieusement et dans le cas d'OSM DATA, si on considère une scène avec 1000 objets 3D, le moteur de rendu doit être capable d'interpréter et d'afficher les 1000 objets 60 fois par seconde.

Le défi de notre application est donc d'être capable de générer des scènes 3D avec un taux de rafraîchissement suffisant pour proposer une expérience utilisateur agréable, c'est-à-dire sans *bugs* (défaut de fonctionnement) et sans *lags* (retard/décalage d'images). Pour cela, étant donné que Giro3D est basé sur Three.js, lui-même basé sur [WebGL](https://get.webgl.org/), il est recommandé une fréquence d'affichage de [60 fps](http://www.opengl-tutorial.org/fr/miscellaneous/an-fps-counter/), soit 1 image toutes les 17 millisecondes.

Ce suivi est rendu possible dans Giro3D à l'aide d'un utilitaire directement intégré (`#!typescript import Inspector from '@giro3d/giro3d/gui/Inspector.js';`) et qui n'est pas encore inclus dans la documentation. :trollface:

En exécutant la commande JavaScript, on obtient un graphique représentant la durée de visualisation (en ordonnée) pour chaque image définie au cours du temps (en abscisse).

![Inspecteur de Giro3D afin de suivre le taux de rafraichissement](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_5/inspecteur_giro3d.png){: .img-center loading=lazy }

Les principales étapes de calcul d'une image dans notre scène sont les suivantes, elles sont exécutées au niveau du *Central Processing Unit (CPU)* :

1. Application des transformations géométriques des objets (position, rotation, échelle) engendré par le déplacement dans la scène 3D
2. Application des lumières et des ombres en fonction des nouvelles conditions de position et d'orientation de la *pose* considérée
3. Génération à la volée des objets 3D présents dans le cône de vue défini.

Une fois les calculs effectués, le rendu 3D de la scène est généré par la réalisation d'appels au *Graphics Processing Unit (GPU)*.

L'ensemble de ces étapes peut être chronophage et extrêmement énergivore si on considère une réalisation du processus pour chaque objet affiché. Voici un résultat obtenu avec mon ordinateur qui a perdu quelques années de vie juste pour vous lecteurs de Geotribu :

![Utilitaire de *monitoring* pour une génération séquentielle d'images](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_5/inspecteur_giro3d_non_optimise.png){: .img-center loading=lazy }

Les temps de génération sont extrêmement longs, variant de 1,5 secondes à ... 8 secondes ! :dizzy_face:

![PC Killer](https://cdn.geotribu.fr/img/articles-blog-rdp/gifs/laptop-smoking.gif){: .img-center loading=lazy }

Afin de réduire ce temps de génération, plusieurs actions peuvent être mises en place :

- Paramétrer Giro3D afin de ne pas afficher des objets qui ne sont pas visibles sur l'écran de l'utilisateur. On utilise pour cela une fonction [Frustum](https://threejs.org/docs/index.html?q=frus#api/en/math/Frustum) permettant de sélectionner un morceau de la scène à afficher. Cette action permet de réduire significativement le temps de traitement de toutes les étapes, elle est mise en place dans OSM DATA.
- Diminuer au minimum le volume des données envoyées au GPU. Cette étape peut être mise en place en limitant la répétition de coordonnées, de textures... mais elle limite les potentielles évolutions de la plateforme, cette action n'est pas mise en place dans OSM DATA.
- Générer une nouvelle scène si et seulement si aucune modification de *pose* n'est intervenue depuis 200 millisecondes, cette action est mise en place dans OSM DATA.
- Tuiler la scène sous la forme d'une grille de tuiles carrées contigues de 512 pixels * 512 pixels. Cette action permet d'accélérer considérablement l'affichage, les objets présents dans une tuile ("enfants") peuvent être fusionnés en un seul objet rattaché à la tuile "parent". Les changements de points de vue sont affectés aux entités de type "parent", moins nombreuses que les entités de type "enfant", assurant un affichage optimisé. Cette action est mise en place dans OSM DATA.
- Extruder directement les objets en 3D côté serveur (avec un cache). Cette action n'est pas mise en place dans OSM DATA (pour l'instant :trollface:)

Cette liste d'optimisations n'est pas exhaustive. En moyenne, avec un ordinateur "standard" (8Go RAM, processeur Intel core-i7), l'application dispose d'un taux de rafraîchissement supérieur à 50 fps.

Dans la prochaine partie, nous approfondissons la méthode de tuilage sous forme de grille.

## Tuilage de la scène

Au fil des interactions avec la scène, les données sont récupérées depuis le serveur cartographique en fonction du cône visible et uniquement au niveau de *zoom* 16 (zoom à partir duquel les bâtiments extrudés s'affichent - choix arbitraire). La grille est générée à ce niveau de *zoom* avec une taille de 512 pixels * 512 pixels. Afin de limiter les ressources en CPU et GPU, chaque tuile doit pouvoir :

- Être chargée une seule fois avec un seul objet fusionné (ensemble des objets présents au sein de l'emprise de la tuile) : cette contrainte permet d’éviter la répétition d'opérations d'extrusion et de fusion géométrique.
- Être affichée dès que tous les objets présents au sein de la tuile sont générés.

Pour réussir ce double objectif, la bibliothèque OpenLayers dispose d'une classe de type [VectorTile](https://openlayers.org/en/v6.15.1/apidoc/module-ol_source_VectorTile-VectorTile.html). Cette classe permet de récupérer directement les données depuis le serveur en les affectant à une grille dont la dimension est spécifiée.

```javascript title="Initialisation de notre source OpenLayers"
const buildingTileSource = new VectorTileSource({
        url: "URL_SERVEUR_CARTO_BATIMENT",
        tileGrid: createXYZ({ tileSize: 512 }) // Spécification de la dimension de notre tuile
});
```

A chaque mouvement de la carte, toutes les tuiles du zoom 16 situées dans la zone visible par l'utilisateur sont récupérées : certaines sont déjà affichées dans la scène (pas de chargement nécessaire), les autres sont chargées pour afficher une scène complète.

```javascript title="Demande de chargement des tuiles"
import VectorRenderTile from "ol/VectorRenderTile";
import { TileCoord } from "ol/tilecoord";
import TileState from "ol/TileState"

// Tableau qui stockera toutes les tuiles à charger
const loadingTiles: VectorRenderTile[] = []

// On parcourt toutes les coordonnées (x,y,zoom) des tuiles du niveau 16 dans la zone visible  par l'utilisateur
// mapExtent : zone visible par l'utilisateur
buildingTileSource.tileGrid.forEachTileCoord(mapExtent, 16, (tileCoord: TileCoord) => {
    const zoom = tileCoord[0]
    const x = tileCoord[1]
    const y = tileCoord[2]
    // On récupère notre tuile à partir de ses coordonnées
    const tile = this.vectorTileSource.getTile(zoom, x, y, "RESOLUTION DE NOTRE SCENE", "EPSG:3857")
    // Si notre tuile a un statut IDLE, ce qu'elle est n'est pas encore chargée
    if (tile.getState() == TileState.IDLE) {
        // On demande à notre source de la charger depuis le serveur cartographique
        tile.getSourceTiles()
        loadingTiles.push(tile)
    }
})
```

Lorsqu'une tuile est entièrement chargée dans la scène, il convient de l'identifier. Pour cela, la bibliothèque [RxJs](https://rxjs.dev/) facilite la gestion des changements : nous pouvons suivre efficacement l’état de chargement des données des tuiles et déclencher les actions nécessaires.

```javascript title="Surveillance du chargement des tuiles afin de les traiter"

import { BehaviorSubject, interval } from 'rxjs';
import { map } from 'rxjs/operators';

// Fonction qui récupère l'état actuel des tuiles à charger qui sont normalement tous en IDLE (0) à l'initialisation
const getTileState = (): { tile: VectorRenderTile, state: number }[] => {
    return tilesToLoad.map((tile) => ({ tile, state: tile.getState() }));
};

// Un observable pour suivre les états des tuiles
// NB : Il ne se met pas à jour tout seul
const getTileState$ = new BehaviorSubject(getTileState());

// Abonnement périodique (500 ms) pour vérifier les changements d'état des tuiles
const updateTileStateSubscription = interval(500).pipe(
    map(() => {
        const previousStates = getTileState$.value;
        const currentStates = getTileState();

        // On filtre les tuiles dont l'état a changé
        // En 500 ms plusieurs tuiles peuvent avoir changées
        const changedTiles = currentStates.filter((currentTileState, index) => {
            const previousTileState = previousStates[index];
            return currentTileState.state !== previousTileState.state;
        });

        // On oublie pas de mettre à jour l'observable avec les nouveaux états
        // afin que dans 500 ms, le filtre précédent puisse détecter s'il y a des changements ;)
        getTileState$.next(currentStates);

        // On continue uniquement avec les tuiles dont l'etat a changé
        return changedTiles;
    })
).subscribe((changedTiles:{ tile: VectorRenderTile, state: number }[]) => {
    // On a nos tuiles à traiter
    changedTiles.forEach(({ tile:VectorRenderTile, state }) => {

        // la tuile Tile, n'attend plus qu'à être traitée...
    });
});

```

Pour les tuiles chargées, nous devons pour chacune d'elles extruder les objets, les fusionner et les ajouter à la scène. Cependant :

- La grille générée par OpenLayers n'est pas directement compatible avec Giro3D. Nous devons créer et gérer une grille spécifique à Giro3D en conservant les paramètres de celle d’OpenLayers (à savoir les emprises des tuiles).
- Les coordonnées des objets issus du serveur sont en projection planimétrique [WGS84 Pseudo-Mercator (EPSG:3857)](https://epsg.io/3857). Pour optimiser les performances, les coordonnées doivent être modifiées et reliées à un système de coordonnées local propre à chaque tuile : elles ne sont plus absolues mais relatives à l'origine définie pour la tuile considérée.

Pour la gestion de la grille dans Giro3D, nous utilisons l'objet [Group](https://threejs.org/docs/index.html?q=group#api/en/objects/Group). Cet objet permet de regrouper plusieurs objets 3D, comme les bâtiments, et de gérer leurs transformations de manière centralisée. Lorsque les objets enfants ont des coordonnées relatives au groupe, toute modification appliquée au groupe est automatiquement répercutée sur ses enfants (qu'il s'agisse de rotation, de translation ou d'autres transformations). La gestion de la scène est simplifiée, les calculs informatiques sont réduits et les objets demeurent correctement positionnés et orientés même en cas de mise à jour de la scène.

Pour faciliter la lisibilité et simplifier le débogage, les coordonnées des objets 3D sont ajustées de manière à être relatives au coin inférieur gauche de chaque tuile (origine). De ce fait, toutes les coordonnées restent positives après modification.

Ensuite nous extrudons et fusionnons les objets de chaque tuile, et l'ajoutons à notre scène Giro3d :

```javascript title="Création de la tuile sous Three.JS"

import {Group} from "three";

// Notre tuile OpenLayers déja chargée
const LoadedTile:VectorRenderTile
// Tableau des features réprésentant les objets de notre tuile
const features:Feature[]

// Coordonnées inférieur gauche de notre tuile OpenLayers
const LoadedTileBottomLeft = getBottomLeft(buildingTileSource.tileGrid.getTileCoordExtent(LoadedTile.getTileCoord()))

const x = LoadedTileBottomLeft[0]
const y = LoadedTileBottomLeft[1]

// Création de notre tuile Three.JS
const treeJsTile = new Group()
// Définition des coordonnées de la tuile Three.JS
treeJsTile.position.set(x,y,0)

// Pour chaque feature (objet), on ajuste les coordonnées
features.map((feature)=>{
    const polygon = feature.getGeometry()
    const newCoordinates = polygon.getLinearRings().map((ring)=>{
        return ring.getCoordinates().map((coordinate:Coordinate)=>{
            // Ajustement des coordonnées par rapport aux coin inférieur gauche de sa tuile
            return [
                coordinate[0] - x,
                coordinate[1] - y
            ]
        })

    })
    polygon.setCoordinates(newCoordinates)
})

// On construit la géométrie unique pour tous nos objets : ceci utilise toutes les méthodes détaillées dans les deux articles précédent de cette série
const buildingsGeometry = buildBuildingsFromFeatures(features)
// Ajout de la tuile directement à notre scène Giro3D
instance.add(treeJsTile)
```

Nous avons présenté dans cet article les spécificités de visualisation avec Giro3D dans OSM DATA : les processus de gestion, de traitement et d'affichage des données 3D doivent être bien déterminés et optimisés en amont afin d'assurer une visualisation fluide des données.

## Fin de série

On espère que cette série d'articles sur les nouveautés d'OSM DATA vous a permis d'en savoir un peu plus sur les possibilités d'exploitation de la base de données d'OpenStreetMap. On espère vous avoir fait partagé notre appétence pour l'*opensource*, l'interopérabilité et l'interconnexion SIG / 3D / jumeaux numériques. Nous reviendrons écrire ici mais nous devons d'abord repartir nous entrainer à FIFA ! :soccer:

[4 : Extrusion des données en 3D - suite :fontawesome-solid-backward-step:](./2025-03-10_osm-data-3D-04-modelisation-facade.md "Extrusion des données en 3D - suite"){: .md-button }
{: align=middle }

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
