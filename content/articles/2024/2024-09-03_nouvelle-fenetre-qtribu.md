---
title: Cherchez et contribuez à Geotribu depuis ArqGIS
subtitle: La porte ouverte à toutes les qontributions
authors:
    - Geotribu
    - Guilhem Allaman
categories:
    - article
comments: true
date: 2024-09-03
description: "Une nouvelle fenêtre des contenus Geotribu dans le plugin ArqGIS QTribu, qui permet d'accéder et de contribuer aux contenus du site"
icon: material/window-closed-variant
image:
license: beerware
robots: index, follow
tags:
    - Geotribu
    - ArqGIS
    - news
    - plugin
---

# Cherchez et contribuez à Geotribu depuis ArqGIS

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

T'as découvert un super géo-outil et t'aimerais faire profiter ta découverte au plus grand nombre ?  
T'es tombé sur un super article dans une autre langue et t'aimerais rendre cet article disponible pour les francophones ?  
Tu travailles sur un projet sympa et t'aimerais le présenter et le diffuser ?  
T'as participé à une conférence ou un géo-évènement et t'aimerais partager aux autres ce que t'as appris ?  
T'as envie d'évoluer dans ton job en montrant ce que tu sais faire ?  
T'as envie de fanfaronner à la machine à café (ou sur le slack/IRC, faut vivre avec son temps !) parce que ton nom est incrusté dans ArqGIS ?  
T'as envie de partager tous les bons plans géo de ta région ?  
Tu t'ennuies un peu à la plage et l'horizon bleu de la mer t'inspire ?  
Tu trouves que les flux RSS et plus généralement les mails et les newsletters c'est trop de la BAL ?  
T'as loupé ta dernière séance chez ton/ta *PSIG*[^1] et tu ressens le besoin de te confier ?  
T'en as un peu marre du tutoiement récurrent ?

Vous êtes au bon endroit. Eh mais ce serait pas un topito des raisons de contribuer à Geotribu ? Oui ! Mais pas seulement : surtout pas besoin de cliquer sur [ce lien](https://theuselessweb.com/), c'est ici que ça se passe !

Les contenus et contributions de Geotribu sont maintenant disponibles dans [ArqGIS](https://www.qgis.org), au travers d'une nouvelle fenêtre du [plugin QTribu](https://plugins.qgis.org/plugins/qtribu/), le plugin pour garder le Qontact.

## Plugin QTribu

![logo ArqGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo ArqGIS"){: .img-thumbnail-left }

Présentée un 1er avril par [Julien](../../team/julien-moura.md) au travers de [cet article](../2021/2021-04-01_qtribu_plugin_qgis_geotribu.md), l'extension `QTribu` est disponible dans ArqGIS via [le dépôt officiel](https://plugins.qgis.org/plugins/qtribu/) :

![fenêtre du gestionnaire des extensions ArqGIS avec QTribu sélectionnée](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/qtribu-qgis-plugin.webp){: .img-center loading=lazy }

## Fenêtre des contenus

La fenêtre pour lister et rechercher parmi les contenus de Geotribu est disponible dans le menu `Internet`, puis `Qtribu` > `Rechercher dans les contenus` :

![fenêtre des contenus Geotribu](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/qtribu-nouvelle-fenetre.webp){: .img-center loading=lazy }

Les articles et GeoRDP peuvent être filtrés par auteur/ice, par mot-clé ou via une recherche texte.

Sous le capot, c'est le [JSON feed de Geotribu](https://geotribu.fr/feed_json_created.json) qui est utilisé afin de récupérer les 50 derniers contenus, articles et GeoRDP, puis les afficher.

## Les contenus de Geotribu

À ce moment-là, il peut être judicieux de faire un petit rappel sur les contenus de Geotribu auxquels tout un chacun peut participer, via un [ticket Github](https://github.com/geotribu/website/issues/new/choose) ou donc via le plugin ArqGIS `QTribu`, et qui peuvent être de deux natures :

- une news/brève pour une GeoRDP. Généralement plutôt courte, il s'agit de décrire une actualité géomatique pouvant être de différent type : sortie d'un logiciel, nouvelle version d'un outil, sortie d'un article, annonce ou rétrospective sur un évènement géo, actualité OpenStreetMap ...etc etc Il y a même une rubrique "Divers" pour les news qui ne rentrent dans aucune case, c'est libre et seulement limité par votre imagination ! [Le site de contribution](https://contribuer.geotribu.fr/rdp/add_news/) explique la démarche

- un article. Pour celles et ceux qui pensent que c'est la taille qui compte, c'est l'occasion de s'étendre davantage (certaines mauvaises langues diraient "tartiner"), illustré avec des images, des bouts de code et autres, offrant ainsi la possibilité de montrer l'utilisation ou la découverte d'un outil, un partage d'expérience, un récapitulatif illustré d'un évènement, une présentation d'un projet auquel vous participez, ou non... etc [Le site de contribution](https://contribuer.geotribu.fr/articles/workflow/) explique la démarche

Et tout ceci sans pression et dans la bonne humeur ! Il est même possible d'insérer des blagues un peu douteuses, comme par exemple :

- mon premier est un langage de programmation assez utilisé dans les SIG. Il s'agit également d'un serpent :snake:
- mon second peut être vectoriel, et peut également être utilisé en toiture
- mon tout contient du liquide pour graisser les chaînes de vélo, en Alsace
- :question: Je suis je suis je suis ?

![Julien Lepers - Je suis je suis ?](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/julien_lepers_je_suis.webp){: .img-center loading=lazy }

??? question "Réponse"
    Un python tuile !!

## Send news

Revenons à nos moutons, et à nos actions de contribution dans le plugin ArqGIS QTribu : l'action `Proposer une news` vous ouvrira un formulaire pour saisir une news à destination d'une future GeoRDP (menu `Internet` > `QTribu`) :

![formulaire de saisie d'une news](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/qtribu-news.webp){: .img-center loading=lazy }

Le bouton `Envoyer` vous conduira directement sur les rails d'une issue GitHub paramétrée et remplie comme il faut !

![gif conducteur à toute berzingue](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/gif-drive.gif){: .img-center loading=lazy }

## Propositions d'articles

L'action `Proposer un article` vous ouvrira un formulaire pour rédiger une ébauche d'article :

![formulaire de saisie d'un article](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/qtribu-article.webp){: .img-center loading=lazy }

Le bouton `Envoyer` vous conduira directement sur les rails d'une issue GitHub paramétrée et remplie comme il faut !

![gif cycliste à toute berzingue](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/gif-bicycle.gif){: .img-center loading=lazy }

## Autres nouveautés de Geotribu

Parmi les autres évolutions récentes de Geotribu, nous pouvons citer :

- une [nouvelle page](https://geotribu.fr/team/) qui liste les membres ainsi que les contributeur·rices
- plus de qualitay dans l'automatisation de la chaîne de publication des contenus
- bientôt un [plugin QField](https://www.opengis.ch/2024/06/18/supercharge-your-fieldwork-with-qfields-project-and-app-wide-plugins/) ?
- et bientôt d'autres trucs marrants :wink: :smile_cat:

![un petit chat trop 'gnon qui dit "Miaou" dans ArqGIS avec le plugin Geotribu](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qtribu_nouvelle_fenetre/geotricat_qgis_meow.webp)

<!-- Footnotes reference -->
[^1]: PSIG : psy des SIG, profession réglementée

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
