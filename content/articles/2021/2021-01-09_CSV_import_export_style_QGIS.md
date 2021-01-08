---
title: "CSV - Import/export d'un style catégorisé QGIS"
authors: ["Florian Boret"]
categories: ["article"]
date: 2021-01-09 11:11
description: "CSV - Import/export d'un style catégorisé QGIS"
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/QGIS_style_CSV.gif"
tags: qgis,style,csv,processing
---

### Historique (QGIS2)

En 2015 après avoir lu un article de José Guerrero :  "[Cómo establecer el color de un rasgo (feature) dependiendo de los valores de los atributos con PyQGIS](https://joseguerreroa.wordpress.com/2015/02/22/como-establecer-el-color-de-un-rasgo-feature-dependiendo-de-los-valores-de-los-atributos-con-pyqgis/)"  l'idée m'était venue de créer de 2 scripts python/processing qui permettaient de générer un **style catégorisé** à partir d'un fichier CSV dans lequel on trouvait des informations de couleur.

* le premier script avait besoin de 3 colonnes R,G,B dans le fichier csv : [CSV_R-G-B_to_categorized_style.py](https://github.com/igeofr/qgis2/blob/master/scripts/CSV_R-G-B_to_categorized_style.py).
* le second avait besoin d'un seul champ de couleur RGB ou Hexadécimal : [CSV_RGB_or_HEX_to_categorized_style.py](https://github.com/igeofr/qgis2/blob/master/scripts/CSV_RGB_or_HEX_to_categorized_style.py).

[![Exempe Réunion](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/CSV_QGIS_style.gif "Exemple réalisé à partir de la donnée Corine Land Cover de la Réunion."){: loading=lazy align=middle }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/CSV_QGIS_style.gif){: data-mediabox="lightbox-gallery" data-title="Exemple réalisé à partir de la donnée Corine Land Cover de la Réunion."}

### Aujourd'hui (QGIS3)

Fin 2020 et après 5 années de bons et loyaux services, il était grand temps de réécrire ces scripts pour QGIS3 en tenant compte des nombreuses évolutions liées aux processing.

* le premier  a toujours besoin de 3 colonnes dans le fichier csv : Red – Green – Blue : [CSV_R_G_B_to_categorized_style_algo.py](https://github.com/igeofr/qgis3/blob/master/scripts/style/CSV_R_G_B_to_categorized_style_algo.py)
* le second a été séparé en deux scripts qui utilisent toujours une seule colonne de couleur : 
Hexadécimal : [CSV_HEX_to_categorized_style_algo.py](https://github.com/igeofr/qgis3/blob/master/scripts/style/CSV_HEX_to_categorized_style_algo.py) ou RGB : [CSV_RGB_to_categorized_style_algo.py](https://github.com/igeofr/qgis3/blob/master/scripts/style/CSV_RGB_to_categorized_style_algo.py)

Pour compléter ces premiers outils, j'ai également ajouté la possiblité d'exporter les couleurs d'un style QGIS vers un fichier CSV : [Style_to_CSV_algo.py](https://github.com/igeofr/qgis3/blob/master/scripts/style/Style_to_CSV_algo.py).

[![Exempe CCPL](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/QGIS_style_CSV.gif "Exemple réalisé à partir de la donnée d'occupation de la CCPL."){: loading=lazy align=middle }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/QGIS_style_CSV.gif){: data-mediabox="lightbox-gallery" data-title="Exemple réalisé à partir de la donnée d'occupation de la CCPL."}


