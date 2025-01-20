---
title: SFCGAL c'est trop de la balle !
subtitle: "Série : De la tolérance en SIG - chapitre 6"
authors:
    - Loïc Bartoletti
categories:
    - article
comments: true
date: 2024-08-22
description: "Sixième partie du tour d'horizon des SIG sur les dessous des calculs géométriques : utilisation de SFCGAL pour des calculs plus robustes"
icon: material/decimal-comma-decrease
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_06_sfcgal.png
license: beerware
robots: index, follow
tags:
    - analyse
    - géométrie
    - SFCGAL
---

# Approche alternative : utilisation de SFCGAL pour des calculs plus robustes

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

Dans les parties précédentes, nous avons montré que le « intersects » d'une intersection, était faux, sauf avec la topologie ou la tolérance.  
Nous allons maintenant utiliser une « approche alternative » dans les calculs. Promis, je garde le code pour une autre partie à la lecture optionnelle.

Pour cela, laissez-moi introduire [SFCGAL](https://sfcgal.gitlab.io/SFCGAL/).

![Série d'été 2024 de Loïc Bartoletti - Les Géométries et les SIG : SFCGAL - Crédits : Sylvain Beorchia](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_06_sfcgal.png){: .img-center loading=lazy }

[Le dossier :octicons-move-to-start-16:](./2024-07-16_de-la-tolerance-en-sig-geometrie-00-annonce.md "De la tolérance en SIG : le dossier"){: .md-button }
[5 : topologie vs spaghetti :fontawesome-solid-backward-step:](./2024-08-15_de-la-tolerance-en-sig-geometrie-05-topologie-forces-et-limites.md "Topologie ; forces et limites"){: .md-button }
{: align=middle }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## SFCGAL ?

Il s'agit d'une bibliothèque logicielle C++ sous licence [LGPL2+](https://www.gnu.org/licenses/old-licenses/lgpl-2.0.html) construite comme une surcouche de [CGAL](https://www.cgal.org/) avec pour objectif de supporter l'[ISO 19107:2013](https://www.iso.org/fr/standard/26012.html) et la norme OGC [Simple Features Access](https://www.opengeospatial.org/standards/sfa/) 1.2 de l'OGC pour les opérations en 3D.

![logo SFCGAL](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/sfcgal.webp){: .img-center loading=lazy }

Concrètement, SFCGAL fournit des types de géométries et des opérations conformes aux normes, auxquels on accède via ses API [C](https://sfcgal.gitlab.io/SFCGAL/doxygen/group__capi.html) ou [C++](https://sfcgal.gitlab.io/SFCGAL/doxygen/group__public__api.html).

Par exemple, PostGIS utilise l'API C pour exposer certaines fonctions de SFCGAL dans les bases de données spatiales (cf. [manuel de PostGIS](https://postgis.net/docs/reference.html#reference_sfcgal)).

Les coordonnées des géométries ont une représentation en [nombre rationnel exact](https://fr.wikipedia.org/wiki/Nombre_rationnel) et peuvent être en 2D ou en 3D.

En gros, SFCGAL, fait la géométrie comme on connaît dans nos SIG, mais avec le moteur de CGAL et surtout des nombres « différents » : rationnel exact.
L'explication plus détaillée sera donnée dans la partie algorithme et code, mais considérons que ce sont des fractions.

On utilisera SFCGAL de deux façons, pour comparer leurs résultats :

- avec Python
- et avec PostGIS.

----

## Python avec PySFCGAL

[PySFCGAL](https://gitlab.com/sfcgal/pysfcgal) est une interface Python pour la bibliothèque SFCGAL, en cours de développement et de packaging. À défaut d'avoir une application `sfcgalop` à la `geosop`  (au moment de la publication de l'article, celle-ci est en cours de développement) l'interface Python permet de faire des calculs plus facilement qu'en C ou C++. Promis, c'est « lisible » comme code.

Sur mon système FreeBSD, voici comment je l'utilise pour notre test :

```python title="Lecture de WKB avec PySFCGAL"
# Import de la bibliothèque
from pysfcgal import sfcgal
# Lecture du wkb base
base = sfcgal.read_wkb('0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341')
# Lecture du wkb line
line = sfcgal.read_wkb('010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341')
```

Notre calcul d'intersection se fera simplement avec cette ligne :

```python title="Calcul d'intersection avec PySFCGAL"
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

## PostGIS avec SFCGAL

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

Malgré les problèmes potentiels de précision dans son utilisation dans PostGIS, SFCGAL reste un outil précieux. Son principal atout réside dans ses fonctionnalités avancées en 2D et 3D, absentes de GEOS/PostGIS natif. Par ailleurs, ces erreurs ne sont pas systématiques et dépendent des données et opérations effectuées.

[7 : La gestion propriétaire de la géométrie : ESRI et FME :fontawesome-solid-forward-step:](./2024-08-29_de-la-tolerance-en-sig-geometrie-07-esri-fme.md "Gestion de la précision géométrique dans Esri et FME"){: .md-button }
{: align=middle }

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}

<!-- Notes de bas de page -->
