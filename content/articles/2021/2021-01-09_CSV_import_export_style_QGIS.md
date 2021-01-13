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

En 2015 après avoir lu un article de José Guerrero :  "[Cómo establecer el color de un rasgo (feature) dependiendo de los valores de los atributos con PyQGIS](https://joseguerreroa.wordpress.com/2015/02/22/como-establecer-el-color-de-un-rasgo-feature-dependiendo-de-los-valores-de-los-atributos-con-pyqgis/)",  l'idée m'était venue de créer de 2 scripts python/processing afin de générer un **style catégorisé** à partir d'un fichier CSV dans lequel des codes couleurs seraient renseignées.

* le premier script avait besoin de 3 colonnes R,G,B dans le fichier csv : [CSV_R-G-B_to_categorized_style.py](https://github.com/igeofr/qgis2/blob/master/scripts/CSV_R-G-B_to_categorized_style.py).
* le second avait besoin d'un seul champ de couleur RGB ou Hexadécimal : [CSV_RGB_or_HEX_to_categorized_style.py](https://github.com/igeofr/qgis2/blob/master/scripts/CSV_RGB_or_HEX_to_categorized_style.py).

![Exempe Réunion](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/CSV_QGIS_style.gif "Exemple réalisé à partir de la donnée Corine Land Cover de la Réunion."){: .img-center } *Exemple réalisé à partir de la donnée Corine Land Cover de la Réunion.* {: align=middle }

### Aujourd'hui (QGIS3)

Fin 2020 et après 5 années de bons et loyaux services, il était grand temps de réécrire ces scripts pour QGIS3 en tenant compte des nombreuses évolutions liées au processing.

* le premier a toujours besoin de 3 colonnes dans le fichier csv : Red - Green – Blue : [CSV_R_G_B_to_categorized_style_algo.py](https://github.com/igeofr/qgis3/blob/master/scripts/style/CSV_R_G_B_to_categorized_style_algo.py).
* le second a été séparé en deux scripts qui utilisent toujours une seule colonne de couleur : Hexadécimal : [CSV_HEX_to_categorized_style_algo.py](https://github.com/igeofr/qgis3/blob/master/scripts/style/CSV_HEX_to_categorized_style_algo.py) ou RGB : [CSV_RGB_to_categorized_style_algo.py](https://github.com/igeofr/qgis3/blob/master/scripts/style/CSV_RGB_to_categorized_style_algo.py).

### Pour aller plus loin

Pour compléter ces premiers outils, j'en ai profité pour travailler sur un nouveau script python/processing qui permet cette fois-ci d'exporter les couleurs d'un style QGIS vers un fichier CSV (la boucle est bouclée!) : [Style_to_CSV_algo.py](https://github.com/igeofr/qgis3/blob/master/scripts/style/Style_to_CSV_algo.py).

![Exempe CCPL](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/QGIS_style_CSV.gif "Exemple réalisé à partir d'une donnée produite sur le territoire du Lunellois."){: .img-center } *Exemple réalisé à partir d'une donnée produite sur le territoire du Lunellois* {: align=middle }

### Pour terminer

En ce qui me concerne, j'ai régulièrement utilisé ces scripts lors de travaux sur l'occupation du sol ou le nombre de classes était généralement important mais au-delà du fait qu'ils m'ont fait gagné du temps, ils m'ont aussi permis de jongler plus facilement entre des nomenclatures (tableurs) et QGIS.

Je vous laisse maintenant assaisonner vos cartes de couleurs :yum:!

----

## Auteur

--8<-- "content/team/fbor.md"
