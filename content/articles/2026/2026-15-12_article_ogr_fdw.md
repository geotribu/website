---
title: Gérer la bdtopo avec PostgreSQL et ogr_fdw
subtitle: Better CALL bdtopo
authors:
  - Thomas Szczurek-Gayant
categories:
  - article
comments: true
date: 2026-12-15
description: "Récupérer et mettre à disposition la bdtopo dans PostgreSQL et QGIS grâce au Foreign DATA WRAPPER ogr_fdw, soit la partie vectorielle de GDAL."
icon: simple/postgresql
image:
license: default
robots: index, follow
tags:
  - bdtopo
  - GDAL
  - Postigs
  - WFS
  - FDW
---

# Gérer la BdTopo avec ogr FDW

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![logo IGN](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/ign.png){: .img-thumbnail-left }

Gérer les données de référence (comme la bdtopo de l'IGN) dans une structure relève souvent du casse-tête.

- "Quand est-ce qu'on a téléchargé le fichier la dernière fois ?"
- "Il y a deux ans"

- "Ah, toi aussi tu l'as téléchargé ? Et l'ensemble du service aussi ?"
- "C'est marrant, l'infra vient de nous dire qu'il y a plus d'eurossous pour racheter des baies de stockage."

Et autres joyeusetés.

Passer par des flux WFS n'est pas non plus une solution toujours pratique. Essayez de lire la couche des batiments de la bdtopo à l'échelle d'une métropole si vous n'êtes pas convaincus.

## Un FDW, Kezako ?

![logo Postgis](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/postgis.png){: .img-thumbnail-left }

Dans le monde de PostgreSQL, un Foreign Data Wrapper (qu'on va raccourcir en FDW car vous ne voulez jamais avoir a prononcer ces mots en réunion plus d'une fois) consiste, comme son nom l'indique, en un *enveloppeur de données externes*, soit un outil qui va permettre de lire dans PostgreSQL des données externes *comme si elles y étaient*. Si vous êtes atteins de névroses profondes, vous pouvez approfondir dans le [Necronomicon](https://www.interdb.jp/pg/pgsql04/index.html).

Ces outils sont le plus souvent présents sous la forme d'extensions. Par défaut, POstgreSQL vient avec `postgres_fdw` qui permet de lire dans une base PostgreSQL des données provenant d'une autre base PostgreSQL, et `file_fdw` qui permet d'y lire des CSV. Mais il y en a énormement d'autres ! [liste non exhaustive](https://wiki.postgresql.org/wiki/Foreign_data_wrappers). Dans les "Exotic Wrappers" on notera la présence du mystérieux mais fascinant *Phillips Hue Lighting Systems*.

L'avantage d'un `FDW` par rapport à un `dblink`, c'est qu'ils n'ont pas besoins d'être rafraichis. Une modification dans la donnée source est directement visible dans la base cible.

Il se trouve que Paul Ramsay a développé [`ogr_fdw`](https://github.com/pramsey/pgsql-ogr-fdw). Soit un `FDW` capable de lire toute la partie vectorielle de `GDAL` (à l'exception notable du parquet). Soit la possibilité de faire un `FDW` sur des flux `WFS`, et ainsi de pouvoir créer, en quelque sorte, une `vue matérialisée` sur les dits flux. Celle-ci servira alors de tampon entre le flux et QGIS pour la lecture tout en pouvant se mettre à jour très facilement.

Et si on faisait ça sur toute la bdtopo ?

## Installation

![logo Outil technique](https://cdn.geotribu.fr/img/logos-icones/divers/outils.png){: .img-thumbnail-left }

Sur Fenêtres, l'extension semble être disponible via StackBuilder, mais je n'ai utilisé ce truc qu'une seule fois dans ma vie il y a des années donc je n'irai pas m'aventurer à expliquer quoi que ce soit.

Le cas étrange du SIG sur Apple ne sera pas non plus détaillé.

On rappelera donc que l'habitat naturel de l'éléphant bleu est Linux. Et comme toutes les espèces protégées, prière de le laisser dans son habitat naturel.

*oui FreeBSD on sait. S'il te plait ne nous déconcentre pas*.

`ogr_fdw` est présent dans le dépôt PGDG qui sert à intaller l'animal correctement comme expliqué pour Débian et dériviées [ici](https://www.postgresql.org/download/linux/debian/) ou [ici](https://www.postgresql.org/download/linux/redhat/) chez RedHat. Postgis devra lui aussi être installé.

Donc, si le dépôt est bien enregistré, la suite est simple :

```sh
sudo apt install ogr_fdw # sous Debian et dérivés

sudo dnf install ogr_fdw # sous RedHat et dérivés
```

J'en profite pour glisser un article de blog pour celles et ceux qui aiment parfaire leurs installation de PostgreSQL [ici](https://blog.dalibo.com/2024/06/07/lp1.html).

Puis, une fois connecté avec un compte super-utilisateur PostgreSQL sur une base où Postgis est installé :

```sql
CREATE EXTENSION ogr_fdw;
```

On peut aussi installer ça via pgdadmin.

![illustration de la création de l'extension via pgdamin](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/ogr_fdw/img1_create_extension.png){: .img-center loading=lazy }

## Création du serveur

![logo WEB](https://cdn.geotribu.fr/img/logos-icones/divers/web.png){: .img-thumbnail-left }

```sql
CREATE SERVER geoplateforme_ign
    FOREIGN DATA WRAPPER ogr_fdw
    OPTIONS (
        datasource 'WFS:https://data.geopf.fr/wfs?SERVICE=WFS&VERSION=2.0.0&COUNT=100&STARTINDEX=0&BBOX=1.26,50.11,2.09,50.59,EPSG:4326',
        format 'WFS'
        );
```

Voilà.

...
...

On rigole comme on peut.

Pour pouvoir utiliser un `FDW` PostgreSQL a besoin d'un `foreign server` qui servira de pont entre la donnée source et la base de données. Cette commande permettant de créer ce dernier.

- CREATE SERVER : nom qu'on veut lui donner
- FOREIGN DATA WRAPPER : nom du FDW qu'il utilisera (donc ici ogr_fdw, le nom de l'extension une fois installée dans PostgreSQL)

![position du nom de l'extension dans pgadmin](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/ogr_fdw/img2_liste_extension.png){: .img-center loading=lazy }

- datasource : la source donnée (ici le serveur WFS de l'IGN)
  - - &COUNT=100&STARTINDEX=0 permet de paginer les requêtes de 100 en 100 pour éviter de demander trente douzes mille milliards d'objets en même temps
  - - &BBOX= : coins inférieur gauche / supérieur droit du rectangle englobant sur lequel on veut limiter notre requête pour éviter de récupérer la France entière.
  - - spécifité `d'ogr_fdw`, il faut préciser `format` qui indique quel pilote GDAL on veut utiliser.

Comme tout Geomaticien qui se respecte je confonds toujours la latitude et la longitude. Ou bien ça n'est que moi. Pour cette bbox je vous laisse donc tester l'ordre des X et des Y (ici il s'agit de la Baie de Somme qui est un coin très très chouette à visiter).

## Création des Foreign Tables et des vues matérialisées

Maintenant, créons un shéma nommé `ign` qui stockera toutes nos données.

```sql
CREATE SCHEMA ign;
```

Les données provenant d'un `FDW` sont stockées dans des objets nommées `tables étrangères`. Il existe une commande [`IMPORT FOREIGN SCHEMA`](https://docs.postgresql.fr/10/sql-importforeignschema.html) mais que l'on utilisera pas ici pour éviter d'importer **l'ensemble** des données contenues sur <https://data.geopf.fr/>. Donc on s'arme de courage et on se prépare a traiter les 54 tables de la bdtopo individuellement. Attention a bien utiliser le type de géométrie d'origine.

Consulter une `table étrangère` c'est requêter la données source, qui nous ramène ici au même problème que de consulter le flux directement. On va donc créer une `vue matérialisée` (et donc avec les données écrites sur disque contrairement a une simple `vue`) sur la `table étrangère` qui servira de tampon pour la consultation de la donnée, et que l'on pourra indexer spatialement et reprojeter en 2154.

```sql
BEGIN;

-- Création de la foreign table

DROP FOREIGN TABLE IF EXISTS ign.ft_bdtopo_arrondissements;
CREATE FOREIGN TABLE IF NOT EXISTS ign.ft_bdtopo_arrondissements(
    cleabs text,
    nom_officiel text,
    code_insee_de_l_arrondissement text,
    numero_de_l_arrondissement text,
    code_insee_du_departement text,
    code_insee_de_la_region text,
    liens_vers_autorite_administrative text,
    date_creation timestamp,
    date_modification timestamp,
    date_d_apparition date,
    date_de_confirmation date,
    geom geometry(MultiPolygon,4326)
)
    SERVER geoplateforme_ign
    OPTIONS (layer 'BDTOPO_V3:arrondissement');

-- Création de la vue matérialisée

DROP MATERIALIZED VIEW IF EXISTS ign.vm_bdtopo_arrondissements;
CREATE MATERIALIZED VIEW IF NOT EXISTS ign.vm_bdtopo_arrondissements
AS
  SELECT
    cleabs,
    st_transform(geom,2154) AS geom,
    nom_officiel,
    code_insee_de_l_arrondissement,
    numero_de_l_arrondissement,
    code_insee_du_departement,
    code_insee_de_la_region,
    liens_vers_autorite_administrative,
    date_creation,
    date_modification,
    date_d_apparition,
    date_de_confirmation
  FROM ign.ft_bdtopo_arrondissements
WITH DATA;

-- Création des indexs

DROP INDEX IF EXISTS ign.idx_ign_bdtopo_arrondissements_geom;
CREATE INDEX IF NOT EXISTS idx_ign_bdtopo_arrondissements_geom ON ign.vm_bdtopo_arrondissements USING gist (geom);

COMMIT;
END;
```

Lors de la création de la table étrangère, il faut passer deux options spécifiques :

- SERVER : le `foreign server` que l'on a créé précédemment.
- OPTIONS : des options spécifiques au `FDW` ou au pilote GDAL. Ici, il s'agit du nom de la table sur <https://data.geopf.fr/>.

Et on peut indiquer en commentaire la date de création pour conserver l'information :

```sql
-- Pour utiliser une fonction dans un commentaire il faut passer par un bloc de code SQL

DO $$
BEGIN
    EXECUTE format(
        'COMMENT ON MATERIALIZED VIEW ign.vm_bdtopo_arrondissements IS %L',
        'Créé le ' || current_date
    );
END
$$;
```

Enfin, on va attribuer des droits à un groupe utilisateur sur la `vue matéralisée` afin que ces derniers puissent la consulter dans QGIS, mais sans voir la `foreign table` associée qui restera proprété du super-utilisateur l'ayant créé uniquement.

```sql
GRANT SELECT ON TABLE ign.vm_bdtopo_arrondissements TO "utilisateurs";
```

Pour le déroulé on ne prends qu'une table qu'une table pour l'exemple mais au cazou, si certains ou certaines sont interessées, comme je suis un être humain vous trouverez à la fin de l'article le script complet pour toutes les tables.

## Création de la procédure

Nous avons une `table étrangère` qui sert de pont avec le flux `WFS`, une `vue matéralisée` qui sert pour la consultation. Il ne reste qu'à simplifier l'actualisation de tout ceci.

Pour rappel, chaque consultation de la `table étrangère` va lancer un appel sur le flux. Un rafraichissement de la `vue matérialisée` va lui lancer une consultation de son script de création, et donc du `SELECT` sur la `table étrangère`. On va donc créer une précédure qui lancera le rafraichissement de l'ensemble des vues matérialisées créées.

```sql
CREATE OR REPLACE PROCEDURE ign.bdtopo_maj()
LANGUAGE plpgsql
AS $$
BEGIN
    RAISE NOTICE 'Refresh de ign.vm_bdtopo_arrondissements...';
    REFRESH MATERIALIZED VIEW ign.vm_bdtopo_arrondissements;
    EXECUTE format(
        'COMMENT ON MATERIALIZED VIEW ign.vm_bdtopo_arrondissements IS %L',
        'Créé le ' || current_date
    );
    COMMIT;
    RAISE NOTICE 'Refresh de ign.vm_bdtopo_arrondissements_municipaux...';
    REFRESH MATERIALIZED VIEW ign.vm_bdtopo_arrondissements_municipaux;
    EXECUTE format(
        'COMMENT ON MATERIALIZED VIEW ign.vm_bdtopo_arrondissements IS %L',
        'Créé le ' || current_date
    );
    COMMIT;

-- Bis repetita par table

    END;
$$;

COMMIT;
```

Ici, il faudra attendre que le rafraichissement soit terminé avant qu'une autre transaction puisse être validée, mais il est possible d'ajouter le mot clé `CONCURENTLY` à la fin de :

> REFRESH MATERIALIZED VIEW ign.vm_bdtopo_arrondissements

Pour permettre les transactions concurentes. Mais attention, ça ralonge le temps de refraichissement

Et voilà, nos données issus des flux de l'IGN sur le périmètre sont consultables dans QGIS avec un temps d'affichage de ~2/3 secondes pour l'entièté de la zone. Et on a même une information dans l'infobulle sur la date de création /  dernière mise à jour de la donnée.

![illustration de l'affichage dans QGIS de la couche des bâtiments](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/ogr_fdw/img3_final.png){: .img-center loading=lazy }

### Mises à jour

Pour raffraichir nos 54 vues matérialisée et donc la donnée, il ne suffira plus qu'à lancer

```sql
CALL ign.bdtopo_maj();
```

Attention ça peut prendre 1 ou 2 heures à cette échelle, mais le flux n'est évidemment pas mit à jour sur une temporalité où cela soit pénalisant.

On peut même imaginer un job `cron` ou `pgcron` qui lancera automatiquement ce `CALL` régulièrement (ou autre outil d'orchestration).

Et enfin, voici le script complet [ici](https://gitlab.com/-/snippets/6093205) !

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-nc-sa.md" %}
