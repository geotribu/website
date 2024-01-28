---
title: Mise en place d'un QFieldCloud custom
subtitle: Du QField pour les gows et les gars sûr·e·s
authors:
    - Guilhem Allaman
categories:
    - article
comments: true
date: "2024-0X-XX 16:20"
description: QFieldCloud, l'abeille cool
icon: octicons/server-16
license: beerware
robots: index, follow
tags:
    - QField
    - QFieldCloud
    - debian
    - Q-ops
---

# Mise en place d'une instance QFieldCloud

:calendar: Date de publication initiale : _à déterminer_

Dans cet article, nous allons voir comment mettre en place un serveur QFieldCloud custom, qui permettra pour vos enquêtes et relevés terrain de synchroniser vos données entre `QGIS`, graĉe au plugin `QFieldSync`, et l'application `QField`, et ce sans avoir à brancher ni péter des câbles.

La doc se trouve :point_right: [ici](https://docs.qfield.org/zh/reference/qfieldcloud/concepts/) :point_left: et le dépôt :point_right: [ici](https://github.com/opengisch/qfieldcloud) :point_left:, merci de lire le `README` et d'y suivre les instructions #RTFM

Voilà, au revoir, merci, bon week-end et Joyeuses Pâques ! :beers: :dancers:

## Auteur {: data-search-exclude }

### Jean-Marc Jisse {: data-search-exclude }

![Portrait de Jean-Marc Jisse](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/mise_en_place_qfieldcloud_custom/jmg.webp){: .img-thumbnail-left}

Je m'appelle Jean-Marc Jisse, je suis le cousin un peu _tech_ de Jean-Claude Dusse, je dois mettre à jour mes refs, j'adore le jardinage et je déteste le bricolage !

<!-- markdownlint-disable MD026 MD041 -->
### Licence :fontawesome-brands-creative-commons: :fontawesome-brands-creative-commons-by: :fontawesome-brands-creative-commons-nc-eu: :fontawesome-brands-creative-commons-sa: {: id="license" data-search-exclude }

Ce contenu est sous licence [`PV`](https://poudreverte.org).

<!-- markdownlint-disable MD046 -->
??? quote "Détails"
    :trollface:

<!-- markdownlint-enable MD026 MD041 MD046 -->

----

NAN NAN ATTENDEZ !! PARTEZ PAS C4EST PAS FINI !

![gif de bob l'éponge et patrick en panique](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/mise_en_place_qfieldcloud_custom/bob_et_patrick.gif){: .img-center loading=lazy }

Bon allez, on reprend.

## Mise en place d'une instance QFieldCloud

Connaissez-vous [QField](https://qfield.org/) ? C'est comme David Copperfield le magicien, sauf que c'est pas de la magie ... enfin, si ! C'est de la magie ! Mais c'est pas ambiance au chaud, le Q vissé dans son siège, dans une salle avec des rideaux qui s'ouvrent, avec des chapeaux desquels sortent des lapins ... tout ça c'est la magie de [QFieldSync](https://plugins.qgis.org/plugins/qfieldsync/). QField, c'est de la magie plutôt ambiance dehors, avec gourde, sac-à-dos, casquette, lunettes, parce qu'y'a du monde partout, ça chauffe à l'arrière de la Modus _[...]_ là j'suis tranquille, j'passe vers le marché aux Puces, posé à la playa playa, avec tous les vaillants vaillants :point_up_2: :point_up:

Plus concrètement, il s'agit d'une application mobile de saisie et relevé terrain, hautement compatible avec QGIS, permettant de reproduire les paramétrages de saisie et formulaires des couches quasi à l'identique, poussée par [OPENGIS.ch](https://www.opengis.ch/) qu'on remercie pour tout le développement made with :love:. [Un précédent article](https://geotribu.fr/articles/2022/2022-05-24_releve_terrain_qfield/) explique plus en détail un processus de relevé grâce à l'appli QField qu'on ne présente dorénavant plus.

Maintenant, connaissez-vous Claude QField, la cousine un peu éloignée de Jean-Marc ? Euh non, pardon, "le cloud QField", ["QFieldCloud"](https://qfield.cloud/), _QFC_ pour les intimes. Aucun rapport avec _Quantum Fried Chicken_, même si on va voir qu'il est parfois question de _buckets_. QfieldCloud c'est LA brique qui permet de faire la liaison cloud entre QGIS et QField, faisant ainsi de ce tryptique un système robuste et complet d'enquête terrain. QFieldCloud offre entre autres la possibilité de synchroniser les données saisies dans QField directement dans l'application, grâce à un mode semi-offline bien articulé, qui permet de se libérer de pas mal de contraintes concernant le transfert de données PC - smartphone/tablette initialement filaire. Ainsi qu'un système de droits et d'accès aux projets qui permet de gérer finement la configuration et les permissions de plusieurs utilisateur/rices en lecture-écriture.

!!! info
    À ce moment de l'article, il est important de noter qu'il existe [ici](https://qfield.cloud/) une instance QFieldCloud "officielle" hébergée par OpenGIS. Qui propose une offre gratuite jusqu'à 100 MO de stockage. Ce qui peut s'avérer limité dès lors que les projets peuvent embarquer beaucoup de photos, et dont les projets privés ne permettent pas forcément la saisie par équipe/organisation ou par plusieurs utilisateur/rices. Pour celà il y a [les offres Pro et Organization](https://qfield.cloud/pricing.html) qui offrent plus de stockage et plus d'autres trucs. Voire la version "Private Cloud", soit l'hébergement custom d'une instance de serveur QFieldCloud, dont la mise en place, rendue possible grâce à l'ouverture du logiciel, est au coeur de cet article. Mais il faut savoir que mettre en place une propre instance suppose la charge d'un tas d'autres contraintes liées à l'hébergement: maintenance, montées de versions, backups ... Alors si vous aimez porter ceinture et bretelles, il vaut mieux privilégier l'instance officielle de QFieldCloud, ce qui aura en plus l'avantage de soutenir la boîte et pousser le développement de la solution. Sans oublier qu'une instance on-premise de QFieldCloud ne propose pas la belle page de configuration qu'on retrouve sur [app.qfield.cloud](https://app.qfield.cloud)...

## Infrastructure

Si vous êtes toujours là, c'est donc que vous n'aimez pas les ceintures et les bretelles. Un traumatisme survenu lors de la Fête de la Bière peut-être ? N'hésitez pas à partager vos aventures dans la partie commentaires.

À moins que ce soit des ****** de la cybersécurité qui vous aient dit "gnagnagna c'est nous qu'on doit héberger les données"... Bon, _toute ressemblance avec des situations existantes ou ayant existé serait purement fortuite_.

Pour le déploiement, on aura besoin d'un système Linux. On va partir sur une VM sous [debian 12](https://www.debian.org/releases/bookworm/). Si vous avez un gentil Service Informatique capable de vous fournir ça, vous pouvez gentiment leur demander. Ou alors en commander une chez votre hébergeur préféré, ce qui va être fait ici pour la suite, chez [un hébergeur bavarois](https://contabo.com/en/). Eh oui, vive la bière ! Vive les traumatismes !

Concernant les specs, pas forcément besoin de beaucoup de ressources, enfin tout dépend du nombre d'utilisateur/rices simultané/es que vous souhaitez pouvoir supporter. Ceci dit le côté asynchrone de QFieldCloud et le fonctionnement de la synchronisation en semi-offline le rend peu gourmand en ressources. Ici 4 CPU et 6GB de RAM nous suffiront.

Au niveau de l'espace de stockage, il nous faudra au grand minimum une vingtaine de GO. Prenons-en 100 pour être sûrs #CeintureEtBretelles. D'autant plus que nous verrons par la suite qu'il y a la possibilité de stocker nos données géo des projets QGIS (geopackages, photos ...) séparément du stockage principal du système QFieldCloud, via des buckets respectant le protocole "Simple Storage Service". Même si ici (spoiler) nous allons tout stocker sur le même serveur.

Il nous faudra également une entrée DNS qui pointe vers la VM. Ici ce sera une entrée de type `A` et le nom de domaine `"qfieldcloud.pennarmenez.com"` qui pointe vers la VM mise en place pour l'article.

## Installations

Une fois l'accès à la VM effectif, on s'y connecte via une [session ssh](https://fr.wikipedia.org/wiki/Secure_Shell). Commençons par créer un utilisateur pour gérer l'installation et le déploiement, auquel on donne le [sudo](https://www.sudo.ws/):

```bash
adduser --shell /bin/bash qfc
apt install -y sudo
usermod -aG sudo qfc
```

Il nous faudra ensuite installer [git](https://git-scm.com/), de sorte à pouvoir récupérer le dépôt QFieldCloud par la suite :

```bash
apt install -y git
```

Maintenant, il est nécessaire d'installer [docker](https://www.docker.com/), en suivant les instructions de [la doc officielle](https://docs.docker.com/engine/install/debian/) dont voici les commandes résumées, que vous pouvez copier-coller (le savoir-faire numero uno de tout/e développeur/se qui se respecte):

```bash
sudo apt-get install ca-certificates curl gnupg
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Docker (et [`compose`](https://docs.docker.com/compose/)) sont les outils de containerisation qui nous permettront de lancer les différents services nécessaires pour notre instance QFieldCloud, qu'il n'est pas recommandé de lancer en tant que `root`. C'est pourquoi on peut ajouter l'utilisateur `qfc` précédemment créé au groupe `docker` :

```bash
usermod -aG docker qfc
```

Puis on lance une session avec cet utilisateur via `su qfc`.

## Un zeste de RTFM

Suivons maintenant les instructions sur [le dépôt GitHub de QFieldCloud](https://github.com/opengisch/qfieldcloud) :

- récupérer le code du dépôt avec git :

```sh
# si vous avez renseigné une clé SSH/GPG sur votre compte GitHub
git clone --recurse-submodules git@github.com:opengisch/qfieldcloud.git

# si vous n'avez pas de clé SSH enregistrée
git clone --recurse-submodules https://github.com/opengisch/qfieldcloud.git
```

- basculer sur la branche de la dernière version, [`0.23.2`](https://github.com/opengisch/qfieldcloud/releases/tag/v0.23.2) à l'heure où sont écrites ces lignes :

```sh
cd qfieldcloud
git checkout -b v0.23.2
```

- copier le fichier `.env.local` vers un fichier `.env` qui va contenir toute la configuration du serveur :

```sh
cp .env.example .env
```

## Paramétrage

Jetons à présent un coup d':eyes: sur ce fichier `.env`, qui va contenir le gros de la configuration du serveur. Il s'agit d'une liste de variables d'environnement 2CRITES EN MAJUSCULES dont il nous faut adapter certaines :

- `ENVIRONMENT=production` : on passe en prod direct :metal: tester c'est douter

- `QFIELDCLOUD_HOST` : dans cette variable on met le nom de domaine utilisé pour l'instance QFieldCloud, "qfieldcloud.pennarmenez.com" dans notre cas

- `SECRET_KEY` : générer une clé et la mettre ici, via `pwgen 64` par exemple

- les variables qui commencent par `STORAGE_` font référence au _bucket_ compatible S3 dans lequel seront stockées les données géo : projets QGIS, geopackages, photos ... Il est possible d'utiliser un bucket de grande enseigne si vous le souhaitez, mais l'équipe de Geotribu vous propose d'utiliser un bucket frais, local et de saison avec [minio](https://min.io/). Qui possède en plus le (gros) avantage de ne rien avoir à changer au niveau de la config (sauf la variable `STORAGE_SECRET_ACCESS_KEY` bien sûr), étant donné que le dépôt de QFieldCloud propose la mise en place d'un service de buckets minio que nous allons voir dans la suite

- les variables qui commencent par `POSTGRES_` représentent les informations de connexion à la base de données postgres. Attention il ne s'agit pas d'une BD spatiale, qui aurait vocation à héberger des données SIG (la config par défaut en propose une, configurable avec les variables qui commencent par `GEODB_`). Il s'agit de la BD interne de QFieldCloud, qui contiendra les données des utilisateurs, des organisations, des équipes ... On peut donc allègrement ne rien changer à ce niveau-là, sauf le `POSTGRES_PASSWORD` bien sûr

- dans les variables qui commencent par `EMAIL_` on peut mettre les informations d'un serveur mél existant, ou les laisser telles quelles dans le cas où on ne souhaite pas utiliser de méls

- `COMPOSE_FILE=docker-compose.yml:docker-compose.override.standalone.yml`: il s'agit des fichiers "compose" qui déclarent les services en question de notre instance QFieldCloud. Zieutons-y un petit coup !

## Déploiement

Ces différents fichiers `docker-compose.*.yml` déclarent donc les différents services nécessaires à notre instance QFieldCloud. On remarque qu'il y en a plusieurs : le principal `docker-compose.yml`, qui contient les services "vitaux", qui vont être enrichis ("surchargés") par d'autres selon l'environnement que l'on souhaite : `dev`, `local`, `prod`, `test` ... et `standalone`, soit celui qu'on va mettre en place ici. Il s'agit d'un environnement autonome, qui offre tous les services nécessaires au bon fonctionnement de l'instance : stockage, BD postgres ...

**TODO** : adapter le paragraphe ci-dessous à l'évolution de [la PR d'override standalone](https://github.com/opengisch/qfieldcloud/pull/844)

```bash
cat > docker-compose.override.standalone.yml
```

Puis un bon CTRL+C / CTRL+V des familles avec le contenu de <https://github.com/opengisch/qfieldcloud/pull/844/files#diff-32a4168a7b1fcd63e4c0b12368085fea9e1aec07a103211409ad8538a27487b5>

## C'est parti :rocket:

Pour démarrer la musique et donner le signe à l'orchestre, un coup de baguette avec la commande suivante :

```bash
docker compose up -d --build
```

Cette commande va télécharger et/ou construire les _images docker_ utilisées pour les services, ce qui peut prendre quelques minutes et consommer de la bande passante (~10 GO).

<!-- markdownlint-disable MD040 -->
<!-- termynal -->

```sh
 ✔ Container qfieldcloud-mkcert-1                       Started
 ✔ Container qfieldcloud-memcached-1                    Running
 ✔ Container qfieldcloud-nginx-1                        Running
 ✔ Container qfieldcloud-mirror_transformation_grids-1  Started
 ✔ Container qfieldcloud-qgis-1                         Started
 ✔ Container qfieldcloud-app-1                          Running
 ✔ Container qfieldcloud-ofelia-1                       Running
 ✔ Container qfieldcloud-worker_wrapper-1               Running
 ✔ Container qfieldcloud-certbot-1                      Running
 ✔ Container qfieldcloud-geodb-1                        Running
 ✔ Container qfieldcloud-db-1                           Running
 ✔ Container qfieldcloud-minio-1                        Healthy
 ✔ Container qfieldcloud-createbuckets-1                Started
 ```

 <!-- markdownlint-enable MD040 -->
Une fois la commande terminée et tous les _containers_ dans le :white_check_mark:, nos services sont actifs et on peut passer à l'initialisation :

```bash
# appliquer les migrations pour créer la base de données interne
docker compose exec app python manage.py migrate

# collecter les fichiers web statiques
docker compose run app python manage.py collectstatic --noinput3

# créer le compte admin pour l'interface web, en remplaçant avec le nom d'utilisateur et le mél adéquat
docker compose run app python manage.py createsuperuser --username admin --email admin@mon.domain
```

:warning: la dernière commande ci-dessus va demander un mot de passe pour le compte super-utilisateur de notre instance QFieldCloud. Il pourrait être judicieux de noter quelque part ce mot de passe, par exemple sur un post-it, ou encore mieux sur votre poignet avec un feutre.

Pour vérifier l'état des composantes du serveur, la commande suivante doit normalement renvoyer des "ok" :

```bash
docker compose exec app python manage.py status
```

Normalement.

## Certificats SSL

Afin de pouvoir nous connecter à notre instance QFieldCloud en HTTPS, un certificat SSL il nous faut. Il est possible d'en récupérer un grâce à [Let's Encrypt](https://letsencrypt.org/) et son utilitaire en ligne de commande `certbot` :

```bash
apt install certbot
source .env
certbot certonly --standalone -d ${QFIELDCLOUD_HOST}
```

:warning: à noter que pour pouvoir récupérer un certificat avec la commande ci-dessus, il est nécessaire que le port 80 soit libre, et donc que nos services QFieldCloud soient éteints. Pour celà, voici l'interrupteur :

```bash
# nuit
docker compose down --remove-orphans

# jour
docker compose up -d --build
```

Une fois le certificat généré, il nous faut à présent le copier dans la config de QFieldCloud :

```bash
sudo cp /etc/letsencrypt/live/${QFIELDCLOUD_HOST}/privkey.pem ./conf/nginx/certs/${QFIELDCLOUD_HOST}-key.pem
sudo cp /etc/letsencrypt/live/${QFIELDCLOUD_HOST}/fullchain.pem ./conf/nginx/certs/${QFIELDCLOUD_HOST}.pem
```

Après avoir relancé les services, normalement le serveur doit maintenant être fonctionnel et prêt à l'emploi. Normalement.

En tappant l'URL de votre nom de domaine en HTTPS dans un navigateur, l'interface web d'admin est maintenant disponible :

![Écran de connexion à l'interface d'admin web](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/mise_en_place_qfieldcloud_custom/qfieldcloud_admin_login.webp){: .img-center loading=lazy }

## Configuration dans l'interface web

C'est dans cette interface - l'interface d'admin de [Django](https://www.djangoproject.com/) soit le framework utilisé par QFieldCloud - que nous allons créer les utilisateurs, les organisations, les équipes, et assigner les droits sur les projets. Les projets sont eux créés directement dans QGIS grâce au plugin QFieldSync.

Voyons maintenant comment créer notre première utilisatrice : il faut nous rendre dans la partie people :notes: people have the power :notes: puis cliquer sur "Add person" en-haut à droite :

![Écran de création d'un utilisateur dans l'interface web d'admin](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/mise_en_place_qfieldcloud_custom/qfieldcloud_create_user.webp){: .img-center loading=lazy }

À noter que la case "Staff status" permet à ce/tte people de pouvoir se connecter à l'interface d'admin web. Combiné à une gestion des droits d'admin via la partie "Groups", celà peut permettre de créer des groupes d'admins avec des droits spécifiques et ce sans avoir à utiliser le super user principal.

P.S. : _le mot de passe de Jane est 4 fois la répétition, en minuscules, du nom d'un logiciel bureautique SIG stylay, avec entre chaque des underscores :eyes:. Si vous avez trouvé vous pouvez essayer [ici](https://qfieldcloud.pennarmenez.com/admin/login).

## Création d'un projet QGIS

Créons maintenant un projet pour tester un tant soit peu notre setup. Il faudra d'abord se connecter à notre instance QFC dans le plugin QFieldSync. Pour celà, cliquer deux fois sur l'abeille cool dans l'interface de connexion et renseigner l'URL de l'instance de même que login / mot de passe :

![Écran de connexion du plugin QFieldSync](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/mise_en_place_qfieldcloud_custom/qfieldsync_login.webp){: .img-center loading=lazy }

Ensuite créer un projet bateau puis le téléverser grâce au bouton "Create new project"

![Écran d'un projet QFieldCloud dans QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/mise_en_place_qfieldcloud_custom/screenshot_qgis_qfc_project.webp){: .img-center loading=lazy }

Le projet apparaît maintenant dans la liste, et même dans les signets "QFieldCloud" de l'explorateur QGIS !

Dans l'application mobile QField, même chose: on clique sur l'abeille ya 2 fois pour pouvoir rentrer l'URL de l'instance et le login / mot de passe :

![Écran de connexion de l'appli QField](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/mise_en_place_qfieldcloud_custom/qfield_login.webp){: .img-center loading=lazy }

Une fois le projet téléchargé dans la liste puis ouvert, c'est parti pour la saisie !

![Écran d'un projet QFieldCloud dans QField](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/mise_en_place_qfieldcloud_custom/screenshot_qfield_qfc_project.webp){: .img-center loading=lazy }

:sparkles: Magie magie ! :sparkles:

![David CopperQField](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/mise_en_place_qfieldcloud_custom/david_copperqfield.webp){: .img-center loading=lazy }

:sleepy: N.B. : il est possible que lors du téléchargement sur le mobile, un message d'erreur comportant la mention "subscription inactive" apparaisse, empêchant par là la possibilité de récupérer le projet. Pour régler celà, il faut se connecter au serveur et rentrer les commandes suivantes de sorte à corriger le statut des souscriptions :

```bash
# se connecter en bash dans le container de la base de données interne
docker exec -it qfieldcloud-db-1 /bin/bash

# se connecter à la base de données avec psql en rentrant le mot de passe renseigné dans le fichier .env
psql -U qfieldcloud_db_admin qfieldcloud_db
```

Puis en SQL, changer le statut des subscriptions :

```sql
UPDATE subscription_subscription SET status = 'active_paid';
```

## Et maintenant ?

Et maintenant ? Nous venons de voir comment mettre en place une instance QFieldCloud fonctionnelle sur un serveur linux, nous permettant de synchroniser aisément les données entre QGIS et QField. Mais ... vous vous souvenez ? La Fête de la Bière ? La ceinture et les bretelles ?

![gif de bob l'éponge et patrick en panique](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/mise_en_place_qfieldcloud_custom/bob_et_patrick.gif){: .img-center loading=lazy }

Les backups, les maintenances, les montées de version ... ne font pas l'objet de cet article. Pourquoi ne pas s'entourer de vrai/es expert/es sur ce domaine purement IT ? Il y a des boîtes qui proposent ces services et qui permettent de se soulager de ces contraintes. Car après tout, qui de mieux que _votre partenaire QField_ pour s'occuper de _votre QField_ ?

## Auteur

--8<-- "content/team/gall.md"

{% include "licenses/beerware.md" %}
