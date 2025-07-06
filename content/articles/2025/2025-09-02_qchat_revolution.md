---
title: La Révolution de QChat
subtitle: Choisis ta room camarade
authors:
    - Guilhem ALLAMAN
    - Geotribu
categories:
    - article
comments: true
date: 2025-09-02
description: Explications techniques de la refonte du système QChat, le plugin pour tchatter avec ses pair/es dans QGIS.
icon: material/chat
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/qchat_revolution/velo_deguise_en_moto.png
license: beerware
tags:
    - QChat
    - QField
    - QGIS
    - Redis
---

# La Revolución del QChat

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

:raised_hands: QChat est mort, vive QChat !

Après [une première version assez bancale](../2024/2024-10-15_qchat.md), la Geotribu est heureuse d'annoncer des changements assez profonds et impactants pour QChat, le système de tchat intégré à QGIS.

QChat nouvelle version, c'est un peu comme [Com Truise](https://www.youtube.com/watch?v=L4ENAdECytk) qui monte sur une moto : ça fait de l'air dans les veuch !

![Un vélo maquillé en moto](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/qchat_revolution/velo_deguise_en_moto.png){: .img-center loading=lazy }

## Pourquoi ?

- précédemment: un seul worker uvicorn -> limité niveau nombres d'utilisateur/rices instantanées
- conférence avec QChat en direct lors des Rencontres QGISFR2025 : et là, c'est le drame...

-> malgré la couverture des tests assez haute, besoin d'un backend plus robuste pour _scaler_ si y'a du monde sur la corde à linge

## Nouveautés

- partager des modèles graphiques
- partager et exécuter du code `pyqgis`

## Refonte du backend gischat

- intégration et utilisation de [redis](https://redis.io/)
- mécanisme pubsub
- stockage des users connectés dans des listes légères

### Monter un serveur gischat

- procédure installation et description du docker-compose + nginx
- référencer l'instance dans l'annuaire

## Création du plugin QGIS officiel: QChat

- pourquoi ? plus simple à retrouver, plus direct
- utilisation du templater de plugins QGIS
- publication sur le dépôt des plugins QGIS avec `qgis-plugin-ci` et un id OSGeo

## Extra: plugin QField

- développement en parallèle d'un client sous forme de plugin QField
- procédure d'installation
