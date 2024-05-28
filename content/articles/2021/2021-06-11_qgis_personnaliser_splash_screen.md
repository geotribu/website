---
title: Personnaliser le splash screen de QGIS
authors:
    - Julien MOURA
categories:
    - article
    - tutoriel
comments: true
date: 2021-06-11
description: Le lancement de QGIS vous semble long ? Vous êtes sur la LTR et las de voir la même image pendant 2 ans ? Voici comment personnaliser l'image au lancement de QGIS.
image: https://cdn.geotribu.fr/img/tuto/qgis_splash_screen/qgis_qtribu_splash_screen_custom.png
license: none
tags:
    - démarrage
    - personnalisation
    - QGIS
    - splash screen
---

# Personnaliser l'image au lancement de QGIS

:calendar: Date de publication initiale : 11 juin 2021

Pré-requis :

- aucun

## Introduction

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png){: .img-thumbnail-left }

Le *splash screen* est l'image qui apparaît au lancement de QGIS. Une image que vous pouvez voir plus ou moins longtemps, la durée étant inversement proportionnelle aux caractéristiques techniques de votre ordinateur et au nombre de plugins installés.

![splash screens QGIS](https://raw.githubusercontent.com/webgeodatavore/qgis-splash-screens-birthday/master/qgis-splash-screens-no-text.gif "Défilement des splash screens de QGIS - Crédits : QGIS et Web Geo Data Vore"){: loading=lazy }
{: align=middle }
> Défilement des splash screens de QGIS - Crédits : QGIS et [Web Geo Data Vore](https://github.com/webgeodatavore/qgis-splash-screens-birthday)
{: align=middle }

Le lancement de QGIS vous semble long ? Vous êtes sur la LTR et las de voir la même image pendant presque 2 ans ?  
Depuis QGIS 3, il est possible de personnaliser cette image, alors pourquoi se priver ?

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Caractéristiques de l'image

L'image doit respecter quelques prérequis :

- nommée `splash.png`
- format PNG
- accessible localement
- dimensions recommandées : 600x300
- être *fair-play* et respecter le projet : s'assurer que les éléments graphiques de QGIS (logo, etc.) restent plus importants que les autres éléments ajoutés

Certes, ce dernier point n'est pas vraiment un pré-requis mais vu que la plupart d'entre nous ne payons pas pour ce merveilleux logiciel, on peut bien le créditer correctement !

### Utiliser les images sources du projet

Peur de la page blanche ? Ou de ta propre inspiration ?  

Le [projet QGIS](https://github.com/qgis/QGIS/tree/master/images/splash/) référence un [dossier Google Drive](https://drive.google.com/drive/folders/0Bwc-5JFVTnfIMUwyLTU2cjI4MEU?usp=sharing) dans lequel on trouve toutes les sources des splash screens (y compris les fichiers gimp `.xcf`). La police référencée est [Source Sans Pro](https://fonts.google.com/specimen/Source+Sans+Pro?preview.text_type=custom) pour le lettrage QGIS.

----

## Activer la personnalisation de l'interface

Pour cela, il suffit suivre les indications de [la documentation officielle](https://docs.qgis.org/3.16/fr/docs/user_manual/introduction/qgis_configuration.html#customization). Si vos valeurs écologiques vous interdisent d'ouvrir un nouvel onglet, voici un résumé :

1. menu `Préférences` > `Personnalisation de l'interface`
2. cocher `Autoriser la modification`

![QGIS menu personnalisation](https://cdn.geotribu.fr/img/tuto/qgis_splash_screen/qgis_customization_ui_menu.png "QGIS - Menu personnalisation de l'interface"){: .img-center loading=lazy }

Ce faisant, QGIS crée un fichier `QGISCUSTOMIZATION3.ini` dans le dossier du profil utilisateur actif.

----

## Modifier le fichier de personnalisation

Le plus simple pour accéder à ce fichier est d'utiliser le menu `Préférences` > `Profils utilisateurs` > `Ouvrir le dossier du profil actif`. Si vous n'avez pas envie de risquer votre profil par défaut, créez-en un avant dédié à cette folle expérience :wink:.

Une fois dans l'explorateur de fichiers, ouvrir le fichier `QGIS/QGISCUSTOMIZATION3.ini` dans un éditeur de texte capable d'enregistrer en UTF8.

En haut du fichier, juste en-dessous de la section `[Customization]`, ajouter une clé nommée `splashpath` qui pointe vers **le dossier contenant** votre image (**avec le slash de fin**) :

```ini hl_lines="2"
[Customization]
splashpath=/home/geouser/Images/qgis_splashscreens/
Docks=true
...
```

!!!info
    Sous Windows, penser à adapter le chemin aux normes du système d'exploitation : `C:\\users\\geouser\\Images\\qgis_splashscreens\\`

Redémarrer QGIS. Si vous trouvez que votre magnifique image disparaît trop vite : installez une quinzaine de plugins :innocent: !

----

## Besoin de ne rien faire, envie d'essayer

![logo QGIS](https://cdn.geotribu.fr/img/geogames/globe_jeu_video_manette_200x200.png){: .img-thumbnail-left }

La flemme de suivre les étapes du tutoriel ? Fatigué/e à l'idée de devoir modifier un fichier à la mimine ?  Mais envie d'essayer ce que ça peut donner ?

Pas de souci, j'ai intégré la possibilité de le faire en un clic sur [notre plugin QTribu](https://geotribu.github.io/qtribu/installation.html) :wink: !

![QGIS splash screen custom](https://cdn.geotribu.fr/img/tuto/qgis_splash_screen/qgis_qtribu_splash_screen_custom.png "QGIS splash screen custom"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-sa.md" %}
