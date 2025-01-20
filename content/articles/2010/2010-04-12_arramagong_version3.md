---
title: "Arramagong en version 3.0"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-04-12
description: "Arramagong en version 3.0"
tags:
    - open source
    - virtualisation
---

# Arramagong en version 3.0

:calendar: Date de publication initiale : 12 avril 2010

![Logo Arramagong](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/arramagong.png "logo Arramagong"){: .img-thumbnail-left }

Il y a peu, nous vous avions présenté [Arramagong](http://www.arramagong.com/Arramagong/home.html) qui permet de disposer d'un environnement virtuel complètement orienté SIG (cf [billet](http://geotribu.net/node/231)). Cette [initiative](http://wiki.osgeo.org/wiki/Live_GIS_Disc_GSoC_2010) de l'[OSGEO](http://www.osgeo.org/) vise à regrouper, au sein d'une distribution [Xubuntu 9.10](http://www.xubuntu.org/), l'ensemble des applications dont pourrait avoir besoin le géomaticien moderne. Une nouvelle version (v3) est désormais disponible, les nouveautés portent notamment sur :

- l'ajout de 14 nouvelles applications
- 13 mises à jour ...

Dans notre précédent billet, nous avions téléchargé [l'image iso](http://download.osgeo.org/livedvd/3.0-Final/Arramagong-Livedvd-v3-Final.iso.html). Cette fois-ci pour varier (et surtout parce que je me suis trompé lors du téléchargement) nous allons utiliser[l'image VMX](http://download.osgeo.org/livedvd/3.0-Final/Arramagong-LiveGIS-v3-Final.7z.html) (format VMware) et voir comment il est possible de l'utiliser avec [VirtualBox](http://www.virtualbox.org/).

## Téléchargement

La première des choses à faire est bien évidemment de la télécharger. Cela pouvant être assez long et soumis à des coupures, je vous conseille de passer en ligne de commande. Pour cela, il faut faire un :

`wget <http://tinyurl.com/osgeolive3-0rc6/Arramagong-LiveGIS-v3-Final.7z>`

Et si le téléchargement est interrompu, il vous suffit de le relancer en précisant à wget l'option `-c`:

`wget -c <http://tinyurl.com/osgeolive3-0rc6/Arramagong-LiveGIS-v3-Final.7z>`

## Conversion de l'image VMX en VDI

Une fois le fichier dézippé, vous disposez alors d'une image d'Arramagong au format VMX. Le problème étant, comment passer de ce format à celui de VirtualBox (VDI) ? Bien évidemment pour les utilisateurs de VMWare, cette étape est inutile. Comme le monde de l'OpenSource est bien fait, il existe une suite d'utilitaire permettant de réaliser cela.

La première étape consiste à transformer notre fichier VMX en BIN grâce à l'utilitaire [qemu](http://doc.ubuntu-fr.org/qemu). Cela se fait via la ligne de commande suivante :

`qemu-img convert Arramagong-LiveGIS-v3-Final.vmdk -O raw Arramagong-LiveGIS-v3-Final.bin`

Une fois muni de votre fichier BIN, nous allons maintenant le transformer en VDI (disk dur) en utilisant l'utilitaire vboxmanage fourni avec VirtualBox. Toujours en ligne de commande vous devez faire un :

`vboxmanage convertdd Arramagong-LiveGIS-v3-Final.bin Arramagong-LiveGIS-v3-Final.vdi`

Et voilà ! Quelques longues minutes plus tard, vous êtes en possession d'un nouveau disk dur sur lequel est Arramagong. Il suffit maintenant de l'ajouter depuis le Gestionnaire de Support Virtuel de VirtualBox. Le temps de lancer la machine et vous devriez voire alors apparaitre l'image ci-dessous.

![Arramagong](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/arramagong_V3.png "Arramagong"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->
