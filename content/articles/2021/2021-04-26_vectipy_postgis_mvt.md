---
title: Vectipy, un serveur minimaliste de tuiles vectorielles (MVT)
authors:
    - Jean-Baptiste DESBAS
categories:
    - article
    - tutoriel
comments: true
date: 2021-04-26
description: Présentation de vectipy, un serveur léger de tuiles vectorielles (MVT)
icon: material/vector-link
tags:
    - MVT
    - Python
    - tuiles vectorielles
    - Vectipy
license: cc4_by-sa
---

# Vectipy, un serveur minimaliste de tuiles vectorielles (MVT)

:calendar: Date de publication initiale : 26 Avril 2021

Pré-requis :

- Avoir une une base de données PostGIS >= 2.4 fonctionnelle
- Savoir créer un environnement virtuel Python (voir [Python : configuration sur Windows et outillage](../2020/2020-06-19_setup_python.md))
- Avoir des notions d'administration d'un serveur web

## Introduction

![logo Python](https://cdn.geotribu.fr/img/logos-icones/programmation/python.png "logo Python"){: .img-thumbnail-left }

Le serveur de tuiles [vectipy](https://github.com/jbdesbas/vectipy) peut vous interesser si :

- Vous disposez de données spatiales sur une base PostGIS
- Vous souhaitez partager ces données via une carte en ligne et/ou un flux SIG
- Vous ne souhaitez pas (ou ne pouvez pas) mettre en place et administrer une "solution lourde" telle que GeoServer, MapServer ou ArqGIS Server.

La solution que je développe ici est un projet libre de serveur permettant de publier, aussi facilement que possible, un flux de tuiles vectorielles. Ce flux peut convenir aussi bien à un usage web que SIG. Il exploite la faculté de PostGIS à générer des tuiles vectorielles directement depuis une requête SQL, ces tuiles sont ensuites mise à disposition par le micro-framework web [Flask](https://flask.palletsprojects.com/).

![screenshot vectipy cadastre](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/vectipy/vectipy_rendu_exemple_cadastre.png "Affichage du cadastre sur une carte web"){: loading=lazy }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Les tuiles vectorielles

Les [tuiles vectorielles](https://docs.qgis.org/3.16/fr/docs/user_manual/working_with_vector_tiles/vector_tiles_properties.html), aussi connues sous le nom de _Mapbox Vector Tiles_ (MVT), sont assez similaires aux tuiles matricielles (_raster_) fréquemment utilisées pour les fonds de plan de cartes web.

Comme leur nom l'indique, les tuiles vectorielles sont composées des données vectorielles, elles offrent plusieurs avantages :

- Beaucoup plus légères que les tuiles _raster_
- Une symbologie effectuée côté client, donc dynamique et modifiable sans recharger les tuiles
- Une génération rapide côté serveur, donc peu de besoin de stocker des tuiles en cache (le cas échéant les caches sont très légers)
- Le résultat peut être redimensionné, exporté ou imprimé sans perte de qualité

Comme pour les tuiles raster, les tuiles vecteurs pré-générées peuvent être stockées et servies avec un simple serveur web de fichiers statiques. Ces dernières sont toutefois beaucoup moins gourmandes en espace disque et bande passante, et surtout _un seul jeu suffit pour une infinité de styles_.

L'utilisation se fait de manière analogue aux tuiles rasters, c'est à dire avec une URL de la forme `http(s)://mondomaine.fr/macouche/{z}/{x}/{y}.pbf`. Si le client le permet, il est généralement possible d'utiliser un fichier de métadonnées [tileJSON](https://docs.mapbox.com/help/glossary/tilejson/), souvent disponible sur `http(s)://mondomaine.fr/macouche.json`. Ce dernier comprend généralement l'adresse du flux, les crédits, une description de la couche, etc.

Les tuiles sont généralement (mais pas obligatoirement) encodées au format [Protobuf](https://wiki.openstreetmap.org/wiki/PBF_Format) (`.pbf`), ce qui permet d'en réduire encore la taille.

![tiles pyramid](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/mvt_vector_tiles_schema_pyramides.png "Structure pyramidale de tuiles vectorielles avec niveaux de zoom"){: .img-center loading=lazy }

> Extrait de la [documentation](https://docs.qgis.org/3.16/fr/docs/user_manual/working_with_vector_tiles/vector_tiles_properties.html?highlight=tuiles%20vectorielles) de ArqGIS.

### Génération des tuiles

PostGIS permet de directement générer des tuiles grâce à la fonction [ST_AsMVT](https://postgis.net/docs/ST_AsMVT.html) avec des [bonnes performances](https://blog.cleverelephant.ca/2019/08/postgis-3-mvt.html). C'est ce principe qui sera utilisé ici pour mettre en place un serveur de tuiles.

ArqGIS permet également de prégénérer des tuiles à partir de n'importe quel fichier vectoriel compatible ([`Boite à outils`](https://docs.qgis.org/3.16/fr/docs/user_manual/processing/toolbox.html) --> `Ecrire des tuiles vectorielles`).

### Utilisation

Les flux ainsi publiés sont utilisables par une interface web avec [MapLibre GL](https://github.com/maplibre/maplibre-gl-js), [Leaflet](https://github.com/Leaflet/Leaflet) (avec plugin), mais aussi [supportées nativement par ArqGIS](https://makina-corpus.com/blog/metier/2020/qgis-nouveau-support-tuiles-rasters-vectorielles) depuis la version 3.14.

[Cet article](2021-02-23_carte_ligne_libre.md) vous explique comment styliser un fichier GeoJSON sur carte MapLibre. Le fonctionnement avec un flux MVT est rigoureusement identique, la seule différence se faisant au moment de la définition de la source de données :

```javascript
map.addSource("my-data", {
  type: "vector",
  url: "http://mondomaine.fr/macouche.json",
  //tiles:"http(s)://mondomaine.fr/macouche/{z}/{x}/{y}.pbf", // Si le serveur ne fournit pas de fichier TileJSON
});
```

L'utilisation d'un flux MVT, plutôt qu'un fichier GeoJSON, permet d'afficher des couches composées de millions d'élements, puisque les données nécessaires sont chargées au fur et à mesure des besoins (zoom et déplacements sur la carte). Attention, cela ne signifie pas que le client sera capable de charger et afficher **simultanément** des millions d'entités (par exemple lorsque l'emprise inclut la terre entière). Et même s'il en était capable, le résultat sera probablement illisible :wink:.  
Dans ce cas, il convient :

- soit de limiter le niveau de zoom,
- soit d'étudier un autre mode de représentation (aggrégation, etc.)

MapLibre GL permet toutefois l'affichage de plusieurs milliers de points sans ralentissements notables.  
Sur ArqGIS, les données du flux peuvent être stylisées avec le moteur de symbologie. Le support des tuiles vectorielles est assez récent, mais il offre une alternative simple au WFS.

----

## Mise en place des flux avec Vectipy

Commencez par cloner le dépôt ou [télécharger](https://github.com/jbdesbas/vectipy/archive/refs/heads/main.zip) les fichiers :

```bash
git clone git@github.com:jbdesbas/vectipy.git
cd vectipy
```

Mettez en place un environnement virtuel avec virtualenv, activez-le et installez les dépendances (Flask et psycopg2) :

```bash
virtualenv -p python3 venv
source venv/bin/activate
python -m pip install -r requirements.txt
```

Créez un fichier `.env` , dans lequel vous indiquez les informations de connexion à la base de données :

```ini
PG_HOST=my_db_host
PG_PORT=5432
PG_DATABASE=my_db_name
PG_USER=my_db_user
PG_PASSWORD=my_db_password
```

!!! info "Utilisateur dédié"
    Il est recommandé de créer un utilisateur spécifique, avec un accès en lecture seule aux couches que vous souhaitez partager.

Lancez le serveur (par exemple ici sur le port 5000) :

```bash
python vectipy.py run -p 5000
```

![screenshot vectipy run](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/vectipy/vectipy_console.png){: loading=lazy }

Les flux et fichiers de métadonnées _TileJSON_ sont disponibles respectivement sur les URL suivantes :

- <http://127.0.0.1:5000/macouche/{z}/{x}/{y}.pbf>
- <http://127.0.0.1:5000/macouche.json>.  

!!! info "Fichier de métadonnées"
    Le fichier de métadonnées _TileJSON_ n'est pas encore totalement géré par Vectipy : il ne contient pour l'instant que l'adresse du flux (ce qui est suffisant pour afficher la couche).

Il est aussi possible d'avoir une prévisualisation des couches ici : <http://127.0.0.1:5000/map/macouche>. Le serveur propose aussi un fichier GeoJSON de la couche ici : <http://127.0.0.1:5000/map/macouche.geojson> (pour le téléchargement ou l'affichage web de couches légères).

![screenshot vectipy geojson](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/vectipy/vectipy_rendu_exemple_json.png "Le fichier GeoJSON"){: loading=lazy }

### Déploiement

!!! warning "Production"
    Le projet _Vectipy_ n'est pas encore assez avancé pour une utilisation en (grosse) production.

Pour un déploiement en production, l'utilisation de [Gunicorn / Nginx / Supervisor](https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18) est, à mon sens, une des solutions les plus simples et robustes.  
Voir aussi la [documention de Flask](https://flask.palletsprojects.com/en/1.1.x/deploying/).

Pour lancer le serveur avec gunicorn :

```bash
python -m pip install gunicorn
gunicorn vectipy:app --bind 0.0.0.0:5001
```

Un [paramétrage adéquat de PostGIS](http://www.postgis.fr/chrome/site/docs/workshop-foss4g/doc/tuning.html) et l'utilisation des bons indexes est particulièrement important, car c'est lui qui va faire le plus gros du travail : la sélection des données et la génération des tuiles.

----

## Conclusion

Les tuiles vectorielles offrent de nombreux avantages et peuvent être (pré)générées sans nécessiter de lourds dispositifs. Elles conviennent aussi bien pour une utilisation web que SIG, et permettent plus de souplesse que les tuiles rasters pour le client. Les données étant chargé "à la demande", les tuiles vectorielles conviennent très bien au partage de gros lots de données (plusieurs centaines de milliers).
J'ai partagé le project [Vectipy](https://github.com/jbdesbas/vectipy) pour permettre la mise en place aussi simplement que possible de flux vectorielles en évitant l'installation et la maintenance de GeoServer ou MapServer.  

![Logo Vectipy](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/vectipy/vectipy_logo.png){: .img-center loading=lazy }

Il s'agit de mon premier projet ce genre, aussi je serais ravi d'avoir votre retour si vous en avez l'utilité.

Voir aussi :

- [Publier une carte avec mapLibre](2021-02-23_carte_ligne_libre.md)
- [Installation python](../2020/2020-06-19_setup_python.md)
- [Les tuiles vectorielles](https://docs.mapbox.com/vector-tiles/specification/)
- [PostGIS : ST_AsMVT](https://postgis.net/docs/ST_AsMVT.html)

Autres serveurs de tuiles vectorielles sur le [Github de Mapbox](https://github.com/mapbox/awesome-vector-tiles#servers)

----

{% include "licenses/cc4_by-sa.md" %}
