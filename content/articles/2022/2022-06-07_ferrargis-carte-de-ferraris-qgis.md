---
title: "FerrarGIS, une carte de Ferraris avec QGIS"
authors:
    - Julien MOURA
categories:
    - article
    - tutoriel
date: "2023-09-15 10:20"
description: "Description pour le SEO."
icon: simple/ferrari
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/export_aix_large.png"
license: default
tags:
    - cartographie
    - OpenStreetMap
    - QGIS
---

<!-- TRUC UTILES A SUPPRIMER

[![image_title](image_url "image_title"){: .img-center loading=lazy}](image_url "image_title"){: data-mediabox="lightbox-gallery" data-title="image_title"}
 -->

# FerrarGIS, un style de carte de Ferraris (1777) avec QGIS

:calendar: Date de publication initiale : 15 septembre 2023

Prérequis :

- QGIS > 3.20
- des droits d'installation
- de préférence un PC sous Linux (ou via [WSL](/articles/2020/2020-10-28_gdal_windows_subsystem_linux_wsl/)) mais les outils utilisés sont tous disponibles sur Windows et MacOS

## Introduction

![logo Ferrari barré](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/ferrari_logo_barre.png "logo Ferrari barré"){: .img-rdp-news-thumb }

Au cours de mes pérégrinations de veille pour une revue de presse, je suis tombé sur [cet article](https://manuelclaeysbouuaert.be/projects/ferrargis.html) de [Manuel Claeys Bouuaert](https://manuelclaeysbouuaert.be/). Je ne connaissais pas la [carte [du comte Joseph] de Ferraris](https://fr.wikipedia.org/wiki/Carte_de_Ferraris) du coup j'étais content d'en apprendre davantage et j'ai trouvé que le rendu était très réussi.

[![Comparaison Namur Ferraris vs FerraGIS (2021)](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/compare_namur_1777-2021.png "Comparaison Namur Ferraris vs FerraGIS (2021)"){: .img-center loading=lazy}](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/compare_namur_1777-2021.png "Comparaison Namur Ferraris vs FerraGIS (2021)"){: data-mediabox="lightbox-gallery" data-title="Comparaison Namur Ferraris vs FerraGIS (2021) - Crédits : Manuel Claeys Bouuaert" }

Voyant que l'auteur [partage ses ressources sur GitHub](https://github.com/mclaeysb/FerrarGIS), j'essaie de voir rapidement ce que ça donne avant d'[écrire ma news](/contribuer/rdp/add_news/) pour la GeoRDP mais je me rends compte que ça ne se fait pas en 3 minutes et que ça mérite de s'y pencher plus en détails.  
L'occasion d'un petit tutoriel, non pas pour manipuler les styles de QGIS et briller dans les soirées mondaines de cartographes mais pour décrire pas à pas les étapes techniques nécessaires pour reproduire le super travail de l'auteur :

1. Installer et configurer PostgreSQL et ses extensions
1. Installer les outils d'import ([osm2pgsql]) et de pré-traitement ([Osmium]) des données OSM
1. Découper et import les données
1. Essayer et optimiser le projet et le style QGIS partagés

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

### Configuration Base Postg

Pour continuer, je dispose :

- [ ] d'un cluster PostgreSQL (15 en l'occurrence mais ça doit fonctionner avec des versions plus anciennes) sur le port `54352`
- [ ] d'une base de données que j'ai appelée `osm_ferrargis`
- [ ] sur laquelle j'ai activé les extensions `postgis` et `hstore`
- [ ] à laquelle je me connecte de façon sécurisée à l'aide des fichiers `~/.pgpass` et `~/.pg_service.conf` dont je mets ci-dessous une idée de ce qu'il y a dedans :

```conf title="Ligne dans le fichier ~/.pgpass (en CHMOD 0600)"
localhost:54352:*:nom_utilisateur_session:mot_de_passe
```

Et cette section dans mon fichier `~/.pg`

```ini title="Section dans le fichier ~/.pg_service.conf"
[local_ferrargis]
dbname=osm_ferrargis
host=localhost
port=54352
```

----

## Les données

### Télécharger OSM sur Aix-en-Provence

![logo OpenStreetMap](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/Openstreetmap.png "logo OpenStreetMap"){: .img-rdp-news-thumb }

