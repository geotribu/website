---
title: De la tolérance en SIG
subtitle: La vraie tolérance consiste à voir large sans perdre la mesure (c) Barratin
authors:
    - Loïc Bartoletti
categories:
    - article
comments: true
date: 2024-07-05
description: "Un tour d'horizon des SIG sur la précision des calculs géométriques."
icon: material/vector-intersection
image:
license: beerware
robots: index, follow
tags:
    - analyse
    - ArcGIS
    - FME
    - géométrie
    - GEOS
    - GRASS
    - PostGIS
    - QGIS
    - SAGA
    - SFCGAL
    - topologie
---

# De la tolérance en SIG

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

Régulièrement, j'ai des questions sur certaines « irrégularités » rencontrées lors d'opérations courantes :

- Pourquoi l'accrochage dans QGIS ne se positionne-t-il pas toujours exactement sur la géométrie ?
- Pourquoi les calculs lors des opérations de superposition semblent manquer de précision ?
- Et pourquoi un calcul et son inverse ne produisent-ils pas toujours des résultats cohérents ?

Ces questions reflètent des préoccupations courantes parmi les utilisateurs de SIG, qui s'attendent à une exactitude et à une précision rigoureuses. La maxime "rigueur, rigueur, rigueur", si chère à l'un de mes anciens chefs, n'est pas toujours… de rigueur sur nos ordinateurs.

