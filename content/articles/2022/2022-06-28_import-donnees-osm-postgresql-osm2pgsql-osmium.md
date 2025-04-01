---
title: Importer des données OSM dans PostgreSQL
subtitle: Installation, configuration, import
authors:
    - Julien MOURA
categories:
    - article
    - tutoriel
comments: true
date: 2022-06-28
description: Guide détaillé pour installer et configurer PostgreSQL, PostGIS et importer des données OpenStreetMap à l'aide d'osm2pgsql et Osmium.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/postgis_osm_setup/marche_elephants_osm_postgres.png
license: default
robots: index, follow
tags:
    - OpenStreetMap
    - osm2pgsql
    - Osmium
    - PostGIS
    - PostgreSQL
---

# Importer les données OpenStreetMap dans PostGIS : un guide détaillé pas à pas

:calendar: Date de publication initiale : 28 juin 2022

Prérequis :

- des droits d'installation
- de préférence un PC sous Linux Debian/Ubuntu (ou via [WSL](../2020/2020-10-28_gdal_windows_subsystem_linux_wsl.md)). Les outils utilisés sont tous disponibles sur Windows, MacOS et même FreeBSD, c'est vous dire !

## Introduction

![logo PostgreSQL](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/postgresql.svg "logo PostgreSQL"){: loading=lazy .img-thumbnail-left }

Dans les tutoriaux d'ici ou d'ailleurs, on part souvent du principe que l'on dispose naturellement d'une base de données PostgreSQL/PostGIS tout bien configurée comme il faut avec, en prime, des données chargées et prêtes à être manipulées comme il se doit, souvent issues d'OpenStreetMap.

C'est justement en voulant rédiger un de ces tutoriaux et en constatant que je refaisais systématiquement le même _setup_ que je me suis dit que ça serait intéressant de le consigner ici. Comme ça, je pourrai y retrouver mes commandes habituelles et y faire référence dans d'autres tutoriels.

Au menu :

1. Installer PostgreSQL, ses extensions et configurer tout ce beau monde
1. Installer les outils d'import ([osm2pgsql]) et de pré-traitement ([Osmium]) des données OSM
1. Découper et importer les données dans la base
1. Se créer la connexion dans ArqGIS

Compagniiiie... en mesure !

![Marche des Eléphants Postgres](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/postgis_osm_setup/marche_elephants_osm_postgres.png "Marche des Eléphants Postgres"){: loading=lazy .img-center }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Installer et configurer PostgreSQL

<!--
    Syntaxe spéciale pour qu'une seule image ne s'affiche selon le thème clair ou sombre
    Voir : https://squidfunk.github.io/mkdocs-material/reference/images/#light-and-dark-mode
  -->

