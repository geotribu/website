---
title: Journées QGIS FR 2022 - Prérequis ateliers
authors:
    - Julien Moura
categories:
    - article
    - événement
comments: true
date: 2022-01-12
description: 'Les 18 et 19 janvier prochains se tiendront les journées QGIS en distanciel : liens utiles et liste d''inventaire pour mes ateliers (rattrapage).'
image: https://cdn.geotribu.fr/img/articles-blog-rdp/evenement/2022_01_rencontres_QGIS.jpg
license: default
tags:
    - OSGeo-fr
    - QGIS
---

# Journées QGIS FR 2022

:calendar: Date de publication initiale : 12 janvier 2022

## Introduction

![logo OSGeo](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/osgeo.png "logo OSGeo"){: .img-thumbnail-left }

Comme chaque année où il n'y a pas de pandémie mondiale, l'OSGeo France (dont [on vous présentait le 3615 à l'automne dernier](../2021/2021-10-15_irc_osgeo.md)) organise donc les [Rencontres des Utilisateurs Francophones de QGIS](https://conf.qgis.osgeo.fr/).

Et comme chaque année où il y a une vague épidémique (et non une vague épidémie), l'événement se fera finalement en distanciel, contrairement à [ce qui avait d'abord été annoncé début novembre](../../rdp/2021/rdp_2021-11-05.md#rencontres-des-utilisateurs-francophones-de-qgis-edition-2022). A nous les caméras figées, les "Vous m'entendez ?" solitaires et autres coupures ! Je plains les animateurs de la journée... Hahaha on va bien se marrer dans le *métaQGISvers* !

![Yes! Oh wait...](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/yes-wait-wtf.gif "Je sens qu'on va bien s'amuser"){: .img-center loading=lazy }
*oh wait...*
{: align=middle }

Bref, ça va être sympa, intéressant et instructif. Et cette année, j'anime ou co-anime 2 ateliers et je me suis rendu compte que contrairement à des gens plus avisés, je n'avais pas indiqué les pré-requis dans le formulaire de soumission...

L'occasion de mettre les liens utiles pour assister à l'événement et de me rattraper !

----

## Participer, assister à l'événement

![icône pop-corn cinema](https://cdn.geotribu.fr/img/logos-icones/divers/popcorn_cinema_3d.webp "icône pop-corn cinema"){: .img-thumbnail-left }

La journée du 18 est dédiée aux ateliers auxquels il faut être inscrit/e (et débité/e) et qui ne seront pas enregistrés. Il n'y a donc rien à voir pour celles et ceux qui n'ont pas leur Pass Workshopaire, circulez !

En revanche, pour la journée du 19, il va y avoir du stream et du tchat pour nous ; de la sueur et des larmes pour l'hébergeur !  
Cette année, c'est la solution de la [société k-prod](https://k-prod.fr/) qui a été retenue d'après [les derniers échanges](https://gitlab.com/osgeo-fr/journees_qgis/-/issues/98), qui intègre son propre outil de tchat et ne requiert aucune création de compte. Les vidéos seront par la suite hébergées sur Youtube et/ou PeerTube pour se les remater pépouze dans son fauteuil :

!!! info "Teasing"
    Le lien du stream n'est pas encore défini donc l'article sera mis à jour dès qu'on en aura connaissance.

<!-- [La chaîne Youtube :fontawesome-brands-youtube:](https://www.youtube.com/channel/UCoD81MU2SrJ4tBvdx4kqIbQ/){: .md-button } -->
[Assister au live (Owncast) :fontawesome-solid-video:](https://qgis.k-prod.fr/){: .md-button }
{: align=middle }

!!! tip "Le bon plan de 14h25"
    Ne manquez pas la présentation de Florian sur la carte topo à partir des données IGN ou OSM (voir aussi [cet article](../2021/2021-05-28_carte_topo_qgis.md)).

### Objectif parité

![icône globes divers](https://cdn.geotribu.fr/img/internal/icons-rdp-news/social.png "icône globes divers"){: .img-thumbnail-left }

Lors de la phase d'organisation de l'événement (pour rappel, ouverte à toutes les bonnes volontés) et en particulier de la constitution du programme, la question de la sous-représentation d'intervenan**tes** (ou la sur-représentation d'intervenan**ts** ?) est [apparue](https://gitlab.com/osgeo-fr/journees_qgis/-/issues/78#note_751448228).

Elle se pose régulièrement, voire devient incontournable dans ce genre d'événement. Ici aussi sur Geotribu, la question s'impose d'elle-même où nous ne parvenons pas à compter de femme dans nos rangs réguliers (en ponctuel sur les GeoRDP, Françoise B. et Delphine M. nous sauvent la mise...) depuis le départ de Julie Pierson, très investie par ailleurs dans la dynamique de l'OSGeo France.

Pour avancer sur [le sujet](https://gitlab.com/osgeo-fr/journees_qgis/-/issues/96), Marie Jagaille, partie prenante du collectif [Women in Copernicus](https://womenincopernicus.eu/) a proposé que la problématique gagne en visibilité et qu'on se donne les moyens de comprendre en posant la question à l'occasion de l'événement via ce formulaire qu'on vous invite à remplir soigneusement :

[Répondre au formulaire sur la quête paritaire :fontawesome-solid-people-carry-box:](https://framaforms.org/rencontres-des-utilisateurs-francophones-de-qgis-et-parite-1642158634){: .md-button }
{: align=middle }

----

## Liste de courses pour les ateliers où j'interviens

### Déployer et maintenir des profils utilisateurs

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-thumbnail-left }

Dans la même veine que [le packaging basé sur l'OSGeo4W présenté l'été dernier par Régis Haubourg](../2021/2021-07-06_qgis_personnaliser_package_osgeo4w.md), mon collègue Benoît Ducarouge (le personnage principal) et moi-même (l'assistant) proposons une méthodologie pour tirer parti des profils QGIS et dont le postulat de départ est la séparation ~~des pouvoirs~~ du logiciel, de la configuration et de la personnalisation.

Au menu : du Git, du fichier `.ini` et du script Python.

#### Pré-requis logiciels

- QGIS (LTR de préférence, la 3.16 à date donc)
- un éditeur de script : ~~bloc-notes~~, nano, gedit, Notepad++, Sublime Text, Visual Studio Code, vim, emacs, etc.
- un compte GitLab ou GitHub
- Git (GitHub Desktop, ça passe)

#### Notions et compétences

- vous savez qu'une variable d'environnement n'est pas un indice du GIEC
- vous avez déjà éprouvé la douleur du message `IndentationError: unindent does not match any outer indentation level`

### Les easter eggs de QGIS : chasser et être chassé

![œuf globe](https://cdn.geotribu.fr/img/logos-icones/divers/oeuf_globe.webp "œuf globe"){: .img-thumbnail-left }

L'idée de cet atelier est d'abord de passer un bon moment tout en apprenant à chasser les fonctions cachées ([*easter eggs*](https://fr.wikipedia.org/wiki/Easter_egg)) dans QGIS et à en ajouter de nouvelles pour voir si les utilisateurs les débusquent.

<!-- markdownlint-disable MD024 -->
#### Pré-requis logiciels
<!-- markdownlint-enable MD024 -->

- QGIS (LTR de préférence, la 3.16 à date donc)
- un éditeur de code qui soit un poil spécialisé Python : ~~bloc-notes~~, Notepad++, Sublime Text, Visual Studio Code, vim, emacs, etc.

<!-- markdownlint-disable MD024 -->
#### Notions et compétences
<!-- markdownlint-enable MD024 -->

- vous savez que le sens de l'humour est le meilleur atout pour ne pas balancer son ordi par la fenêtre quand QGIS affiche "Crash dumped - minidump written..."
- vous êtes abonné/e à Geotribu d'une façon ou d'une autre
- vous avez déjà éprouvé la douleur du message `IndentationError: unindent does not match any outer indentation level`
- vous avez déjà écrit un script PyQGIS ou contribué à un plugin QGIS
- vous regrettez que le droit au troll ne soit ouvert que le vendredi

----

## Et si vous pigiez tout ?

![icône globe lobby](https://cdn.geotribu.fr/img/internal/icons-rdp-news/lobby.png "icône globe lobby"){: .img-thumbnail-left }

Pendant que je rédige ce billet de blog, je me dis que ça pourrait être sympa si plusieurs personnes prennent des notes pendant les interventions !

Si ça marche, on les publiera sous forme de compte-rendu sur Geotribu après la conférence histoire d'aider les absents à réduire le poids de leur amertume.

Les pré-requis ici aussi :

- avoir les bases de la syntaxe Markdown **OU** savoir taper sur son clavier et cliquer sur les boutons de la barre de mise en forme (*WYSIWYG*)
- comprendre que vous pouvez seulement pointer vers des images externes mais pas glisser/déposer d'images sur le pad (mais on pourra les héberger ensuite sur notre [pseudo-CDN](https://cdn.geotribu.fr/))
- avoir envie de donner un coup de pouce à l'événement tout en y assistant
- ne pas avoir envie d'écrire des choses cheloues ou illégales

J'ai préparé un bloc-notes partagé pour l'occasion :

[Devenir géo-pigiste ! :fontawesome-solid-leaf:](https://geotripad.herokuapp.com/TrS30q62T5GSSkjtW1mBtw?both){: .md-button }
{: align=middle }

----

<!-- geotribu:authors-block -->
