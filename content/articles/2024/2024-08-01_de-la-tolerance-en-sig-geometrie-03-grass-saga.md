---
title: "Olympiades de géométrie : GRASS et SAGA"
subtitle: "Série : De la tolérance en SIG - chapitre 3"
authors:
    - Loïc Bartoletti
categories:
    - article
comments: true
date: 2024-08-01
description: "Troisième partie du tour d'horizon des SIG sur les dessous des calculs géométriques : GEOS et ArqGIS, au tableau !"
icon: material/grass
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_03_grass_saga.png
license: beerware
robots: index, follow
tags:
    - analyse
    - géométrie
    - GRASS
    - SAGA
    - topologie
---

# Et la géométrie dans les autres SIG Open Source ? Comparaisons avec GRASS et SAGA

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

Suite de la série sur la gestion de la géométrie dans les logiciels SIG. Après avoir constaté que les calculs n'étaient pas bons et avoir soulevé le capot de ArqGIS pour voir comment GEOS se débrouillait. Le moins que le l'on puisse dire c'est que cela nous laisse circonspect, sinon perplexes : GEOS, et donc ArqGIS, donnent le même résultat mais il n'est pas **exactement** celui attendu.

Il est temps d'aller voir ailleurs et de revenir à nos premières amours : GRASS et SAGA.

