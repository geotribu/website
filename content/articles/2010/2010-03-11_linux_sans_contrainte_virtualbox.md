---
title: "Linux sans contrainte grace à VirtualBox"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-03-11
description: "Linux sans contrainte grace à VirtualBox"
tags:
    - Linux
    - open source
    - VirtualBox
---

# Linux sans contrainte grace à VirtualBox

:calendar: Date de publication initiale : 11 mars 2010

![icône globe](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "icône globe"){: .img-thumbnail-left }

Il peut être agréable, quand vous testez de nouvelles applications, de ne pas avoir à les installer sur votre environnement de travail. En effet, il peut arriver que celles-ci ne soient pas encore complètement stables ou bien qu'il soit nécessaire de les compiler.  
De ce fait, cela peut rendre votre environnement instable et conduire à une réinstallation complète de votre système.

C'est pourquoi, je préfère maintenant utiliser un [système virtualisé](https://fr.wikipedia.org/wiki/Virtualisation). Dans les faits, il s'agit simplement de faire tourner, sur une machine physique, un logiciel qui va émuler une ou plusieurs machines virtuelles. Ainsi, même si j'effectue une mauvaise manipulation ou que mon système virtualisé est corrompu, cela n'entraine aucune conséquence sur mon environnement de travail.

Concrètement comment cela se passe? Pour cela vous avez besoin de deux composantes. Tout d'abord, le logiciel qui va permettre la virtualisation et ensuite l'image virtuel. Côté logiciel, j'utilise [virtualbox](http://doc.ubuntu-fr.org/virtualbox) qui est téléchargeable directement depuis les dépôts d'Ubuntu. Ensuite, il suffit de vous rendre sur le site [virtualboxes](http://virtualboxes.org/) qui propose plus d'une dizaine [d'images](http://virtualboxes.org/images/) de distributions linux. Enfin, une fois les paramètres de votre nouvel environnement définis, il ne reste qu'à émuler l'image. Et voilà, le tour est joué.

![VirtualBox](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/800px-VirtualBox2.png "VirtualBox"){: .img-center loading=lazy }

Source : [Wikipedia](https://fr.wikipedia.org/wiki/Fichier:VirtualBox2.png)

Ainsi, en à peine le temps d'un téléchargement, vous avez à votre disposition un environnement complet vous permettant de travailler ou, comme moi, de faire vos tests. A noter que, pour ceux qui souhaiteraient disposer d'un environnement SIG, vous pouvez utiliser [Arramagong](http://www.arramagong.com/Arramagong/home.html) basé sur Xubuntu ou encore [GISvm](http://geotribu.net/node/190) basé sur Ubuntu.

----

<!-- geotribu:authors-block -->
