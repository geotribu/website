---
title: Publication d'un site avec les icônes QGIS
subtitle: Et tout totomatique svp !
authors:
    - Julien MOURA
categories:
    - article
comments: true
date: 2023-03-24
description: 'Pour faciliter le travail d''intégration des icônes de QGIS par les développeurs de plugins, j''ai automatisé la génération et la mise à jour d''un site web : PyQGIS Icons Cheatsheet.'
image: https://pyqgis-icons-cheatsheet.geotribu.fr/assets/images/social/index.png
license: beerware
robots: index, follow
tags:
    - icônes
    - interface graphique
    - plugin
    - PyQGIS
    - PyQt5
    - QGIS
---

# Geotribu vous présente le site PyQGIS Icons Cheatsheet

:calendar: Date de publication initiale : 24 mars 2023

![logo PyQGIS](https://cdn.geotribu.fr/img/logos-icones/programmation/pyqgis.png){: .img-thumbnail-left }

En janvier 2021, je publiais un article pour encourager les développeurs de plugins QGIS à (ré)utiliser les icônes intégrées pour enrichir leurs interfaces graphiques sans effort (ni talent): [Utiliser les icônes intégrées de QGIS pour égayer ses plugins](../2021/2021-01-19_pyqgis_utiliser_icones_integrees.md).  
Un mois plus tard, je donnais une recette technique pour extraire automatiquement les icônes depuis le fichier de ressource directement depuis les sources du projet : [Récupérer et prévisualiser les icônes intégrées à QGIS](../2021/2021-02-02_pyqgis_previsualiser_images_integrees.md).

Cette année, dans le même élan que [le nettoyage des contenus de Geotribu](2023-01-30_voeux-geotribu-2023.md#nettoyage-et-historique), j'ai pris le temps d'extraire le tableau des icônes pour en faire un site dédié et surtout d'en automatiser complètement la (re)génération histoire qu'il reste à jour avec le projet QGIS sans que cela ne me coûte en maintenance (bénévolat tout ça...).

Je vous présente donc PyQGIS Icons Cheatsheet :

[![PyQGIS Icons Cheatsheet](https://pyqgis-icons-cheatsheet.geotribu.fr/assets/images/social/index.png){: .img-center .off-glb loading=lazy }](https://pyqgis-icons-cheatsheet.geotribu.fr/)

----

## Un site tout totomatique

En soi, le site n'est pas bien différent de la page que j'avais publiée ici suite à mon deuxième article ([voir dans Web Archive](https://web.archive.org/web/20211024083001/https://geotribu.fr/toc_nav_ignored/qgis_resources_preview_table/)), sinon que les icônes sont à jour par rapport à celles présentes réellement dans QGIS.

C'est sous le capot que les choses ont changé : tout est automatisé via [un workflow GitHub](https://github.com/geotribu/pyqgis-icons-cheatsheet/blob/main/.github/workflows/deploy.yml), programmé pour s'exécuter tous les mois, déroulant alors le scénario suivant :

1. le quasiment même [script](https://github.com/geotribu/pyqgis-icons-cheatsheet/blob/main/qrc_preview_in_md.py) qu'en 2021 récupère le fichier de ressources depuis le projet QGIS et génère la page en Markdown
1. le [fichier README.md](https://github.com/geotribu/pyqgis-icons-cheatsheet/blob/main/README.md) contenant les crédits est copié dans le sous-dossier `docs/`
1. le site est généré avec Mkdocs et le thème Material, les mêmes outils que pour le site de Geotribu
1. le site est publié sur GitHub Pages

À noter que les images sont toutes téléchargées depuis le dépôt de QGIS puis compressées, de façon à ne pas avoir de souci de lien cassé et d'avoir une certaine indépendance en termes techniques.

----

## Un navigateur intégré au plugin ENMap-Box

Suite à mon mail de présentation de ce site sur la liste QGIS-Dév, j'ai eu quelques retours et notamment de la part de Benjamin Jakimow, développeur du [plugin ENMap-Box](https://enmap-box.readthedocs.io/en/latest/) dans lequel il a intégré un navigateur de toutes les ressources accessibles en PyQt, y compris celles de QGIS donc :

![Plugin ENMap-Box - Resource Browser](https://cdn.geotribu.fr/img/tuto/qgis_plugin_embedded_images/qgis_enmap-box_resource_browser.webp){: .img-center loading=lazy }

C'est vraiment cool d'avoir ce genre d'outils directement dans QGIS, mais c'est un perdu dans un plugin dont le champ fonctionnel est juste énorme !

Je lui ai donc proposé mon aide pour en faire un plugin dédié indépendant. À suivre !

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
