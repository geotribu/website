---
title: A la découverte de GeoExt
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2009-08-13
description: A la découverte de GeoExt
tags:
    - ExtJS
    - GeoExt
    - OpenLayers
    - open source
---

# A la découverte de GeoExt

:calendar: Date de publication initiale : 13 août 2009

## Introduction

Né de la fusion d'[OpenLayers](http://openlayers.org/) et d'[Ext](http://extjs.com/), [GeoExt](http://geoext.org/) est une librairie javascript permettant de créer facilement des d'interfaces cartographiques riches. Bien plus qu'un simple portage des deux librairies mères, GeoExt a complètement repensé les modèles de classes initiaux pour proposer au final de nouveaux objets complètement personnalisés. Néanmoins, celle-ci peut être difficile à appréhender du fait du mélange des genres entre OpenLayers et Ext. De ce fait, il est important de bien comprendre le rôle joué par chacune des composantes.

![GeoExt](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/geo_ext_lib.png "GeoExt"){: .img-center loading=lazy }

Nous découvrirons au cours de ce tutoriel les éléments principaux de GeoExt, vous pouvez également vous référez aux tutoriaux [ext-primer](http://geoext.org/primers/ext-primer.html), [openlayers-primer](http://geoext.org/primers/openlayers-primer.html) et [geoext-quickstart](http://geoext.org/tutorials/quickstart.html) réalisés par l'équipe de GeoExt.

Avant de construire notre première application, il convient d'étudier un peu l'architecture des classes de GeoExt. Celle-ci se divise en différentes [catégories](http://geoext.org/lib/GeoExt/widgets.html) que sont :

* Widgets : Composants liés à la carte (fonctionnalités, actions...) - [Exemple](http://dev.geoext.org/trunk/geoext/examples/mappanel-viewport.html)
* Form : Composants qui étendent la classe Ext.Form pour permettre la gestion des éléments cartographiques - [Exemple](http://dev.geoext.org/trunk/geoext/examples/search-form.html)
* Grid : Composants qui étendent la classe classe Ext.grid pour permettre la gestion des éléments cartographiques - [Exemple](http://dev.geoext.org/trunk/geoext/examples/feature-grid.html)
* tree : Composants qui étendent la classe classe Ext.tree pour permettre la gestion des éléments cartographiques - [Exemple](http://dev.geoext.org/trunk/geoext/examples/tree.html)
* data : Composants qui étendent la classe classe Ext.data pour permettre la gestion de données cartographiques - [Exemple](http://dev.geoext.org/trunk/geoext/examples/wms-capabilities.html)

## L'objet MapPanel, coeur de l'application

L'objet [Map](http://dev.openlayers.org/releases/OpenLayers-2.8/doc/apidocs/files/OpenLayers/Map-js.html) d'OpenLayers et [l'objet Panel](http://extjs.com/deploy/dev/docs/?class=Ext.Panel) d'Ext sont les objets centraux de ces librairies. La fusion de ces deux classes à donné naissance dans GeoExt à l'objet [MapPanel](http://geoext.org/lib/GeoExt/widgets/MapPanel.html). C'est lui qui aura à charge de "construire" la carte ainsi que son conteneur (panel).

L'objet ViewPort, que nous utilisons dans l'exemple ci-dessous, à la particularité de prendre automatiquement tout l'espace disponible. C'est à l'intérieur de celui-ci que nous allons construire les différents éléments de notre application. Pour cela nous spécifions que la propriété `layout` de l'objet Viewport est de type `border`. Cela signifie que son espace interne sera divisé en 5 zones (north, east, south, west et center). La zone "center" prenant automatiquement tout le reste d'espace disponible en fonction des dimensions des autres panels.

Étudions en détail l'exemple ci-dessous :

* [1] - Liste des couches qui sera ajoutée ensuite à l'objet MapPanel
* [2] - Construction de l'objet MapPanel.
* [3] - Panel qui accueillera ensuite une légende, un tableau de données ...
* [4] - Construction de l'objet Ext 'ViewPort" auquel on ajoute l'objet MapPanel

```javascript
Ext.onReady(function() {  
    // [1] - layer
 var bluemarble = new OpenLayers.Layer.WMS(
  "bluemarble"
  ,"http://sigma.openplans.org/geoserver/wms?"
  ,{layers: 'bluemarble'}
 );

    // [2] - MapPanel
 var mapUI = new GeoExt.MapPanel({
        map: {
            controls: [new OpenLayers.Control.Navigation()]
        }
        ,region : 'center'
        ,title : 'map'
        ,layers: [bluemarble]
        ,extent: [-5, 35, 15, 55]
    });

     // [3] - Data Panel
 var dataPanel = new Ext.Panel({  
        region : 'west'
        ,layout : 'fit'
        ,width : 150  
    });  

    // [4] - Final User Interface
    new Ext.Viewport({
        layout: "border"
        ,items: [
            mapUI
            ,dataPanel
        ]
    });  
}); //EOF Ext.onReady
```

Il est déjà facile de voir l'un des avantages de GeoExt, le prototypage rapide d'interface. En effet, en quelques lignes de code nous avons dors et déjà une application fonctionnelle qui pourra servir ensuite de base à une réflexion plus approfondie.

## Enrichir l'interface

Nous allons maintenant habiller notre interface pour cela GeoExt propose plusieurs classes regroupées au sein de la classe parent Widgets. Celle que nous allons utiliser est [ZoomSlider](http://geoext.org/lib/GeoExt/widgets/ZoomSlider.html) qui permet de disposer d'un outil de zoom par niveaux. De plus nous allons en profiter pour améliorer un peu le design de notre application en modifiant notre fichier CSS.

Regardons en détail notre exemple d'enrichissement de l'interface :

* [1] - Nous construisons notre objet ZoomSlider dont le but est d'offrir un outil de zoom avant et arrière.
* [2] - Par rapport à l'exemple précédent l'attribut items a été ajouté à l'objet mapPanel. Il référence notre objet ZoomSlider.

```javascript
// [1] - ZoomSlider
var zSlider = new GeoExt.ZoomSlider({
    vertical: true
    ,height: 110
    ,x: 18
    ,y: 85
    ,map: mapPanel
    ,plugins: new GeoExt.ZoomSliderTip({
        template: '<div>Zoom Level: <b>{zoom}</b></div>'
    })
});

// [2] - MapPanel
var mapPanel = new GeoExt.MapPanel({
    map: {
        controls: [
            new OpenLayers.Control.Navigation()
            ,new OpenLayers.Control.PanPanel()
            ,new OpenLayers.Control.ZoomPanel()
        ]
    }
    ,region : 'center'
    ,title : 'map'
    ,layers: [bluemarble]
    ,extent: [-5, 35, 15, 55]
    ,items  : [zSlider]
});
```

Dans notre exemple nous avons fait le choix de n'afficher que le niveau de zoom lors de l'utilisation du zoomSlider. Mais vous pouvez également y ajouter l'échelle ou la résolution en cours.

Comme vous avez pu le constater l'ajout d'une nouvelle fonctionnalité ne nous a pas obligé à casser tout notre code. L'architecture est dès le départ bien pensée (Merci Ext).

## Ajout de l'arbre de couches

Il existe différentes façons de créer notre arbre de couche. Soit en instanciant un à un à chacun des objets ou alors en créant un "pseudo" fichier de configuration. Nous verrons successivement chacune d'entre elles.

La création initiale de l'arbre de couches se fait via l'objet Ext [TreeNode](http://extjs.com/deploy/dev/docs/?class=Ext.tree.TreeNode) auquel nous ajoutons ensuite des "feuilles" via la méthode appendChild. GeoExt permet grâce aux méthodes [GeoExt.tree.BaseLayerContainer](http://www.geoext.org/lib/GeoExt/widgets/tree/BaseLayerContainer.html) et [GeoExt.tree.OverlayLayerContainer](http://www.geoext.org/lib/GeoExt/widgets/tree/OverlayLayerContainer.html) de créer plus facilement les "feuilles" de cet arbre en se basant sur l'organisation des couches d'OpenLayers

Étudions en détails l'exemple de création de notre arbre de couches :

* [1] - Création de la racine de l'arbre (la base).
* [2] - Ajout des couches de base.
* [3] - Ajout des couches Overlay.
* [4] - Création du panel contenant notre arbre de couche.

```javascript
//[1] - Tree Layer
var layerRoot = new Ext.tree.TreeNode({
    text        : "All Layers"
    ,expanded   : true
    ,loader: new GeoExt.tree.LayerLoader({
        applyLoader : true
    })
});

//[2] - Base Layers
layerRoot.appendChild(new GeoExt.tree.BaseLayerContainer({
    text        : "Base Layers"
    ,map        : mapPanel.map
    ,expanded   : true
}));

//[3] - Overlay
layerRoot.appendChild(new GeoExt.tree.OverlayLayerContainer({
    text        : "Overlays"
    ,map        : mapPanel.map
    ,expanded   : true
}));

//[4] - Creation du panel
var layerTree = new Ext.tree.TreePanel({
    title       : "Map Layers"
    ,root       : layerRoot
    ,expanded   : true
    ,animate    : true
});
```

Plutôt sympa comme résultat non? Et tout ça en à peine une vingtaine de ligne de code. Néanmoins, cela fait beaucoup d'objet à créer non? Ne serait-il pas plus facile d'utiliser un fichier de configuration? Comme cela est visible sur cet exemple, cela est tout à fait possible, testons-le immédiatement :

```javascript
var treeConfig = new OpenLayers.Format.JSON().write([
    {
        nodeType    : 'gx_baselayercontainer'
        ,expanded   : true
        ,allowDrag  : false
        ,allowDrop  : false
        ,draggable  : false
        ,icon       : './img/map.png'
    },{
        text        : 'Overlays'
        ,icon       : './img/maps-stack.png'
        ,expanded   : true
        ,children   : [
            {
                nodeType    : 'gx_layer'
                ,draggable  : false
                ,layer      : 'city'
                ,qtip       : "Villes d'Europe"
                ,icon       : './img/city-16x16.png'
            },{
                nodeType    : 'gx_layer'
                ,layer      : 'moutains'
                ,qtip       : "Montagnes d'Europe"
                ,icon       : './img/Mountain-16x16.png'  
            }  
        ]
    }
], true);
```

La variable `treeConfig` contient toute l'architecture de l'arbre de couches. L'exemple n'est pas difficile à comprendre mais j'aimerais attirer votre attention sur la propriété `nodeType`. Celle-ci peut prendre trois valeurs : gx_baselayercontainer, gx_overlaylayerontainer (classe [LayerNode](http://www.geoext.org/lib/GeoExt/widgets/tree/LayerNode.html)) et `gx_layer` (classe [LayerNode](http://www.geoext.org/lib/GeoExt/widgets/tree/LayerNode.html)) qui correspond successivement aux couches de bases, aux couches superposables et à toutes les couches. C'est cette dernière qui nous interesse car nous allons pouvoir construire notre branche en spécifiant exactement la couche correspondante tout en lui ajoutant des options de personnalisation (comme une icon ou un qtip).

Comme nous souhaitons également ajouter plus tard un tableau de données à ce panel (zone), nous allons immédiatement modifier ses caractéristiques afin qu'il se comporte comme un accordéon :

```javascript
var accordion = new Ext.Panel({
    margins : '5 0 5 5'
    ,split  : true
    ,width  : 160
    ,layout :'accordion'
    ,items  : [layerTree]
});  

//Data Panel
var dataPanel = new Ext.Panel({  
title   : 'Legend & Data'  
    ,region : 'west'
    ,layout : 'fit'
    ,width  : 160  
    ,items  : [accordion]
});
```

Passons maintenant à notre tableau de données.

## Ajout des données vecteurs

Si vous n'avez pas encore été convaincu par GeoExt, l'objet [FeatureStore](http://www.geoext.org/lib/GeoExt/data/FeatureStore.html) de la classe data vous fera certainement basculer définitivement. Imaginez simplement que vous puissiez, à partir d'un simple objet, créer un tableau de données ainsi que les données cartographiques associées et qu'en plus ces deux éléments soient liés entre eux. C'est ce que permet FeatureStore auquel nous avons ajouté dans l'exemple ci-dessous l'objet FeatureSelectionModel dont le but est de gérer les interactions entre les deux éléments.

Étudions en détails notre exemple :

* [1] - Creation de l'objet FeatureStore (entrepôt de données) dans lequel nous définissons la structure des données (fields).
* [2] - Creation de l'objet Grid (tableau) contenant l'entrepôt de données. Nous spécifions également que la propriété sm (selection model) prend pour valeur FeatureSelectionModel
* [3] - Ajout du tableau dans l'application.

```javascript
// [1] - Creation de l'entrepot de donnees
store = new GeoExt.data.FeatureStore({
    layer: city
    ,fields: [
        {name: 'Name', type: 'string'}
        ,{name: 'Country', type: 'string'}
    ]
});

// [2] - Creation du tableau
gridPanel = new Ext.grid.GridPanel({
    title: "Feature Grid"
    ,store: store
    ,columns: [{
        header: "Name"
        ,width: 100
        ,dataIndex: "Name"
    }, {
        header: "Country"
        ,width: 60
        ,dataIndex: "Country"
    }],
    sm: new GeoExt.grid.FeatureSelectionModel()
});

// [3] - Ajout du tableau a l'interface
var grid = new Ext.Panel({
    title   : 'Grid'
    ,layout :'fit'
    ,items  : [gridPanel]
});
```

## Affichage d'une infobulle

La création d'une infobulle se fait via la classe [GeoExt.Popup](http://www.geoext.org/lib/GeoExt/widgets/Popup.html). Sa création n'a rien de compliqué et se passe je pense de commentaire :

Ci-dessous le code ayant servi à notre exemple :

```javascript
city.events.on({
        featureselected: function(e) {  
        if(typeof(popup) != "undefined"){
            popup.destroy();
        }
        var content = "<b>"+e.feature.attributes.Name+
                      "</b><br /> Lon : "+e.feature.attributes.Longitude+
                      "<br /> Lat : "+e.feature.attributes.Latitude;

        popup = new GeoExt.Popup({
            title       : 'City'
            ,feature    : e.feature
            ,width      : 200
            ,html       : content
            ,collapsible: true
            ,anchored   : true
        });  
        popup.show();
    }
});
```

## Conclusion

J'espère que ce petit tour d'horizon de GeoExt vous donnera envie de continuer dans l'exploration de cette fantastique librairie. Le mariage de deux librairies dont les objectifs et les concepts sont différents n'est pas une chose aisée et pourtant les développeurs de GeoExt ont réussi ce tour de force.

----

<!-- geotribu:authors-block -->
