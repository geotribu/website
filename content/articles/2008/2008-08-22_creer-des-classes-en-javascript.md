---
title: "Créer des classes en JavaScript"
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-08-22
description: "Créer des classes en JavaScript"
tags:
    - classe
    - JavaScript
---

# Créer des classes en JavaScript

:calendar: Date de publication initiale : 22 août 2008

## Introduction

Comme nous l'avons vu dans le tutoriel précédent, JavaScript (JS) n'offre qu'un support partiel (limité?) des concepts liés à la programmation orientée objet (POO). Le concept de classe en tant que telle (pas de mot-clé class dédié) n'existe pas. Toute la POO en JavaScript se base uniquement sur les mécanismes de fonctions, closures et prototype. En même temps que nous apprendrons à créer manuellement nos classes nous utiliserons la bibliothèque Prototype qui offre des mécanismes et raccourcis très intéressants quant à l'utilisation du JavaScript Orienté Objet.

## Créer sa propre classe

- **le mot clé this**

Le mot clé this fait référence à l'objet en cours. De ce fait il est possible d'avoir accès à tous les attributs et méthodes de l'objet dans le code d'une fonction.

- **L'attribut prototype**

Prototype est un attribut particulier que possèdent toutes les classes JS. Il est utilisé lors de l'instanciation de l'objet pour définir un modèle structurel (tiens tiens ne se rapproche t'on pas de la définition d'une classe)? Il permet en effet de définir tous les attributs et méthodes de toutes les instances de la classe.

- **Création d'une classe**

Ça y'est, on passe aux choses sérieuses et l'on met les mains dans le cambouis. Mais à peine commencé les choses se gâtent, en effet mauvaise nouvelle, il n'existe pas qu'une manière de créer des classes (pseudo-classes?) en JS.

Pour faire simple, il est tout à fait possible de définir des classes en se basant uniquement sur le concept des fonctions, mais, dans ce cas, le code de chaque méthode serait dupliqué à chaque instanciation d'un nouvel objet alourdissant d'autant la place réservée en mémoire.

```javascript
function maClasse() {
 this.attribut1;
 this.attribut2;
 this.methodeA = function() {
    // code
 }
 this.methodeB = function() {
    // code
 }
}
```

Comment faire alors? Mais oui bien sur, en se basant sur l'objet prototype. En effet, la technique consiste à créer une classe de base. Ensuite celle-ci est enrichie grâce au prototype ce qui permet de ne charger en mémoire qu'une seule partie de l'objet. En se basant sur le schéma précédent cela donnerait :

```javascript
function maClasse() {
 this.attribut1;
 this.attribut2;
}

maClasse.prototype.methodeA() = function() {
  // code
}

maClasse.prototype.methodeB() = function() {
  // code
}
```

L'inconvénient de cette procédure est que les méthodes ne sont pas définies dans le constructeur lui même. Il est néanmoins possible de contourner cette restriction en se basant sur la propriété "initialized" du constructeur Ce qui donne :

```javascript
function maClasse() {
 this.attribut1;
 this.attribut2;
 if (typeOf maClasse.initialized == "undefined" ) {
  maClasse.prototype.methodeA() = function() {
   // code
  }

  maClasse.prototype.methodeB() = function() {
   // code
  }
  maClasse.initialized = true;
 }
}
```

## Créer sa propre classe avec la bibliothèque Prototype

Merci à Sam Stephenson pour le développement du framework Prototype. En effet vous verrez au travers des quelques lignes qui vont suivre que l'écriture de classe grâce à cette bibliothèque devient plus facile et logique. D'ailleurs de nombreuses autres librairies utilisent à la base Prototype

Allé hop, vérifions si je ne vous ai pas menti. Comment faire pour créer une classe via prototype ? Suivez le guide :

```javascript
var maClasse = Class.create();

maClasse.prototype =  {
 initialize : function() {
  this.attribut1;
  this.attribut2;
 }
 methodeA : function() {
  //code
 }
 methodeB : function {
  //code
 }
}
```

Dans la bibliothèque prototype initialize joue le rôle de constructeur. Jusqu'ici vous me direz que l'avantage entre la bibliothèque prototype et la manière classique via l'objet prototype (on finit par en perdre son latin) n'est pas flagrant. Mais vous verrez que les avantages sont indéniables lorsque l'on passera aux concepts d'héritage et visibilité.

----

<!-- geotribu:authors-block -->
