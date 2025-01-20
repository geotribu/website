---
title: CSV - Import/export d'un style catégorisé QGIS
authors:
    - Florian BORET
categories:
    - article
comments: true
date: 2021-01-22
description: CSV - Import/export d'un style catégorisé QGIS
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/QGIS_style_CSV.gif
tags:
    - CSV
    - Processing
    - QGIS
    - style
---

# CSV - Import/export d'un style catégorisé QGIS

:calendar: Date de publication initiale : 22 janvier 2021

## Historique (QGIS2)

En 2015, après avoir lu l'article de José Guerrero [_Cómo establecer el color de un rasgo (feature) dependiendo de los valores de los atributos con PyQGIS_](https://joseguerreroa.wordpress.com/2015/02/22/como-establecer-el-color-de-un-rasgo-feature-dependiendo-de-los-valores-de-los-atributos-con-pyqgis/),  l'idée m'était venue de créer 2 scripts python/processing afin de générer un **style catégorisé** à partir d'un fichier CSV dans lequel des codes couleurs seraient renseignés.

Pourquoi ? Parce que saisir jusqu'à 80 codes couleur à la mains c'était juste pas concevable :wink: !

* le premier script avait besoin de 3 colonnes R,G,B dans le fichier csv : [CSV_R-G-B_to_categorized_style.py](https://github.com/igeofr/qgis2/blob/master/scripts/CSV_R-G-B_to_categorized_style.py).
* le second avait besoin d'un seul champ de couleur RGB ou Hexadécimal : [CSV_RGB_or_HEX_to_categorized_style.py](https://github.com/igeofr/qgis2/blob/master/scripts/CSV_RGB_or_HEX_to_categorized_style.py).

![Exemple Réunion](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/CSV_QGIS_style.gif "Exemple réalisé à partir de la donnée Corine Land Cover de la Réunion."){: loading=lazy }  
_Exemple réalisé à partir de la donnée Corine Land Cover de la Réunion._
{: align=middle }

## Aujourd'hui (QGIS3)

Fin 2020 et après 5 années de bons et loyaux services, il était grand temps de réécrire ces scripts pour QGIS3 en tenant compte des nombreuses évolutions liées au processing.

* le premier a toujours besoin de 3 colonnes dans le fichier csv : Red - Green – Blue : [CSV_R_G_B_to_categorized_style_algo.py](https://github.com/igeofr/qgis3/blob/master/scripts/style/CSV_R_G_B_to_categorized_style_algo.py).

!!! info "Structure du fichier CSV"
    Par défaut, la structure du fichier CSV est la suivante : `Value;Label;Red;Green;Blue` mais l'ordre peut être modifié puisque le script permet de définir le numéro de chaque colonne en commençant par zéro.  
    Par défaut : `value : 0 ; label : 1 ; Red : 2 ; Green : 3 ; Blue : 4`.

* le second a été séparé en deux scripts qui utilisent toujours une seule colonne de couleur :
    * Hexadécimal : [CSV_HEX_to_categorized_style_algo.py](https://github.com/igeofr/qgis3/blob/master/scripts/style/CSV_HEX_to_categorized_style_algo.py)
    * ou RGB : [CSV_RGB_to_categorized_style_algo.py](https://github.com/igeofr/qgis3/blob/master/scripts/style/CSV_RGB_to_categorized_style_algo.py).

!!! info "Structure du fichier CSV"
    Par défaut, la structure du fichier CSV est la suivante : `Value;Label;RGB` mais l'ordre peut être modifié puisque le script permet là aussi de définir le numéro de chaque colonne en commençant par zéro.  
    Parr défaut : `value : 0 ; label : 1 ; RGB : 2`.

## Pour aller plus loin

Pour compléter ces premiers outils, j'en ai profité pour travailler sur un nouveau script python/processing qui permet cette fois-ci d'exporter les couleurs d'un style QGIS vers un fichier CSV (la boucle est bouclée !) : [Style_to_CSV_algo.py](https://github.com/igeofr/qgis3/blob/master/scripts/style/Style_to_CSV_algo.py).

![Exemple Lunellois](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/QGIS_style_CSV.gif "Exemple réalisé à partir d'une donnée produite sur le territoire du Lunellois."){: loading=lazy }  
_Exemple réalisé à partir d'une donnée produite sur le territoire du Lunellois_
{: align=middle }

----

## Comment ajouter ces scripts dans QGIS3

### La facilité

Ouvrir la fenêtre du processing et :point_down:

![Liste des scripts](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ajouter_scripts.png "Liste des scripts."){: loading=lazy }
{: align=middle }

### A l'ancienne

1. Vous devez placer le ou les script(s) dans ce répertoire :

    * Linux : `/home/USER/.local/share/QGIS/QGIS3/profiles/default/processing/scripts`
    * MacOS : `~/Bibliothèque/Application Support/QGIS/QGIS3/profiles/default/processing/scripts`
    * Windows : `C:\Users\USER\AppData\Roaming\QGIS\QGIS3\profiles\default\processing\scripts`

2. Lancer QGIS
3. Ensuite au niveau de la fenêtre du processing, vous devez voir une section `Scripts` :

    ![Scripts](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/scripts_processing.png "Scripts."){: loading=lazy }
    {: align=middle }

4. Si vous la déroulez vous devez voir la sous-section "Style" dans laquelle se trouvent les scripts ajoutés.

    ![Liste des scripts](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/scripts_QGIS_style.png "Liste des scripts."){: loading=lazy }
    {: align=middle }

## Pour terminer

En ce qui me concerne, j'ai régulièrement utilisé ces scripts lors de travaux sur l'occupation du sol ou le nombre de classes était généralement important. Au-delà du fait qu'ils m'ont fait gagné un temps précieux, ils m'ont aussi permis de jongler plus facilement entre des nomenclatures (tableurs) et QGIS.

Je vous laisse maintenant assaisonner vos cartes de couleurs :yum:!

----

<!-- geotribu:authors-block -->
