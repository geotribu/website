---
title: Compiler sa propre librairie OpenLayers
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-11-02
description: Compiler sa propre librairie OpenLayers
image: ''
license: default
robots: index, follow
tags:
    - compilation
    - OpenLayers
---

# Compiler sa propre librairie OpenLayers

:calendar: Date de publication initiale : 02 novembre 2008

## Introduction

**Documentation source** : [trac.openlayers.org/wiki/Profiles](http://trac.openlayers.org/wiki/Profiles)

Généralement lorsque OpenLayers est utilisé en mode développement il est plus simple de pointer vers le script situé dans `/lib/OpenLayers.js`. Cela aura pour effet de créer, lors de l'appel client, une balise script pour chacune des classes déclarée dans ce fichier. Mais les désavantages sont évidents. En effet, le fichier étant non compressé et non optimisé cela entraine surcharge inutile de la bande passante et donc un baisse de l'interactivité pour l'utilisateur final.

C'est pourquoi afin d'optimiser l'environnement proposé, la distribution OpenLayers inclut un outil (écrit en python) permettant la création d'un fichier unique compressé contenant la totalité des classes et dont tous les commentaires ont été supprimés (jsmin library).

Cet outil utilise un fichier de configuration (profils) permettant de choisir les classes à ajouter ou supprimer du fichier final. une application directe est par exemple la suppression des classes non utilisées afin d'alléger l'application.

## Créer son profil

**OpenLayers Build Profiles** est l'outil (python) permettant de "compiler" sa propre librairie OpenLayers (situé dans `build/build.py`).

Afin de créer son profil il suffit simplement simplement, à l'intérieur du dossier build, de copier le fichier `library.cfg` ou `lite.cfg` en `maVersion.cfg`. Vous n'avez plus ensuite qu'à lancer la commande suivante : `python build.py maVersion`

Ce fichier obéit à une syntaxe rigoureuse utilisant des paramètres entre crochets comme configuration : [first], [last], [include], [exclude]

La première parti du fichier du fichier de configuration est consacrée au code devant être inclut prioritairement. Par exemple par défaut la configuration d'OpenLayers est :

- `OpenLayers/SingleFile.js`
- `OpenLayers.js`
- `OpenLayers/BaseTypes.js`
- `OpenLayers/Util.js`

Si vous souhaitez inclure des fichiers en particuliers (autres que ceux spécifiés dans le fichier `/lib/js/OpenLayers.js`) il suffit d'ajouter ces derniers après la balise [include].

Si au contraire vous souhaitez enlevez des fichiers il faudra alors spécifier ces derniers après la balise [exclude].

## Compiler son fichier

Pour créer un fichier unique et optimisé, il suffit de se rendre dans le répertoire `build` d'OpenLayers et de taper la commande suivante : `python build.py profilename` (où `profilname` correspond au nom de votre fichier de configuration).

Crééons maintenant notre propre fichier. Imaginons que nous souhaitons incorporer l'[addins ScaleBar](http://trac.openlayers.org/browser/addins/scalebar/trunk/lib/OpenLayers/Control/ScaleBar.js) directement à notre fichier unique. Cela nous évitera par la suite de le déclarer dans chacun de nos scripts. Pour cela, deux moyens sont possibles. Soit après, avoir téléchargé ce dernier dans le répertoire Control (lib/control), vous pouvez éditer le fichier lib/OpenLayers.js et rajouter le chemin d'accès vers cette nouvelle classe dans le tableau listant l'ensemble des classes.

```javascript
var jsfiles = new Array(  
  "OpenLayers/Util.js",  
  "OpenLayers/BaseTypes.js",  
  ...,  

  "OpenLayers/Control/ScaleBar.js"  
);
```

Sinon vous pouvez simplement, spécifier dans votre fichier "profil" le chemin vers cette nouvelle classe.

```ini
[include]  
OpenLayers/Control/ScaleBar.js
```

Il vous suffit ensuite de lancer la commande :

```python
python build.py OpenLayersScaleBar.js
```

Cela aura pour effet de créer un nouveau fichier OpenLayers compressé contenant la classe `ScaleBar`.

----

<!-- geotribu:authors-block -->
