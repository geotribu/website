---
title: Geotribu déménage
subtitle: Attachez vos ceintures de favoris
authors:
    - Geotribu
categories:
    - article
date: "2023-05-05 10:20"
description: Après 3 ans sur un sous-domaine, le site va revenir sur son domaine principal. Attachez vos ceintures de favoris navigateurs !
image:
license: default
robots: index, follow
tags:
    - Geotribu
---

# Changement d'URL du site Geotribu cet été

:calendar: Date de publication initiale : 5 mai 2023

Voilà 3 ans que Geotribu est de retour après une coupure de service.  
3 ans que ce nouveau site est en place.  
3 ans à en améliorer l'ergonomie, les fonctionnalités et surtout à réintégrer et nettoyer les anciens contenus.  
3 ans qu'il est accessible sur <https://static.geotribu.fr>

Il est temps de rebasculer

Après les sondages sur [Mastodon](https://mapstodon.space/@geotribu/110270184196372019) et [Twitter](https://twitter.com/geotribu/status/1651526470991245312), la nouvelle URL sera donc :

`https://geotribu.fr/`
{: align=middle }

----

## Toutes ces routes mènent au site Geotribu

On parle bien ici de l'URL principale, celle de référence notamment pour les moteurs d'indexation et qui l'adresse finale qui s'affiche dans la barre de votre navigateur web.
Mais différentes adresses mènent à cette URL :

```mermaid title="Schéma des URLs Geotribu"
flowchart TB
    A(http://www.geotribu.fr) -->|https| B
    B(https://www.geotribu.fr) -->|Redirection DNS| U
    C(http://geotribu.fr) -->|https| U
    D(http://geotribu.net) -->|https| E
    E(https://www.geotribu.net) -->|Redirection DNS| U
    U{{"https://geotribu.fr/\n(Apex)"}}

    click A href "http://www.geotribu.fr"
    click B href "https://www.geotribu.fr"
```

Sans oublier le site miroir sur un autre serveur, quand les services de GitHub toussotent : <https://www2;geotribu.fr/>.

----

## Changements

### Check-list pour que tout se passe bien

- [ ] mettre à jour son lecteur RSS avec la nouvelle adresse :
    - les nouveaux contenus : <https://geotribu.fr/feed_rss_created.xml>
    - les contenus mis à jour : <https://geotribu.fr/feed_rss_updated.xml>
- [ ]

----

## Auteur {: data-search-exclude }

--8<-- "content/toc_nav_ignored/snippets/authors/geotribu.md"
