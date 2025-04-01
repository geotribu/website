---
title: "Le constat : les calculs géométriques ne sont pas bons"
subtitle: "Série : De la tolérance en SIG - partie 1"
authors:
    - Loïc Bartoletti
categories:
    - article
comments: true
date: 2024-07-18
description: "Premier chapitre du tour d'horizon des SIG sur la précision des calculs géométriques : analyse des opérations de superposition et de leurs limites."
icon: material/vector-intersection
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_01_calculs.png
license: beerware
robots: index, follow
tags:
    - analyse
    - géométrie
    - QGIS
    - topologie
    - WKB
    - WKT
---

# Le constat : les calculs ne sont pas bons

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

Dans nos SIG, les opérations de superposition (_overlay_ dans la langue de Shakespeare) telles que les intersections, les unions, les différences, etc. ainsi que l'accrochage utilisé par les dessinateurs, sont omniprésentes. Ces processus s'appuient sur des calculs similaires, simplifiés ici pour une meilleure compréhension dans cette présentation générale.

![Série d'été 2024 de Loïc Bartoletti - Les Géométries et les SIG : calculs - Crédits : Sylvain Beorchia](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_01_calculs.png){: .img-center loading=lazy }

Cet article est la première partie de la série d'été sur la gestion de la géométrie dans les SIG.

[Le dossier :octicons-move-to-start-16:](2024-07-16_de-la-tolerance-en-sig-geometrie-00-annonce.md "De la tolérance en SIG : le dossier"){: .md-button }
{: align=middle }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Identification du problème

### Chargement des données

![icône add layer](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/qgis_icon_mActionAddOgrLayer.png){: .img-thumbnail-left }

Toutes les données utilisées sont disponibles sur [mon GitHub](https://github.com/lbartoletti/lbartoletti.github.io/tree/master/assets/2024_intersection_intersects), et pour simplifier la compréhension et la transposition de ces données dans différents SIG, j'utiliserai les formats WKB et WKT[^wkt_wkb].

!!! tip "autopromo"
    Pour celles et ceux qui veulent en savoir plus sur ces formats, pensez à suivre Geotribu sur les réseaux sociaux ou à vous abonner à notre [newsletter](https://geotribu.fr/newsletter/signup/) pour être informé du prochain article dédié :wink:.

Revenons-en au fait, prenons un exemple avec une géométrie de type ligne, ici fermée, mais cela serait similaire pour un polygone (puisqu'un polygone est une ligne). Les géométries utilisées sont projetées dans le système de coordonnées EPSG:3946, projection de mon coin magnifique.

Exemple d'une géométrie de ligne au format WKB :

```bin
0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341
```

À partir de cette ligne, je génère d'autres lignes qui s'accrochent aux points d'intersection/accrochage avec la ligne suivante :

```bin
010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341
```

Sur QGIS, on peut charger ces WKB - ainsi que les EWKB, EWKT, WKT - avec le très utile plugin [QuickWKT](https://plugins.qgis.org/plugins/QuickWKT/).

![Plugin QGIS QuickWKT](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/quickwkt_base.png){: .img-center loading=lazy }

Ce qui nous donne :

![QGIS - Base and line](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/base_line.png){: .img-center loading=lazy }

### Intersections de ces lignes

![icône intersection](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/qgis_icon_mIconSnappingIntersection.png){: .img-thumbnail-left }

Nous avons désormais notre base pour étudier ce problème de précision/tolérance/intersection.

Justement, calculons l'intersection entre ces lignes. Pour cela, nous allons utiliser l'outil `native:lineintersections` de QGIS.

![Base and line intersection](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/native_lineintersections_base_line.png){: .img-center loading=lazy }

Nous obtenons deux points d'intersection. Visuellement, les résultats sont conformes à nos attentes, les points d'intersection se trouvant précisément sur les lignes.

![Base and line points intersection](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/point_intersection_base_line.png){: .img-center loading=lazy }

Quand je dis « précisément », si l'on visualise sur une échelle totalement « absurde », on a toujours cette superposition.

![Base and line points intersection, absurd scale](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/point_intersection_base_line_absurd_scale.png){: .img-center loading=lazy }

Pour plus tard, on notera leurs WKB :

```bin
0101000000a899efc8c83c3e4175e5698166d55341
```

dont l'équivalent WKT est `POINT(1981640.7849060092 5199258.022088398)`

et

```bin
0101000000b5ebdd9e8f3c3e416bf8515379d55341
```

respectivement `POINT(1981583.6205737416 5199333.301878075)`

### Création de lignes depuis ces intersections

![icône création de ligne](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/qgis_icon_mActionCaptureLine.png){: .img-thumbnail-left }

QGIS propose différentes options pour s'accrocher. On en utilisera deux, l'accrochage sur un sommet et l'accrochage aux intersections.

#### Accrochage sur les points d'intersection

Tout d'abord, on va utiliser la fonctionnalité d'accrochage sur les intersections. Attention, ce n'est pas sur les points que l'on vient de générer, mais sur les intersections entre les géométries. On repère l'icône d'accrochage d'intersection avec une croix. L'accrochage sur un sommet avec un carré.

Dans la vidéo ci-après, je montre comment j'ai généré des lignes de part et d'autre de la ligne principale aux points d'intersection.

![QGIS - Snap line intersection](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/line_snap_draw.gif){: .img-center loading=lazy }

#### Accrochage sur les intersections

Je répète l'opération, cette fois en me focalisant sur les points d'intersection. L'objectif est de garantir l'accrochage précis sur la ligne principale, indépendamment des variations des sommets adjacents.

![QGIS - Snap line points intersection](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/line_intersection_draw.gif){: .img-center loading=lazy }

#### Comparaison des points d'accrochage

On fait confiance à QGIS et, visuellement, les lignes apparaissent bien accrochées à la ligne de base.

Comparons maintenant nos géométries textuelles. On a 8 lignes/segments dans les deux cas.
Si l'accrochage se déroule correctement, on devrait avoir les mêmes points de départs.

`line_intersection` :

| wkb_geom | wkt_geom |
| :------- | :------- |
| b'010200000002000000b5ebdd9e8f3c3e416bf8515379d5534124c410b4923c3e411668a7ae7bd55341' | LineString (1981583.62057374161668122 5199333.30187807511538267, 1981586.70338083151727915 5199342.7289676871150732) |
| b'010200000002000000b5ebdd9e8f3c3e416bf8515379d553414819cb1c8c3c3e41d19efa7177d55341' | LineString (1981583.62057374161668122 5199333.30187807511538267, 1981580.11247404105961323 5199325.78092165384441614) |
| b'010200000002000000a899efc8c83c3e4175e5698166d5534120d8f49bcc3c3e41ff84f6ed68d55341' | LineString (1981640.78490600921213627 5199258.02208839822560549, 1981644.60920477658510208 5199267.71817135717719793) |
| b'010200000002000000a899efc8c83c3e4175e5698166d55341bc8cd13bc53c3e411d15f16064d55341' | LineString (1981640.78490600921213627 5199258.02208839822560549, 1981637.23366622533649206 5199249.5147145064547658) |
| b'010200000002000000a899efc8c83c3e4175e5698166d5534199299383d33c3e412d56acf265d55341' | LineString (1981640.78490600921213627 5199258.02208839822560549, 1981651.51396427140571177 5199255.79176859278231859) |
| b'010200000002000000a899efc8c83c3e4175e5698166d55341faacc621bc3c3e4126b2ed1567d55341' | LineString (1981640.78490600921213627 5199258.02208839822560549, 1981628.13193780044093728 5199260.34263280592858791) |
| b'010200000002000000b5ebdd9e8f3c3e416bf8515379d55341dc272032983c3e41f6e5308b78d55341' | LineString (1981583.62057374161668122 5199333.30187807511538267, 1981592.19580315705388784 5199330.17485951445996761) |
| b'010200000002000000b5ebdd9e8f3c3e416bf8515379d5534167a9c58f873c3e41c2567db879d55341' | LineString (1981583.62057374161668122 5199333.30187807511538267, 1981575.56160982861183584 5199334.88265007920563221) |

`line_snap`:

| wkb_geom | wkt_geom |
| :------- | :------- |
| b'010200000002000000b5ebdd9e8f3c3e416bf8515379d553419c2333eb913c3e417ba04d457cd55341' | LineString (1981583.62057374161668122 5199333.30187807511538267, 1981585.91874907072633505 5199345.08286296855658293) |
| b'010200000002000000b5ebdd9e8f3c3e416bf8515379d553416d6001368d3c3e41080dad2b77d55341' | LineString (1981583.62057374161668122 5199333.30187807511538267, 1981581.2109585062135011 5199324.68243718892335892) |
| b'010200000002000000b5ebdd9e8f3c3e416bf8515379d553412f400c50963c3e413ab69fef78d55341' | LineString (1981583.62057374161668122 5199333.30187807511538267, 1981590.31268693110905588 5199331.74412303604185581) |
| b'010200000002000000b5ebdd9e8f3c3e416bf8515379d5534142628f76863c3e41b7d3bff479d55341' | LineString (1981583.62057374161668122 5199333.30187807511538267, 1981574.46312536345794797 5199335.82420819159597158) |
| b'010200000002000000a899efc8c83c3e4175e5698166d55341259db491ca3c3e410908b4b168d55341' | LineString (1981640.78490600921213627 5199258.02208839822560549, 1981642.56916219857521355 5199266.77661324385553598) |
| b'010200000002000000a899efc8c83c3e4175e5698166d5534175e25c6ad23c3e4164c45eac65d55341' | LineString (1981640.78490600921213627 5199258.02208839822560549, 1981650.41547980648465455 5199254.69328412786126137) |
| b'010200000002000000a899efc8c83c3e4175e5698166d55341cccd8ccdc63c3e414a00e65664d55341' | LineString (1981640.78490600921213627 5199258.02208839822560549, 1981638.80292974691838026 5199249.35778815485537052) |
| b'010200000002000000a899efc8c83c3e4175e5698166d55341d0a0d012bd3c3e4126b2ed1567d55341' | LineString (1981640.78490600921213627 5199258.02208839822560549, 1981629.07349591329693794 5199260.34263280592858791) |

On remarque que nos points d'origine sont dans les deux cas :

- `1981583.62057374161668122 5199333.30187807511538267`
- `1981640.78490600921213627 5199258.02208839822560549`

respectivement en WKB :

- `0101000000b5ebdd9e8f3c3e416bf8515379d55341`
- `0101000000a899efc8c83c3e4175e5698166d55341`

Les lignes semblent donc avoir été correctement accrochées, comme le montrent nos représentations en WKT et WKB.

En effet, on retrouve bien les coordonnées d'origine :

`b5ebdd9e8f3c3e416bf8515379d55341` et `a899efc8c83c3e4175e5698166d55341` dans les points.

### Sélection des lignes intersectant la base

![icône intersection](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/qgis_icon_mIconSelectIntersect.png){: .img-thumbnail-left }

Par conséquent, nous avons des lignes qui sont sur le point d'intersection. Si l'on souhaite vérifier l'accrochage, on utilise le prédicat « intersecte » de QGIS. Pour vérifier cela, utilisons l'outil « sélection par localisation » :

#### Le prédicat `intersects` avec `line_snap`

On regarde si `line_snap` est accroché sur `base`. Dans les exemples ci-après, même si je devrais n'utiliser que touches ou intersects, je vais tout cocher sauf disjoint.

![line snap intersects base](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fr_line_snap_intersects_base.png){: .img-center loading=lazy }

Le résultat :

![selected line snap](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/selected_line_snap.png){: .img-center loading=lazy }

Aïe, seulement 2 sur les 4…

#### Le prédicat `intersects` avec `line_intersection`

On fait de même pour `line_intersection` :

![Line snap intersects base](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fr_line_intersection_intersects_base.png){: .img-center loading=lazy }

Et voici le résultat :

![Select line snap intersects base](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/selected_line_snap.png){: .img-center loading=lazy }

Re Aïe. Seulement 2 sur les 4, et du même côté. C'est au moins ça de cohérent dans notre incohérence…

#### Est-ce que ce n'est que pour ces deux points ?

Pour aller plus loin, je réalise des tests aléatoires en essayant d'accrocher la ligne principale à différents endroits. C'est la couche `test_line` dans le GeoPackage.

![Spiderman](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/test_line_spider.png){: .img-center loading=lazy }

Dans notre franchise [OSGeo](https://www.osgeo.org), QGIS est un de nos superhéros, tel [Spider-Man](https://www.youtube.com/watch?v=i5P8lrgBtcU). Notre petite toile d'araignée manque de [glu](https://www.youtube.com/watch?v=rf6Yv4lMhhs), car notre accrochage n'est toujours pas bon :

![Spider selected](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/test_line_spider_selected.png){: .img-center loading=lazy }

#### Testons tous les 1 mètre sur la base

Il y a quelques années, j'ai développé un outil pour créer des transects. Il génère des bandes, suivant un angle donné. Il est principalement utilisé pour des analyses sur des profils en travers, en génie civil, en écologie, etc. Ici, on va réaliser un transect avec l'outil… « transect »,  tous les mètres de part et d'autre de la ligne principale.

Pour commencer, nous allons densifier la géométrie :

![Densify](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fr_densify.png){: .img-center loading=lazy }

Ensuite, on génère de cette couche les transects à gauche et à droite de la ligne (suivant le sens de la ligne) :

![Transect densify left](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fr_transect_densify_left.png){: .img-center loading=lazy }

![Transect densify right](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fr_transect_densify_right.png){: .img-center loading=lazy }

Notre dessin ressemble à :

![Canvas transect](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/transect_left_right.png){: .img-center loading=lazy }

Et maintenant, on va sélectionner les entités de `transect_left` et `transect_right` qui intersectent la base :

![Select transect left](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fr_select_transect_left.png){: .img-center loading=lazy }

![Select transect right](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fr_select_transect_right.png){: .img-center loading=lazy }

Et, non, ce n'est pas l'algo de transect qui est tout buggué.

![Canvas select transect](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/selected_transect_left_right.png){: .img-center loading=lazy }

Mais, comme on dit… "Caramba ! Encore raté !"

![carambar](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/carramba.jpg){: .img-center loading=lazy }

Et si je teste sur la géométrie densifiée ?

![Select transect densify left](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fr_select_transect_left_densify.png){: .img-center loading=lazy }

![Select transect densify right](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fr_select_transect_right_densify.png){: .img-center loading=lazy }

Et notre résultat ?

![Canvas select transect densify](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/selected_transect_left_right_densify.png){: .img-center loading=lazy }

Cela fonctionne ! Mais pourquoi ?

Et bien, nous verrons cela plus tard.

[2 : QGIS et GEOS :fontawesome-solid-forward-step:](./2024-07-25_de-la-tolerance-en-sig-geometrie-02-qgis-et-geos.md "GEOS au cœur de QGIS"){: .md-button }
{: align=middle }

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}

<!-- Notes de bas de page -->

<!-- markdownlint-disable   MD007 MD032 -->
[^wkt_wkb]: formats standards de représentation des géométries :

    - **WKB (Well-Known Binary)** : Le WKB est un format binaire utilisé pour représenter des objets géométriques de manière compacte et efficace, couramment utilisé dans les bases de données géospatiales pour le stockage et l'échange de données géographiques.
    - **WKT (Well-Known Text)** : Le WKT est un format texte utilisé pour représenter des objets géométriques de manière lisible par l'humain. Il est souvent utilisé pour le partage et l'affichage de données géographiques.

    Pour plus d'informations, consultez la page [Wikipedia](https://fr.wikipedia.org/wiki/Well-known_text).
<!-- markdownlint-enable  MD007 MD032 -->