Alors que je préparais un article sur la topologie que je dois à [Julien](https://geotribu.fr/team/julien-moura/) depuis plusieurs mois, j'ai été frappé par ce que l'on appelle le [phénomène Baader-Meinhof, ou l'illusion de fréquence](https://fr.wikipedia.org/wiki/Illusion_de_fr%C3%A9quence) : soudainement, ce sujet paraît surgir partout, des cours aux discussions en ligne. Entre les _issues_ signalées et les conversations avec mes collègues, j'ai décidé de changer mon fusil d'épaule. Plutôt que de continuer sur le chemin prévu, j'ai opté pour réaliser plusieurs séries d'articles, explorant certains traitements, « problèmes », différences dans les SIG. Cet article, subdivisé en chapitres, fera partie d'une série qui vise donc à montrer le dessous des SIG.

Dans les sections suivantes, nous explorerons ensemble :

- Le constat : les calculs ne sont pas bons.
- Fonctionnement Interne de QGIS et GEOS : comment ces outils gèrent-ils les données et les opérations géométriques.
- Et les autres SIG Open Source ? Comparaisons avec GRASS et SAGA.
- Et dans les bases de données ? Comparaisons de SQL Server, Oracle et PostGIS.
- Utilisation de la Topologie : est-ce que la topologie peut nous sauver ?
- Approche alternative : exploration de méthodes alternatives telles que l'utilisation de SFCGAL pour des calculs plus robustes.
- Et chez la concurrence, ça se passe comment ?
- Algorithmes et Code : comment cela fonctionne-t-il ? Cette partie sera optionnelle, pour ceux ne voulant pas voir de code.
- La conclusion : comment arrêter de trop penser et vivre une vie meilleure !

Êtes-vous prêts pour l'aventure ? Sortons nos SIG !

## Le constat : les calculs ne sont pas bons

Dans nos SIG, les opérations de superposition (_overlay_ dans la langue de Shakespeare) telles que les intersections, les unions, les différences, etc. ainsi que l'accrochage utilisé par les dessinateurs, sont omniprésentes. Ces processus s'appuient sur des calculs similaires, simplifiés ici pour une meilleure compréhension dans cette présentation générale.

### Identification du problème

#### Chargement des données

![icône add layer](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/qgis_icon_mActionAddOgrLayer.png){: .img-thumbnail-left }

Toutes les données utilisées sont disponibles sur [mon GitHub](https://github.com/lbartoletti/lbartoletti.github.io/tree/master/assets/2024_intersection_intersects), et pour simplifier la compréhension et la transposition de ces données dans différents SIG, j'utiliserai les formats WKB et WKT[^1].

!!! tip "autopromo"
    Pour celles et ceux qui veulent en savoir plus sur ces formats, pensez à suivre Geotribu sur les réseaux sociaux ou à vous abonner à notre [newsletter](https://geotribu.fr/newsletter/signup/) pour être informé du prochain article dédié :wink:.

Revenons-en au fait, prenons un exemple avec une géométrie de type ligne, ici fermée, mais cela serait similaire pour un polygone (puisqu'un polygone est une ligne). Les géométries utilisées sont projetées dans le système de coordonnées EPSG:3946, projection de mon coin magnifique.

Exemple d'une géométrie de ligne au format WKB : :

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

#### Intersections de ces lignes

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

#### Création de lignes depuis ces intersections

![icône création de ligne](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/qgis_icon_mActionCaptureLine.png){: .img-thumbnail-left }

QGIS propose différentes options pour s'accrocher. On en utilisera deux, l'accrochage sur un sommet et l'accrochage aux intersections.

##### Accrochage sur les points d'intersection

Tout d'abord, on va utiliser la fonctionnalité d'accrochage sur les intersections. Attention, ce n'est pas sur les points que l'on vient de générer, mais sur les intersections entre les géométries. On repère l'icône d'accrochage d'intersection avec une croix. L'accrochage sur un sommet avec un carré.

Dans la vidéo ci-après, je montre comment j'ai généré des lignes de part et d'autre de la ligne principale aux points d'intersection.

![QGIS - Snap line intersection](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/line_snap_draw.gif){: .img-center loading=lazy }

##### Accrochage sur les intersections

Je répète l'opération, cette fois en me focalisant sur les points d'intersection. L'objectif est de garantir l'accrochage précis sur la ligne principale, indépendamment des variations des sommets adjacents.

![QGIS - Snap line points intersection](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/line_intersection_draw.gif){: .img-center loading=lazy }

##### Comparaison des points d'accrochage

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

#### Sélection des lignes intersectant la base

![icône intersection](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/qgis_icon_mIconSelectIntersect.png){: .img-thumbnail-left }

Par conséquent, nous avons des lignes qui sont sur le point d'intersection. Si l'on souhaite vérifier l'accrochage, on utilise le prédicat « intersecte » de QGIS. Pour vérifier cela, utilisons l'outil « sélection par localisation » :

##### Le prédicat `intersects` avec `line_snap`

On regarde si `line_snap` est accroché sur `base`. Dans les exemples ci-après, même si je devrais n'utiliser que touches ou intersects, je vais tout cocher sauf disjoint.

![line snap intersects base](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fr_line_snap_intersects_base.png){: .img-center loading=lazy }

Le résultat :

![selected line snap](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/selected_line_snap.png){: .img-center loading=lazy }

Aïe, seulement 2 sur les 4…

##### Le prédicat `intersects` avec `line_intersection`

On fait de même pour `line_intersection` :

![Line snap intersects base](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fr_line_intersection_intersects_base.png){: .img-center loading=lazy }

Et voici le résultat :

![Select line snap intersects base](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/selected_line_snap.png){: .img-center loading=lazy }

Re Aïe. Seulement 2 sur les 4, et du même côté. C'est au moins ça de cohérent dans notre incohérence…

##### Est-ce que ce n'est que pour ces deux points ?

Pour aller plus loin, je réalise des tests aléatoires en essayant d'accrocher la ligne principale à différents endroits. C'est la couche `test_line` dans le GeoPackage.

![Spiderman](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/test_line_spider.png){: .img-center loading=lazy }

Dans notre franchise [OSGeo](https://www.osgeo.org), QGIS est un de nos superhéros, tel [Spider-Man](https://www.youtube.com/watch?v=i5P8lrgBtcU). Notre petite toile d'araignée manque de [glu](https://www.youtube.com/watch?v=rf6Yv4lMhhs), car notre accrochage n'est toujours pas bon :

![Spider selected](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/test_line_spider_selected.png){: .img-center loading=lazy }

##### Testons tous les 1 mètre sur la base

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

![carambar](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/carramba.jpg?raw=true)

Et si je teste sur la géométrie densifiée ?

![Select transect densify left](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fr_select_transect_left_densify.png){: .img-center loading=lazy }

![Select transect densify right](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fr_select_transect_right_densify.png){: .img-center loading=lazy }

Et notre résultat ?

![Canvas select transect densify](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/selected_transect_left_right_densify.png){: .img-center loading=lazy }

Cela fonctionne ! Mais pourquoi ?

Et bien, nous verrons cela plus tard.

[^1] - **WKB (Well-Known Binary)** : Le WKB est un format binaire utilisé pour représenter des objets géométriques de manière compacte et efficace, couramment utilisé dans les bases de données géospatiales pour le stockage et l'échange de données géographiques.

- **WKT (Well-Known Text)** : Le WKT est un format texte utilisé pour représenter des objets géométriques de manière lisible par l'humain. Il est souvent utilisé pour le partage et l'affichage de données géographiques.

Pour plus d'informations, consultez la page [Wikipedia](https://fr.wikipedia.org/wiki/Well-known_text).

## GEOS au cœur de QGIS

Dans la partie précédente, nous avons posé le problème : le résultat d'une intersection n'intersecte pas toujours la donnée d'origine. Cette réalité peut surprendre les nouveaux utilisateurs de SIG et frustrer les plus expérimentés qui cherchent une précision dans leurs analyses spatiales.

Dans cette section, nous allons plonger dans les dessous des SIG en explorant le fonctionnement de ces traitements. Nous nous concentrerons en particulier sur le rôle de GEOS dans QGIS.

### Qu'est-ce que GEOS ?

![logo GEOS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/geos.png){: .img-thumbnail-left }

[GEOS (Geometry Engine - Open Source)](https://libgeos.org/) est une bibliothèque C++ qui fournit des fonctions de calculs sur les géométries Simple Feature OGC. Elle est largement utilisée dans divers outils SIG, y compris QGIS, pour effectuer des calculs géométriques. GEOS est une implémentation de l'API de JTS (Java Topology Suite) qui vise à manipuler des géométries planes en 2D.

![GEOS diagram from crunchy data](https://f.hubspotusercontent00.net/hubfs/2283855/geos-jts%20(1).png)

(Source : <https://www.crunchydata.com/blog/performance-improvements-in-geos>)

### Le rôle de GEOS dans QGIS

Dans QGIS, GEOS joue un rôle crucial dans le traitement des données géographiques. Il est particulièrement utilisé pour évaluer les prédicats spatiaux tels que `intersects`, `touches`, `disjoint`, etc. Ces prédicats sont essentiels pour déterminer les relations spatiales entre différentes géométries.

Pour les connaisseurs du code de QGIS, il est vrai que certains traitements ne sont pas réalisés par GEOS, mais par QGIS. Nous regarderons cela dans la partie sur l'étude des algorithmes, mais en soi, cela ne change pas grand-chose au problème.

### Utilisation de GEOS sans QGIS

Si vous ne le savez pas, il est également possible de réaliser des calculs directement avec GEOS, sans utiliser l'interface graphique de QGIS. Une des façons de faire cela est d'utiliser `geosop`, un outil en ligne de commande qui permet de manipuler des géométries avec les fonctions de GEOS.

`geosop` permet aux utilisateurs d'exécuter des opérations complexes sur les géométries grâce à des commandes simples. Par exemple, pour vérifier si une géométrie en intersecte une autre, on peut utiliser la commande suivante :

```shell
> geosop -a "LineString(0 0, 10 10)" -b "Point(5 5)" intersects
true
> geosop -a "LineString(0 0, 10 10)" -b "Point(5 4)" intersects
false
```

Ici, nous avons utilisé le format WKT pour tester si les géométries `a` et `b` s'intersectent. Par la suite, on ajoutera et expliquera d'autres options au fur et à mesure de nos utilisations.

### Testons notre cas directement avec GEOS

Pour rappel, nos géométries sont les suivantes :

- base : 0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341
- line : 010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341

Pour se faire la main, on va tester si nos géométries s'intersectent bien. On ne l'avait pas testé sur QGIS, mais cela semble évident.

```shell
> geosop \
-a \
"0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341" \
-b \
"010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341" \
intersects
```

!!! tip
    Ici, j'ai utilisé `\` pour que la commande soit sur plusieurs lignes afin de simplifier la lecture de la commande ; vous pouvez évidemment tout faire sur une ligne.

Le résultat retourné est `true`. C'est cohérent.

Maintenant, nous allons calculer l'intersection. Pour cela, on utilise l'opérateur `intersection` au lieu de `intersects`, rien de compliqué.

```shell
> geosop \
-a \
"0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341" \
-b \
"010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341" \
intersection
```

La réponse est `MULTIPOINT ((1981640.7849060092 5199258.022088398), (1981583.6205737416 5199333.301878075))`

Ah ! C'est une petite différence avec QGIS qui retourne deux points. Ici, GEOS retourne un MULTIPOINT, qui, selon moi, est plus cohérent, mais qu'importe.
Le WKT est plus lisible, mais il a l'inconvénient de ne pas toujours avoir la même représentation. QGIS nous retourne 17 décimales et GEOS : 10 ; ce qui, dans tous les cas, est déjà trop pour du projeté, on en reparlera plus tard.

Afin d'éviter ces différences, nous allons travailler avec le WKB. Pour le récupérer, on ajoute simplement l'option WKB à l'option `-f` pour le format de sortie :

```shell
> geosop \
-a \
"0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341" \
-b \
"010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341" \
-f wkb \
intersection
```

Notre résultat est : `0104000000020000000101000000A899EFC8C83C3E4175E5698166D553410101000000B5EBDD9E8F3C3E416BF8515379D55341`

Vous comprendrez mieux l'opération qui va suivre grâce à la lecture de l'article sur le WKT et WKB. En attendant, je vous demande de me faire confiance.
Ce WKB est la représentation d'un multipoint. On peut en extraire les coordonnées des deux points suivants :

- `0101000000A899EFC8C83C3E4175E5698166D55341`
- `0101000000B5EBDD9E8F3C3E416BF8515379D55341`

Ce qui équivaut, moyennant la différence, sans conséquence, entre majuscules et minuscules, à :

- `0101000000a899efc8c83c3e4175e5698166d55341`
- `0101000000b5ebdd9e8f3c3e416bf8515379d55341`

Très bien. Est-ce que le point intersecte ou touche une des géométries d'origine ?

```shell
> geosop \
-a \
"0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341" \
-b \
"0104000000020000000101000000A899EFC8C83C3E4175E5698166D553410101000000B5EBDD9E8F3C3E416BF8515379D55341" \
intersects
```

Ici, je teste si le multipoint intersecte la géométrie `base`. Cela retourne faux.

De même entre le multipoint et `line` :

```shell
> geosop \
-a \
"010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341" \
-b \
"0104000000020000000101000000A899EFC8C83C3E4175E5698166D553410101000000B5EBDD9E8F3C3E416BF8515379D55341" \
intersects
```

Vous pouvez également essayer directement avec les points `0101000000A899EFC8C83C3E4175E5698166D55341` et `0101000000B5EBDD9E8F3C3E416BF8515379D55341`, plutôt que le multipoint.
De même, vous pouvez tester les autres prédicats comme `touches`, le résultat sera toujours `false`...
Sauf pour... `disjoint` ce qui veut dire que les points ne sont pas sur les géométries.

Alors pourquoi, si les points ne sont pas sur les lignes, nous avions sur QGIS des segments qui intersectaient la géométrie d'origine ?

Si vous êtes attentif, vous pouvez remarquer qu'un côté des deux, seulement, avait une intersection ; et ce n'était pas toujours le même.
Je vous laisse regarder les images de la partie précédente.

On commence à toucher du doigt le problème. Le point d'intersection est d'un côté ou de l'autre du segment. Si l'on était sur un hyper zoom, on aurait quelque chose comme :

![Example points along line](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/example_grid_line.png){: .img-center loading=lazy }

En simplifiant, on pourrait dire que les points sont sur de minuscules grilles. Le point n'est pas sur la ligne, mais très proche.

D'ailleurs, demandons à GEOS où se trouvent les points sur nos géométries d'origine.

La distance du premier point par rapport à la `base` :

```shell
> geosop \
-a \
"0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341" \
-b \
"0101000000A899EFC8C83C3E4175E5698166D55341" \
distance
```

`3.356426828584339e-10`

Le second point :

```shell
> geosop \
-a \
"0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341" \
-b \
"0101000000B5EBDD9E8F3C3E416BF8515379D55341" \
distance
```

`3.0508414550559678e-10`

La distance du premier point par rapport à `line` :

```shell
> geosop \
-a \
"010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341" \
-b \
"0101000000A899EFC8C83C3E4175E5698166D55341" \
distance
```

`1.812697635977354e-10`

Le second point :

```shell
> geosop \
-a \
"010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341" \
-b \
"0101000000B5EBDD9E8F3C3E416BF8515379D55341" \
distance
```

`1.7234470954287178e-10`

On remarque que le résultat n'est pas 0, mais très proche. C'est en gros 0, mais y'a une « blague » vers 10 chiffres après la virgule.
Pour celles et ceux que cela intéresse, je reviendrai sur l'importance du calcul dans la partie algorithme.
En attendant, on observe que QGIS donne le même résultat que GEOS. Ce qui n'est pas étonnant puisque derrière QGIS [^1], c'est GEOS.

C'est donc GEOS qui est faux ? Non, GEOS donne le « bon » résultat, mais la vérité est ailleurs.
Nous continuerons cette exploration dans les parties suivantes.

[^1] Comme expliqué avant, QGIS réalise certains calculs, identiques à ceux de GEOS, pourtant sans utiliser cette bibliothèque. En particulier, l'accrochage ne repose pas sur GEOS, mais sur des calculs équivalents. Je simplifie ici pour éviter de perdre les moins connaisseurs de cet écosystème.

## Et les autres SIG Open Source ? Comparaisons avec GRASS et SAGA

### GRASS : Le vénérable du SIG

![logo GRASS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/grass.png){: .img-thumbnail-left }

Comme j'ai déjà trahi les petits secrets internes, Julien m'avait ~~demandé~~ proposé de faire une version actualisée de cet [article](https://geotribu.fr/articles/2014/2014-11-13_corriger_automatiquement_geometries_invalides_qgis/). J'ai ~~procrastiné~~ volontairement, attendu jusqu'en 2024, pour fêter les 10 ans de l'article. Mais, ce n'est pas dans celui-là que je le ferai. Néanmoins, on va bien évidemment utiliser GRASS pour tester si notre cas est différent avec GRASS.

Pour notre expérience avec GRASS, il faudra faire quelques manipulations, car on n'a pas la possibilité de faire directement nos calculs avec le WKB.
Afin de simplifier la reproductibilité aux lecteurs, j'ai ajouté des modèles de traitements dans le projet ; ils sont également disponibles individuellement sur mon GitHub.

#### Utilisation de v.overlay

Dans GRASS, `v.overlay` permet de réaliser des opérations… d'overlay - superposition en français - (intersection, union, différence) entre deux couches vectorielles. Il nécessite deux vecteurs, dont le second B, doit être de type « area » (polygone en langage OGC). Si le vecteur n'est pas un polygone, il nécessite une conversion avant d'effectuer le traitement ; ce qui est notre cas.

La couche `base` est une polyligne fermée, elle sera utilisée pour être convertie en polygone. Pour les puristes, on regardera que les coordonnées du WKB sont bien identiques entre le linestring et le (multi)polygone. Il y a plusieurs façons de procéder, mais, pour rendre accessible à tous, nous allons utiliser GRASS via QGIS, j'utilise les premières conversions dans QGIS ; ensuite, nous utiliserons uniquement les outils de GRASS.

![grass_line_overlay_points](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/grass_line_overlay_points.svg)

Notre algorithme va convertir la `base` en polygone, puis effectuer l'opération d'overlay. Pour calculer l'intersection entre `line` et `base_poly`, on extrait les points d'intersections que l'on peut afficher dans QGIS. On retrouve le même résultat, ici, je passe les détails, mais on retrouve bien nos WKB :

- `0101000000a899efc8c83c3e4175e5698166d55341`
- `0101000000b5ebdd9e8f3c3e416bf8515379d55341`

Pour le prédicat `intersects`, nous allons continuer d'utiliser GRASS avec la commande `v.select` avec l'opération `intersects`.
Encore false… du moins, les points retournés sont ceux des extrémités de `line` et aucun point pour `base` ou `base_poly`.

![grass_select_line_overlay](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/grass_select_line_overlay_points.svg){: .img-center loading=lazy }

Le modèle est disponible [ici](https://github.com/lbartoletti/lbartoletti.github.io/blob/master/assets/2024_intersection_intersects/data/processing/line_overlay_points.model3).

C'est au moins rassurant, car derrière `v.select` avec l'opérateur `intersects` on utilise… GEOS.
Il existe une autre façon de réaliser la sélection, mais je la garde pour la prochaine partie :wink:

### SAGA : Le Chevalier Oublié du SIG

![logo SAGA](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/logo_saga.png){: .img-thumbnail-left }

Si [SAGA](https://fr.wikipedia.org/wiki/Saga_(personnage)) est le plus puissant des chevaliers du zodiaque, [SAGA GIS](https://saga-gis.sourceforge.io/en/index.html) est malheureusement bien souvent le chevalier oublié du SIG. Il possède certains traitements qui ne sont pas disponibles dans QGIS et peut également se révéler utile pour d'autres existants.

Depuis quelques versions, il n'est plus possible d'avoir les traitements de SAGA directement depuis QGIS. Il faut installer le plugin [SAGA NG](https://plugins.qgis.org/plugins/processing_saga_nextgen/) mais il a quelques limitations m'empêchant de l'utiliser pour l'article.
Pour cette partie, je vais directement passer par l'interface de SAGA, notamment afin de visualiser le résultat.

Il est intéressant de comparer le résultat de SAGA avec GEOS/QGIS. En effet, les opérations d'overlay ne reposent pas sur GEOS, mais sur une autre bibliothèque dédiée ; pour ceux intéressés, j'y reviendrai dans la partie sur les algorithmes.

Comme pour les autres, nous allons réaliser les points d'intersection entre `line` et `base`, puis tester si ceux-ci intersectent les géométries d'origine et également, combien de lignes de `test_line` intersectent `base`.

Tout d'abord, SAGA, ne sait pas lire le GeoPackage. J'ai réalisé une conversion de nos couches dans ce bon vieux ShapeFile.

On charge ces fichiers dans l'interface de SAGA.

![Load shapes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/saga_load_shapes.png){: .img-center loading=lazy }

Nous affichons nos données. Rien de surprenant, on se retrouve avec nos deux géométries.

![Map base line](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/saga_map_base_line.png){: .img-center loading=lazy }

Première étape, vérifier le calcul d'intersection. Dans le vocabulaire de SAGA, l'intersection entre lignes s'appelle "Crossing".
On exécute le traitement : Geoprocessing -> Shapes -> Lines -> Line Crossing

![Line Crossing](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/saga_line_crossing.png){: .img-center loading=lazy }

On retrouve bien nos deux points :

![Map crossing](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/saga_map_crossing.png){: .img-center loading=lazy }

Je passe ici les étapes pour leurs récupérations, mais, les WKB sont bien les mêmes, à savoir :

- `0101000000b5ebdd9e8f3c3e416bf8515379d55341`
- `0101000000a899efc8c83c3e4175e5698166d55341`

L'algorithme de SAGA qui, rappelons-le, n'utilise pas GEOS retourne le même résultat. Très bien !

### sélection

Maintenant, tentons de vérifier si les points intersectent, ou non, notre base. Pour cela, on utilise l'outil « sélection par localisation » :
Geoprocessing -> Shapes -> Selection -> Selection by localisation.

![Select crossing base](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/saga_select_crossing_base.png){: .img-center loading=lazy }

Paf, erreur intéressante. Cela fonctionne seulement pour un point avec un polygone !

![Select crossing base error](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/saga_select_crossing_base_error.png){: .img-center loading=lazy }

Dans notre expérience avec GRASS, on avait un problème identique. Nous allons donc tester avec `base_poly` :

![Select crossing base poly](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/saga_select_crossing_base_poly.png){: .img-center loading=lazy }

Aucune sélection. Le message d'exécution nous l'indique bien (en Anglais) : "selected shapes: 0"

Même si l'on peut critiquer la méthode, car le dessin a été fait dans un autre contexte, QGIS/GEOS, on va tout de même tester la sélection des lignes :

On va reprendre notre exemple entre base et test_line.

20 sur 34, comme pour GEOS !

![Select base test line](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/saga_select_base_test_line.png){: .img-center loading=lazy }

C'est normal d'une certaine façon. Cependant, le premier test avec crossing, nous montre également que le point d'intersection n'intersecte pas la géométrie d'origine, comme pour GEOS.

## Et dans les bases de données ? Comparaisons de SQL Server, Oracle et PostGIS

Si vous avez bien suivi les parties précédentes, vous savez que PostGIS va utiliser GEOS pour réaliser la plupart de ses opérations.
En particulier, notre cas sur l'intersection et le prédicat « intersects », sera délégué à GEOS.

![GEOS diagram from crunchy data](https://f.hubspotusercontent00.net/hubfs/2283855/geos-jts%20(1).png)

(Source : <https://www.crunchydata.com/blog/performance-improvements-in-geos>)

Dans un premier temps, nous allons vérifier que les résultats de PostGIS sont identiques à ceux de GEOS « natifs », puis nous comparerons avec d'autres bases de données propriétaires.

Autant, je connais très bien PostGIS, autant, ma connaissance est limitée sur les autres bases. Je vous prie de m'excuser s'il y a des erreurs dans les requêtes ou des façons de faire plus académiques. Si une erreur se glisse ou une meilleure méthode existe, surtout n'hésitez pas à laisser un commentaire, respectueux, et je corrigerai cela.

### PostGIS, même résultat que GEOS

![logo PostGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/postgis.jpg){: .img-thumbnail-left }

Le titre donne directement la conclusion, mais c'était déjà annoncé.

Nous allons reprendre nos deux WKB :

- base : `0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341`

- ligne : `010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341`

```sql
 SELECT ST_Intersection(base, line) FROM ST_GeomFromWKB(decode('0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341', 'hex'), 3946) as base, ST_GeomFromWKB(decode('010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341', 'hex'), 3946) as line;
```

`01040000206A0F0000020000000101000000A899EFC8C83C3E4175E5698166D553410101000000B5EBDD9E8F3C3E416BF8515379D55341`

Retourne un EWKB, d'où la différence avec notre WKB de GEOS ; j'expliquerai cela dans le prochain article sur le WKB/WKT.

Si l'on enlève la partie « E », à savoir le SRID `0206A0F0`, on se retrouve avec le « bon » WKB :

`0104000000020000000101000000A899EFC8C83C3E4175E5698166D553410101000000B5EBDD9E8F3C3E416BF8515379D55341`

On peut directement le retrouver avec PostGIS en utilisant ST_AsBinary :

```sql
SELECT ST_AsBinary(ST_Intersection(base, line)) FROM ST_GeomFromWKB(decode('0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341', 'hex'), 3946) as base, ST_GeomFromWKB(decode('010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341', 'hex'), 3946) as line;
```

`\x0104000000020000000101000000a899efc8c83c3e4175e5698166d553410101000000b5ebdd9e8f3c3e416bf8515379d55341`

Pour la géométrie lisible, utilisant le format textuel, cela se fait avec `ST_AsText` :

```sql
SELECT ST_AsText(ST_Intersection(base, line)) FROM ST_GeomFromWKB(decode('0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341', 'hex'), 3946) as base, ST_GeomFromWKB(decode('010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341', 'hex'), 3946) as line;
```

`MULTIPOINT((1981640.7849060092 5199258.022088398),(1981583.6205737416 5199333.301878075))`

Je vais légèrement adapter la requête, grâce à des [CTE](https://www.postgresql.org/docs/current/queries-with.html), pour plus de lisibilité par la suite.

```sql
WITH
base AS (
    SELECT ST_GeomFromWKB(decode('0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341', 'hex'), 3946) AS geom
),
line AS (
    SELECT ST_GeomFromWKB(decode('010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341', 'hex'), 3946) AS geom
)
SELECT ST_AsBinary(ST_Intersection(base.geom, line.geom)), ST_AsText(ST_Intersection(base.geom, line.geom)) FROM base, line
```

Retourne le même résultat :
`\x0104000000020000000101000000a899efc8c83c3e4175e5698166d553410101000000b5ebdd9e8f3c3e416bf8515379d55341`
`MULTIPOINT((1981640.7849060092 5199258.022088398),(1981583.6205737416 5199333.301878075))`

```sql
WITH
base AS (
    SELECT ST_GeomFromWKB(decode('0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341', 'hex'), 3946) AS geom
),
line AS (
    SELECT ST_GeomFromWKB(decode('010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341', 'hex'), 3946) AS geom
)
SELECT
    ST_Intersects(base.geom, ST_Intersection(base.geom,line.geom)), ST_Intersects(line.geom, ST_Intersection(base.geom,line.geom)),
    ST_Distance(base.geom, ST_Intersection(base.geom,line.geom)), ST_Distance(line.geom, ST_Intersection(base.geom,line.geom))
FROM base, line
```

On retrouve bien, notre malheureux `false` et notre distance très proche de 0, mais pas 0.

Ils se passent quoi chez les autres ?

### Microsoft SQL Server

![logo MS SQL Server](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/microsoft_sql_server.png){: .img-thumbnail-left }

La syntaxe SQL Server est différente de celle de PostGIS, mais assez lisible. La « grosse » différence est l'ajout du « 0 x » dans le WKB d'entrée. Il s'agit en fait de sa représentation hexadécimale ; plus d'informations dans le prochain article.

Voici cette requête :

```sql
WITH
base AS (
    SELECT geometry::STGeomFromWKB(0x0102000000050000007997C6B68D3C3E4139EB62C260D55341AC9EA7316A3C3E41CBEB40E073D55341403E0BFBC33C3E41B3FC06F380D55341387A2A800C3D3E41F256B8176DD553417997C6B68D3C3E4139EB62C260D55341, 3946) AS geom
),
line AS (
    SELECT geometry::STGeomFromWKB(0x010200000002000000EA9C6D2B873C3E41A03D941B7CD5534133DB7796CE3C3E413FBA569864D55341, 3946) AS geom
)
SELECT
    base.geom.STIntersection(line.geom) AS WKB,
    base.geom.STIntersects(base.geom.STIntersection(line.geom)) AS Intersects_Base_Line,
    line.geom.STIntersects(base.geom.STIntersection(line.geom)) AS Intersects_Line_Base,
    base.geom.STDistance(base.geom.STIntersection(line.geom)) AS Distance_Base_Line,
    line.geom.STDistance(base.geom.STIntersection(line.geom)) AS Distance_Line_Base
FROM base, line;
```

Le résultat, sur SQL Server 15.0.4153, remis en forme, est :

`
0x6A0F0000010402000000B5EBDD9E8F3C3E416BF8515379D55341A899EFC8C83C3E4175E5698166D55341020000000100000000010100000003000000FFFFFFFF0000000004000000000000000001000000000100000001,
false,false,
0,0.00000000023283064365386963
`

Le résultat d'intersects est faux, et pourtant pour un des cas, la distance est égale à 0. Intéressant, est-ce vraiment un zéro ou tellement proche de 0, que ça retourne 0 ? Sinon, le second, est égal à celui de GEOS : 2.3283064365386963e-10

Pour le WKB, il est « particulier », mais nous retrouvons nos coordonnées :

- A899EFC8C83C3E4175E5698166D55341
- B5EBDD9E8F3C3E416BF8515379D55341

SQL Server n'utilise pas GEOS, mais sa propre [bibliothèque](https://docs.lib.purdue.edu/ddad2011/8/). Encore une fois, le problème n'est pas dans le code de GEOS.

### ORACLE Spatial

![logo ORACLE](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/oracle.png){: .img-thumbnail-left }

ORACLE va nous donner des éléments intéressants. Passons directement à la requête :

```sql
WITH
base AS (
    SELECT SDO_UTIL.FROM_WKBGEOMETRY(
        HEXTORAW('0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341')
    ) AS geom
    FROM DUAL
),
line AS (
    SELECT SDO_UTIL.FROM_WKBGEOMETRY(
        HEXTORAW('010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341')
    ) AS geom
    FROM DUAL
)
SELECT
    SDO_GEOM.SDO_INTERSECTION(base.geom, line.geom) AS Intersection,
    SDO_UTIL.TO_WKTGEOMETRY(SDO_GEOM.SDO_INTERSECTION(base.geom, line.geom)) AS WKT,
    SDO_UTIL.TO_WKBGEOMETRY(SDO_GEOM.SDO_INTERSECTION(base.geom, line.geom)) AS WKB,
    SDO_GEOM.RELATE(base.geom, 'ANYINTERACT', SDO_GEOM.SDO_INTERSECTION(base.geom, line.geom), 0.00000000001) AS Intersects_Base_Line,
    SDO_GEOM.RELATE(line.geom, 'ANYINTERACT', SDO_GEOM.SDO_INTERSECTION(base.geom, line.geom), 0.00000000001) AS Intersects_Line_Base,
    SDO_GEOM.SDO_DISTANCE(base.geom, SDO_GEOM.SDO_INTERSECTION(base.geom, line.geom), 0.00000000001) AS Distance_Base_Line,
    SDO_GEOM.SDO_DISTANCE(line.geom, SDO_GEOM.SDO_INTERSECTION(base.geom, line.geom), 0.00000000001) AS Distance_Line_Base
FROM base, line;
```

Dont le résultat, sur ORACLE XE 21, est :

`"{2005,null,null,{1,1,2},{1981583.62057374,5199333.30187808,1981640.78490601,5199258.0220884}}",
"MULTIPOINT ((1981583.62057374 5199333.30187808), (1981640.78490601 5199258.0220884))",
0x0000000004000000020000000001413E3C8F9EDDEBAE4153D5795351F8700000000001413E3CC8C8EF99AB4153D5668169E577,
FALSE,FALSE,
0.00000000104125029291017,0.00000000023283064365387`

Encore une fois ici, un résultat `false`. Comme PostGIS et SQL Server, on retrouve notre distance d'environ 2.3e-10, et une autre de 1e-9. Je trouve intéressant d'avoir ce petit écart sur une distance, mais je m'égare.

Ici, j'ai adapté la requête au langage SDO, expliquons la requête et le résultat :

Comme pour SQL Server, il faut convertir le WKB hexadécimal pour Oracle, on utilise `HEXTORAW`.

Si PostGIS va retourner un EWKB, pour un résultat de géométrie, ORACLE, retourne sa représentation interne, à savoir :
`{2005,null,null,{1,1,2},{1981583.62057374,5199333.30187808,1981640.78490601,5199258.0220884}}`

Ce qui nous intéresse ici est le code `2005` qui veut dire MultiPoint 2D, ainsi que le tableau de coordonnées X/Y `{1981583.62057374,5199333.30187808,1981640.78490601,5199258.0220884}`.

On retrouve cette information avec la représentation WKT à laquelle nous sommes habitués :
`MULTIPOINT ((1981583.62057374 5199333.30187808), (1981640.784906015199258.0220884))`

Je ne vais pas m'étendre sur le WKB qui est « étrange », il est en Big Endian, alors que jusqu'à présent, je n'ai eu que du Little Endian ; encore une fois plus d'explications dans l'article sur le WKB/WKT. Néanmoins, on a quelques différences entre ceux-ci, sans-doute liées à la précision du résultat ; n'étant pas expert ORACLE, il me manque des éléments de compréhension et des tests à mener.

Toutefois, à la représentation après la virgule près, on a le même résultat :

| Base | x1 | y1 | x2 | y2 |
|-|-|-|-|-|
| ORACLE | 1981583.62057374 | 5199333.30187808 | 1981640.78490601 | 5199258.0220884 |
| PostGIS | 1981583.6205737416 | 5199333.301878075 | 1981640.7849060092 | 5199258.022088398 |

J'ai indiqué en introduction qu'ORACLE [allait] nous donner des éléments intéressants, mais pour l'instant, c'est comme les autres ? Oui, mais, il y a un paramètre que je n'ai pas encore expliqué. D'où sort le `0.00000000001` ?

Sur ma version, je n'ai pas de `ST_Intersects` ou un `SDO_Intersects`, je dois utiliser [`RELATE`](https://docs.oracle.com/en/database/oracle/oracle-database/21/spatl/SDO_GEOM-reference.html#GUID-E1209A71-F5D8-42A9-A93E-72657B115579). Nous avons également cela avec [PostGIS](https://postgis.net/docs/ST_Relate.html) (et GEOS). `ANYINTERACT` retourne `TRUE` si les objets ne sont pas disjoints, c'est ce que l'on veut.
Donc, on a notre équivalent de `ST_Intersects` ou plus exactement `not ST_Disjoint`. Toutefois, cela ne nous dit toujours pas ce qu'est ce `0.00000000001`. Vous souvenez-vous du titre principal de cette série ? [La tolérance](https://docs.oracle.com/en/database/oracle/oracle-database/21/spatl/spatial-concepts.html#GUID-7469388B-6D23-4294-904F-78CA3B7191D3).

Il s'agit donc d'une tolérance dans le calcul du prédicat. Avec une valeur « extrême », comme ici, le résultat est faux. Cependant, si l'on utilise une valeur plus cohérente avec notre unité, par exemple `1e-6`, nous aurons enfin notre « bon » résultat tant attendu :

`"{2005,null,null,{1,1,2},
{1981583.62057374,5199333.30187808,1981640.78490601,5199258.0220884}}",
"MULTIPOINT ((1981583.62057374 5199333.30187808), (1981640.78490601 199258.0220884))",
0x0000000004000000020000000001413E3C8F9EDDEBAE4153D5795351F8700000000001413E3CC8C8EF99AB4153D5668169E577,
TRUE,TRUE,
0,0`

Les géométries WKT et WKB sont identiques, en revanche, on obtient `TRUE` et `0`.

Comment interpréter cela ? L'utilisation de la tolérance va être plus… tolérante dans le calcul. Dans notre cas, on va retourner vrai, si le point est aux alentours de la géométrie d'environ la tolérance donnée, ici 1e-6.

En PostGIS, on pourrait réécrire cela avec ST_DWithin :

```sql
WITH
base AS (
    SELECT ST_GeomFromWKB(decode('0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341', 'hex'), 3946) AS geom
),
line AS (
    SELECT ST_GeomFromWKB(decode('010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341', 'hex'), 3946) AS geom
)
SELECT
    ST_DWithin(base.geom, ST_Intersection(base.geom,line.geom), 1e-6), ST_DWithin(line.geom, ST_Intersection(base.geom,line.geom), 1e-6)
FROM base, line;
```

Enfin, concernant la distance, ORACLE accepte un paramètre tolérance et donne un résultat différent suivant ce paramètre.
On pourrait penser que la distance devrait toujours être la même. Cependant, je pense — supposition, car connaissant mal ORACLE — que celle-ci sert à arrondir si l'on est dans sa plage, et alors, pour notre cas, retourne 0, plutôt qu'un presque zéro.

Notre exploration n'est pas encore terminée, même si l'on s'approche de l'explication. On vient de voir, que, comme les SIG OpenSource, on ignore comment retourner correctement le prédicat `intersects` d'une intersection. Sauf à être tolérant, et nous y reviendrons.

## Utilisation de la topologie : est-ce que la topologie peut nous sauver ?

Dans les SIG, on distingue souvent deux types de modèles pour représenter les données spatiales : le modèle « spaghetti » et le modèle topologique.

SIG Spaghetti : dans un système de type spaghetti, les entités géographiques sont stockées et gérées individuellement, sans relations explicites entre elles. Chaque ligne ou polygone est dessiné sans tenir compte d'autres éléments qui pourraient se toucher ou se chevaucher. Cela peut conduire à des incohérences, comme des doublons de lignes ou des intersections non gérées, ce qui complique les analyses spatiales et peut réduire la précision des résultats.

Topologie : À l'inverse, la topologie dans QGIS (ou dans tout autre SIG supportant ce modèle) s'assure que les entités spatiales sont stockées avec des règles qui définissent et maintiennent les relations spatiales entre les entités. Par exemple, deux polygones adjacents partageront une ligne commune sans duplication, et les intersections seront gérées correctement. La gestion topologique aide à prévenir les erreurs géométriques, améliore la précision des analyses et facilite la maintenance des données.

Non, ce n'est toujours pas ici que je ferai l'article sur la topologie. Au mieux, cela sert de teaser.

### Retour sur GRASS

L'une des caractéristiques de GRASS GIS est sa gestion topologique des données vectorielles. Contrairement à d'autres systèmes qui utilisent un modèle de données « spaghetti », où les entités géométriques sont stockées sans considération explicite des relations spatiales entre elles, GRASS GIS maintient une structure topologique stricte.

#### Overlap pour une meilleure sélection dans GRASS

Dans la partie précédente, j'ai indiqué qu'il y avait une autre façon de faire du `v.select`. En effet, on a utilisé GEOS avec `intersects`.

La documentation de GRASS mentionne un autre opérateur `overlap`, celui par défaut et utilisant les fonctions GRASS natives. Quel est le résultat ?

Oui, celui que l'on attend ! Enfin ! Tant sur la `base` que sur la `line`, les points d'intersection intersectent bien les géométries d'origine !

#### Utilisation de v.clean

Mais, comme GRASS est topologique, on peut également s'en servir pour retrouver nos intersections. Pour cela, on va réaliser un petit hack pour simplifier nos calculs.

Pour utiliser la topologie, nous allons faire l'union de nos deux lignes de `base` et `line` pour ensuite nettoyer celles-ci.
Le nettoyage, via `v.clean` se fera seulement avec l'outil `break`.
L'utilisation de l'outil `break` de `v.clean` dans ce cas précis sert à « nettoyer » les données en réalisant une opération topologique :

Que fait la fonction `break` ?

    - Cela découpe les lignes à leurs points d'intersection.
    - Cela crée de nouveaux nœuds aux endroits où les lignes se croisent.

On parle de nettoyage, car, initialement, les lignes de `base` et `line` se croisent sans être réellement connectées topologiquement. Le « nettoyage » consiste à établir une véritable connexion topologique à ces intersections.

Dans notre cas, en appliquant « break » après l'union des lignes, on force GRASS à reconnaître et à matérialiser les points d'intersection ; cela transforme de simples croisements géométriques en nœuds topologiques explicites.

Cela permet d'exploiter ensuite la structure topologique de GRASS pour identifier facilement ces points d'intersection.

Ainsi, nous allons passer de :

![GRASS line overlay](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/grass_line_overlay_points.svg){: .img-center loading=lazy }

à

![GRASS line overlay clean](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/grass_select_line_clean_points.svg){: .img-center loading=lazy }

Maintenant, on regarde si notre fonction v.select avec `intersects` fonctionne.

Hourra !

Quels sont les points ? Les mêmes que jusqu'à présent. Mais, alors, que s'est-il passé ? Eh bien, revenons sur QGIS et expliquons cela graphiquement.

### De la topologie dans QGIS

Dans QGIS, il existe un mode d'édition que j'affectionne particulièrement, qui est… l'édition topologique.

Le stockage dans QGIS est dit « spaghetti ». Les données sont toutes dans ce plat de pâtes : les entités géographiques sont stockées individuellement sans relations topologiques explicites.
Mais, bien que QGIS utilise un modèle de données de type « spaghetti », le logiciel propose des outils qui aident à maintenir la cohérence géométrique entre les couches.

En particulier, ici, nous allons utiliser la fonction d'édition topologique, qui, lors de chaque accrochage sur un segment, va ajouter des nœuds sur le segment accroché.

La couche `base_topology` est une copie de `base` sur laquelle j'ai dessiné, avec l'édition topologique, la couche `test_line`.

Si l'on refait notre test de « sélection par localisation » avec le prédicat « intersects », nous avons nos 34 lignes de sélectionnées.

Pour être certain que ce n'est pas juste des sommets qui seraient de l'autre côté de la ligne, on peut les extraire et refaire l'opération.

La topologie est grande, la topologie est bonne, elle va sauver nos calculs !

### Les limites de la topologie

Oui, la topologie c'est très bien, et son utilisation dans QGIS, via ses outils ou via GRASS, est très puissante. Mais, l'on peut faire quelques reproches :

- plus difficile à utiliser/à maintenir ;
- traitements plus longs lors d'intégrations de données externes, non topologiques ;
- nombre de sommets plus important ;
- modification de la donnée d'origine ;
— etc.

En particulier, j'expliquerai bientôt ce que j'indique par « modification de la donnée d'origine ».

Dans la première partie, j'ai écrit que la distance du point par rapport à la géométrie d'origine était proche de zéro, mais pas exactement 0.

Avec l'édition topologique de QGIS ou le stockage de GRASS, les points d'intersections coïncident avec les sommets de nos géométries, merci à la topologie.

Toutefois, en dehors des nœuds ajoutés, est-ce que notre géométrie est la même ? Visuellement, encore une fois, hormis les nœuds, cela semble identique.

Comparons les angles des segments.

Dans notre géométrie d'origine, nous avons quatre segments, avec comme azimut, en radians :

![QGIS segments azimuth](https://github.com/lbartoletti/lbartoletti.github.io/blob/master/assets/2024_intersection_intersects/data/processing/qgis_segments_azimuth.svg){: .img-center loading=lazy }

Soit, en partant du bas gauche et en tournant dans le sens horaire :

- 4.341309933406307
- 1.0434054052601267
- 2.401617769614756
- 5.848325554504713

Dans notre base qui a été éditée topologiquement ?

Sur le premier segment d'origine :

- 4.341309933414985
- 4.3413099333929175
- 4.341309933355925
- 4.341309933411935
- 4.34130993343072
- 4.341309933414806
- 4.341309933388343
- 4.341309933497785
- 4.341309933391953

Le deuxième :

- 5.848325554496416
- 5.848325554486275
- 5.8483255545512725
- 5.848325554512849
- 5.848325554487155
- 5.848325554478932
- 5.848325554530697
- 5.848325554523524
- 5.848325554479168

Le troisième :

- 1.0434054052235737
- 1.043405405251191
- 1.0434054052730521
- 1.0434054052793966
- 1.0434054052156936
- 1.0434054052777524
- 1.043405405257653
- 1.0434054052902961
- 1.0434054052482782

Le quatrième :

- 2.401617769621854
- 2.401617769590059
- 2.4016177695994174
- 2.4016177696075154
- 2.401617769638797
- 2.401617769583275
- 2.4016177696211147
- 2.401617769630777
- 2.4016177696067103
- 2.4016177696313

Les nouveaux segments ne sont pas « alignés » comme le segment d'origine. De rien du tout, en vrai, car si on convertit ces angles en degrés, on obtient 4 valeurs, identiques à nos segments d'origine :

- 335.084
- 59.783
- 137.603
- 248.739

En réalité, pas totalement, mais j'ai volontairement arrondi à trois chiffres après la virgule.
Pourquoi ai-je fait ça ? Marre de me trimbaler autant de chiffres.
Et, puis, est-ce vraiment utile d'avoir autant de chiffres après la virgule ? :wink:

## Approche Alternative : Exploration de méthodes alternatives telles que l'utilisation de SFCGAL pour des calculs plus robustes

Dans les parties précédentes, nous avons montré que le « intersects » d'une intersection, était faux, sauf avec la topologie ou la tolérance.

Nous allons maintenant utiliser une « approche alternative » dans les calculs. Promis, je garde le code pour une autre partie à la lecture optionnelle.

Pour cela, laissez-moi introduire SFCGAL.

> SFCGAL est une bibliothèque d'enveloppe C++ autour de [CGAL](https://www.cgal.org/) avec pour objectif de supporter l'ISO 19107:2013 et l'accès aux fonctions simples (Simple Features Access) 1.2 de l'OGC pour les opérations en 3D.
>
> SFCGAL fournit des types de géométries et des opérations conformes aux normes, qui peuvent être accédées via ses API C ou C++. PostGIS utilise l'API C pour exposer certaines fonctions de SFCGAL dans les bases de données spatiales (cf. manuel de PostGIS).
>
> Les coordonnées des géométries ont une représentation en nombre rationnel exact et peuvent être en 2D ou en 3D.

En gros, SFCGAL, fait la géométrie comme on connaît dans nos SIG, mais avec le moteur de CGAL et surtout des nombres « différents » : rationnel exact. L'explication plus détaillée sera donnée dans la partie algorithme et code, mais considérons que ce sont des fractions.

On utilisera SFCGAL de deux façons, pour comparer leurs résultats, avec Python et avec PostGIS.

### Python avec PySFCGAL

PySFCGAL est une interface Python pour la bibliothèque SFCGAL, en cours de développement et de packaging. À défaut d'avoir une application `sfcgalop` à la `geosop`  (au moment de la publication de l'article, celle-ci est en cours de développement) l'interface Python permet de faire des calculs plus facilement qu'en C ou C++. Promis, c'est « lisible » comme code.

Sur mon système FreeBSD, voici, comment je l'utilise pour notre test :

```python
# Import de la bibliothèque
from pysfcgal import sfcgal
# Lecture du wkb base
base = sfcgal.read_wkb('0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341')
# Lecture du wkb line
line = sfcgal.read_wkb('010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341')
```

Notre calcul d'intersection se fera simplement avec cette ligne :

```python
# Calcul de l'intersection
result = base.intersection(line)
# Affiche du WKT avec 10 décimales
print(result.wktDecim(10))
```

Le résultat `MULTIPOINT((1981583.62057374 5199333.30187807),(1981640.78490601 5199258.02208840))` est conforme à ce que nous avons jusqu'à présent `MULTIPOINT ((1981583.6205737416 5199333.301878075), (1981640.7849060092 5199258.022088398))`.

On note, une petite différence à partir du 10e chiffre. Cela se traduit dans le WKB qui, outre l'inversion des points, est légèrement différent.

```python
print(result.wkb)
```

`0104000000020000000101000000b6ebdd9e8f3c3e416af8515379d553410101000000a899efc8c83c3e4175e5698166d55341`

Et notre calcul d'intersects ?

```python
print(result.intersects(base))
print(result.intersects(line))
```

C'est un double `TRUE` !

- Tu as parlé de SFCGAL disponible dans PostGIS ?
- Oui, tu veux voir ce que cela va donner ?
- Bah… True !
- On va voir…

### PostGIS avec SFCGAL

Le principal consommateur de SFCGAL est PostGIS, il est notamment utilisé pour les calculs 3D et certaines opérations qui ne sont pas disponibles dans GEOS.
À l'heure où j'écris, la version 3.5 de PostGIS n'est pas encore sortie. Cependant, elle contient tous les algorithmes de SFCGAL, y compris ceux pouvant faire « doublons » avec GEOS.
Vous connaissez vos fonctions `ST_` de PostGIS, vous remplacez le préfixe par `CG_` et vous aurez les fonctions SFCGAL.

Comme il s'agit d'une extension, il faudra l'activer avec la commande SQL `CREATE EXTENSION postgis_sfcgal CASCADE;`

Si l'on reprend notre requête PostGIS, pour SFCGAL, cela ressemble à ça :

```sql
WITH
base AS (
    SELECT ST_GeomFromWKB(decode('0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341', 'hex'), 3946) AS geom
),
line AS (
    SELECT ST_GeomFromWKB(decode('010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341', 'hex'), 3946) AS geom
)
SELECT
    CG_Intersects(base.geom, CG_Intersection(base.geom,line.geom)), CG_Intersects(line.geom, CG_Intersection(base.geom,line.geom)),
    CG_Distance(base.geom, CG_Intersection(base.geom,line.geom)), CG_Distance(line.geom, CG_Intersection(base.geom,line.geom))
FROM base, line
```

Le résultat tant attendu :

| cg_intersects | cg_intersects |      cg_distance       |     cg_distance      |
|---------------|---------------|------------------------|----------------------|
|  f            | f             | 3.0508500689910857e-10 | 1.72344247851053e-10 |

Comment ça, « faux » ? C'était vrai avec Python.

En effet, mais il faut comprendre que, lorsque l'on réalise cette requête, plusieurs conversions s'effectuent.

Si vous vous souvenez, plus haut, j'ai indiqué que SFCGAL utilisait « d'autres nombres », des sortes de fractions. En vrai, sa représentation interne ressemble à ça :

```python
print(result.wkt)
```

On obtient un "WKT" mais avec des fractions :

`MULTIPOINT((39835383350819973229271557358571370825/20102802090827818983138002993152 26130292092976317370966223130398592513/5025700522706954745784500748288),(4210607705173521426482690542319302151/2124808763144847138096555229184 2761857251796143622778067803204906245/531202190786211784524138807296))`

Le passage de la fraction au nombre à virgule « double » va faire une légère approximation. De fait, on ne va pas retomber sur nos ~~pattes~~ bits, d'où ce comportement.

Pour les plus curieux, la partie « algorithme » contiendra un exemple en Python SFCGAL et d'autres exemples en PostGIS SFCGAL.

Ce qu'il faut comprendre, c'est que SFCGAL peut donner le résultat correct, à condition de rester dans son modèle de représentation des nombres ou d'avoir des nombres qui sont finis ou dans la plage de valeur des doubles.

Il existerait une façon de rendre le calcul correct dans PostGIS avec SFCGAL, mais ce n'est pas encore implémenté.

## Et chez la concurrence, ça se passe comment ?

On ne va pas tous les faire, mais seulement deux un peu connus et installés parfois à côté de QGIS :wink:

Le premier sera FME, une sorte de boîte à outils de QGIS et l'autre ArcGis Pro, le concurrent payant de GRASS/QGIS.

### FME

![logo FME](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/FME.png){: .img-thumbnail-left }

Pour FME, pas de blabla. J'insère les WKB, je fais une test d'intersection et je regarde si les points intersectent `line` et `base`.

Vous pouvez trouver le fichier [fmw sur mon github](https://github.com/lbartoletti/lbartoletti.github.io/blob/master/assets/2024_intersection_intersects/data/fme_test_intersects.fmw)

Et le résultat :

![FME test intersects](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/fme_test_intersects.png){: .img-center loading=lazy }

KO !

FME utilise, et contribue, aux outils open source. Néanmoins, même si le résultat est le même qu'avec GEOS, ce n'est pas cette bibliothèque qui est utilisée, mais une de leur conception. Encore une fois, le problème n'est donc pas GEOS.

### ESRI ArcGis Pro

![logo ArcGis Pro](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/arcgis_pro.png){: .img-thumbnail-left }

Comme pour QGIS, nous allons tester notre problème de deux façons : par les traitements via une couche SIG et directement avec le WKB.

#### Utilisation du ShapeFile

Sauf erreur de ma part, ArcGis ne sait pas ouvrir les fichiers GeoPackage. Qu'importe, nous utiliserons le bon vieux ShapeFile qui sera importé dans une GeoDatabase.

Afin de réaliser le calcul de l'intersection, nous utilisons l'outil [Pairwise Intersect](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/pairwise-intersect.htm).

Contrairement à ce que j'ai pu faire pour QGIS, je ne montre pas les formulaires graphiques, mais le code qu'exécute ArcGis.

En entrée `in_features`, on donne nos deux couches `line` et `base`. On sait que l'on va avoir des points, donc on déclare le type de sortie comme `POINT`.

```python
arcpy.analysis.PairwiseIntersect(
    in_features="line;base",
    out_feature_class=r"C:\Users\xxx\AppData\Local\Temp\ArcGISProTemp37912\Sans titre\Default.gdb\line_PairwiseIntersect",
    join_attributes="ALL",
    cluster_tolerance=None,
    output_type="POINT"
)
```

Je passe les étapes pour l'extraction du WKB et WKT, dont voici les résultats :

- `0104000000020000000101000000e034efc8c83c3e4120166a8166d55341010100000040a4df9e8f3c3e416054525379d55341`
- `MultiPoint ((1981640.78490000218153 5199258.02210000157356262),(1981583.62060000002384186 5199333.30189999938011169))`

ArcGis nous sort un résultat légèrement différent. Testons avec l'autre outil pour les intersections : [Intersect](https://pro.arcgis.com/en/pro-app/latest/tool-reference/analysis/intersect.htm)

```python
arcpy.analysis.Intersect(
    in_features="line #;base #",
    out_feature_class=r"C:\Users\xxx\AppData\Local\Temp\ArcGISProTemp37912\Sans titre\Default.gdb\line_Intersect1",
    join_attributes="ALL",
    cluster_tolerance=None,
    output_type="POINT"
)
```

- `01040000000200000001010000008016d99e8f3c3e416054525379d553410101000000e034efc8c83c3e4120166a8166d55341`
- `MultiPoint ((1981583.62049999833106995 5199333.30189999938011169),(1981640.78490000218153 5199258.02210000157356262))`

Un résultat également légèrement différent, mais proche de celui que nous obtenons avec les autres SIG.
Que se passe-t-il ici ?

ArcGis utilise, pour tous les calculs, une notion que l'on retrouve parfois dans les SIG OpenSource, celui de résolution et tolérance.
On peut la modifier en passant en paramètres des valeurs XY. Voici les requêtes et les résultats avec une valeur de 0.00001 mm.

```python
with arcpy.EnvManager(XYResolution="0.00001 Millimeters", XYTolerance="0.00001 Millimeters"):
    arcpy.analysis.PairwiseIntersect(
        in_features="line;base",
        out_feature_class=r"C:\Users\xxx\AppData\Local\Temp\ArcGISProTemp37912\Sans titre\Default.gdb\line_PairwiseIntersect1",
        join_attributes="ALL",
        cluster_tolerance=None,
        output_type="POINT"
    )
```

- `MultiPoint ((1981640.78490600734949112 5199258.02208840474486351),(1981583.6205737441778183 5199333.30187807604670525))`
- `0104000000020000000101000000a099efc8c83c3e417ce5698166d553410101000000c0ebdd9e8f3c3e416cf8515379d55341`

Ah, on retrouve nos petits ! Du moins, l'écart a été réduit.

L'équivalent de notre sélection par localisation se fait comme suit :

```python
arcpy.management.SelectLayerByLocation(
    in_layer="line_PairwiseIntersect1;pariwiseIntersect_tolerance;lineIntersect",
    overlap_type="INTERSECT",
    select_features="line",
    search_distance=None,
    selection_type="NEW_SELECTION",
    invert_spatial_relationship="NOT_INVERT"
)
```

Avec une distance de recherche (tolérance)

```python
arcpy.management.SelectLayerByLocation(
    in_layer="line_PairwiseIntersect1;pariwiseIntersect_tolerance;lineIntersect",
    overlap_type="INTERSECT",
    select_features="line",
    search_distance="0.000000001 Millimeters",
    selection_type="NEW_SELECTION",
    invert_spatial_relationship="NOT_INVERT"
)
```

Dans les deux cas, ArcGis sélectionne les points d'intersection. C'est donc un bon point pour eux.

#### Via le WKB et ArcPy

Dans la partie suivante, nous allons regarder comment cela se passe, en utilisant directement les fonctions de base.

```python
import binascii
# on importe le WKB de base
base = arcpy.FromWKB(binascii.unhexlify('0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341'))
# on importe le WKB de line
line = arcpy.FromWKB(binascii.unhexlify('010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341'))
# calcul du point d'intersection en WKT
base.intersect(line, 1).WKT
# 'MULTIPOINT ((1981583.6207275391 5199333.3018798828), (1981640.7850952148 5199258.0220947266))'
# en WKB
base.intersect(line, 1).WKB
# bytearray(b'\x01\x04\x00\x00\x00\x02\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\xe8\x9e\x8f<>A\x00\x00RSy\xd5SA\x01\x01\x00\x00\x00\x00\x00\xfc\xc8\xc8<>A\x00\x00j\x81f\xd5SA')
# avec la conversion pour l'afficher en hexa
binascii.hexlify(base.intersect(line, 1).WKB)
# b'01040000000200000001010000000000e89e8f3c3e410000525379d5534101010000000000fcc8c83c3e4100006a8166d55341'
```

Maintenant, regardons les relations spatiales entre notre résultat `result` et les [géométries](https://pro.arcgis.com/en/pro-app/latest/arcpy/classes/geometry.htm) `base` et `line`.
On utilisera : disjoint, contains, crosses, equals, overlaps, touches et whitin ; ce dernier étant notre intersects.

Base :

```python
result.disjoint(base)
# False
```

```python
result.contains(base), result.crosses(base), result.equals(base), result.overlaps(base), result.touches(base), result.within(base)
# (False, False, False, False, False, True)
```

Line :

```python
result.disjoint(line)
# False
```

```python
result.contains(line), result.crosses(line), result.equals(line), result.overlaps(line), result.touches(line), result.within(line)
# (False, False, False, False, False, True)
```

On obtient bien le résultat souhaité. En fait, vous l'aurez peut-être compris en filigrane, ArcGis ne propose pas un calcul "strict" comme les autres, mais bien quelque chose de particulier. Il est "tolérant".

## Algorithmes et Code : comment cela fonctionne-t-il ?

![logo console terminal](https://cdn.geotribu.fr/img/logos-icones/divers/ligne_commande.png){: .img-thumbnail-left }

Disclaimer : Cet article s'adresse à tous les géomaticiens, quel que soit leur niveau de compétence. Cependant, ceux qui sont déjà familiers avec les erreurs comme 0.1 + 0.2 != 0.3 ne trouveront peut-être pas de nouvelles informations ici. Encore une fois, j'essaie de vulgariser. Si une version plus détaillée vous intéresse, je peux essayer d'en faire une.

Ceci dit, comment qu'on calcule si un point C est sur un segment AB ? On calcule l'aire du triangle ABC !

Dit autrement, avec un peu plus de formalisme, pour déterminer si un point \( C \) est sur une droite définie par deux points \( A \) et \( B \), on peut utiliser la géométrie vectorielle. Voici une méthode simple pour le faire :

1. **Coordonnées des points** : Supposons que les coordonnées des points \( A \), \( B \) et \( C \) soient respectivement \( (x_A, y_A) \), \( (x_B, y_B) \) et \( (x_C, y_C) \).

2. **Vecteur AB et AC** : Calculons les vecteurs \( $\overrightarrow{AB}$ \) et \( $\overrightarrow{AC}$ \) :
   - \( $\overrightarrow{AB}$ = (x_B - x_A, y_B - y_A) \)
   - \( $\overrightarrow{AC}$ = (x_C - x_A, y_C - y_A) \)

3. **Déterminant** : Calculons le déterminant des vecteurs \( $\overrightarrow{AB}$ \) et \( $\overrightarrow{AC}$ \). Ce déterminant est donné par :
   \[
   $\text{D}$ = (x_B - x_A) $\cdot$ (y_C - y_A) - (y_B - y_A) $\cdot$ (x_C - x_A)
   \]

4. **Vérification** :
   - Si \( $\text{D}$ = 0 \), alors les points \( A \), \( B \) et \( C \) sont colinéaires, ce qui signifie que \( C \) est sur la droite \( AB \).
   - Si \( $\text{D} \neq 0$ \), alors \( C \) n'est pas sur la droite \( AB \).

### Exemple

Supposons que les coordonnées soient :

- \( A = (1, 2) \)
- \( B = (4, 6) \)
- \( C = (2, 3) \)

Calculons les vecteurs :

- \( $\overrightarrow{AB}$ = (4 - 1, 6 - 2) = (3, 4) \)
- \( $\overrightarrow{AC}$ = (2 - 1, 3 - 2) = (1, 1) \)

Calculons le déterminant :
\[
$\text{D} = 3 \cdot 1 - 4 \cdot 1 = 3 - 4 = -1$
\]

Puisque $\text{D} \neq 0$, le point \( C \) n'est pas sur la droite \( AB \).

Voici une implémentation simple en Python :

```python
def orient2d(x_a, y_a, x_b, y_b, x_c, y_c):
    """
    Calcule le double de l'aire du triangle formé par les points a, b et c.
    Si le résultat est positif, les points sont orientés dans le sens antihoraire.
    Si le résultat est négatif, les points sont orientés dans le sens horaire.
    Si le résultat est nul, les points sont alignés.
    """
    return (x_b - x_a) * (y_c - y_a) - (y_b - y_a) * (x_c - x_a)

def shoelace_area(x_a, y_a, x_b, y_b, x_c, y_c):
    # Calcul de l'aire en utilisant la formule de la shoelace
    area = 0.5 * (x_a * (y_b - y_c) + x_b * (y_c - y_a) + x_c * (y_a - y_b))
    return area

# Exemple d'utilisation
x_a, y_a = 1, 2
x_b, y_b = 4, 6
x_c, y_c = 2, 3

area = shoelace_area(x_a, y_a, x_b, y_b, x_c, y_c)
orient = orient2d(x_a, y_a, x_b, y_b, x_c, y_c)
print(f"L'aire du triangle est : {area}")
print(f"L'orientation du triangle ABC est : {orient}")
```

Le code retourne un nombre négatif ; l'aire étant la moitié de l'orientation.

Si l'on inverse A et B, comme suit,

```python
area = shoelace_area(x_b, y_b, x_a, y_a, x_c, y_c)
orient = orient2d(x_b, y_b, x_a, y_a, x_c, y_c)
print(f"L'aire du triangle est : {area}")
print(f"L'orientation du triangle BAC est : {orient}")
```

On retrouve un nombre positif. Le point C est de l'autre côté de l'axe AB, dit autrement, AB et C ne sont pas collinéaires.

```python title="Exemple d'utilisation avec des points colinéaires"
x_a, y_a = 1, 1
x_b, y_b = 2, 2
x_c, y_c = 3, 3

area = shoelace_area(x_b, y_b, x_a, y_a, x_c, y_c)
orient = orient2d(x_b, y_b, x_a, y_a, x_c, y_c)
print(f"L'aire du triangle est : {area}")
print(f"L'orientation du triangle BAC est : {orient}")
```

```python title="Exemple d'utilisation avec des points colinéaires"
x_a, y_a = 0.1, 0.1
x_b, y_b = 0.2, 0.2
x_c, y_c = 0.3, 0.3

area = shoelace_area(x_b, y_b, x_a, y_a, x_c, y_c)
orient = orient2d(x_b, y_b, x_a, y_a, x_c, y_c)
print(f"L'aire du triangle est : {area}")
print(f"L'orientation du triangle BAC est : {orient}")
```

Ici, vous devriez avoir une « blague ». L'aire n'est pas exactement égale à 0, mais proche de 0.

Quelles sont donc les problèmes de cette « blague » ?

### L'utilisation des nombres flottants

Si l'on admet que C est le point d'intersection d'un segment avec AB, alors, en théorie, les lignes se croisent en un point bien défini : C. Cependant, en pratique, les ordinateurs effectuent des calculs en utilisant une représentation numérique finie qui peut introduire de petites erreurs. Voici pourquoi cela se produit :

Les ordinateurs utilisent majoritairement une représentation en [virgule flottante](https://fr.wikipedia.org/wiki/Virgule_flottante) pour stocker des nombres réels. C'est même la norme pour les coordonnées de nos géométries. Ce fameux double que l'on retrouve de partout. Toutefois son utilisation peut introduire des erreurs d'arrondi. J'ai indiqué une opération en introduction, 0.1 + 0.2 != 0.3. Comme 0.3 ne peut pas être représenté exactement cela conduit à des approximations. C'est un problème connu des informaticiens, au point d'avoir [son propre site](https://0.30000000000000004.com/).
De même, je ne peux qu'encourager la lecture de l'article [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html).

Il existe d'autres nombres sur des ordinateurs. Vous avez pu voir que 1 + 2 est bien égal à 3. Tandis que 0.1 + 0.2 n'est pas égal à 0.3.

Les opérations sur les entiers sont toujours justes, dans leurs limites. Alors pourquoi ne pas utiliser que des entiers ?

C'est plus ou moins ce qui est fait par d'autres bibliothèques de calculs. On pensera notamment à SFCGAL, mais comme on l'a vu, cela ne fait pas tout. L'enregistrement se faisant en double, la conversion va introduire des erreurs ; on détaillera cela plus bas.

### L'accumulation d'erreurs

Lors de calculs complexes, ces petites erreurs d'arrondi peuvent s'accumuler et devenir significatives.

Lors du calcul de l'intersection de deux lignes, plusieurs opérations arithmétiques sont nécessaires. Chaque opération peut introduire une petite erreur.

Des solutions comme GEOS ou Clipper (pour SAGA), repose sur des calculs bien plus robustes que notre exemple ; d'ailleurs, elles passent également par des entiers. Le calcul de l'intersection va être juste - à la précision du float.

### Comparaisons de précision

En réalité, ce qu'il manque dans nos SIG, c'est de la tolérance.

Lorsqu'on vérifie si un point est sur une ligne, la précision des calculs peut affecter le résultat.

Une des règles lorsque l'on utilise des nombres à virgule est de calculer suivant une valeur. On ne doit jamais comparer directement un nombre flottant. C'est à dire, éviter :

```python
0.1 + 0.2 == 0.3
```

mais plutôt utiliser des fonctions réalisant une comparaison approchée comme :

```python
def compare_doubles(a, b, tolerance=1e-9):
    """
    Compare deux nombres à virgule flottante avec une tolérance donnée.

    :param a: Premier nombre à comparer
    :param b: Deuxième nombre à comparer
    :param tolerance: Tolérance pour la comparaison (par défaut 1e-9)
    :return: True si les nombres sont égaux dans la tolérance, False sinon
    """
    return abs(a - b) <= tolerance

# Exemple d'utilisation
a = 0.1 + 0.2
b = 0.3
tolerance = 1e-9

if compare_doubles(a, b, tolerance):
    print(f"Les nombres {a} et {b} sont égaux avec une tolérance de {tolerance}.")
else:
    print(f"Les nombres {a} et {b} ne sont pas égaux avec une tolérance de {tolerance}.")
```

Vous devriez avoir cette sortie :

`Les nombres 0.30000000000000004 et 0.3 sont égaux avec une tolérance de 1e-09.`

Pour une étude plus approfondie, je vous encourage à lire l'article [Comparing Two Floating-Point Numbers
](https://embeddeduse.com/2019/08/26/qt-compare-two-floats/).

Comme vous avez pu le deviner, c'est ce que fait ArcGIS.
Dans plusieurs endroits de nos SIG, il existe des comparaisons floues, peut-être que les prochaines versions de GEOS intègreront cette tolérance pour les relations. :wink:

### Retour sur SFCGAL

On a vu que SFCGAL est la seule bibliothèque à donner le bon résultat pour intersects, mais seulement en python. Avec PostGIS, il retourne faux comme GEOS, pourquoi ?

SFCGAL, n'utilise pas les flottants, mais une autre arithmétique. Pour rappel, notre code exemple est :

```python
from pysfcgal import sfcgal
base = sfcgal.read_wkb('0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341')
line = sfcgal.read_wkb('010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341')
result = base.intersection(line)
# Affiche du WKT avec 10 décimales
print(result.wktDecim(10))
print(base.intersects(result))
print(line.intersects(result))
```

On a le résutat souhaité. Maintenant, essayons de reproduire ce qu'il se passe dans PostGIS.
Dans notre requête, on calcule le point d'intersection avec CG_Intersection. A la fin de son traitement, elle va convertir sa géométrie, et ses nombres, en [double PostGIS](https://github.com/postgis/postgis/blob/d29ba84cb05988ab0aa1b2da3eef90108dfae1db/sfcgal/lwgeom_sfcgal.c#L559). Cette étape est la cause du problème. Cette conversion revient à cela en Python :

```python
# Création d'un point np en passant par des floats
p = sfcgal.lib.sfcgal_geometry_collection_geometry_n(result._geom, 0)
# conversion du nombre gmp en double
x = sfcgal.lib.sfcgal_point_x(p)
y = sfcgal.lib.sfcgal_point_y(p)
# création du point avec ces doubles
np = sfcgal.Point(x, y)
print(base.intersects(np))
print(line.intersects(np))
```

Et, voilà, « l'imprécision » des doubles nous donne ce mauvais résultat.

Une solution, qui n'est pas élégante et donc pas encore implémentée, serait d'avoir des fonctions qui s'enchaînent et ne fassent pas continuellement des va-et-vient entre les nombres. Avec une fonction CG_IntersectsIntersection comme suit, le résultat dans PostGIS sera juste.

```c
PG_FUNCTION_INFO_V1(sfcgal_intersects_intersection);
Datum
sfcgal_intersects_intersection(PG_FUNCTION_ARGS)
{
       GSERIALIZED *input0, *input1;
       GSERIALIZED *output;
       LWGEOM *lwgeom;
       bool intersect1, intersect2;
       char *values[3];

       sfcgal_geometry_t *geom0, *geom1;
       sfcgal_geometry_t *sfcgal_result;
       srid_t srid;

       sfcgal_postgis_init();

       input0 = PG_GETARG_GSERIALIZED_P(0);
       srid = gserialized_get_srid(input0);
       input1 = PG_GETARG_GSERIALIZED_P(1);
       geom0 = POSTGIS2SFCGALGeometry(input0);
       PG_FREE_IF_COPY(input0, 0);
       geom1 = POSTGIS2SFCGALGeometry(input1);
       PG_FREE_IF_COPY(input1, 1);

       sfcgal_result = sfcgal_geometry_intersection(geom0, geom1);
       output = SFCGALGeometry2POSTGIS(sfcgal_result, 0, srid);
       lwgeom = lwgeom_from_gserialized(output);
       intersect1 = sfcgal_geometry_intersects(geom0, sfcgal_result);
       intersect2 = sfcgal_geometry_intersects(geom1, sfcgal_result);
       values[0] = intersect1 ? "t" : "f";
       values[1] = intersect2 ? "t" : "f";
       values[2] = lwgeom_to_hexwkb_buffer(lwgeom, WKB_EXTENDED);
       lwpgnotice(
           "%s %s %s",
           values[0], values[1], values[2]);

       sfcgal_geometry_delete(geom0);
       sfcgal_geometry_delete(geom1);

       sfcgal_geometry_delete(sfcgal_result);

       PG_RETURN_POINTER(intersect1 && intersect2);
}
```

Plus généralement, vous pouvez exécuter ce [mini script python](https://github.com/lbartoletti/lbartoletti.github.io/blob/master/assets/2024_intersection_intersects/data/intersects_intersection_numbers.py) qui résume ce que l'on a vu.

Il réalise notre calcul d'intersects/intersection sur 2 segments en utilisant des nombres floats, Decimal et Fraction de Python.

### Webographie

En plus des liens vers les documentations que j'ai indiquées par moments, voici quelques liens permettant de compléter ou d'approfondir le sujet.

Tout d'abord, rendons à César ce qui est à César, cette suite d'articles, n'est qu'une explication illustrée de la [FAQ](https://locationtech.github.io/jts/jts-faq.html) de JTS ; qui est à l'origine de GEOS. Mais, comme personne ne lit la documentation :wink: autant remettre le lien [ici](https://locationtech.github.io/jts/jts-faq.html#D8).

Sur la robustesse de l'intersection des segments, vous pouvez commencer par cet échange [stack](https://cs.stackexchange.com/questions/119760/robust-two-lines-segments-intersection-point-in-2d) et ensuite lire et utiliser le code de Shewchuk sur la robustesse des calculs avec des nombres flottants :

- <https://people.eecs.berkeley.edu/~jrs/meshpapers/robnotes.pdf>
- <https://www.cs.cmu.edu/~quake/robust.html>
- <https://www.cs.cmu.edu/afs/cs/project/quake/public/code/predicates.c>

Des versions modernes ont été reprises comme <https://github.com/mourner/robust-predicates> qui a également fait un article complet sur ce concept.

JTS/GEOS utilise une version modifiée de ces calculs. Afin de ne pas allonger un article déjà bien long. Je n'ai pas montré d'exemple avec ces fonctions, mais le résultat est le même.

Dans nos SIG, voici quelques liens vers les codes sources utilisés :

QGIS

- Les fonctions sur les calculs géométriques de [QGIS](https://github.com/qgis/QGIS/blob/0c41c22343ded7c6b6a7be0d382477128e837bd9/src/core/geometry/qgsgeometryutils_base.cpp)

Grass

Le manuel de [v.clean](https://grass.osgeo.org/grass83/manuals/v.clean.html) qui utilise une fonction `split` qui va découper  le segment avec une [distance](https://github.com/OSGeo/grass/blob/9cb4745b6c4abfeaf542ef05468060d68af72703/vector/v.clean/split.c). Pour être exhaustif, j'aurais pu indiquer que ce traitement peut légèrement modifier les géométries.

SAGA

- Le calcul de [l'intersection](https://github.com/saga-gis/saga-gis/blob/0e66e5a768d771052553f270c0ffe24efda1d0a8/saga-gis/src/saga_core/saga_api/geo_functions.cpp#L280)
- La fonction [line crossings](https://github.com/saga-gis/saga-gis/blob/0e66e5a768d771052553f270c0ffe24efda1d0a8/saga-gis/src/tools/shapes/shapes_lines/line_crossings.cpp#L226)
- et la bibliothèque [Clipper2](https://github.com/AngusJohnson/Clipper2) qui est utilisée par SAGA.

Enfin, GEOS :

- Le test d'[intersects](https://github.com/libgeos/geos/blob/a8d2ed0aba46f88f9b8987526e68eea6565d16ae/src/algorithm/LineIntersector.cpp#L222)
- Le calcul [orient2d](https://github.com/libgeos/geos/blob/a8d2ed0aba46f88f9b8987526e68eea6565d16ae/src/algorithm/CGAlgorithmsDD.cpp#L54) où l'on aperçoit un premier test rapide et si la robustesse n'est pas assez bonne, on passe sur une autre [arithmétique](https://github.com/libgeos/geos/blob/a8d2ed0aba46f88f9b8987526e68eea6565d16ae/include/geos/math/DD.h).

## Comment arrêter de trop penser et vivre une vie meilleure !

![Globe cerveau](https://cdn.geotribu.fr/img/internal/icons-rdp-news/mentale.png){: .img-thumbnail-left }

On a souvent ces interrogations sur les « irrégularités » rencontrées lors des opérations courantes dans les SIG : pourquoi les accrochages dans QGIS ne se positionnent-ils pas toujours exactement sur la géométrie ? Pourquoi les calculs de superposition manquent-ils de précision ? Et pourquoi les résultats peuvent-ils être incohérents ?

Plutôt que de se perdre dans une quête de surprécision, voici quelques conseils pour améliorer votre expérience SIG et vivre une vie meilleure :

Derrière cette expression « incitaclic », voici en réalité quelques conseils ou expériences que j'ai pu rencontrer sur différents projets.

### Arrêtez de chercher la surprécision

_La rigueur à tout prix peut devenir une source de frustration. Acceptez qu’une légère imprécision est inévitable et concentrez-vous sur l’essentiel._

On est dans un monde infini, mais avec des ressources finies. Quelques arrondis ne font pas de mal. De combien de chiffres après la virgule avez-vous réellement besoin ? Votre précision c'est le décimètre, le centimètre, le millimètre, au-delà  ? Vous avez besoin de combien de chiffres pour [Pi](https://www.jpl.nasa.gov/edu/news/2016/3/16/how-many-decimals-of-pi-do-we-really-need/). Combien d'approximations réalisez-vous au quotidien, tout en étant précis ? Il est actuellement 21 h 02 ou simplement 21 h ? Quand vous réalisez un trajet de chez vous aux rencontres QGIS, vous êtes précis à la seconde, à la minute, au quart d'heure ? Bref, la précision dépend de votre contexte et il y a fort à parier que vous allez rarement être en dessous de 10^-3 sur du cartésien et 10^-8 en géodésique.

![xkcd 2170 - Credits : Randall Monroe](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/xkcd_coordinate_precision.webp){: .img-center loading=lazy }

### Gérez la tolérance

_Utilisez des tolérances appropriées dans vos calculs pour minimiser les effets des erreurs d'arrondi. Définissez des tolérances adaptées à l’échelle et aux objectifs de votre projet._

En lien avec le nombre de chiffres après la virgule, vous pouvez également ajouter une tolérance. En France, les gestionnaires de réseaux savent qu'on les caractérise suivant 3 classes : A, B ou C. 10 cm, 40 cm, etc. Une bonne pratique est de se demander si le point n'est pas à une distance d'environ X cm. Sur PostGIS, cela va se caractériser par l'utilisation de `ST_DWithin` plutôt qu'un `ST_Intersects`.

### Utilisez la topologie

_La topologie permet de gérer les relations spatiales et de corriger les erreurs géométriques. Les outils topologiques garantissent que les entités spatiales respectent certaines règles, améliorant ainsi la cohérence des données._

Si vraiment, vous souhaitez que les nœuds soient identiques, la topologie est là pour vous. Mais, attention, vous avez vu, cela transforme légèrement la donnée en entrée. Par ailleurs, suivant les outils que vous utilisez, elle peut ne pas être respectée lors d'éditions dans d'autres outils que ceux sur lesquels vous allez travailler. D'où l'idée de déporter l'intelligence en base : Thick database (base épaisse).

### Connaissez les autres nombres

_Comprenez comment les nombres sont représentés dans les ordinateurs. Cela aide à anticiper et à gérer les erreurs de calcul, notamment les différences entre les nombres en virgule flottante et les autres._

Tout est de la faute des nombres en virgule flottante ! Vous pouvez utiliser d'autres outils, mais attention, la conversion peut engendrer des erreurs.

### Investissez dans l'évolution des outils

_Soutenez le développement et l'amélioration des outils SIG, surtout les projets open source comme ceux de l'OSGeo !_

On ne le dira jamais assez, mais si un fonctionnement ou un bug vous dérange. Financez-nous ! On se fera un plaisir d'y répondre. Ça vaut également pour les demandes de fonctionnalités.

### Conclusion

_La quête de la perfection numérique dans les SIG peut être frustrante. En adoptant une approche pragmatique et en comprenant les limites des calculs numériques, vous pouvez réduire le stress et améliorer votre efficacité. En acceptant ces réalités, vous pourrez arrêter de trop penser et commencer à vivre une vie meilleure, plus sereine et productive dans vos projets géospatiaux._

C'est beau, hein ?

En réalité, vivez vos SIG comme vous le voulez, mais ayez connaissance de leurs fonctionnements. Oui, leurs, car chacun peut vous donner des résultats plus ou moins différents.

J'espère que cette série d'articles vous a intéressé. D'autres sur la comparaison entre les outils devraient venir.

Et pour finir, merci à mes relecteurs de GeoTribu, à Sandro Santilli (correction d'une erreur dans un code), Martin Davis aka Dr. Jts (pour ses apports sur les « concurrents ») et tout ce qu'il a pu faire pour nos outils ! Et, enfin, merci à Julien Moura qui a su être patient avant de voir la première phrase :D

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
