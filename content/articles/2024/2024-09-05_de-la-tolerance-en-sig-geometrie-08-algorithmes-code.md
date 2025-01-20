---
title: "Algorithmes géométriques et code : comment cela fonctionne-t-il ?"
subtitle: "Série : De la tolérance en SIG - chapitre 8"
authors:
    - Loïc Bartoletti
categories:
    - article
comments: true
date: 2024-09-05
description: "Huitième partie du tour d'horizon des SIG sur les dessous des calculs géométriques : algorithmes et code"
icon: material/code-block-tags
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_08_algos.png
license: beerware
robots: index, follow
tags:
    - algorithmes
    - analyse
    - géométrie
    - python
    - SFCGAL
---

# Algorithmes géométriques et code : comment cela fonctionne-t-il ?

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![logo console terminal](https://cdn.geotribu.fr/img/logos-icones/divers/ligne_commande.png){: .img-thumbnail-left }

Maintenant que l'on a regardé comment sont gérées les opérations géométriques sous le capot de différents logiciels SIG, essayons de comprendre comment se code concrètement une formule mathématique. En somme, codons notre propre algorithme de calcul géométrique !

!!! info "Disclaimer"
    Cet article s'adresse à tous les géomaticiens, quel que soit leur niveau de compétence informatique. Cependant, ceux qui sont déjà familiers avec les erreurs comme `#!python 0.1 + 0.2 != 0.3` ne trouveront peut-être pas de nouvelles informations ici. Encore une fois, j'essaie de vulgariser. Si une version plus détaillée vous intéresse, je peux essayer d'en faire une.

![Série d'été 2024 de Loïc Bartoletti - Les Géométries et les SIG : Algorithmes - Crédits : Sylvain Beorchia](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_08_algos.png){: .img-center loading=lazy }

Cet article est la huitième partie de la série d'été sur la gestion de la géométrie dans les SIG.

[Le dossier :octicons-move-to-start-16:](./2024-07-16_de-la-tolerance-en-sig-geometrie-00-annonce.md "De la tolérance en SIG : le dossier"){: .md-button }
[7 : gestion propriétaire de la géométrie : ESRI et FME :fontawesome-solid-backward-step:](./2024-08-29_de-la-tolerance-en-sig-geometrie-07-esri-fme.md "Gestion de la géométrie dans ESRI et FME"){: .md-button }
{: align=middle }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Un triangle ne manque pas d'aire

Ceci dit, comment qu'on calcule si un point C est sur un segment AB ? On calcule l'aire du triangle ABC !

Dit autrement, avec un peu plus de formalisme mathématique, pour déterminer si un point \( C \) est sur une droite définie par deux points \( A \) et \( B \), on peut utiliser la géométrie vectorielle. Voici une méthode simple pour le faire :

1. **Coordonnées des points** : supposons que les coordonnées des points \( A \), \( B \) et \( C \) soient respectivement \( (x_A, y_A) \), \( (x_B, y_B) \) et \( (x_C, y_C) \).

1. **Vecteur AB et AC** : calculons les vecteurs \( \overrightarrow{AB} \) et \( \overrightarrow{AC} \) :

    - \( \overrightarrow{AB} = (x_B - x_A, y_B - y_A) \)
    - \( \overrightarrow{AC} = (x_C - x_A, y_C - y_A) \)

1. **Déterminant** : calculons le déterminant des vecteurs \( \overrightarrow{AB} \) et \( \overrightarrow{AC} \). Ce déterminant est donné par :

    \[
    \text{D} = (x_B - x_A) \cdot (y_C - y_A) - (y_B - y_A) \cdot (x_C - x_A)
    \]

1. **Vérification** :

    - Si \( \text{D} = 0 \), alors les points \( A \), \( B \) et \( C \) sont colinéaires, ce qui signifie que \( C \) est sur la droite \( AB \).
    - Si \( \text{D} \neq 0 \), alors \( C \) n'est pas sur la droite \( AB \).

## Exemple

Supposons que les coordonnées soient :

- \( A = (1, 2) \)
- \( B = (4, 6) \)
- \( C = (2, 3) \)

Calculons les vecteurs :

- \( \overrightarrow{AB} = (4 - 1, 6 - 2) = (3, 4) \)
- \( \overrightarrow{AC} = (2 - 1, 3 - 2) = (1, 1) \)

Calculons le déterminant :

\[
\text{D} = 3 \cdot 1 - 4 \cdot 1 = 3 - 4 = -1
\]

Puisque \( \text{D} \neq 0 \), le point \( C \) n'est pas sur la droite \( AB \).

Voici une implémentation simple en Python :

```python title="Calcul aire et orientation d'un triangle"
def orient2d(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float):
    """Calcule le double de l'aire du triangle formé par les points a, b et c.
    Si le résultat est positif, les points sont orientés dans le sens antihoraire.
    Si le résultat est négatif, les points sont orientés dans le sens horaire.
    Si le résultat est nul, les points sont alignés.
    """
    return (x_b - x_a) * (y_c - y_a) - (y_b - y_a) * (x_c - x_a)

def shoelace_area(x_a: float, y_a: float, x_b: float, y_b: float, x_c: float, y_c: float):
    """Calcul de l'aire en utilisant la formule de la shoelace."""  
    area = 0.5 * (x_a * (y_b - y_c) + x_b * (y_c - y_a) + x_c * (y_a - y_b))
    return area

# Exemple d'utilisation
x_a, y_a = 1, 2
x_b, y_b = 4, 6
x_c, y_c = 2, 3

area = shoelace_area(x_a, y_a, x_b, y_b, x_c, y_c)
orient = orient2d(x_a, y_a, x_b, y_b, x_c, y_c)
print(f"L'aire du triangle est : {area}")
# L'aire du triangle est : -0.5
print(f"L'orientation du triangle ABC est : {orient}")
# L'orientation du triangle ABC est : -1
```

Le code retourne un nombre négatif ; l'aire étant la moitié de l'orientation.

Si l'on inverse A et B, comme suit :

```python
area = shoelace_area(x_b, y_b, x_a, y_a, x_c, y_c)
orient = orient2d(x_b, y_b, x_a, y_a, x_c, y_c)
print(f"L'aire du triangle est : {area}")
# L'aire du triangle est : 0.5
print(f"L'orientation du triangle BAC est : {orient}")
# L'orientation du triangle BAC est : 1
```

On retrouve un nombre positif. Le point C est de l'autre côté de l'axe AB, dit autrement, AB et C ne sont pas colinéaires.

```python title="Exemple d'utilisation avec des points colinéaires"
x_a, y_a = 1, 1
x_b, y_b = 2, 2
x_c, y_c = 3, 3

area = shoelace_area(x_b, y_b, x_a, y_a, x_c, y_c)
orient = orient2d(x_b, y_b, x_a, y_a, x_c, y_c)
print(f"L'aire du triangle est : {area}")
# L'aire du triangle est : 0.0
print(f"L'orientation du triangle BAC est : {orient}")
# L'orientation du triangle BAC est : 0
```

```python title="Exemple d'utilisation avec des points colinéaires"
x_a, y_a = 0.1, 0.1
x_b, y_b = 0.2, 0.2
x_c, y_c = 0.3, 0.3

area = shoelace_area(x_b, y_b, x_a, y_a, x_c, y_c)
orient = orient2d(x_b, y_b, x_a, y_a, x_c, y_c)
print(f"L'aire du triangle est : {area}")
# L'aire du triangle est : -1.734723475976807e-18
print(f"L'orientation du triangle BAC est : {orient}")
# L'orientation du triangle BAC est : 0.0
```

Comme sur ma machine, vous devriez avoir une « blague ». L'aire n'est pas exactement égale à 0, mais proche de 0.

Quelles sont donc les problèmes de cette « blague » ?

## L'utilisation des nombres flottants

Si l'on admet que C est le point d'intersection d'un segment avec AB, alors, en théorie, les lignes se croisent en un point bien défini : C. Cependant, en pratique, les ordinateurs effectuent des calculs en utilisant une représentation numérique finie qui peut introduire de petites erreurs. Voici pourquoi cela se produit :

Les ordinateurs utilisent majoritairement une représentation en [virgule flottante](https://fr.wikipedia.org/wiki/Virgule_flottante) pour stocker des nombres réels. C'est même la norme pour les coordonnées de nos géométries. Ce fameux double que l'on retrouve de partout. Toutefois son utilisation peut introduire des erreurs d'arrondi. J'ai indiqué une opération en introduction, 0.1 + 0.2 != 0.3. Comme 0.3 ne peut pas être représenté exactement cela conduit à des approximations. C'est un problème connu des informaticiens, au point d'avoir [son propre site](https://0.30000000000000004.com/).
De même, je ne peux qu'encourager la lecture de l'article [What Every Computer Scientist Should Know About Floating-Point Arithmetic](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html).

Il existe d'autres nombres sur des ordinateurs. Vous avez pu voir que 1 + 2 est bien égal à 3. Tandis que 0.1 + 0.2 n'est pas égal à 0.3.

Les opérations sur les entiers sont toujours justes, dans leurs limites. Alors pourquoi ne pas utiliser que des entiers ?

C'est plus ou moins ce qui est fait par d'autres bibliothèques de calculs. On pensera notamment à SFCGAL, mais comme on l'a vu, cela ne fait pas tout. L'enregistrement se faisant en double, la conversion va introduire des erreurs ; on détaillera cela plus bas.

## L'accumulation d'erreurs

Lors de calculs complexes, ces petites erreurs d'arrondi peuvent s'accumuler et devenir significatives.

Lors du calcul de l'intersection de deux lignes, plusieurs opérations arithmétiques sont nécessaires. Chaque opération peut introduire une petite erreur.

Des solutions comme GEOS ou Clipper (pour SAGA), repose sur des calculs bien plus robustes que notre exemple ; d'ailleurs, elles passent également par des entiers. Le calcul de l'intersection va être juste - à la précision du float.

## Comparaisons de précision

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

Pour une étude plus approfondie, je vous encourage à lire l'article [Comparing Two Floating-Point Numbers](https://embeddeduse.com/2019/08/26/qt-compare-two-floats/).

Comme vous avez pu le deviner, c'est ce que fait ArcGIS.
Dans plusieurs endroits de nos SIG, il existe des comparaisons floues, peut-être que les prochaines versions de GEOS intègreront cette tolérance pour les relations. :wink:

## Retour sur SFCGAL

On a vu que SFCGAL est la seule bibliothèque à donner le bon résultat pour intersects, mais seulement en python. Avec PostGIS, il retourne faux comme GEOS, pourquoi ?

SFCGAL, n'utilise pas les flottants, mais une autre arithmétique. Pour rappel, notre code exemple est :

```python title="Intersection avec PySFCGAL"
from pysfcgal import sfcgal

base = sfcgal.read_wkb('0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341')
line = sfcgal.read_wkb('010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341')

result = base.intersection(line)
# Affiche du WKT avec 10 décimales
print(result.wktDecim(10))
# MULTIPOINT((1981583.6205737418 5199333.3018780742),(1981640.7849060092 5199258.0220883982))
print(base.intersects(result))
# True
print(line.intersects(result))
# True
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
# False
print(line.intersects(np))
# False
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

## Webographie

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

[9 : 5 conseils pour bien vivre géométriquement (le 4è va vous étonner) :fontawesome-solid-forward-step:](./2024-09-26_de-la-tolerance-en-sig-geometrie-09-conclusions.md "Conclusions et conseils de vie"){: .md-button }
{: align=middle }

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
