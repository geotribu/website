---
title: Classification automatisée avec le plugin QGIS dzetsaka
authors:
    - Sylvain KERDREUX
categories:
    - article
comments: true
date: 2022-07-22
description: Présentation de Dzetsaka, un plugin QGIS pour faire de la classification semi-automatisée.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_plugin_dzetsaka_classification/L_Dzetsaka_Resultat4.png
license: default
tags:
    - classification
    - QGIS
---

# Dzetsaka : outil de classification pour QGIS

:calendar: Date de publication initiale : 22 juillet 2022

## Introduction

![logo Dzetsaka](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis_dzetsaka.png "logo Dzetsaka"){: .img-thumbnail-left }

La classification (dans notre exemple d'une image raster) est une tâche permettant d'extraire des classes d'information à partir de l'analyse du jeu de données.

Je vous propose un guide pour réaliser ce travail en prenant en main le [plugin Dzetsaka pour QGIS](https://github.com/nkarasiak/dzetsaka). Il est issu d'un premier plugin (Historical Map) développé aussi par Nicolas Karasiak dont le but était d'automatiser la vectorisation des forêts sur des vieilles cartes papiers. Il a été publié en version 1.0 en octobre 2016 suite à une conférence au début de la même année où Nicolas a découvert la possibilité d'ajouter des algorithmes directement dans la toolbox des géotraitements. Depuis 2016 les mises à jour sont très nombreuses jusqu'en 2021 où le plugin peut être considéré comme stable (des mises à jour mineures sur des petits bugs).

Initialement, le plugin a été développé pour classifier différents types de végétation mais il peut être utilisé pour différencier des structures bien distinctes.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Installation du plugin

L'installation se fait simplement via la gestion des extensions de QGIS (ici en version 3.22) :

![QGIS - Installation plugin Dzetsaka](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_plugin_dzetsaka_classification/A_QGIS_InstallPlugin.png "QGIS - Installation plugin Dzetsaka"){: .img-center loading=lazy }

Puis on effectue une recherche `dzetsaka` :

![QGIS - Installation plugin Dzetsaka](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_plugin_dzetsaka_classification/B_QGIS_InstallPlugin_suite.png "QGIS - Installation plugin Dzetsaka"){: .img-center loading=lazy }

Une fois installé le plugin est accessible via le menu Extension :

![QGIS - Installation plugin Dzetsaka](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_plugin_dzetsaka_classification/C_QGIS_InstallPlugin_Fin.png "QGIS - Installation plugin Dzetsaka"){: .img-center loading=lazy }

----

## Paramétrage

### Bienvenue

La fenêtre de bienvenue permet d'accéder à la documentation et à un jeu d'essai (que nous n'allons pas utiliser dans notre exemple).

![QGIS - Installation plugin Dzetsaka](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_plugin_dzetsaka_classification/D_Dzetsaka_Welcome.png "QGIS - Installation plugin Dzetsaka"){: .img-center loading=lazy }

### Configuration

Avant de s'attaquer à la partie classification, un petit détour par la partie configuration est préférable :

![QGIS - Installation plugin Dzetsaka](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_plugin_dzetsaka_classification/E_Dzetsaka_Configuration.png "QGIS - Installation plugin Dzetsaka"){: .img-center loading=lazy }

Cette fenêtre regroupe plusieurs propriétés :

- `Classifier` qui contient 4 types de classification
    - `Gaussian Mixture Model` pour [modèle de mélange gaussien](https://fr.wikipedia.org/wiki/Mod%C3%A8le_de_m%C3%A9lange_gaussien)
    - `Random Forest` pour [forêt d'arbre décisionnels](https://fr.wikipedia.org/wiki/For%C3%AAt_d'arbres_d%C3%A9cisionnels)
    - `Support Vector Machines` pour [machine à vecteurs de support](https://fr.wikipedia.org/wiki/Machine_%C3%A0_vecteurs_de_support)
    - `k-nearest neighbors` pour [méthode des K plus proches voisins](https://fr.wikipedia.org/wiki/M%C3%A9thode_des_k_plus_proches_voisins)
- `Temp suffix` : suffixe pour les fichiers temporaires
- `Temp préfixe` : préfixe pour les fichiers temporaires
- `Mask suffix` : suffixe pour les masques
- `Providers` qui contient 2 propriétés (standard ou expérimental - l'expérimental étant le dernier code mais non garanti de fonctionnement)

### Parcelles d'entraînement

L'utilisation du plugin nécessite de créer une couche d'entraînement avec des données qu'on arrive à identifier facilement sur l'image raster.
La couche créée sera de type `polygone` et devra être dans le même système de coordonnées que la couche raster.  
Elle devra comporter a minima un champ de type entier pour identifier les classes.

Dans notre cas, on crée aussi un champ description :

![QGIS - Installation plugin Dzetsaka](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_plugin_dzetsaka_classification/F_Dzetsaka_Configuration_Train.png "QGIS - Installation plugin Dzetsaka"){: .img-center loading=lazy }

Nous allons ensuite créer différentes entités sur les zones qui nous intéressent :

- la Loire (et la Sèvre nantaise)
- les prairies
- les arbres
- les toits en tuiles
- les routes

Nous obtenons la couche d'entraînement suivante (les tuiles et routes ne sont pas visibles à cette échelle) :

![Plugin Dzetsaka - Couche d'entraînement](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_plugin_dzetsaka_classification/G_Train_.png "Plugin Dzetsaka - Couche d'entraînement"){: .img-center loading=lazy }

## Classification

A partir du dock de configuration :

![Plugin Dzetsaka - Dock configuration](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_plugin_dzetsaka_classification/H_Dzetsaka_Dock.png "Plugin Dzetsaka - Dock configuration"){: .img-center loading=lazy }

On sélectionne la couche raster, la couche d'entraînement et pour cette dernière l'attribut qui porte l'identification des éléments d'entraînements.

On lance ensuite la classification qui va durer dans notre cas une dizaine de minutes.

!!! important
    Ne pas oublier de stopper le mode édition de la couche d'entrainement !

----

## Résultats

Le résultat obtenu est une image résultat en dégradé de gris :

![Plugin Dzetsaka - Résultat dégradé gris](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_plugin_dzetsaka_classification/I_Dzetsaka_Resultat1.png "Plugin Dzetsaka - Résultat dégradé gris"){: .img-center loading=lazy }

En appliquant la symbologie initiale :

![Plugin Dzetsaka - Symbologie initialee](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_plugin_dzetsaka_classification/J_Dzetsaka_Resultat2.png "Plugin Dzetsaka - Symbologie initialee"){: .img-center loading=lazy }

On obtient l'image suivante :

![Plugin Dzetsaka - Résultat stylisé](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_plugin_dzetsaka_classification/K_Dzetsaka_Resultat3.png "Plugin Dzetsaka - Résultat stylisé"){: .img-center loading=lazy }

En zoomant un peu plus, on peut analyser un peu plus les résultats :

![Plugin Dzetsaka - Résultat zoom](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_plugin_dzetsaka_classification/L_Dzetsaka_Resultat4.png "Plugin Dzetsaka - Résultat zoom"){: .img-center loading=lazy }

Les prairies, arbres et rivières/fleuves sont globalement bien identifiés (la turbidité de la Loire génère des résultats un peu complexe à certains endroits).  
Les toits en tuiles sont globalement bien identifiés aussi tandis que le reste est très difficile à analyser (on retrouve des couleurs globalement identiques entre la route et les bâtiments récents).

## Conclusion

Le plugin offre des résultats très intéressants dans des contextes d'éléments fortement contrastés. Cependant l'utilisation sur du raster dépourvu de bandes infrarouges montre des limites quant à la possibilité de différencier des éléments de même couleur (par exemple routes et bâtiments).  
A noter qu'il existe aussi d'autres méthodes de calcul (expérimental) du plugin qui pourrait donner d'autres résultats plus précis.

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
