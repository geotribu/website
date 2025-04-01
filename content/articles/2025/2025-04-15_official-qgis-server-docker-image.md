---
title: "Que se cache-t-il derrière l'image Docker officielle de QGIS Server ?"
subtitle: (ou l’article que personne ne lira)
authors:
    - Paul BLOTTIERE
categories:
    - article
comments: true
date: 2025-04-15
description: "Les mystères de l'image Docker officielle de QGIS Server"
icon: material/docker
image:
license: default
robots: index, follow
tags:
    - Docker
    - QGIS
    - QGIS Server
---

# Que se cache-t-il derrière l'image Docker officielle de QGIS Server ?

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

Le dernier article de Geotribu sur le [déploiement de QGIS Server](../2010/2010-09-03_creer_diffuser_services_wms_avec_qgis.md) date de 2010 :scream: ! À cette époque, [Docker](https://www.docker.com/) ne faisait pas encore partie des pratiques de déploiement, et pour cause puisqu'il n'a été rendu disponible qu'en 2013. Nous allons donc profiter de la publication d'une image Docker officielle QGIS Server l'année dernière pour revenir dans la course.

Pour rappel, QGIS Server est une solution open source de serveur cartographique, similaire à [GeoServer](https://geoserver.org/) ou [MapServer](https://mapserver.org/), qui permet de diffuser des cartes et des données géospatiales sur le web. Il s'appuie sur les standards OGC (Open Geospatial Consortium) pour offrir des services interopérables. QGIS Desktop joue le rôle d'outil de configuration WYSIWYG, permettant ainsi aux utilisateurs de configurer facilement leurs cartes.

La documentation officielle de QGIS Server explique en détail l'[installation de QGIS Server](https://docs.qgis.org/3.40/fr/docs/server_manual/getting_started.html) de manière native, c'est-à-dire directement depuis les dépôts de paquets de votre plateforme ou distribution. Cependant, il existe très peu de ressources concernant le déploiement conteneurisé de manière générale. Nous allons donc expliquer en quoi et comment l'utilisation de l'image Docker officielle de QGIS Server facilite le déploiement.

## Écosystème technique

Oui il existe depuis 2024 une image Docker officielle de QGIS Server :tada:... mais qu'est ce que cela signifie ? Commençons par rappeler d'abord la pile technologique sous-jacente ainsi qu'un peu de vocabulaire.


`Docker`

:   Docker est une plateforme qui permet de créer, déployer et exécuter des applications dans des conteneurs, garantissant ainsi leur portabilité et leur isolation. Ces applications peuvent être distribuées sous forme d'images via des plateformes spécialisées ou reconstruites à partir des sources.

`Dockerfile`

:   [Dockerfile](https://docs.docker.com/reference/dockerfile/) est un script définissant les étapes pour construire une image Docker personnalisée.

`Docker Hub`

:   [Docker Hub](https://hub.docker.com/) est une plateforme en ligne qui permet de stocker, partager et distribuer des images Docker, offrant ainsi un dépôt centralisé pour les applications et leurs composants.

`docker-compose`

:   La composition - généralement via l'outil [Docker Compose](https://docs.docker.com/compose/) - permet de définir et de gérer des applications multi-conteneurs en utilisant un fichier de configuration, qui décrit les services, réseaux et volumes nécessaires à l'application.

`Cluster cloud`

:   La clusterisation - non abordée dans cet article - concerne la gestion de plusieurs instances de Docker réparties sur plusieurs machines physiques ou virtuelles pour augmenter la disponibilité, la résilience et la scalabilité de l'application. Il s'agit généralement d'environnements cloud basés par exemple sur [Kubernetes](https://kubernetes.io/).

De nombreuses images Docker de QGIS Server sont disponibles en ligne, chacune ayant des spécificités liées à son utilisation et à sa configuration. Mais depuis 2024, l'image initialement fournie par [OPENGIS.ch](https://www.opengis.ch/) est désormais disponible en tant qu'image officielle sur le [Docker Hub de QGIS.org](https://hub.docker.com/r/qgis/qgis-server). Pour l'obtenir, rien de plus simple:

```bash title="Téléchargement de l'image officielle QGIS Server"
docker pull qgis/qgis-server:ltr
```

## Étude du contenu

Pour déployer QGIS Server en tant qu'application, il est nécessaire d'intégrer des services tiers dans le conteneur afin d'assurer son bon fonctionnement. Comme indiqué dans la documentation, QGIS Server est une application :

- Nécessitant un serveur graphique.
- Basée sur le protocole de communication FastCGI pour interagir avec un serveur Web.
- En fonction du serveur Web utilisé (Apache, NGINX, etc.), un utilitaire spécifique peut être requis pour lancer le processus FCGI sous-jacent.

Afin de répondre à ces contraintes, plusieurs solutions techniques peuvent être envisagées, ce qui explique en partie la diversité des images Docker de QGIS Server disponibles en ligne. L'image proposée par OPENGIS.ch repose sur :

- [Xvfb](https://www.x.org/archive/X11R7.7/doc/man/man1/Xvfb.1.xhtml) (X virtual framebuffer) comme serveur graphique.
- [NGINX](https://nginx.org/) comme serveur Web.
- [spawn-fcgi](https://linux.die.net/man/1/spawn-fcgi) comme utilitaire pour exécuter l'application FastCGI QGIS Server.

### QGIS Server et FastCGI

Il est possible de tester simplement l'application QGIS Server en ligne de commande dès lors qu'un serveur graphique est en cours d'exécution. Pour cela, il faut simuler le passage des variables d'environnement au processus FCGI, comme le ferait un serveur Web. Par exemple, il est possible d'envoyer une requête à QGIS Server en utilisant la variable d'environnement `REQUEST_URI`:

```bash title="Exécution d'une requête par le process FCGI QGIS Server"
# Démarrage d'un shell dans un conteneur QGIS Server
$ docker run -it qgis/qgis-server:ltr /bin/bash

# Exécution du serveur graphique virtuel Xvfb en tâche de fond et redirection
# des logs vers /dev/null
$ /usr/bin/Xvfb :99 > /dev/null 2>&1 &

# Envoie d'une requête à QGIS Server et redirection des logs vers /dev/null
$ REQUEST_URI="MAP=fake.qgs" /usr/lib/cgi-bin/qgis_mapserv.fcgi 2>/dev/null
Content-Length: 195
Content-Type: text/xml; charset=utf-8
Server:  QGIS FCGI server - QGIS version 3.43.0-Master
Status:  500

<?xml version="1.0" encoding="UTF-8"?>
<ServerException>Project file error. For OWS services: please provide a SERVICE and a MAP parameter pointing to a valid QGIS project file</ServerException>
```

On observe ici un code d'erreur `500` de QGIS Server indiquant que le projet `fake.qgs` renseigné via `REQUEST_URI="MAP=fake.qgs"` n'existe pas.  L'exception `<ServerException>Project file error.</ServerException>` est donc retournée par QGIS Server.

### Script de démarrage

Auparavant, nous avons lancé le conteneur QGIS Server en mode interactif à l'aide de l'option `-i` et de la commande `/bin/bash`. Sans ces options, l'application QGIS Server démarre de manière classique en fonction de l'instruction `CMD` ou `ENTRPYPOINT` précisée dans le Dockerfile.

Le script de démarrage utilisé, situé dans le système de fichiers du conteneur, peut être trouvé à l'emplacement `/usr/local/bin/start-xvfb-nginx.sh`, et son chemin peut être obtenu en inspectant l'image.

{% raw %}

```bash title="Inspection de l'image pour localiser le script de démarrage"
# Récupération du chemin du script de démarrage
$ docker inspect -f '{{.Config.Cmd}}' qgis/qgis-server:ltr
[/bin/sh -c /usr/local/bin/start-xvfb-nginx.sh]

# Affichage du contenu du script de démarrage
$ docker run qgis/qgis-server:ltr cat /usr/local/bin/start-xvfb-nginx.sh
```

{% endraw %}

En étudiant le contenu de ce script, nous observons la séquence de démarrage des utilitaires tiers mentionnés ci-dessus:

- le serveur graphique `Xvfb`
- `spawn-fcgi` avec le lancement de QGIS Server en spécifiant le port TCP `9993` pour la communication entre le serveur Web et le processus FCGI
- `NGINX` si besoin en fonction de la variable d'environnement `SKIP_NGINX` renseignée au moment de l'exécution

```bash title="Extrait du script de démarrage"
...
/usr/bin/Xvfb :99 -ac -screen 0 1280x1024x16 +extension GLX +render -noreset >/dev/null &
XVFB_PID=$(waitfor /usr/bin/Xvfb)

if [ -z "$SKIP_NGINX" ] || [ "$SKIP_NGINX" == "false" ] || [ "$SKIP_NGINX" == "0" ]; then
    nginx
    NGINX_PID=$(waitfor /usr/sbin/nginx)
fi

spawn-fcgi -n -u ${QGIS_USER:-www-data} -g ${QGIS_USER:-www-data} -d ${HOME:-/var/lib/qgis} -P /run/qgis.pid -p 9993 -- /usr/lib/cgi-bin/qgis_mapserv.fcgi &
...
```

### Configuration NGINX

La configuration du serveur Web NGINX est déployée de manière standard dans le fichier de configuration `/etc/nginx/nginx.conf`:

```bash title="Affichage du contenu du fichier de configuration de NGINX"
$ docker run -it qgis/qgis-server:ltr cat /etc/nginx/nginx.conf
...
    location /ogc/ {
        rewrite ^/ogc/(.*)$ /qgis/qgis_mapserv.fcgi?map=/io/data/$1/$1.qgs;
    }
    # Direct access without map rewrite
    location /ows/ {
        rewrite ^/ows/$ /qgis/qgis_mapserv.fcgi;
    }
    location /wfs3/ {
        rewrite ^/wfs3/(.*)$ /qgis/qgis_mapserv.fcgi;
    }
    location /qgis/ {
        internal; # Used only by the OGC rewrite
        root /var/www/data;
        fastcgi_pass  localhost:9993;
...
```

Dans cette configuration, on distingue trois points d'entrée publics et un point d'entrée interne :

- Un accès via `/ogc/my_project`, qui attend spécifiquement un projet QGIS situé à `/io/data/my_project/my_project.qgs`.
- Un accès via `/ows/` et `/wfs3/`.
- Un accès interne via `/qgis`, utilisé par les autres points d'accès, permettant la communication avec le processus FCGI via la socket `localhost:9993`.

Le point d'accès numéro 1 nécessite donc un montage du répertoire `/io/data/` afin de fonctionner avec un répertoire dédié à chaque projet.

## Démarrage du conteneur

Maintenant que nous avons exploré les fonctionnalités de notre image, nous pouvons tester les différentes configurations de lancement.

### Configuration par défaut

Il est possible de démarrer le conteneur QIGS Server avec la configuration par défaut grâce aux paramètres ci-dessous:

- Redirection du port `8080` local vers le port `80` du serveur Web du conteneur.
- Montage du répertoire de projets QGIS vers `/io/data` du conteneur.

```bash title="Démarrage d'un conteneur QGIS Server"
# Clone du dépôt QGIS-Training-Data de QGIS
git clone https://github.com/qgis/QGIS-Training-Data

# Préparation du répertoire projet world/world.qgs pour le point de montage
# /io/data
cp -r QGIS-Training-Data/exercise_data/qgis-server-tutorial-data/ \
    QGIS-Training-Data/exercise_data/world

# Démarrage d'un conteneur en montant le répertoire des projets QGIS du tutorial
docker run \
    -v ./QGIS-Training-Data/exercise_data/:/io/data \
    -p 8080:80 \
    qgis/qgis-server:ltr
```

Une fois le conteneur déployé, il est possible d'envoyer des requêtes à QGIS Server par le biais des points d'entrée NGINX décrit dans la partie précédente:

```bash title="Points d'entrée /ogc, /ows et /wfs3"
# Requête WMS vers /ogc du serveur web NGINX du conteneur pour accéder au projet
# /io/data/world/world.qgs
curl "http://localhost:8080/ogc/world?SERVICE=WMS&REQUEST=GetCapabilities"

# Requête WMS vers /ows en indiquant explicitement le chemin du projet via le paramètre MAP
curl "http://localhost:8080/ows/?MAP=/io/data/qgis-server-tutorial-data/world.qgs&SERVICE=WMS&REQUEST=GetCapabilities"

# Requête OGC API Features vers /wfs3 en indiquant explicitement le chemin du projet via le
# paramètre MAP
curl "http://localhost:8080/wfs3/collections.json?MAP=/io/data/qgis-server-tutorial-data/world.qgs"
```

Le protocole OGC API Feature, aussi connu sous le nom de WFS3, offre également un rendu HTML, permettant ainsi d'accéder directement, via votre navigateur, à une page web pour explorer les données sous-jacentes.

```bash title="URL d'une page de rendu HTML de OGC API Features"
http://localhost:8080/wfs3/collections/countries/items/65.html?MAP=/io/data/qgis-server-tutorial-data/world.qgs
```

![OGC API Features Landing Page](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/qgis_server_docker/ogcapif.png "OGC API Feeatures Landing Page"){: .img-center loading=lazy }

### Composition avec NGINX externe

Comme mentionné précédemment, une variable d'environnement `SKIP_NGINX` permet d'utiliser le conteneur QGIS Server sans serveur web intégré. Dans ce cas, le conteneur QGIS Server fonctionne uniquement comme un *backend* de rendu graphique. Il est alors possible de recourir à la notion de composition pour créer une application multi-conteneurs avec:

- Un conteneur QGIS Server pour le rendu graphique.
- Un conteneur NGINX comme serveur Web qui redirige les requêtes vers le processus FCGI via la socket `9993`.

Tout d'abord le fichier de configuration de NGINX permet de décrire un point d'accès et le moyen de communiquer avec QGIS Server:

```Nginx title="Fichier de configuration de NGINX nginx.conf"
events {
    worker_connections  1024;
}

http {
    upstream qgis-fcgi {
        server qgis-server:9993;
    }
    server {
        location /qgisserver/ {
            fastcgi_pass  qgis-fcgi;
            fastcgi_param QUERY_STRING $query_string;
            include fastcgi_params;
        }
    }
}
```

Il faut ensuite rédiger un fichier de configuration pour l'outil `docker compose`, afin de décrire notre application multi-conteneurs:

```yml title="Fichier de configuration docker-compose.yml"
services:
  nginx:
    image: "nginx"
    volumes:
      # montage du fichier de configuration NGINX dans le conteneur
      - ./nginx.conf:/etc/nginx/nginx.conf
    ports:
      - "8080:80"
    depends_on:
      - qgis-server
  qgis-server:
    image: "qgis/qgis-server:ltr"
    environment:
      # désactivation du NGINX interne
      SKIP_NGINX: "true"
    volumes:
      # montage du répertoire de projets
      - ./QGIS-Training-Data/exercise_data/:/io/data
```

!!! warning
    Les scripts de configuration ci-dessus sont volontairement simplifiés pour la compréhension du lecteur mais ne doivent pas être utilisés en production :bomb:

Il reste finalement à exécuter nos conteneurs grâce à la commande `docker-compose` qui va automatiquement lire le fichier de configuration nommé `docker-compose.yml` présent dans le répertoire courant:

```bash
# Exécution des conteneurs en fond
$ docker-compose up -d
[+] Running 3/3
 ✔ Network tmp_default          Created
 ✔ Container tmp-qgis-server-1  Started
 ✔ Container tmp-nginx-1        Started

# Statuts des conteneurs NGINX et QGIS Server en cours d'exécution
$ docker ps
CONTAINER ID   IMAGE                  COMMAND                  CREATED             STATUS             PORTS                                               NAMES
30dce3dd878f   nginx                  "/docker-entrypoint.…"   3 seconds ago       Up 2 seconds       0.0.0.0:8081->80/tcp, [::]:8081->80/tcp             test-nginx-1
8b73de48d754   qgis/qgis-server:ltr   "/bin/sh -c /usr/loc…"   3 seconds ago       Up 2 seconds       80/tcp, 9993/tcp                                    test-qgis-server-1

# GET vers /qgisserver en indiquant explicitement le chemin du projet via le paramètre MAP
$ curl "http://localhost:8080/qgisserver/?MAP=/io/data/qgis-server-tutorial-data/world.qgs&SERVICE=WMS&REQUEST=GetCapabilities"
```

## Et les plugins?

Depuis le début de cet article nous nous sommes ammusé (oui oui :sparkles:!) à explorer l'image officielle de QGIS Server à travers un peu de rétro-ingénierie. Toutefois, il est également possible de consulter la [documentation](https://github.com/qgis/qgis-docker/blob/main/server/README.md) ou d'examiner le fichier [Dockerfile](https://github.com/qgis/qgis-docker/blob/main/server/Dockerfile) utilisé pour générer cette image.

En regardant ce fichier de plus prêt, nous pouvons constater l'existence de l'instruction `ENV QGIS_PLUGINPATH /io/plugins`. Cela implique que QGIS Server s'attend à avoir des plugins Python dans le répertoire indiqué. Pour tester cette mécanique, le plugin [wfsOutputExtension](https://plugins.qgis.org/plugins/wfsOutputExtension/) de la société [3Liz](https://www.3liz.com/) peut être déployé:

```bash title="Déploiement du plugin wfsOutputExtension"
# Création d'un répertoire dédié pour les plugins
mkdir plugins

# Récupération du plugin serveur wfsOutputExtension
gt clone https://github.com/3liz/qgis-wfsOutputExtension plugins

# Démarrage d'un conteneur en montant les répertoires des projets QGIS et des
# plugins
docker run \
    -v ./QGIS-Training-Data/exercise_data/:/io/data \
    -v ./plugins/:/io/plugins \
    -p 8080:80 \
    qgis/qgis-server:ltr
```

Grâce au plugin `wfsOutputExtension`, il est possible de spécifier divers formats supplémentaires à travers le paramètre `OUTPUTFORMAT` de la requête WFS `GetFeature`. Nous pouvons par exemple spécifier le format `csv` non supporté nativement par QGIS Server:

```bash title="Exécution d'une requête WFS GetFeature"
$ curl "http://localhost:8080/ows/?MAP=/io/data/qgis-server-tutorial-data/world.qgs&SERVICE=WFS&REQUEST=GetFeature&TYPENAME=countries&FEATUREID=countries.1&OUTPUTFORMAT=csv"
gml_id,id,name
countries.1,1,Antigua and Barbuda
```

## Conclusion

L'image Docker officielle de QGIS Server simplifie considérablement le déploiement de cette solution serveur cartographique, offrant une configuration prête à l'emploi et facilement adaptable. Grâce à Docker, il devient facile de déployer QGIS Server de manière portable et isolée, sans se soucier des dépendances complexes telles que les serveurs graphiques ou Web.

En intégrant `NGINX`, `Xvfb` et `FastCGI`, l'image permet de faire fonctionner QGIS Server de manière fluide dans un environnement conteneurisé. Elle offre aussi la possibilité d'utiliser un serveur Web externe, comme NGINX, pour séparer les fonctions et mieux contrôler les configurations.

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
