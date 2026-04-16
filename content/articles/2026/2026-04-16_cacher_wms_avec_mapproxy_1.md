---
title: Servir du WMS caché avec MapProxy - partie 1
subtitle: On joue à cache-cache ?
authors:
    - Guilhem ALLAMAN
categories:
    - article
comments: true
date: 2026-04-16
description: Un article qui montre une manière de servir en WMS des flux en provenance d'autres serveurs cartographiques. Première partie d'introduction et d'installation.
icon: simple/tile
image:
license: beerware
tags:
    - cache
    - MapProxy
    - nginx
    - WMS
---

# Servir du WMS caché avec MapProxy - partie 1

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![Logo MapProxy](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/mapproxy.png){: .img-thumbnail-left }

Dans certains contextes, des utilisateurs de QGIS peuvent être amenés à consommer du WMS et des tuiles, avec des enjeux et défis de connectivité et performances, compte-tenu du fait que les serveurs sont parfois distants des utilisateurs finaux. Aussi, la bande passante des réseaux dans lesquels les postes QGIS demandent des flux n'est pas toujours garantie, alors il faut parfois se creuser la tête pour rendre un usage fluide de ces flux, dans notre logiciel SIG Desktop préféré.

## MapProxy : quèsaco ?

Une brique existe pour cela, [MapProxy](https://mapproxy.org/) : opensource, léger et svelte, écrit en Python et qui porte plutôt bien son nom : un proxy de cartes, qui va servir à mettre en cache des flux générés par **d'autres** serveurs cartographiques. L'avantage est déjà que MapProxy possède, à l'instar d'autres serveurs géographiques la possibilité de mettre en cache les tuiles servies, et ce de différentes manières : fichiers classiques, mbtiles, geopackage, redis, s3... Aussi, MapProxy permet comme son nom l'indique de servir de proxy, c'est-à-dire de relai de flux entre un serveur carto et d'autres clients, qui peuvent être par ex. QGIS, du WebGIS, d'autres serveurs carto...

La configuration est basée sur des fichiers [YAML](https://yaml.org/spec/), ce qui peut faciliter des automatisations et des déploiements d'instances iso.

À noter qu'[Arnaud](../../team/arnaud-vandecasteele.md) en parlait déjà en 2010, au travers [de cet article](../2010/2010-04-23_accelerer-et-personnaliser-services-WMS-avec-MapProxy.md) qui explique comment installer un serveur local, avec environnement virtuel Python.

## Cas d'usage de MapProxy

Le site de MapProxy présente un premier cas d'usage, où un serveur `MapProxy` cache et sert à des clients finaux des flux générés par plusieurs autres serveurs :

![Architecture avec un mapproxy qui sert des flux en provenance d'autres serveurs carto à des clients](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/MapProxy/mapproxy_schema.png){: .img-center loading=lazy }

On note déjà que les flux en entrée du MapProxy peuvent être du WMS ou de la tuile (par exemple les couches `XYZ` dans QGIS), fournies par exemple par MapServer, GeoServer, QGIS Server...

Les clients qui consomment ce WMS en provenance du MapProxy peuvent être des clients Desktop comme QGIS, ou des librairies web style OpenLayers, MapLibre, Leaflet, ou encore des app mobiles comme QField / Mergin Maps, ou bien même d'autres serveurs cartographiques ! C'est la beauté des protocoles.

----

Un autre cas d'usage pourrait être le suivant :

- des clients éparpillés et/ou à l'autre bout du monde, avec des latences très lentes en visant un unique serveur cartographique.

- un _super_ serveur cartographique, quelque part, qui calcule et sert tout le nécessaire, par exemple QGIS server. Nous n'avons pas envie de répliquer et manipuler plusieurs instances de QGIS server ayant vocation à servir strictement les mêmes flux, alors nous allons préférer instancier différentes instances de MapProxy.

- des instances de MapProxy plus proches des clients, permettant ainsi de cacher et fournir les flux aux clients de manière plus fluide et performante.

La logique pourrait se traduire par le schéma suivant :

```mermaid
graph TD

    subgraph Col1[ ]
        direction TB
        ClientZ11[👩 Alicia<br>sur QGIS]
        ClientZ12[👨 Boby<br>sur MapLibre]
    end

    subgraph Col2[ ]
        direction LR
        mapproxyZ1[🤖 MapProxy zone 1]
    end

    subgraph Col3[ ]
        direction TB
        ServeurCentral[💾 Serveur Central]
    end


    ClientZ11 --> |1: ✉️ Demande le flux| mapproxyZ1
    mapproxyZ1 ---> D1{2: 🌀 Ressource<br>en cache ?}
    D1 --> |✅ Oui<br>📦 Retourne la ressource| ClientZ11
    D1 --> |❌ Non| R1Z1[3: ✉️ Demande la ressource]
    R1Z1 --> ServeurCentral
    ServeurCentral --> |4: 👷 Calcule la ressource| ServeurCentral
    ServeurCentral --> |5: 📦 Retourne la ressource| mapproxyZ1
    mapproxyZ1 --> |6: 🌀 Met en cache<br>la ressource| mapproxyZ1
    mapproxyZ1 --> |7: 📦 Retourne la ressource| ClientZ11
```

## Mise en route avec un exemple

Afin d'illustrer et mettre en route une stack avec MapProxy au centre, entre un serveur carto et un client, faisons un petit exemple en mettant en cache des données sur le 19e arrondissement de Paris. En bout de chaîne, notre MapProxy va donc servir des couches WMS pour cette zone, pour laquelle nous auront besoin de la _bounding box_.

Concernant les sources "centrales", étant donné qu'on n'a pas vraiment de serveur carto qui tourne avec des "vraies" données, on va utiliser les tuiles d'OpenStreetMap, du WMS de la Géoplateforme ainsi que des tuiles d'imagerie satellite de Google et Bing.

!!! warning
    Ici on est dans un tuto à but pédagogique, si vous souhaitez utiliser et mettre en cache ces sources de données en production, et/ou pour des usages commerciaux, allez d'abord lire attentivement les conditions générales d'utilisation de ces _datasources_.

Pour rappel, il est déjà possible d'ajouter ces couches à QGIS, en ajoutant par exemple une nouvelle source `XYZ`, ou bien via une connexion WMS :

- _OpenStreetMap_ : `https://tile.openstreetmap.org/{z}/{x}/{y}.png`, qui [propose d'ailleurs un guide pour configurer MapProxy avec OSM](https://wiki.openstreetmap.org/wiki/MapProxy).
- _Géoplateforme_ : on va utiliser la couche [`BU.building` du service _WMS-Vecteur_](https://geoservices.ign.fr/documentation/services/services-geoplateforme/diffusion#70068). Ce service est limité à 50 requêtes par seconde.
- _Googly Hybrid_ : `https://mt.google.com/vt/lyrs=y&hl=en&x={x}&y={y}&z={z}`
- _Bing Aerial_ : `http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1` - ici on n'utilise pas de `x/y/z` mais un paramètre `q`, pour _quadkey_. Rien à voir avec un véhicule de kéké des forêts, c'est plutôt une manière d'indexer spatialement des tuiles carrées. [Plus d'infos ici](https://medium.com/data-science/geospatial-indexing-with-quadkeys-d933dff01496).

![Configuration d'une source XYZ avec les tuiles d'OpenStreetMap](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/servir_wms_cache_mapproxy/xyz_openstreetmap_source_config.webp){: .img-center loading=lazy }

!!! info
    À noter que lors de la création d'une connexion de type `XYZ`, le bas de l'interface montre des niveaux de zoom min et max à demander (respectivement 0 et 19). Gardez ces valeurs en tête, nous pourrions les ressortir plus tard lorsque nous jouerons à cache-cache :wink:

## Installation de MapProxy sur un serveur debian / ubuntu

Entrons maintenant dans le vif du sujet, et la partie _geek_ : l'installation de MapProxy sur une machine linux. Ici on se limitera aux distributions basées sur debian et ubuntu.

Une fois n'est pas coutume - j'ai plutôt l'habitude de déployer des MapProxy avec [systemd](https://fr.wikipedia.org/wiki/Systemd), étant donné qu'on va utiliser [docker](https://www.docker.com/) pour lancer l'applicatif, il est déjà nécessaire d'installer cet outil [en suivant la doc officielle](https://docs.docker.com/engine/install/debian/).

Une fois docker installé, attardons-nous sur le léger fichier `docker-compose.yaml` pour lancer le service :

```yaml title="Contenu du docker-compose.yaml"
services:
  mapproxy:
    image: kartoza/mapproxy:6.0.1
    restart: unless-stopped
    environment:
      - PRODUCTION=true
      - PROCESSES=4
      - CHEAPER=2
      - THREADS=10
      - MULTI_MAPPROXY=false
      - ALLOW_LISTING=true
      - LOGGING=true
    volumes:
      - ./config:/mapproxy
      - ./cache:/cache_data
    ports:
      - 8765:8080

```

- On redirige vers le port 8765 en sortie, qu'on configurera dans nginx, notre serveur agissant comme reverse-proxy devant notre map proxy :hot_face:...
- On désactive le mode `MULTI_MAPPROXY` pour ce tuto.
- Les deux entrées dans la partie `volumes` représentent les dossiers locaux montés dans le container :
    - Il doit y avoir un répertoire `config` là où vous vous trouvez (où créez-le via `mkdir -p config`). Ce répertoire contiendra notamment la configuration et la déclaration des couches servies par le MapProxy.
    - Il doit y avoir un répertoire `cache` là où vous vous trouvez (où créez-le via `mkdir -p cache`). Ce répertoire accueillera les tuiles cachées, étant donné qu'ici on va rester sur du cache simple de type [_file_](https://mapproxy.github.io/mapproxy/latest/caches.html#file). Notez qu'il est possible d'enregistrer les tuiles cachées dans [du geopackage](https://mapproxy.github.io/mapproxy/latest/caches.html#cache-geopackage), dans [des mbtiles](https://mapproxy.github.io/mapproxy/latest/caches.html#cache-mbtiles), dans [du redis](https://mapproxy.github.io/mapproxy/latest/caches.html#cache-redis), dans [du s3](https://mapproxy.github.io/mapproxy/latest/caches.html#cache-s3), et d'autres trucs comme nous le savons, _à nous l'savon_ !

<!-- markdownlint-disable MD033 -->

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/cknUKHVD-00?si=yhtTkNjjgRv8PtUw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<!-- markdownlint-enable MD033 -->

Une fois ce `docker-compose.yaml` créé de même que les deux dossiers nécessaires, jettons un coup d'oeil au fichier de configuration (unique) de MapProxy !

## Configuration du MapProxy

Il s'agit donc d'[un fichier unique `mapproxy.yaml`](https://mapproxy.github.io/mapproxy/latest/configuration.html#mapproxy-yaml), qui doit se trouver dans votre dossier `config` là où vous vous trouvez.

Abordons le contenu d'un tel fichier de conf, pour un seul _layer_ - OpenStreetMap caché sur Paris 19.

Il y a plusieurs sections :

- la partie [_services_](https://mapproxy.github.io/mapproxy/latest/services.html#) qui déclare du WMS uniquement ici (WMTS, TMS possibles etc.)
- un [_layer_](https://mapproxy.github.io/mapproxy/latest/configuration.html#layers) pointe vers un [_cache_](https://mapproxy.github.io/mapproxy/latest/configuration.html#caches), qui lui-même se réfère à une [_source_](https://mapproxy.github.io/mapproxy/latest/configuration.html#sources-conf-label) et une [_grid_](https://mapproxy.github.io/mapproxy/latest/configuration.html#id6).
- ici on délimite la source avec une _bbox_, qui représente l'emprise du 19e arrondissement de Paris. [Plusieurs types de _coverages_ sont disponibles](https://mapproxy.github.io/mapproxy/latest/coverages.html#coverages).

Ce qui donne un fichier `mapproxy.yaml` qui ressemble à ça :

```yaml linenums="1" title="Contenu de config/mapproxy.yaml"
sources:
  paris19osm_source:
    type: tile
    url: https://tile.openstreetmap.org/%(z)s/%(x)s/%(y)s.png
    grid: osm_grid
    coverage:
      bbox:
        - 2.3646858891194782
        - 48.8720621793437502
        - 2.4108388540828618
        - 48.9021619064262865
      srs: EPSG:4326

caches:
  paris19osm_cache:
    sources:
      - paris19osm_source
    grids:
      - osm_grid

layers:
  - name: paris19_OSM
    sources:
      - paris19osm_cache
    title: Paris19 - OpenStreetMap

grids:
  osm_grid:
    base: GLOBAL_WEBMERCATOR
    origin: nw
    srs: EPSG:3857

services:
  demo: null
  wms:
    bbox_srs:
      - EPSG:4326
    featureinfo_types:
      - text
      - html
      - xml
    image_formats:
      - image/jpeg
      - image/png
    md:
      abstract: WMS server
      access_constraints: For testing purposes only.
      contact:
        address: 12 Boulevard de la Geotribu
        city: GeotribuVille
        country: GeotribuCountry
        email: geotribu@gmail.com
        organization: Geotribu
        person: Guilhem Allaman
        position: Geotribun
        postcode: 75019
      online_resource: http://mapproxy.geotribu.net/mapproxy/service?
      title: Geotribu Test WMS Proxy
    on_source_errors: raise
    srs:
      - EPSG:2154
      - EPSG:3857
      - EPSG:4326
    strict: true
    versions:
      - 1.3.0
      - 1.1.1

globals:
  cache:
    base_dir: /cache_data
```

Voyons maintenant comment configurer les différentes sources de données qu'on définissait plus haut.

- Source _OpenStreetMap_ :

```yaml
paris19_osm_source:
  type: tile
  url: https://tile.openstreetmap.org/%(z)s/%(x)s/%(y)s.png
  grid: osm_grid
  coverage:
    bbox:
      - 2.3646858891194782
      - 48.8720621793437502
      - 2.4108388540828618
      - 48.9021619064262865
    srs: EPSG:4326
```

Source _WMS-Vecteur Géoplateforme_ :

```yaml
paris19_bu_building_source:
  type: wms
  req:
    url: https://data.geopf.fr/wms-v/ows
    layers: BU.Building
    transparent: true
  grid: osm_grid
  coverage:
    bbox:
      - 2.3646858891194782
      - 48.8720621793437502
      - 2.4108388540828618
      - 48.9021619064262865
    srs: EPSG:4326
  wms_opts:
    legendurl: https://data.geopf.fr/wms-v/ows?service=WMS&version=1.3.0&request=GetLegendGraphic&format=image%2Fpng&width=20&height=20&layer=BU.Building
  image:
    transparent_color: "#ffffff"
    transparent_color_tolerance: 0
```

Source _Imagerie Google Hybrid_ :

```yaml
paris19_googlehybrid_source:
  type: tile
  url: https://mt.google.com/vt/lyrs=y&hl=en&x=%(x)s&y=%(y)s&z=%(z)s
  grid: osm_grid
  coverage:
    bbox:
      - 2.3646858891194782
      - 48.8720621793437502
      - 2.4108388540828618
      - 48.9021619064262865
    srs: EPSG:4326
```

Source _Imagerie Bing Aerial_ :

```yaml
paris19_bing_aerial_source:
  type: tile
  url: https://ecn.t3.tiles.virtualearth.net/tiles/a%(quadkey)s.jpeg?g=1
  grid: osm_grid
  coverage:
    bbox:
      - 2.3646858891194782
      - 48.8720621793437502
      - 2.4108388540828618
      - 48.9021619064262865
    srs: EPSG:4326
```

Les `caches` et `layers` sont sensiblement les mêmes, adaptés pour pointer sur la bonne `source`.

## Configuration du serveur web nginx

Maintenant, configurons notre serveur web nginx, qui va directement recevoir les requêtes en provenance des clients avant de les dispatcher à l'instance MapProxy.

Pour cela créer un nouveau "site", dans `/etc/nginx/sites-available/` :

``` title="Configuration du site nginx dans /etc/nginx/sites-available/mapproxy.conf"
upstream mapproxy_upstream {
  server 127.0.0.1:8765;
}

server {
  listen 80;
  server_name mapproxy.geotribu.xyz;
  return 301 https://$host$request_uri;
}

server {

  listen 443 ssl;
  server_name mapproxy.geotribu.xyz;

  ssl_certificate /etc/letsencrypt/live/mapproxy.geotribu.xyz/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/mapproxy.geotribu.xyz/privkey.pem;

  error_log /var/log/nginx/mapproxy.error.log;
  access_log /var/log/nginx/mapproxy.access.log combined;

  location /mapproxy {
    proxy_pass http://mapproxy_upstream;
    proxy_set_header Host $http_host;
    proxy_set_header X-Script-Name /mapproxy;
  }
}
```

Créer ensuite un lien symbolique vers `/etc/nginx/sites-enabled/` :

```sh
sudo ln -s /etc/nginx/sites-available/mapproxy.conf /etc/nginx/sites-enabled/mapproxy.conf
```

Récupérer ensuite des certificats Let's Encrypt, soit en éteignant nginx avec `systemctl stop nginx` puis `sudo certbot certonly --standalone -d mapproxy.geotribu.xyz`, soit avec le plugin nginx pour certbot via `sudo certbot certonly --nginx -d mapproxy.geotribu.xyz`.

Retourner maintenant à l'emplacement où vous avez mis le `docker-compose.yaml` ainsi que le dossier de config de MapProxy. Démarrer l'instance via  `docker compose up -d`.

Regarder les logs avec `docker compose logs -f -n 200`, si tout est ok, on a maintenant un MapProxy fonctionnel :tada: !

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
