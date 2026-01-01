---
title: Expérimentations avec le plugin Cornelis
subtitle: Peuchère Escher
authors:
    - Guilhem ALLAMAN
categories:
    - article
comments: true
date: 2026-02-06
description: Découverte et expérimentations avec le plugin Cornelis, pour mimer la lithographie façon Maurits Cornelis Escher.
icon: fontawesome/solid/paintbrush
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/decouverte_plugin_cornelis/cornelis_tesselation_final.png
tags:
    - Cornelis
    - QGIS
---

# Expérimentations avec le plugin Cornelis

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![icone art SIG](https://cdn.geotribu.fr/img/logos-icones/divers/artsig.png){: .img-thumbnail-left }

Connaissez-vous l'artiste [M.C. Escher](https://fr.wikipedia.org/wiki/Maurits_Cornelis_Escher) ? Il y a quelques temps, j'aurais répondu non à cette question, issu d'un cursus académique lors duquel j'ai appris à manier les pointeurs plutôt que les pinceaux. Et encore...

Il s'agit d'un artiste néerlandais du XXe siècle, connu notamment pour ses gravures sur bois et [lithographies](https://fr.wikipedia.org/wiki/Lithographie), souvent inspirées des mathématiques et des motifs de l'art islamique.

![Reptiles de M.C. Escher](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/decouverte_plugin_cornelis/Study_of_Regular_Division_of_the_Plane_with_Reptiles.webp){: .img-center loading=lazy }

_[Reptiles](https://en.wikipedia.org/wiki/Reptiles_(M._C._Escher)) de M.C. Escher_

Il a notamment été influencé par les motifs du [palais de l'Alhambra, à Grenade](https://fr.wikipedia.org/wiki/Alhambra_(Grenade)) :

![Alhambra par Juan Laurent, c. 1874, Department of Image Collections [archive], National Gallery of Art Library, Washington, D.C.](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/decouverte_plugin_cornelis/Alhambra_by_Juan_Laurent.webp){: .img-center loading=lazy }

Je suis personnellement plutôt sensible à cet art, et une récente découverte d'outillage QGIS permet de relier ceci avec les SIG !

## Un plugin QGIS : Cornelis

Dans l'activité de géo-veille qu'on aime bien faire avec la Geotribu, il y a quelques temps on est tombé sur ce post mastodon, qui laisse un peu sans voix...

<!-- markdownlint-disable MD033 -->

<blockquote class="mastodon-embed" data-embed-url="https://mapstodon.space/@geum/114236294753939621/embed" style="background: #FCF8FF; border-radius: 8px; border: 1px solid #C9C4DA; margin: 0; max-width: 540px; min-width: 270px; overflow: hidden; padding: 0;"> <a href="https://mapstodon.space/@geum/114236294753939621" target="_blank" style="align-items: center; color: #1C1A25; display: flex; flex-direction: column; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', Roboto, sans-serif; font-size: 14px; justify-content: center; letter-spacing: 0.25px; line-height: 20px; padding: 24px; text-decoration: none;"> <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="32" height="32" viewBox="0 0 79 75"><path d="M63 45.3v-20c0-4.1-1-7.3-3.2-9.7-2.1-2.4-5-3.7-8.5-3.7-4.1 0-7.2 1.6-9.3 4.7l-2 3.3-2-3.3c-2-3.1-5.1-4.7-9.2-4.7-3.5 0-6.4 1.3-8.6 3.7-2.1 2.4-3.1 5.6-3.1 9.7v20h8V25.9c0-4.1 1.7-6.2 5.2-6.2 3.8 0 5.8 2.5 5.8 7.4V37.7H44V27.1c0-4.9 1.9-7.4 5.8-7.4 3.5 0 5.2 2.1 5.2 6.2V45.3h8ZM74.7 16.6c.6 6 .1 15.7.1 17.3 0 .5-.1 4.8-.1 5.3-.7 11.5-8 16-15.6 17.5-.1 0-.2 0-.3 0-4.9 1-10 1.2-14.9 1.4-1.2 0-2.4 0-3.6 0-4.8 0-9.7-.6-14.4-1.7-.1 0-.1 0-.1 0s-.1 0-.1 0 0 .1 0 .1 0 0 0 0c.1 1.6.4 3.1 1 4.5.6 1.7 2.9 5.7 11.4 5.7 5 0 9.9-.6 14.8-1.7 0 0 0 0 0 0 .1 0 .1 0 .1 0 0 .1 0 .1 0 .1.1 0 .1 0 .1.1v5.6s0 .1-.1.1c0 0 0 0 0 .1-1.6 1.1-3.7 1.7-5.6 2.3-.8.3-1.6.5-2.4.7-7.5 1.7-15.4 1.3-22.7-1.2-6.8-2.4-13.8-8.2-15.5-15.2-.9-3.8-1.6-7.6-1.9-11.5-.6-5.8-.6-11.7-.8-17.5C3.9 24.5 4 20 4.9 16 6.7 7.9 14.1 2.2 22.3 1c1.4-.2 4.1-1 16.5-1h.1C51.4 0 56.7.8 58.1 1c8.4 1.2 15.5 7.5 16.6 15.6Z" fill="currentColor"/></svg> <div style="color: #787588; margin-top: 16px;">Post by @geum@mapstodon.space</div> <div style="font-weight: 500;">View on Mastodon</div> </a> </blockquote> <script data-allowed-prefixes="https://mapstodon.space/" async src="https://mapstodon.space/embed.js"></script>

<!-- markdownlint-enable MD033 -->

Waouh ! Possible de décliner des motifs dans QGIS grâce à ce plugin !

Styley, et [le _README_ du dépôt GitHub du plugin](https://github.com/xcaeag/Cornelis-QGis-Plugin) est vraiment magnifique :star_struck: !

Cet article aurait simplement pu reprendre ce _README_, qui est une oeuvre d'art en soi, ceci dit j'ai aussi voulu essayer ce plugin avec un autre truc que j'aime bien faire : des cartes psychédéliques dans QGIS avec des projections random.

## Création d'un "fond de carte" en guise de base au motif

De temps à autre, je prends donc mon pied à créer des cartes, dans QGIS, avec un SCR random, histoire d'en découvrir quelques uns, histoire d'admirer les artefacts des reprojections géodésiques et les glitchs du _rendering_ de QGIS :two_hearts:...

En voici une réalisée, en période post-Noël, dont voici, dans les grandes lignes, la recette de création :

1. Ouvrir un nouveau projet vide dans QGIS.

1. Tapper "`world`" dans la barre des coordonnées de QGIS. Il s'agit ici d'un _easter egg_, et vous pouvez [en découvrir d'autres dans cet article](../2022/2022-04-18_easter_eggs_qgis_regale.md) de [Delphine](../../team/delphine-montagne.md) et [Julien](../../team/julien-moura.md). Concrètement, cette action va ajouter une carte du monde avec la projection `EPSG:4326` dans le canvas de QGIS.

1. Créer une grille avec l'algorithme de processing adéquat, en essayant différentes tailles.

1. Ouvrir le dialogue du choix du SCR du projet QGIS actuel, explorer et se lâcher. Parfois j'utilise un générateur de nombres aléatoires, ceci dit QGIS affiche parfois un message disant l'impossibilité de reprojeter, ce qui je dois l'avouer dépasse mon champ d'intervention. Ici j'ai pris [le SCR _ESRI:102036_](https://spatialreference.org/ref/esri/102036/), soit le "South Pole Gnomonic" :smirk: En plus - le hasard fait bien les choses, j'avais regardé la veille [ce super documentaire, sur les traces du manchot empereur en Antarctique](https://www.arte.tv/fr/videos/060769-000-A/antarctica-sur-les-traces-de-l-empereur/)...

1. Jouer avec les symbologies, les couleurs de remplissages, les bordures, etc... Personnellement j'aime bien le jaune, pas seulement parce que c'est rafraîchissant en été à l'apéro, mais aussi parce que c'est la couleur par défaut de la sélection dans QGIS !

Et voici la carte finale :

![Carte géométrique faisant usage du SCR ESRI:102036](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/decouverte_plugin_cornelis/esri102036.webp){: .img-center loading=lazy }

## Création d'un pavage avec le plugin Cornelis

Maintenant, installons et utilisons [le plugin Cornelis](https://plugins.qgis.org/plugins/Cornelis) pour créer et décliner des motifs sur base de cette "carte".

À noter que ce plugin est en mode expérimental, il vous faudra donc activer les plugins expérimentaux dans vos paramètres.

Une fois installé, une boîte à outils vient s'intégrer dans QGIS. Voyons ce qu'elle fournit et comment créer des motifs.

![Choix du type de pavage dans la boîte à outils du plugin Cornelis](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/decouverte_plugin_cornelis/cornelis_tesselation_menu_choice.webp){: .img-center loading=lazy }

Il y a différents types de pavages disponibles, avec une image qui permet de prévisualiser ce que ce type de pavage fera.

Une fois le type de pavage choisi, celui-ci est visible dans le canvas de QGIS, et peut être modifié / affiné à souhait :

![Dessin d'un pavage dans QGIS avec le plugin Cornelis](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/decouverte_plugin_cornelis/cornelis_tesselation_drawing.webp){: .img-center loading=lazy }

Il est possible de déplacer le motif, rajouter ou supprimer des sommets, changer d'échelle, etc. Ainsi que sauvegarder puis recharger un tel pavage sous forme de fichier `.pav` grâce aux deux derniers boutons de la boîte à outils.

## Génération de la carte pavée

Une fois le pavage dessiné, on lance la génération de la carte grâce au bouton adéquat.

À noter que les géométries des couches vectorielles visibles qui intersectent le motif de base seront utilisées, et les motifs générés placés sous forme de couches temporaires dans un nouveau groupe de _layers_ QGIS.

Voici le résultat final de l'expérimentation :

![Résultat final - carte pavée 1 avec le plugin Cornelis](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/decouverte_plugin_cornelis/cornelis_tesselation_final_1.png){: .img-center loading=lazy }

Et avec une autre tesselation :

![Résultat final - carte pavée 2 avec le plugin Cornelis](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/decouverte_plugin_cornelis/cornelis_tesselation_final_2.png){: .img-center loading=lazy }

Un processus très sympa à dérouler, et j'apprécie particulièrement les capacités artistiques de QGIS qui ne sont plus à démontrer, et enrichies grâce à ce plugin Cornelis que je vous invite à essayer sur vos données vecteur !

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
