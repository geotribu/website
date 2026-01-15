---
title: Mise en place d'un NextCloud
subtitle: Efficace et pas cher, c'est NextCloud que j'préfère !
authors:
    - Guilhem ALLAMAN
categories:
    - article
comments: true
date: 2026-04-14
description: Mise en place d'un serveur NextCloud pour stocker et partager ses fichiers en mode collaboratif, sur Desktop et Mobile.
icon: fontawesome/solid/cloud
image:
tags:
    - auto-hébergement
    - cloud
    - déploiement
    - docker
    - infrastructure
    - linux
    - NextCloud
---

# Mise en place d'un NextCloud auto-hébergé

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![Logo NextCloud](https://cdn.geotribu.fr/img/logos-icones/nextcloud.webp){: .img-thumbnail-left }

Salut les _géomaniacs_ ! Aujourd'hui on va voir, au long de cet article, comment mettre en place un serveur NextCloud auto-hébergé, pour stocker et partager des fichiers en toute sérénité, au poste comme en mobilité.

![Interface web de NextCloud, qui montre les dossiers et fichiers stockés](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/mise_en_place_nextcloud_autoheberge/nextcloud_files.webp){: .img-center loading=lazy }

## Un énième article sur NextCloud :thinking: ?

Alors, devant la multitude de docs et tutos qui traînent sur le net concernant l'installation de NextCloud, comme par exemple [la documentation officielle](https://docs.nextcloud.com/server/latest/admin_manual/installation/source_installation.html), ou encore [un billet sur le blog officiel](https://nextcloud.com/blog/how-to-install-the-nextcloud-all-in-one-on-linux/), ou encore des tutos sur les plateformes vidéos, et si le sujet n'est pas à proprement parler orienté géo, la question c'est pourquoi en faire un tuto ici dans Geotribu ? _Why_ ? _Wieso_ ? ¿_Por qué_? _今すぐチーズをくれ_ !

Premièrement, on a souvent besoin de partager des documents, par exemple des données géospatiales, style [geopackage](https://www.geopackage.org/), ou _chépe[^1]_, ou que sais-je encore. Ce que permet NextCloud, avec des partages de liens, de la synchronisation de fichiers sur le _File System_, etc. Et franchement ça marche bien, le bouzin est solide et stable. Et il y a aussi un système d’extensions, avec beaucoup qui sont sympa ! En plus, utiliser NextCloud permet de garder le contrôle sur ses données... Bref, il s'agit d'un applicatif cloud qui mérite d'être mis en avant, pour un usage perso, ou pro, ou associatif, ou autre.

Le sujet est également revenu sur la géotable de Geotribu récemment, après qu'on ait ~~bousculé~~ basculé [le serveur qui fournit le CDN des photos du site ainsi que les commentaires, vers un nouvel hébergeur](https://mapstodon.space/@geotribu/114929845299328320). On en profite pour dire un grand merci à [Georezo](https://georezo.net/), qui nous met un serveur à disposition en ce sens :heart: ! Alors peut-être qu'on mettra en place un NextCloud pour Geotribu à l'avenir, qui sait ?

De plus, _last but not least_, ici dans Geotribu on peut se permettre des blagues qu'il est difficile de faire sur le blog officiel de NextCloud :grin:. Par exemple :

??? question "Qu'est-ce qui est rouge, qui accroche parfaitement ses vectorisations aux sommets voisins, qui nous sauve des feux en été et qui est toujours bien habillé ?"
    Un snapeur-pompier...

Et enfin, cet article est un appel à la rédaction d'autres, pour aborder l'utilisation et l'intégration de NextCloud avec des outils SIG.

Allez, fini le [non-sense](https://youtu.be/J6G9t6haDII?si=roO8rcYY30lxq4v6&t=362), c'est parti ! Pas d'inquiétude ceci dit, on espère qu'il y aura plus de blabla que de lignes de commande au long de cet article...

## NextCloud ? Qu'est-ce ?

NextCloud est donc un logiciel qui fournit un cloud de fichiers et documents. [Issu d'un fork de ownCloud en 2016](https://nextcloud.com/blog/press_releases/pr20160602/), NextCloud est développé [sous license AGPL](https://help.nextcloud.com/t/nextcloud-licensing/206830) et écrit dans le langage PHP.

Il y a une interface web NextCloud qu'il est possible de customiser, ainsi que des applications clients : app Android (aussi [sur le f-droid](https://f-droid.org/en/packages/com.nextcloud.client/)), iOS, [applis _Desktop_ sur toutes les plateformes](https://nextcloud.com/install/#desktop-files) + même [un client NextCloud Talk](https://github.com/nextcloud/talk-desktop#nextcloud-talk-desktop) pour faire des visios grâce à une extension :call_me_hand:, même si bon, c'est lent...

À noter que dans cet article, nous nous concentrerons sur l'installation du serveur.

La "méthode d'installation officielle" mise en avant est la méthode maintenue par NextCloud GmbH : _AIO_. Rien à voir avec quelqu'un dont le clavier se serait bloqué en écrivant "aïoli", c'est plutôt pour [_All-In-One_](https://github.com/nextcloud/all-in-one#nextcloud-all-in-one), une méthode qui lance tout le nécessaire [dans une seule image docker](https://hub.docker.com/r/nextcloud/all-in-one).

Oui on va passer par [docker](https://www.docker.com/) ici, une technologie qui a ses avantages et ses inconvénients, et à noter qu'il est aussi possible [de lancer une installation manuelle](https://docs.nextcloud.com/server/latest/admin_manual/installation/source_installation.html#prerequisites-for-manual-installation). Il existe aussi une manière d'installer NextCloud [via des paquets snap](https://doc.ubuntu-fr.org/snap).

Ici on va lancer [la version via l'image _community_](https://hub.docker.com/_/nextcloud/), rien que pour se la raconter et le goût du risque, car la description stipule "_:warning::warning::warning: This image is maintained by community volunteers and designed for expert use_" :sunglasses: (notez les 3 _warnings_). Plus sérieusement, il s'agit d'une version maintenue par la communauté, et qui lance uniquement l'applicatif, nous permettant ainsi de choisir la base de données utilisée, ainsi que la configuration du [_reverse-proxy_](https://en.wikipedia.org/wiki/Reverse_proxy) nginx.

!!! warning "Ceintures et bretelles"
    Vous comprendrez que ça part sur une installation d'un NextCloud auto-hébergé, donc à administrer, maintenir, sauvegarder etc. Notez qu'il y a des fournisseurs et hébergeurs sur qui vous pouvez vous appuyer concernant ces joies :yum:. Si vous souhaitez mettre en production une instance installée à partir de cet article, c'est à vos rixes et périls !

!!! warning "Nombre d'utilisateurs max sur une instance _Community_"
    [Certaines discussions sur la plateforme communautaire de NextCloud](https://help.nextcloud.com/t/nextcloud-licensing/206830/2) semblent indiquer des nombres max de comptes d'utilisateur/rices. Personnellement, sur les instances que j'ai mises en place et utilisées, je n'ai jamais atteint ce plafond, alors je ne saurais vous dire.

## Mise en route :truck:

Pour installer NextCloud, il vous faudra une machine virtuelle linux, sous debian ou ubuntu pour la méthode expliquée ici. Privilégiez les dernières versions stables en date, [Ubuntu 24.04 LTS](https://ubuntu.com/about/release-cycle) ou [debian 13 "trixie"](https://www.debian.org/releases/trixie/release-notes/), ou autre.

Pour schématiser, on aura principalement besoin de 3 briques :

1. l'applicatif NextCloud, qui fournit l'API et l'interface web.
2. une base de données, pour stocker en interne le nécessaire qui fait fonctionner l'applicatif ci-dessus.
3. une arborescence de dossiers et fichiers, c'est un peu là le coeur et le but du truc.

### Base de données sous-jacente

[NextCloud est compatible avec 3 systèmes de bases de données](https://docs.nextcloud.com/server/stable/admin_manual/configuration_database/linux_database_configuration.html): PostgreSQL, MySQL et Oracle. _Ouh la la_, vraiment du mal à me décider sur lequel partir ! Et si on lançait un dé à 3 faces, histoire de se dédouaner de cette responsabilité et comme [il est possible de le faire avec la commande slash `/roll` dans QChat, le plugin de tchat dans QGIS #PlacementDeProduit ?](https://geotribu.github.io/qchat/usage/slash_commands.html#roll)

Résultat : les dés ont parlé, c'est PostgreSQL ! Dîtes-donc, le hasard fait bien les choses...

Deux manières de la jouer maintenant :

- Façon "ceinture et bretelles" : on utilise une base pg externe, c'est plus simple à mettre à jour et ça décorrèle l'applicatif des données.
- Façon ["Les hébergeurs de l'extrême"](https://www.youtube.com/watch?v=1H4toKvejZ8) ou Fast'n'Furious : on lance une base postgres dans un docker, au même endroit que l'applicatif. C'est plus rapide, c'est _quick and dirty_, ça permet de tester directement l'installe, mais disons que c'est fortement déconseillé...

### Arborescence des dossiers et fichiers

Pour héberger les dossiers et fichiers qui seront accessibles dans les clients (web, synchro desktop, app mobile, etc.), on a besoin d'un chemin de répertoire sur la machine hôte. Vous pouvez vous rapprocher de votre administrateur/trice systèmes, si vous avez la chance d'en avoir un/e dans votre organisation, pour monter une partition adéquate, réseau ou autres. Ou alors choisir un dossier sur la machine virtuelle, par exemple `/opt/nextcloud/data`.

### Définition des services

Abordons maintenant les services déclarés, dans le [fichier `docker-compose`](https://docs.docker.com/reference/compose-file/) qui permettra de lancer le nécessaire.

!!! info "À noter que..."
    À noter que cet exemple s'applique dans le cas où nous souhaiterions instancier un NextCloud sur le domaine `cloud.lageowcestshow.xyz`. Ce qui présuppose une configuration du DNS en amont.

<!-- markdownlint-disable MD046 -->
=== "Ceintures et bretelles"

    ``` linenums="1" title="docker compose pour NextCloud - `docker-compose.yaml`"
    services:

      app:
        image: nextcloud:32
        container_name: nextcloud-app
        restart: unless-stopped
        ports:
          - 8123:80
        volumes:
          - /opt/nextcloud/data:/var/www/html
        environment:
          OVERWRITEPROTOCOL: https
          POSTGRES_HOST: <HOTE_BASE_PG_EXTERNE>
          POSTGRES_DB: <NOM_DB_BASE_PG_EXTERNE>
          POSTGRES_USER: <NOM_ROLE_BASE_PG_EXTERNE>
          POSTGRES_PASSWORD: <MOT_DE_PASSE_BASE_PG_EXTERNE>
          NEXTCLOUD_ADMIN_USER: admin
          NEXTCLOUD_ADMIN_PASSWORD: <MOTDEPASSE_ADMIN>
          NEXTCLOUD_TRUSTED_DOMAINS=cloud.lageowcestshow.xyz
    ```

    - Dans la partie `environment` du service `app`, on met les infos de connexion à la base PostgreSQL externe.

=== "Les hébergeurs de l'extrême"

    ``` linenums="1" title="docker compose pour NextCloud - `docker-compose.yaml`"
    services:

      db:
        image: pgautoupgrade/pgautoupgrade:18-alpine
        container_name: nextcloud-db
        restart: unless-stopped
        volumes:
          - db_data:/var/lib/postgresql/data
        environment:
          POSTGRES_DB: nextcloud
          POSTGRES_USER: nextcloud
          POSTGRES_PASSWORD: <MOTDEPASSE>

      app:
        image: nextcloud:32
        container_name: nextcloud-app
        restart: unless-stopped
        ports:
          - 8123:80
        volumes:
          - /opt/nextcloud/data:/var/www/html
        environment:
          OVERWRITEPROTOCOL: https
          POSTGRES_HOST: db
          POSTGRES_DB: nextcloud
          POSTGRES_USER: nextcloud
          POSTGRES_PASSWORD: <MOTDEPASSE>
          NEXTCLOUD_ADMIN_USER: admin
          NEXTCLOUD_ADMIN_PASSWORD: <MOTDEPASSE_ADMIN>
          NEXTCLOUD_TRUSTED_DOMAINS=cloud.lageowcestshow.xyz

    volumes:
      db_data:
    ```

    - On utilise [l'image `pgautoupgrade`](https://hub.docker.com/r/pgautoupgrade/pgautoupgrade), qui aura la sympathie de mettre à jour les futures versions majeures de PostgreSQL en toutautomatique.
    - Les valeurs d'environment `POSTGRES_DB`, `POSTGRES_USER` et `POSTGRES_PASSWORD` doivent concorder, donc être les mêmes dans le service `db` et le service `app`.

<!-- markdownlint-enable MD046 -->

- La 1e partie des `ports` du service `app` représente le port interne sur lequel NextCloud écoutera, à réutiliser plus tard dans la conf nginx.

- Dans la clé `volumes` du service `app`, mettre le chemin du dossier qui hébergera tous les fichiers stockés sur l'instance.

### Configuration du serveur web nginx

Dans ce tuto on va utiliser [le serveur nginx](https://nginx.org/), qui va faire office de "reverse-proxy" : il va représenter le point d'entrée de l'application des requêtes en provenance des clients, et se chargera de rediriger ces requêtes vers l'applicatif NextCloud. C'est un peu [le videur-physionomiste](https://www.youtube.com/watch?v=mXUeHIGdN9c)...

- On créé un nouveau fichier pour configurer notre site NextCloud, dans `/etc/nginx/sites-available` :

``` linenums="1" title="/etc/nginx/sites-available/nextcloud.conf"
upstream nextcloud_upstream {
  server 127.0.0.1:8123;
}

server {
  listen 80;
  server_name cloud.lageowcestshow.xyz;
  client_max_body_size 2048M;
  return 301 https://$host$request_uri;
}

server {
  listen 443 ssl;
  server_name cloud.lageowcestshow.xyz;
  client_max_body_size 2048M;

  ssl_certificate /etc/letsencrypt/live/cloud.lageowcestshow.xyz/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/cloud.lageowcestshow.xyz/privkey.pem;

  location / {
    proxy_pass http://nextcloud_upstream;
    include proxy_params;
  }
}
```

!!! info "À noter que..."
    À noter que la valeur `client_max_body_size` représente la taille max des fichiers qui transiteront par nginx. Ne pas hésiter à mettre une valeur plus grande, si besoin.

!!! info "À noter que...²"
    À noter que cette conf redirige toutes les requêtes en HTTP plain vers le HTTPS. On s'assure ainsi que les communications avec le serveur NextCloud sont chiffrées.

- On créé [un lien sympbolique](https://fr.wikipedia.org/wiki/Lien_symbolique) vers le répertoire `/etc/nginx/sites-enabled` :

```sh
sudo ln -s /etc/nginx/sites-available/nextcloud.conf /etc/nginx/sites-enabled/nextcloud.conf
```

- On vérifie que le nginx est correctement configuré :

```sh
sudo nginx -t
```

S'il y a des erreurs, on avise, on corrige. Il est possible qu'un fichier `default.conf` - [1 crocodile, 2 crocodiles, 3 crocodiles](https://youtu.be/QUK2CMG1KqA?si=Zk0drT1AxbwMMvg9&t=94) - soit déjà là, si ce dernier n'a pas d'utilité, on peut le supprimer.

### Récupération des certificats

Maintenant, pour naviguer et synchroniser avec le NextCloud en utilisant du HTTPS, il nous faut des certificats TLS/SSL.

Pour cela, on utilise [Let's Encrypt](https://letsencrypt.org/), qui nous fournit ça gracieusement, et plus particulièrement [l'utilitaire `certbot` en mode _standalone_](https://certbot.eff.org/), ce qui nécessite d'éteindre nginx en amont.

- Arrêter le service nginx :

```sh
sudo systemctl stop nginx
```

- Récupérer un certificat pour notre domaine - le DNS doit être configuré correctement et pointer sur notre machine hôte :

```sh
sudo certbot certonly --standalone -d cloud.lageowcestshow.xyz
```

Si tout va bien, tant mieux : vous verrez un message de confirmation dans le terminal.

- On vérifie que nginx est correctement configuré, notamment concernant la configuration des chemins des certificats récupérés à l'étape précédente :

```sh
sudo nginx -t
```

Si tout est ok, on rallume le service nginx :

```sh
sudo systemctrl start nginx
```

Et voilà ! Nous avons maintenant un NextCloud fonctionnel :clap: !

![DiCaprio qui porte un toast avec une coupe de champagne](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/mise_en_place_nextcloud_autoheberge/dicaprio_toast_champagne.webp){: .img-center loading=lazy }

Vous pouvez vous rendre, dans votre navigateur web, sur l'URL de votre domaine pour la finalisation dans l'interface graphique - `cloud.lageowcestshow.xyz` dans notre cas.

![Écran d'accueil lors de la finalisation après la création d'un compte NextCloud](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/mise_en_place_nextcloud_autoheberge/nextcloud_init_welcome_apps.webp){: .img-center loading=lazy }

<!-- Footnotes reference -->
[^1]: _chépe_: format de données géo [_ancient_](https://dictionary.cambridge.org/dictionary/english/ancient), enterré au géocimetière ?

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
