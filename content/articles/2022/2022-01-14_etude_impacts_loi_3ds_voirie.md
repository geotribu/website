---
title: '3DS : mesurer l''impact du transfert des Routes Nationales aux Départements'
authors:
    - Michaël GALIEN
categories:
    - article
comments: true
date: 2022-01-14
description: Etude d'impacts du déclassement de la voirie nationale aux Départements dans le cadre de la loi 3DS ; loi relative à la Différenciation, la Décentralisation, la Déconcentration et portant diverses mesures de Simplification de l'action publique locale.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/etude_impacts_loi_3ds_voirie/etude_impacts_loi_3ds_voirie-logo.png
tags:
    - loi 3DS
    - PostGIS
    - PostgreSQL
    - route
    - SQL
    - voirie
---

# 3DS : mesurer l'impact du transfert des Routes Nationales aux Départements

## Introduction

Et non, je ne vais pas vous parler dans cet article de la célèbre console Nintendo (11 ans déjà) mais de la loi relative à la Différenciation, la Décentralisation, la Déconcentration et portant diverses mesures de Simplification de l'action publique locale.

![Loi 3DS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/etude_impacts_loi_3ds_voirie/etude_impacts_loi_3ds_voirie-logo.png "Loi 3DS"){: .img-center loading=lazy }

