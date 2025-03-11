---
title: Faire une carte en relief des Écrins
authors:
    - Jean-Marc Viglino
categories:
    - article
    - tutoriel
comments: true
date: 2021-11-11
description: 'Réalisez facilement une carte en relief du Parc National des Écrins avec des données IGN et QGIS. #30DayMapChallenge 2021.'
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_en_relief_des_ecrins/0-head.jpg
license: default
tags:
    - 3D
    - BDAlti
    - DEM
    - QGIS
    - relief
    - Three.js
---

# Faire une carte en relief des Écrins

:calendar: Date de publication initiale : 11 novembre 2021

## Introduction

Aujourd'hui, nous allons voir comment réaliser une carte en relief du [Parc National des Écrins](https://fr.wikipedia.org/wiki/Parc_national_des_%C3%89crins).
Vous pouvez suivre le déroulement [sur la vidéo :fontawesome-brands-youtube:](https://youtu.be/wJjlKoSkmjY) (activez les sous-titres).

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/wJjlKoSkmjY?cc_load_policy=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Pour cela, nous aurons besoin :

- d'un modèle numérique de terrain (MNT)
- d'un fond de carte
- et d'un logiciel SIG ([QGIS](https://www.qgis.org/fr/site/))

Mais tout d'abord, il nous faut trouver une emprise du parc pour nous repérer. Un fichier est disponible sur [le catalogue des parcs nationaux](https://catalogue.parcnational.fr/catalogue/pne/fre/catalog.search#/metadata/b1b74e1bffa193453a75cccc39f6f304c8cc5561a03b2729092127ebf81439ff) qui publie des données relatives aux parcs nationaux dans le cadre de la directive INSPIRE.

Ouvrez [QGIS](https://www.qgis.org/fr/site/) et faites glisser le fichier sur la fenêtre pour afficher cette limite.

----

## Le MNT

### Charger les données

Il va nous falloir un modèle numérique de terrain pour plaquer la carte dessus.
Vous en trouverez disponible en OpenData [sur le site de l'IGN, rubrique BDAlti :fontawesome-solid-up-right-from-square:](https://geoservices.ign.fr/bdalti).

![La BDAlti](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_en_relief_des_ecrins/0-BDAlti.jpg "BDAlti IGN"){: .img-center loading=lazy }

Il faudra charger les deux départements de l'Isère (38) et les Hautes-Alpes (05) sur lesquels se trouve le parc.
Attention, ils sont fournis en FTP et il vous faudra un logiciel tel que [FileZilla](https://filezilla-project.org/) pour les charger. Sinon ils sont également disponibles en téléchargement sur [opendatarchives.fr](https://files.opendatarchives.fr/professionnels.ign.fr/bdalti/).

- [le MNT de l'Isère (06) :fontawesome-solid-download:](https://files.opendatarchives.fr/professionnels.ign.fr/bdalti/BDALTIV2_2-0_25M_ASC_LAMB93-IGN69_D005_2021-08-04.7z)
- [le MNT Hautes-Alpes (38) :fontawesome-solid-download:](https://files.opendatarchives.fr/professionnels.ign.fr/bdalti/BDALTIV2_2-0_25M_ASC_LAMB93-IGN69_D038_2020-11-13.7z)

### Afficher les données

Décompressez les fichiers chargés précédemment et faite glisser les fichiers `.asc` dans la fenêtre de QGIS.
Il vous faudra définir le système de coordonnées de référence (SCR) pour les données afin que QGIS sache comment placer ces fichiers sur la carte. Faites un clic-droit sur la couche pour définir le SCR.

![Menu définir le CRS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_en_relief_des_ecrins/1-SCR.jpg "QGIS - Menu définir le CRS"){: .img-center loading=lazy }

Les données sont dans le système Lambert 93 (code 2154).

![Choisir le CRS Lambert93](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_en_relief_des_ecrins/2-SCR.jpg "Choisir le CRS Lambert93"){: .img-center loading=lazy }

Comme le parc est à cheval sur deux départements, le plus simple est de recopier les fichiers `.asc` des deux archives dans un même répertoire et de les faire glisser tous ensemble sur QGIS. On peut ensuite les sélectionner et changer leur SCR en une seule fois.

### Préparer le terrain

En fait, vous n'aurez pas besoins de tous les fichiers, seuls ceux qui se superposent avec le parc sont nécessaires.

Soit les fichiers :

- BDALTIV2*25M_FXX***0925_6400**\_MNT_LAMB93_IGN69.asc
- BDALTIV2*25M_FXX***0925_6425**\_MNT_LAMB93_IGN69.asc
- BDALTIV2*25M_FXX***0925_6450**\_MNT_LAMB93_IGN69.asc
- BDALTIV2*25M_FXX***0925_6475**\_MNT_LAMB93_IGN69.asc
- BDALTIV2*25M_FXX***0950_6400**\_MNT_LAMB93_IGN69.asc
- BDALTIV2*25M_FXX***0950_6425**\_MNT_LAMB93_IGN69.asc
- BDALTIV2*25M_FXX***0950_6450**\_MNT_LAMB93_IGN69.asc
- BDALTIV2*25M_FXX***0950_6475**\_MNT_LAMB93_IGN69.asc
- BDALTIV2*25M_FXX***0975_6400**\_MNT_LAMB93_IGN69.asc
- BDALTIV2*25M_FXX***0975_6425**\_MNT_LAMB93_IGN69.asc
- BDALTIV2*25M_FXX***0975_6450**\_MNT_LAMB93_IGN69.asc
- BDALTIV2*25M_FXX***0975_6475**\_MNT_LAMB93_IGN69.asc

Il faudra encore une petite opération si vous voulez éviter les discontinuités en bord de tuile : il va falloir les fusionner.
Dans le menu, choisissez `Raster > Divers > Construire un raster virtuel...`.

![Construire un VRT](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_en_relief_des_ecrins/3-merge.jpg "QGIS - Construire un VRT"){: .img-center loading=lazy }

Dans la boite de dialogue, indiquez les tuiles à fusionner (input layers) et décocher `Place each input file in separate band`, indiquez la projection (Lambert 93).

![Dialogue construire un VRT](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_en_relief_des_ecrins/3-vrt.jpg "QGIS - Dialogue construire un VRT"){: .img-center loading=lazy }

Supprimer les dalles et ne conservez que le résultat de la fusion.

----

## Charger les cartes

Il va maintenant falloir trouver une carte à mettre sur ces données.
Pour cela, l'IGN met à disposition [un ensemble de fond de carte qui sont situés sur Géoservice](https://geoservices.ign.fr/services-web-experts).
En particulier, pour ajouter les cartes, rendez-vous [sur cette page](https://geoservices.ign.fr/services-web-experts-cartes) pour récupérer l'URL du service :

```html
https://wxs.ign.fr/cartes/geoportail/wmts?SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetCapabilities
```

Puis rendez-vous dans l'explorateur de QGIS à gauche pour ajouter une couche WMS/WMTS (clic-droit nouvelle connexion) et coller l'URL dans le champ dédié du dialogue.

![Charger les Géoservices](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_en_relief_des_ecrins/4-WMTS.jpg "QGIS - Charger les Géoservices"){: .img-center loading=lazy }

Dans notre cas, nous allons choisir le SCAN 50 historique qui a un rendu plutôt sympa.

![Scan 50 historique](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_en_relief_des_ecrins/5-scanhisto.jpg "QGIS - Scan 50 historique"){: .img-center loading=lazy }

----

## Passez dans la 3ème dimension

Pour cela, vous devrez ajouter une extension à QGIS.
Allez dans le menu `Extension > Installer / gérer les extensions` et recherchez Qgis2threejs et installez la si ce n'est pas déjà fait.

Il vous suffit alors de cliquer sur la nouvelle icône ![Qgis2threejs](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_en_relief_des_ecrins/qgis2threejs.png "QGIS - Icône Qgis2threejs") (ou via le menu Internet).  
Dans la fenêtre, choisissez la couche terrain à utiliser (DEM = Digital Elevation Model) et dans le menu `Scene > Scene settings` réglez les paramètres de la vue.  
Vous pouvez modifier l'exagération verticale pour donner plus de relief...

![Paramètres de la scène](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_en_relief_des_ecrins/6-scene.jpg "QGIS2ThreeJS Paramètres de la scène"){: .img-center loading=lazy }

Vous pouvez fixer l'étendue de la carte (fixed extent). Dans notre cas, on peut fixer le centre à x 958500, y 6418000 et la largeur 68300 et hauteur 87000.

Vous pouvez également augmenter la résolution de la carte en faisant un clic-droit sur la couche d'élévation (DEM). Il suffit d'augmenter la largeur de la texture.

![Propriétés de la couche](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_en_relief_des_ecrins/7-DEM.jpg "QGIS2ThreeJS Propriétés de la couche"){: .img-center loading=lazy }

Ensuite, il suffit d'enregistrer le résultat 3D pour l'afficher sur une page internet (Export to web et l'extension QGis2threejs).

----

## Et voilà le résultat !

<iframe src="https://viglino.github.io/maps/static/PNE_coeur.html" width="100%" height="500"></iframe>

[Voir en plein écran :fontawesome-solid-expand:](https://viglino.github.io/maps/static/PNE_coeur.html){: .md-button }
{: align=middle }

----

<!-- geotribu:authors-block -->
