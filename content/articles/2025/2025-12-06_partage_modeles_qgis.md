---
title: "Partagez vos modèles QGIS facilement !"
subtitle: Cinq méthodes pour partager un modèle dans QGIS en toute simplicité
authors:
  - Marc Ducobu
categories:
  - article
comments: true
date: 2025-12-06
description: "Découvrez 4 façons de partager vos modèles QGIS : de l'avion à l’intégration dans un plugin !"
icon: fontawesome/regular/paper-plane
image:
license: default
robots: index, follow
tags:
  - QGIS
  - modèles
---

# Cinq méthodes pour partager un modèle dans QGIS en toute simplicité

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

Après de longues heures de travail et beaucoup trop de litres de café, vous avez enfin créé un modèle digne d’[un tableau de Qandinsky](https://fr.wikipedia.org/wiki/Vassily_Kandinsky#/media/Fichier:Vassily_Kandinsky,_1923_-_Circles_in_a_Circle.jpg). Maintenant, vous souhaitez le partager avec vos collègues, tata Jeannine ou d'autres, afin de ne pas être le seul à pouvoir en profiter !

Dans cet article, je vous propose cinq méthodes pour diffuser votre modèle QGIS de manière simple et efficace.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Méthode de l'avion en papier

Un collègue très créatif, pourrait vous proposer la méthode suivante : faire une copie d'écran du modèle, l'imprimer sur une feuille A4, un pliage magique pour la transformer en concorde et l'envoyer. Merci à lui !

Cette méthode, qui peut paraître un peu loufoque, n'est pas si éloignée du temps où l'on partageait les connaissances avec des codes imprimés dans les manuels. Cela se fait encore dans certains magazines spécialisés.

Bon, on est d'accord, ce n'est pas très efficace. Heureusement, la communauté de QGIS s'est penchée sur le problème et propose d'autres solutions.

## Répertoire partagé

Si vous travaillez en équipe et que vous souhaitez partager vos modèles avec vos collègues sans les rendre publics, vous pouvez configurer QGIS pour qu’il aille aussi chercher des modèles dans un répertoire partagé.

Pour cela, rendez-vous dans "Préférences" > "Options" > "Traitement" > "Modèles" et ajoutez le chemin du répertoire partagé dans la liste des dossiers de modèles. Rapide et efficace ( merci à GeoJulien pour l’astuce ! ) !

![Capture d'écran de la configuration du répertoire partagé.](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/partage_modeles_qgis/SHARE_FOLDER.png){: .img-center loading=lazy }

## Utilisation du hub de QGIS

Connaissez-vous le hub des ressources QGIS ? Le hub a été introduit dans QGIS 3.14 et permet de partager facilement des modèles, des scripts, des styles, des symboles, etc. J'avoue que je n'ai pas encore le réflexe de l'utiliser et de l'inclure dans les solutions que je mets en œuvre. Si c’est aussi votre cas, voici un petit aperçu de son fonctionnement.

![Capture d'écran de la page internet du Hub de QGIS.](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/partage_modeles_qgis/hub_qgis_1.png){: .img-center loading=lazy }

Le hub de QGIS est accessible à l’adresse [https://hub.qgis.org](https://hub.qgis.org). Il s’agit d’une plateforme en ligne où les utilisateurs peuvent publier et télécharger des ressources QGIS : styles, projets, modèles, etc. Vous pouvez y trouver la ressource qui vous intéresse et l’intégrer directement dans QGIS.

![Présentation des différentes ressources du Hub.](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/partage_modeles_qgis/qgis_hub_2.png){: .img-center loading=lazy }

Si, comme moi, vous préférez limiter les manipulations, vous pouvez installer l’extension [QGIS Hub Plugin](https://plugins.qgis.org/plugins/qgis_hub_plugin/) et accéder aux ressources directement dans QGIS via l'extension.

![Capture d'écran de l'extension QGIS Hub.](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/partage_modeles_qgis/QGIS_HUB_PLUGIN.png){: .img-center loading=lazy }

## Utilisation du QGIS Resource Sharing

Le [QGIS Resource Sharing](https://plugins.qgis.org/plugins/qgis_resource_sharing/) est un plugin qui permet de charger des ressources depuis des dépôts (repositories) en ligne. Ces dépôts peuvent contenir des styles, des symboles, des scripts et des modèles de de traitement, des modèles de traitement, des scripts R, etc. Une fois installé, le partage de ressources se fait très facilement.

![Capture d'écran du plugin QGIS Resource Sharing.](https://qgis-contribution.github.io/QGIS-ResourceSharing/_images/repositories.png){: .img-center loading=lazy }

Cette méthode a comme avantage de pouvoir paramétrer des sources multiples. De plus, la gestion des mises à jour est automatisée : les collections sont téléchargées et mises à jour via Git, ce qui facilite grandement la synchronisation des ressources partagées.

Pour partager vos ressources, vous pouvez [créer votre propre dépôt Git](https://qgis-contribution.github.io/QGIS-ResourceSharing/authoring/creating-repository.html) ou contribuer à des dépôts existants.

( merci à GeoJulien et à lbartoletti pour la découverte de l'outil ! )-

## Intégration dans un plugin

La dernière méthode consiste à intégrer vos modèles dans un plugin QGIS. Un plugin permet d’ajouter des outils dans la "Boîte à outils de traitements" (Processing Toolbox) de QGIS, y compris des modèles. Par exemple, l’extension [Cadastre](https://plugins.qgis.org/plugins/cadastre/) ajoute à la boîte à outils des traitements supplémentaires :exploding_head: !

![Capture d'écran des outils de l'extenstion Cadastre dans la Processing Toolbox](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/partage_modeles_qgis/cadastre_processing.png){: .img-center loading=lazy }

Si vous avez les compétences, vous pouvez créer un plugin pour partager vos modèles. Dans ce cas, je vous recommande d'utiliser le [QGIS plugin Templater](https://oslandia.gitlab.io/qgis/template-qgis-plugin/) qui permet d'initier une structure de plugin contenant un fournisseur de traitements. Vous pouvez aussi vous aider de l'extension [QGIS Plugin Templater GUI](https://plugins.qgis.org/plugins/qgis_plugin_templater_gui/) qui permet de configurer l'outil à partir de QGIS.

Sinon, ne nous inquiétez pas, j'ai pensé à vous ! Comme je trouve que créer un plugin n'est pas une mince affaire, j'ai entrepris le développement d'un outil qui facilite cette tâche : le plugin [Models2Plugin](https://plugins.qgis.org/plugins/models2plugin/).

En 3 étapes : encodage des informations de base, sélection des modèles à intégrer et génération du plugin, vous pouvez créer un plugin QGIS contenant vos modèles.

![Image présentant le plugin Models2Plugin](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/partage_modeles_qgis/img_modes2plugin.png){: .img-center loading=lazy }

## Pour conclure

Nous venons de voir cinq méthodes pour partager vos modèles QGIS. Chaque méthode a ses spécificités et peut répondre à un besoin particulier. La communauté QGIS est très active et créative pour rendre l'utilisation de QGIS toujours plus efficace.

Connaissiez-vous ces différentes méthodes ? Qu’en pensez-vous ? Avez-vous d’autres astuces pour partager vos modèles ? N’hésitez pas à partager votre expérience dans les commentaires !

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
