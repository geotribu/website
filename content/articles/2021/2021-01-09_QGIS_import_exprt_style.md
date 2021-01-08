---
title: "QGIS - Import/export de styles CSV"
authors: ["Geotribu"]
categories: ["article"]
date: 2021-01-06 11:11
description: "L'équipe de Geotribu vous souhaite ses meilleurs voeux pour 2021, avec quelques statistiques sur l'année 2020 et une feuille de route 2021."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/divers/phoenix_constellation_map_fr.png"
tags: geotribu,voeux,statistiques,fréquentation,géomatique,sig,contribution,collaboratif
---

### Historique (QGIS2)

En 2015 après avoir lu un article de José Guerrero :  "[Cómo establecer el color de un rasgo (feature) dependiendo de los valores de los atributos con PyQGIS](https://joseguerreroa.wordpress.com/2015/02/22/como-establecer-el-color-de-un-rasgo-feature-dependiendo-de-los-valores-de-los-atributos-con-pyqgis/)"  l'idée m'était venue de créer de 2 scripts python/processing qui permettent de générer un style catégorisé à partir d'un fichier CSV dans lequel on trouve des informations de couleur.

– le premier script nécessitait d'avoir 3 colonnes dans le fichier csv : Red – Green – Blue : CSV_R-G-B_to_categorized_style.py
– le second avait besoin d'un seul champ de couleur : R,G,B ou Hexadécimal :  CSV_RGB_or_HEX_to_categorized_style.py

### Aujourd'hui (QGIS3)

