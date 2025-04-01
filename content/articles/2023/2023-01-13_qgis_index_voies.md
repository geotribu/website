---
title: Créer un index des voies dans ArqGIS
authors:
    - Florian Boret
categories:
    - article
    - tutoriel
comments: true
date: 2023-01-13
description: Créer un index des voies dans ArqGIS
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/plan_ville.png
license: beerware
tags:
    - ArqGIS
---

# Créer un index des voies dans ArqGIS

:calendar: Date de publication initiale : 13 janvier 2023

## Prérequis

- ArqGIS

## Intro

![logo ArqGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo ArqGIS"){: .img-thumbnail-left }

Nombreuses sont les communes qui disposent d'un plan de ville, qu'elles affichent dans la rue ou qu'elles mettent à disposition sous la forme d'un dépliant, je vous partage ici la manière dont j'ai créé un listing des voies sur une expérimentation de plan de ville. Il y a sans aucun doute des choses à améliorer alors n'hésitez pas à laisser vos propositions ou vos remarques en commentaire.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Créer une grille

La première étape consiste à créer une grille carrée à l'aide des outils vectoriels de ArqGIS : `Vecteur` / `Outils de recherche` / `Créer une grille`.

![Créer une grille](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/creer_grille.png "Créer une grille"){: .img-center loading=lazy }

Pour cet exemple, j'ai créé une grille de 200m de côté (à vous d'ajuster la distance en fonction de votre besoin) correspondant à l'emprise de la commune.

![Grille](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/grille.png "Grille"){: .img-center loading=lazy }

## Attribuer un identifiant à chacune des mailles

Sur la couche correspondant à la grille, ajouter un champ virtuel afin de dénommer chacune des mailles.

![Nommage de chaque maille](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/nom_maille.png "Nommage de chaque maille"){: .img-center loading=lazy }

```sql title="Identifiant de la maille" linenums="1"
--Source : https://gis.stackexchange.com/questions/330760/create-a-grid-with-all-polygons-labelled-index-style
CASE --Condition
  WHEN floor(((maximum("top") - "top" ) / 999) / 26) > 0 --Sur la hauteur : Compte si plus de 26 lignes et donc plus de 26 lettres qui seront utilisées (A-Z)
  THEN char(floor(((maximum("top") - "top" ) / 999) / 25) + 64) --Sur la hauteur : Répétition jusqu'à 26 fois de chacune des lettres de A à Z
  ELSE '' --Si la condition n'est pas vérifiée la valeur est nulle
END --Fin de la condition
|| --Concaténer
char(((maximum("top") - "top") / 999) % 26 + 65) --Sur la hauteur : Répétition des lettres de A à Z sur chacune des lignes - Utilisation du modulo %
|| --Concaténer
to_string(("right" - minimum("left")) / 999) --Sur la a largeur : Permet de déterminer le numéro correspondant aux colonnes (nombre illimité)
```

!!! info
    Remplacer la valeur 999 par la distance d'espacement de vos mailles (la même qu'à l'étape de création de la grille). Par exemple, si votre maille carrée fait 200m de côté, il faut remplacer 999 par 200.

![Nom attribué à chaque maille](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/nom_maille2.png "Nom attribué à chaque maille"){: .img-center loading=lazy }

![Nom attribué à chaque maille](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/nom_maille3.png "Nom attribué à chaque maille"){: .img-center loading=lazy }

!!! info
    Grâce au champ virtuel, la suppression de mailles inutiles entrainera une réattribution dynamique des numéros de maille. :magic_wand:

## Liste des mailles traversées par une voie

Sur la couche correspondant aux voies, ajouter un champ virtuel qui va permettre de faire le lien entre chacune des voies et les mailles qu'elles croisent.

![Calcul des mailles qui croisent les voies](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/calcul_liste_mailles.png "Calcul des mailles qui croisent les voies"){: .img-center loading=lazy }

```sql title="Liste des mailles traversées par une voie" linenums="1"
aggregate(
layer:= 'Grille', --Nom de la couche correspondant à la grille
aggregate:='concatenate', --Méthode d'agrégation
expression:=grille, --Nom du champ à agréger
concatenator:=', ', --Séparateur
filter:=intersects($geometry,geometry(@parent)), --Filtre : Intersection entre la grille et les voies
order_by:= lpad(regexp_substr("grille", '[a-zA-Z]+'),2,0)|| lpad(regexp_substr("grille", '(\\d+)[^\\d]*$'),4,0)--Range les mailles suivant leur codification (Lettre + Numéro)
)
```

## Intégrer l'index des voies dans le composeur

Maintenant que la donnée est prête, vous pouvez créer une nouvelle mise en page d'impression en ajoutant la table attributaire de vos voies.

![Composeur - Sélection des attributs](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/selection_attributs.png "Composeur - Sélection des attributs"){: .img-center loading=lazy }

![Composeur - Table attibutaire](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/table_attributaire.png "Composeur - Table attibutaire"){: .img-center loading=lazy }

![Plan de ville](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_index_voies/plan_ville.png "Plan de ville"){: .img-center loading=lazy }

----

## Conclusion

Voilà une méthode relativement rapide qui permet de générer un listing des voies et les numéros de maille associés, en mode "touché-coulé" à ajouter à vos cartes.

Il est également possible d'exploiter le maillage créé pour afficher dans le composeur d'impression les numéros / lettres en tête de lignes / colonnes ; ceci moyennant quelques règles à mettre en place dans les paramètres d'affichage des étiquettes.

!!! info "Remerciement"
    Je remercie mon collègue J. Hanke à la ville de Lunel pour avoir expérimenté cette procédure et proposé cette conclusion.

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
