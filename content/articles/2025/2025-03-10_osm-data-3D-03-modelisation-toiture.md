---
title: "OSM Data : Extrusion des données en 3D"
subtitle: OSM Data 3/5
authors:
    - Karl TAYOU
    - Romain LATAPIE
categories:
    - article
comments: true
date: 2025-03-18
description: "OSM DATA 3D : des données 2D à leur représentation en 3D"
icon: material/home-roof
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/miniature.png
license: default
robots: index, follow
tags:
    - CGAL
    - MapBox
    - Modélisation 3D
    - OpenLayers
    - OpenStreetMap
    - Straight skeleton
    - Three.js
    - WebGL
---

# OSM DATA V2 : de la visualisation cartographique à la scène 3D

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

Dans [l'article précédent](./2025-03-10_osm-data-3D-02-donnees-diffusion.md), le processus de gestion des données SIG a été présenté afin de définir des flux cartographiques WMS et WFS. Ces flux permettent d'exposer des données en 2D, mais comment est générée la visualisation 3D avec [OSM DATA](https://demo.openstreetmap.fr/map?profil=1&layers=8,15,layer;3,15,layer;253,11,layer;396,11,layer;36,11,layer;519,16,layer&pos=259312,6253359,260.6,258894.7,6253800.6,0) ?

De manière simple, les géométries `Point`, `Polyline`, `Polygon` peuvent être représentées en 3D en renseignant l'altitude dans la géométrie (`PointZ`, `PolylineZ`, `PolygonZ`) ou alors à l'aide d'une valeur attributaire définie pour chaque entité.

Avec les entités polygonales, il est aussi possible de générer des **volumes** en 3D à l'aide de traitements géométriques. Par exemple et pour tout le reste de cet article, nous allons nous intéresser à la modélisation architecturale.

## Processus de modélisation architecturale 3D dans OSM DATA

Pour ce processus, nous utilisons la table `planet_osm_polygon` dans laquelle nous retrouvons les informations suivantes :

- L'emprise géométrique du bâtiment ou/et de la toiture représentée par le polygone considéré.
- La [hauteur de la toiture *roof:height*](https://wiki.openstreetmap.org/wiki/Key:roof:height?uselang=fr) définie entre le sommet le plus haut de la toiture et son sommet le plus bas.
- La [hauteur du bâtiment par rapport au sol *min_height*](https://wiki.openstreetmap.org/wiki/Key:min_height) définie entre le point le plus bas du bâtiment et le point projeté au sol.
- La [hauteur du point le plus haut du bâtiment par rapport au sol *height*](https://wiki.openstreetmap.org/wiki/Key:height) définie entre le point le plus haut du bâtiment et le point projeté au sol.
- Le [type de toiture](https://wiki.openstreetmap.org/wiki/Key:roof:shape) définissant la forme du toit.
- La [texture](https://wiki.openstreetmap.org/wiki/Key:roof:material) caractérisant les matériaux du toit et/ou de la façade.

![Hauteur du toit et hauteur par rapport au sol](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/calcul_toit_cottage_on_a_chicken_foot_3D_height_definition.webp){: .img-center loading=lazy }

Avec l'ensemble de ces informations, il est donc possible de reconstruire le bâti en 3D d'un territoire en appliquant à l'ensemble des polygones le processus suivant :

1. Création de la toiture
2. Reconstruction des façades
3. Application des matériaux

Cet article aborde la création de la toiture, le prochain article présente la génération des façades.
En modélisation 3D, la notion de *Level Of Detail* (LOD) est importante et caractérise le niveau de représentation géométrique d'un objet, il s'appuie sur l'une des normes suivantes :

- [BIMForum](https://bimforum.org/bimforum-level-of-development-lod-specification-2024-in-english-and-spanish-language-version/), essentiellement utilisée dans le cadre de projets *Building Information Modeling* (BIM)
- [CityGML](https://www.ogc.org/publications/standard/citygml/), largement répandue dans la création de socles 3D territoriaux

OpenStreetMap étant une base de données d'emprise mondiale, il nous semble plus pertinent d'utiliser la norme CityGML pour définir le niveau de détail. Dans OSM DATA, le niveau de détail est équivalent à celui d'un **LOD2**.

![Les différents niveaux de détail (LOD)](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/differents_niveaux_de_lod.png){: .img-center loading=lazy }

## Exemple de modélisation

Pour faciliter la compréhension, utilisons un exemple pour présenter l'ensemble du processus de modélisation 3D.

Considérons le [bâtiment suivant](https://www.openstreetmap.org/way/822290992) dans OpenStreetMap (oui oui ce bâtiment est présent dans l'Opéra Garnier) :

![Exemple de bâtiment considéré](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/objectif_batiment_sur_osm.png){: .img-center loading=lazy }

Le `GeoJSON` de ce bâtiment est :

??? "GeoJSON du bâtiment exemple"
    ```json title="GeoJSON du bâtiment exemple"
    {
        "type": "Feature",
        "geometry": {
            "type": "Polygon",
            "coordinates": [
                [
                    [
                        259521.14076069795,
                        6253167.799861707
                    ],
                    [
                        259606.34863939675,
                        6253192.28359733
                    ],
                    [
                        259590.5611086523,
                        6253248.230426137
                    ],
                    [
                        259505.31590718575,
                        6253223.7466905145
                    ],
                    [
                        259521.14076069795,
                        6253167.799861707
                    ]
                ]
            ]
        },
        "properties": {
            "roofType": "gabled",
            "roofHeight": 10,
            "roofOrientation": "along",
            "type": "building",
            "minHeight": 31,
            "roofMaterial": "metal",
            "osmId": 822290992,
            "buildingType": "yes",
            "height": 58
        }
    }
    ```

L'objectif est d'arriver au résultat suivant :

![Objectif batiment 3D](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/objectif_batiment_3D.png){: .img-center loading=lazy }

Pour le reste de l'article, à des fins de simplification, les visualisations 3D sont affichées sous Three.js. Dans le dernier article, nous présentons la visualisation avec Giro3D dans OSM DATA.

## Création de la toiture

En interprétant le fichier `GeoJSON` ci-dessus, nous avons les informations suivantes concernant le bâtiment considéré :

- Hauteur de la toiture : 10 m.
- Hauteur du bâtiment par rapport au sol : 31 m.
- Hauteur du point le plus bas de la toiture : 48 m (*height* 58 m - *roof:height* 10 m).
- Hauteur du point le plus haut du bâtiment par rapport au sol : 58 m
- Type de toiture : *Gabled* (toiture à pignon).
- Texture : Métal.

Pour réaliser la toiture, trois étapes sont nécessaires :

1. Détermination du squelette droit (*straight skeleton*).
2. Post-traitement du squelette afin de l'ajuster au type de toiture.
3. Ajout de la hauteur à chaque sommet du squelette.

Pour réaliser cette transformation, nous nous appuyons sur la bibliothèque [CGAL](https://www.cgal.org/).

## Détermination du squelette droit (*straight skeleton*)

La construction d'un squelette droit permet de définir, à partir de l'emprise d'un polygone, la version la plus fine d'un polygone jusqu'à l'obtention d'un ou plusieurs axes médians. Si vous n'avez rien compris, c'est normal, on essaye d'une autre manière : imaginez qu'un polygone (rectangle pour faire facile) se rétracte progressivement comme si ses bords brûlaient uniformément vers l'intérieur. Les lignes tracées par les sommets qui se déplacent pendant cette "rétraction" forment le squelette droit. Si vous n'avez toujours rien compris, c'est encore normal, rendez-vous sur [Wikipedia](https://en.wikipedia.org/wiki/Straight_skeleton) pour les bilingues.  

![Exemple de squelette droit](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/exemple_squelette_droit_wikimedia.webp){: .img-center loading=lazy }

La majorité des toitures dans OSM DATA sont construites à l'aide du squelette droit. En assignant une hauteur à chaque segment du squelette et/ou à chaque sommet du polygone initial, il est donc possible de générer des toitures complexes et cohérentes avec la géométrie initiale.

Sur la page ci-dessous, nous illustrons le polygone de notre bâtiment exemple (en haut) associé à son squelette droit (en bas).

<iframe height="450" style="width: 100%;" scrolling="no" title="Article GeoTribu" src="https://codepen.io/TANK2003/embed/azoVbJp?default-tab=" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  Allez sur le codepen <a href="https://codepen.io/TANK2003/pen/azoVbJp">
  Construction du squelette droit de la toiture</a> by Karl TAYOU (<a href="https://codepen.io/TANK2003">@TANK2003</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Si on ajoute une hauteur à l'axe médian uniquement on obtient donc le résultat suivant :

![Squelette droit en 3D](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/skeleton_droit_avec_altitude.png){: .img-center loading=lazy }

## Post-traitement du squelette droit pour obtenir la forme à pignon (*Gabled*)

En considérant le squelette droit précédemment créé, on peut donc décomposer le polygone initial en quatre polygones :

- En rose, 2 polygones à trois sommets (des triangles pour les plus scientifiques)
- En vert, 2 polygones à quatre sommets (à vous de donner la réponse en commentaire !)

![Les quatres polygones associés au squelette droit](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/quatres_polygones_du_skeleton_droit.png){: .img-center loading=lazy }

Ci-dessous, l'écriture de ces quatre polygones au format `JSON`, chacun avec un somment de début et un sommet de fin de polygone :

??? "Les 4 polygones associées au squelette droit"
    ```json title="Les 4 polygones associées au squelette droit"
    {
        "polygons": [
            {
                "vertices": [
                    {
                        "x": 259521.140625,
                        "y": 6253168
                    },
                    {
                        "x": 259540.953125,
                        "y": 6253203.5
                    },
                    {
                        "x": 259505.3125,
                        "y": 6253223.5
                    }
                ],
                "edgeStart": {
                    "x": 259505.3125,
                    "y": 6253223.5
                },
                "edgeEnd": {
                    "x": 259521.140625,
                    "y": 6253168
                }
            },
            {
                "vertices": [
                    {
                        "x": 259606.34375,
                        "y": 6253192.5
                    },
                    {
                        "x": 259570.71875,
                        "y": 6253212.5
                    },
                    {
                        "x": 259540.953125,
                        "y": 6253203.5
                    },
                    {
                        "x": 259521.140625,
                        "y": 6253168
                    }
                ],
                "edgeStart": {
                    "x": 259521.140625,
                    "y": 6253168
                },
                "edgeEnd": {
                    "x": 259606.34375,
                    "y": 6253192.5
                }
            },
            {
                "vertices": [
                    {
                        "x": 259590.5625,
                        "y": 6253248
                    },
                    {
                        "x": 259570.71875,
                        "y": 6253212.5
                    },
                    {
                        "x": 259606.34375,
                        "y": 6253192.5
                    }
                ],
                "edgeStart": {
                    "x": 259606.34375,
                    "y": 6253192.5
                },
                "edgeEnd": {
                    "x": 259590.5625,
                    "y": 6253248
                }
            },
            {
                "vertices": [
                    {
                        "x": 259505.3125,
                        "y": 6253223.5
                    },
                    {
                        "x": 259540.953125,
                        "y": 6253203.5
                    },
                    {
                        "x": 259570.71875,
                        "y": 6253212.5
                    },
                    {
                        "x": 259590.5625,
                        "y": 6253248
                    }
                ],
                "edgeStart": {
                    "x": 259590.5625,
                    "y": 6253248
                },
                "edgeEnd": {
                    "x": 259505.3125,
                    "y": 6253223.5
                }
            }
        ]
    }
    ```

Afin d'obtenir un toit à pignon, nous souhaitons atteindre le résultat suivant :

![Objectif du post-traitement](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/objectif_post_traitement_skeleton_droit.png){: .img-center loading=lazy }

Ainsi, il faut supprimer les polygones roses et modifier les sommets des polygones verts en deux étapes :

- Modification des sommets des deux polygones verts : projection orthogonale des sommets intérieurs sur la base des triangles roses.

![Projection orthogonale des sommets intérieurs](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/projection_skeleton_droit.png){: .img-center loading=lazy }

- Suppression des triangles roses

Ces deux actions peuvent être faites de manières simultanées (à voir dans l'onglet `TypeScript`) :

<iframe height="400" style="width: 100%;" scrolling="no" title="post traitement du skeleton droit pour obtention d'un gabled" src="https://codepen.io/TANK2003/embed/wBwPvqO?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  Allez sur le codepen <a href="https://codepen.io/TANK2003/pen/wBwPvqO">
  post traitement du squelette droit pour obtention d'un gabled</a> by Karl TAYOU (<a href="https://codepen.io/TANK2003">@TANK2003</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Notre squelette maintenant adapté au type de toit, il faut affecter une hauteur à chaque sommet.

## Ajout de la hauteur à chaque sommet du squelette

Pour représenter les polygones en WebGL (et donc avec Three.js et Giro3D), il convient de réaliser un réseau triangulé irrégulier (*Triangulated Irregular Network*, TIN) à partir du squelette modifié. Les triangles disposent des avantages suivants :

- Les triangles sont la forme polygonale la plus simple, définie par seulement trois sommets. Ils représentent une surface toujours plane quelle que soit la position des sommets.
- Tout polygone, aussi complexe soit-il, peut être décomposé en un ensemble de triangles.

La triangulation est réalisée avec la bibliothèque JS [Earcut](https://github.com/mapbox/earcut) pour obtenir la géométrie ci-dessous : Chaque polygone est représenté par deux triangles.

<iframe height="400" style="width: 100%;" scrolling="no" title="Triangulation de la géométrie de notre toiture" src="https://codepen.io/TANK2003/embed/azoVzVa?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  Allez sur le codepen <a href="https://codepen.io/TANK2003/pen/azoVzVa">
  Triangulation de la géométrie de notre toiture</a> by Karl TAYOU (<a href="https://codepen.io/TANK2003">@TANK2003</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Pour rappel, voici les informations importantes pour l'affectation des hauteurs :

- Hauteur de la toiture : 10 m.
- Hauteur du bâtiment par rapport au sol : 31 m.
- Hauteur du point le plus bas de la toiture : 48 m (*height* 58 m - *roof:height* 10 m).

Dans le cas de notre polygone, la détermination des hauteurs est assez simple car il n'y a que deux hauteurs différentes.

Dans le cas de toitures plus complexes et à des fins d'industrialisation de la solution, nous avons défini une formule de détermination générale de la hauteur pour chaque point de notre géométrie. Soit le point i, son altitude est définie de la manière suivante :

$Zi = height - roof:height + roof:height * (Dmax / Di)$

Avec :

- $Zi$, la hauteur du point souhaité.
- $Dmax$, la distance projetée maximale entre le point haut de la toiture et le point bas.
- $Di$, la distance projetée entre le point haut de la toiture et le point souhaité.

![Schéma d'évalution de l'altitude d'un sommet (i)](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/evaluation_altitude_sommet_toiture.png){: .img-center loading=lazy }

Dans notre cas, la formule ci-dessous est égale à :

$Zi = 58 - 10 + 10 * (Dmax / Di) = 48 + 10 * (Dmax / Di)$

La même schéma mais en 3D pour une meilleure représentation de `Dmax`:

![Représentation du Dmax](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/representation_dmax.png){: .img-center loading=lazy }

Pour déterminer la valeur $Dmax$, on analyse tous les polygones par itération afin de déterminer la distance projetée entre deux points la plus importante sur notre géométrie. La fenêtre ci-dessous détaille les caluls implémentés.

<iframe height="400" style="width: 100%;" scrolling="no" title="Visualisation des sommets de debuts et de fin + calcul de Hmax" src="https://codepen.io/TANK2003/embed/ByBmrOb?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  Allez sur le codepen <a href="https://codepen.io/TANK2003/pen/ByBmrOb">
  calcul de Dmax</a> by Karl TAYOU (<a href="https://codepen.io/TANK2003">@TANK2003</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Nous avons déterminé $Dmax$ pour notre exemple, sa valeur est de 28.85 m. La formule ci-dessus est utilisée afin de déterminer chaque hauteur de sommet. On peut alors visualiser notre toiture en 3D à l'aide de Three.js (n'hésitez pas à bouger la scène avec votre souris :mouse2:).

<iframe height="500" style="width: 100%;" scrolling="no" title="Affectation de l'altitude à chaque sommet des triangles" src="https://codepen.io/TANK2003/embed/YPKELWd?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href="https://codepen.io/TANK2003/pen/YPKELWd">
  Affectation de l'altitude à chaque sommet des triangles</a> by Karl TAYOU (<a href="https://codepen.io/TANK2003">@TANK2003</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Dans ce troisième article, nous avons construit la toiture d’un bâtiment issu d’OpenStreetMap. Les principales étapes sont la génération du squelette droit, sa correction éventuelle, la triangulation et la détermination de la hauteur de chaque sommet. Dans le prochain article, nous présentons la génération des façades afin de produire le modèle géométrique 3D complet du bâtiment.

[2 : Des données à la cartographie :fontawesome-solid-backward-step:](./2025-03-10_osm-data-3D-02-donnees-diffusion.md "Des données à la cartographie"){: .md-button }
{: align=middle }

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
