---
title: Une infobulle à la GoogleMaps avec GeoExt
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2009-08-16
description: Une infobulle à la GoogleMaps avec GeoExt
tags:
    - GeoExt
    - Open Source
---

# Une infobulle à la GoogleMaps avec GeoExt

:calendar: Date de publication initiale : 16 août 2009

## Introduction

Une des fonctionnalités qui me semble intéressante dans la librairie GoogleMaps et que je n'ai encore trouvé nulle part ailleurs est la possibilité d'afficher des infobulles avec des onglets. Mais avec l'arrivée de GeoExt et de sa classe [Popup](http://www.geoext.org/lib/GeoExt/widgets/Popup.html) hautement personnalisable cela est dorénavant faisable. Regardons comment y arriver.

## Création du popup

L'objet Popup de GeoExt hérite de la classe [Windows](http://extjs.com/deploy/dev/docs/?class=Ext.Window) d'EXT. Dans celle-ci il est possible d'ajouter des éléments supplémentaires via la propriété `items`, dans notre cas nous y ajouterons un objet [tabPanel](http://extjs.com/deploy/dev/docs/?class=Ext.TabPanel).

Regardons en détail comment cela se passe :

```javascript
var tab = new Ext.TabPanel({
    activeTab : 0
    ,border:false
    ,items: [{
        title: 'Texte',
        html : "Lorem ipsum dolor sit ame ... id est laborum"
    },{
        title: 'Image',
        html: 'another content'
    }]
});

popup = new GeoExt.Popup({
    feature    : e.feature
    ,closable   : false
    ,unpinnable : false
    ,collapse   : false
    ,collapsible: false
    ,resizable : false
    ,width      : 250
    ,height     : 250
    ,anchored   : true  
    ,layout : 'fit'
    ,items: [ tab ]
});
```

Comme vous pouvez le constater cela n'a rien de compliqué, juste une simple utilisation des composants de base d'Ext et de GeoExt.

## Exemple

[![Exemple de popup](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/exemple_popup.png "Exemple de popup"){: .img-center loading=lazy }](http://geotribu.net/applications/tutoriaux/GeoExt/tutoriel/popup_gmap.html)

----

<!-- geotribu:authors-block -->
