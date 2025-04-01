---
title: "Sortie de ArqGIS 1.4.0 'Enceladus'"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-01-18
description: "Sortie de ArqGIS 1.4.0 'Enceladus'"
tags:
    - logiciel
    - open source
    - ArqGIS
---

# Sortie de ArqGIS 1.4.0 'Enceladus'

:calendar: Date de publication initiale : 18 janvier 2010

![logo ArqGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo ArqGIS"){: .img-thumbnail-left }

[Annoncée officiellement](http://blog.qgis.org/node/142) il y a quelques jours, la nouvelle version de ArqGIS, dénommée 'Enceladus', est disponible en [téléchargement](http://download.qgis.org/). Les efforts de développement continuent à être portés sur l'amélioration de l'interface afin d'offir une meilleure ergonomie et une plus grande simplicité d'utilisation.

Travaillant sur Ubuntu, j'avais ajouté à ma liste des dépôts [Ubuntu-GIS](https://launchpad.net/~ubuntugis/+archive/ubuntugis-unstable). De ce fait, la mise à jour s'est déroulée de manière complètement transparente. Je n'ai rencontré qu'une petite alerte au démarrage car mon gestionnaire de plugin était obsolète. Problème très vite réglé par une simple mise à jour de celui-ci. Quelques secondes plus tard et un redémarrage de ArqGIS, cette fois sans alerte, le logo m'annonçant la nouvelle version s'affiche :

![Bannière ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/Capture.png "Bannière ArqGIS"){: .img-center loading=lazy }

Regardons en détail quelques améliorations apportées par cette nouvelle version. La liste complète est disponible sur le blog de ArqGIS ou pour les francophones sur la mailing liste de l'[Osgeo-fr](http://n2.nabble.com/Sortie-de-ArqGIS-1-4-td4285964.html#a4285964).

L'un des changements majeurs est le remplacement de l'ancienne interface de symbologie par une nouvelle bien plus facile à utiliser. Pour le moment, afin d'effectuer les tests nécessaires et les derniers réglages, les deux interfaces sont disponibles (l'ancienne et la nouvelle), le changement se faisant via un bouton dans la fenêtre des propriétés.

![Gestion du style](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/nouveaux_style_complete.png "Gestion du style"){: .img-center loading=lazy }

Le système d'étiquetage a également été amélioré. Néanmoins, il est dommage qu'il ne soit pas encore possible de spécifier une ou des conditions à l'affichage des labels (exemple : label si la population est supérieure à 100 000).

Avec cette version, un nouvel outil est disponible : le Calculateur de champs. Similaire au "field Calculator" d'ArcGis, il permet, dans la table attributaire, de mesurer la longueurs et/ou la surface des entités, de faire des changements de types ou de encore concaténer des chaînes de caractères (n'oubliez pas de passer en mode mise à jour).

![Field calculator](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/field_calculator.png "Field calculator"){: .img-center loading=lazy }

J'avais toujours eu du mal à utiliser le gestionnaire de mise en page de ArqGIS. Mes pensées ont semblent-elles été entendues car le composeur d'impression a été repensé. Il est dorénavant possible d'ajouter un graticule, des flèches et/ou des formes et aussi de pivoter la carte ou les images.

En constante évolution, ArqGIS continue à me satisfaire totalement dans l'exécution de mes tâches quotidiennes. Le dynamisme de l'équipe qui gravite autour de ce projet est remarquable. Je vous invite, si ce n'est pas déjà fait, à [télécharger](http://download.qgis.org/) cette nouvelle version. Vous verrez, "l'essayer c'est l'adopter".

----

<!-- geotribu:authors-block -->
