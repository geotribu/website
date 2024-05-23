---
title: Réaliser un héritage en JavaScript
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-08-30
description: Réaliser un héritage en JavaScript
tags:
    - heritage
    - JavaScript
---

# Réaliser un héritage en JavaScript

:calendar: Date de publication initiale : 30 août 2008

## Introduction

La Programmation Orientée Objet (POO) offre l'avantage indéniable de fournir un code modulaire. En effet, celle-ci se base sur deux concepts que sont **les niveaux de visibilité** et **l'héritage**.

Les niveau de visibilité sont un peu des moyens de protections pour sécuriser les classes. Il en existe quatre :

- Default : Seuls les entités de la classe et et les classes filles accèdent aux éléments de la classe
- Public : Toutes les entités externes accèdent aux éléments de la classe
- Private : Seuls les entités de la classe accèdent aux éléments de la classe
- Protected : Seuls les classes filles accèdent aux éléments de la classe

Une fois ces barrières misent en place, on peut maintenant faire communiquer les classes entres elles. Cela se passe grâce à la notion d'héritage. Celle-ci permet, en se basant sur le niveau de visibilité, de faire hériter une classe fille de tous les attributs et méthodes d'une classe mère. Nous traiterons dans ce tutoriel uniquement des héritages unilatéraux en sachant bien sûr qu'il existe des cas plus complexes telles que : les Classes et méthodes abstraites/finales, les héritages multiples, les concepts d'agrégation et de composition...

Prenons un exemple concret :

