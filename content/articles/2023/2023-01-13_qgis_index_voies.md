---
title: "Créer un index des voies dans QGIS"
authors:
    - Florian Boret
categories:
    - article
    - tutoriel
date: 2023-01-13 14:20
description: "Créer un index des voies dans QGIS"
image: ""
license: default
tags:
    - QGIS
---

# Créer un index des voies dans QGIS

:calendar: Date de publication initiale : 13 janvier 2023

## Prérequis

- QGIS

## Intro

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-rdp-news-thumb }

Nombreuses sont les communes qui disposent d'un plan de ville, qu'elles affichent dans la rue ou qu'elles mettent à disposition sous la forme d'un dépliant, je vous partage ici la manière dont j'ai créé un listing des voies sur une expérimentation de plan de ville. Il y a sans aucun doute des choses à améliorer alors n'hésitez pas à laisser vos propositions ou vos remarques en commentaire.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Créer une grille

La première étape consiste à créer une grille carrée à l'aide des outils vectoriels de QGIS : `Vecteur` / `Outils de recherche` / `Créer une grille`.

![Créer une grille](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/creer_grille.png "Créer une grille"){: .img-center loading=lazy }

Pour cet exemple, j'ai créé une grille de 200m de côté (à vous d'ajuster la distance en fonction de votre besoin) correspondant à l'emprise de la commune.

![Grille](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/grille.png "Grille"){: .img-center loading=lazy }

## Attribuer un identifiant à chacune des mailles

Sur la couche correspondant à la grille, ajouter un champ virtuel afin de dénommer chacune des mailles.

![Nommage de chaque maille](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/nom_maille.png "Nommage de chaque maille"){: .img-center loading=lazy }

```python
# source : https://gis.stackexchange.com/questions/330760/create-a-grid-with-all-polygons-labelled-index-style
CASE
  WHEN floor(((maximum("top") - "top" ) / 999) / 26) > 0 --height
  THEN char(floor(((maximum("top") - "top" ) / 999) / 25) + 64) --height
  ELSE ''
END
||
char(((maximum("top") - "top") / 999) % 26 + 65) --height
||
to_string(("right" - minimum("left")) / 999) --width
```

!!! info
    Remplacer la valeur 999 par la taille par la distance d'espacement de vos mailles.

![Nom attribué à chaque maille](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/nom_maille2.png "Nom attribué à chaque maille"){: .img-center loading=lazy }

![Nom attribué à chaque maille](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/nom_maille3.png "Nom attribué à chaque maille"){: .img-center loading=lazy }

!!! info
    Grâce au champ virtuel, la suppression de mailles inutiles entrainera une réattribution dynamique des numéros de maille. :magic_wand:

## Liste des mailles qui croisent une voie

Sur la couche correspondant aux voies, ajouter un champ virtuel qui va permettre de faire le lien entre chacune des voies et les mailles qu'elles croisent.

![Calcul des mailles qui croisent les voies](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/calcul_liste_mailles.png "Calcul des mailles qui croisent les voies"){: .img-center loading=lazy }

```python
aggregate(
layer:= 'Grille',
aggregate:='concatenate',
expression:=grille,
concatenator:=', ',
filter:=intersects($geometry,geometry(@parent))
)
```

## Intégrer l'index des voies dans le composeur

Maintenant que la donnée est prête, vous pouvez créer une nouvelle mise en page d'impression en ajoutant la table attributaire de vos voies.

![Composeur - Table attibutaire](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/table_attributaire.png "Composeur - Table attibutaire"){: .img-center loading=lazy }

![Plan de ville](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/plan_ville.png "Plan de ville"){: .img-center loading=lazy }

----

## Conclusion

A COMPLETER

----

## Auteur {: data-search-exclude }

--8<-- "content/team/fbor.md"

{% include "licenses/default.md" %}
