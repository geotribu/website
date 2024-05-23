---
title: "Interroger GeoServer en Python grâce à gsconfig"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-08-25
description: "Interroger GeoServer en Python grâce à gsconfig"
tags:
    - GeoServer
    - open source
    - Python
    - serveur cartographique
---

# Interroger GeoServer en Python grâce à gsconfig

:calendar: Date de publication initiale : 25 août 2010

![logo Geoserver](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/geoserver.png "logo Geoserver"){: .img-thumbnail-left }

Comme vous l'avez surement remarqué, je ne suis pas un grand fan de Java. Le fait est que je trouve ce langage trop verbeux et vraiment compliqué à prendre en main. C'est pourquoi quand je suis tombé sur, [gsconfig](http://wiki.github.com/dwins/gsconfig.py/), une librairie python permettant via le protocole [REST](https://fr.wikipedia.org/wiki/Representational_State_Transfer) de dialoguer avec GeoServer, j'ai de suite été emballé.

Au cours de ce billet, nous aborderons deux sujets principaux. Tout d'abord la création d'un environnement virtuel afin de ne pas "polluer" nos dépôts sources. Ensuite l'installation et l'utilisation de gsconfig

## 1 - Jouer en toute sécurité grâce à Virtualenv

### Installation de virtualenv

L'une des (nombreuses) raisons pour laquelle j'aime python, est la liberté offerte par ce langage. Ne vous est-il jamais arrivé de vouloir utiliser une même application mais sous des versions différentes, d'installer une librairie python encore en développement pour faire des tests sans corrompre tout votre système ? Avec une architecture classique cela est impossible. Pour remédier à cela, Python offre une alternative des plus intéressantes, les environnements virtuels.

Ces derniers permettent tout simplement de disposer d'une sorte de boite virtuelle au sein de laquelle vous pouvez installer localement les librairies que vous ne souhaitez pas avoir dans votre système global. L'énorme avantage est que vous n'avez pas besoin d'installer un système complet. En effet les librairies installées dans votre système global restent utilisables localement. J'arrêterai là les explications, mais si vous souhaitez en savoir davantage, je vous renvoie vers les billets de [clemesha](http://clemesha.org/blog/2009/jul/05/modern-python-hacker-tools-virtualenv-fabric-pip/) et de l'incontournable [sgillies](http://sgillies.net/blog/1012/bootstrapping-a-python-project/)

Passons maintenant à la pratique. Il est bien évidemment nécessaire, dans un premier temps, d'installer `virtualenv`. Ubuntu faisant les choses bien, il est disponible dans les dépôts. Par Synaptic ou par un apt-get commencez par installer `python-virtualenv`. Puisque nous y sommes, installez également git-core. Cela nous servira à télécharger gsconfig qui utilise le système de version [Git](https://fr.wikipedia.org/wiki/Git).

### Création d'un environnement virtuel

Cela réalisé, il ne nous reste plus qu'à créer concrètement notre environnement virtuel. Cela se fait via un terminal, mais rassurez-vous, vous n'aurez en tout et pour tout que deux lignes à taper ! Commencez par vous placer à l'endroit où vous souhaitez créer votre nouvel environnement. Vous pouvez le faire où vous souhaitez, mais je vous conseille de créer un répertoire spécifique. En terme d'organisation cela sera tout de même plus simple. Ensuite, il vous suffit simplement de taper la ligne de commande `virtualenv` suivi du nom que vous souhaitez :

```bash
user@osgeolive:~/App/geo$ virtualenv gsconfig-virtual  
New python executable in gsconfig-virtual/bin/python  
Installing setuptools............done.  
```

Voilà votre nouvel environnement est créé mais pas encore actif. Pour cela il est nécessaire, après s'être rendu dans votre nouvel environnement, de spécifier la source de la manière suivante :

```bash
user@osgeolive:~/App/geo$ cd gsconfig-virtual/  
user@osgeolive:~/App/geo/gsconfig-virtual$ source bin/activate  
(gsconfig-virtual)user@osgeolive:~/App/geo/gsconfig-virtual$  
```

Comme vous l'avez certainement remarqué, la dernière ligne de mon terminal a changé. Elle est précédée de (`gsconfig-virtual`) signe que je suis bien maintenant dans un environnement virtuel. Nous sommes prêt maintenant à installer `gsconfig`.

## 2 -Interroger GeoServer en Python grâce à gsconfig

### Installation de gsconfig

Au sein de votre nouvel environnement virtuel, vous disposez de trois répertoires : `bin`, `include` et `lib`. Rendez-vous dans le répertoire bin et lancez la commande ci-dessous qui va télécharger `gsconfig`.

```bash
(gsconfig-virtual)user@osgeolive:~/App/geo/gsconfig-virtual/gsconfig-virtual/gsconfig-virtual/bin$ git clone <http://github.com/dwins/gsconfig.py.git>  
```

Une fois le téléchargement terminé, il ne vous reste plus qu'à installer gsconfig :

```bash
(gsconfig-virtual)user@osgeolive:~/App/geo/gsconfig-virtual/bin$ cd gsconfig.py  
(gsconfig-virtual)user@osgeolive:~/App/geo/gsconfig-virtual/bin/gsconfig.py$ python setup.py install  
```

Ma première tentative d'installation s'est soldée par un échec en raison de l'absence de la librairie `httplib2`. Rien de très grave rassurez-vous. Si c'est également votre cas, téléchargeons-la immédiatement et relançons l'installation.

```bash
(gsconfig-virtual)user@osgeolive:~/App/geo/gsconfig-virtual$ easy_install httplib2  
(gsconfig-virtual)user@osgeolive:~/App/geo/gsconfig-virtual$ cd bin/gsconfig.py  
(gsconfig-virtual)user@osgeolive:~/App/geo/gsconfig-virtual/bin/gsconfig.py$ python setup.py install  
...  
Using /home/user/App/geo/gsconfig-virtual/lib/python2.6/site-packages/httplib2-0.6.0-py2.6.egg  
Finished processing dependencies for gsconfig.py==1.0  
```

Et voilà le tour est joué, l'installation est terminée.

### Utilisation de gsconfig

Maintenant que toute notre infrastructure est en place, utilisons immédiatement `gsconfig`. Mais avant toute chose, il est nécessaire de démarrer GeoServer. En effet, gsconfig va dialoguer avec notre serveur cartographique via le protocole Rest. Une fois cela réalisé, il suffit dans votre environnement virtuel de lancer un interpréteur python. Nous allons ensuite importer la librairie et effectuer quelques tests :

```python
>>> from geoserver.catalog import Catalog  
>>> cat = Catalog("http://localhost:8082/geoserver/rest")  
>>> cat.get_layers()  
[Layer[giant_polygon], Layer[poi], Layer[poly_landmarks], Layer[tiger_roads], Layer[Pk50095], Layer[Img_Sample], Layer[mosaic], Layer[Arc_Sample], Layer[tasmania_cities], Layer[tasmania_roads], Layer[tasmania_water_bodies], Layer[tasmania_state_boundaries], Layer[states], Layer[sfdem], Layer[bugsites], Layer[restricted], Layer[archsites], Layer[roads], Layer[streams]]  
```

Imaginons que nous souhaitons en connaitre davantage à propos de la couche states :

```python
>>> states = cat.get_layer('states')  
>>> states.href  
'http://localhost:8082/geoserver/rest/layers/states.xml'  
>>> states.name  
'states'  
>>> states.styles  
[Style[polygon], Style[pophatch]]  
```

De la même manière si nous souhaitons connaitre les workspaces disponibles :

```python
>>> cat.get_workspaces()  
[it.geosolutions @ <http://localhost:8082/geoserver/rest/workspaces/it.geosolutions.xml>, cite @ <http://localhost:8082/geoserver/rest/workspaces/cite.xml>, tiger @ <http://localhost:8082/geoserver/rest/workspaces/tiger.xml>, sde @ <http://localhost:8082/geoserver/rest/workspaces/sde.xml>, topp @ <http://localhost:8082/geoserver/rest/workspaces/topp.xml>, sf @ <http://localhost:8082/geoserver/rest/workspaces/sf.xml>, nurc @ <http://localhost:8082/geoserver/rest/workspaces/nurc.xml>]  
```

L'installation ainsi que la prise en main de `gsconfig` sont réellement très rapides. Quel plaisir de pouvoir s'amuser avec geoserver tout en utilisant python ! Mais bon, c'est décidé cette année je me mets au java...

----

<!-- geotribu:authors-block -->
