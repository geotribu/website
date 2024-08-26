---
title: "Les opérations géométriques dans PostGIS, Oracle et SQL Server"
subtitle: "Série : De la tolérance en SIG - chapitre 4"
authors:
    - Loïc Bartoletti
categories:
    - article
comments: true
date: 2024-08-08
description: "Quatrième partie du tour d'horizon des SIG sur les dessous des calculs géométriques : comparons les systèmes de gestion de bases de données relationnelles et spatiales PostGIS, Oracle et Microsoft SQL Server."
icon: material/database-marker
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_04_sgbdr.png
license: beerware
robots: index, follow
tags:
    - analyse
    - base de données
    - géométrie
    - GEOS
    - Oracle
    - PostGIS
    - SQL Server
---

# Et dans les bases de données ? Comparaison de SQL Server, Oracle et PostGIS

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

Si vous avez bien suivi les parties précédentes, vous savez que PostGIS va utiliser GEOS pour réaliser la plupart de ses opérations.
En particulier, notre cas sur l'intersection et le prédicat « intersects », sera délégué à GEOS.

![GEOS diagram from crunchy data](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/geos_diagram_dependent_project.webp){: .img-center loading=lazy }

> Source : [Performance Improvements in GEOS](https://www.crunchydata.com/blog/performance-improvements-in-geos), Paul Ramsey (2021, Crunchy Data)

Dans un premier temps, nous allons vérifier que les résultats de PostGIS sont identiques à ceux de GEOS « natifs », puis nous comparerons avec d'autres bases de données propriétaires.

Autant, je connais très bien PostGIS (au code duquel je contribue), autant, ma connaissance est limitée sur les autres bases. Je vous prie de m'excuser s'il y a des erreurs dans les requêtes ou des façons de faire plus académiques. Si une erreur se glisse ou une meilleure méthode existe, surtout n'hésitez pas à laisser un commentaire, respectueux, et je corrigerai cela.

![Série d'été 2024 de Loïc Bartoletti - Les Géométries et les SIG : PostGIS, Oracle et MS SQL Server - Crédits : Sylvain Beorchia](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_04_sgbdr.png){: .img-center loading=lazy }

Cet article est la quatrième partie de la série d'été sur la gestion de la géométrie dans les SIG.

[Le dossier :octicons-move-to-start-16:](./2024-07-16_de-la-tolerance-en-sig-geometrie-00-annonce.md "De la tolérance en SIG : le dossier"){: .md-button }
[3 : GRASS et SAGA :fontawesome-solid-backward-step:](./2024-08-01_de-la-tolerance-en-sig-geometrie-03-grass-saga.md "GRASS et SAGA"){: .md-button }
{: align=middle }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## PostGIS, même résultat que GEOS

![logo PostGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/postgis.jpg){: .img-thumbnail-left }

Le titre donne directement la conclusion, mais c'était déjà annoncé.

Nous allons reprendre nos deux WKB[^wkt_wkb] :

- base : `0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341`

- ligne : `010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341`

```sql
SELECT
    ST_Intersection(base, line)
FROM  
    ST_GeomFromWKB(decode(
        '0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341'
        , 'hex'), 3946) AS base,
    ST_GeomFromWKB(decode(
        '010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341'
        , 'hex'), 3946) AS line;
```

`01040000206A0F0000020000000101000000A899EFC8C83C3E4175E5698166D553410101000000B5EBDD9E8F3C3E416BF8515379D55341`

Retourne un EWKB, d'où la différence avec notre WKB de GEOS ; j'expliquerai cela dans le prochain article sur le WKB/WKT.

Si l'on enlève la partie « E », à savoir le SRID `0206A0F0`, on se retrouve avec le « bon » WKB :

`0104000000020000000101000000A899EFC8C83C3E4175E5698166D553410101000000B5EBDD9E8F3C3E416BF8515379D55341`

On peut directement le retrouver avec PostGIS en utilisant ST_AsBinary :

```sql
SELECT
    ST_AsBinary(ST_Intersection(base, line))
FROM
    ST_GeomFromWKB(decode(
        '0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341'
        , 'hex'), 3946) AS base,
    ST_GeomFromWKB(decode(
        '010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341'
        , 'hex'), 3946) AS line;
```

`\x0104000000020000000101000000a899efc8c83c3e4175e5698166d553410101000000b5ebdd9e8f3c3e416bf8515379d55341`

Pour la géométrie lisible, utilisant le format textuel, cela se fait avec `ST_AsText` :

```sql
SELECT
    ST_AsText(ST_Intersection(base, line))
FROM  
    ST_GeomFromWKB(decode(
        '0102000000050000007997c6b68d3c3e4139eb62c260d55341ac9ea7316a3c3e41cbeb40e073d55341403e0bfbc33c3e41b3fc06f380d55341387a2a800c3d3e41f256b8176dd553417997c6b68d3c3e4139eb62c260d55341'
        , 'hex'), 3946) AS base,
    ST_GeomFromWKB(decode(
        '010200000002000000ea9c6d2b873c3e41a03d941b7cd5534133db7796ce3c3e413fba569864d55341'
        , 'hex'), 3946) AS line;
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
SELECT
    ST_AsBinary(ST_Intersection(base.geom, line.geom)), ST_AsText(ST_Intersection(base.geom, line.geom))
FROM
    base, line;
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
FROM
    base, line;
```

On retrouve bien, notre malheureux `false` et notre distance très proche de 0, mais pas 0.

Ils se passent quoi chez les autres ?

----

## Microsoft SQL Server

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
FROM
    base, line;
```

Le résultat, sur SQL Server 15.0.4153, remis en forme, est :

```sql
0x6A0F0000010402000000B5EBDD9E8F3C3E416BF8515379D55341A899EFC8C83C3E4175E5698166D55341020000000100000000010100000003000000FFFFFFFF0000000004000000000000000001000000000100000001,
false,
false,
0,
0.00000000023283064365386963
```

Le résultat d'intersects est faux, et pourtant pour un des cas, la distance est égale à 0. Intéressant, est-ce vraiment un zéro ou tellement proche de 0, que ça retourne 0 ? Sinon, le second, est égal à celui de GEOS : 2.3283064365386963e-10

Pour le WKB, il est « particulier », mais nous retrouvons nos coordonnées :

- `A899EFC8C83C3E4175E5698166D55341`
- `B5EBDD9E8F3C3E416BF8515379D55341`

SQL Server n'utilise pas GEOS, mais sa propre [bibliothèque](https://docs.lib.purdue.edu/ddad2011/8/). Encore une fois, le problème n'est pas dans le code de GEOS.

----

## Oracle Spatial

![logo Oracle](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/oracle.png){: .img-thumbnail-left }

Oracle va nous donner des éléments intéressants. Passons directement à la requête :

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

Dont le résultat, sur Oracle XE 21, est :

```sql
"{2005,null,null,{1,1,2},{1981583.62057374,5199333.30187808,1981640.78490601,5199258.0220884}}",
"MULTIPOINT ((1981583.62057374 5199333.30187808), (1981640.78490601 5199258.0220884))",
0x0000000004000000020000000001413E3C8F9EDDEBAE4153D5795351F8700000000001413E3CC8C8EF99AB4153D5668169E577,
FALSE,
FALSE,
0.00000000104125029291017,
0.00000000023283064365387
```

Encore une fois ici, un résultat `false`. Comme PostGIS et SQL Server, on retrouve notre distance d'environ 2.3e-10, et une autre de 1e-9. Je trouve intéressant d'avoir ce petit écart sur une distance, mais je m'égare.

Ici, j'ai adapté la requête au langage SDO, expliquons la requête et le résultat :

Comme pour SQL Server, il faut convertir le WKB hexadécimal pour Oracle, on utilise `HEXTORAW`.

Si PostGIS va retourner un EWKB, pour un résultat de géométrie, Oracle, retourne sa représentation interne, à savoir :
`{2005,null,null,{1,1,2},{1981583.62057374,5199333.30187808,1981640.78490601,5199258.0220884}}`

Ce qui nous intéresse ici est le code `2005` qui veut dire MultiPoint 2D, ainsi que le tableau de coordonnées X/Y `{1981583.62057374,5199333.30187808,1981640.78490601,5199258.0220884}`.

On retrouve cette information avec la représentation WKT à laquelle nous sommes habitués :
`MULTIPOINT ((1981583.62057374 5199333.30187808), (1981640.784906015199258.0220884))`

Je ne vais pas m'étendre sur le WKB qui est « étrange », il est en Big Endian[^big_little_endian], alors que jusqu'à présent, je n'ai eu que du Little Endian[^big_little_endian] ; encore une fois plus d'explications dans l'article sur le WKB/WKT. Néanmoins, on a quelques différences entre ceux-ci, sans-doute liées à la précision du résultat ; n'étant pas expert Oracle, il me manque des éléments de compréhension et des tests à mener.

Toutefois, à la représentation après la virgule près, on a le même résultat :

| Base | x1  | y1  | x2  | y2  |
| :--  | :-: | :-: | :-: | :-: |
| Oracle | 1981583.62057374 | 5199333.30187808 | 1981640.78490601 | 5199258.0220884 |
| PostGIS | 1981583.6205737416 | 5199333.301878075 | 1981640.7849060092 | 5199258.022088398 |

J'ai indiqué en introduction qu'Oracle allait nous donner des éléments intéressants, mais pour l'instant, c'est comme les autres ? Oui, mais, il y a un paramètre que je n'ai pas encore expliqué. D'où sort le `0.00000000001` ?

Sur ma version, je n'ai pas de `ST_Intersects` ou un `SDO_Intersects`, je dois utiliser [`RELATE`](https://docs.oracle.com/en/database/oracle/oracle-database/21/spatl/SDO_GEOM-reference.html#GUID-E1209A71-F5D8-42A9-A93E-72657B115579). Nous avons également cela avec [PostGIS](https://postgis.net/docs/ST_Relate.html) (et GEOS). `ANYINTERACT` retourne `TRUE` si les objets ne sont pas disjoints, c'est ce que l'on veut.
Donc, on a notre équivalent de `ST_Intersects` ou plus exactement `not ST_Disjoint`. Toutefois, cela ne nous dit toujours pas ce qu'est ce `0.00000000001`. Vous souvenez-vous du titre principal de cette série ? [La tolérance](https://docs.oracle.com/en/database/oracle/oracle-database/21/spatl/spatial-concepts.html#GUID-7469388B-6D23-4294-904F-78CA3B7191D3).

Il s'agit donc d'une tolérance dans le calcul du prédicat. Avec une valeur « extrême », comme ici, le résultat est faux. Cependant, si l'on utilise une valeur plus cohérente avec notre unité, par exemple `1e-6`, nous aurons enfin notre « bon » résultat tant attendu :

```sql
"{2005,null,null,{1,1,2},{1981583.62057374,5199333.30187808,1981640.78490601,5199258.0220884}}",
"MULTIPOINT ((1981583.62057374 5199333.30187808), (1981640.78490601 199258.0220884))",
0x0000000004000000020000000001413E3C8F9EDDEBAE4153D5795351F8700000000001413E3CC8C8EF99AB4153D5668169E577,
TRUE,
TRUE,
0,
0
```

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
    ST_DWithin(base.geom, ST_Intersection(base.geom,line.geom), 1e-6),
    ST_DWithin(line.geom, ST_Intersection(base.geom,line.geom), 1e-6)
FROM
    base, line;
```

Enfin, concernant la distance, Oracle accepte un paramètre tolérance et donne un résultat différent suivant ce paramètre.
On pourrait penser que la distance devrait toujours être la même. Cependant, je pense — supposition, car connaissant mal Oracle — que celle-ci sert à arrondir si l'on est dans sa plage, et alors, pour notre cas, retourne 0, plutôt qu'un presque zéro.

Notre exploration n'est pas encore terminée, même si l'on s'approche de l'explication. On vient de voir, que, comme les SIG OpenSource, on ignore comment retourner correctement le prédicat `intersects` d'une intersection. Sauf à être tolérant, et nous y reviendrons.

[5 : la topologie à la rescousse des spaghettis :fontawesome-solid-forward-step:](./2024-08-15_de-la-tolerance-en-sig-geometrie-05-topologie-forces-et-limites.md "Modèles topologique et spaghetti"){: .md-button }
{: align=middle }

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}

<!-- Notes de bas de page -->

[^big_little_endian]: ou en Français, gros- et petit-boutisme, sont l'ordre dans lequel les octets sont placés. Pour plus d'informations, je vous invite à regarder [la page Wikipedia](https://fr.wikipedia.org/wiki/Boutisme)

<!-- markdownlint-disable   MD007 MD032 -->
[^wkt_wkb]:
    - **WKB (Well-Known Binary)** : Le WKB est un format binaire utilisé pour représenter des objets géométriques de manière compacte et efficace, couramment utilisé dans les bases de données géospatiales pour le stockage et l'échange de données géographiques.
    - **WKT (Well-Known Text)** : Le WKT est un format texte utilisé pour représenter des objets géométriques de manière lisible par l'humain. Il est souvent utilisé pour le partage et l'affichage de données géographiques.

    Pour plus d'informations, consultez la page [Wikipedia](https://fr.wikipedia.org/wiki/Well-known_text).
<!-- markdownlint-enable  MD007 MD032 -->
