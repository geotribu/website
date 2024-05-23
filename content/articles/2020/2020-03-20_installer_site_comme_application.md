---
title: Installer le site Geotribu comme une application
authors:
    - Julien MOURA
categories:
    - article
    - tutoriel
comments: true
date: 2020-03-31
description: Le site de Geotribu se présente comme une PWA. Voici comment l'installer comme une application (Windows 10 et Android).
icon: simple/pwa
image: https://cdn.geotribu.fr/img/internal/install_pwa/geotribu_uninstall_pwa_win10.png
license: default
tags:
    - application
    - astuce
    - Geotribu
    - PWA
    - site
---

# Installer Geotribu en tant qu'application

!!! warning "Cette fonctionnalité n'est plus disponible"
    Très peu utilisée, elle a été désactivée à l'automne 2021 sur Geotribu et retirée à partir de la version 8 du thème [Material for Mkdocs](https://github.com/squidfunk/mkdocs-material/issues/3219).

Ce site étant entièrement statique et déclaré comme une [application web progressive] (_progressive web apps_ ou PWA), il est possible de l'installer à la manière d'une application classique.

Pour en savoir plus sur les PWA, consulter [Progressive Web Apps : utilité, installation et gestion dans des environnements fixes et mobiles](https://www.nextinpact.com/news/108095-progressive-web-apps-utilite-installation-et-gestion-dans-environnements-fixes-et-mobiles.htm)

## Windows 10

!!! note
    Pour l'instant, seuls les navigateurs utilisant une base Chromium proposent cette option. Par exemple : Google Chrome, Microsoft Edge (à partir de la version 2020, aussi appelée Edgium), etc.

1. Une fois sur la page d'accueil, dérouler le menu _hamburger_ en haut à droite, sélectionner le menu `Applications` > `Installer ce site en tant qu'application` :

    ![Installer Geotribu comme PWA](https://cdn.geotribu.fr/img/internal/install_pwa/geotribu_install_pwa_edgium.png)

2. Un mini-formulaire apparaît pour savoir comment nommer l'application. Sauf soudaine inspiration originale, confirmer :

    ![Nommer l'application](https://cdn.geotribu.fr/img/internal/install_pwa/geotribu_install_pwa_edgium_naming.png)

3. L'application est désormais "installée" et à l'instar d'un autre logiciel, se retrouve avec son raccourci sur le Bureau et dans le menu démarrer :

    ![Geotribu dans le menu démarrer de Windows 10](https://cdn.geotribu.fr/img/internal/install_pwa/geotribu_install_pwa_win10_start_menu.png)

En l'ouvrant, le site web est lancé dans sa propre fenêtre, une interface navigateur minimaliste :

![Geotribu lancé comme une appli Windows 10](https://cdn.geotribu.fr/img/internal/install_pwa/geotribu_pwa_win10_launched.png)

### Désinstaller

Deux méthodes :

- depuis le gestionnaire d'applications du navigateur utilisé pour l'installer
- depuis le gestionnaire des applications de Windows 10 :

    ![Désinstaller Geotribu de Windows 10](https://cdn.geotribu.fr/img/internal/install_pwa/geotribu_uninstall_pwa_win10.png)

----

## Android

1. Une fois sur la page d'accueil, selon le navigateur, soit cliquer sur l'icône de maison avec un +, soit ouvrir le menu et sélectionner `Ajouter à l'écran d'accueil` :

    ![Ajouter Geotribu à l'écran d'accueil](https://cdn.geotribu.fr/img/internal/install_pwa/geotribu_pwa_install_android_firefox_chrome.png)

2. Le site est donc ajouté à l'écran principal du smartphone :

    ![Geotribu sur l'écran d'accueil d'un smartphone Android](https://cdn.geotribu.fr/img/internal/install_pwa/geotribu_pwa_install_android_homescreen.jpg)

En cliquant dessus, le site s'ouvre dans sa propre fenêtre et se comporte comme une application, avec notamment l'accès hors-ligne aux pages déjà consultées avec une connexion.

<!-- geotribu:authors-block -->

<!-- Hyperlinks -->

[application web progressive]: https://developer.mozilla.org/fr/docs/Web/Progressive_web_apps
