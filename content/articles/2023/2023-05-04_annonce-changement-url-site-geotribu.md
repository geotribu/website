---
title: Geotribu déménage
subtitle: Attachez vos ceintures de favoris
authors:
    - Geotribu
categories:
    - article
date: "2023-05-05 10:20"
description: Après 3 ans sur un sous-domaine, le site va revenir sur son domaine principal. Attachez vos ceintures de favoris !
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/changement_url_geotribu/demenagement_globe_terrestre.png
license: default
robots: index, follow
tags:
    - Geotribu
---

# Changement d'URL du site Geotribu cet été

:calendar: Date de publication initiale : 5 mai 2023

![logo GeoTribu](https://cdn.geotribu.fr/img/internal/charte/geotribu_logo_75x75.webp){: .img-rdp-news-thumb loading=lazy }

Voilà 3 ans que Geotribu est de retour après une [coupure de service de... 3 ans](/articles/2020/2020-08-31_geotribu_histoire/).  

3 ans que ce nouveau site est en place.  
3 ans à en améliorer l'ergonomie, les fonctionnalités et surtout à réintégrer et nettoyer les anciens contenus.  
3 ans qu'il est accessible sur <https://geotribu.fr>

Il est temps de rebasculer le site sur l'adresse principale.

Après les sondages sur [Mastodon](https://mapstodon.space/@geotribu/110270184196372019) et [Twitter](https://twitter.com/geotribu/status/1651526470991245312), la nouvelle URL sera donc :

```url
https://geotribu.fr/
```

----

## Toutes ces routes mènent au site Geotribu

On parle bien ici de l'URL principale, celle de référence notamment pour les moteurs d'indexation et qui s'affiche dans la barre de votre navigateur web.
Mais différentes adresses mènent (ou mèneront) à cette URL :

```mermaid
flowchart TB
    A(http://www.geotribu.fr) -->|https| B
    B(https://www.geotribu.fr) -->|Redirection DNS| U
    C(http://geotribu.fr) -->|https| U
    D(http://www.geotribu.net) -->|https| E
    E(https://www.geotribu.net) -->|Redirection DNS| U
    F(http://geotribu.fr) -->|https| G
    G(https://geotribu.fr) -->|Redirection DNS| U
    U{"https://geotribu.fr/ <br /> (Apex)"}
```

Sans oublier le site miroir sur un autre serveur, quand les services de GitHub toussotent : <https://www2.geotribu.fr/>.

----

## Date effective du changement

Le changement sera effectif **aux alentours du 1er août**. Rien de mieux qu'une canicule et qu'un désert de consultation pour tout péter !

### Check-list pour que tout se passe bien

- [ ] mettre à jour son lecteur RSS avec la nouvelle adresse :
    - les nouveaux contenus : <https://geotribu.fr/feed_rss_created.xml>
    - les contenus mis à jour : <https://geotribu.fr/feed_rss_updated.xml>
- [ ] mettre à jour ses favoris (ou marque-pages) de navigateur

Merci de nous lire !

----

--8<-- "content/toc_nav_ignored/snippets/authors/geotribu.md"
