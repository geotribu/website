---
title: Servir du WMS caché avec MapProxy - partie 2
subtitle: On s'était caché/es !
authors:
    - Guilhem ALLAMAN
categories:
    - article
comments: true
date: 2026-04-30
description: Un article qui montre une manière de servir en WMS des flux en provenance d'autres serveurs cartographiques. Deuxième partie, pour aller plus loin.
icon: simple/tile
image:
license: beerware
tags:
    - cache
    - MapProxy
    - QGIS
    - WMS
---

# Servir du WMS caché avec MapProxy - partie 2

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![Logo MapProxy](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/mapproxy.png){: .img-thumbnail-left }

Voici la deuxième partie de l'article sur [MapProxy](https://mapproxy.org/), suite du [premier lors duquel nous avons installé une instance qui sert quelques couches en WMS](./2026-04-16_cacher_wms_avec_mapproxy_1.md).

Voyons maintenant comment l'utiliser et l'optimiser !

## Tester dans QGIS

Ouvrons maintenant le logiciel Desktop numero uno, et créons une nouvelle connexion WMS, avec l'URL `https://DOMAIN/mapproxy/service` :

![Écran de création d'une nouvelle connexion WMS dans QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/servir_wms_cache_mapproxy/ecran_qgis_new_wms_connection.webp){: .img-center loading=lazy }

Les 4 couches définies sont listées une fois que nous sommes connecté/es :

![Écran avec liste des couches WMS fournies par notre connexion WMS dans QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/servir_wms_cache_mapproxy/ecran_qgis_wms_layers.webp){: .img-center loading=lazy }

Ouvrons la couche des Buildings de la Géoplateforme, tada :tada: :

![Affichage d'une couche de buildings de la Géoplateforme dans QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/servir_wms_cache_mapproxy/ecran_qgis_wms_layer_loaded.webp){: .img-center loading=lazy }

## Pré-cacher les zones configurées

Comme tout bon serveur de cache tuilé, MapProxy vient avec un utilitaire, qui permet de pré-générer les tuiles dans le cache.

Pour cela, on a (encore) besoin de configurer un fichier `seeds.yaml`, qu'on dépose au même endroit que le `mapproxy.yaml` - dans le dossier `config` monté dans le container docker :

```yaml linenums="1" title="Contenu de config/seeds.yaml"
seeds:
  paris19osm_seed:
    caches:
      - paris19osm_cache
    coverages:
      - paris19_coverage
    grids:
      - osm_grid
    levels:
      from: 8
      to: 18
    refresh_before:
      weeks: 4

cleanups:
  paris19osm_cleanup:
    caches:
      - paris19osm_cache
    levels:
      from: 0
      to: 20
    remove_before:
      weeks: 4

coverages:
  paris19_coverage:
    bbox:
      - 2.3646858891194782
      - 48.8720621793437502
      - 2.4108388540828618
      - 48.9021619064262865
    srs: EPSG:4326
```

Pour le seed `paris19osm_seed`, les tuiles correspondantes au niveaux de zoom de 8 à 18 seront générées avec une telle config. Aussi, toutes les tuiles mise en cache il y a plus de 4 semaines seront régénérées (clé `refresh_before`). [La doc](https://mapproxy.github.io/mapproxy/latest/seed.html#seeding) montre toutes les options et configurations possibles.

Pour lancer une opération de _seeding_, voici la commande qui spécifie avec l'option `--seed=x,y` quel(s) _seed(s)_ pré-générer :

```sh
$ docker compose exec -it mapproxy mapproxy-seed -s /mapproxy/seeds.yaml -f /mapproxy/mapproxy.yaml --seed=paris19osm_seed

========== Seeding tasks ==========
Start seeding process (1 task)
  paris19osm_seed:
    Seeding cache 'paris19osm_cache' with grid 'osm_grid' in EPSG:3857
    Limited to coverage in: 2.36469, 48.87206, 2.41084, 48.90216 (EPSG:4326)
    Levels: [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
    Overwriting: tiles older than 2025-11-03 11:51:25
[11:51:25]  8   0.00% 263235.62906, 6253180.83813, 268373.35362, 6258276.59247 (0 tiles)
[11:51:28] 17  18.75% 263235.62906, 6256829.38731, 263554.87353, 6257440.88354 (59 tiles)
[11:51:29] 17  21.88% 263554.87353, 6256829.38731, 264166.36975, 6257440.88354 (76 tiles)
[11:51:30] 17  29.69% 263554.87353, 6255606.39486, 264166.36975, 6256217.89109 (155 tiles)
[11:51:31] 17  35.94% 263554.87353, 6254383.40241, 264166.36975, 6254994.89863 (232 tiles)
[11:51:32] 17  46.88% 263554.87353, 6253180.83813, 264166.36975, 6253771.90618 (310 tiles)
[11:51:33] 16  56.25% 264166.36975, 6256829.38731, 265389.36221, 6258052.37976 (381 tiles)
[11:51:35] 17  58.59% 264777.86598, 6256829.38731, 265389.36221, 6257440.88354 (444 tiles)
[11:51:36] 17  61.72% 266000.85843, 6256829.38731, 266612.35466, 6257440.88354 (529 tiles)
[11:51:37] 17  69.53% 267223.85088, 6257440.88354, 267835.34711, 6258052.37976 (608 tiles)
[11:51:38] 16  71.88% 267835.34711, 6256829.38731, 268373.35362, 6258052.37976 (672 tiles)
[11:51:39] 17  75.78% 264166.36975, 6255606.39486, 264777.86598, 6256217.89109 (759 tiles)
[11:51:43] 17  76.95% 266000.85843, 6256217.89109, 266612.35466, 6256829.38731 (823 tiles)
[11:51:45] 17  78.52% 264777.86598, 6254994.89863, 265389.36221, 6255606.39486 (908 tiles)
[11:51:46] 16  79.69% 265389.36221, 6254383.40241, 266612.35466, 6255606.39486 (972 tiles)
[11:51:47] 17  80.86% 266000.85843, 6254383.40241, 266612.35466, 6254994.89863 (1035 tiles)
[11:51:48] 17  82.03% 266612.35466, 6255606.39486, 267223.85088, 6256217.89109 (1100 tiles)
[11:51:50] 17  82.42% 267223.85088, 6255606.39486, 267835.34711, 6256217.89109 (1121 tiles)
[11:51:51] 17  84.77% 267223.85088, 6254994.89863, 267835.34711, 6255606.39486 (1207 tiles)
[11:51:52] 17  86.72% 267835.34711, 6254383.40241, 268373.35362, 6254994.89863 (1292 tiles)
[11:51:53] 17  89.84% 264777.86598, 6253180.83813, 265389.36221, 6253771.90618 (1378 tiles)
[11:51:55] 17  92.97% 266000.85843, 6253180.83813, 266612.35466, 6253771.90618 (1463 tiles)
[11:51:56] 17  96.09% 267223.85088, 6253180.83813, 267835.34711, 6253771.90618 (1549 tiles)
[11:51:57]  8 100.00% 263235.62906, 6253180.83813, 268373.35362, 6258276.59247 (1621 tiles)
```

Une fois l'opération terminée, on se retrouve avec nos différents niveaux de zoom mis en cache, dans le dossier `cache` :

```sh
$ ls -l cache/paris19osm_cache_EPSG3857/

total 44
drwxr-xr-x 3 root root 4096 Dec 29 12:51 08
drwxr-xr-x 3 root root 4096 Dec 29 12:51 09
drwxr-xr-x 3 root root 4096 Dec 29 12:51 10
drwxr-xr-x 3 root root 4096 Dec 29 12:51 11
drwxr-xr-x 3 root root 4096 Dec 29 12:51 12
drwxr-xr-x 3 root root 4096 Dec 29 12:51 13
drwxr-xr-x 3 root root 4096 Dec 29 12:51 14
drwxr-xr-x 3 root root 4096 Dec 29 12:51 15
drwxr-xr-x 3 root root 4096 Dec 29 12:51 16
drwxr-xr-x 3 root root 4096 Dec 29 12:51 17
drwxr-xr-x 3 root root 4096 Dec 29 12:51 18
```

!!! info
    L'utilitaire `mapproxy-seed` permet également de supprimer des tuiles du cache, déclarés via la clé `cleanups` dans le fichier `seeds.yaml`, et à supprimer via l'option `--cleanup=x,y` de l'outil `mapproxy-seed`.

## Conclusion

En conclusion, nous avons vu comment instancier un serveur MapProxy, qui comme son nom l'indique permet de jouer au proxy et mettre en cache des tuiles en provenance de un ou plusieurs serveurs cartographiques, et à destination de clients consommateurs de WMS.

J'attire l'attention sur l'utilisation des datasources qu'on peut être amenés à configurer et servir via MapProxy : important de lire et de s'informer des conditions d'utilisation avant de se lancer.

Et nous avons ici réalisé un setup rudimentaire, sans implémenter les requêtes WMS `GetFeature` et autres. Et généralement, en production il est toujours judicieux de décrire les flux servis avec des métadonnées.

À l'heure où éclosent des formats optimisés pour le cloud, comme [COG](https://cogeo.org/), [Zarr](https://zarr-specs.readthedocs.io/en/latest/v3/core/index.html), etc. Et à une époque où les tuiles vectorielles prennent véritablement leur essor - d'ailleurs [OpenStreetMap en sert maintenant sur son site principal](https://blog.openstreetmap.org/2025/07/22/les-tuiles-vectorielles-sont-deployees-sur-openstreetmap-org/?lang=fr), le format et les flux WMS ont-ils toujours leur place ? Ou la cèderont-ils à ces nouveaux formats, plus optimisés et moins ressourcivores en terme de stockage et bande passante ? J'imagine que l'avenir nous le dira.

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
