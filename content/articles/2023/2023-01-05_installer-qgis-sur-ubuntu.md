---
title: Installer QGIS sur Ubuntu avec apt
subtitle: apt install qgis-zen-mode
authors:
    - Julien MOURA
categories:
    - article
    - tutoriel
comments: true
date: 2023-01-05
description: Installer QGIS sur la distribution la plus répandue de l'écosystème Linux pose encore question, voire des problèmes. Un tutoriel sur la marche à suivre pour s'en rappeler quand le besoin se fait sentir.
icon: fontawesome/brands/ubuntu
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/qgis_installation_ubuntu/qgis_ubuntu_linux.png
license: beerware
tags:
    - Linux
    - QGIS
    - Ubuntu
---

# Installer QGIS sur Ubuntu, le pense-bête simple et efficace

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

!!! info ""
    À l'occasion de la publication de [sa version traduite en anglais](https://blog.geotribu.net/2025/02/11/installing-qgis-on-ubuntu-with-apt/), l'article a été mis à jour début février 2025 avec QGIS 3.34 LTR et Ubuntu 24.04 LTS.

## Introduction

![logo Ubuntu](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/ubuntu.svg "logo Ubuntu"){: loading=lazy .img-thumbnail-left }

Ça peut paraître idiot dit comme ça, mais je trouve qu'installer le logiciel SIG open source le plus utilisé sur la distribution la plus répandue de l'écosystème Linux pose encore question, voire des difficultés, y compris à des utilisateurs quotidiens des deux outils.

Il faut dire que les notions de dépôts, de paquets, de clés d'authentification etc. ne sont pas faciles à appréhender, surtout quand notre métier c'est de faire de la géomatique, pas de l'administration système ou du packaging.

![Géographe domptant un pingouin](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/qgis_installation_ubuntu/geographe_contre_linux_dall-e.webp "Géographe domptant un pingouin - Crédits : DALL·E"){: .img-center loading=lazy }

Par ailleurs, en plus d'un site officiel de QGIS peu lisible sur la partie installation, en tout cas pour un utilisateur non développeur ou linuxien aguerri, le projet opère régulièrement des changements normaux dans le cycle de vie logicielle, peu visibles mais qui impactent les utilisateurs finaux lambda.

Enfin, on ne va pas râler puisque c'est gratuit, qu'on n'est pas le produit et qu'il n'y a rien de plus susceptible et légitime qu'un bénévole ! Et je sais de quoi je parle :wink: !

