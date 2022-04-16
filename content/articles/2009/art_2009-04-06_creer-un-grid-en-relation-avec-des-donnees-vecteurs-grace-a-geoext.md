---
authors:
- Arnaud Vandecasteele
categories:
- article
date: 2009-04-06 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- GeoExt
- OpenLayers
- ExtJS
- grid
title: Créer un grid en relation avec des données vecteurs grâce à GeoExt
---

# Créer un grid en relation avec des données vecteurs grâce à GeoExt


:calendar: Date de publication initiale : 06 avril 2009


----

### Introduction




---


[GeoExt](http://www.geoext.org/trac/geoext) a pour objectif de fournir une bibliothèque de fonctions couplant [OpenLayers](http://www.openlayers.org/) pour la partie cartographique et [Ext](http://extjs.com/) pour la partie IHM ([billet blog](http://geotribu.net/node/75)). Même si nous en sommes encore aux prémices, les fonctionnalités qu'il est possible d'imaginer en consultant les [démos d'Ext](http://extjs.com/deploy/dev/examples/samples.html) et les exemples déjà disponibles ([Tree](http://demo.opengeo.org/ems/examples/gx-tree-demo.html), [MapPanel](http://geoext.blogspot.com/2009/03/geoext-mappanel-is-born.html) et [PopUp](http://geoext.blogspot.com/2009/03/new-widget-in-geoext-popup.html)) laissent à penser que c'est de cette librairie que s'inspireront nos applications cartographiques de demain.


### Déclarons les fichiers nécessaires




---


Commençons tout d'abord par la [télécharger](http://www.geoext.org/trac/geoext/wiki/Development) (téléchargement par SVN - révision 351 au moment où j'ai réalisé ce script) et télécharger la nouvelle classe [GridPanelFeature](http://ks356007.kimsufi.com/arno/lib/js/geoext/geoext/lib/GeoExt/grid/GridPanelFeature.js) (ou en [version compactée](http://ks356007.kimsufi.com/arno/lib/js/geoext/geoext/lib/GeoExt/grid/GridPanelFeature_packed.js) 1,9ko) .


Maintenant appelons les différents scripts nécessaires :


`xml version="1.0" encoding="UTF-8"?  







OpenLayers map preview`









Ici nous avons appelé notre fichier JavaScript GridPanelFeature.js directement dans la page Html. Nous aurions pu également le déclarer dans la variable jsfiles du fichier GeoExt.js (geoext/geoext/lib) :


`var jsfiles = new Array(  

"GeoExt/data/FeatureRecord.js",  

"GeoExt/data/FeatureReader.js",  

"GeoExt/data/FeatureStore.js",  

"GeoExt/data/FeatureStoreMediator.js",  

"GeoExt/data/LayerRecord.js",  

"GeoExt/data/LayerReader.js",  

"GeoExt/data/LayerStore.js",  

"GeoExt/data/LayerStoreMediator.js",  

"GeoExt/data/ProtocolProxy.js",  

"GeoExt/widgets/MapPanel.js",  

"GeoExt/widgets/Popup.js",  

//Personnal JavaScript file  

"GeoExt/grid/GridPanelFeature.js"  

);`


### Création de notre objet GridPanelFeature




---


La création de l'objet GridPanelFeature se fait exactement de la même façon que l'objet [GridPanel](http://extjs.com/deploy/dev/docs/?class=Ext.grid.GridPanel) de Extjs à ceci près qu'il a besoin d'un store particulier, featureStore. Ce dernier n'est pas encore disponible dans la version svn car encore en discussion.


Passons maintenant à notre objet :


`Layer = new OpenLayers.Layer.GML('Disaster','./data/YourGMLLayer.gml');  

map.addLayer(Layer);`


var featureStore = new GeoExt.data.FeatureStore({  

fields: [  

{name: 'ID', type: 'int'}  

,{name: 'NAME', type: 'string'}  

,{name: 'REGION', type: 'string'}  

,{name:'idFeature', type:'int'}  

,{name: 'Y\_2004', type: 'int'}  

],  

layer : Layer  

});


var olGrid = new GeoExt.grid.GridPanelFeature({  

store: featureStore,  

width:300,  

columns: [{  

header: "Pays",  

width:100,  

dataIndex: "NAME"  

},{  

header: "Population touchée",  

width:170,  

dataIndex: "Y\_2004"  

}],//EOF columns  

});  




Comme souligné précédemment, le store inclut dans le GridPanelfeature est un peu particulier, il prend directement en argument le fichier contenant les entités vecteurs que l'on souhaite afficher. La méthode createLayer va ensuite créer la couche comme cela se fait habituellement dans OpenLayers.


### Démo




---


[![GridPanelFeature.png](/sites/default/files/Tuto/img/GridPanelFeature.png)](http://geotribu.net/applications/tutoriaux/GeoExt/disaster/index.html)




----

## Auteur

--8<-- "content/team/avdc.md"
