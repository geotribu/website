---
title: Ajouter des infobulles (tooltips) avec OpenLayers et Ext
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2009-03-01
description: Ajouter des infobulles (tooltips) avec OpenLayers et Ext
tags:
    - OpenLayers
    - ExtJS
    - infobulle
    - tooltips
---

# Ajouter des infobulles (tooltips) avec OpenLayers et Ext

:calendar: Date de publication initiale : 01 mars 2009

## Introduction

Il y a quelques mois suite à l'initiative de quelques passionnés est né [GeoExt](http://www.geoext.org/trac/geoext) mariage de la librairie cartographique [OpenLayers](http://openlayers.org/) et de la librairie orienté GUI (IHM) [Ext](http://extjs.com/).

Ce tutoriel a pour objectif d'ajouter une nouvelle fonctionnalité à cette librairie GeoExt en fournissant la possibilité d'ajouter des tooltips (infobulles) au passage de la souris sur des objets de type feature. Ce n'est qu'une version 0.1 et de nombreuses améliorations sont possibles, notamment une prochaine intégration de la classe OpenLayers.popup.

## Ajouter et utiliser le script olExtToolTips

L'objet [tooltips](http://extjs.com/deploy/dev/docs/output/Ext.ToolTip.html) existe par défaut dans la librairie Ext nous l'avons modifié afin qu'il puisse être plus facilement utilisé par OpenLayers.

Pour l'utiliser, cela n'est pas très compliqué il suffit simplement, après l'avoir [téléchargé](http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/tooltips_ext/olExtToolTips.js) (ou la version [compactée](http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/tooltips_ext/olExtToolTipsPacked.js)), et de l'ajouter dans votre page de la manière suivante :

`<script src="pathTo/olExtToolTips.js" type="text/javascript""></script>`

Ensuite pour dans votre script de l'initialiser :

```javascript
tt = new GeoExt.toolTip({  
  map: map,  
  featureLayer : vectors,  
  autoHeight : true,  
  autoWidth : true,  
  hidden: true,  
  autoHide: true,  
  plain: true,  
  showDelay: 0,  
  hideDelay: 0,  
  trackMouse: true,  
  animCollapse : true  
});
```

Les propriétés initiales de l'objet ToolTips n'ont pas été modifiées, référez-vous donc à l'[API d'Ext](http://extjs.com/deploy/dev/docs/) pour savoir ce que vous pouvez ou souhaitez ajouter au constructeur.

## Exemple

![Infobulles](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/tooltips_ext.png "Infobulles"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->
