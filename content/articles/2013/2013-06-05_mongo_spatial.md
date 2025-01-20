---
title: Mongo Spatial
authors:
    - Guillaume De Boyer
categories:
    - article
comments: true
date: 2013-06-05
description: Mongo Spatial
tags:
    - Mongo
    - Node.js
---

# Mongo Spatial

!!! warning
    Ce contenu est une archive. Son contenu n'est sûrement plus très frais...

Tuto GeoTribu d'introduction à MongoDB pour l'information spatiale. Nécessite de légère base de [Javascript](http://fr.openclassrooms.com/informatique/cours/dynamisez-vos-sites-web-avec-javascript), rien de sorcier.

Je recommande vivement l'utilisation de l'excellent editeur de code open source [Brackets](http://brackets.io/).

## Introduction

Le but de ce tutorial est de découvrir via un exemple simple comment assembler une architecture de données spatiales avec mongodb, puis dans un second tutoriel, en y ajoutant node.js.

Mongo et node sont deux technologies qui font beaucoup parler d'elles. Beaucoup s'y opposent arguant que [javascript est une abération](http://sametmax.com/un-gros-troll-de-plus-sur-javacscript/), spécialement côté serveur. Revenir aussi sur 40 ans de maturation de SQL, simplement par effet de mode, serait pour certains une perte de temps. Ça se défend. De mon point de vue, je prends mon pieds avec ces outils et en participant au bouillaunement qui les entoure, notamment dans le domaine de la carto. Ça innove de partout. Malgrès quelques contraintes, Javascript apporte aussi une forme de simplicité et d'accessibilité. Si vous ne vous y êtes pas encore mis, les compétances que vous développerez en vous plongeant dans mongo et node vous serviront par la suite à mieux appréhender [D3.js](http://d3js.org/) et pourquoi pas [Three.js](http://threejs.org/). La dynamique autour de javascript ne semble pas ralentir, bien au contraire.

## Installation

Je ne vais pas m'étendre ici, pour node, rendez vous simplement sur [nodejs.org](http://nodejs.org/ "nodejs.org") et sélectionner votre OS. Si vous utilisez Ubuntu, vous pouvez ouvrir un terminal et entrer:

```sh
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:chris-lea/node.js
sudo apt-get update
sudo apt-get install nodejs
```

Vous pouvez ensuite lancer un `node --version` pour vérifier que l'instalation s'est bien passée.

Pour MongoDB, c'est la même chose, vous n'avez qu'à suivre le [Guide d'installation](http://docs.mongodb.org/manual/installation/ "docs.mongodb.org/manual/installation/")

## Configurer Mongo

Si vous avez suivi le guide mongo, votre serveur de base de données devrait être actif. Si la commande `mongo` retourne `Error: couldn't connect to server 127.0.0.1:27017`... c'est qu'il ne l'est pas. Rien de plus simple:

```sh
mongod  # pour lancer mongodb
mongod --repair # parfois utile après avoir fermé malencontreusement mongod...
```

La première chose à faire est de créer une base de données. C'est extrèment simple. Toujours dans le terminal, lancer la commande `mongo` pour ouvrir une connection à la base de données par defaut "test":

```sh
mongo
MongoDB shell version: 2.4.9 // Ceci est le résultat de la commande mongo.
connecting to: test
>
```

Vous remarquerez que le curseur a changé. A partir de maintenant, mongo n'acceptera plus que du javascript, mais extrêmement simple.  
Commençons par créer une base de données:

```sh
use surfdb
switched to db surfdb // Ceci est le résultat de la commande use [dbname].
>
```

Fermer la connection en pressant `Ctrl + C`.

La base de données est prête.

----

## Insertion de données spatiales

Passons à l'étape de l'insertion des données. De base, mongodb propose un outil pour importer les formats JSON, CSV or TSV. Même s'il gère une sorte de GEOJSON, l'objet [FeatureCollection](http://geojson.org/geojson-spec.html#feature-collection-objects) pose encore problème. Rien de grâve car il suffit juste d'extrère l'array `features`:

Au lieu d'utiliser ça:

```json
{
  "type": "FeatureCollection",
  "features":
  [
    {
      "type": "Feature", "id": 0, "properties": {
        "Name": "Queensie Mini", "Lat": -33.7857729, "Long": 151.2899673
      }, "geometry": {
        "type": "Point",
        "coordinates": [ 151.2899673, -33.785772899999586 ]
      }
    }
  ]
}
```

Utiliser ceci:

```json
    [
      {
        "type": "Feature", "id": 0, "properties": {
          "Name": "Queensie Mini", "Lat": -33.7857729, "Long": 151.2899673
        }, "geometry": {
          "type": "Point",
          "coordinates": [ 151.2899673, -33.785772899999586 ]
        }
      }
    ]
```

Nos données étant au bon format, passons à la commande `mongoimport`. Par defaut cette commande se connecte au serveur local, ce qui réduit dans notre cas le nombre d'arguments à passer :

```bash
mongoimport -d surfdb -c spot --type json --jsonArray --file data.json
```

Si tout ce passe bien, vous devriez voir ça:

```sh
connected to: 127.0.0.1
Fri Apr  4 00:13:22.965 check 9 32
Fri Apr  4 00:13:24.326 imported 32 objects
```

En ouvrant une connexion au serveur avec la commande `mongo`, nous pouvons maintenant accéder à nos données:

```sh
mongo
> use surfdb
show collections; // affiche les collections dans la base.
db.spot.stats(); // retourne les stats de la collection spot, type {Object}.
db.spot.findOne(); // retourne un document de la collection, type {Object}.
db.spot.find(); // retourne tous les documents de la collection, type [Array].
db.spot.find({'properties.Name':'Winki'}) // retourne tous les documents qui ont comme proprieté "properties.Name" = "Winki".
```

C'est aussi simple que ça !

C'est certes simple, mais à part stocker un pseudo geojson, ça ne sert pas à grand chose. Pour "activer" la fonction spatiale, mongo a besoin d'un index spacial. Toujours dans le terminal, serveur demarré [`mongod`] et connexion active [`mongo`]...

```sh
> db.spot.ensureIndex({'geometry':'2dsphere'}); // Explicite non ?
```

C'est prêt :).

----

<!-- geotribu:authors-block -->
