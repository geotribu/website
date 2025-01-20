---
title: Automatisation de publication des données de qualité de l'air sur Mastodon
subtitle: Brassons de l'air !
authors:
    - Guilhem Allaman
categories:
    - article
comments: true
date: 2024-04-04
description: Des cartes automatiques et géopulmonaires, sur le Fédivers, pour avertir des épisodes de pollution et de qualité de l'air en Ile-de-France et pas que
icon: material/air-conditioner
license: beerware
robots: index, follow
tags:
    - AirParif
    - API
    - Mastodon
    - Python
    - qualité de l'air
    - WMS
---

# Automatisation de publication des données de qualité de l'air sur Mastodon

:calendar: Date de publication initiale : 4 avril 2024

![logo AirParif](https://cdn.geotribu.fr/img/logos-icones/airparif.png){: .img-thumbnail-left }

Connaissez-vous [AirParif](https://www.airparif.fr/) ? Il s'agit de l'observatoire de la qualité de l'air en Ile-de-France, qui publie données, prévention et alertes sur les épisodes de pollution. Les données de l'association sont ouvertes, et il y a une API tout comme des flux OGC pour les récupérer.

![logo Mastodon](https://cdn.geotribu.fr/img/logos-icones/social/mastodon.png){: .img-thumbnail-left }

Connaissez-vous [Mastodon](https://fr.wikipedia.org/wiki/Mastodon_(r%C3%A9seau_social)) ? [Présenté par Julien récemment](./2024-02-16_de-twitter-a-mastodon-guide-geo-import-liste-comptes.md), il s'agit d'un réseau social décentralisé et ouvert (le Fédivers), pour les non-geeks tout comme les geeks, qui propose notamment une API permettant d'automatiser des posts.

Et si on combinait les deux ? Et si on développait un bot mastodon, qui publierait sur le réseau social les données et épisodes de pollution de l'air fournis par l'API d'AirParif ? Est-ce que ça servirait à quelque chose ? Pas sûr, ça reste à voir, personnellement j'en suis pas forcément convaincu. En plus il y a [l'application mobile](https://www.airparif.fr/actualite/2023/nouvelle-application-mobile-airparif) avec les notifications qui vont bien. Bon en tout cas c'est plus ou moins l'objet de cet article.

Dans cet article, vous l'aurez compris, on va donc :

👉 Dire des trucs

👉 Faire des machins

👉 Brasser un grand volume d'air

Mais pas seulement ! On va aussi, accessoirement, entre les lignes :

🦶 Découvrir (un peu) et utiliser l'API d'AirParif pour récupérer les données de qualité de l'air et d'épisodes de pollution

🦶 Développer un programme en python qui récupère et traite ces données

🦶 Découvrir (un peu) et utiliser l'API de Mastodon pour publier des toots automatiques

----

## Dénomination

La première chose à faire, c'est de trouver un nom à notre bot. Eh oui, le nommage c'est important pour ne pas s'emmêler les pinceaux.

Mais tout ça, c'est après une page de pub ! Qui pourrait vous intéresser si jamais votre qarosserie ou votre data a subi un impact...

----

![Qargrass répare, Qargrass remplace](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/airbot_mastodon_airparif/qargrass_repare_qargrass_remplace.webp){: .img-center loading=lazy }

 _Powered by :point_right: [OsGeo](https://www.osgeo.org/) :point_left: pour votre santé et vos trajets courts, veuillez privilégier 5 trajets à pied avec fruizélégumes ou en vélo par jour_

----

On est de retour sur Geotribu, et à ce stade de la dénomination de notre bot, la _short list_ est composée de 4 propositions : `Patrick`, `Patricia`, `Patrice`, et `air_bot`, avec ceci dit une légère préférence pour la dernière.

Et il n'y a pas que Paname dans la vie (il y a aussi la petite couronne), le nom `air_bot` est générique car le [nouvel indice ATMO](https://www.atmo-france.org/) a vocation à normaliser les données de qualité de l'air, et est implémenté notamment [au Bassin](https://www.atmo-nouvelleaquitaine.org/) et [sur la Côte d'Azur](https://www.atmosud.org/air-commune/Ville/13055/previsions). [Le reste](#viendez), désolé, on s'en fiche un peu... Ah si ! Il y a peut-être [la région dans les montagnes là](https://www.atmo-auvergnerhonealpes.fr/), c'est toujours sympa pour les parigots de respirer du bon air au ski... Mais les vrai.e.s sachent que [les Pyrénées](https://www.atmo-occitanie.org/occitanie#forecast_map) c'est aussi stylé ! Et pas qu'en hiver ou au [Tour de France](https://data.opendatasoft.com/explore/dataset/parcours-tour-de-france-a-montpellier-mediterranee-metropole%40occitanie/map/?flg=fr-fr&location=11,43.6354,3.87337&basemap=jawg.streets) !

## Gestion de l'environnement virtuel

Qui dit programme en Python ("programme en Python !") dit "gestion de l'environnement virtuel". Ici on va partir sur [poetry](https://python-poetry.org/), parce que quand même, un truc de geek qui s'appelle "poésie" ça claque ! _Where are thou, my dear `virtual_environment` ?_ Et quand on vient du Java comme moi, c'est toujours sympa d'avoir un endroit où tout est déclaré, ça rappelle toujours des bons souvenirs, n'est-ce pas Rémi F.

On peut utiliser `poetry` comme ceci :

```sh
# initialiser un nouveau projet
poetry init

# ajouter un paquet dans nos dépendances, en l'occurrence la lib mastodon python
poetry add mastodon-py

# lancer une commande dans notre environnement virtuel, exemple
poetry run python script_claque_au_sol.py --help
```

## API d'AirParif

Partons maintenant à la découverte des données AirParif via son API.

Mais tout ça, c'est après une page de pub, qui pourrait intéresser les viandards et les viandardes à côté du grill et parfois de la plaque cet été...

----

![Qing of the grid, Queen of the fid](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/airbot_mastodon_airparif/qing_of_the_grid_queen_of_the_fid.webp){: .img-center loading=lazy }

----

On est de retour sur Geotribu, et on va maintenant aborder l'API d'AirParif.

Il y a [un swagger](https://fr.wikipedia.org/wiki/Swagger_(logiciel)) qui liste [les interactions possibles](https://api.airparif.asso.fr/docs) via appel HTTP. Tout comme un flux [WMS](https://www.ogc.org/standard/wms/) sur les données en direct à l'adresse suivante : [https://magellan.airparif.asso.fr/geoserver/siteweb/wms](https://magellan.airparif.asso.fr/geoserver/siteweb/wms?request=GetCapabilities).

### Demande de duplicata

L'authentification pour un appel à l'API REST se fait grâce à une clé d'API, dont il faut faire [la demande à AirParif](https://www.airparif.fr/interface-de-programmation-applicative). Et [les prérogatives de la demande de duplicata](https://www.youtube.com/watch?v=2NiPaR0wjQY&pp=ygUgRnJhbsOnb2lzIGwnZW1icm91aWxsZSBkdXBsaWNhdGE%3D) sont plutôt rapides et la demande vite traitée, ce qui a été mon cas.

Pour le développement de ce bot, on aura besoin des données bulletin et prévisions, soit l'appel à [cette route](https://api.airparif.asso.fr/docs#/Indices/get_bulletin_indices_prevision_bulletin_get), qui fournit un texte écrit par le prévisionniste d'AirParif, tout comme les valeurs [des 4 polluants réglementés et surveillés](https://www.airparif.fr/surveiller-la-pollution/les-polluants-surveilles), en µg/m³ : NO2, O3, PM10 et PM25. On peut effectuer cet appel comme ceci en python :

```python linenums="1" title="API AirParif - requête bulletin"
import requests
from requests import Response

AIRPARIF_API_BASE_URL = "https://api.airparif.asso.fr"
AIRPARIF_API_KEY = "tralalilalère !"

# appel à l'API sur le endpoint /indices/prevision/bulletin avec la clé renseignée dans les headers HTTP
r: Response = requests.get(
    f"{AIRPARIF_API_BASE_URL}/indices/prevision/bulletin",
    headers={"X-Api-Key": AIRPARIF_API_KEY},
)

# vérification du code de retour de l'appel
r.raise_for_status()

# récupération des données JSON dans un dictionnaire
data = r.json()
```

### Récupération des données

Pour récupérer l'image carto de la qualité de l'air du moment, ça peut être fait via un appel au service WMS d'AirParif, comme ceci :

```python linenums="1" title="API AirParif - requête WMS"
from datetime import datetime
import requests
from requests import Response

AIRPARIF_WMS_BASE_URL = "https://magellan.airparif.asso.fr/geoserver/siteweb/wms"

# appel HTTP au service WMS d'AirParif
r: Response = requests.get(
    AIRPARIF_WMS_BASE_URL,
    params={
        "service": "WMS",
        "version": "1.1.0",
        "request": "GetMap",
        "layers": "siteweb:vue_indice_atmo_2020_com,Administratif:comm_idf,siteweb:idf_dept",
        "styles": "siteweb:nouvel_indice_polygones,poly_trait_blanc,poly_trait_blanc_50",
        "bbox": "530000.0,2335000.0,695000.0,2475000.0",
        "width": 600,
        "height": 500,
        "srs": "EPSG:27572",
        "format": "image/png",
        "format_options": "layout:bulletin",
    },
    stream=True,
)

# vérification du code de retour de l'appel (toujours !)
r.raise_for_status()

# enregistrement de l'image récupérée vers un fichier png, qui porte le nom de la date et l'heure
with open(f"airparif_idf_{datetime.now().strftime('%Y%m%d%H%M%S')}.png", "wb") as f:
    r.raw.decode_content = True
    shutil.copyfileobj(r.raw, f)
```

Une fois le code ci-dessus exécuté, on se retrouve avec l'image de la carte de la qualité de l'air du jour enregistrée sur le disque :

![Carte de la qualité de l'air du moment](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/airbot_mastodon_airparif/airparif_idf_20240304120032.webp){: .img-center loading=lazy }

!!! info
    La couche WMS appelée `siteweb:vue_indice_atmo_2020_com_jp1` permet de récupérer la carte du lendemain quand elle est disponible (à partir de 11h généralement).

## Mastodon automatique

Découvrons maintenant l'automatisation de posts sur le réseau social Mastodon, au travers de son API.

Mais tout ça, c'est après une page de pub, qui pourrait intéresser les mélomanes endiablé/es sur les campings cet été...

----

![La Qompile des tubes pour l'été, les meilleurs hits par DJ Frangis Qabrel](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/airbot_mastodon_airparif/qompile_frangis_qabrel.webp){: .img-center loading=lazy }

----

On est de retour sur Geotribu, et on va aborder la partie Mastodon, le réseau social sur lequel publiera notre bot.

### Choix de l'instance

Il nous faut à présent choisir une instance pour créer le compte de notre bot. Il y a deux options possibles à mes yeux :

- l'instance [botsin.space](https://botsin.space/about), "une instance pour les bots et les alliés des bots", qui est parfois instable du fait du zbeul qui règne dessus
- l'instance [mapstodon.space](https://mapstodon.space/about), mise en place pour les géo* grâce à [Jérémy](https://mapstodon.space/@jeremy) et les admins  
Ça part sur la deuxième option, merci Jérémy !

On peut suivre [l'article de Julien](./2024-02-16_de-twitter-a-mastodon-guide-geo-import-liste-comptes.md) pour dérouler la création d'un compte.

### Configuration du compte Mastodon

Configurons à présent le bot pour poster de manière automatique.

La première chose à faire est de cocher la case `This is an automated account` dans `Preferences` > `Public profile` :

![Écran case compte automatique dans les paramètres Mastodon](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/airbot_mastodon_airparif/ecran_mastodon_automated_account.webp){: .img-center loading=lazy }

Ensuite, il nous faudra créer une "Application" dans la partie `Development`, qu'on appelle ~~"Patrick"~~ "air_bot", en vérifiant que le scope `write` soit coché (pas besoin pour le moment des autres scopes). Tout ceci va nous permettre de récupérer un `access_token` permettant de nous connecter en python à l'API :

![Ecran application Mastodon](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/airbot_mastodon_airparif/ecran_mastodon_application_air_bot.webp){: .img-center loading=lazy }

!!! warning "Le token qui fout les j'tons"
    Il est conseillé de noter quelque part ce token, sur un post-it idéalement.

On programme aussi une suppression automatisée des posts, dans l'onglet "Automated post deletion", pour ne pas surcharger l'instance. On peut par exemple supprimer les toots postés il y a plus d'1 mois :

![Écran suppression automatique des posts](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/airbot_mastodon_airparif/ecran_mastodon_auto_delete.webp){: .img-center loading=lazy }

### API Mastodon

Mastodon permet d'automatiser des posts, et ce dans plusieurs langages de programmation. Nous allons donc utiliser l'API en python, dont la doc est disponible :point_right: [ici](https://mastodonpy.readthedocs.io/en/stable/) :point_left:

Pour notre besoin du moment, on pourra simplement utiliser la méthode [`status_post`](https://mastodonpy.readthedocs.io/en/stable/05_statuses.html#writing), qui permet de poster automatiquement des toots avec notre compte nouvellement créé :

![Ecran doc Mastodon méthode status_post](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/airbot_mastodon_airparif/ecran_doc_mastodon.webp){: .img-center loading=lazy }

!!! warning
    Selon les instances utilisées, la longueur max des posts est variable. Sur mapstodon.space la limite est de 500 caractères, émojis compris :heart: !

### Posts totomatiques

Utilisons maintenant l'API mastodon en python, comme ceci :

```python linenums="1" title="API Mastodon - post automatique"
from mastodon import Mastodon

MASTODON_INSTANCE = "https://mapstodon.space"
MASTODON_ACCESS_TOKEN = "tralalilalère !"

# création d'un objet connexion à Mastodon
mastodon = Mastodon(
    api_base_url=MASTODON_INSTANCE,
    access_token=MASTODON_ACCESS_TOKEN
)

# création et postage d'un toot automatique avec une image
mastodon.status_post(
    status="Bonjour 👋 le vrai sens de la vie réside dans le fromage 🧀💟",
    media_ids=[
        mastodon.media_post(
            "/chemin/vers/image/de/fromage.png",
            mime_type="image/png",
            description="Image du paradis",
        )
    ],
    visibility="unlisted",
    language="fr",
)
```

!!! info
    Ici on publie les posts en langue française et avec la visibilité "unlisted", ce qui signifie que les toots seront visibles pour les followers et sur la page de profil du bot, mais pas dans les "Live feeds" du serveur [mapstodon.space](https://mapstodon.space/public/local) ou [fédéré](https://mapstodon.space/public/remote). On évite de trop spammer les gens quoi.

## Et maintenant ?

Le code du bot implémenté avec AirParif est [disponible sur GitHub](https://github.com/gounux/air_bot).

Les posts automatiques du bot sont configurés de la manière suivante, tous les jours :

- le bulletin de la journée à 8h, avec la carte de la journée
- le bulletin du lendemain à 18h, avec la carte du lendemain
- les épisodes potentiels de pollution du lendemain à 19h

<iframe src="https://mapstodon.space/@air_bot/112055472229879411/embed" class="mastodon-embed" style="max-width: 100%; border: 0" width="400" allowfullscreen="allowfullscreen"></iframe>

### Viendez !

Nous venons de voir comment publier sur Mastodon les données d'AirParif. Or ce ne sont pas les seules données de qualité de l'air disponibles et ouvertes ! Les autres régions proposent également leurs services de données ouvertes ATMO :

- [Auvergne-Rhône-Alpes](https://www.atmo-auvergnerhonealpes.fr/)
- [Bourgogne-Franche-Comté](https://www.atmo-bfc.org/accueil)
- [Bretagne](https://www.airbreizh.asso.fr/)
- [Centre-Val de Loire](https://www.ligair.fr/)
- [Grand-Est](https://www.atmo-grandest.eu/)
- [Hauts-de-France](https://www.atmo-hdf.fr/)
- [Nouvelle-Aquitaine](https://www.atmo-nouvelleaquitaine.org/)
- [Normandie](https://www.atmonormandie.fr/)
- [Occitanie](https://www.atmo-occitanie.org/occitanie#forecast_map)
- [Pays de la Loire](https://www.airpl.org/)
- [Provence Alpes Côte d'Azur](https://www.atmosud.org/air-commune/Ville/13055/previsions)

Et ...

- [Corse](https://www.qualitaircorse.org/)

Et ...

- [Guyane](https://www.atmo-guyane.org/)
- [Antilles](https://www.gwadair.fr/)
- [La Réunion](https://atmo-reunion.net/)
- [Mayotte](https://www.hawa-mayotte.fr/)

Et enfin ...

- [ATMO France](https://www.atmo-france.org/)

Et aussi !

- la [carte](https://aqicn.org/map/belgium/fr/) de pollution de l'air en [Belgique une fois](https://www.wallonair.be/fr/mesures/mesures-en-direct.html)

:loudspeaker: N'hésitez pas à contribuer à ce bot, ou à en créer d'autres pour diffuser les données de votre région / pays ! Je suis disponible pour fournir des `access_token` et publier les données via ce bot [air_bot@mapstodon.space](https://mapstodon.space/@air_bot).

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
