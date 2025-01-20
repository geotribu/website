---
title: "Compiler OpenLayers 3"
authors:
    - Arnaud VANDECASTEELE
categories:
    - article
comments: true
date: 2013-05-21
description: "Compiler OpenLayers 3"
tags:
    - OpenLayers
---

# Comment compiler OpenLayers 3

:calendar: Date de publication initiale : 21 mai 2013

[OpenLayers](https://openlayers.org/) 3 s'annonce comme étant la bibliothèque Javascript Open Source la plus avancée dans le domaine de la cartographie. De nombreuses fonctionnalités seront présentes comme des moteurs de rendu aux capacités améliorées (grace a WebGL), mais aussi l'intégration d'environnement 3D avec Cesium.

Pour un avant goût de ses potentialités, le mieux est de consulter les [différents exemples](http://ol3js.org/ol3/master/examples/) ou encore de tester la bibliothèque en ajoutant le lien internet vers le fichier Javascript. C'est cette dernière méthode que j'utilisais habituellement. Mais, récemment quelques soucis de connexions m'ont poussé à télécharger les sources pour l'utiliser en local. Rien de bien méchant me direz-vous, pas la peine d'en faire un billet de blog !

En réalité, c'est un plus compliqué car afin d'optimiser le code, l’équipe en charge du projet a décidé d'utiliser les outils fournis par Google Closure. Il est donc nécessaire dorénavant de compiler cette libraire. Compiler du Javascript ? Oui, c'est bien le cas. Je vous livre ici mon expérience qui sans être compliquée ne fût pas pour autant triviale.

## Compiler OpenLayers 3

Avant de commencer, il est nécessaire de préciser que j'utilise [Ubuntu](http://www.ubuntu.com/). Les commandes qui sont donc présentées peuvent varier en fonction de votre distribution.

Première étape, bien lire le [guide du développeur](https://github.com/openlayers/ol3/wiki/Developer-Guide) disponible sur GitHub. Comme vous pouvez le constater, vous aurez besoin de certains prérequis comme notamment disposer de l’utilitaire Git, d'avoir les langages Python et Java d'installés, mais aussi bien évidemment de Google Closure. Oui, je sais, cela fait tout de même beaucoup pour au final travailler en JavaScript...

Cela peu paraître bizarre, mais pour que la compilation fonctionne il ne faut pas télécharger l'archive de la bibliothèque mais cloner le dépôt Git. Sans cela vous obtenez une erreur à la compilation du fait que votre dossier n'est pas reconnu comme un projet Git. Il y a peut-être un moyen d’éviter cela mais je ne l'ai pas trouvé. Donc, clonons le dépôt:

```bash
git clone https://github.com/openlayers/ol3.git
```

Maintenant, installons les différents outils nécessaires. Tout d'abord, commençons par Google Closure. Un simple `easy_install` a suffi pour télécharger la bibliothèque et à l'ajouter à mon [path système](http://www.commentcamarche.net/faq/3585-bash-la-variable-d-environnement-path). Aucune difficulté particulière.

```bash
sudo easy_install http://closure-linter.googlecode.com/files/closure_linter-latest.tar.gz
```

Maintenant que nous avons les outils nécessaires, nous pouvons passer à la compilation de la bibliothèque elle-même. Cela se fait par l’intermédiaire du script python `build.py` auquel vous devez ajouter un argument précisant l’opération à effectuer. Les arguments possibles sont notamment : `serve`, `lint`, `build`, test ou encore `check`. Dans notre cas, c'est build qui nous intéresse. Une fois la commande lancée vous devriez obtenir le résultat suivant:

```bash
./build.py build
2013-05-17 12:42:54,063 build/ol.js: java -jar build/plovr-eba786b34df9.jar build buildcfg/ol.json
0 error(s), 0 warning(s), 95.29% typed
2013-05-17 12:43:08,939 build/ol.js: uncompressed: 219009 bytes
2013-05-17 12:43:08,961 build/ol.js:   compressed: 70725 bytes
2013-05-17 12:43:08,974 build/ol-simple.js: java -jar build/plovr-eba786b34df9.jar build buildcfg/ol-simple.json
0 error(s), 0 warning(s), 95.24% typed
2013-05-17 12:43:18,514 build/ol-simple.js: uncompressed: 733865 bytes
2013-05-17 12:43:18,564 build/ol-simple.js:   compressed: 151608 bytes
2013-05-17 12:43:18,565 build/ol-whitespace.js: java -jar build/plovr-eba786b34df9.jar build buildcfg/ol-whitespace.json
0 error(s), 0 warning(s)
2013-05-17 12:43:22,312 build/ol-whitespace.js: uncompressed: 1472903 bytes
2013-05-17 12:43:22,441 build/ol-whitespace.js: compressed: 237490 bytes
```

Si c'est le cas, deux nouveaux fichiers (`ol.css` et `ol.js`) ont alors été générés dans le répertoire build. Vous pouvez à présent intégrer OpenLayers 3 en local. Mais qu'en est-il pour la documentation?

## Compiler la documentation d'OpenLayers 3

Bon après avoir compilé notre librairie, la documentation ne devrait pas poser de souci. Les développeurs ont fait le choix d'utiliser [JSDoc](https://github.com/jsdoc3/jsdoc). Il vous faudra donc la télécharger via GitHub

```bash
git clone git://github.com/jsdoc3/jsdoc.git
```

Ensuite, il faut ajouter le lien de l'utilitaire dans votre path système:

```bash
export PATH=$PATH:/path_to/jsdoc
```

La commande ci-dessus ne permettra d'ajouter `jsdoc` que le temps de votre session bash. Si vous souhaitez que cela soit permanent, le plus simple est de modifier votre fichier `.bashrc`.

Passons maintenant a la compilation de la documentation. Cela se fait toujours avec le script `build.py` mais en ajoutant doc comme paramètre:

```bash
./build.py apidoc
2013-05-17 12:54:11,732 host-resources: rm -rf build/gh-pages/master/resources
2013-05-17 12:54:11,733 host-resources: cp -r resources build/gh-pages/master/resources
2013-05-17 12:54:11,742 build/jsdoc-master-timestamp: jsdoc -c doc/conf.json src doc/index.md -d build/gh-pages/master/apidoc
```

À la fin, dans le dossier build, le répertoire `gh-page` contenant la documentation sera ajouté. Et voilà, nous avons donc tout le nécessaire pour utiliser et développer avec OpenLayers 3. C'est maintenant à votre tour de jouer !

----

<!-- geotribu:authors-block -->
