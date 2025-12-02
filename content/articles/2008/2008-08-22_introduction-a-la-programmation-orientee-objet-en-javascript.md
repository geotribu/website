---
title: "Introduction à la programmation orientée objet en JavaScript"
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-08-22
description: "Introduction à la programmation orientée objet en JavaScript"
tags:
    - JavaScript
    - programmation objet
---

# Introduction à la programmation orientée objet en JavaScript

:calendar: Date de publication initiale : 22 août 2008

## Introduction

Ce tutorial n'a pas vocation à être une bible du JavaScript (JS), mais les librairies cartographiques (OpenLayers, GoogleMap...) utilisent de plus en plus ce langage. Il est donc important d'en comprendre les fondements afin de pouvoir lire, utiliser et appliquer les API disponibles. Et si vous désirez passer un jour à l'étape supérieure qu'est l'enrichissement de l'API par vos propres fonctions il sera nécessaire que vous maitrisiez certains aspects particuliers de la programmation orientée en JS.

JavaScript est un langage basé sur une notion de prototype par opposition à un langage basé sur des classes et sous-classes pour réaliser un héritage. Un prototype est un objet à partir duquel de nouveaux objets sont créés par clonage. Pour les personnes habituées au système de classes et d'instances (Delphi, C++, Java, C#...) cette notion peut paraitre déroutante. En réalité ce n'est qu'une habitude à prendre, une autre manière de programmer.

## Créer un nouvel objet

Il existe deux manières de créer un objet en JavaScript :

```javascript
var obj1 = new object(); // A partir de la notion d'objet
// ou
var obj2 = {}; // A partir de la notation JSON
```

JavaScript considère les objets en tant que tableau associatif.

## Mise en pratique

N'importe quel objet primitif de JavaScript peut être étendu. Nous nous intéresserons pour notre exemple à l'objet string et à l'objet array.

Dans notre premier exemple nous étendrons l'objet string par une méthode permettant de vérifier si la fin de deux chaines de caractères correspondent.
Dans notre second exemple nous étendrons l'objet array par une méthode permettant de calculer la somme des valeurs qu'il contient.

- Verification si la fin de deux chaines de caractères correspondent

```javascript
String.prototype.endsWith = function(suffix){
  /*
    verifie si la fin de deux chaines de caractères sont égales
  */
  /*
    lastIndexOf -> méthode est similaire à indexOf(), à la différence que la recherche se fait de droite à gauche :
      Retourne la position d'une sous-chaîne (lettre ou groupe de lettres) dans une chaîne de caractère
   */
  return this.length - suffix.length==this.indexOf(suffix);
};
```

Exemple :

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://geotribu.net/applications/tutoriaux/tuto_js/objetString_lastIndexOf.htm" width="100%" height="250px"></iframe>`

- Calcul de la somme des valeurs d'un tableau

```javascript
Array.prototype.sum = function(){
  /*
    fait la somme des valeurs d'un tableau
    et verifie que la valeur est bien un nombre
     Number() convertit un string en number

  */
  sum =0;
  for(var x=0; arraySum.length>x; ++x){
    if (!isNaN(Number(this[x]))){
      sum = Number(this[x]) + sum;
    }
  }
  return sum;
};
```

Exemple :

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://geotribu.net/applications/tutoriaux/tuto_js/objetArray_lsumValue.htm" width="100%" height="250px"></iframe>`

## Tableau récapitulatif

| Concept | Support par JavaScript |
| :------ | :------------ |
| Classe | Support partiel, aucun élément élément de langage dédié. Mais possibilité d'utilisation via les fonctions/closures/prototype |
| Composition/agrégation | Ces deux mécanismes sont supportés |
| Encapsulation/visibilité | Aucun support |
| Héritage | JS permet de faire de l'héritage mais il n'existe pas de mot-clé extends prévu à cet effet. L'héritage est une recopie compléte des méthodes et attributs |
| Mot-clé super | Non supporté |
| Mot-clé this | This est supporté il fait référence à l'objet en cours sur lequel la methode s'applique |
| Polymorphisme | Concept non supporté |
| Typage | JS possédant un typage dynamique, le type d'un objet n'est connu que lors de son exécution et peut varier au cours de celle-ci. |

## Conclusion

A l'heure actuelle la notion d'orienté objet n'est en réalité qu'une émulation. En effet, il n'existe presque aucun support (extends, super...) ni aucune logique (pas de réel concept de classe) permettant de mettre en oeuvre ce paradigme.

Néanmoins, plusieurs techniques (astuces?) permettent d'y arriver. Pourquoi alors essayer d'utiliser ce langage pour quelque chose pour lequel il n'a pas été prévu? A cette question je n'ai malheureusement aucune réponse claire (vos idées sont les bienvenues).

Néanmoins 'avantage indéniable de JS est sa fléxibilité (ex changement en cours d'exécution la structure des classes) ainsi que sa modularité qui en découle. De plus, on peut estimer qu'il a acquis une certaine robustesse (rigeur de codage des développeurs ?) au vu des librairies qui sont aujourd'hui disponibles telles que : Prototype, YUI, script.aculo.us, GoogleMap, OpenLayers...

----

<!-- geotribu:authors-block -->
