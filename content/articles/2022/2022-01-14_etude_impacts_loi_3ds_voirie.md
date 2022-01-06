---
title: "3DS : Impacts du déclassement du réseau routier national aux départements"
authors:
    - Michaël GALIEN
categories:
    - article
date: "2022-01-14 10:00"
description: "Etude d'impacts du déclassement de la voirie nationale aux départements dans le cadre de la loi 3DS ; loi relative à la Différenciation, la Décentralisation, la Déconcentration et portant diverses mesures de Simplification de l'action publique locale."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/etude_impacts_loi_3ds_voirie/etude_impacts_loi_3ds_voirie-logo.png"
tags:
    - Loi 3DS
    - PostGIS
    - PostgreSQL
    - Route
    - SQL
    - Voirie
---

# 3DS : Impacts du déclassement du réseau routier national aux départements

## Introduction

Et non, je ne vais pas vous parler dans cet article de la célèbre console Nintento (10 ans déjà) mais de la loi relative à la Différenciation, la Décentralisation, la Déconcentration et portant diverses mesures de Simplification de l'action publique locale.

![Loi 3DS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/etude_impacts_loi_3ds_voirie/etude_impacts_loi_3ds_voirie-logo.png "Loi 3DS"){: loading=lazy }

Les fonctionnaires territoriaux connaissent par coeur les 3 actes de la décentralisation, la loi 3DS sera peut-être considérée comme le quatrième acte.

