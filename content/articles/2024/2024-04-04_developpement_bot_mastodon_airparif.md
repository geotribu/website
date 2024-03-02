---
title: Développement d'un bot Mastodon avec les données AirParif
subtitle: Brassons de l'air !
authors:
    - Guilhem Allaman
categories:
    - article
comments: true
date: 2024-04-04
description: Des cartes automatiques et géopulmonaires, sur le Fédivers, pour avertir des épisodes de pollution et de qualité de l'air en Île-de-France
icon: material/air-conditioner
license: beerware
robots: index, follow
tags:
    - AirParif
    - bot
    - mastodon
    - python
---

# Développement d'un bot Mastodon avec les données AirParif

:calendar: Date de publication initiale : 4 avril 2024

Connaissez-vous [AirParif](https://www.airparif.fr/) ? Il s'agit de l'observatoire de la qualité de l'air en Île-de-France, qui publie données, prévention et alertes sur les épisodes de pollution. Les données de l'association sont ouvertes, et il y a une API tout comme des flux OGC pour les récupérer.

Connaissez-vous [Mastodon](https://fr.wikipedia.org/wiki/Mastodon_(r%C3%A9seau_social)) ? [Présenté par Julien récemment](./), il s'agit d'un réseau social décentralisé et ouvert (le Fédivers), pour les non-geeks tout comme les geeks, qui propose notamment une API permettant d'automatiser des posts.

Et si on conciliait les deux ? Et si on développait un bot mastodon, qui publierait sur le réseau social les données et épisodes de pollution de l'air fournis par l'API d'AirParif ? Est-ce que ça servirait à quelque chose ? Pas sûr, ça reste à voir, personnellement j'en suis pas forcément convaincu. En plus il y a [l'application mobile](https://www.airparif.fr/actualite/2023/nouvelle-application-mobile-airparif) avec les notofications qui vont bien. Bon en tout cas c'est plus ou moins l'objet de cet article. Après tout, un brin d'astroturfing ne fait jamais de mal, alors pourquoi pas nous ? *Why not oui* ?

Dans cet article, vous l'aurez compris, on va donc :

👉 Dire des trucs 

👉 Faire des machins

👉 Brasser un grand volume d'air

Mais pas seulement ! On va aussi, accessoirement, entre les lignes :

🦶 Découvrir et utiliser l'API d'AirParif pour récupérer les données de qualité de l'air et d'épisodes de pollution

🦶 Développer un programme en python qui récupère et traite ces données

🦶 Découvrir et utiliser l'API de Mastodon pour publier des posts totomatiques 

---

La première chose à faire, c'est de trouver un nom à notre bot. Eh oui, le nommage c'est important pour ne pas s'emmêler les pinceaux.

Mais tout ça, après une page de pub ! Eh oui, rien n'est gratuit... enfin si !

Une page de réclame donc, qui pourrait vous intéresser si jamais votre qarosserie ou votre data a subi un impact...

![Qargrass répare, Qargrass remplace](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/airbot_mastodon_airparif/qargrass_repare_qargrass_remplace.webp)

---

## Dénomination

On est de retour sur Geotribu, et à ce stade de la dénomination de notre bot, la short list est composée de 4 propositions : `Patrick`, `Patricia`, `Patrice`, et `air_bot`, avec ceci dit une légère préférence pour la dernière.

À ce moment-là, bon, il y sûrement quelque chose qui doit vous sauter aux yeux. AirParif ? Genre à Paris ?? Attends, y'a encore des gens qui habitent à Paris ? Sérieux ?!? Après tout ce qu'il s'est passé récemment : la grève des éboueurs, la réélection d'Annie, l'épidémie de CoDir19, l'élimination habituelle de l'EPSG en Ligue des Champions... Nan sérieux il y a toujours des gens qui habitent à Paris ? Nan mais réveillez-vous wesh ! Nan mais allô quoi.

## Gestion de l'environnement virtuel

Qui dit programme en python ("programme en python !") dit "gestion de l'environnement virtuel". Ici on va partir sur [poetry](https://python-poetry.org/), parce que quand même, un truc de geek qui s'appelle "poésie" ça claque ! _Where are thou, my dear `virtual_environment` ?_

## API d'AirParif

Partons maintenant à la découverte des données AirParif via son API.

Mais tout ça, c'est après une page de pub, qui pourrait intéresser les viandards et les viandardes au bord du grill cet été...

![Qing of the grid, Queen of the fid](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/airbot_mastodon_airparif/qing_of_the_grid_queen_of_the_fid.webp)

---

On est de retour sur Geotribu ...

### Demande de duplicata

- explication de la démarche pour demander un clé d'API
- description brève de l'API

### Récupération des données

- récupération de l'image du jour et/ou du lendemain via [appel WMS](https://magellan.airparif.asso.fr/geoserver/siteweb/wms?service=WMS&version=1.1.0&request=GetMap&layers=siteweb:vue_indice_atmo_2020_com,Administratif:comm_idf,siteweb:idf_dept&styles=siteweb:nouvel_indice_polygones,poly_trait_blanc,poly_trait_blanc_50&bbox=530000.0,2335000.0,695000.0,2475000.0&width=600&height=487&srs=EPSG:27572&format=image/png&format_options=layout:bulletin)
- récupération via appel API REST données épisode

## API de mastodon

Découvrons maintenant l'automatisation de posts sur le réseau social Mastodon, au travers de son API.

Mais tout ça, c'est après une page de pub, qui pourrait intéresser les mélomanes endiablé/es sur les campings cet été...

![La Qompile des tubes pour l'été, les meilleurs hits par DJ FranGIS Qabrel](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/airbot_mastodon_airparif/qompile_frangis_qabrel.webp)

---

On est de retour sur Geotribu ...

### Choix de l'instance

- botsin.space ? mapstodon.space ?
- création compte (avec case `bot` cochée)

### Posts totomatiques

- description de la démarche pour créer une application et récupérer un access token sur l'interface web de mastodon
- ajout du paquet `mastodon-py` au `pyproject.toml`
- description brève de l'API, notamment l'unique fonction qu'on utilise

## Et maintenant ?

- lien dépôt GitHub `air_bot`
- commande pour lancer un post totomatique
- tâche cron périodique :
  - à 8h pour publier la carte des prévisions du jour
  - le soir à disons 22h pour vérifier si épisode le lendemain (post uniquement si oui)
- embarquer un toot du compte mastodon du bot en prod
- appel à contribution pour publier les données des autres villes
- finir sur [nouvel indice ATMO](https://www.airparif.fr/2020/webinaire-sur-le-lancement-du-nouvel-indice-de-qualite-de-lair)

## Auteur

--8<-- "content/team/gall.md"

{% include "licenses/beerware.md" %}
