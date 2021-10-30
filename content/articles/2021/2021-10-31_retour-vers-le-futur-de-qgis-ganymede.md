---
title: "A la redécouverte de QGIS 0.x"
authors:
    - Julien MOURA
categories:
    - article
date: "2021-10-31 10:20"
description: "Tiens et si on installait QGIS 0.9 Ganymède en 2021 et qu'on essayait de faire une carte ? Petit voyage dans le temps."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_0-9_ganymede_splash.png"
tags:
    - Halloween
    - QGIS
---

# Retour vers le futur de QGIS

:calendar: Date de publication initiale : 31 octobre 2021

## Introduction

![icône citrouille](https://cdn.geotribu.fr/img/logos-icones/divers/citrouille.png "icône citrouille"){: .img-rdp-news-thumb }

Ces jours-ci je formais quelques éminents membres des [CEN](https://fr.wikipedia.org/wiki/Conservatoire_d%27espaces_naturels) sur [le déploiement de QGIS sur un parc informatique](https://oslandia.com/formations/qgis9-administration-dun-parc-qgis/) (principalement Windows) et, lors d'une de mes rares digressions, j'ai eu l'inspiration de télécharger la version la plus ancienne de QGIS encore disponible au téléchargement.

![QGIS 0.9.1 Ganymede - Splash](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_0-9_ganymede_splash.png "QGIS 0.9.1 Ganymede - Splash"){: .img-center loading=lazy }

Alors, plus de 12 ans après [notre article "A la découverte de Quantum GIS 1.0.0"](/articles/2009/art_2009-08-28/), pour fêter la Toussaint / Halloween, je vous propose d'exhumer Quantum GIS 0.x et de voir si le cadavre bouge encore :skull: :headstone:.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Installation

![Ancien logo de QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis_old.png "Ancien logo de QGIS"){: .img-rdp-news-thumb }

Le site officiel indique [où trouver les anciennes versions](https://download.osgeo.org/qgis/), y'a plus qu'à se servir. J'ai opté pour la plus vieille : la [0.9.1 Ganymède, mise en ligne le 18 décembre 2017](https://download.osgeo.org/qgis/windows/qgis_setup0.9.1.18_12_2007.exe).

Lancer l'installateur en mode administrateur et quelques instants plus tard, c'est bon : Quantum GIS est dans Program Files x86 de Windows 10 :men_with_bunny_ears_partying:.

[![QGIS 0.9 About](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_0-9-1x_about.png "QGIS 0.9 About"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_0-9-1x_about.png){: data-mediabox="lightbox-gallery" data-title="QGIS 0.9 - A propos"}

### Le poids des ans

La première chose que l'on remarque, c'est que comme bon nombre d'entre nous, QGIS a pris du poids avec les années :

- l'installateur pesait alors 65 Mo contre 1 Go pour le MSI de la 3.20
- le dossier d'installation environ 210 Mo, contre 2.22 Go pour la 3.20

![Installation QGIS 0.11](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_0x_size_installed.png "Taille de l'installation de QGIS 0.11"){: loading=lazy width=350px }
![Installation QGIS 3.20](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_320_size_installed.png "Taille de l'installation de QGIS 3.20"){: loading=lazy width=350px }
{: align=middle }

----

## Retour aux sources

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-rdp-news-thumb }

Mais qu'y avait-il donc dans Quantum GIS avant même sa version 1, seuil conventionnel de stabilisation d'un logiciel ?  
A l'époque où [Esri investissait près de 20% de son CA en R&D, sortait ArcExplorer, ArcGIS for AutoCAD et amorçait ArcGIS Online](https://www.esri.com/news/arcnews/winter0708articles/arcgis-product-suite.html) et que MapInfo, alors principal logiciel SIG dans les institutions françaises, [était racheté par Pitney Bowes](https://www.investorrelations.pitneybowes.com/news-releases/news-release-details/pitney-bowes-completes-acquisition-mapinfo) et que l'open source géospatial utilisait entre autres [Puzzle GIS](/articles/2009/art_2009-05-24/), [OpenJump](/articles/2009/art_2009-05-31/), [uDig](/articles/2009/art_2009-06-07/) ?

Eh bien, voici quelques captures :

[![QGIS 0.9 - Propriétés projet](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_0-9-1x_project_properties.png "QGIS 0.9 - Propriétés projet"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_0-9-1x_project_properties.png){: data-mediabox="lightbox-gallery" data-title="QGIS 0.9 - Propriétés projet"}

> Les propriétés d'un projet

[![QGIS 0.9 - Options](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_0-9-1x_options.png "QGIS 0.9 - Options"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_0-9-1x_options.pn){: data-mediabox="lightbox-gallery" data-title="QGIS 0.9 - Options"}

> Le panneau des options était épuré

[![QGIS 0.9 - Plugins](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_0-9-1x_plugins.png "QGIS 0.9 - Plugins"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_0-9-1x_plugins.png){: data-mediabox="lightbox-gallery" data-title="QGIS 0.9 - Plugins"}

> La modularité était déjà de la partie avec le gestionnaire de plugins

----

## Challenge : une carte avec un logiciel de 2007

![icône accident](https://cdn.geotribu.fr/img/logos-icones/divers/accident.png "icône accident"){: .img-rdp-news-thumb }

Chaud comme j'étais, je me suis dit : et si je faisais une carte avec QGIS 0.9 en utilisant des données d'aujourd'hui ?

Pour rester dans le thème, j'ai cherché des données sur data.gouv.fr avec les déconvenues habituelles : lien mort (post-mortem geo.data.gouv.fr), données pas vraiment ouvertes (écosanté), etc. Mais en creusant les mots-clés dans la recherche, [`crémation`](https://www.data.gouv.fr/fr/datasets/?q=cr%C3%A9mation) m'a donné satisfaction !

Nous voici donc avec le jeu de données de [l'origine des défunts incinées depuis 2014 sur Lille Métropole](https://www.data.gouv.fr/fr/datasets/cremations-depuis-2014/) qui semble [avoir 2 crématoriums](https://www.lillemetropole.fr/votre-metropole/competences/cadre-de-vie/crematorium). Niquel :smoking: !

Un rapide coup d'oeil aux données et je me dis : "Trop cool ! Je vais faire une carte de flux entre les origines des défunts et les crématorium."

![gif enthousiasme](https://i.imgur.com/N6J6vbf.gif){: .img-center loading=lazy }

:hourglass_flowing_sand: 30 minutes plus tard :

[![Carte QGIS 0.9](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_0-9-1x_carte_crematoriums.png "Carte QGIS 0.9"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_0-9-1x_carte_crematoriums.png){: data-mediabox="lightbox-gallery" data-title="Carte avec QGIS 0.9 - Fail 2021"}

Oui, un bel échec ! Malgré mon enthousiasme, j'ai juste galéré avec les limites de l'époque :

- pas possible d'ajouter un champ
- pas de calculatrice de champ
- pas de symbologie avancée
- impossible d'afficher un WMS (j'ai essayé ceux de l'IGN, Géo2France et Lille Métropole)

----

## Conclusion

Bref, avant c'était pas forcément mieux. Je ne sais pas si l'adage des marmites s'applique aux SIG (Soupes d'Information Géographique :thinking: ?), mais une chose est sûre ~~qu'est-ce qu'on rigole bien en formation !~~ le projet QGIS a bien évolué depuis [son premier commit](/rdp/2020/rdp_2020-09-04/#avalanche-de-ressources-sur-qgis), nous avec et rien de mieux qu'un saut dans le temps pour s'en rendre compte !

[![QGIS 0.9 vs 3.16](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_both_versions.png "QGIS 0.9 vs 3.16"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/qgis_both_versions.png){: data-mediabox="lightbox-gallery" data-title="QGIS 0.9 vs 3.16"}

### Bonus

Un participant de la formation a tenu à montrer que MapInfo 1998 tournait également très bien sur Windows 10 :

[![MapInfo 1998 sur Windows 10](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/mapinfo1998.png "MapInfo 1998 sur Windows 10"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_0x/mapinfo1998.png){: data-mediabox="lightbox-gallery" data-title="MapInfo 1998 sur Windows 10"}

----

## Auteur

--8<-- "content/team/jmou.md"

{% include "licenses/beerware.md" %}

<!-- Intègre le glossaire centralisé -->
--8<-- "content/toc_nav_ignored/snippets/glossaire.md"

<!-- Hyperlinks reference -->
