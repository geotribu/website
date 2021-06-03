---
title: "Personnaliser le splash screen de QGIS"
authors: ["Julien MOURA"]
categories: ["article"]
date: "2021-06-17 18:20"
description: "Description pour le SEO."
image: "Image d'illustration de l'article qui sert ensuite dans la mise en avant : réseaux sociaux, flux RSS..."
tags: "QGIS,personnalisation,splash screen,démarrage"
---

# Personnaliser l'image au lancement de QGIS

:calendar: Date de publication initiale : 17 juin 2021

**Mots-clés :** QGIS | interface graphique

Pré-requis :

- QGIS installé

## Introduction

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png){: .img-rdp-news-thumb }

Le *splash screen* est l'image qui apparaît au lancement de QGIS. Une image que vous pouvez voir plus ou moins longtemps, la durée étant inversement proportionnelle aux caractéristiques techniques de votre ordinateur et du nombre de plugins installés.

![splash screens QGIS](https://raw.githubusercontent.com/webgeodatavore/qgis-splash-screens-birthday/master/qgis-splash-screens-no-text.gif "Défilement des splash screens de QGIS - Crédits : QGIS et Web Geo Data Vore")
{: align=middle }
> Défilement des splash screens de QGIS - Crédits : QGIS et [Web Geo Data Vore](https://github.com/webgeodatavore/qgis-splash-screens-birthday)
{: align=middle }

Depuis QGIS 3, il est possible de personnaliser cette image, alors pourquoi se priver ?

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Caractéristiques de l'image

L'image doit respecter quelques prérequis :

- nommée `splash.png`
- format PNG
- accessible localement
- dimensions recommandées : 600x300
- faire apparaître le logo QGIS

Certes, ce dernier point n'est pas vraiment un pré-requis mais vu que la plupart d'entre nous ne payons pas pour ce merveilleux logiciel, on peut bien le créditer correctement !

----

## Activer la personnalisation de l'interface

Pour cela, suivre les indications de [la documentation officielle](https://docs.qgis.org/3.16/fr/docs/user_manual/introduction/qgis_configuration.html#customization) :

1. menu `Préférences` > `Personnalisation de l'interface`
2. cocher `Autoriser la modification`

![QGIS menu personnalisation](https://cdn.geotribu.fr/img/tuto/qgis_splash_screen/qgis_customization_ui_menu.png "QGIS - Menu personnalisation de l'interface")

Ce faisant, QGIS crée un fichier `QGISCUSTOMIZATION3.ini` dans le dossier du profil utilisateur actif.

----

## Modifier le fichier de personnalisation

Le plus simple pour accéder à ce fichier est d'utiliser le menu `Préférences` > `Profils utilisateurs` > `Ouvrir le dossier du profil actif`.

Une fois dans l'explorateur de fichiers, ouvrir le fichier `QGIS/QGISCUSTOMIZATION3.ini` dans un éditeur de texte capable d'enregistrer en UTF8.

En haut du fichier, juste en-dessous de la section `[Customization]`, ajouter une clé nommée `splashpath` qui pointe vers le dossier contenant votre image (**avec le slash de fin**) :

```ini
[Customization]
splashpath=/home/geouser/Images/qgis_splashscreens/
Docks=true
...
```

!!!info
    Sous Windows, penser à adapter le chemin aux normes du système d'exploitation : `C:\\users\\geouser\\Images\\qgis_splashscreens\\`

Redémarrer QGIS. Si vous trouvez que votre magnifique image disparaît trop vite : installez une quinzaine de plugins :innocent: !

----

## Auteur

--8<-- "content/team/jmou.md"
