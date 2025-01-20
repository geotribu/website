---
title: Personnaliser les icônes et controles d'OpenLayers
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-12-22
description: Personnaliser les icônes et controles d'OpenLayers
image: ''
tags:
    - OpenLayers
    - icône
---

# Personnaliser les icônes et controles d'OpenLayers

:calendar: Date de publication initiale : 22 décembre 2008

## Introduction

![Logo OpenLayers](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/openlayers.png){: .img-thumbnail-left }

Même si la librairie OpenLayers se veut la plus souple et la plus ouverte possible, certaines parties sont encore codées en dures. C'est le cas notamment pour tout ce qui traite de la customisation.

La nouvelle classe proposée dans ce tutoriel, qui hérite de [PanZoom](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Control/PanZoom-js.html), vous permettra de personnaliser facilement vos controls.

## Personnaliser la classe PanZoom

La première étape consiste à télécharger le fichier "[PanZoomCustom](http://ks356007.kimsufi.com/arno/lib/js/OpenLayers/lib/OpenLayers/Control/PanZoomCustom.js)" ainsi qu'un [pack](http://ks356007.kimsufi.com/arno/lib/js/OpenLayers/img/olayers_icone/olayers_icone.tar.gz) contenant de nouvelles icônes. Ce pack doit être placé dans le répertoire img d'OpenLayers, le fichier JavaScript doit lui être copier dans le répertoire OpenLayers/Controls.

## Exemple d'utilisation

Vous devez ensuite appeler cette nouvelle classe dans votre page qui affichera votre carte. Cela se passe de la manière suivante :

```javascript
custom = new OpenLayers.Control.PanZoomCustom({
   imgPanup : "north_blue_square_glossy.png",
   imgPanleft : "west_blue_square_glossy.png",
   imgPanright : "east_blue_square_glossy.png",
   imgPandown : "south_blue_square_glossy.png",
   imgZoomin : "z_plus_blue_square_glossy.png",
   imgZoomworld : "z_world.png",
   imgZoomout : "z_moins_blue_square_glossy.png",
  });
map.addControl(custom);
```

Par rapport au code d'origine, outre le fait de pouvoir disposer de nouvelles icônes, cette classe apporte une nouvelle action qui permet au survol de la souris de faire un rollover donnant ainsi l'illusion que le bouton est enfoncé.

Ci-dessous voici quelques exemples présentant cette nouvelle classe ainsi que les icônes :

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/openlayers/customisation/glossy_blue.htm" height="400px" width="100%"></iframe>`

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/openlayers/customisation/glossy_red_square.htm" height="400px" width="100%"></iframe>`

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/openlayers/customisation/white_circle.htm" height="400px" width="100%"></iframe>`

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/openlayers/customisation/glossy_green.htm" height="400px" width="100%"></iframe>`

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/openlayers/customisation/glossy_green_square.htm" height="400px" width="100%"></iframe>`

----

<!-- geotribu:authors-block -->
