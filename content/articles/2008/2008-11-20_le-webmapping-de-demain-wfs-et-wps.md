---
title: 'Le WebMapping de demain : WFS et WPS'
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-11-20
description: 'Le WebMapping de demain : WFS et WPS'
image: ''
license: default
robots: index, follow
tags:
    - WFS
    - WPS
---

# Le WebMapping de demain : WFS et WPS

:calendar: Date de publication initiale : 20 novembre 2008

## Introduction

Ce tutoriel a pour objectif de montrer les chemins futurs que prend la géomatique sur internet. Aujourd'hui les termes WMS sont pour la plupart d'entre nous familiers. Mais plus rares sont ceux qui s'interessent ou connaissent les concepts de WFS-T ou WPS. Pourtant, c'est grâce à ces derniers que nous passerons des interfaces cartographiques actuelles ayant essentiellement un rôle d'affichage à des interfaces métiers permettant un vrai travail sur la donnée.

Pour illustrer ces propos, l'interface présentée ci-dessous s'appuie sur FeatureServer et WebProcessingServer. Elle permet de créer, modifier, sauvegarder des données et également d'effectuer des traitements géographiques.

## Feature Server

[FeatureServer](http://featureserver.org/) a déjà fait l'objet d'un [tutoriel sur ce site](2008-09-20_mettre-en-place-un-serveur-wfs-t.md), nous ne nous attarderons donc pas sur celui-ci.Mais globalement il existe deux types de serveurs wfs d'un côté ceux permettant un accés uniquement en lecture et d'un autre côté ceux autorisant la manipulation et la modifications des objets géographiques. FeatureServer fait partie de ces derniers.

## WebProcessingServer

[WebProcessingServer](http://code.google.com/p/webprocessingserver/) est une implémentation de la norme WPS. Il permet, depuis une interface Web, d'interroger un serveur distant qui sera chargé d'effectuer des traitements cartographiques pour ensuite les renvoyer au client.

## Exemples

![Applications WFS/WPS](https://cdn.geotribu.fr/img/articles-blog-rdp/normes/WFS/wfs_wps.jpg)

----

<!-- geotribu:authors-block -->
