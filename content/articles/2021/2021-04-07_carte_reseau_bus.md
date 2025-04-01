---
title: Représentation d'un réseau de bus
authors:
    - Florian BORET
categories:
    - article
    - tutoriel
comments: true
date: 2021-04-07
description: Représenter un réseau de bus et gérer la superposition des lignes
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/reseau_bus_qgis/reseau_bus_osm.png
tags:
    - bus
    - PostGIS
    - PostgreSQL
    - ArqGIS
---

# Représentation d'un réseau de bus

:calendar: Date de publication initiale : 07 Avril 2021

Pré-requis :

- Maîtriser PostgreSQL et PostGIS
- Définir un style ArqGIS

## Intro

Fin 2020, une demande a émergé du service transport de ma collectivité qui souhaitait visualiser toutes les lignes de bus du territoire sur une même carte. De prime abord, cela ne me paraissait pas spécialement compliqué mais j'avais omis que plusieurs lignes pouvaient passer par des tronçons identiques et qu'il allait falloir gérer ces superpositions.  
Après avoir parcouru internet, je suis tombé sur une solution apportée par un utilisateur sur le forum [gis.stackexchange.com](https://gis.stackexchange.com/questions/197384/how-to-split-overlapping-linestrings) et je vous propose de revenir sur la mise en oeuvre de cette solution pour nos 5 lignes de bus.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Constitution du réseau de bus

Tout d'abord, créer une table dans PostgreSQL pour dessiner le réseau de bus :

```sql title="Création de la table des lignes de bus" linenums="1"
-- Création de la table bus_ligne
CREATE TABLE bus.bus_lignes
(
    id integer NOT NULL,
    geom geometry(LineString,2154),
    numero_ligne integer,
    CONSTRAINT bus_lignes_pkey PRIMARY KEY (id)
);
```

Ensuite, dessiner le réseau de bus en veillant à :

- bien superposer les tronçons des lignes de bus qui passent au même endroit
- ce que les tronçons qui se superposent soient numérisés dans le même sens

![Numérisation](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/reseau_bus_qgis/numerisation_qgis.png "Numérisation"){: loading=lazy }
{: align=middle }

Après la saisie, je vous conseille de faire des filtres sur le numéro de chaque ligne pour contrôler qu'il ne manque pas un tronçon et que lorsqu'il y a des superpositions vos tronçons vont dans le même sens.

## Créer des points de rencontre entre les lignes

Maintenant que les tronçons des lignes de bus ont été dessinés proprement (avec des superpositions), on va chercher à distinguer tous les points qui marquent :

- le début ou la fin d'un tronçon
- le début ou la fin d'une superposition

Pour ce faire, vous devez utiliser cette requête :

```sql title="Création de la table des points de rencontre" linenums="1"
-- Suppression de la table si elle existe
DROP TABLE IF EXISTS bus.bus_lignes_pt;
-- Création de la table
CREATE TABLE bus.bus_lignes_pt (
  id serial PRIMARY KEY,
  geom geometry(Point, 2154)
);

INSERT INTO bus.bus_lignes_pt (WITH ix AS
(
-- Intersection des lignes entre elles
  SELECT DISTINCT ST_Intersection(a.geom, b.geom) geom
  FROM bus.bus_lignes a JOIN bus.bus_lignes b ON ST_Intersects(a.geom, b.geom)
),
ix_simple_lines AS
(
-- Extraction des lignes simples
  SELECT
    (ST_Dump(ST_LineMerge(ST_CollectionExtract(geom, 2)))).geom geom
  FROM
    ix
)
-- Extraction des points de départ et d'arrivée
SELECT
  row_number() OVER() id,
  geom
FROM
(
  SELECT ST_StartPoint(geom) geom FROM ix_simple_lines
  UNION
  SELECT ST_EndPoint(geom) FROM ix_simple_lines
) points_union);
```

![Points de rencontre](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/reseau_bus_qgis/points_de_rencontre.png "Points de rencontre"){: loading=lazy }
{: align=middle }

## Découper les lignes de bus en tronçons

A partir des points qu'on a déterminé, on peut découper les lignes de bus en tronçons et en fonction du nombre de superpositions attribuer une valeur de décalage.

```sql title="Découper les lignes de bus en tronçons" linenums="1"
-- Suppression de la table si elle existe
DROP TABLE IF EXISTS bus.bus_lignes_offset;
-- Création de la table
CREATE TABLE bus.bus_lignes_offset (
    fid serial PRIMARY KEY,
    pt_from integer,
    loc_from numeric,
    pt_to integer,
    loc_to numeric,
    line_id integer,
    numero integer,
    offset_nr integer,
    geom geometry(Linestring, 2154)
);

INSERT INTO bus.bus_lignes_offset (WITH
a AS
(
-- Calcul de la position linéaire (loc) des points sur la ligne
  SELECT
    bus_lignes.id line_id,
    bus_lignes_pt.id pt_id,
    ST_LineLocatePoint(bus_lignes.geom, bus_lignes_pt.geom) loc
  FROM
    bus.bus_lignes
  JOIN
    bus.bus_lignes_pt ON ST_DWithin(bus_lignes.geom, bus_lignes_pt.geom, 4.0)
),
b AS
(
-- Calcul du départ et de l'arrivée des tronçons
  SELECT
    line_id,
    pt_id pt_from,
    loc loc_from,
    LEAD(pt_id) OVER w_b pt_to,
    LEAD(loc) OVER w_b loc_to
  FROM
    a
  WINDOW w_b AS (PARTITION BY line_id ORDER BY loc)
)
SELECT
  row_number() OVER() fid, -- Création d'un identifiant unique
  pt_from,
  loc_from,
  pt_to,
  loc_to,
  line_id,
  numero_ligne AS numero,
  row_number() OVER w_c offset_nr, --itération sur des lignes qui se chevauchent
  ST_CollectionExtract(ST_LineSubstring(bus_lignes.geom, loc_from, loc_to),2)::geometry(LineString, 2154) geom  -- Découpe les lignes en tronçons
FROM
  b
JOIN
  bus.bus_lignes ON b.line_id = bus_lignes.id
WHERE
  pt_to IS NOT NULL
WINDOW w_c AS (PARTITION BY pt_from, pt_to ORDER BY line_id, loc_from));
```

## Compter le nombre de lignes qui se chevauchent

La dernière étape consiste à compter le nombre de chevauchements pour chacun des tronçons.

```sql title="Compter les chevauchements" linenums="1"
-- Suppression de la table si elle existe
DROP TABLE IF EXISTS bus.bus_lignes_offset_count;
-- Création de la table
CREATE TABLE bus.bus_lignes_offset_count (
    fid serial PRIMARY KEY,
    pt_from integer,
    loc_from numeric,
    pt_to integer,
    loc_to numeric,
    line_id integer,
    numero integer,
    offset_nr integer,
    geom geometry(Linestring, 2154),
    pt_from2 integer,
    pt_to2 integer,
    count integer
);
INSERT INTO bus.bus_lignes_offset_count (
SELECT
    b.fid,
    b.pt_from,
    b.loc_from,
    b.pt_to,
    b.loc_to,
    b.line_id,
    b.numero,
    b.offset_nr,
    b.geom,
    a.pt_from,
    a.pt_to,
    a.count
FROM bus.bus_lignes_offset as b LEFT JOIN
(SELECT pt_from,
    pt_to,
    count(*) AS COUNT -- Compter le nombre de tronçons qui ont les mêmes points de départ et d'arrivée (rappel : les lignes doivent être dans le même sens)
FROM bus.bus_lignes_offset GROUP BY
    pt_from,
    pt_to) AS a ON a.pt_from = b.pt_from AND a.pt_to = b.pt_to);
```

## Le rendu ArqGIS

Pour terminer, vous pouvez ajouter la dernière table créée dans ArqGIS pour travailler sur le rendu :

1. Faire un style catégorisé sur le numéro de ligne et attribuer une couleur différente par ligne
2. Définir l'épaisseur des tronçons pour chacune des lignes

    ```sql title="Définir l'épaisseur des tronçons" linenums="1"
    CASE
        WHEN "count" = 2 THEN 1.2
        WHEN "count" > 2 THEN 0.8
        ELSE  1.6
    END
    ```

3. Définir le décalage pour chacune des lignes

    ```sql title="Définir le décalage des tronçons" linenums="1"
    CASE
        WHEN "count" = 2 THEN (("offset_nr"-1)*1.2)-((("count"-1)/2)*1.2)
        WHEN "count" > 2 THEN (("offset_nr"-1)*0.8)-((("count"-1)/2)*0.8)
        ELSE  0
    END
    ```

:warning: Attention si les tronçons qui se superposent ne vont pas dans le même sens, le décalage des lignes ne se fera pas correctement.

![Réseau de bus](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/reseau_bus_qgis/reseau_bus_osm.png "Réseau de bus"){: loading=lazy }
{: align=middle }

----

## Conclusion

La solution proposée permet :

- de gérer et de représenter sans trop de difficultés la superposition de plusieurs lignes de bus
- de relancer facilement les scripts si le réseau venait à évoluer

Toutefois, l’automatisation a ses limites et en l’état ce rendu ne pourrait être communiqué au grand public sans un travail graphique complémentaire.

A noter, que j'envisage de suivre la même démarche pour représenter nos itinéraires de randonnées alors si vous avez des remarques n'hésitez pas à laisser un commentaire.

----

<!-- geotribu:authors-block -->