Comme je n'installe ni ne réinstalle QGIS tous les 4 matins, je me note la procédure ici histoire de pouvoir la retrouver et la partager facilement.  
Vu que c'est un sujet vivant, je tenterai de mettre ce tutoriel à jour de temps à autre mais n'hésitez pas à signaler un souci ou à [proposer un ajustement](https://contribuer.geotribu.fr/edit/fix_content_from_website/).

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Prérequis

- des droits d'installation
- une connexion internet ouverte sur <https://qgis.org/> et capable d'avaler 1 497 Mo sans s'étouffer, même après les fêtes de fin d'année

----

## Choix

Avant d'installer, sonne l'heure du choix : quelle version de QGIS ?

Pour ma part, je cherche à installer **QGIS LTR** (3.34.15 à date) sur **Ubuntu LTS** (24.04.1 à date) via **le dépôt officiel** des paquets du projet QGIS.

Oui, j'aime la stabilité.  
Oui, le [dépôt `ubuntugis-unstable`](https://wiki.ubuntu.com/UbuntuGIS) porte bien son nom.  
Non, les versions non LTR ne sont pas suffisamment stables, surtout celles qui ont moins de 6 correctifs (le dernier chiffre dans le numéro de version).  
Je n'ai pas les dernières fonctionnalités qui font le buzz sur les sites qui font de la veille, j'ai des versions de GDAL et de PROJ plus vieilles que ma fille... mais chez moi, ça marche(tm) :sunglasses:.  
Et je peux travailler en tout zénitude sans me demander si la prochaine mise à jour va casser quelque chose. :person_in_lotus_position:

![Les gens qui installent QGIS non LTR](https://media.giphy.com/media/nneVpy2YnHZNm/giphy.gif "Les gens qui installent QGIS non LTR"){: .img-center loading=lazy }

> :person_juggling: Les personnes qui installent la version de QGIS non LTR et sans correctif :person_juggling:
{: align=middle }

!!! note "Disponibilité des versions"
    Notez que la version de votre distribution est également importante puisque toutes les versions de QGIS ne sont pas packagées et dsitribuées pour toutes les versions des distributions, notamment pour des questions de dépendances incompatibles ou manquantes. Par exemple, sur une base Ubuntu 20.04, on ne trouve pas de version de QGIS au-delà de la 3.22. Voir [ce commentaire](#isso-239) et sa réponse.

----

## Dépendances

On commence par installer le nécessaire pour les différentes étapes d'installation, en considérant que la machine est neuve ou tout comme. Si l'état de votre ordinateur vous évoque d'antiques écuries [faites donc un coup de propre](#nettoyage) avant de continuer.

On met à jour et on installe la trousse à outils de base via le terminal :

```sh
sudo apt update
sudo apt install ca-certificates gnupg lsb-release software-properties-common
```

----

## Ajout du dépôt officiel

Première étape : on ajoute le PPA officiel du projet QGIS. C'est là que les gentils packageurs du projet QGIS pour Debian et dérivés (dont Ubuntu donc) publient les paquets liés au projet.

### Authentification du dépôt

Pour pouvoir installer quoique ce soit depuis ce dépôt, il faut pouvoir l'authentifier auprès du système.

On va donc télécharger la clé d'authentification du PPA à l'endroit qui va bien, c'est-à-dire dans le dossier dédié aux trousseaux d'authentification du gestionnaire de paquets :

```sh
sudo mkdir -p /etc/apt/keyrings
sudo wget -O /etc/apt/keyrings/qgis-archive-keyring.gpg https://download.qgis.org/downloads/qgis-archive-keyring.gpg
```

### Référencement du dépôt dans la liste des sources de paquets

On référence ensuite le dépôt dans un fichier chargé de lister les sources de paquets et qui sera dédié à QGIS `/etc/apt/sources.list.d/qgis.list` :

<!-- markdownlint-disable MD046 -->
=== ":person_in_lotus_position: QGIS LTR"

    ```sh
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/qgis-archive-keyring.gpg] https://qgis.org/ubuntu-ltr \
    $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/qgis.list > /dev/null
    ```

    On vérifie que le fichier a bien été écrit :

    ```sh
    less -F /etc/apt/sources.list.d/qgis.list
    ```

    Ce qui donne sur Ubuntu 24.04 :

    ```debsources title="/etc/apt/sources.list.d/qgis.list"
    deb [arch=amd64 signed-by=/etc/apt/keyrings/qgis-archive-keyring.gpg] https://qgis.org/ubuntu-ltr noble main
    ```

=== ":person_juggling: QGIS, version 'basique'"

    ```sh
    echo \
    "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/qgis-archive-keyring.gpg] https://qgis.org/ubuntu \
    $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/qgis.list > /dev/null
    ```

    On vérifie que le fichier a bien été écrit :

    ```sh
    less -F /etc/apt/sources.list.d/qgis.list
    ```

    Ce qui donne sur Ubuntu 24.04 :

    ```debsources title="/etc/apt/sources.list.d/qgis.list"
    deb [arch=amd64 signed-by=/etc/apt/keyrings/qgis-archive-keyring.gpg] https://qgis.org/ubuntu noble main
    ```

<!-- markdownlint-enable MD046 -->

#### Alternative : le fichier `qgis.sources`

Il existe une autre façon de référencer le dépôt dans la liste des sources. Les informations stockées sont les mêmes mais elles ne sont pas structurées de la même façon.

On référence alors dans un fichier `/etc/apt/sources.list.d/qgis.sources` :

<!-- markdownlint-disable MD046 -->
=== ":person_in_lotus_position: QGIS LTR"

    ```sh
    echo \
    "Types: deb deb-src
    URIs: https://qgis.org/ubuntu-ltr
    Suites: $(lsb_release -cs)
    Architectures: amd64
    Components: main
    Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg" | sudo tee /etc/apt/sources.list.d/qgis.sources > /dev/null
    ```

    On vérifie que le fichier a bien été écrit :

    ```sh
    less -F /etc/apt/sources.list.d/qgis.sources
    ```

    Ce qui donne sur Ubuntu 24.04 :

    ```yaml title="/etc/apt/sources.list.d/qgis.sources"
    Types: deb deb-src
    URIs: https://qgis.org/ubuntu-ltr
    Suites: noble
    Architectures: amd64
    Components: main
    Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
    ```

=== ":person_juggling: QGIS, version 'basique'"

    ```sh
    echo \
    "Types: deb deb-src
    URIs: https://qgis.org/ubuntu
    Suites: $(lsb_release -cs)
    Architectures: amd64
    Components: main
    Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg" | sudo tee /etc/apt/sources.list.d/qgis.sources > /dev/null
    ```

    On vérifie que le fichier a bien été écrit :

    ```sh
    less -F /etc/apt/sources.list.d/qgis.sources
    ```

    Ce qui donne sur Ubuntu 24.04 :

    ```yaml title="/etc/apt/sources.list.d/qgis.sources"
    Types: deb deb-src
    URIs: https://qgis.org/ubuntu
    Suites: noble
    Architectures: amd64
    Components: main
    Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
    ```
<!-- markdownlint-enable MD046 -->

----

## Installation de QGIS

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-thumbnail-left }

Allez, tout est désormais fin prêt, on passe à l'installation !

On met à jour la liste des paquets accessibles depuis qu'on a ajouté le dépôt :

```sh
sudo apt update
```

Pour savoir quels paquets liés à QGIS sont disponibles, on commence à taper `sudo apt install qgis` et on laisse faire l'autocomplétion via la touche ++tab++ :

```sh title="Lister les packages installables et dont le nom commence par 'qgis'"
$ sudo apt install qgis
qgis                      qgis-plugin-grass-common  qgis-server-common        qgis-server-wms
qgis3-survex-import       qgis-provider-grass       qgis-server-dummy         qgis-server-wmts
qgis-api-doc              qgis-providers            qgis-server-landingpage   qgis-sip
qgis-common               qgis-providers-common     qgis-server-wcs  
qgis-dbg                  qgis-server               qgis-server-wfs  
qgis-plugin-grass         qgis-server-bin           qgis-server-wfs3
```

![Paquets commençant par qgis disponibles](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/qgis_installation_ubuntu/ubuntu_apt_install_qgis_autocompletion.webp){: .img-center loading=lazy }

Sauf à avoir des besoins particuliers, il est toujours préférable de n'installer que le minimum utilisé. Dans mon cas, ce sera donc `qgis`... et c'est amplement suffisant, car ça fait déjà du monde :

![Dépendances tirées par une installation de QGIS sur Ubuntu](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/qgis_installation_ubuntu/ubuntu_apt_install_qgis_dependances.webp){: .img-center loading=lazy }

----

## Nettoyage

Parfois, que ce soit suite à une mise à jour de la distribution, à une mauvaise manip ou en ayant copié/collé une commande depuis un tuto comme celui-ci sans avoir vraiment cherché à comprendre, tout est cassé. Il est alors temps de faire le grand ménage.

![GIF technique terre brûlée](https://media.tenor.com/fQmZ_N0b57kAAAAC/kaamelott-leodagan.gif){: .img-center loading=lazy }

On désinstalle QGIS :

```sh
sudo apt --purge remove qgis*
```

Si jamais vous avez joué à un moment avec un dépôt exotique tel `ubuntugis`, il est aussi recommandé de désinstaller toute dépendance liée à QGIS, notamment GDAL et PROJ dont les conflits de versions peuvent jouer des tours au détours de certains traitements spatiaux :

```sh
sudo apt --purge remove gdal-* proj-*
```

On supprime ensuite les références au dépôt de QGIS qui peuvent encore traîner dans le fichier des sources principales.  
Pour cela, on ouvre le fichier :

```sh
sudo nano /etc/apt/sources.list
```

Et on supprime toutes les lignes qui contiennent une référence à QGIS. Toutes. On quitte l'éditeur avec ++ctrl+x++ puis ++o++ pour confirmer.

Puis on finit de lessiver les murs et sols :

```sh
sudo rm /etc/apt/sources.list.d/qgis*
sudo apt autoremove
sudo apt update
```

On aère un peu et on repart sur [le début de la procédure](#dependances).

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}

## Crédits {: data-search-exclude }

- l'image d'en-tête est récupérée du site [Instrutor GIS](https://www.instrutorgis.com.br/)

<!-- abbréviations spécifiques -->
*[PPA]: Les  PPA, pour Personal Package Archive, sont des dépôts de paquets caractéristiques des distributions basées sur Debian et qui permettent d'installer des logiciels qui ne sont pas disponibles dans les dépôts officiels d'une distribution (Ubuntu dans notre cas).
