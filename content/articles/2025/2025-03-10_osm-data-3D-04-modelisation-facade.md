---
title: "OSM Data : Extrusion des données en 3D - suite"
subtitle: OSM Data 4/5
authors:
    - Karl TAYOU
    - Romain LATAPIE
categories:
    - article
comments: true
date: 2025-03-25
description: "OSM DATA 3D : des données 2D à leur représentation en 3D - suite"
icon: material/video-3d
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

# OSM DATA V2 : de la visualisation cartographique à la scène 3D - suite

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

Dans l'épisode précédent, nous avons pu présenter le processus de génération de la toiture d'un bâtiment issu d'OpenStreetMap. Dans cet article, nous poursuivons notre processus de modélisation 3D en nous concentrant sur la création des façades.

L'objectif ici est donc de reconstruire les polygones comme celui présenté en bleu dans la figure ci-dessous.

![Représentation des façades](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/representation_facade.png){: .img-center loading=lazy }

## Création des façades

Pour rappel, voici les informations importantes de nôtre bâtiment exemple de l'article précédent :

- Hauteur de la toiture : 10 m.
- Hauteur du bâtiment par rapport au sol : 31 m.
- Hauteur du point le plus bas de la toiture : 48 m (*height* 58 m - *roof:height* 10 m).
- Hauteur du point le plus haut du bâtiment par rapport au sol : 58 m.

Les façades correspondent à des polygones produits à l'aide des sommets de la toiture et de leurs projections sur une surface de référence de hauteur constante *min_height*, 31 m dans notre exemple.

Sur l'image ci dessous, les sommets A ($Ax$, $Ay$, $Az$), B ($Bx$, $By$, $Bz$) et C ($Cx$, $Cy$, $Cz$) correspondent aux sommets de notre toiture. Les coordonnées des sommets projetés sont définis de la manière suivante :

- A'($Ax$, $Ay$, *min_height*)
- B'($Bx$, $By$, *min_height*)
- C'($Cx$, $Cy$, *min_height*)

![Définition des coordonnées d'une façade](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/modelisation_triangles_polygone.png){: .img-center loading=lazy }

En itérant sur l'ensemble des segments composant le périmètre du bâtiment, on peut donc définir l'ensemble des sommets constituant les façades.

WebGL ne pouvant gérer les polygones à plus de trois sommets, une triangulation est réalisée sur chaque façade du bâtiment.

On aurait pu refaire cette manipulation avec [Earcut](https://github.com/mapbox/earcut) mais on a décidé de se compliquer la vie en se rajoutant le défi de réaliser la triangulation. On considère donc le premier point du polygone, et les deux points suivants pour définir notre premier triangle. Pour le second triangle, on considère le second sommet et les deux suivants et on recommence ce processus itératif jusqu'au dernier point, ou sont alors considérés les deux premiers sommets traités. Ce traitement permet de s'assurer qu'on obtient des géométries fermées. Si vous n'avez rien compris, c'est normal, utilisez [Earcut](https://github.com/mapbox/earcut).

![Modélisation des triangles d'un polygone](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/osm_data/article_3/modelisation_traingles_polygone_2.png){: .img-center loading=lazy }

Plus en détails, c'est la fonction ci-dessous qui permet de trianguler les façades :

```javascript title="Triangulation des façades"
// positions représente tous les sommets de notre toiture
function createWallTriangles(positions: Array<Vector3>) {
  const postionsResult = positions.slice();

  for (let index = 0; index < positions.length; index++) {
    const A = positions[index];
    const B = positions[index + 1] ? positions[index + 1] : positions[0];

    // Triangle A, B, A'
    postionsResult.push(A); // A
    postionsResult.push(B); // B
    postionsResult.push(new Vector3(A.x, A.y, minHeight)); // A'

    // Triangle A',B,B'
    postionsResult.push(new Vector3(A.x, A.y, minHeight)); // A'
    postionsResult.push(B); // B
    postionsResult.push(new Vector3(B.x, B.y, minHeight)); // B'
  }

  return postionsResult;
}
```

Une fois que toutes les façades sont triangulées, leur affichage peut être réalisé en 3D à l'aide de Three.js :

<iframe height="400" style="width: 100%;" scrolling="no" title="Modélisation des facades" src="https://codepen.io/TANK2003/embed/KwPZqLK?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  Consultez le codeen <a href="https://codepen.io/TANK2003/pen/KwPZqLK">
  Modélisation des facades</a> by Karl TAYOU (<a href="https://codepen.io/TANK2003">@TANK2003</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Pour terminer la reconstruction architecturale 3D, vous trouverez ci-dessous l'ensemble des résultats générés dans le cadre des deux articles. Le dernier affichage permet de représenter la toiture et les façades assemblées sous un même objet.

<iframe height="500" style="width: 100%;" scrolling="no" title="Résumé des étapes de construction de la toitures" src="https://codepen.io/TANK2003/embed/vEBrgyo?default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  Allez sur le codepen <a href="https://codepen.io/TANK2003/pen/vEBrgyo">
  Résumé des étapes de construction du bâtiment</a> by Karl TAYOU (<a href="https://codepen.io/TANK2003">@TANK2003</a>)
  on <a href="https://codepen.io">CodePen</a>.
</iframe>

Ainsi s'achève la présentation de reconstruction architecturale 3D en niveau de détail CityGML LOD2. Dans le dernier article, nous présentons le processus de visualisation de l'ensemble des données d'OSM DATA en 3D avec Giro3D.

[3 : des données 2D à leur représentation en 3D - première partie :fontawesome-solid-backward-step:](./2025-03-10_osm-data-3D-03-modelisation-toiture.md "des données 2D à leur représentation en 3D - première partie"){: .md-button }
{: align=middle }

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