La loi ambitionne de [donner aux collectivités de nouvelles compétences](https://www.cnews.fr/france/2022-01-04/decentralisation-quest-ce-que-le-projet-3ds-qui-doit-etre-adopte-par-les-deputes). Il y est notamment question du transfert des routes nationales (RN) aux départements.

C'est dans ce cadre que le département du Gard m'a demandé d'analyser les impacts de ce transfert sur nos organisations.

Let's go !

**Pré-requis :**

* Une base de données PostgreSQL/PostGIS.
* Un client d'accès à la base de données type _pgAdmin_ ou _DBeaver_.
* La BDTopo sur l'emprise d'étude.

## Données sources

![logo IGN](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/ign.png "logo IGN"){: .img-rdp-news-thumb }

J'utilise pour cette analyse la BDTopo de l'IGN et plus précisément la classe _troncon_de_route_ du thème _transport_ que j'ai importé dans une table nommée `bdtopo_troncon_de_route`.

Je dispose des données France entière et je dois donc limiter l'analyse aux seuls tronçons du département.

Je pourrais pour cela faire une jointure géographique mais pour ne pas avoir à utiliser une autre table, je m'appuie sur les champs `insee_commune_droite` et `insee_commune_gauche`. Je regarde que l'un ou l'autre matche le COG d'une commune du Gard c'est à dire qu'il commence par 30.

## Les requêtes

### RN concernées


Le premier besoin est simplement de connaître la liste des routes nationales concernées.

Je cherche pour cela les numéros distincts des nationales présentes sur l'emprise d'étude grâce à la requête suivante :

NB : Le recours aux expressions régulières c'est clairement pour me la péter, j'aurais pu faire un like...mais ça a l'intérêt de montrer [l'opérateur ~](https://www.postgresql.org/docs/current/functions-matching.html#FUNCTIONS-POSIX-REGEXP).

```SQL
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

Vient ensuite la question du nombre de Km supplémentaires de voirie que le département aura en gestion.

Je calcule pour cela la somme (`sum`) des longueurs ([`ST_3DLength`](https://postgis.net/docs/ST_3DLength.html)) des tronçons. La valeur obtenue est convertie en Km puis arrondie à deux décimales (`round`).

Le `group by` me permet d'avoir la longueur non pas totale mais par RN.

```SQL
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

Si ces premiers indicateurs sont intéressants, ils ne permettent pas de bien mesurer les incidences pour le département.

En effet, les profils de routes sont variés et nécessitent un entretien adapté. Une 2 * 2 sera plus consommatrice de ressources qu'une simple chaussée.

J'adapte ici la requête qui précède pour afficher les longueurs par nature et nombre de voies, ce qui donne :

```SQL
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

On a appris grâce au résultat qui précède que le département devrait récupérer l'équivalent d'environ 5 Km de ronds-points, mais combien de giratoires cela représente ?

Il est possible de répondre à cette question en se focalisant sur les tronçons de nature _Rond-point_ et à l'aide de la fonction [`ST_ClusterIntersecting`](https://postgis.net/docs/ST_ClusterIntersecting.html). Celle-ci retourne un tableau dont chaque cellule agrège les géométries qui s'intersectent.

Il ne reste alors plus qu'à compter le nombre de cellules du tableau, ce qui donne :

```SQL
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

![Giratoires RN580](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/etude_impacts_loi_3ds_voirie/etude_impacts_loi_3ds_voirie-giratoires.png "Giratoires RN580"){: loading=lazy }

### Et les ponts ? Et les tunnels ?

Les ouvrages d'arts nécessitent une attention particulière. Il est donc utile de savoir combien d'ouvrages se trouvent sur l'actuel réseau national.

Pour les identifier, j'utilise cette fois l'attribut `position_par_rapport_au_sol`.

Ma première idée était de réutiliser la fonction [`ST_ClusterIntersecting`](https://postgis.net/docs/ST_ClusterIntersecting.html) mais celle-ci présente une limite pour ce cas d'usage.

Lorsqu'on regarde en détail, on remarque que plusieurs ouvrages supportent 2 chaussées séparées et donc 2 lignes distinctes dans la BDTopo.

![Chaussées séparées soutenues par un OA](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/etude_impacts_loi_3ds_voirie/etude_impacts_loi_3ds_voirie-oa.png "Chaussées séparées soutenues par un OA"){: loading=lazy }

Pour contourner ce cas, j'utilise plutôt la fonction [`ST_ClusterWithin`](https://postgis.net/docs/ST_ClusterWithin.html).

Son fonctionnement est équivalent mais les géométries sont cette fois agrégées dès lors qu'elles sont à moins d'une distance donnée.

J'ai fixé de façon empirique cette distance à 25 mêtres dans les requêtes qui suivent. La mesure doit être suffisante pour raccrocher les chaussées séparées mais pas trop importante pour ne pas associer à tord deux ouvrages qui seraient proches.

Requête de comptage des ponts :

```SQL
select cpx_numero as "RN", array_length(ST_ClusterWithin(geometrie, 25), 1) as "Nb. ouvrages"
from bdtopo_troncon_de_route
where cpx_classement_administratif = 'Nationale'
and (insee_commune_droite ~ '^30' or insee_commune_gauche ~ '^30')
and position_par_rapport_au_sol ~ '^(Gué ou radier|[1-9])'
group by cpx_numero
order by 1;
```

Requête de comptage des tunnels :

```SQL
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

Plus que les distances, il est surtout intéressant de mesurer l'évolution du linéaire que cela représente.

Pour cela, je reprends la requête de calcul des longueurs par nature et nombre de voies, vue plus haut, que j'applique aux routes nationales et aux routes départementales.

Je mets face à face les chiffres obtenus à l'aide d'un `full join` (c'est à dire l'équivalent d'un `right join` et d'un `left join` combinés).

Je peux ensuite calculer le ratio en prennant soin de gérer les cas aux limites (division par null et 0) notamment à l'aide de la fonction [`coalesce`](https://www.postgresql.org/docs/current/functions-conditional.html#FUNCTIONS-COALESCE-NVL-IFNULL).

Enfin j'ordonne le résultat dans l'ordre décroissant des valeurs ce qui donne la requête suivante :

```SQL
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

## Bilan

En conclusion, on peut voir qu'il est assez rapide de produire quelques indicateurs routiers à l'aide de la BDTopo IGN et grâce au couple PostgreSQL/PostGIS.

Les ratios obtenus avec la dernière requête peuvent être appliqués aux ressources financières et humaines actuelles pour en déduire les besoins futurs.

Ce que j'apprécie avec ce type d'analyse c'est que d'une donnée géographique sont déduits plusieurs indicateurs...preuve que la géomatique ne se limite pas à la cartographie.

## Auteur

--8<-- "content/team/mgal.md"