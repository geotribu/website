---
title: "Partagez vos modèles QGIS facilement !"
subtitle: Quatres méthodes pour un modèle en QGIS en toute simplicité
authors:
  - Marc Ducobu
categories:
  - article
comments: true
date: 2025-11-19
description: "Découvrez 4 façons de partager vos modèles QGIS : de l'avion à l’intégration dans un plugin !"
icon: fontawesome/regular/paper-plane
image: "Image d'illustration de l'article qui sert ensuite dans la mise en avant : réseaux sociaux, flux RSS... 400x800 en PNG"
license: default
robots: index, follow
tags:
  - QGIS
  - modèles
---

# Quatres méthodes pour un modèle en QGIS en toute simplicité

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

Après de longues heures de travail et beaucoup trop de litres de café, vous avez enfin créé un modèle digne d’un tableau de Kandinsky. Maintenant, vous souhaitez le partager avec vos collègues, tata Jeannine afin de ne pas être le seul à pouvoir en profiter !

Dans cet article, nous vous proposons quatre méthodes pour diffuser votre modèle QGIS de manière simple et efficace.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Méthode du stagiaire

Un stagiaire, très créatif, pourrait vous proposer la méthode suivante : faire une copie d'écran du modèle, l'imprimer sur une feuille A4, un pliage magique pour la transformer en concorde et l'envoyer. Merci à lui !

Bon, on est d'accord, c'est drôle mais très efficace. Heureusement, la communauté de QGIS s'est penchée sur le problème et propose d'autres alternatives.

## Utilisation du hub de QGIS

Connaissez-vous le hub des ressources QGIS ? Le hub a été introduit dans QGIS 3.14 et permet de partager facilement des modèles, des scripts, des styles, des symboles, etc. J'avoue que je n'ai pas encore le réflexe de l'utiliser et de l'inclure dans les solutions que je mets en œuvre. Si c’est aussi votre cas, voici un petit aperçu de son fonctionnement.

IMG hub_qgis_1

Le hub de QGIS est accessible à l’adresse [https://hub.qgis.org](https://hub.qgis.org). Il s’agit d’une plateforme en ligne où les utilisateurs peuvent publier et télécharger des ressources QGIS : styles, projets, modèles, etc. Vous pouvez y trouver la ressource qui vous intéresse et l’intégrer directement dans QGIS.

IMG_HUB_2

Si, comme moi, vous préférez limiter les manipulations, vous pouvez installer l’extension [QGIS Hub Plugin](https://plugins.qgis.org/plugins/qgis_hub_plugin/) et accéder aux ressources directement dans QGIS via l'extension.

QGIS_HUB_PLUGIN

## Répertoire partagé

Si vous travaillez en équipe et que vous souhaitez partager vos modèles avec vos collègues sans les rendre publics, vous pouvez configurer QGIS pour qu’il aille aussi chercher des modèles dans un répertoire partagé.

Pour cela, rendez-vous dans "Settings" > "Options" > "Processing" > "Modèles" et ajoutez le chemin du répertoire partagé dans la liste des dossiers de modèles. Rapide et efficace !

SHARE_FOLDER.png

## Intégration dans un plugin

La dernière méthode consiste à intégrer vos modèles dans un plugin QGIS. Un plugin permet d’ajouter des outils dans la "Boîte à outils de traitement" (Processing Toolbox) de QGIS, y compris des modèles. Par exemple, l’extension [Cadastre](https://plugins.qgis.org/plugins/cadastre/) ajoute à la boîte à outils des traitements supplémentaires 🤯 !

PROCESSING_TOOL_BOX_CADASTRE.png

Créer un plugin n'est pas une mince affaire, mais depuis quelque temps, un outil facilite cette tâche : le plugin [Models2Plugin](https://plugins.qgis.org/plugins/models2plugin/). En 3 étapes : encodage des informations de base, sélection des modèles à intégrer et génération du plugin, vous pouvez créer un plugin QGIS contenant vos modèles.

MODELS2PLUGIN_1.png

## Pour conclure

Nous venons de voir quatre méthodes pour partager vos modèles QGIS. Chaque méthode a ses spécificités et peut répondre à un besoin spécifique. La communauté QGIS est très active et créative pour rendre l'utilisation de QGIS toujours plus efficace.

Connaissiez-vous ces différentes méthodes ? Qu’en pensez-vous ? Avez-vous d’autres astuces pour partager vos modèles ? N’hésitez pas à partager votre expérience dans les commentaires !

---

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
