---
title: Créer une MiniMap personnalisable avec mapFish et Ext
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-11-30
description: Créer une MiniMap personnalisable avec mapFish et Ext
image: ''
tags:
    - OpenLayers
    - ExtJS
    - MapFish
    - minimap
---

# Créer une MiniMap personnalisable avec mapFish et Ext

:calendar: Date de publication initiale : 30 novembre 2008

## Introduction

Développé par [CampToCamp](http://www.camptocamp.com/), [MapFish](http://trac.mapfish.org/trac/mapfish/wiki/Home) est un famework utilisant [OpenLayers](http://openlayers.org/) pour la partie cartographie et [Ext](http://extjs.com) pour la partie GUI (Graphical User Interface).

Nous apprendrons dans ce tutoriel a créer notre propre objet MapFish afin d'enrichir la librairie existante. Celui-ci devra permettre d'afficher dans une fenêtre la mini-map d'OpenLayers.

## Comment créer une nouvelle classe avec mapFish ?

Il existe deux étapes primordiales pour réaliser un héritage de classe avec MapFish (et plus globalement avec tout langages de programmation). Tout d'abord le constructeur et ensuite l'héritage lui même.

* **Le constructeur**

Cet objet qui héritera de la classe windows d'ext permettra d'afficher dans une fenêtre flottante une mini carte. Nous y ajouterons une méthode qui permettra le placement automatique de cette mini-map dans le bloc center.

Commencons par créer notre nouvel objet. La méthode mapfish.widgets.miniMap est le [constructeur de la classe](2008-08-22_creer-des-classes-en-javascript.md). La méthode apply permet d'appeler une fonction Javascrit pour l'objet spécifié en lui passant les paramètres dans un tableau. Ainsi chacune de options de configuration que vous aurez défini deviendra des propriétés de l'objet lui même.

```javascript
mapfish.widgets.miniMap = function(config) {  
  Ext.apply(this, config);
  mapfish.widgets.miniMap.superclass.constructor.call(this);  
};
```

* **Réaliser l'héritage de classe**

Ext fournit une méthode permettant de réaliser facilement un héritage de classe. Celle-ci se nomme Ext.extend. Elle prend en premier paramètre la classe fille, puis la classe mère et enfin c'est dans le troisième argument que sera ajouté notre code.

```javascript
Ext.extend(mapfish.widgets.miniMap, Ext.Window, {  
  /*  
  *
  * Some code  
  *
  */  
});
```

A l'intérieur même de cette classe deux méthodes nous intéressent particulièrement, il s'agit de onRender et initComponent. La première va être déclenché au moment de la construction de l'objet, la seconde va permettre de créer le ou les composants à afficher. Ce qui donne :

```javascript
Ext.extend(mapfish.widgets.miniMap, Ext.Window, {

  initComponent: function() {  
    // Code  
  },

  onRender: function(container, position) {  
    // Code  
  }

});
```

## Créer la minimap

Nous allons maintenant étudier le code complet. Dans la partie **initComponent**, nous allons créer notre objet window. Nous définissons pour celui une position sur la carte grâce à la méthode **__setPosition**. Enfin celui-ci est appelé par la méthode onrender.

```javascript
/**  
* @requires OpenLayers/Map.js  
*/

Ext.namespace('mapfish.widgets');

/**  
* Class: mapfish.widgets.miniMap  
* Window that containe the miniMap.  
*  
* Typical usage:  
* (start code)  
* var minimap = new mapfish.widgets.miniMap({  
* contentEl : 'miniMap',  
* map: map,  
* positionXY : 'br'  
* });  
* (end)  
*  
* Inherits from:  
* - {Ext.Window}  
*/

/**  
* Constructor: mapfish.widgets.miniMap  
*  
* Parameters:  
* config - {Object} The config object  
*/  

mapfish.widgets.miniMap = function(config) {  
  Ext.apply(this, config);  
  mapfish.widgets.miniMap.superclass.constructor.call(this);  
};

Ext.extend(mapfish.widgets.miniMap, Ext.Window, {

  /**  
  * Defaults property params  
  */  
  title : 'Mini Map',  
  closable : false,  
  resizable : false,  
  margins: '0 0 0 0',  
  hideBorder : false,  
  collapsible : true,  
  width : 190,  
  height : 120,

  initComponent: function() {  
    var mMap = new Ext.Window({  
      title: this.title,  
      closable : this.closable,  
      resizable : this.resizable,  
      margins: this.margins,  
      hideBorder : this.hideBorder,  
      collapsible : this.collapsible,  
      width : this.width,  
      height : this.height  
    });  
    this.items = mMap;  
    mapfish.widgets.Shortcuts.superclass.initComponent.call(this);  
  },

  // private  
  onRender: function(container, position) {  
    if (!this.el) {  
      //this.el = document.createElement('divMiniMap');  
      this.contentEl = document.createElement('divMiniMap');  
    }  
    miniMap = new OpenLayers.Control.OverviewMap({div : $(this.contentEl) });  
    map.addControl(miniMap);  
    mapfish.widgets.miniMap.superclass.onRender.apply(this, arguments);  
  }
});  
Ext.reg('miniMap', mapfish.widgets.miniMap);  
```

## Un exemple concret

Et enfin, l'exemple illustrant le code ci-dessus :

![Mini Map](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/miniMap.png "Mini Map"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->
