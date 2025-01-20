---
title: "GeoScript"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-04-23
description: "GeoScript"
tags:
    - API
    - GeoScript
---

# GeoScript

:calendar: Date de publication initiale : 23 avril 2010

![icône globe](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "icône globe"){: .img-thumbnail-left }

[GeoScript](http://geoscript.org/) a pour objectif de faciliter les manipulations géographiques dans des environnements de script. L'objectif est le support de 4 langages : Javascript, Python, Scala et Groovy. Cette bibliothèque permet de manipuler facilement des objets géométriques - création et manipulation d'objets ainsi que la création et manipulation de projections.  
GeoScript est fondé sur la librairie Java [GeoTools](http://geotools.org/).  

Pour le moment, seules les versions Javascript et Groovy sont disponibles :

- Javascript : [version 0.8](http://geoscript.org/js/download.html)
- Python : à venir
- Scala : à venir
- Groovy : [version 0.6](http://geoscript.org/groovy/download.html)

## Scala et Groovy - et non, ce n'est pas le nom d'un groupe de punk

Vous connaissez tous Javascript et Python, mais Scala et Groovy, qu'est-ce que c'est encore que ces nouveaux trucs ?  
Et bien c'est pas si nouveau que ça : 2003 pour Scala et 2007 pour Groovy.  
Scala et Groovy sont deux langages pour la [JVM](https://fr.wikipedia.org/wiki/Machine_virtuelle_Java), prévu pour être compilés en bytecode Java et exécutés sur la JVM.

### Scala

Quelques liens :

- <http://www.scala-lang.org/>
- <http://www.scala-fr.org/>
- [https://fr.wikipedia.org/wiki/Scala_%28langage%29](https://fr.wikipedia.org/wiki/Scala_%28langage%29)
- <http://daily-scala.blogspot.com/2010/03/geoscriptscala.html>
- <http://blog.xebia.fr/2008/03/21/introduction-a-scala/>

### Groovy

Quelques liens :

- <http://groovy.codehaus.org/>
- <http://ericreboisson.developpez.com/tutoriel/java/groovy/>
- <http://torrefacteurjava.free.fr/?q=content/groovy-par-la-pratique>

## Travaillons avec Javascript, c'est plus prudent :)

Pour la suite de ce billet, nous utiliserons donc la version Javascript de GeoScript.  
Bon, c'est du Javascript côté serveur et non côté navigateur dont nous parlons ici - d'ailleurs en passant, Javascript a été créé d'abord pour une utilisation côté serveur. En effet, GeoScript - en mode Javascript - est édité pour la plateforme [Narwhal](http://narwhaljs.org/).  
Pourquoi donc utiliser JavaScript côté serveur me direz-vous ? Et bien, depuis que les éditeurs de butineurs s'efforcent à optimiser les moteurs Javascript, ces derniers rivalisent désormais en performance avec les langages typés serveur. De plus, pour des applications Web, avoir le même langage côté client et côté serveur permet de ne pas se disperser [[http://www.clochix.net](http://www.clochix.net/post/2009/10/04/JavaScript-:-retour-sur-le-serveur)]. Dans ce mode de fonctionnement nommé Server-side JavaScript ([SSJS](https://en.wikipedia.org/wiki/Server-side_JavaScript)) il est bien évidemment nécessaire de disposer d'un serveur compatible, une grande partie d'entre eux sont [listés](https://en.wikipedia.org/wiki/Server-side_JavaScript#Server-side_JavaScript_use) sur la page de Wikipédia.

## Installation de Narwhal

Narwhal est une suite d'outils et de librairies permettant l'exécution d'applications JS côté serveur en suivant les spécifications du [CommonJS](http://commonjs.org/) et permettant ainsi d'utiliser le moteur Javascript de notre choix - [Rhino](http://www.mozilla.org/rhino/), [v8](http://code.google.com/p/v8/), [SpiderMonkey](http://www.mozilla.org/js/spidermonkey/), [TraceMonkey](https://wiki.mozilla.org/JavaScript:TraceMonkey), etc.  

Tout d'abord il faut télécharger Narwhal via [Git](http://git-scm.com/) (système de contrôle de révision) qu'il faudra préalablement installer aussi - comme d'habitude nous utiliserons Ubuntu pour l'exemple :  

```bash
~$ sudo apt-get install git-core  
~$ git clone git://github.com/280north/narwhal.git
```

Voilà, nous avons maintenant Narwhal sur notre serveur. Vous pouvez déplacer le répertoire ainsi créé où vous voulez.  

Et ajoutons Narwhal dans notre PATH - pour cela éditer le fichier `.bashrc` et ajouter la ligne suivante :  

```bash
export PATH=$PATH:~/narwhal/bin  
```

Ou sinon tapez simplement cette commande dans un terminal, et le PATH ne sera modifié que pour la durée de la session. La modification du fichier `.bashrc` permet de ne pas avoir à saisir cette commande à chaque redémarrage.  
Par défaut Narwhal est livré avec le moteur Rhino. Celui-ci est codé en Java, il faut donc avoir la JRE installée :  

```bash
~$ sudo apt-get install sun-java6-jre  
```

Testons maintenant l'installation de Narwhal :  

```bash
~$ js narwhal/examples/hello  
```

Nous devrions avoir comme réponse :  

`Hello, World!`

Note : nous pouvons utiliser la commande 'js' ou 'narwhal', c'est identique :  

```bash
~$ narwhal narwhal/examples/hello  
```

## GeoScript ... enfin !

Maintenant que nous avons installé tout ce qu'il fallait pour être opérationnel, nous pouvons tester enfin GeoScript.  
Pour cela, télécharger le `.zip` de la version JavaScript ou utiliser encore une fois Git :  

```bash
~$ sudo git clone git://github.com/tschaub/geoscript-js.git  
```

Nous avons donc un répertoire `geoscript-js` à l'endroit où vous avez lancé la commande git.  
Il faut maintenant activer notre environnement de façon à ce que Narwhal puisse charger les modules présents dans GeoScript :  

```bash
~$ ~geoscript-js/bin/sea
```

### Jouons un peu maintenant

Nous pouvons dorénavant lancer une console Javascript (commande `js` ou `narwhal`) et utiliser la bibliothèque :  

```bash
~$ js  
js> var geom = require('geoscript/geom')  
js> var p1 = new geom.Point([0, 0])  
js> var p2 = new geom.Point([10, 20])  
js> p1.distance(p2)  
22.360679774997898  
js> var poly = p2.buffer(23)  
js> poly.contains(p1)  
true  
js> quit()  
```

Ici, nous avons créé 2 points, calculé la distance entre eux, créé un polygone grâce à la fonction buffer et demandé si le premier point était contenu dans le polygone.  
Voilà, nous pouvons maintenant lire l'[API](http://geoscript.org/js/api/index.html) afin d'exploiter tous les modules :

- [geom module](http://geoscript.org/js/api/geom.html)
- [feature module](http://geoscript.org/js/api/feature.html)
- [filter module](http://geoscript.org/js/api/filter.html)
- [proj module](http://geoscript.org/js/api/proj.html)
- [layer module](http://geoscript.org/js/api/layer.html)
- [workspace module](http://geoscript.org/js/api/workspace.html)

Il faut garder à l'esprit qu'il s'agit ici de la version 0.8 et donc que l'API est susceptible d'être modifiée.

### Pour la suite

Dans un prochain billet, nous verrons comment lier GeoScript et Narwhal avec un serveur Web grâce à [Jack](http://jackjs.org/).

----

<!-- geotribu:authors-block -->
