---
title: "FerrarGIS, une carte de Ferraris avec QGIS"
authors:
    - Julien MOURA
categories:
    - article
    - tutoriel
date: "2022-06-07 10:20"
description: "Description pour le SEO."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/export_aix_large.png"
license: default
tags:
    - cartographie
    - OpenStreetMap
    - osm2pgsql
    - Osmium
    - PostgreSQL
    - QGIS
---

<!-- TRUC UTILES A SUPPRIMER

[![image_title](image_url "image_title"){: .img-center loading=lazy}](image_url "image_title"){: data-mediabox="lightbox-gallery" data-title="image_title"}
 -->

# FerrarGIS, un style de carte de Ferraris (1777) avec QGIS

:calendar: Date de publication initiale : 7 juin 2022

Prérequis :

- QGIS > 3.20
- des droits d'installation
- de préférence un PC sous Linux (ou via [WSL](/articles/2020/2020-10-28_gdal_windows_subsystem_linux_wsl/)) mais l'ensemble des outils sont aussi disponibles sur Windows et MacOS

## Introduction

![logo Ferrari barré](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/ferrari_logo_barre.png "logo Ferrari barré"){: .img-rdp-news-thumb }

Au cours de mes pérégrinations de veille pour une revue de presse, je suis tombé sur [cet article](https://manuelclaeysbouuaert.be/projects/ferrargis.html) de [Manuel Claeys Bouuaert](https://manuelclaeysbouuaert.be/). Je ne connaissais pas la [carte [du comte Joseph] de Ferraris](https://fr.wikipedia.org/wiki/Carte_de_Ferraris) du coup j'étais content d'en apprendre davantage et j'ai trouvé que le rendu était très réussi.

Voyant que l'auteur [partage ses ressources sur GitHub](https://github.com/mclaeysb/FerrarGIS), j'essaie de voir rapidement ce que ça donne avant d'[écrire ma news](/contribuer/rdp/add_news/) pour la GeoRDP mais je me rends compte que ça ne se fait pas en 3 minutes et que ça mérite de s'y pencher plus en détails.  
L'occasion d'un petit tutoriel, non pas pour manipuler les styles de QGIS et briller dans les soirées mondaines de cartographes mais pour décrire pas à pas les étapes techniques nécessaires pour reproduire le super travail de l'auteur :

1. Installer et configurer PostgreSQL et ses extensions
1. Installer les outils d'import ([osm2pgsql]) et de pré-traitement ([Osmium]) des données OSM
1. Découper et import les données
1. Essayer et optimiser le projet et le style QGIS partagés

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Les outils

### Installer osm2pgsql

![logo osm2pgsql](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/osm2pgsql.png "logo osm2pgsql"){: .img-rdp-news-thumb }

Afin d'importer les données OpenStreetMap dans PostgreSQL, on va devoir utiliser [osm2pgsql](/?q=osm2pgsql*) qui est un outil en ligne de commande maintenu par la communauté OSM. Pour l'installation, rien de plus simple.

Sur Debian et dérivés comme Ubuntu :

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

### Installer et configurer PostgreSQL et ses extensions

![logo PostgreSQL](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/postgresql.png "logo PostgreSQL"){: .img-rdp-news-thumb }

Installer PostgreSQL n'a rien de sorcier, tant le travail de packaging et de distribution est remarquablement réalisé et documenté, comme en témoigne [la page de téléchargement](https://www.postgresql.org/download/). Mais c'est toujours bon de se noter les commandes à utiliser pour installer les versions depuis les dépôts communautaires.

Par exemple, sur les distributions Linux comme Ubuntu :

```sh
# quelques dépendances communes
sudo apt install curl gpg gnupg2 software-properties-common apt-transport-https lsb-release ca-certificates
# on télécharge et on inscrit la clé permettant de certifier la provenance des paquets logiciels
curl -fsSL https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo gpg --dearmor -o /etc/apt/trusted.gpg.d/postgresql.gpg
# on référence le dépôt communautaire dans les sources logicielles du système
echo "deb http://apt.postgresql.org/pub/repos/apt/ `lsb_release -cs`-pgdg main" | sudo tee /etc/apt/sources.list.d/pgdg.list
# on installe PostgreSQL
sudo apt install postgresql-14 postgresql-client-14 postgresql-14-postgis-3
```

Le truc avec le packaging de PostgreSQL sur Debian et Ubuntu c'est que les scripts de post-installation créent par défaut un cluster `main`. C'est sympa de faire une partie du taf mais ce serait plus correct de demander avant quand même, en plus, le cluster est même pas optimisé !  
Quand je fais installer un four en terre chez moi, je ne m'attends pas à ce que l'artisan me fasse une calzone mal cuite juste après la dernière pierre posée ! :pizza:

#### Création d'un cluster optimisé

C'est parti pour la création d'un cluster aux ~~petits oignons~~ petites olives ! On commence par lister les versions installées et les ports respectifs :

```bash
> grep -H '^port' /etc/postgresql/*/main/postgresql.conf
/etc/postgresql/12/main/postgresql.conf:port = 5432  # (change requires restart)
/etc/postgresql/14/main/postgresql.conf:port = 5434  # (change requires restart)
```

Ou :

```bash
> pg_lsclusters
Ver Cluster Port Status Owner    Data directory              Log file
12  main    5432 online postgres /var/lib/postgresql/12/main /var/log/postgresql/postgresql-12-main.log
14  main    5434 online postgres /var/lib/postgresql/14/main /var/log/postgresql/postgresql-14-main.log
```

L'idée c'est donc de créer un cluster dédié avec des paramètres optimisés pour les tâches souhaitées (import de données OSM) et par rapport à l'ordinateur utilisé (un Dell XPS 15 7590 avec un Intel Core i7-9750H de 9e génération - voir la [fiche technique](https://www.dell.com/support/manuals/fr-fr/xps-15-7590-laptop/xps-15-7590-setup-and-specifications/processeurs?guid=guid-bfa52f40-8ad1-4df0-8d0f-942766bc2118&lang=fr-fr)).

Pour cela, on va s'appuyer sur deux éléments :

- la [documentation d'osm2pgsql](https://osm2pgsql.org/doc/manual.html#tuning-the-postgresql-server) qui recommande des paramètres de configuration
- les outils comme [PGTune](https://pgtune.leopard.in.ua/) qui permettent de générer une configuration selon les capacités de la machine et le type d'application

[![PGTune - Dell XPS 15 7590](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/pgtune_dell-xps-15-7590_osm_data.png "PGTune - Dell XPS 15 7590"){: .img-center loading=lazy}](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/pgtune_dell-xps-15-7590_osm_data.png "PGTune - Dell XPS 15 7590"){: data-mediabox="lightbox-gallery" data-title="PGTune - Dell XPS 15 7590"}

C'est parti, on crée un cluster `ferrargis` en passant directement les options qui nous intéressent. Notez que je réduis certains paramètres pour garder la main sur mon interface graphique et qu'en cas de valeurs différentes entre PGTune et osm2pgsql, j'ai choisi de donner la priorité à ce dernier :

```bash
sudo pg_createcluster 14 ferrargis \
--port=5434 \
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
--pgoption random_page_cost='1.1' \
--pgoption shared_buffers='1GB' \
--pgoption wal_buffers='16MB' \
--pgoption wal_level='minimal' \
--pgoption wal_senders='0' \
--pgoption work_mem='50MB' \
-- --data-checksums --lc-messages=C --auth-host=scram-sha-256 --auth-local=peer
```

<!-- markdownlint-disable MD046 -->
??? example "Le détail de l'exécution sur ma machine"

    ```bash
    Creating new PostgreSQL cluster 14/ferrargis ...
    /usr/lib/postgresql/14/bin/initdb -D /var/lib/postgresql/14/ferrargis --no-instructions --data-checksums --lc-messages=C --data-checksums --lc-messages=C --auth-host=scram-sha-256 --auth-local=peer
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

    correction des droits sur le répertoire existant /var/lib/postgresql/14/ferrargis... ok
    création des sous-répertoires... ok
    sélection de l'implémentation de la mémoire partagée dynamique...posix
    sélection de la valeur par défaut pour max_connections... 100
    sélection de la valeur par défaut pour shared_buffers... 128MB
    sélection du fuseau horaire par défaut... Europe/Paris
    création des fichiers de configuration... ok
    lancement du script bootstrap...ok
    exécution de l'initialisation après bootstrap... ok
    synchronisation des données sur disque... ok
    Ver Cluster   Port Status Owner    Data directory                   Log file
    14  ferrargis 5434 down   postgres /var/lib/postgresql/14/ferrargis /var/log/postgresql/postgresql-14-ferrargis.log
    ```
<!-- markdownlint-enable MD046 -->

Il est évidemment possible de changer les paramètres du cluster par la suite, soit via une instuction sql `ALTER SYSTEM` soit en éditant le `postgresql.conf` :

```bash
sudo nano /etc/postgresql/14/main/postgresql.conf
# puis redémarrer le serveur
sudo systemctl restart postgresql@14-main
```

Démarrer l'instance :

```bash
sudo systemctl start postgresql@14-main
# ou
sudo pg_ctlcluster 14 main start
```

!!! tip "Astuce pour avoir une Calzone réussie à chaque installation"
    Il est possible de changer le comportement des scripts de post-installation du packaging PostgreSQL en modifiant le fichier `/etc/postgresql-common/createcluster.conf`, soit pour désactiver la création automatisée du cluster `main`, soit pour en modifier les paramètres par défaut (par exemple avec `initdb_options = '--data-checksums --lc-messages=C'`).

#### Créer le rôle et gérer l'accès

Création du rôle en base correspondant à l'utilisateur système (trouvable avec la commande `whoami`) de façon à utiliser le mode d'authentification `peer`) :

```bash
sudo -u postgres createuser -p 5434 --createdb --pwprompt --superuser "$(whoami)"
```

Ajout au `.pgpass` pour faciliter le travail :

```bash
echo "localhost:5434:*:$(whoami):motdepasse_assigned_a_mon_utilisateur" >> ~/.pgpass
```

Référencer la connexion au `.pg_service.conf` :

```ini
[local_ferrargis]
dbname=osm
host=localhost
port=5434
```

#### Créer la base de données

![logo PostGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/postgis.png "logo PostGIS"){: .img-rdp-news-thumb }

Créer la base de données :

```bash
createdb --owner $(whoami) --port 5434 --encoding=UTF8 osm
```

S'y connecter pour tester puis ressortir :

```bash
> psql -p 5434 -U $(whoami) osm
psql (14.3 (Ubuntu 14.3-1.pgdg20.04+1))
Saisissez « help » pour l'aide.

osm=# \q
>
```

Activer PostGIS :

```bash
psql -p 5434 -U $(whoami) osm -c "CREATE EXTENSION postgis;"
```

Activer HSTore :

```bash
psql -p 5434 -U $(whoami) osm -c "CREATE EXTENSION hstore;"
```

----

## Les données

### Télécharger OSM sur la Belgique

![logo OpenStreetMap](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/Openstreetmap.png "logo OpenStreetMap"){: .img-rdp-news-thumb }

Franchement on va pas se mentir : si Napoléon avait eu les données OpenStreetMap, on aurait moins de [problèmes de bornes](https://www.lavoixdunord.fr/992266/article/2021-04-27/bousignies-sur-roc-il-deplace-une-borne-frontiere-et-viole-le-traite-de-courtrai ) (de frontières, pas de ministre) de nos jours.

<https://download.geofabrik.de/europe/belgium.html>

On peut également utiliser un outil en ligne de commande, par exemple `wget` avec l'option `-N` qui permet de télécharger uniquement si le fichier distant (ici le serveur GeoFabrik) est plus récent par rapport à la version locale (sur votre machine) :

```bash
wget -N https://download.geofabrik.de/europe/belgium-latest.osm.pbf -P /tmp/osmdata/belgium
```

### Optionnel : découper les données

![logo Osmium Tool](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/osmium.svg "logo Osmium Tool"){: .img-rdp-news-thumb }

Si on craint de manquer d'espace disque, de puissance ou que vous ciblez une zone en particulier et qu'on ne souhaite pas charger une région ou un département entier pour rien, on peut découper les données avec une emprise avant de les importer avec un outil comme Osmium par exemple.

On installe [Osmium](https://osmcode.org/osmium-tool/) :

```sh
sudo apt install osmium-tool
```

Et on découpe sur la zone qui nous intéresse :

```bash
osmium extract -b 4.29,50.815,4.47,50.90 /tmp/osmdata/belgium/belgium-latest.osm.pbf -o /tmp/osmdata/belgium/brussels.osm.pbf
```

!!! tip "Vigilance"
    Du coup, le nom de fichier sera différent pour la commande d'import à suivre :wink: !

### Import des données

```bash
osm2pgsql --create --database osm --port 5434 --cache 1000 --number-processes 4 /tmp/osmdata/belgium/belgium-latest.osm.pbf
```

Détail des options :

- `--create` : créer les données, quitte à les écraser si elles existent déjà dans la base
- `--database` : nom de la base de données
- `--port` : port de connexion à la base de données
- `--cache` : gère la taille du cache (en MB) à allouer pour l'import des noeuds OSM. Je pensais au début que la valeur par défaut (800) suffirait mais j'ai eu l'erreur : *Node cache size is too small to fit all nodes. Please increase cache size*. Dépend de la RAM de votre machine.
- `--hstore-match-only` :
- `--number-processes` : nom de processus à utiliser pour paralléliser les tâches qui peuvent l'être

Sur mon ordinateur portable (Dell XPS 15 7590 avec un Intel Core i7-9750H de 9e génération - voir [fiche technique](https://www.dell.com/support/manuals/fr-fr/xps-15-7590-laptop/xps-15-7590-setup-and-specifications/processeurs?guid=guid-bfa52f40-8ad1-4df0-8d0f-942766bc2118&lang=fr-fr)) sur batterie, Pour celles et ceux que ça intéresse, dépliez pour voir ce que ça donne en termes de performances :

<!-- markdownlint-disable MD046 -->
??? example "Le détail de l'exécution sur ma machine"

    ```bash
    ❯ osm2pgsql --create --database osm --port 5434 -C 2000 -k /tmp/osmdata/belgium/belgium-latest.osm.pbf
    osm2pgsql version 1.2.1 (64 bit id space)

    Allocating memory for dense node cache
    Allocating dense node cache in one big chunk
    Allocating memory for sparse node cache
    Sharing dense sparse
    Node-cache: cache=2000MB, maxblocks=32000*65536, allocation method=3
    Using built-in tag processing pipeline
    Using projection SRS 3857 (Spherical Mercator)
    Setting up table: planet_osm_point
    Setting up table: planet_osm_line
    Setting up table: planet_osm_polygon
    Setting up table: planet_osm_roads

    Reading in file: /tmp/osmdata/belgium/belgium-latest.osm.pbf
    Using PBF parser.
    Processing: Node(53934k 7705.0k/s) Way(8262k 140.05k/s) Relation(79780 11397.14/s)  parse time: 73s
    Node stats: total(53934689), max(9770554582) in 7s
    Way stats: total(8262733), max(1063729340) in 59s
    Relation stats: total(87128), max(14183120) in 7s
    node cache: stored: 53934689(100.00%), storage efficiency: 50.16% (dense blocks: 170, sparse nodes: 53066475), hit rate: 100.00%
    Sorting data and creating indexes for planet_osm_point
    Sorting data and creating indexes for planet_osm_polygon
    Sorting data and creating indexes for planet_osm_line
    Sorting data and creating indexes for planet_osm_roads
    Copying planet_osm_roads to cluster by geometry finished
    Creating geometry index on planet_osm_roads
    Creating indexes on planet_osm_roads finished
    All indexes on planet_osm_roads created in 6s
    Completed planet_osm_roads
    Copying planet_osm_point to cluster by geometry finished
    Creating geometry index on planet_osm_point
    Creating indexes on planet_osm_point finished
    All indexes on planet_osm_point created in 16s
    Completed planet_osm_point
    Copying planet_osm_line to cluster by geometry finished
    Creating geometry index on planet_osm_line
    Creating indexes on planet_osm_line finished
    All indexes on planet_osm_line created in 69s
    Completed planet_osm_line
    Copying planet_osm_polygon to cluster by geometry finished
    Creating geometry index on planet_osm_polygon
    Creating indexes on planet_osm_polygon finished
    All indexes on planet_osm_polygon created in 145s
    Completed planet_osm_polygon

    Osm2pgsql took 218s overall
    ```
<!-- markdownlint-enable MD046 -->

----

## La carto sur QGIS

```bash
qgis --profile geotribu_tuto_ferragis --noversioncheck
```

### Installer les polices supplémentaires

> TO DOC

----

## Un procédé réutilisable

Une fois la base de données et le mode d'accès (via un fichier de service) en place et le projet stabilisé, on peut alors facilement appliquer le style à un autre territoire, en changeant simplement l'URL des données à télécharger et, optionnellement, l'emprise.

Exemple pour Aix-en-Provence :

```bash
# téléchargement
wget http://download.geofabrik.de/europe/france/provence-alpes-cote-d-azur-latest.osm.pbf -O /tmp/osmdata/osm_data.pbf
# découpage
osmium extract -b 5.347,43.484,5.536,43.565 /tmp/osmdata/osm_data.pbf -o /tmp/osmdata/osm_data_filtered.pbf
5.347,43.484,5.536,43.565
# import
osm2pgsql --slim --database osm --port 5434 --cache 2000 --number-processes 4 /tmp/osmdata/osm_data_filtered.pbf
```

----

## Nettoyage

Voici les commandes si vous souhaitez supprimer le cluster créé pendant le tutoriel. Attention, cela supprimera toutes les données donc à n'exécuter que si vous êtes certain/e de ne pas y tenir :

```bash
sudo systemctl stop postgresql@14-ferrargis
sudo pg_dropcluster 14 ferrargis
```

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

{% include "licenses/default.md" %}
