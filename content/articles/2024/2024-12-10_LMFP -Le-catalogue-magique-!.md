---
title: "LMFP : LE catalogue magique !"
subtitle : Retour d'expérience sur le plugin Layers Menu From Project
authors:
    - Emilie BIGORNE
    - Céline PORNIN
categories:
    - article
comments: true
date: 2024-12-10
description: "Une extension extension Qgis peut être (trop) méconnue : Layers Menu From Project permet de simplifier la vie des administrateurs ET des utilisateurs, retour d'expérience à deux voix. "
icon: "fontawesome/solid/wand-magic-sparkles"
image: "https://pad.oslandia.net/uploads/3b830185-b8c1-495f-bc4e-33af8ba08c8e.png"
license: default
robots: index, follow
tags:
    - Layers Menu From Project
    - Plugin QGIS
    - QGIS


---

# Plugin Layers Menu From Project : LE catalogue magique !

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

Bonjour à toi lectrice ou lecteur !

Aujourd'hui, à deux voix, nous avons choisi de faire un retour d'expérience sur l'utilisation d'une extension Qgis peut être (trop) méconnue : Layers Menu From Project

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

# Menus magiques - par Emilie

J'ai découvert il y a déjà plusieurs années, l'outil "layers menu from project" et depuis, les utilisateurs ne jurent plus que par ça. Chez nous, on l'appelle "menu magique".

## Pourquoi c'est magique

