---
title: "Faire une carte façon Ed Fairburn avec QGis"
authors:
    - Michaël GALIEN
categories:
    - article
date: "2022-08-31 10:00"
description: "Utiliser les modes de fusion pour produire avec QGis une carte inspirée des dessins d'Ed Fairburn."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_facon_ed_fairburn/carte_facon_ed_fairburn.png"
tags:
    - QGis
    - carte
    - rendu
    - mode de fusion
    - composeur d'impression
---

# Faire une carte façon Ed Fairburn avec QGis

## Introduction

Si tu ne connais pas encore le travail d'[Ed Fairburn](https://edfairburn.com/about/), son [portfolio est par là](https://edfairburn.com/full-portfolio/).

Sympa cette façon de mélanger portrait et fond de carte, non ?

Dans ce tuto, je te propose de faire une carte inspirée de ses réalisations grâce aux possibilités qu'offrent les [modes de fusion](https://docs.qgis.org/3.22/fr/docs/user_manual/introduction/general_tools.html#blend-modes).

**Pré-requis :**

* [QGis](https://qgis.org/fr/site/).
* Une dose de géo-données.
* Un soupçon de créativité.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Les modes de fusion en quelques mots

_Superposition_, _Écran_, _Soustraire_, _Différence_, ... j'avais prévenu : quelques mots.

Plus sérieusement, sous QGis les modes de fusion sont disponibles dans les options de rendu.
On les trouve à plusieurs endroits, au niveau de la symbologie d'une couche aussi bien vecteur que raster par exemple, mais aussi sur les objets d'une mise en page dans le composeur d'impression.

Le mode de fusion détermine comment un élément graphique se comporte vis à vis des éléments qui se trouvent en-dessous.
Classiquement, le mode de fusion est _Normal_ de sorte que l'objet au-dessus masque ceux qui sont placés en dessous.
En jouant sur les transparences, il est possible de ne pas totalement masquer les autres éléments mais les modes de fusion permettent d'aller plus loin.

La description du comportement de chacun des modes est bien évidemment [disponible dans le documention](https://docs.qgis.org/3.22/fr/docs/user_manual/introduction/general_tools.html#blend-modes).
Difficile en quelques lignes de décrire de façon intelligible ces options alors le mieux reste de tester, jouer, et enfin comprendre.

----

## Projet QGis

![Logo QGis](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "Logo QGis"){: .img-rdp-news-thumb }

J'utilise ici la [BD Topo® de l'IGN](https://geoservices.ign.fr/bdtopo) mais tu peux travailler avec d'autres sources, pourquoi pas te tourner vers [OSMData](https://demo.openstreetmap.fr/map) et chopper 2 - 3 données sympas.

Pour ma part, ce sera un plan basé sur les classes :
* _batiment_
* _voie_nommee_
* _zone_de_vegetation_
* _troncon_hydrographique_
* _surface_hydrographique_

La classe _batiment_ est l'élément principal. Je colore cette couche en noir, c'est important pour la suite, et j'ajoute une bordure blanche pour distinguer les constructions les unes des autres.
Les _voie_nommee_ sont quant à elles colorées en gris et étiquetées.
Les _zone_de_vegetation_ et _surface_hydrographique_ sont respectivement vertes et bleues (si si ! c'est vrai !).
La classe _troncon_hydrographique_ est simplement utilisée pour l'étiquetage des surfaces hydrographiques.

![Aperçu du projet QGis](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_facon_ed_fairburn/projet_qgis.png "Aperçu du projet QGis"){: .img-center loading=lazy }

----

## Mise en page

Tu as probablement reconnu le [Jardin des Tuileries](https://fr.wikipedia.org/wiki/Jardin_des_Tuileries) et le [Louvre](https://www.louvre.fr/) sur l'image précédente.
On va essayer de faire une affichcarto, ou cartaffiche si tu préfères, pour le plus célèbre des musées parisiens.

### Quand le fond...

Pour cette mise en page carrée de 50 cm de côté, je ne vais pas commencer par l'objet _Carte_.

Je construis à la place une sorte de fond de mise en forme avec :
* une bordure bien épaisse grâce à un objet _Rectangle_,
* deux objets _Etiquette_ en guise de titre et sous-titre,
* et deux objets _Polygone_ placés de sorte à rappeler le premier symbole du Louvre : la Pyramide.

![Fond de mise en page](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_facon_ed_fairburn/fond.png "Fond de mise en page"){: .img-center loading=lazy }

### ...fait la forme !

C'est à cette étape qu'on va ajouter l'objet _Carte_, mais avant ça, parlons un peu du mode de fusion _Addition_.

Comme son nom l'indique, le mode _Addition_ additionne les couleurs, et là tu te dis _"Ah ok, donc jaune et bleu ça fait vert !!!"_ et bien pas du tout.

La somme est réalisée sur les 3 composantes des codes RGB.
Ainsi, l'addition de deux couleurs `#UUVVWW` et `#XXYYZZ` donne `#(UU+XX)(VV+YY)(WW+ZZ)`.

En RGB, le code hexa du jaune est `#FFFF00` et celui du bleu est `#0000FF`.
La somme de `#FFFF00` et `#0000FF` est égale à `#FFFFFF` soit le blanc.

En image, voilà ce que donne le croisement du rouge (`#FF0000`), du vert (`#00FF00`) et du bleu (`#0000FF`).

![Comportement du mode de fusion Addition](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_facon_ed_fairburn/mode_fusion_addition.png "Comportement du mode de fusion Addition"){: .img-center loading=lazy }

On retrouve bien le jaune (`#FFFF00`) au croisement du rouge et du vert (`#FF0000` + `#00FF00`).
Au centre, le croisement des trois couleurs (`#FF0000` + `#00FF00` + `#0000FF`) donne le blanc (`#FFFFFF`).

De fait, n'importe quelle couleur additionnée à du blanc donne du blanc...parce que [plus blanc que blanc](https://www.youtube.com/watch?v=VEZw1Vmq97Y) on ne sait toujours pas ce que c'est.
Inversement, n'importe quelle couleur avec du noir (`#000000`) donne la couleur elle-même. Tu commences à comprendre pourquoi le choix du noir à l'étape qui précède ?

J'ajoute la carte et fixe son rendu à _Addition_ et là ... magie ! On vient de transformer le fond en forme.

![Plan en mode Addition](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_facon_ed_fairburn/plan.png "Plan en mode Addition"){: .img-center loading=lazy }

!!! Note
    La police d'écriture de l'étiquette _"- PARIS -"_ est trop fine et illisible si elle s'additionne avec la carte.
    Comme vu plus haut, le mode de fusion définit le comportement d'un objet avec ce qu'il y a en dessous.
    En plaçant _"- PARIS -"_ au-dessus, j'évite la fusion.

### LE portrait

A cette étape, pour faire honneur aux travaux d'Ed Fairburn, on ne va pas utiliser un portrait mais LE portrait, celui de Mona Lisa.

Par contre, on va cette fois opter pour le mode _Éclaircir_ qui conserve sur chacune des composantes RGB celle qui a la plus grande valeur.
Avec ce rendu, l'assemblage des couleurs `#UUVVWW` et `#XXYYZZ` donne `#max(UU,XX)max(VV,YY)max(WW,ZZ)`

Comme pour _Addition_, avec le mode _Éclaircir_ couleur + blanc = blanc et couleur + noir = couleur, mais le résultat est différent sur les valeurs intermédiaires, la preuve en image.

![Comportement du mode de fusion Eclaircir](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_facon_ed_fairburn/mode_fusion_eclaircir.png "Comportement du mode de fusion Eclaircir"){: .img-center loading=lazy }

On voit que le mode _Addition_ tend plus rapidement vers le blanc.
Pour l'ajout du portrait, il donnerait une sensation de brûlage/surexposition de la Joconde.

Le mode _Éclaircir_ permet de remplacer le noir des bâtiments par le visage de Mona Lisa et d'avoir un mélange plus fondu sur les zones de végétation, les surfaces hydrographiques et les voies nommées.

![La Joconde en mode Eclaircir](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_facon_ed_fairburn/joconde.png "La Joconde en mode Eclaircir"){: .img-center loading=lazy }

### "Rue de Rivoli" Touch

Je ne suis vraiment pas fier de cette dernière étape mais c'est là encore pour aller dans le sens d'Ed Fairburn qui met parfois en lumière certaines rues dans ses dessins.
En plus GéoTribu me rémunère au nombre de mots donc bon...

Le musée du Louvre étant Rue de Rivoli, j'ajoute simplement une ligne rouge/blanche au premier plan et une étiquette.
Par défaut en mode de fusion _Normal_, ces deux nouveaux éléments masquent ce qu'il y a en-dessous.

On voit ici que la superposition des modes est possible à l'infini...enfin l'infini, disons que c'est possible tant que ton PC et QGis sont capables de calculer les fusions à l'affichage.

![Mise en avant de la rue de Rivoli](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_facon_ed_fairburn/final.png "Mise en avant de la rue de Rivoli"){: .img-center loading=lazy }

----

## Et voilà le travail

Nous avons terminé notre portrait de la Joconde façon Ed Fairburn.

Nous avons utilisé pour cela deux des modes de fusion proposés par QGis, mais comme tu as pu le voir dans la [documentation](https://docs.qgis.org/3.22/fr/docs/user_manual/introduction/general_tools.html#blend-modes), il y en a bien plus.
Il existe notamment _Soustraire_ et _Assombrir_ qui sont les exacts opposés des modes _Addition_ et _Éclaircir_ que nous avons vus.
Pour le reste, il te faudra tester...

Tiens, et si on demandait à [DALL.E](https://openai.com/dall-e-2/) de nous générer le "portrait de la Joconde dans un plan de Paris en forme de pyramide" ?

![La Joconde par DALL.E - version 1](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_facon_ed_fairburn/DALL.E_mona_misa_1.png "La Joconde par DALL.E - version 1"){: .img-center loading=lazy }
![La Joconde par DALL.E - version 2](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_facon_ed_fairburn/DALL.E_mona_misa_2.png "La Joconde par DALL.E - version 2"){: .img-center loading=lazy }

Je ne sais pas toi mais perso je préfère notre version QGis.

![La Joconde façon Ed Fairburn](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_facon_ed_fairburn/affiche.png "La Joconde façon Ed Fairburn"){: .img-center loading=lazy }

Dans le détail, on voit bien comment le portrait est fusionné avec les zones de végétation et les surfaces hydrographiques.

![Détails de la fusion](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/carte_facon_ed_fairburn/details.png "Détails de la fusion"){: .img-center loading=lazy }

A toi de jouer maintenant !

----

## Auteur {: data-search-exclude }

--8<-- "content/team/mgal.md"