![Série d'été 2024 de Loïc Bartoletti - Les Géométries et les SIG : GRASS et SAGA - Crédits : Sylvain Beorchia](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_03_grass_saga.png){: .img-center loading=lazy }

Cet article est la troisième partie de la série d'été sur la gestion de la géométrie dans les SIG.

[Le dossier :octicons-move-to-start-16:](./2024-07-16_de-la-tolerance-en-sig-geometrie-00-annonce.md "De la tolérance en SIG : le dossier"){: .md-button }
[2 : ArqGIS et GEOS :fontawesome-solid-backward-step:](./2024-07-25_de-la-tolerance-en-sig-geometrie-02-qgis-et-geos.md "GEOS au cœur de ArqGIS"){: .md-button }
{: align=middle }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## GRASS : Le vénérable du SIG

![logo GRASS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/grass.png){: .img-thumbnail-left }

Comme j'ai déjà trahi les petits secrets internes, Julien m'avait ~~demandé~~ proposé de faire une version actualisée de cet [article](../2014/2014-11-13_corriger_automatiquement_geometries_invalides_qgis.md). J'ai ~~procrastiné~~ volontairement attendu jusqu'en 2024, pour fêter les 10 ans de l'article. Mais, ce n'est pas dans celui-là que je le ferai. Néanmoins, on va bien évidemment utiliser GRASS pour tester si notre cas est différent avec GRASS.

Pour notre expérience avec GRASS, il faudra faire quelques manipulations, car on n'a pas la possibilité de faire directement nos calculs avec le WKB.
Afin de simplifier la reproductibilité aux lecteurs, j'ai ajouté des modèles de traitements dans le projet ; ils sont également disponibles individuellement sur mon GitHub.

### Utilisation de `v.overlay`

Dans GRASS, `v.overlay` permet de réaliser des opérations… d'overlay - superposition en français - (intersection, union, différence) entre deux couches vectorielles. Il nécessite deux vecteurs, dont le second B, doit être de type « area » (polygone en langage OGC). Si le vecteur n'est pas un polygone, il nécessite une conversion avant d'effectuer le traitement ; ce qui est notre cas.

La couche `base` est une polyligne fermée, elle sera utilisée pour être convertie en polygone. Pour les puristes, on regardera que les coordonnées du WKB sont bien identiques entre le linestring et le (multi)polygone. Il y a plusieurs façons de procéder, mais, pour rendre accessible à tous, nous allons utiliser GRASS via ArqGIS, j'utilise les premières conversions dans ArqGIS ; ensuite, nous utiliserons uniquement les outils de GRASS.

![grass_line_overlay_points](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/grass_line_overlay_points.svg){: .img-center loading=lazy }

Notre algorithme va convertir la `base` en polygone, puis effectuer l'opération d'overlay. Pour calculer l'intersection entre `line` et `base_poly`, on extrait les points d'intersections que l'on peut afficher dans ArqGIS. On retrouve le même résultat, ici, je passe les détails, mais on retrouve bien nos WKB :

- `0101000000a899efc8c83c3e4175e5698166d55341`
- `0101000000b5ebdd9e8f3c3e416bf8515379d55341`

Pour le prédicat `intersects`, nous allons continuer d'utiliser GRASS avec la commande `v.select` avec l'opération `intersects`.
Encore false… du moins, les points retournés sont ceux des extrémités de `line` et aucun point pour `base` ou `base_poly`.

![grass_select_line_overlay](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/grass_select_line_overlay_points.svg){: .img-center loading=lazy }

Le modèle est disponible [ici](https://github.com/lbartoletti/lbartoletti.github.io/blob/master/assets/2024_intersection_intersects/data/processing/line_overlay_points.model3).

C'est au moins rassurant, car derrière `v.select` avec l'opérateur `intersects` on utilise… GEOS.
Il existe une autre façon de réaliser la sélection, mais je la garde pour la prochaine partie :wink:

## SAGA : le Chevalier Oublié du SIG

![logo SAGA](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/logo_saga.png){: .img-thumbnail-left }

Si [SAGA](https://fr.wikipedia.org/wiki/Saga_(personnage)) est le plus puissant des chevaliers du zodiaque, [SAGA GIS](https://saga-gis.sourceforge.io/en/index.html) est malheureusement bien souvent le chevalier oublié du SIG. Il possède certains traitements qui ne sont pas disponibles dans ArqGIS et peut également se révéler utile pour d'autres existants.

Depuis quelques versions, il n'est plus possible d'avoir les traitements de SAGA directement depuis ArqGIS. Il faut installer le plugin [SAGA NG](https://plugins.qgis.org/plugins/processing_saga_nextgen/) mais il a quelques limitations m'empêchant de l'utiliser pour l'article.
Pour cette partie, je vais directement passer par l'interface de SAGA, notamment afin de visualiser le résultat.

Il est intéressant de comparer le résultat de SAGA avec GEOS/ArqGIS. En effet, les opérations d'overlay ne reposent pas sur GEOS, mais sur une autre bibliothèque dédiée ; pour ceux intéressés, j'y reviendrai dans la partie sur les algorithmes.

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

### Sélection et intersection

Maintenant, tentons de vérifier si les points intersectent, ou non, notre base. Pour cela, on utilise l'outil « sélection par localisation » :
Geoprocessing -> Shapes -> Selection -> Selection by localisation.

![Select crossing base](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/saga_select_crossing_base.png){: .img-center loading=lazy }

Paf, erreur intéressante. Cela fonctionne seulement pour un point avec un polygone !

![Select crossing base error](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/saga_select_crossing_base_error.png){: .img-center loading=lazy }

Dans notre expérience avec GRASS, on avait un problème identique. Nous allons donc tester avec `base_poly` :

![Select crossing base poly](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/saga_select_crossing_base_poly.png){: .img-center loading=lazy }

Aucune sélection. Le message d'exécution nous l'indique bien (en Anglais) : "selected shapes: 0"

Même si l'on peut critiquer la méthode, car le dessin a été fait dans un autre contexte, ArqGIS/GEOS, on va tout de même tester la sélection des lignes :

On va reprendre notre exemple entre base et test_line.

20 sur 34, comme pour GEOS !

![Select base test line](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/saga_select_base_test_line.png){: .img-center loading=lazy }

C'est normal d'une certaine façon. Cependant, le premier test avec crossing, nous montre également que le point d'intersection n'intersecte pas la géométrie d'origine, comme pour GEOS.

Et qu'en est-il avec les bases de données relationnelles ? C'est ce que nous verrons dans la prochaine partie avec Microsoft SQL Server, Oracle et PostGIS.

[4 : les bases de données relationnelles :fontawesome-solid-forward-step:](./2024-08-08_de-la-tolerance-en-sig-geometrie-04-postgis-oracle-ms-sql-server.md "PostGIS, Oracle et MS SQL Server"){: .md-button }
{: align=middle }

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}

<!-- Notes de bas de page -->