Layers menu from project répond aux questions récurrentes des utilisateurs : où est stockée la donnée (sur le serveur, dans une base de données, dans un flux WMS ?), quelle est la dernière version, comment dois-je la représenter ? Les données sont désormais accessibles en 2 clicks, depuis des menus intégrés directement à Qgis.
Grâce à LMFP, en deux coups de baguette magique, la donnée est affichée !
![](https://pad.oslandia.net/uploads/7587eaf7-ae68-4bee-af5f-791a6340fafc.png){: align=middle }

### Comment ça fonctionne ?

Les entrées du menu correspondent aux couches stockées dans un projet qgis (qgs ou qgz), accessible depuis les postes utilisateurs. Les données peuvent être vecteurs ou rasters, des fichiers plats, issus d'une base de données ou des flux, et toute la configuration de la couche est conservée : symbologie, actions, mise en forme de la table attributaire, formulaire, notes de couche,…
Concrètement, l’administrateur prépare le.s projet.s QGIS, l’utilisateur le pointe dans le plugin LMP et le tour est joué.
![](https://pad.oslandia.net/uploads/4e78da7c-0f23-4554-9332-25d390ba124f.png)

!!! tip Astuce déploiement  
    ![](https://pad.oslandia.net/uploads/83db5967-9c29-4217-a17d-4d9aac11f655.png)
    Pour encore plus de rapidité côté administrateur et de simplicité côté utilisateur, le déploiement peut se faire via [QGIS Deployment Toolbelt (QDT)](https://qgis-deployment.github.io/qgis-deployment-toolbelt-cli/#) : installation du plugin et paramétrage automatique selon les profils utilisateurs.

### L'association avec une base de données PostgreSql

Avec une base PG, je peux afficher les couches directement depuis une requête, plus besoin de stocker des vues qui induise des dépendances parfois complexes. En revanche, attention, le mode de connexion à la base (identifiant/mot de passe) est également stocké.

!!! tip Astuce sécurité
    Pour contourner cette difficulté, j'ajoute des couches depuis une connexion dont je n'ai pas sauvegardé les paramètres d'authentification. Ainsi, l'utilisateur est invité à saisir ses propres identifiants.

### Une limite  de taille ?

Dans la théorie, non. En revanche, un projet source avec trop de couches va mettre beaucoup de temps à s'ouvrir et c'est l'administrateur qui va être embêté pour faire ses mises à jour. Mais l'outil propose une solution: il est possible de créer une entrée (un menu) à partir de plusieurs projets QGis. Ainsi, on peut avoir plusieurs petits projets plus faciles à maintenir plutôt qu'un seul gros projet.

Pour l'utilisateur, un menu trop long peut être inconfortable. Pour remédier aux listes trop longues, plus ou moins bien organisées, il est possible de grouper les couches en sous-menu (voire sous-sous-menu) en utilisant les groupes de couches. Un groupe de couches vide peut également être utilisé comme séparateur.

### En action

Les actions des couches sont également conservées. On peut ainsi par exemple permettre, au clic sur des entités, d'ouvrir une page web, de charger des dalles raster ou des photos (moyennant quelques lignes de python)

!!! quote La conclusion d'Emilie :
    En interne, on adore la magie.

# LE catalogue  - par Céline

De mon côté, c'est sur un outil mutualisé par plusieurs structures que LMFP a changé la donne !

## C'est pratique, voilà pourquoi !

### Du côté utilisateur

Une base de données pour plusieurs structures, ça veut dire plusieurs utilisateurs plus ou moins habitués à l'utilisation de QGIS.
**La formation et l'accompagnement ne font pas tout, il nous fallait une solution "User friendly"** ergonomique et facile à lire pour n'importe qui.
Du coup, la liste des couches configurées depuis la base de données dans l'explorateur : ça ne fonctionne pas ! Un menu dédié, qu'on a appelé "catalogue" : c'est explicite et c'est facile pour tout le monde.

![](https://)![](https://pad.oslandia.net/uploads/1d453727-fb6a-4b16-8668-2c2ac37a74f7.JPG){: align=middle }

### Du coté administrateur

La liste des couches configurée depuis la base de données dans l'explorateur : ça ne fonctionne pas non plus ! Il faudrait nommer les schémas, tables et vues et que tout soit rangé en pensant à l'utilisateur ... ou utiliser un schéma dédié avec toutes les vues renommées ...
Avec LMFP : pas de sujet ! **Peu importe le modèle de données, c'est le nommage et la configuration dans le projet QGIS utilisé qui comptent**.

!!! tip Autre avantage
     Etant donné qu'il est possible aussi de mettre des flux, on s'épargne des actions de mise à jour et on remercie les producteurs de gérer leurs mises à jour tous seuls !

Comme dit précédemment : la principale contrainte est alors liée au maintient du projet QGis en entrée du plugin et à l'accès des utilisateurs à ce projet. Chez nous, il est enregistré en base de donnée. Une authentification avec un identifiant / mot de passe est enregistrée à la première connexion de l'utilisateur, qui lui donne accès au projet via le menu et aux différentes données en base (en lecture ou en écriture).

!!!tip **Encore plus de paillettes**
    En plus des groupes, sous-groupes et agencement de différents projets, il est possible de créer des sections avec des titres et des séparateurs. Rendez-vous sur la documentation du plugin pour rendre tout ça encore plus beau ! [C'est par ici](https://aeag.github.io/MenuFromProject-Qgis-Plugin/usage/fr_use.html#)

Pour finir, la **cerise sur le gateau : la mise à jour d'un outil sans réinstallation ou téléchargement.**
Notre outil est en constante évolution : champs, listes de valeurs, symbologie ... on change des trucs régulièrement (on corrige aussi des fautes de frappe dans les formulaires par exemple...). Il suffit simplement à l'utilisateur de recharger la couche depuis le menu pour que tout soit à jour : pas besoin de redémmarer QGIS, réinstaller une extension, aller chercher un style enregistré quelque part ou encore télécharger et écraser un projet QGIS !

## L'évolution du plugin

Il n'y a pas que nos outils qui évoluent, le plugin aussi !
L'année dernière, on a commencé à intégrer des relations dans notre projet QGIS. Le problème : charger une couche depuis le menu ne chargeait ni l'autre (ou les autres ) couche(s) ni la relation.
Un ticket Git, quelques échanges avec le développeur : et voilà, problème réglé.

Aujourd'hui, on a remarqué d'autres limites à cette extension (nul n'est parfait ...) alors on va continuer d'apporter notre contribution et nos retours pour la faire évoluer. Et quand on est plusieurs concernés, autant mutualiser, et c'est ce qu'on va faire avec d'autres structures qui utilisent ce plugin !

!!! quote La conclusion de Céline :
     User et Administrateur friendly !

# En résumé

## Nos :heavy_plus_sign:

* Facile d'utilisation pour les utilisateurs et adaptable par groupes d'utilisateurs
* Facile à configurer
* Permet de rendre accessible des données issues de différentes sources (base de données, fichiers, flux, requêtes...)
* Permet de gérer facilement les styles (symbologie, formulaires, actions)
* Mises à jour des données et styles facilitées
* Une communauté de fans grandissante qui va permettre de faire évoluer l'extension pour encore plus de magie !

## Nos :heavy_minus_sign:

* Attention aux menus trop longs : le projet initial est lourd, le chargement trop impactant sur les perfs d'ouverture du logiciel
* Trop de menus différents : temps d'ouverture de qgis plus long
* Des optimisations à faire côté performances dans certains cas techniques

!!! success Le mot de la fin
    Un grand merci à tous les développeurs et financeurs des évolutions du plugin LMFP !

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}