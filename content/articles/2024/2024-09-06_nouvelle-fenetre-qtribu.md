---
title: Nouvelle fenêtre des contenus Geotribu dans QGIS
subtitle: Fenêtre ou ne pas fenêtre, telle est la question
authors:
    - Geotribu
    - Guilhem Allaman
categories:
    - article
comments: true
date: 2024-09-06
description: "Une nouvelle fenêtre des contenus Geotribu dans le plugin QGIS QTribu, qui permet d'accéder et de contribuer aux contenus du site"
icon: material/window-closed-variant
image:
license: beerware
robots: index, follow
tags:
    - article
    - Geotribu
    - QGIS
    - news
    - plugin
---

# Une nouvelle fenêtre des contenus Geotribu dans QGIS

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

T'as découvert un super géo-outil et t'aimerais faire profiter ta découverte au plus grand nombre ?  
T'es tombé sur un super article dans une autre langue et t'aimerais rendre cet article disponible pour les francophones ?  
Tu travailles sur un projet sympa et t'aimerais le présenter et le diffuser ?  
T'as participé à une conférence ou un géo-évènement et t'aimerais partager aux autres ce que t'as appris ?  
T'as envie d'évoluer dans ton job en montrant ce que tu sais faire ?  
T'as envie de fanfaronner à la machine à café (ou sur le slack/IRC, faut vivre avec son temps !) parce que ton nom est incrusté dans QGIS ?  
T'as envie de partager tous les bons plans géo de ta région ?  
Tu t'ennuies un peu à la plage et l'horizon bleu de la mer t'inspire ?  
Tu trouves que les flux RSS et plus généralement les mails et les newsletters c'est trop de la BAL ?  
T'as loupé ta dernière séance chez ton/ta *PSIG*[^1] et tu ressens le besoin de te confier ?  
T'en as un peu marre du tutoiement récurrent ?

Vous êtes au bon endroit. Eh mais ce serait pas un topito des raisons de contribuer à Geotribu ? Oui ! Mais pas seulement : surtout pas besoin de cliquer sur [ce lien](https://theuselessweb.com/), c'est ici que ça se passe !

Les contenus et contributions de Geotribu sont maintenant disponibles dans [QGIS](https://www.qgis.org), au travers d'une nouvelle fenêtre du [plugin QTribu](https://plugins.qgis.org/plugins/qtribu/), le plugin pour garder le Qontact.

## Plugin QTribu

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-thumbnail-left }

Présentée un 1er avril par [Julien](../../team/julien-moura.md) au travers de [cet article](../2021/2021-04-01_qtribu_plugin_qgis_geotribu.md), l'extension `QTribu` est disponible dans QGIS via le dépôt officiel :

![fenêtre du gestionnaire des extensions QGIS avec QTribu sélectionnée](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/qtribu-qgis-plugin.webp)

## Fenêtre des contenus

La fenêtre pour lister et rechercher parmi les contenus de Geotribu est disponible dans le menu `Internet`, puis `Qtribu` > `Rechercher dans les contenus` :

![fenêtre des contenus Geotribu](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/qtribu-nouvelle-fenetre-contenus.webp)

Les articles et GeoRDP peuvent être filtrées par auteur/ice, par mot-clé ou via une recherche texte.

Sous le capot, c'est le [JSON feed de Geotribu](https://geotribu.fr/feed_json_created.json) qui est utilisé afin de récupérer les 50 derniers contenus, articles et GeoRDP, puis les afficher.

## Send news

L'action `Proposer une news` vous ouvrira un formulaire pour saisir une news à destination d'une future GeoRDP.

![formulaire de saisie d'une news](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/qtribu-news-form.webp)

Le bouton `Envoyer` vous conduira directement sur les rails d'une issue GitHub paramétrée et remplie comme il faut !

![gif conducteur à toute berzingue](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/gif-drive.gif)

## Propositions d'articles

L'action `Proposer un article` vous ouvrira un formulaire pour saisir un article à destination d'une future GeoRDP.

![formulaire de saisie d'un article](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/qtribu-article-form.webp)

Le bouton `Envoyer` vous conduira directement sur les rails d'une issue GitHub paramétrée et remplie comme il faut !

![gif cycliste à toute berzingue](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/gif-bicycle.gif)

## Autres nouveautés de Geotribu

Parmi les autres évolutions récentes de Geotribu, nous pouvons citer :

- une [nouvelle page](https://geotribu.fr/team/) qui liste les membres ainsi que les contributeur/rices
- plus de qualitay dans l'automatisation de la chaîne de publication des contenus
- la [rétrospective Gource](https://www.youtube.com/watch?v=cHQzkNkLeW8) des contributions de 2023 au site
- bientôt un [plugin QField](https://www.opengis.ch/2024/06/18/supercharge-your-fieldwork-with-qfields-project-and-app-wide-plugins/) ?
- et bientôt d'autres trucs marrants :wink:

<!-- Footnotes reference -->
[^1]: PSIG : psy des SIG, profession réglementée

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
