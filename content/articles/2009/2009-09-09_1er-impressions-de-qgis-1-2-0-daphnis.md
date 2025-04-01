---
title: "Premières impressions de QGIS 1.2.0 - Daphnis"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-09-09
description: "Premières impressions de QGIS 1.2.0 - Daphnis"
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_1-2_daphnis_splash_screen.png"
tags:
    - logiciel
    - open source
    - Python
    - QGIS
---

# Premières impressions de QGIS 1.2.0 - Daphnis

:calendar: Date de publication initiale : 09 septembre 2009

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-thumbnail-left }

Suite à [l'annonce](http://geotribu.net/node/154) de la nouvelle version de QGIS (1.2.0) et après avoir installé celle-ci, j'ai réalisé quelques rapides tests et vous livre ici mes impressions.

## Mise à jour ou installation

La nouvelle version de QGIS est d'ores et déjà disponible en [téléchargement](http://qgis.org/en/download/current-software.html) sur la quasi-totalité des plates-formes (Linux, Mac, Ubunutu). Travaillant sur Ubuntu, il m'a suffi d'ajouter le dépôt [Ubuntu-GIS](https://launchpad.net/~ubuntugis/+archive/ubuntugis-unstable) afin de pouvoir en disposer. Synaptic, le gestionnaire de paquets d'Ubuntu, m'a alors proposé de mettre à jour ma version 1.0 de QGIS vers la 1.2. Une fois celle-ci réalisée, je lance alors mon application, dont le nouveau logo, au ton de rouge, s'affiche alors.

Après quelques rapides tests et réglages (suppression de mon répertoire `.qgis` dans mon home) la seule erreur à laquelle j'ai été confronté fut la fermeture inopinée de QGIS lors de l'activation du plugin GRASS. Heureusement pour moi, un simple `apt-get update` puis `upgrade` a suffi à régler ce malencontreux dysfonctionnement.

![QGIS Daphnis](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_1-2_daphnis_splash_screen.png "QGIS Daphnis"){: .img-center loading=lazy }

## Plugin OSM

Dans la [liste des changements](http://blog.qgis.org/node/137), j'avais noté qu'un nouveau plugin permettant de travailler sur les données d'OpenStreetMap (OSM) était disponible. Une fois celui-ci installé puis activé grâce au plugin manager de QGIS, un nouveau tableau de bord regroupant les options habituelles d'OSM (téléchargement ou chargement des données...) apparaît. Je sélectionne donc la zone qui m'intéresse et télécharge les données correspondantes depuis le serveur d'OSM.

![Plugin OSM](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/OSM_PLUGIN.png "Plugin OSM"){: .img-center loading=lazy }

J'explore rapidement les fonctionnalités de ce nouvel outil mais rencontre malheureusement quelques difficultés. En effet, lorsque je souhaite modifier le tracé d'une rue, QGIS tente alors de "snapper" automatiquement le sommet que je suis en train de déplacer vers le sommet voisin le plus proche. Peut-être est-ce simplement une question de réglage, mais au niveau ergonomie et possibilité, il y a encore un peu de travail avant d'arriver au niveau de JOSM. De plus au niveau de la symbologie, quelque soit celle que j'adopte, QGIS refuse de coloriser les routes ayant pour valeur unclassified.

![Plugin OSM - Erreurs](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/errors.png "Plugin OSM - Erreurs"){: .img-center loading=lazy }

Par contre, je trouve que l'affichage des informations sous la forme d'une table rend le travail, sur les attributs, plus lisible. De plus, tout comme dans JOSM, QGIS suggère les valeurs possibles lors de l'ajout d'un nouveau tag ou d'une nouvelle valeur.

![Plugin OSM - Table attributaire](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/table_attributaire.png "Plugin OSM - Table attributaire"){: .img-center loading=lazy }

Je réalise quelques légères modifications et valide ensuite mon travail. Avant d'uploader mes données sur le serveur d'OSM, QGIS affiche une boite de dialogue me permettant de décrire les changements effectués ainsi que de spécifier mon nom d'utilisateur et mon mot de passe.

![Plugin OSM - Upload](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/osm_upload.png "Plugin OSM - Upload"){: .img-center loading=lazy }

Même si JOSM, grâce à l'éventail de ces fonctionnalités et à son antériorité, garde une nette longueur d'avance, l'arrivée de ce nouveau plugin permet pour les géomaticiens de disposer d'un outil tout en un. Pour ma part et toujours dans l'idée de disposer d'un logiciel tout-en-un, j'ai essayé de connecter mon GPS à l'ordinateur et de piloter celui-ci directement depuis QGIS grâce au plugin GPS qui s'appuie sur la librairie [GPSBabel](http://www.gpsbabel.org/). Cette tentative s'est malheureusement soldée par un échec du fait de la non-prise en charge de mon récepteur par GPSBabel.

## Amélioration des outils d'édition

Cette nouvelle version apporte une nette amélioration de la prise en charge des objets multiples et des polygones à trou. De plus, l'outil de simplification m'a particulièrement impressionné. Une fois celui-ci activé, il suffit de sélectionner l'objet auquel on souhaite appliquer la transformation ainsi que le degré de simplification pour voir les modifications se faire en temps réel. Au niveau ergonomie, je n'ai rien à dire c'est parfait !

![Simplification](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/simplification.png "Simplification"){: .img-center loading=lazy }

### Changement de l'interface de l'outil permettant l'ouverture des couches vecteurs

Ce n'est certes pas une amélioration majeure mais je trouve que la nouvelle interface est bien plus sympathique et intuitive. De plus, il est dorénavant possible d'ouvrir toutes les données contenues dans un dossier, plutôt sympa non?

![Ajouter une couche vecteur](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/file.png "Ajouter une couche vecteur"){: .img-center loading=lazy }

### Conclusion

Cette nouvelle version de QGIS apporte son lot de nouveautés et de surprises. Je reste conquis par ce logiciel comparable, par ses fonctionnalités, à MapInfo ou GeoConcept. L'API disponible depuis la version 1.0 lui à permis d'élargir considérablement sa communauté et d'augmenter ainsi le nombre de plugins disponibles. En conclusion, ce véritable outil métier est à mettre entre toutes les mains.

----

<!-- geotribu:authors-block -->
