---
title: "Faire une carte en relief des Écrins"
authors:
    - Viglino
categories:
    - article
    - tutoriel
date: 2021-10-10 00:00
description: "Réalisez facilement une carte en relief du Parc National des Écrins avec des données IGN et QGIS."
image: "https://camo.githubusercontent.com/c8c6044847a7d623c9bd638181da2e143454f3aa1cc85feb06e697e152941552/68747470733a2f2f692e696d6775722e636f6d2f4c3871384373332e706e67"
license: default
tags: 
    - TutoCarto
    - QGIS
    - BDAlti
    - ThreeJS
    - relief
    - DEM
    - 3D
breaks: false
---
# 🗺️ Faire une carte en relief des Écrins

Aujourd'hui, nous allons voir comment réaliser une carte en relief du [Parc National des Écrins](https://fr.wikipedia.org/wiki/Parc_national_des_%C3%89crins). 
Vous pouvez suivre le déroulement [sur la vidéo <i class="fa fa-youtube-play"></i>](https://youtu.be/wJjlKoSkmjY) (activez les sous-titres).

<iframe width="100%" height="315" src="https://www.youtube-nocookie.com/embed/wJjlKoSkmjY?cc_load_policy=1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Pour cela, nous aurons besoins : 
- d'un modèle numérique de terrain (MNT)
- d'un fond de carte
- et d'un logiciel SIG ([QGis](https://www.qgis.org/fr/site/))

Mais tout d'abord, il nous faut trouver une emprise du parc pour nous repérer. Un fichier est disponible sur [le catalogue des parcs nationaux](https://catalogue.parcnational.fr/catalogue/pne/fre/catalog.search#/metadata/b1b74e1bffa193453a75cccc39f6f304c8cc5561a03b2729092127ebf81439ff) qui publie des données relatives aux parcs nationaux dans le cadre de la directive INSPIRE.

Ouvrez [QGis](https://www.qgis.org/fr/site/) et faites glisser le fichier sur la fenêtre pour afficher cette limite.

## Le MNT


### Charger les données

Il va nous falloir un modèle numérique de terrain pour plaquer la carte dessus.
Vous en trouverez disponible en OpenData [sur le site de l'IGN, rubrique BDAlti <i class="fa fa-external-link"></i>](https://geoservices.ign.fr/bdalti).
![](https://geoservices.ign.fr/sites/default/files/2021-05/bdalti_Visuel.png)
Il faudra charger les deux départements de l'Isère (38) et les Hautes-Alpes (05) sur lesquels se trouve le parc.
Attention, ils sont fournis en ftp et il vous faudra un logiciel tel que [FileZilla](https://filezilla-project.org/) pour les charger. Sinon ils sont également disponible en téléchargement sur [opendatarchives.fr](https://files.opendatarchives.fr/professionnels.ign.fr/bdalti/).
- [le MNT del'Isère (06) <i class="fa fa-download"></i>](https://files.opendatarchives.fr/professionnels.ign.fr/bdalti/BDALTIV2_2-0_25M_ASC_LAMB93-IGN69_D005_2021-08-04.7z)
- [le MNT Hautes-Alpes (38)  <i class="fa fa-download"></i>](https://files.opendatarchives.fr/professionnels.ign.fr/bdalti/BDALTIV2_2-0_25M_ASC_LAMB93-IGN69_D038_2020-11-13.7z)

### Afficher les données

Décompressez les fichiers chargés précédemment et faite glisser les fichiers `.asc` dans le fenêtre de QGis.
Il vous faudra définir le système de coordonnées de référence (SCR) pour les données afin que QGis sache comment placer ces fichiers sur la carte. Faites un clic-droit sur la couche pour définir le SCR.
![](https://i.imgur.com/cVAmody.png)

Les données sont dans le système Lambert 93 (code 2154).
![](https://i.imgur.com/2PPPWrG.png)

Comme le parc est à cheval sur deux départements, le plus simple est de recopier les fichiers `.asc` des deux archives dans un même répertoire et de les faire glisser tous ensemble sur QGis. On peut ensuite les sélectionner et changer leur SCR en une seule fois.

### Préparer le terrain

En fait, vous n'aurez pas besoins de tous les fichier, seul ceux qui se superposent avec le parc sont nécessaires.

Soit les fichiers :
- BDALTIV2_25M_FXX_**0925_6400**_MNT_LAMB93_IGN69.asc
- BDALTIV2_25M_FXX_**0925_6425**_MNT_LAMB93_IGN69.asc
- BDALTIV2_25M_FXX_**0925_6450**_MNT_LAMB93_IGN69.asc
- BDALTIV2_25M_FXX_**0925_6475**_MNT_LAMB93_IGN69.asc
- BDALTIV2_25M_FXX_**0950_6400**_MNT_LAMB93_IGN69.asc
- BDALTIV2_25M_FXX_**0950_6425**_MNT_LAMB93_IGN69.asc
- BDALTIV2_25M_FXX_**0950_6450**_MNT_LAMB93_IGN69.asc
- BDALTIV2_25M_FXX_**0950_6475**_MNT_LAMB93_IGN69.asc
- BDALTIV2_25M_FXX_**0975_6400**_MNT_LAMB93_IGN69.asc
- BDALTIV2_25M_FXX_**0975_6425**_MNT_LAMB93_IGN69.asc
- BDALTIV2_25M_FXX_**0975_6450**_MNT_LAMB93_IGN69.asc
- BDALTIV2_25M_FXX_**0975_6475**_MNT_LAMB93_IGN69.asc

Il faudra encore une petite opération si vous voulez éviter les discontinuités en bord de tuile : il va falloir les fusionner.
Dans le menu, choississez `Raster > Divers > Fusionner` et indiquez les tuiles à fusionner.

![](https://i.imgur.com/c2UShiQ.png)

Supprimer les dalles et ne conservez que le résultat de la fusion.

## Charger les cartes

Il va maintenant falloir trouver une carte à mettre sur ces données.
Pour cela, l'IGN met à disposition [un ensemble de fond de carte sur sont sit Géoservice](https://geoservices.ign.fr/services-web-experts).
En particulier, pour ajouter les cartes, rendez-vous [sur cette page](https://geoservices.ign.fr/services-web-experts-cartes) pour récupérer l'url du service : 
```html
https://wxs.ign.fr/cartes/geoportail/wmts?SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetCapabilities
```
Puis rendez-vous dans l'explorateur de QGIS à gauche pour ajouter une couche WMS/WMTS (clic-droit nouvelle connexion) et coller l'url dans le champ dédié du dialogue.

![](https://i.imgur.com/H79A9nN.png)

Dans notre cas, nous allons choisir le SCAN historique qui a un rendu plutôt sympa.

![](https://i.imgur.com/yCfwagS.jpg)


## Passez dans la 3ième dimension

Pour cela, vous devrez ajouter une extension à QGis. 
Allez dans le menu `Extension > Installer / gérer les extensions` et recherchez Qgis2threejs et installez la si ce n'est pas déjà fait.

Il vous suffit alors de cliquer sur la nouvelle icone ![](https://i.imgur.com/qzmotVy.png) (ou via le menu Internet).
Dans la fenêtre, choissez la couche terrain à utiliser (DEM = Digital Elevation Model) et dans le menu `Scene > Scene settings` règlez les paramètres de la vue.
Vous pouvez modifier l'exagération vertical pour donner plus de relief...

![](https://i.imgur.com/0GjwdiZ.png)

Vous pouvez fixer l'étendue de la carte (fixed extent). Dans notre cas, on peut fixer le centre à x 958500, y 6418000 et la largeur 68300 et hauteur  87000.

Vous pouvez également augmenter la résolution de la carte en faisant un clic-droit sur la couche d'élévation (DEM). Il suffit d'augmenter la largeur de la texture.

![](https://i.imgur.com/TlusqjN.png)

Ensuite, il suffit d'enregistrer le résultat 3D pour l'afficher sur une page internet (Export to web et l'extension QGis2threejs).

## Et voilà le résultat...

<iframe src="https://viglino.github.io/maps/static/PNE_coeur.html" width="100%" height="500"></iframe>

[Voir en plein écran <i class="fa fa-external-link"></i>](https://viglino.github.io/maps/static/PNE_coeur.html)
    
