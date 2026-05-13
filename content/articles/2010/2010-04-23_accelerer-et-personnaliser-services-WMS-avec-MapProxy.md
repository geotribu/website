---
title: "Accélérer et personnaliser vos services WMS avec MapProxy"
subtitle: "On a tous quelque chose à cacher"
authors:
    - Arnaud Vandecasteele
categories:
    - article
    - tutoriel
date: 2010-04-23
description: Tutoriel sur l’installation et la configuration de MapProxy pour accélérer et transformer des services WMS.
image:
legacy:
    - node: 249
license: default
robots: index, follow
tags:
    - cache
    - MapProxy
    - Python
    - WMS
---

# Accélérer et personnaliser vos services WMS avec MapProxy

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![Logo MapProxy](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/mapproxy.png){: .img-thumbnail-left }

[MapProxy](https://mapproxy.org) est un framework Open Source permettant la gestion des données spatiales. Il permet d'accélérer, de transformer et de tatouer (_watermarking_) des données provenant de serveurs cartographiques. Côté fonctionnement, il se place entre le serveur et le client (architecture _middleware_).

Dans ce tutoriel, nous installerons tout d'abord MapProxy, ensuite nous le paramétrerons et enfin nous effectuerons nos premiers tests.

![Architecture middleware de MapProxy. Source : MapProxy](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/MapProxy/mapproxy_schema.png){: .img-center loading=lazy }

## Téléchargement et pré-requis

Il existe différentes manières d'installer un package Python. Vous pouvez faire une installation manuelle en téléchargeant [le package source](https://pypi.org/project/MapProxy/) ou alors utiliser la commande shell `easy_install` (disponible via `python-setuptools` sur Linux Debian). Dans ce tutoriel nous utiliserons un environnement virtuel Python ; toute l'étape de téléchargement sera donc quasi automatique. Il n'est donc pas nécessaire de télécharger l'archive Python de MapProxy.

Nous allons tout d'abord installer les différentes librairies Python que nous allons utiliser :

- [`virtualenv`](https://pypi.org/project/virtualenv/) : permet de séparer vos différents projets python en créant des instances virtuelles. Cela permet par exemple d'essayer une nouvelle librairie encore en phase bêta sans pour autant polluer et/ou corrompre votre répertoire `site-packages` ou encore de faire fonctionner plusieurs versions de la même librairie.
- [`pip`](https://pypi.org/project/pip/) : tout comme `easy_install`, Pip permet d'installer des packages python. Écrit par le même auteur que virtualenv il s'intègre parfaitement à ce dernier.

Si ces termes n'évoquent rien pour vous, je vous conseille la lecture de l'excellent article de Sean Gillies [_Bootstrapping a Python project_](https://sgillies.net/2010/04/01/bootstrapping-a-python-project.html). Dans le monde "Pythonique", ces deux librairies tendent à devenir incontournables. N'hésitez donc pas à prendre quelques minutes et à bien comprendre les concepts.

Pour les personnes fonctionnant sur Ubuntu un simple `sudo aptitude install python-setuptools` suffira à installer les librairies ci-dessus. Enfin pour finir, MapProxy nécessite également l'installation des librairies suivantes :

- C compiler
- Python 2.5 or 2.6 (development tools)
- libjpeg
- zlib

Nous allons le faire en ligne de commande :

```bash
sudo aptitude install build-essential python-dev libjpeg-dev libz-dev libfreetype6-dev```
```

Pour ma part, l'installation s'est faite sur Xubuntu et ce sont les packages suivants qui m'ont été proposés : `libfreetype6-dev`, `libjpeg62-dev` et `zlib1g-dev`.

Voilà tout notre environnement est en place. Il ne reste plus maintenant qu'à installer et paramétrer MapProxy.

----

## Création de l'architecture virtuelle et installation des composants

Nous avions parlé au paragraphe précédent de `virtualenv`. Nous allons le mettre en application immédiatement. Pour cela, placez-vous dans le répertoire où vous allez réaliser votre installation. Pour notre exemple, dans notre répertoire **home**, nous allons créer un répertoire **envPython** qui servira à notre installation.

```bash
~/envPython$ source mapProxy/
~/envPython$ cd mapProxy/
~/envPython$ source bin/activate
(mapProxy)user@osgeolive:~/envPython$
```

La dernière ligne vous indique que vous êtes dans votre environnement Python virtuel. À partir de maintenant toutes les librairies python que vous installerez seront localisées au sein de votre environnement (dans le répertoire `bin`). Ainsi elles ne "pollueront" pas votre répertoire site-packages "officiel".

Passons maintenant aux librairies, utilisées par MapProxy (encore d'autres ^^), que nous allons installer au sein de notre nouvel environnement python virtuel. Le plus simple est de passer par l'utilitaire [`pip`](https://pypi.org/project/pip/).  
Celui-ci va permettre de parser un fichier texte et d'installer les librairies qui y sont définies. Pip est normalement installé par défaut dans votre environnement virtuel. Si ce n'est pas le cas (comme sur kubuntu par exemple), faites :

```bash
~/envPython/mapProxy$ easy_install pip
```

Utilisons le maintenant :

```bash
~/envPython/mapProxy$ pip install -r http://bitbucket.org/olt/mapproxy/raw/tip/requirements.txt
```

Quelques minutes plus tard maintenant que tout est installé (enfin !...). Vous pouvez vérifier que tout s'est correctement déroulé en exécutant la commande suivante :

```bash
~/envPython/mapProxy$ python -m mapproxy.core.version
0.8.2
```

Nous pouvons nous attaquer à la configuration de MapProxy.

----

## Initialisation de MapProxy

Rassurez-vous, l'initialisation de MapProxy tient en une ligne de commande. L'utilitaire [Paster](http://pythonpaste.org/) va en effet créer automatiquement toute l'architecture (_skeleton_) des dossiers et fichiers nécessaires.
Toujours dans votre environnement virtuel faites :

```bash
~/envPython/mapProxy$ paster create -t mapproxy_conf mymapproxy
```

`mymapproxy` est le répertoire qui contiendra l'applicatif. Au sein de celui-ci 3 nouveaux répertoires ont été créés :

- `etc` : contient les fichiers de configuration
- `tmp` : comme son nom l'indique, c'est un simple répertoire pour les fichiers temporaires
- `var` : contient les fichiers de log et les données

Il ne reste plus maintenant qu'à démarrer notre serveur MapProxy. pour cela faites :

```bash
mapProxy$ cd mymapproxy/
mymapproxy$ paster serve etc/develop.ini --reload
```

Et vous devriez voir affiché le texte suivant :

```bash
Starting subprocess with file monitor
2010-04-15 12:12:26,504 - INFO - 2663:mapproxy.core.conf_loader:load_services - Reading services configuration: /home/user/envPython/mapProxy/mymapproxy/etc/services.yaml
Starting server in PID 2663.
serving on 0.0.0.0:8080 view at http://127.0.0.1:8080
```

Voilà, notre serveur est maintenant démarré. Il tourne en local (localhost ou 127.0.0.1) sur le port 8080. Testons-le immédiatement avec [la couche Omniscale OpenStreetMap WMS](http://osm.omniscale.net/) configurée par défaut. Pour cela dans votre navigateur exécutez la requête suivante : <http://localhost:8080/service?> . L'image ci-dessous devrait alors vous être retournée.

![Couche OSM Omniscale mise en cache localement avec MapProxy](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/mapproxy_image_request.png){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
