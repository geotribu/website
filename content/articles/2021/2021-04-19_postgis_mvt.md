---
title: "Publier une couche PostGIS en tuiles vectorielles (MVT)"
authors: ["Jean-Baptiste DESBAS"]
categories: ["article", "tutoriel"]
date: "2021-04-19 15:00"
description: "Présentation d'un serveur léger de tuiles vectorielles"
image: "server-web.png"
tags: "geotribu,python,vector tiles,mvt"
---

# Publier une couche PostGIS en tuiles vectorielles (MVT)

:calendar: Date de publication initiale : 19 Avril 2021

**Mots-clés :** Mapbox Vector Tiles | MVT | Tuiles vectorielles | PostGIS | PostgreSQL

Pré-requis :

- Avoir une une base de données PostGIS >= 2.4 fonctionnelle
- Savoir mettre un place un environnement virtuel Python (voir [Python : configuration sur Windows et outillage](https://static.geotribu.fr/articles/2020/2020-06-19_setup_python/) )

## Introduction

La méthode que je présente ici utilise [vectipy](https://github.com/jbdesbas/vectipy), un projet libre sans prétention permettant de publier un flux de tuiles vectorielles à partir de couches PostGIS. L'objectif est ici de pouvoir publier des données stockées dans une base PostGIS, sans installer et administrer un GeoServer ou MapServer. Le flux de tuiles vectorielle peut convenir aussi bien à un usage web que SIG.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Les tuiles vectorielles

Les tuiles vectorielles, aussi connues sous le nom de _Mapbox Vector Tiles_ (MVT), sont assez similaires aux tuiles matricielles (_raster_) fréquements utilisées pour les fonds de plan de cartes web.

Comme leurs nom l'indique, les tuiles vectorielles sont composées des données vectorielles, elles offrents plusieurs avantages :
- Beaucoup plus légères que les tuiles _raster_
- Une symbologie effectuée côté client, donc dynamique et modifiable sans recharger les tuiles
- Une génération rapide côté serveur, donc peu de besoin de stocker des tuiles en cache (le cas échéant les caches sont très légers)
- Le résultat peut être redimensionné, exporté ou imprimé sans perte de qualité

Commes pour les tuiles raster, les tuiles vecteurs pré-générées (par exemple avec l'algorithme (_Écrire des tuiles vectorielles (XYZ)_ ) peuvent être stockées et servies avec un simple serveur http. Ces dernières sont toutefois beaucoup moins gourmandes en espace disque et bande passante, et surtout *un seul jeu suffit pour une infinité de styles*.

L'utilisation se fait de manière analogue aux tuiles rasters, c'est à dire avec une url de la forme _http(s)://mondomaine.fr/macouche/{z}/{x}/{y}.pbf_. Si le client le permet, il est généralement possible d'utiliser un fichier de métadonnées [tileJSON](https://docs.mapbox.com/help/glossary/tilejson/), souvent disponible sur http(s)://mondomaine.fr/macouhe.json.

Les tuiles sont généralement (mais pas obligatoirement) encodées au format [Protobuf](https://wiki.openstreetmap.org/wiki/PBF_Format) (pbf), ce qui permet d'en réduire encore la taille.

### Génération
PostGIS permet de directement générer des tuiles grâce à la fonction [ST_AsMVT](https://postgis.net/docs/ST_AsMVT.html) avec des [bonnes performances](https://blog.cleverelephant.ca/2019/08/postgis-3-mvt.html).
QGIS permet également de générer des tuiles à partir de n'importe quel fichier vectoriel compatible (Boite à outil --> _Ecrire des tuiles vectorielles).

### Utilisation
Les flux ainsi publiés sont utilisables par une interface web avec [MapLibre GL](https://github.com/maplibre/maplibre-gl-js), [Leaflet](https://github.com/Leaflet/Leaflet) (avec plugin), mais aussi [supportées nativement par QGIS](https://makina-corpus.com/blog/metier/2020/qgis-nouveau-support-tuiles-rasters-vectorielles) depuis la version 3.14.

[Cet article](https://static.geotribu.fr/articles/2021/2021-02-23_carte_ligne_libre/) vous explique comment styliser un fichier geoJSON sur carte MapLibre. Le fonctionnement avec un flux est identique, la seule différence se faisant au moment de la définition de la source de données :

```javascript
 map.addSource('my-data', {
  type: 'vector',
  url:"http://mondomaine.fr/macouhe.json",
  //tiles:"http(s)://mondomaine.fr/macouche/{z}/{x}/{y}.pbf", //Si le serveur ne fournis pas de fichier TileJSON
});
```
L'utilisation d'un flux MVT, plutôt qu'un fichier GeoJSON, permet d'afficher des couches composées de millions d'élements, puisque les données nécessaires sont chargées au fur et à mesure des besoins (zoom et déplacements sur la carte). Attention, cela ne signifie pas que le client sera capable de charger et afficher **simultanément** des millions d'entités (par exemple lorsque l'emprise inclue la terre entière). Et même s'il en été capable, le résultat sera probablement illisible. Dans ces cas, il convient donc, soit de limiter le niveau de zoom, soit d'étudier un autre mode de représentation (aggrégation, etc.).


Sur QGIS, les données du flux peuvent être stylisées avec le moteur de symbologie. Le support des tuiles vectorielles est assez récent, mais il offre une alternative simple au WFS.


## Mise en place des flux avec vectipy

Commencez par cloner le dépot, ou [télécharger](https://github.com/jbdesbas/vectipy/archive/refs/heads/main.zip) les fichiers :

```bash
git clone git@github.com:jbdesbas/vectipy.git
cd vectipy
```

Mettez en place un environnment virtuel avec virtualenv, activez-le, et installez les dépendences (flask et psycopg2)

```bash
virtualenv -p python3 venv

source venv/bin/activate

pip install -r requierements.txt
```

Créez un fichier _.env_ , dans lequel vous indiquez les informations de connexion à la base de données :

```
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

![screenshot vectipy run](https://raw.githubusercontent.com/jbdesbas/vectipy/develop/screenshot1.png)

Les flux et fichiers de métadonnées sont disponibles respectivement sur les url suivantes : http://127.0.0.1:5000/macouhe/{z}/{x}/{y}.pbf et http://127.0.0.1:5000/macouhe.json
Il est aussi possible d'avoir une prévisualisation des couches ici : http://127.0.0.1:5000/map/macouhe

### Déploiement

!!! warning "Production"
    Le projet _Vectipy_ n'est pas encore assez avancé pour une utilisation en (grosse) production. 

Toutefois, pour un déploiement en production, l'utilisation de [Gunicorn / Nginx / Supervisor](https://medium.com/ymedialabs-innovation/deploy-flask-app-with-nginx-using-gunicorn-and-supervisor-d7a93aa07c18) est, à mon sens, une des solutions les plus simples et robustes. Voir aussi la [documention de Flask](https://flask.palletsprojects.com/en/1.1.x/deploying/).

Pour lancer le serveur avec gunicorn :
```bash
pip install gunicorn
gunicorn vectipy:app --bind 0.0.0.0:5001
```

Un [paramétrage adéquat de PostGIS](http://www.postgis.fr/chrome/site/docs/workshop-foss4g/doc/tuning.html) et l'utilisation des bons indexes est particulièrement important, car c'est lui qui va faire le gros du travail : la sélection des données et la génération des tuiles. 



## Conclusion

Les tuiles vectorielles offrent de nombreux avantages et peuvent être (pré)générées sans nécessiter de lourds dispositifs. Elles conviennent aussi bien pour une utilisation web que SIG, et permettent plus de souplesse que les tuiles rasters pour le client.
J'ai partagé le project _Vectipy_ pour permettre la mise en place aussi simplement que possible de flux vectorielles et éviter l'installation et la maintenance de GeoServer ou MapServer. Si vous utilisez déjà ces outils, il est probable que le mini-serveur _Vectipy_ vous soit inutile.

Il s'agit de mon premier projet ce genre, aussi n'hésitez pas à m'en faire un retour si vous en avez l'utilité.


Voir aussi :
[Publier une carte](https://static.geotribu.fr/articles/2021/2021-02-23_carte_ligne_libre/)

[Installation python](https://static.geotribu.fr/articles/2020/2020-06-19_setup_python/)

[Les tuiles vectorielles](https://docs.mapbox.com/vector-tiles/specification/)

[ST_AsMVT](https://postgis.net/docs/ST_AsMVT.html)
