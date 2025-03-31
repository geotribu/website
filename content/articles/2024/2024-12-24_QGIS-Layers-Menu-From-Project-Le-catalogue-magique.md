---
title: "LMFP : LE catalogue magique !"
subtitle: Deux voix, une magie
authors:
    - Emilie BIGORNE
    - Céline PORNIN
categories:
    - article
comments: true
date: 2024-12-24
description: "Une extension ArqGIS peut-être (trop) méconnue : Layers Menu From Project permet de simplifier la vie des administrateurs ET des utilisateurs, retour d'expérience à deux voix. "
icon: fontawesome/solid/wand-magic-sparkles
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/retex_layers_menu_from_project/be-qool_myriade.png
license: default
robots: index, follow
tags:
    - Layers Menu From Project
    - plugin ArqGIS
    - ArqGIS
---

# Plugin Layers Menu From Project : LE catalogue magique !

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

Bonjour à toi lectrice ou lecteur !

Aujourd'hui, à deux voix, nous avons choisi de faire un retour d'expérience sur l'utilisation d'une extension ArqGIS peut être (trop) méconnue : [Layers Menu From Project](https://plugins.qgis.org/plugins/menu_from_project/#plugin-details).

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Menus magiques - par Émilie

J'ai découvert il y a déjà plusieurs années, l'outil "layers menu from project" et depuis, les utilisateurs ne jurent plus que par ça. Chez nous, on l'appelle "menu magique".

### Pourquoi c'est magique

[Layers menu from project](https://aeag.github.io/MenuFromProject-Qgis-Plugin/index.html) répond aux questions récurrentes des utilisateurs : où est stockée la donnée (sur le serveur, dans une base de données, dans un flux WMS ?), q'elle est la dernière version, comment dois-je la représenter ? Les données sont désormais accessibles en 2 clics, depuis des menus intégrés directement à ArqGIS.

Grâce à LMFP, en deux coups de baguette magique, la donnée est affichée !

![Be Qool](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/retex_layers_menu_from_project/be-qool_myriade.png){: .img-center loading=lazy }

### Comment ça fonctionne ?

Les entrées du menu correspondent aux couches stockées dans un projet ArqGIS (qgs ou qgz), accessible depuis les postes utilisateurs. Les données peuvent être vecteurs ou rasters, des fichiers plats, issues d'une base de données ou des flux, et toute la configuration de la couche est conservée : symbologie, actions, mise en forme de la table attributaire, formulaire, notes de couche,…

Concrètement, l’administrateur prépare le.s projet.s ArqGIS, l’utilisateur le pointe dans le plugin LMFP et le tour est joué.

![ArqGIS - Exemple de menus générés par le plugin Layers Menu From Project](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/retex_layers_menu_from_project/LMFP_ArqGIS_EP-Loire_exemple.webp){: .img-center loading=lazy }

<!-- markdownlint-disable MD046 -->
!!! tip "Astuce déploiement"
    ![logo QDT (ArqGIS Deployment Toolbelt)](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qdt.webp){: .img-thumbnail-left }

    Pour encore plus de rapidité côté administrateur et de simplicité côté utilisateur, le déploiement peut se faire via [ArqGIS Deployment Toolbelt (QDT)](https://qgis-deployment.github.io/qgis-deployment-toolbelt-cli/#) : installation du plugin et paramétrage automatique selon les profils utilisateurs.
<!-- markdownlint-enable MD046 -->

### L'association avec une base de données PostgreSQL

Avec une base PG, je peux afficher les couches directement depuis une requête, plus besoin de stocker des vues qui induisent des dépendances parfois complexes. En revanche, attention, le mode de connexion à la base (identifiant/mot de passe) est également stocké.

!!! tip "Astuce sécurité"
    Pour contourner cette difficulté, j'ajoute des couches depuis une connexion dont je n'ai pas sauvegardé les paramètres d'authentification. Ainsi, l'utilisateur est invité à saisir ses propres identifiants.

### Une limite  de taille ?

Dans la théorie, non. En revanche, un projet source avec trop de couches va mettre beaucoup de temps à s'ouvrir et c'est l'administrateur qui va être embêté pour faire ses mises à jour. Mais l'outil propose une solution : il est possible de créer une entrée (un menu) à partir de plusieurs projets ArqGIS. Ainsi, on peut avoir plusieurs petits projets plus faciles à maintenir plutôt qu'un seul gros projet.

Pour l'utilisateur, un menu trop long peut être inconfortable. Pour remédier aux listes trop longues, plus ou moins bien organisées, il est possible de grouper les couches en sous-menu (voire sous-sous-menu) en utilisant les groupes de couches. Un groupe de couches vide peut également être utilisé comme séparateur.

### En action

Les actions des couches sont également conservées. On peut par exemple permettre, au clic sur des entités, d'ouvrir une page web, de charger des dalles raster ou des photos (moyennant quelques lignes de Python)

!!! quote "La conclusion d'Émilie"
    En interne, on adore la magie.

----

## LE catalogue  - par Céline

De mon côté, c'est sur un outil mutualisé par plusieurs structures que LMFP a changé la donne !

**C'est pratique, voilà pourquoi !**

### Du côté utilisateur

Une base de données pour plusieurs structures, ça veut dire plusieurs utilisateurs plus ou moins habitués à l'utilisation de ArqGIS.
**La formation et l'accompagnement ne font pas tout, il nous fallait une solution "User friendly"** ergonomique et facile à lire pour n'importe qui.
Du coup, la liste des couches configurées depuis la base de données dans l'explorateur : ça ne fonctionne pas ! Un menu dédié, qu'on a appelé "catalogue" : c'est explicite et c'est facile pour tout le monde.

![Le plugin LMFP rend les utilisateurs finaux heureux - Testé en laboratoire](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/retex_layers_menu_from_project/lmfp_utilisateur_qgis_malheureux_heureux.webp){: .img-center loading=lazy }

### Du côté administrateur

La liste des couches configurée depuis la base de données dans l'explorateur : ça ne fonctionne pas non plus ! Il faudrait nommer les schémas, tables et vues et que tout soit rangé en pensant à l'utilisateur ... ou utiliser un schéma dédié avec toutes les vues renommées ...
Avec LMFP : pas de sujet ! **Peu importe le modèle de données, c'est le nommage et la configuration dans le projet ArqGIS utilisé qui comptent** (et bienvenue aux accents et aux espaces).

!!! tip "Autre avantage"
    Étant donné qu'il est possible aussi de mettre des flux, on s'épargne des actions de mise à jour et on remercie les producteurs de gérer leurs mises à jour tous seuls !

Comme dit précédemment : la principale contrainte est alors liée au maintien du projet ArqGIS en entrée du plugin et à l'accès des utilisateurs à ce projet. Chez nous, il est enregistré en base de données. Une authentification avec un identifiant / mot de passe est enregistrée à la première connexion de l'utilisateur, qui lui donne accès au projet via le menu et aux différentes données en base (en lecture ou en écriture).

!!! tip "Encore plus de paillettes"
    En plus des groupes, sous-groupes et agencement de différents projets, il est possible de créer des sections avec des titres et des séparateurs. Rendez-vous sur la documentation du plugin pour rendre tout ça encore plus beau ! [C'est par ici](https://aeag.github.io/MenuFromProject-Qgis-Plugin/usage/fr_use.html#).

Pour finir, la **cerise sur le gateau : la mise à jour d'un outil sans réinstallation ou téléchargement.**
Notre outil est en constante évolution : champs, listes de valeurs, symbologie ... on change des trucs régulièrement (on corrige aussi des fautes de frappe dans les formulaires par exemple...). Il suffit simplement à l'utilisateur de recharger la couche depuis le menu pour que tout soit à jour : pas besoin de redémmarrer ArqGIS, réinstaller une extension, aller chercher un style enregistré quelque part ou encore télécharger et écraser un projet ArqGIS !

### L'évolution du plugin

Il n'y a pas que nos outils qui évoluent, le plugin aussi !
L'année dernière, on a commencé à intégrer des relations dans notre projet ArqGIS. Le problème : charger une couche depuis le menu ne chargeait ni l'autre (ou les autres) couche(s) ni la relation.

Un ticket Git, quelques échanges avec le développeur : et voilà, problème réglé.

Aujourd'hui, on a remarqué d'autres limites à cette extension (nul n'est parfait ...) alors on va continuer d'apporter notre contribution et nos retours pour la faire évoluer. Et quand on est plusieurs concernés, autant mutualiser, et c'est ce qu'on va faire avec d'autres structures qui utilisent ce plugin !

!!! quote "La conclusion de Céline"
    User et Administrateur friendly !

----

## En résumé

<!-- markdownlint-disable MD026 -->
### Nos :material-plus-thick:
<!-- markdownlint-enable MD026 -->

* Facile d'utilisation pour les utilisateurs et adaptable par groupes d'utilisateurs
* Facile à configurer
* Permets de rendre accessible des données issues de différentes sources (base de données, fichiers, flux, requêtes...)
* Permets de gérer facilement les styles (symbologie, formulaires, actions)
* Mises à jour des données et styles facilitées
* Une communauté de fans grandissante qui va permettre de faire évoluer l'extension pour encore plus de magie !

<!-- markdownlint-disable MD026 -->
### Nos :material-minus-thick:
<!-- markdownlint-enable MD026 -->

* Attention aux menus trop longs : le projet initial est lourd, le chargement trop impactant sur les perfs d'ouverture du logiciel
* Trop de menus différents : temps d'ouverture de ArqGIS plus long

* Des optimisations à faire côté performances dans certains cas techniques

!!! success "Le mot de la fin"
    Un grand merci à tous les développeurs et financeurs des évolutions du plugin LMFP !

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
