---
title: Ajouter de nouvelles fonctionnalités à la bibliothèque OpenLayers
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-08-31
description: Ajouter de nouvelles fonctionnalités à la bibliothèque OpenLayers
tags:
    - OpenLayers
---

# Ajouter de nouvelles fonctionnalités à la bibliothèque OpenLayers

:calendar: Date de publication initiale : 31 août 2008

## Etendre l'API d'OpenLayers

![Logo OpenLayers](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/openlayers.png){: .img-thumbnail-left }

Une fonctionnalité qui , à mon sens, manque à [OpenLayers](http://openlayers.org/ "Site internet <a href=") est la possibilité d'ajouter des "toolTips" sur un marqueur au passage de la souris. J'avais à l'époque réalisé un script, et même si il fonctionnait, il restait trés éloigné des standards de dévellopements. En effet, [OpenLayers](http://openlayers.org/ "Site internet OpenLayers") propose des moyens simples permettant facilement d'étendre l'API actuelle.

Pour cela nous utiliserons l'idée précédente qu'était de pouvoir afficher des toolTips au passage de la souris et nous développerons notre propre module qui s'interfacera natullerement avec [OpenLayers](http://openlayers.org/ "Site internet OpenLayers"). Pour cela je me suis inspiré de ce script d'affichage de [label](http://trac.openlayers.org/ticket/751 "Script label OpenLayers") dans lequel j'ai ajouté ensuite quelques particularités.

Ajouter de nouvelles classes à OpenLayers n'est pas très difficile. Deux points sont important, tout d'abord bien comprendre la réalisation d'un héritage et savoir définir le constructeur.

## Déclarer un nouvel objet et réaliser un héritage

Il y a peu de chance que vous ayez à créer un nouvel objet de base. La plupart des scripts que vous serez amenés à réaliser viendront enrichir l'API existante en se basant sur des objets déjà existants. Nous devrons donc effectuer un mécanisme d'héritage. Cela se passe de la manière suivante :

```javascript
OpenLayers.ObjetOpenLayers.MaNouvelleMethode = OpenLayers.Class(OpenLayers.ClasseMere, {  
//code  
}
```

Tiens tiens, cette manière de faire rappel est étrangement similaire à Prototype ! non ? En fait, c'est tout à fait normal puisqu'[OpenLayers](http://openlayers.org/ "Site internet OpenLayers") se base en partie sur cette bibliothèque.

Partant de là que souhaitons nous faire ? Par où commencer ?

D'abord identifier la classe qui va être enrichi. Dans notre cas cela sera la classe Marker que nous allons spécialiser en créant une nouvelle classe label. Il est très important que vous compreniez comment réaliser un héritage via la librairie [OpenLayers](http://openlayers.org/ "Site internet OpenLayers"). Pour cela il suffit de créer une nouvelle classe avec en premier argument la classe mère :

```javascript
OpenLayers.MarkerLabel = OpenLayers.Class(OpenLayers.Marker, {  
//code  
}
```

Ainsi notre nouvel classe Label héritera de toutes les propriétés et méthodes de la classe Marker. Voilà une bonne chose de faite, nous disponsons maintenant de l'ossature générale permettant de batir notre nouvel objet.

## Définir les propriétés et méthodes de notre classe

Il sera nécessaire dans un premier temps de lister l'ensemble des propriétés et méthodes que vous souhaitait affecter à votre classe. Cela sera par exemple (dans notre cas) le contenu qui sera affiché dans le tooltips, sa couleur de fond, la couleur du texte...

Partant de là, il ne vous reste plus qu'a construire votre nouvelle classe, cela se passe de la manière suivante :

```javascript
OpenLayers.MarkerLabel = OpenLayers.Class(OpenLayers.Marker, {

  fontColor: "black",

  bckColor: "none",

  opacity: "1",

  // Constructeur  
  initialize: function(lonlat, icon, label, options) {  
    //code  
  }

  destroy: function() {  
    //code  
  },

  draw: function(px) {  
    //code  
  },

  onmouseover: function (evt) {  
    //code  
  },

  onmouseout: function (evt) {  
    //code  
  },

  setLabel: function (label) {  
    //code  
  },

  setLabelVisibility: function (visibility) {  
    //code  
  },

  getTextSize: function(labelSize) {  
    //code  
  },

  getLabelVisibility: function () {  
    //code  
  },

  CLASS_NAME: "OpenLayers.MarkerLabel"  
});
```

Une méthode particulière vous interpelle peut être ? Oui en effet, qu'est ce donc que cet initialize ? En fait il joue le rôle de constructeur (encore un héritage de). [C'est lui qui va être exécuté lorsque l'on créera un nouvel objet.](http://www.prototypejs.org "site internet prototype")

## Le constructeur : initialize

Comme nous l'avons vu précédemment c'est la méthode prototype qui joue le rôle de constructeur. Dans notre cas elle se présentera de la manière suivante :

```javascript
initialize: function(lonlat, icon, label, options) {  
  var newArguments = [];  
  "Clonage" des éléments  
  OpenLayers.Util.extend(this, options);  
  newArguments.push(lonlat, icon, label);  
  // Utilisation du constructeur de la classe mère  
  OpenLayers.Marker.prototype.initialize.apply(this, newArguments);  
  this.label = label;  
  // Div properties  
  this.labelDiv = OpenLayers.Util.createDiv(this.icon.id + "_Text", null, null);  
  this.labelDiv.className = this.labelClass;  
  this.labelDiv.innerHTML = label;  
  this.labelDiv.style.marginTop = this.labelOffset;  
  // Div Color Text, Background Color and Opacity  
  this.labelDiv.style.backgroundColor= this.bckColor;  
  this.labelDiv.style.color= this.fontColor;  
  this.labelDiv.style.filter="alpha(opacity="+this.opacity*100+")";  
  this.labelDiv.style.opacity=this.opacity;  
  // Div Position  
  this.labelDiv.style.padding = "1px 4px 1px 4px";  
  this.labelDiv.style.textAlign = "center";  
  this.labelDiv.style.position = "Inherit";  
  this.labelDiv.style.top = this.marginTop;  
  this.labelDiv.style.left = this.marginLeft;  
}
```

Il ne vous reste plus qu'a rajouter les divers attributs et méthodes que vous souhaitez implémenter. Vous remarquerez le mot clé *this* dans le constructeur qui référence l'objet en cours. Et voilà vous disposez de tous les outils pour étendre et améliorer votre librairie cartographique préférée.

----

<!-- geotribu:authors-block -->