Nous utiliserons ici un point de vue géographique en se basant sur l'[API d'OpenLayers](http://dev.openlayers.org/releases/OpenLayers-2.6/doc/apidocs/files/OpenLayers/Layer-js.html "API OpenLayers") est son concept de couche. Partons donc de la Classe couche. Celle-ci est définie par un certains nombres d'attributs et méthodes comme son nom, son extension, la possibilité d'être affiché ou non... Cette Classe de base est la classe mère de laquelle vont hériter d'autres classes. Ces sous-classes sont donc forcément plus spécialisées à l'exemple de la Classe `layers.WMS` qui hérite de la classe grid qui hérite elle même de la classe `httpRequest`.

## Faire hériter une classe en JavaScript

Bon passons sur les choses douloureuses immédiatement, **il n'existe pas de mécanismes spécifique JS permettant de réaliser des héritages de classes**. Partant de là, toutes les solutions proposées (éh oui il existe plusieurs manières de faire), bien que fonctionnelles, ne sont que des enrichissements (~~rustine~~).

Il existe trois manières de faire hériter des classes en JS. La première se base sur le constructeur de la classe-mère, la seconde sur le prototype de la classe mère et la dernière est une combinaison des deux.

- Héritage par le constructeur de la classe mère

Cette première méthode consiste en fait en une recopie du constructeur de la classe mère vers une méthode de la classe fille. Ainsi, l'appel de cette méthode initialise cette dernière en se fondant sur le constructeur de la classe mère.

L'exemple ci-dessous permet de mieux comprendre les étapes :

```javascript
function classeMere() {  
  this.attribut = attribut1;  
}
classeMere.prototype.methodeA() = function() {  
// code  
}
classeMere.prototype.methodeB() = function() {  
// code  
}

function classeFilleExtendsMere() {  
  classeMere.call(this); // Héritage  
  /* ***************  
  Correspond à :  
  this.parent = classeMere; // Héritage  
  this.parent();  
  *************** */  
}
```

Cette méthode souffre d'un handicap. En effet, si les méthodes de la classe mère sont définies en dehors du constructeur via l'attribut prototype, l'héritage ne peut alors se faire.

- Héritage par le prototype de la classe mère

Il existe deux manières, en se basant sur le prototype de la classe mère, de réaliser un héritage.

1. Soit en remplaçant la valeur du prototype de la classe fille par celui de la classe mère  
2. Ou alors en ajoutant les éléments de la classe mère dans celui de la classe fille

### Exemple 1 : Initialisation du prototype "fille" avec une instance de la classe mère

```javascript
function classeMere() {  
  this.attribut = attribut1;  
}

classeMere.prototype.methodeA() = function() {  
// code  
}
classeMere.prototype.methodeB() = function() {  
// code  
}
function classeFilleExtendsMere() {
}
// Tout le prototype fille est remplacé par celuin de la mère  
classeFilleExtendsMere.prototype = new classeMere();  
```

Le principal inconvénient de cette approche est que si avant la recopie du prototype de la classe mère vers la classe fille des nouvelles méthodes ont été ajoutées (à la classe fille) celles-ci sont alors écrasées. A cela s'ajoute qu'il n'est pas possible de réaliser des héritages multiples via cette méthode.

### Exemple 2 : Recopie des éléments contenus dans l'attribut prototype de la classe mère vers le prototype de la classe fille

```javascript
function classeMere() {  
  this.attribut = attribut1;  
}
classeMere.prototype.methodeA() = function() {  
// code  
}
classeMere.prototype.methodeB() = function() {  
// code  
}
function classeFilleExtendsMere() {
}
// Recopie des éléments au moyen d'une simple boucle  
for (var element in classeMere.prototype ) {  
  classeFilleExtendsMere.prototype[element] = classeMere.prototype[element]
}  
```

Par contre dans cette méthode la restriction porte sur le fait que la classe fille n'hérite pas des éléments définis dans le constructeur de la classe mère.

Chacune des deux approches ci-dessus ont leurs défauts et leurs inconvénients mais ne sont pas des solutions satisfaisantes. Nous allons donc les utiliser conjointement afin de réaliser un héritage plus réaliste.

- Combinaison des deux approches

La combinaison des deux approches précédentes donnerait le code suivant :

```javascript
// Classe mère  
function classeMere() {  

  this.attribut = attribut1;  

  if ( typeOf classeMere.initialized == "undefined" ) {  

    classeMere.prototype.methodeA() = function() {  
      // code  
    }

    classeMere.prototype.methodeB() = function() {  
      // code  
    }  
    classeMere.initialized = true ;  
  }  
}

function classeFilleExtendsMere() {  
  classeMere.call(this); // Cf Héritage par le constructeur de la classe mère  
  if ( typeOf classeFilleExtendsMere.initialized == "undefined" ) {  
    // Recopie des éléments au moyen d'une simple boucle  
    for (var element in classeMere.prototype ) {  
      classeFilleExtendsMere.prototype[element] = classeMere.prototype[element]  
    }  
    // Ajout d'une nouvelle méthode  
    classeFilleExtendsMere.prototype.methodeC = function() {  
      // code  
    }  
    classeFilleExtendsMere.initialized = true;  
  }  
}
```

Et voilà comment on peut réaliser un héritage en JavaScript... C'est dur et laborieux ! Et d'ici que vous ayez sauté quelques lignes de ce tutoriel je suis persuadé que vous vous sentez un peu perdu. N'ayez crainte [Prototype](http://www.prototypejs.org "site internet prototype") (encore lui ?? :/, nan la bibliothèque :p ), est là pour vous aider.

## Faire hériter une classe en JavaScript grace à la biblithèque prototype

L'héritage de classe via la bibliothèqe [Prototype](http://www.prototypejs.org "site internet prototype") se fait de la manière suivante : `create([superclass][, methods...]) -> Class`

Ce qui nous donnerait :

```javascript
// Classe mère  
var classeMere = Class.create({  
  this.attribut = attribut1;  
  methodeA : function() {  
    // code  
  }
  methodeB : function() {  
    // code  
  }  
});

var classeFilleExtendsMere = Class.create(classeMere, {  
  // Ajout d'une nouvelle méthode  
  methodeC : function() {  
    // code  
  }
}
// Et ça marche !  
var newObjet = new classeFilleExtendsMere()  
newObjet.methodeA();
```

Clair, propre et conçis que demander de plus ? Un point de plus encore pour cette formidable bibliothèque qu'est [Prototype](http://www.prototypejs.org "site internet prototype").

----

<!-- geotribu:authors-block -->