La loi 3DS ambitionne de [donner aux collectivités de nouvelles compétences](https://www.cnews.fr/france/2022-01-04/decentralisation-quest-ce-que-le-projet-3ds-qui-doit-etre-adopte-par-les-deputes), comprenant notamment le transfert d'une partie des Routes Nationales (RN) aux Départements, gestionnaires de la voirie départementale.

C'est dans ce cadre que le [Département du Gard](http://www.gard.fr/accueil.html) a souhaité analyser l'impact pour son organisation de ce transfert de la voirie nationale vers la voirie départementale.

Let's go !

**Pré-requis :**

* Une base de données [PostgreSQL](https://www.postgresql.org)/[PostGIS](https://postgis.net).
* Un client d'accès à la base de données type [_pgAdmin_](https://www.pgadmin.org/) ou [_DBeaver_](https://dbeaver.io/).
* La [BD Topo® de l'IGN](https://geoservices.ign.fr/bdtopo) sur l'emprise d'étude.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Données sources

![logo IGN](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/ign.png "logo IGN"){: .img-thumbnail-left }

J'utilise pour cette analyse la [BD Topo® de l'IGN](https://geoservices.ign.fr/bdtopo) et plus précisément la classe _troncon_de_route_ du thème _transport_ que j'ai importée dans une table nommée `bdtopo_troncon_de_route`.

Je dispose des données France entière et je dois donc limiter l'analyse aux seuls tronçons du département du Gard (30).

Afin ne pas avoir à réaliser une jointure géographique sur une autre table, je m'appuie sur les champs `insee_commune_droite` et `insee_commune_gauche`. Je vérifie que l'un ou l'autre matche avec le [COG](https://fr.wikipedia.org/wiki/Code_officiel_g%C3%A9ographique) d'une commune du Gard c'est à dire qu'il commence par 30.

----

## Les requêtes réalisées

### Les Routes Nationales (RN) concernées

Le premier besoin est d'identifier la liste des Routes Nationales sur le territoire d'étude.

Je cherche pour cela les numéros distincts des Routes Nationales présentes sur l'emprise d'étude grâce à la requête suivante :

!!! Note
    Le recours aux expressions régulières c'est clairement pour me la péter, j'aurais pu faire un `like`...mais ça a l'intérêt de montrer [l'opérateur ~](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP).

```sql
select distinct cpx_numero as "RN"
from bdtopo_troncon_de_route
where cpx_classement_administratif = 'Nationale'
and (insee_commune_droite ~ '^30' or insee_commune_gauche ~ '^30')
order by 1;
```

Le résultat obtenu est le suivant :

|RN|
|-|
|N100|
|N106|
|N113|
|N580|
|N86|

### Longueur en Km par RN

Vient ensuite la question du nombre de Km supplémentaires de voirie que le Département aura en gestion.

Je calcule pour cela la somme (`sum`) des longueurs ([`ST_3DLength`](https://postgis.net/docs/ST_3DLength.html)) des tronçons. La valeur obtenue est convertie en Km puis arrondie à deux décimales (`round`).

Le `group by` me permet d'avoir la longueur non pas totale mais par RN.

```sql
select cpx_numero as "RN", round(sum(ST_3DLength(geometrie))::numeric / 1000, 2) as "Km"
from bdtopo_troncon_de_route
where cpx_classement_administratif = 'Nationale'
and (insee_commune_droite ~ '^30' or insee_commune_gauche ~ '^30')
group by cpx_numero
order by 1;
```

Le résultat tombe :

|RN|Km|
|-|-|
|N100|20.14|
|N106|106.21|
|N113|27.48|
|N580|23.61|
|N86|12.64|

### Longueur en Km par nature et nombre de voies

Cette première liste des RN avec les longueurs associées est intéressante mais elle ne permet pas de mesurer précisément l'impact pour le Département du Gard.

En effet, les profils de RN sont variés et nécessitent un entretien adapté. Une 2 * 2 voies sera plus consommatrice de ressources qu'une simple chaussée.

J'adapte ici la requête qui précède pour afficher les longueurs par nature et nombre de voies, ce qui donne la syntaxe suivante :

```sql
select nature as "Nature", nombre_de_voies as "Nb. voies", round(sum(ST_3DLength(geometrie))::numeric / 1000, 2) as "Km"
from bdtopo_troncon_de_route
where cpx_classement_administratif = 'Nationale'
and (insee_commune_droite ~ '^30' or insee_commune_gauche ~ '^30')
group by nature, nombre_de_voies
order by 1, 2;
```

La requête me permet d'obtenir les mesures suivantes :

|Nature|Nb. voies|Km|
|-|-|-|
|Bretelle|1|0.27|
|Bretelle|2|0.06|
|Rond-point|1|0.50|
|Rond-point|2|4.45|
|Rond-point|3|0.20|
|Route à 1 chaussée|1|4.78|
|Route à 1 chaussée|2|66.64|
|Route à 1 chaussée|3|6.73|
|Route à 1 chaussée|4|0.78|
|Route à 2 chaussées|1|31.35|
|Route à 2 chaussées|2|19.66|
|Route à 2 chaussées|3|0.69|
|Type autoroutier|1|5.19|
|Type autoroutier|2|48.76|

### Nombre de giratoires

Grâce à la requête précédente, on apprend qu'environ 5 Km de ronds-points pourraient être transférés au Département du Gard, il serait intéressant de connaître le nombre exact de giratoires que cela représente.

Il est possible de déterminer ce nombre en se focalisant sur les tronçons de nature _Rond-point_ et à l'aide de la fonction [`ST_ClusterIntersecting`](https://postgis.net/docs/ST_ClusterIntersecting.html), qui retourne un tableau dont chaque cellule agrège les géométries qui s'intersectent.

Il reste ensuite à compter le nombre de cellules du tableau, ce qui donne la requête suivante :

```sql
select cpx_numero as "RN", array_length(ST_ClusterIntersecting(geometrie), 1) as "Nb. giratoires"
from bdtopo_troncon_de_route
where cpx_classement_administratif = 'Nationale'
and (insee_commune_droite ~ '^30' or insee_commune_gauche ~ '^30')
and nature = 'Rond-point'
group by cpx_numero
order by 1;
```

Il sera donc question pour le Gard d'assurer la gestion de 36 nouveaux giratoires ainsi répartis :

|RN|Nb. giratoires|
|-|-|
|N100|6|
|N106|13|
|N113|5|
|N580|5|
|N86|7|

![Giratoires RN580](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/etude_impacts_loi_3ds_voirie/etude_impacts_loi_3ds_voirie-giratoires.png "Giratoires RN580"){: .img-center loading=lazy }

### Et les ponts ? Et les tunnels ?

Les ouvrages d'art (ponts, tunnels, etc.) nécessitent un entretien suivi et une organisation de service spécifique. Il est donc utile de connaitre le nombre d'ouvrages d'art se trouvant actuellement sur le réseau routier national.

Pour les identifier, j'utilise cette fois l'attribut `position_par_rapport_au_sol`.

Ici, la fonction [`ST_ClusterIntersecting`](https://postgis.net/docs/ST_ClusterIntersecting.html) ne convient pas car en visualisant les données, on remarque que plusieurs ouvrages supportent deux chaussées séparées et donc deux géométries distinctes dans la BD Topo®.

![Chaussées séparées soutenues par un OA](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/etude_impacts_loi_3ds_voirie/etude_impacts_loi_3ds_voirie-oa.png "Chaussées séparées soutenues par un OA"){: .img-center loading=lazy }

Pour gérer ce cas, j'utilise la fonction [`ST_ClusterWithin`](https://postgis.net/docs/ST_ClusterWithin.html) qui permet d'agréger des géométries dès lors qu'elles sont à moins d'une distance donnée.

J'ai fixé de façon empirique cette distance à 25 mètres dans les requêtes qui suivent. La distance utilisée doit être suffisante pour raccrocher les deux géométries représentant les chaussées séparées mais pas trop importante afin d'éviter d'associer à tord deux ouvrages qui seraient proches.

Requête permettant de compter les ponts :

```sql
select cpx_numero as "RN", array_length(ST_ClusterWithin(geometrie, 25), 1) as "Nb. ouvrages"
from bdtopo_troncon_de_route
where cpx_classement_administratif = 'Nationale'
and (insee_commune_droite ~ '^30' or insee_commune_gauche ~ '^30')
and position_par_rapport_au_sol ~ '^(Gué ou radier|[1-9])'
group by cpx_numero
order by 1;
```

Requête permettant de compter les tunnels :

```sql
select cpx_numero as "RN", array_length(ST_ClusterWithin(geometrie, 25), 1) as "Nb. ouvrages"
from bdtopo_troncon_de_route
where cpx_classement_administratif = 'Nationale'
and (insee_commune_droite ~ '^30' or insee_commune_gauche ~ '^30')
and position_par_rapport_au_sol ~ '^-[1-9]'
group by cpx_numero
order by 1;
```

Les résultats respectifs sont :

|RN|Nb. ouvrages|
|-|-|
|N100|1|
|N106|59|
|N113|14|
|N580|7|
|N86|7|

et :

|RN|Nb. ouvrages|
|-|-|
|N106|1|

### Pourcentage d'évolution

Plus que les distances, il est surtout intéressant de mesurer l'évolution du linéaire que cela représente par rapport à l'actuelle voirie départementale gérée par le Département du Gard.

Pour cela, je reprends la requête de calcul des longueurs par nature et nombre de voies, vue plus haut, que j'applique aux routes nationales et aux routes départementales.

Je mets face à face les chiffres obtenus à l'aide d'un `full join` (c'est à dire l'équivalent d'un `right join` et d'un `left join` combinés).

Je peux ensuite calculer le ratio en prennant soin de gérer les cas aux limites (division par null et 0) notamment à l'aide de la fonction [`coalesce`](https://www.postgresql.org/docs/current/functions-conditional.html#FUNCTIONS-COALESCE-NVL-IFNULL).

Enfin, je trie le résultat dans l'ordre décroissant des valeurs, ce qui donne la requête suivante :

```sql
with RN as (
    select nature as "Nature", nombre_de_voies as "Nb. voies", round(sum(ST_3DLength(geometrie))::numeric / 1000, 2) as "Km"
    from bdtopo_troncon_de_route
    where cpx_classement_administratif = 'Nationale'
    and (insee_commune_droite ~ '^30' or insee_commune_gauche ~ '^30')
    group by nature, nombre_de_voies
),
RD as (
    select nature as "Nature", nombre_de_voies as "Nb. voies", round(sum(ST_3DLength(geometrie))::numeric / 1000, 2) as "Km"
    from bdtopo_troncon_de_route
    where cpx_classement_administratif = 'Départementale'
    and (insee_commune_droite ~ '^30' or insee_commune_gauche ~ '^30')
    group by nature, nombre_de_voies
)
select
    coalesce(rn."Nature", rd."Nature") as "Nature",
    coalesce(rn."Nb. voies", rd."Nb. voies") as "Nb. voies",
    coalesce(rn."Km", 0) as "Km RN",
    coalesce(rd."Km", 0) as "Km RD",
    case
        when rd."Km" is null then '∞'
        else (round((coalesce(rn."Km", 0) / rd."Km") * 100, 2)::varchar) || '%'
    end as "Evolution"
from RN
full join RD on rn."Nature" = rd."Nature" and rn."Nb. voies" = rd."Nb. voies"
order by coalesce(rn."Km", 0) / rd."Km" desc nulls first;
```

Le requête s'exécute, sur mon infra, pendant plus de 2 minutes avant de donner le résultat qui suit :

|Nature|Nb. voies|Km RN|Km RD|Evolution|
|-|-|-|-|-|
|Rond-point|3|0.20|0|∞|
|Type autoroutier|1|5.19|0|∞|
|Type autoroutier|2|48.76|0|∞|
|Bretelle|2|0.06|0.02|300.00%|
|Route à 2 chaussées|3|0.69|0.36|191.67%|
|Route à 1 chaussée|3|6.73|17.09|39.38%|
|Route à 1 chaussée|4|0.78|2.52|30.95%|
|Route à 2 chaussées|2|19.66|94.33|20.84%|
|Route à 2 chaussées|1|31.35|169.13|18.54%|
|Rond-point|2|4.45|41.21|10.80%|
|Rond-point|1|0.50|6.44|7.76%|
|Bretelle|1|0.27|3.88|6.96%|
|Route à 1 chaussée|2|66.64|3501.79|1.90%|
|Route à 1 chaussée|1|4.78|790.90|0.60%|
|Route empierrée|NULL|0|0.41|0.00%|

----

## Bilan

![logo PostGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/postgis.png "logo PostGIS"){: .img-thumbnail-left }

En conclusion, le couple PostgreSQL/PostGIS a permis d'évaluer assez rapidement l'impact de la loi 3DS en mesurant quelques indicateurs routiers à partir des données présentes dans la BD Topo® de l'IGN.

Il est désormais possible d'utiliser les ratios obtenus avec la dernière requête pour estimer l'impact financier et les besoins RH associés au transfert de la voirie nationale vers les Départements.

J'apprécie ce type de d'analyses qui montrent bien que la géomatique ne se limite pas à la cartographie. Elles permettent à partir de quelques requêtes sur un jeu de donnée géographique de sortir des indicateurs assez fins qui pourront aider la direction en charge des routes et les élus pour la prise de décisions.

A noter que les requêtes peuvent facilement être adaptées pour les autres Départements. Il suffit pour cela de cibler la table PostgreSQL qui contient les données sources et modifier le filtre appliqué sur les champs `insee_commune_droite` et `insee_commune_gauche`.

----

<!-- geotribu:authors-block -->
