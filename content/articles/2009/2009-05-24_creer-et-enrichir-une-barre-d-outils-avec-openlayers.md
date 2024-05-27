---
title: Créer et enrichir une barre d'outils avec OpenLayers
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2009-05-24
description: Créer et enrichir une barre d'outils avec OpenLayers
tags:
    - OpenLayers
    - Toolbar
---

# Créer et enrichir une barre d'outils avec OpenLayers

:calendar: Date de publication initiale : 24 mai 2009

## Introduction

![logo OpenLayers](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/openlayers.png "logo OpenLayers"){: .img-thumbnail-left }

OpenLayers permet, grâce à la classe [EditingToolbar](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Control/EditingToolbar-js.html), de créer facilement une barre d'outils de dessin. Nous verrons au cours de ce tutoriel comment créer notre propre barre d'outils afin d'y ajouter de nouvelles fonctionnalités.

## Création de la barre d'outils

Créer et enrichir sa propre barre d'outils n'est pas très difficile. Pour cela Openlayers met à notre disposition la classe [Panel](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Control/Panel-js.html) auquel nous ajoutons ensuite les outils que l'on souhaite à partir de la méthode [addControls](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Control/Panel-js.html#OpenLayers.Control.Panel.addControls). Regardons le code ci-dessous pour comprendre :

```javascript
//Création du l'objet Panel
panel = new OpenLayers.Control.Panel(
 {'displayClass': 'olControlEditingToolbar'}
);

controls = {
 move : new OpenLayers.Control.Navigation(),
 select : new OpenLayers.Control.SelectFeature(vectors,
  {'displayClass': 'olControlSelect'}),
 point: new OpenLayers.Control.DrawFeature(vectors,
  OpenLayers.Handler.Point,
  {'displayClass': 'olControlDrawFeaturePoint'}),
 line: new OpenLayers.Control.DrawFeature(vectors,
  OpenLayers.Handler.Path,
  {'displayClass': 'olControlDrawFeaturePath'}),
 polygon: new OpenLayers.Control.DrawFeature(vectors,
  OpenLayers.Handler.Polygon,
  {'displayClass': 'olControlDrawFeaturePolygon'}),
 zoomMaxExtent : new OpenLayers.Control.ZoomToMaxExtent
  ({'displayClass': 'olControlMaxExtent'})
}
//Ajout des outils à la barre
for(var key in controls) {
 panel.addControls([controls[key]]);
}
//Ajout de la barre à la carte
map.addControl(panel);
```

Il est possible d'adapter le css à sa guise avec l'attribut displayClass. Prenons l'exemple de l'icone select :

```javascript
.olControlEditingToolbar .olControlSelectItemActive {
    background-image: url(./select_on.png);
    background-repeat: no-repeat;
    background-position: 0px 1px;
}

.olControlEditingToolbar .olControlSelectItemInactive {
    background-image: url(./select_off.png);
    background-repeat: no-repeat;
    background-position: 0px 1px;
}
```

## Exemple

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://geotribu.net/applications/tutoriaux/openlayers/custom_toolbar/index.htm" height="500px" width="600px"></iframe>`

----

<!-- geotribu:authors-block -->
