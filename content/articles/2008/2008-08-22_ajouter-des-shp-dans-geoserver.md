---
title: "Ajouter des SHP dans GeoServer"
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-08-22
description: "Ajouter des SHP dans GeoServer"
tags:
    - GeoServer
    - shapefiles
---

# Ajouter des SHP dans GeoServer

:calendar: Date de publication initiale : 22 août 2008

## Introduction

![logo GeoServer](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/geoserver.png "logo GeoServer"){: .img-thumbnail-left }

Nous apprendrons ici comment ajouter des données de type SHP (esri) dans GeoServer. Il est nécéssaire que vous ayez auparavant GeoServer d'installé et que vous l'ayez démarré.

Ce tutorial s'inspire en grande partie de celui proposé sur le site de GeoServer intitulé User Tutorial ShapeFile. Pour les personnes désireuses d'approfondir leurs connaissance, je ne saurais que vous conseiller d'aller y jeter un oeil.

Voici les grandes étapes qui composent ce tutorial. Elles seront ensuite expliquées plus en détails et accompagnées de captures d'écran.

1. Copiez vos shapefiles dans le répertoire `/data_dir/data/` situé dans le répertoire d'installation de GeoServer
2. Créez un nouvel Entrepôt dont la source pointe vers vos donnés `file:data/myShapefile.shp`
3. Créez un nouveau type de données qui pointe sur votre entrepôt
4. Définissez la valeur SRS de votre shp (soyez sûr que votre shp dispose d'un .prj)
5. Définissez l'emprise de votre couche
6. Validez
7. Visualisez votre couche en vous rendant dans la partie prévisualisation des cartes de la page de démonstration
8. Visualisez vos données dans GoogleEarth en copiant une url de ce type (mais en changeant myFeatureType), le port 8080 étant le port par défaut pour GéoServer :

```html
http://localhost:8080/geoserver/wms/kml_reflect?layers=myFeatureType
```

## Préparation des données

Dans un premier temps vous allez devoir copier vos donné dans le répertoire /data_dir/data/ du répertoire d'installation de GeoServer. Vous pouvez, si vous le souhaitez, changer le chemin par défaut des data.

### Windows

Ordinateur->Propriété->Paramètres Systèmes Avancés->Variables d'environnement

Ajoutez ou modifiez la variable `GEOSERVER_DATA_DIR` pour qu'elle pointe vers votre entrepôt de donné

### Linux

Pour un changement temporaire il faut exporter la variable d'environnement DATA DIR : (dans un shell) `export GEOSERVER_DATA_DIR=/home/path_to_myData/`

Pour que ce changement soit permanent modifier le fichier `.bashrc` en conséquence.

## Ajout des données à GeoServer

Les premières étapes sont assez simples, elles sont résumées par les 4 images ci-dessous. Nous allons spécifier à GéoServer que nous allons ajouter une nouvelle donnée

![Configuration](https://cdn.geotribu.fr/img/articles-blog-rdp/serveur/geoserver/configuration.jpg "Configuration"){: .img-center loading=lazy }

![Données](http://ks356007.kimsufi.com/arno/geotribu/img_site/tutoriaux/geoserver/donnees.jpg "Données"){: .img-center loading=lazy }

![Entrepots](http://ks356007.kimsufi.com/arno/geotribu/img_site/tutoriaux/geoserver/entrepots.jpg "Entrepots"){: .img-center loading=lazy }

![Nouveau entrepot](http://ks356007.kimsufi.com/arno/geotribu/img_site/tutoriaux/geoserver/nouveau_entrepot.jpg "Nouveau entrepot"){: .img-center loading=lazy }

Nous allons spécifier le type de données que nous allons utiliser (dans notre cas du Shp) :

![Data shape](http://ks356007.kimsufi.com/arno/geotribu/img_site/tutoriaux/geoserver/data_shape.jpg "Data shape"){: .img-center loading=lazy }

Nous allons, pour finir, décrire la donnée. Pour cela il faut lui assigner un style :

![Style](http://ks356007.kimsufi.com/arno/geotribu/img_site/tutoriaux/geoserver/style.jpg "Style"){: .img-center loading=lazy }

Et enfin définir son système de projection (Rechercher un SRS) ainsi que son emprise spatiale (Générer) :

![Edition](http://ks356007.kimsufi.com/arno/geotribu/img_site/tutoriaux/geoserver/edition.jpg "Edition"){: .img-center loading=lazy }

![Entite](http://ks356007.kimsufi.com/arno/geotribu/img_site/tutoriaux/geoserver/entite.jpg "Entite"){: .img-center loading=lazy }

Vous devez enfin appliquer puis sauvegarder les modifications

![Sauvegarde](http://ks356007.kimsufi.com/arno/geotribu/img_site/tutoriaux/geoserver/sauvegarde.jpg "Sauvegarde"){: .img-center loading=lazy }

## Visualisez ses données

La visulation de vos données pourra se faire sous différents formats (pdf, KML, SVG, OpenLayers....). Pour cela vous devez vous rendre dans la partie démonstration puis prévisualisation des cartes :

![Démo](http://ks356007.kimsufi.com/arno/geotribu/img_site/tutoriaux/geoserver/demo.jpg "Démo"){: .img-center loading=lazy }

![Carte](http://ks356007.kimsufi.com/arno/geotribu/img_site/tutoriaux/geoserver/carte.jpg "Carte"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->