Franchement on va pas se mentir : si Napoléon avait eu les données OpenStreetMap, on aurait moins de [problèmes de borne](https://www.lavoixdunord.fr/992266/article/2021-04-27/bousignies-sur-roc-il-deplace-une-borne-frontiere-et-viole-le-traite-de-courtrai) (de frontières, pas de ministre) de nos jours ! :smile:

Un petit tour par GeoFabrik pour télécharger les données de la Belgique : <https://download.geofabrik.de/europe/belgium.html>.

On peut également utiliser un outil en ligne de commande, par exemple `wget` avec l'option `-N` qui permet de télécharger uniquement si le fichier distant (ici le serveur GeoFabrik) est plus récent par rapport à la version locale (sur votre machine) :

```sh
wget -N http://download.geofabrik.de/europe/france/provence-alpes-cote-d-azur-latest.osm.pbf -P /tmp/osmdata/paca
```

### Optionnel : découper les données

![logo Osmium Tool](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/osmium.svg "logo Osmium Tool"){: .img-rdp-news-thumb }

Si on craint de manquer d'espace disque, de puissance ou qu'on cible une zone restreinte en particulier, on peut découper les données avec une emprise avant de les importer avec un outil comme Osmium par exemple.

On installe [Osmium](https://osmcode.org/osmium-tool/) :

```sh
sudo apt install osmium-tool
```

Et on découpe sur la zone qui nous intéresse, par exemple Aix-en-Provence :

```sh
osmium extract -b 5.21,43.42,5.72,43.66 /tmp/osmdata/paca/provence-alpes-cote-d-azur-latest.osm.pbf -o /tmp/osmdata/paca/aixenprovence.osm.pbf
```

!!! tip "Vigilance"
    Du coup, le nom de fichier sera différent pour la commande d'import à suivre :wink: !

### Import des données

```bash
osm2pgsql --create --database osm_ferrargis --port 54352 --cache 1000 --number-processes 4 /tmp/osmdata/paca/aixenprovence.osm.pbf
```

----

## La carto sur QGIS

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-rdp-news-thumb }

Maintenant que l'on a chargé les données, en avant pour la représentation sous QGIS !

```bash
qgis --profile geotribu_tuto_ferragis --noversioncheck
```

### Installer les polices supplémentaires

Pour pouvoir chargf

### Créer la connexion à la base de données

Ouvrir le gestionnaire de sources de données et créer une connexion PostgreSQL en entrant le nom du service (celui entre `[]` dans le fichier `.pg_service.conf`) :

[![QGIS - Connexion à la base via le pg_service](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/qgis_connexion_base_osm.png "QGIS - Connexion à la base via le pg_service"){: .img-center loading=lazy}](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/qgis_connexion_base_osm.png "QGIS - Connexion à la base via le pg_service"){: data-mediabox="lightbox-gallery" data-title="QGIS - Connexion à la base via le pg_service"}

### Désactiver les couches inutiles

Afin de grapiller quelques points de performance d'affichage, j'ai choisi de désactiver les couches qui concernent des objets non présents sur Bruxelles :

- les dunes
- les frontières

### Visualiser le résultat

On a un pe

[![FerraGIS - Bruxelles](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/qgis_ferraris_bruxelles_centre.png "FerraGIS - Bruxelles"){: .img-center loading=lazy}](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/qgis_ferraris_bruxelles_centre.png "FerraGIS - Bruxelles"){: data-mediabox="lightbox-gallery" data-title="FerraGIS - Bruxelles"}

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
osm2pgsql --create --database osm --port 54342 --cache 1000 --number-processes 4 /tmp/osmdata/osm_data_filtered.pbf
```

[![FerrarGIS - Aix-en-Provence](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/qgis_ferraris_aix-en-provence_centre.png "FerrarGIS - Aix-en-Provence"){: width=50% loading=lazy}](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/qgis_ferraris_aix-en-provence_centre.png "FerrarGIS - Aix-en-Provence"){: data-mediabox="lightbox-gallery" data-title="FerrarGIS - Aix-en-Provence"}
[![FerraGIS - Aix-en-Provence - zoom](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/qgis_ferraris_aix-en-provence_centre_zoom.png "FerraGIS - Aix-en-Provence - zoom"){: width=50% loading=lazy}](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_ferraris/qgis_ferraris_aix-en-provence_centre_zoom.png "FerraGIS - Aix-en-Provence - zoom"){: data-mediabox="lightbox-gallery" data-title="FerraGIS - Aix-en-Provence - zoom"}

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
