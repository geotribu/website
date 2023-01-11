---
title: "Voeux 2023 et bilan 2022"
subtitle: "Calmement, se remémorant chaque news"
authors:
    - Geotribu
categories:
    - article
date: "2023-01-16 10:20"
description: ""
image: ""
license: default
tags:
    - Geotribu
---

# Installer QGIS sur Ubuntu, le pense-bête simple et efficace

:calendar: Date de publication initiale : 16 janvier 2023

## Introduction

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Meilleurs voeux pour 2023 de la part de Geotribu !

----

## Rétrospective 2022

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/mbDAz9aAVW8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Contenus

- 16 articles publiés de 13 auteurs différents, mais dont 1 seule autrice
- 23 revues de presse publiées

## Audience

- :incoming_envelope: on a passé la barre des XXX inscrits à [la newsletter](/newsletter/signup/)

## Fonctionnalités

- les avatars GitHub des principaux contributeur/ices d'une page sont automatiquement ajoutés en bas de page
- :frame_photo: ajout du [plugin mkdocs-glightbox](https://blueswen.github.io/mkdocs-glightbox/) pour appliquer un mode galerie à toutes les images par défaut. Vous savez, quand on clique sur une image et que ça l'agrandit en floutant le site à l'arrière-plan et en permettant de naviguer d'une image à l'autre ? Avant c'était ~~galère~~ exigeant de faire ça dans un contenu Geotribu, maintenant y'a rien à faire. Plus d'information dans [le guide de contribution](/contribuer/guides/image/#lightbox-mode-galerie).
- :heartpulse: il est désormais possible de montrer son amour d'un contenu sans avoir à écrire de commentaire. Idéal pour les timides qui souhaiteraient quand même remercier les auteur/ices :wink:.
- :material-puzzle: notre [plugin QGIS](https://plugins.qgis.org/plugins/qtribu/) est désormais publié dans le dépôt officiel des extensions pour que son installation soit plus facile
- :robot: un robot pré-mâche le travail d'intégration des news proposées via le formulaire GitHub ([voir cet exemple](https://github.com/geotribu/website/issues/703#issuecomment-1256246426))
- :label: ajout d'icônes aux mots-clés (travail en cours) et légère amélioration du design
- :factory_worker: des évolutions sous le capot du site notamment liées au thème [Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/insiders/) dont on contribue à financer la version payante (*Insiders*) via notre [Tipeee](https://fr.tipeee.com/geotribu).

## Architecture

- :mirror: pour améliorer notre résilience et réduire notre adhérence à GitHub, on a mis en place [un site miroir](https://fr.wikipedia.org/wiki/Site_miroir#Nom_de_domaine) sur <https://www2.geotribu.fr> (synchronisé quotidiennement).
- :fontawesome-solid-server: migration de serveur (merci GeoRezo !) : CDN, commentaires et mécanisme de sauvegarde sont déjà sur le nouveau serveur. Au passage, on en profite pour rendre le déploiement de notre infrastructure reproductible avec Ansible. Pour les curieux, ça se passe sur [ce dépôt GitHub](https://github.com/geotribu/infra).

## Archives

Fin 2021, nous attaquions l'homogénéisation et l'assainissement des contenus anciens. Ce travail de reprise chronophage s'est échelonné tout au long de l'année 2022 avec de nombreux ajustements sur :

- le markdown : niveau des titres, mise en valeur du code, suppression des anciennes ancres, retraits en début de ligne
- l'intégration des icônes et images manquantes.

----

## Perspectives 2023

### Objectifs

- [ ] tenir le rythme d'une revue de presse toutes les 2 semaines (hors déserts vacanciers français)
- [ ] intégrer les derniers contenus historiques manquants
- [ ] harmoniser des tags et des textes de remplacement sur les icônes

### Evolutions

On a d'ores et déjà quelques annonces à faire :

- le site changera d'adresse d'ici le printemps : fin du sous-domaine `static`, le site retourne à la racine `https://geotribu.fr/`
- la section dédiée à la contribution a désormais son propre site web : <https://contribuer.geotribu.fr/>
- optimiser automatiquement les images

----

## Auteur {: data-search-exclude }

--8<-- "content/toc_nav_ignored/snippets/authors/geotribu.md"
