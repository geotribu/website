---
title: Mise en place et utilisation d'un serveur BAN/BANO pour un usage personnalisé sous Ubuntu 14.04
authors:
    - Thomas Gratier
categories:
    - article
comments: true
date: 2015-06-04
description: Tutoriel d'installation et de déploiement d'addok, le servur de géocodage lié à la BAN/BANO.
license: default
robots: index, follow
tags:
    - addok
    - adresse
    - API
    - BAN
    - BANO
    - géocodage
---

# Mise en place et utilisation d'un serveur BAN/BANO pour un usage personnalisé sous Ubuntu 14.04

:calendar: Date de publication initiale : 4 juin 2015

## Introduction

![logo BAN](https://cdn.geotribu.fr/img/logos-icones/divers/ban.png "logo BAN"){: .img-thumbnail-left }

Le but est de rappeler ce qu'est le géocodage. A quoi généralement, cela sert.

Dans un deuxième temps, nous introduisons la Base Adresse Nationale (BAN) et la Base Adresse Nationale Ouverte (BANO, historique). En effet, dans ce contexte, des outils pour géocoder ont été mis en oeuvre. Nous expliquerons comment les utiliser, comment installer un serveur pour géocoder chez vous si par exemple, vous avez des besoins de géocodage massif ou de personnaliser la recherche d'adresse avec vos critères lors du géocodage.

Enfin, nous verrons comment consommer les informations venant du géocodeur en voyant les principaux outils pour cela. Nous avons fait le choix dans certains cas de référencer plutôt que de simplement copier/coller les ressources officielles. Ce tutoriel n'a pas vocation à remplacer les sources officielles mais à essayer de présenter les possibilités offertes par la BAN et les outils associés pour faciliter le géocodage.

Nous nous concentrons sur l'utilisation des données mais si votre rue ou votre numéro de rue n'est pas présent, vous pouvez contribuer aussi à faire cette mise à jour (même si vous êtes une collectivité) en allant sur [la partie Contribuer](https://web.archive.org/web/20151114055739/https://adresse.data.gouv.fr/contrib/).

!!! note
    Ce contenu a été présenté lors du SOTM (State Of The Map) France 2015 à Brest (29) pendant la journée d'organisation libre, le Dimanche.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Le géocodage, pour qui, pour quoi ?

Il s'agit d'être capable d'associer des adresses à des coordonnées.

Cela peut servir pour calculer des itinéraires. Un utilisateur final pour chercher le trajet le plus court saisit l'adresse de départ, le géocodeur renvoie les coordonnées de départ. Il saisit ensuite l'adresse d'arrivée et obtient encore les coordonnées. Ce sont ces coordonnées qui sont généralement utilisées pour appeler le calculateur d'itinéraires. En passant un point d'arrivée et de départ, il renvoie le trajet pour par exemple faire le trajet Paris - Brest.

Un autre usage est de déterminer les coordonnées géographiques de vos clients pour ensuite comprendre comment ils sont distribués: cela peut servir pour répartir les commerciaux d'une société.

Il est aussi intéressant de pouvoir effectuer l'opération inverse, c'est du géocodage inverse (ou "reverse-geocoding") qui consiste à déterminer l'adresse depuis les coordonnées. Cela peut servir par exemple à un livreur pour confirmer qu'il est bien dans la rue où il doit livrer.

## BAN/BANO, quezako ?

### Rappel du projet

Pompage assumé de <http://adresse.data.gouv.fr/about/> à propos de la BAN (Base Adresse Nationale) :

> La Base Adresse Nationale est une base de données qui a pour but de référencer l'intégralité des adresses du territoire français.
>
> Elle est constituée par la collaboration entre :
>
> - des acteurs nationaux tels que l'IGN et La Poste,
> - des acteurs locaux tels que les collectivités, les communes, les SDIS,
> - des citoyens par exemple à travers le projet OpenStreetMap et l'association OpenStreetMap France.
>
> Le projet est co-gouverné par l'Administrateur Général des Données et le Conseil National de l'Information Géographique.
>
> Le site adresse.data.gouv.fr est développé par la mission Etalab du Secrétariat Général à la Modernisation de l'Action Publique (SGMAP).

Pour BANO (Base Adresse Nationale Ouverte), il s'agit du projet initié par OpenStreetMap France qui a mené à la mise en place de la BAN qui regroupe principalement OpenStreetMap France, La Poste, l'IGN et d'autres acteurs publics (collectivités locales).

### La licence

Les données BAN sont sous licence double (dont ODBL) et celles de BANO en [ODBL](http://bano.openstreetmap.fr/data/LICENCE.txt).

L'intérêt de BAN est qu'on dispose de plus de données car certaines viennent de l'IGN et de La Poste. Cela est à la fois une force et une faiblesse: plus d'adresses à disposition mais à l'inverse risque de bruit et moindre qualité (du moins dans un premier temps).

----

## De l'intérêt d'installer son propre serveur Addok

Voici quelques raisons:

- On ne peut avoir besoin de travailler que sur une zone. Dans ce cas, il n'est pas très productif d'interroger un serveur national.
- On veut géocoder de manière massive: même si c'est possible, on risque de surcharger le serveur officiel et on aura toujours la latence liée au réseau qui sera handicapante. Pensez au concept du "fair-use" (voir la section OSM sur l'usage des tuiles par exemple). De plus, vous risquez le bannissement de votre IP pour avoir abusé des "bonnes choses".
- On veut indexer en favorisant un champ parmi d'autres. Par exemple, on veut que la recherche favorise des résultats pour un code INSEE. En indexant spécifiquement et en donnant des règles spécifiques, on peut favoriser ce cas.
- On peut ajouter un filtre pour par exemple spécifier le département lors de la recherche, en plus de l'adresse "classique" de type "numéro, type de voie, nom de voie, commune"

----

## La technique

### Architecture générale

On a deux composantes :

- un serveur qui mange des données adresse et s'occupe de les indexer, nommé Addok. Cela s'effectue avec Redis (une base de données clés/valeurs) permettant une indexation efficace combinée à des algorithmes de ressemblance de caractères (ngrams) côté Python.

- un client qui appelle le serveur. Il le fait par l'intermédiaire d'un appel http. Cet appel peut être fait depuis :
    - un client lourd bureautique SIG type ArqGIS
    - une bibliothèque JavaScript pour la cartographie web (Leaflet ou OpenLayers)
    - une ligne de commande (géocodage CSV)
    - depuis un navigateur

### Installation

Paquets, création dossier et environnement Python.

#### Installation des paquets

Au lieu de télécharger et d'enchainer des "clics-clics", les paquets sont la même chose mais installable en tapant des instructions dans la ligne de commande

```bash
sudo apt-get install redis-server python3.4 python3.4-dev python-pip python-virtualenv virtualenvwrapper
```

#### Création du répertoire

```bash
mkdir ban && cd ban
```

#### Création d'un environnement virtuel

```bash
virtualenv addok --python=/usr/bin/python3.4
```

!!! tip
    Il est possible d'utiliser virtualenvwrapper lorsqu'on gère de nombreux environnements virtuels Python.

#### Activation de l'environnement virtuel

```bash
source addok/bin/activate
```

#### Installation de Addok

```bash
pip install addok
```

----

### Les données

#### Deux sources supportées officiellement

- la base de données Nominatim
- un fichier "JSON streaming" (JSON délimité)

Nous avons retenu l'option 2 pour nous car plus facile à mettre en oeuvre.

Faites vos courses par département sur <http://bano.openstreetmap.fr/data/> pour BANO

Sinon, faites-les sur BAN <http://bano.openstreetmap.fr/BAN_odbl/>. Pour ce dernier, les données de type JSON ne sont pas par département mais nationales. Il vous faudra télécharger la base complète et la filtrer ("recette" plus bas).

Pour info, les tailles des fichiers France ci-dessous

252 MB

```bash
wget http://bano.openstreetmap.fr/data/full.sjson.gz
```

1.8GB

```bash
gzip -d full.sjson.gz
```

Attention, ces chiffres sont trompeurs: l'indexation fait littéralement exploser le volume de données.

Pour notre démonstration, nous allons travailler à l'échelle du Finistère (29).

5.8 MB

```bash
wget http://bano.openstreetmap.fr/data/bano-29.json.gz
```

48MB

```bash
gzip -d bano-29.json.gz
```

Quelques exemples de filtrage pour information

Cela peut servir pour limiter encore plus les données.

Brest seule

```bash
grep '"city": "Brest"' bano-29.json > bano-29-brest.json
```

Brest et agglo

```bash
grep '"city": "Brest\|Bohars\|Gouesnou\|Guilers\|Guipavas\|Plougastel-Daoulas\|Plouzané\|Le Relecq-Kerhuon' bano-29.json > bano-29-brest-agglo.json
```

Après cet aparté, passons à Redis.

#### Import et indexation des données dans Redis

```bash
addok batch /home/adminuser/ban/bano-29.json
addok ngrams
```

On utilise en fait une configuration par défaut et c'est un peu magique.

Inspectons la configuration :

```bash
gedit addok/lib/python3.4/site-packages/addok/config/default.py
```

En effet, il est possible par exemple de changer l'indexation: nous pourrions très bien vouloir utiliser d'autres champs.

Vous pouvez aussi voir [la documentation officielle](https://addok.readthedocs.org/en/latest/config/).

### Test du serveur

Lancer le serveur :

```bash
gunicorn addok.server:app
```

Tester que ça marche dans le navigateur avec :

<http://127.0.0.1:8000/search/?q=Loguillo>

Il est possible de déployer gunicorn seul ou en combinaison avec un serveur web plus classique type Apache ou Nginx mais nous ne rentrons pas dans ce détail. Une petite recherche web peut répondre facilement à cette question.

Pour visualiser dans le navigateur, il est recommandé d'avoir [JSONView] sous [Firefox](https://addons.mozilla.org/fr/firefox/addon/jsonview/) et sous [Chrome/Chromium](https://chrome.google.com/webstore/detail/jsonview/chklaanhfefbnpoihckbnefhakgolnmc).

En ligne de commande,

```bash
sudo pip install httpie
http http://127.0.0.1:8000/search/?q=Loguillo
```

ou

```bash
sudo apt-get install curl
curl http://127.0.0.1:8000/search/?q=Loguillo | python -mjson.tool
```

----

## Utiliser le géocodeur

### Comprendre les appels

Vous pouvez tout simplement utiliser [la documentation officielle](https://web.archive.org/web/20151114055739/http://adresse.data.gouv.fr/api/#search)

Elle est simplement tellement bien faite et didactique, que ce serait bête de ne pas l'utiliser. Elle est en français donc aucune excuse n'est possible :wink:.

### Consommer l'API

#### Via des bibliothèques JavaScript dans le navigateur

- Leaflet : le plugin est récupérable sur <https://github.com/komoot/leaflet.photon>. Une illustration de son usage est [le site officiel de la BAN](https://adresse.data.gouv.fr/map/).
- OpenLayers 3 : le plugin est sur <https://github.com/webgeodatavore/ol3-photon>. Il est accompagné de la démo.
- OpenLayers 2 : il n'existe pas de code pour OpenLayers 2 mais le code pour OpenLayers 3 est quasi prêt pour cela, seule la partie zoom et construction du point pour zoomer est à changer.

#### Via un client comme ArqGIS

Sinon en ligne de commande, en ouvrant la console Python :

```python
canvas = qgis.utils.iface.mapCanvas()
centre = qgis.core.QgsPoint(-1.7923, 47.1993)
canvas.setCenter(centre)
qgis.utils.iface.mapCanvas().refresh()

import urllib2
import json

def centerToAdress(placeName):
    req = urllib2.Request('http://api-adresse.data.gouv.fr/search/?q=%s' % placeName)
    response = urllib2.urlopen(req).read()
    jsonResp = json.loads(response)
    coords = jsonResp['features'][0]['geometry']['coordinates']
    ptCentre = qgis.core.QgsPoint(*coords)
    print ptCentre
    canvas.setCenter(ptCentre)
    qgis.utils.iface.mapCanvas().refresh()

centerToAdress('Paris')
```

Il est possible de "pluginiser" les appels à BAN/BANO :

- soit en hackant [MMGIS](http://michaelminn.com/linux/mmqgis/),
- soit sur [GeoCoding ArqGIS](http://www.itopen.it/geocoding-qgis-plugins-released/),
- soit avec un développement "from scratch" (à partir de rien).

#### En géocodant un CSV

Si vous n'avez pas besoin de cartes dans l'immédiat mais juste des données.

Par le site web, c'est possible avec <http://adresse.data.gouv.fr/csv/>.
Sinon, passez par les exemples officiels (dupliqués ci-dessous)

```bash
http --timeout 600 -f POST <http://api-adresse.data.gouv.fr/search/csv/> data@path/to/file.csv

http -f POST <http://api-adresse.data.gouv.fr/search/csv/> columns='voie' columns='ville' data@path/to/file.csv
```

Un jeu de données pour tester peut être [l'annuaire des débits de tabac en France métropolitaine](https://web.archive.org/web/20151114055739/http://www.douane.gouv.fr/datadouane/a12431-annuaire-des-debits-de-tabac-en-france-metropolitaine).

Pensez à n'utiliser que les premières lignes plutôt que tout le jeu de données.
Même si le géocodage marche sur le jeu de données complet, il est inutile de patienter, ni de faire des appels lourds vers le serveur officiel (ou le votre) juste pour un test.

#### Par des appels individuels

En fait, on les a déjà vus dans la section "Comprendre les appels".

Pour du géocodage en masse, évitez de "bourriner" sur l'API et utilisez le géocodage CSV (qui permet d'éviter de saturer le réseau à cause du nombre d'appels et aussi de diminuer la consommation mémoire) ou bien installez votre propre serveur, d'où ce workshop.

----

## Conclusion

Nous espérons que vous avez apprécié ce contenu. N'hésitez pas à commenter qu'il s'agisse d'incompréhensions, d'erreurs de notre part (typo comme contenu) ou pour simplement nous remercier !

----

<!-- geotribu:authors-block -->