![logo Grand Eléphant des Machines de l'île de Nantes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/postgis_osm_setup/machines_nantes_grand_elephant_icon_white.svg#only-dark "logo Grand Eléphant des Machines de l'île de Nantes"){: loading=lazy .img-thumbnail-left }
![logo Grand Eléphant des Machines de l'île de Nantes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/postgis_osm_setup/machines_nantes_grand_elephant_icon_black.svg#only-light "logo Grand Eléphant des Machines de l'île de Nantes"){: loading=lazy .img-thumbnail-left }

Installer PostgreSQL n'a rien de sorcier, tant le travail de packaging et de distribution est remarquablement réalisé et documenté, comme en témoigne [la page de téléchargement](https://www.postgresql.org/download/). Mais c'est toujours bon de se noter les commandes à utiliser pour installer les versions depuis les dépôts communautaires.

Par exemple, sur les distributions Linux Debian comme Ubuntu :

```sh
# quelques dépendances communes
sudo apt install curl gpg gnupg2 software-properties-common apt-transport-https lsb-release ca-certificates
# on télécharge et on inscrit la clé permettant de certifier la provenance des paquets logiciels
curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
# on référence le dépôt communautaire dans les sources logicielles du système
echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list
# on installe PostgreSQL et PostGIS
sudo apt install postgresql-14 postgresql-client-14 postgresql-14-postgis-3
```

En revanche, le packaging de PostgreSQL sur Debian et Ubuntu intègre des scripts de post-installation qui créent par défaut un cluster `main`. C'est sympa de faire une partie du taf mais ce serait plus correct de demander avant quand même, en plus, le cluster n'est même pas optimisé !  
Quand je fais installer un four en terre chez moi, je ne m'attends pas à ce que l'artisan me fasse un calzone mal cuite juste après la dernière pierre posée ! :pizza:

![Pizza dans son four](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/pizza_four.webp "Pizza dans son four"){: loading=lazy .img-center }

### Création d'un cluster optimisé

![Grappe de Chanaan](https://cdn.geotribu.fr/img/logos-icones/divers/grappe_raisin_chanaan.webp "Grappe de Chanaan"){: loading=lazy .img-thumbnail-left }

On prend donc l'habitude de refaire la pâte nous-même. C'est parti pour la création d'un cluster aux ~~petits oignons~~ petites olives !

On commence par lister les clusters (grappes en bon français) existants avec l'utilitaire fourni dans le paquet `postgresql-common` :

```bash
> pg_lsclusters
Ver Cluster Port Status Owner    Data directory              Log file
14  main    5432 online postgres /var/lib/postgresql/14/main /var/log/postgresql/postgresql-14-main.log
```

L'objectif est donc de créer un cluster dédié avec des paramètres optimisés pour les tâches souhaitées (import de données OSM) et par rapport à l'ordinateur utilisé (dans mon cas, un Dell XPS 15 7590 avec un Intel Core i7-9750H de 9e génération - voir la [fiche technique](https://www.dell.com/support/manuals/fr-fr/xps-15-7590-laptop/xps-15-7590-setup-and-specifications/processeurs?guid=guid-bfa52f40-8ad1-4df0-8d0f-942766bc2118&lang=fr-fr)).

Pour cela, on va s'appuyer sur deux éléments :

- la [documentation d'osm2pgsql](https://osm2pgsql.org/doc/manual.html#tuning-the-postgresql-server) qui recommande des paramètres de configuration
- les outils comme [PGTune](https://pgtune.leopard.in.ua/) ou [Cybertec Postgres Configurator](http://pgconfigurator.cybertec.at/) qui permettent de générer une configuration "_good enough_" selon les capacités de la machine et le type d'application

![PGTune - Dell XPS 15 7590](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/postgis_osm_setup/pgtune_dell-xps-15-7590_osm_data.png "PGTune - Dell XPS 15 7590"){: .img-center loading=lazy}

C'est parti, on crée un cluster `osmdata` en passant directement les options qui nous intéressent.

```bash title="Commande multi-ligne pour créer un cluster PostgreSQL"
sudo pg_createcluster 14 osmdata \
--port=54342 \
--pgoption autovacuum_work_mem='2GB' \
--pgoption checkpoint_completion_target='0.9' \
--pgoption checkpoint_timeout='60min' \
--pgoption default_statistics_target='500' \
--pgoption effective_cache_size='10GB' \
--pgoption effective_io_concurrency='200' \
--pgoption maintenance_work_mem='10GB' \
--pgoption min_wal_size='4GB' \
--pgoption max_connections='40' \
--pgoption max_wal_size='12GB' \
--pgoption max_worker_processes='10' \
--pgoption max_parallel_workers_per_gather='6' \
--pgoption max_parallel_workers='10' \
--pgoption max_parallel_maintenance_workers='4' \
--pgoption max_wal_senders='0' \
--pgoption random_page_cost='1.1' \
--pgoption shared_buffers='1GB' \
--pgoption wal_buffers='16MB' \
--pgoption wal_level='minimal' \
--pgoption work_mem='50MB' \
-- --data-checksums --lc-messages=C --auth-host=scram-sha-256 --auth-local=peer
```

A noter :

- j'abaisse volontairement certaines valeurs pour garder la main sur mon interface graphique et qu'en cas de valeurs différentes entre PGTune et osm2pgsql, j'ai choisi de donner la priorité à ce dernier
- le port doit être différent de ceux déjà utilisés par les autres clusters. Pour me faciliter la mémoire, j'aligne toujours le 4ème chiffre avec l'unité de la version de PostgreSQL et j'ajoute un 5ème pour incrémenter les clusters. Ici, ça donne donc `54342`.
- on fait la différence entre les options qui s'appliquent au cluster (`--pgoption`) et celles qui s'appliqueront à toute création de base de données (`initdb`) dans ce cluster (qui se situent à la fin, après `--`). Ici, il s'agit de paramètres d'intégrité et de sécurité recommandés habituellement (notamment par Dalibo).

Si vous êtes curieux/se, vous pouvez dérouler le détail de ce que la commande retourne.

<!-- markdownlint-disable MD046 -->
??? example "Le détail de l'exécution sur ma machine"

    ```bash
    Creating new PostgreSQL cluster 14/osmdata ...
    /usr/lib/postgresql/14/bin/initdb -D /var/lib/postgresql/14/osmdata --no-instructions --data-checksums --lc-messages=C --data-checksums --lc-messages=C --auth-host=scram-sha-256 --auth-local=peer
    Les fichiers de ce système de bases de données appartiendront à l'utilisateur « postgres ».
    Le processus serveur doit également lui appartenir.

    L'instance sera initialisée avec les locales
    COLLATE:  fr_FR.UTF-8
    CTYPE:    fr_FR.UTF-8
    MESSAGES: C
    MONETARY: fr_FR.UTF-8
    NUMERIC:  fr_FR.UTF-8
    TIME:     fr_FR.UTF-8
    L'encodage par défaut des bases de données a été configuré en conséquence
    avec « UTF8 ».
    La configuration de la recherche plein texte a été initialisée à « french ».

    Les sommes de contrôle des pages de données sont activées.

    correction des droits sur le répertoire existant /var/lib/postgresql/14/osmdata... ok
    création des sous-répertoires... ok
    sélection de l'implémentation de la mémoire partagée dynamique...posix
    sélection de la valeur par défaut pour max_connections... 100
    sélection de la valeur par défaut pour shared_buffers... 128MB
    sélection du fuseau horaire par défaut... Europe/Paris
    création des fichiers de configuration... ok
    lancement du script bootstrap...ok
    exécution de l'initialisation après bootstrap... ok
    synchronisation des données sur disque... ok
    Ver Cluster Port  Status Owner    Data directory                 Log file
    14  osmdata 54342 down   postgres /var/lib/postgresql/14/osmdata /var/log/postgresql/postgresql-14-osmdata.log
    ```
<!-- markdownlint-enable MD046 -->

Enfin, on démarre l'instance :

```bash
sudo systemctl start postgresql@14-osmdata
# ou
sudo pg_ctlcluster 14 osmdata start
```

Et voilà, on a notre PostgreSQL proprement installé et configuré sur notre machine !

![Croquis du Grand Eléphant des machines de l'île de Nantes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/postgis_osm_setup/machines_nantes_grand_elephant_croquis.webp "Croquis du Grand Eléphant des machines de l'île de Nantes"){: .img-center loading=lazy}

#### Changer la configuration du cluster plus tard

Il est évidemment possible de changer les paramètres du cluster par la suite, soit via une instuction SQL `ALTER SYSTEM`, soit en éditant le `postgresql.conf` :

```bash
sudo nano /etc/postgresql/14/osmdata/postgresql.conf
# puis redémarrer le serveur - généralement un reload peut suffire mais là on joue à domicile donc on doit pouvoir supporter la coupure de service
sudo systemctl restart postgresql@14-osmdata
```

!!! tip "Astuce pour avoir une Calzone réussie à chaque installation"
    Il est aussi possible de changer le comportement des scripts de post-installation du packaging PostgreSQL en modifiant le fichier `/etc/postgresql-common/createcluster.conf`, soit pour désactiver la création automatisée du cluster `main`, soit pour en modifier les paramètres par défaut (par exemple avec `initdb_options = '--data-checksums --lc-messages=C'`).

### Créer le rôle et gérer l'accès

Comme on travaille à la maison, on va se faciliter la vie et créer un rôle en base correspondant à notre utilisateur système (trouvable avec la commande `whoami` pour que la commande reste générique) de façon à utiliser le mode d'authentification `peer` :

```bash
sudo -u postgres createuser -p 54342 --createdb --pwprompt --superuser "$(whoami)"
```

De façon à ne pas stocker de mot de passe en clair dans les applications clientes comme ArqGIS et pour se faciliter la vie, on se crée un fichier `.pgpass` dans le répertoire personnel de l'utilisateur :

```bash
echo "localhost:54342:*:$(whoami):motdepasse_assigne_a_mon_utilisateur" >> ~/.pgpass
```

Dans la foulée, on change les permissions de ce fichier `.pgpass` pour en [limiter les accès en lecture et écriture à l'utilisateur](https://chmodcommand.com/chmod-0600/) - sans quoi le fichier sera ignoré :

```bash
chmod 0600 ~/.pgpass
```

De même, de façon à garder la connexion la plus générique possible dans le but de rendre la suite le plus facilement reproductible possible, on stocke les paramètres de connexion dans le fichier `PGSERVICE` (voir [la doc officielle de PostgreSQL](https://www.postgresql.org/docs/current/libpq-pgservice.html) et [celle de ArqGIS](https://docs.qgis.org/3.22/fr/docs/user_manual/managing_data_source/opening_data.html#pg-service-file)) :

- emplacement par défaut : `~/.pg_service.conf` (Linux) ou `%APPDATA%/postgresql/.pg_service.conf` (Windows)
- ou personnalisable via une variable d'environnement `PGSERVICEFILE` pointant sur le fichier directement (nommage libre) ou `PGSYSCONFDIR` pointant sur le répertoire où trouver le fichier (qui doit forcément être nommé `pg_service.conf`)

```ini
[local_osmdata]
dbname=osm
host=localhost
port=54342
```

!!! note "pg_service_all_inclusive"
    Il est également possible de stocker directement le mot de passe dans le `.pg_service.conf` pour se simplifier encore plus la vie, mais personnellement j'aime que les mots de passe soient dans un fichier séparé de façon à pouvoir diffuser mon `.pg_service.conf` tranquillement.

### Créer et configurer la base de données

![logo PostGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/postgis.png "logo PostGIS"){: loading=lazy .img-thumbnail-left }

Créer la base de données que l'on nomme `osm` :

```bash
createdb --owner $(whoami) --port 54342 --encoding=UTF8 osm
```

S'y connecter pour tester puis ressortir :

```bash
> psql -p 54342 -U $(whoami) osm
psql (14.3 (Ubuntu 14.3-1.pgdg20.04+1))
Saisissez « help » pour l'aide.

osm=# \q
>
```

Activer PostGIS :

```bash
psql -p 54342 -U $(whoami) osm -c "CREATE EXTENSION postgis;"
```

Activer HSTore :

```bash
psql -p 54342 -U $(whoami) osm -c "CREATE EXTENSION hstore;"
```

## Installer les outils liés à OpenStreetMap

C'est dans ces moments-là où on mesure combien le projet est remarquable à plus d'un titre. Au-delà de la dimension collaborative et de la base de données, c'est aussi tout l'outillage disponible et "naturellement" maintenu qui fait d'OSM une réussite incontournable de notre écosystème.

### Installer osm2pgsql

Afin d'importer les données OpenStreetMap dans PostgreSQL, on utilise [osm2pgsql](?q=osm2pgsql*) qui est un outil en ligne de commande maintenu par la communauté OSM. Pour l'installation, rien de plus simple pour Debian et dérivés comme Ubuntu :

```sh
sudo apt install osm2pgsql
```

Sur Windows, le [tutoriel de LearnOSM](https://learnosm.org/en/osm-data/osm2pgsql/) est très bien !

- Oui, une question Joséphine ?
- Monsieur, il est en anglais votre tuto et dans plein d'autres langues sauf en Français !
- Mon ange, c'est une excellente remarque que vous faites là ! C'est justement l'occasion de vous proposer pour contribuer à la traduction de ce merveilleux support !
- Ah ouais, bonne idée, ça me fera un bon exercice pour travailler la [version en anglais](https://www.edulide.fr/blog/reussir-version-anglais/) !

[Faites chauffer DeepL et Transifex pour contribuer à LearnOSM :fontawesome-solid-language:](https://learnosm.org/en/contribute/translator/){: .md-button }
{: align=middle }

### Installer osmium

Là encore, tout est packagé comme il faut pour notre distribution préférée pour installer [Osmium] facilement :

```sh
sudo apt install osmium-tool
```

----

## Les données

### Télécharger OSM sur la Belgique

![logo OpenStreetMap](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/Openstreetmap.png "logo OpenStreetMap"){: loading=lazy .img-thumbnail-left }

Franchement on va pas se mentir : si Napoléon avait eu les données OpenStreetMap, on aurait moins de [problèmes de borne](https://www.lavoixdunord.fr/992266/article/2021-04-27/bousignies-sur-roc-il-deplace-une-borne-frontiere-et-viole-le-traite-de-courtrai) (de frontières, pas de ministre) de nos jours ! :smile:

Un petit tour par GeoFabrik pour télécharger les données de la Belgique : <https://download.geofabrik.de/europe/belgium.html>.

On peut également utiliser un outil en ligne de commande, par exemple `wget` avec l'option `-N` qui permet de télécharger uniquement si le fichier distant (ici le serveur GeoFabrik) est plus récent par rapport à la version locale (sur votre machine) :

```bash
wget -N https://download.geofabrik.de/europe/belgium-latest.osm.pbf -P /tmp/osmdata/belgium
```

<video width="100%" controls>
    <!-- markdownlint-disable MD033 -->
      <source src="https://cdn.geotribu.fr/img/articles-blog-rdp/articles/postgis_osm_setup/wget_osm_geofabrik_belgium.webm" type="video/webM">
      Votre navigateur ne supporte pas la balise video HTML 5.
      <!-- markdownlint-enable MD033 -->
</video>

### Découper les données

![logo Osmium Tool](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/osmium.svg "logo Osmium Tool"){: loading=lazy .img-thumbnail-left }

Si on craint de manquer d'espace disque, de puissance ou qu'on cible une zone restreinte en particulier, on peut découper les données avec une emprise avant de les importer avec un outil comme Osmium par exemple.

Et on découpe sur la zone qui nous intéresse, par exemple Bruxelles :

```sh
osmium extract -b 4.29,50.815,4.47,50.90 /tmp/osmdata/belgium/belgium-latest.osm.pbf -o /tmp/osmdata/belgium/brussels.osm.pbf
```

### Importer des données

![logo osm2pgsql](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/osm2pgsql.png "logo osm2pgsql"){: loading=lazy .img-thumbnail-left }

La commande osm2pgsql semble facile mais il faut bien régler les options pour ne pas avoir d'erreur :

```bash
osm2pgsql --create --database osm --port 54342 --cache 1000 --number-processes 4 /tmp/osmdata/belgium/brussels.osm.pbf
```

Détail des options :

- `--create` : créer les données, quitte à les écraser si elles existent déjà dans la base
- `--database` : nom de la base de données
- `--port` : port de connexion à la base de données
- `--cache` : gère la taille du cache (en MB) à allouer pour l'import des noeuds OSM. Je pensais au début que la valeur par défaut (800) suffirait mais j'ai eu l'erreur : _Node cache size is too small to fit all nodes. Please increase cache size_. Dépend de la RAM de votre machine.
- `--number-processes` : nom de processus à utiliser pour paralléliser les tâches qui peuvent l'être

Pour celles et ceux que ça intéresse, voici le détail de l'exécution sur mon ordinateur qui a pris 187 secondes :

<!-- markdownlint-disable MD046 -->
??? example "Le détail de l'exécution sur ma machine"

    ```bash
    >  osm2pgsql --create --database osm --port 54342 --cache 1000 --number-processes 4 /tmp/osmdata/belgium/belgium-latest.osm.pbf
    osm2pgsql version 1.2.1 (64 bit id space)

    Allocating memory for dense node cache
    Allocating dense node cache in one big chunk
    Allocating memory for sparse node cache
    Sharing dense sparse
    Node-cache: cache=1000MB, maxblocks=16000*65536, allocation method=3
    Using built-in tag processing pipeline
    Using projection SRS 3857 (Spherical Mercator)
    Setting up table: planet_osm_point
    Setting up table: planet_osm_line
    Setting up table: planet_osm_polygon
    Setting up table: planet_osm_roads

    Reading in file: /tmp/osmdata/belgium/belgium-latest.osm.pbf
    Using PBF parser.
    Processing: Node(53962k 8993.7k/s) Way(8267k 145.05k/s) Relation(81920 11702.86/s)  parse time: 70s
    Node stats: total(53962322), max(9777797946) in 6s
    Way stats: total(8267595), max(1064657400) in 57s
    Relation stats: total(87197), max(14192617) in 7s
    node cache: stored: 53962322(100.00%), storage efficiency: 50.16% (dense blocks: 170, sparse nodes: 53094157), hit rate: 100.00%
    Sorting data and creating indexes for planet_osm_point
    Sorting data and creating indexes for planet_osm_line
    Sorting data and creating indexes for planet_osm_roads
    Sorting data and creating indexes for planet_osm_polygon
    Copying planet_osm_roads to cluster by geometry finished
    Creating geometry index on planet_osm_roads
    Copying planet_osm_point to cluster by geometry finished
    Creating geometry index on planet_osm_point
    Creating indexes on planet_osm_roads finished
    All indexes on planet_osm_roads created in 5s
    Completed planet_osm_roads
    Creating indexes on planet_osm_point finished
    All indexes on planet_osm_point created in 15s
    Completed planet_osm_point
    Copying planet_osm_line to cluster by geometry finished
    Creating geometry index on planet_osm_line
    Creating indexes on planet_osm_line finished
    Copying planet_osm_polygon to cluster by geometry finished
    Creating geometry index on planet_osm_polygon
    All indexes on planet_osm_line created in 44s
    Completed planet_osm_line
    Creating indexes on planet_osm_polygon finished
    All indexes on planet_osm_polygon created in 117s
    Completed planet_osm_polygon

    Osm2pgsql took 187s overall
    ```
<!-- markdownlint-enable MD046 -->

----

## Se connecter à la base

![logo ArqGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo ArqGIS"){: .img-thumbnail-left }

Maintenant que nos données sont bien au chaud dans la base, il est temps de s'y connecter et voir ce qu'elle a dans le ventre ! On peut déjà faire un petit listing des tables via la console `psql` :

```sh
> psql -p 54342 -U $(whoami) osm
psql (14.4 (Ubuntu 14.4-1.pgdg20.04+1))
Saisissez « help » pour l'aide.

osm=# \dt
                Liste des relations
 Schéma |        Nom         | Type  | Propriétaire
--------+--------------------+-------+--------------
 public | planet_osm_line    | table | jmo
 public | planet_osm_point   | table | jmo
 public | planet_osm_polygon | table | jmo
 public | planet_osm_roads   | table | jmo
 public | spatial_ref_sys    | table | jmo
(5 lignes)

osm=#
```

Pour s'y connecter avec ArqGIS, on va pouvoir tirer parti de notre [configuration d'authentification à l'aide du fichier pg_service.conf](#creer-le-role-et-gerer-lacces). Ainsi, seul le nom du service (= le nom de section entre `[]`) est nécessaire :

![ArqGIS - Connexion PostGIS avec service](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/postgis_osm_setup/qgis_connexion_postgis_pg_service.webp "ArqGIS - Connexion PostGIS avec service"){: .img-center loading=lazy}

Et voilà notre liste de tables :

![ArqGIS - Liste des tables PostGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/postgis_osm_setup/qgis_postgis_osm_listing.webp "ArqGIS - Liste des tables PostGIS"){: .img-center loading=lazy}

----

## Nettoyage

Voici les commandes si vous souhaitez supprimer le cluster créé pendant le tutoriel. Attention, cela supprimera toutes les données donc à n'exécuter que si vous êtes certain/e de ne pas y tenir :

```bash
sudo systemctl stop postgresql@14-osmdata
sudo pg_dropcluster 14 osmdata
```

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
