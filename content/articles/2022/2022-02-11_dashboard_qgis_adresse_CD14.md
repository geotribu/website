---
title: "Dashboard QGIS : Suivi des indicateurs adresse du Département du Calvados"
authors:
    - Théo GRONDIN
categories:
    - article
date: "2022-01-16 10:20"
description: "Depuis 2019, le Département accompagne les communes pour la saisie et la diffusion de leur adresse vers la Base adresse Nationale. Après plus de 2 ans de projet, et avec l’augmentation constante du nombre de demandes d’accompagnements par les communes, les équipe du pôle SIG ont souhaité se doter d’un tableau de bord de suivi des indicateurs clés du projet intégré au logiciels SIG utilisés quotidiennement par les équipes et les partenaires."
image: ""
license: default
robots: index, follow
tags:
    - adresse
    - BAN
    - dashboard
    - QGIS
    - tableau de bord
---

# Dashboard QGIS : Suivi des indicateurs adresse du Département du Calvados

:calendar: Date de publication initiale : 16 janvier 2022

Depuis 2019, le Département accompagne les communes pour la saisie et la diffusion de leur adresse vers la Base adresse Nationale. Après plus de 2 ans de projet, et avec l’augmentation constante du nombre de demande d’accompagnements par les communes, les équipe du pôle SIG ont souhaité se doter d’un tableau de bord de suivi des indicateurs clés du projet intégré aux logiciels SIG utilisés quotidiennement par les équipes et les partenaires.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Accompagnement à l’adressage du Département

L’adressage est obligatoire pour les communes de plus de 2000 habitants et est très fortement conseillé aux plus petites communes.
Pour permettre aux communes de diffuser leurs adresses, la Direction du numérique de l’État a mis en place la Base Adresse Nationale (BAN), une base qui référence l’ensemble des adresses locales à l’échelle nationale. Depuis octobre 2019, les adresses de « sources communales » publiées sur la BAN ont la priorité sur les autres sources.

Afin d’accompagner les communes dans cette démarche, le Département du Calvados met à disposition des communes une application cartographique de gestion des adresses atlas.calvados.fr (base adresse du calvados), permettant de consulter la BAN, dénommer des voie, créer des nouvelles adresses et modifier ou supprimer des adresses existantes. Cette application a été développée à partir des logiciels open sources Lizmap/POSTGIS/QGIS serveur.

En janvier 2022, le département accompagnait ainsi plus de 200 communes et avait publié près de XXX adresses sur la BAN. Cet accompagnement, réalisé par 2 agents du pôle SIG, implique des interventions sur le terrain, des formations aux normes de l’adressage, la résolution des problématiques terrain complexes, un support pour la saisie des adresses dans l’application, le contrôle des voies et des points adresses saisis.


## Un outil de suivi intégré

Le pôle SIG souhaitait obtenir une vue d’ensemble des données produites au fur et à mesure de l’avancement du projet. Il fallait donc identifier une solution SIG permettant d’assurer un suivi interactif des données.
Elle devait s’intégrer au logiciel QGIS de gestion et sur l’application cartographique Lizmap à disposition des communes et des partenaires.

Si sur le logiciel QGIS aucun module additionnel (plugin) ne propose à ce jour de solution complète de dashboarding, Nous avons pu nous appuyer sur une méthodologie publiée sur le site https://plugins.QGIS.org/geopackages/5/ (Sutton, 2020) , afin de développer un « dashboard » par manipulation des étiquettes de couches QGIS.

Cette méthode permet, en créant une couche spécifique de tableau de bord, de paramétrer le style des étiquettes de la couche et via requêtes sql d’agrégation, de produire un tableau interactif de suivi des données présentes dans le projet QGIS.


## Les étapes de construction du Dashboard

### Etape 1 : création de la couche dashboard

Créer une couche « dashboard » de polygone composée des champs suivant :

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/2022-01-03_14h39_28.png "QGIS - Menu étiquettes")


### Etape 2 : créer un polygone

Editer la couche « dashboard » et créer un polygone suivant l’emprise du projet.

![](https://geotripad.herokuapp.com/uploads/upload_3712a28a62e74b24ec58cda816db5558.png)


### Etape 3 : symbologie de la couche

Ouvrir les propriétés de la couche dashboard et dans l’onglet symbologie sélectionner ‘aucun symbole’.

Le polygone doit disparaitre à l’écran.

![](https://geotripad.herokuapp.com/uploads/upload_08d131680d7037f80058f41de414fae9.png)


### Etape 4 : paramétrer les étiquettes

Sélectionner ‘Etiquettes simples’ dans l’onglet Etiquettes. Dans le sous onglet valeur, faites une sélection par expression et inscrivez le code suivant : eval( "label_expression")

![](https://geotripad.herokuapp.com/uploads/upload_1b485acb02dadede72f315328f40f578.png)

Dans le sous onglet texte cliquer sur l’icône à droite de la police. Aller chercher type de champs et pointer vers le champ **font** de la table « dashboard » crée à l’étape 1.

![](https://geotripad.herokuapp.com/uploads/upload_7bcd590e60bb7b263f45c6494ef73b95.png)

Faire de même avec le **style** et pointer sur le champs style.

![](https://geotripad.herokuapp.com/uploads/upload_f05852314319714d2b2c40892bfd9f17.png)

Faire de même avec la **couleur** et pointer sur le champ ***font_colour***.

![](https://geotripad.herokuapp.com/uploads/upload_fc0fe8fdf08a99a635fdd6e33e09a34a.png)

Aller maintenant dans l’onglet **arrière-plan.**

Faire de même que précédemment avec la **taille X** et pointer sur le champ ***width***.

![](https://geotripad.herokuapp.com/uploads/upload_aeba86b57d1a93ee111914360b5ae9b3.png)

Faire de même que précédemment avec la **taille Y** et pointer sur le champ ***height***.

![](https://geotripad.herokuapp.com/uploads/upload_b197dacd8828c5aac9c857aca2dc8469.png)

Faire de même avec la **couleur de remplissage** et pointer sur le champ ***bg_colour***.

![](https://geotripad.herokuapp.com/uploads/upload_7c3907acb2657d0c167d8efa369f2ea4.png)

Aller maintenant dans l’onglet **position**.

Choisir l’option quadrant de l’image ci-dessous.

Cliquer sur l’icône à droite de **décalage X,Y**. Choisissez cette fois ci la sélection par expression.

Dans le constructeur de requête qui s’ouvre, indiquer la variable suivante : ***array( "label_offset_x" , "label_offset_y")***
Appuyer sur ok.

![](https://geotripad.herokuapp.com/uploads/upload_42e525c3259916e908ed30adf588dc78.png)



### Etape 5 : Remplir les champs de la table attributaire

Revenir à la table attributaire de « dashboard ».

Donner un nom qui mette en évidence l’action. Ici le titre de la première étiquette que nous appellerons fenêtre dashboard. Dans le champs **geometry_generator** inscrire la valeur ***point_n(  @map_extent, 4  )***.

Puis indiquer dans le champs label expression l’expression qui s’affichera dans la première fenêtre dashboard, ici, simplement le titre *****'nbr pt total'*****

![](https://geotripad.herokuapp.com/uploads/upload_ee9dd6d0dc338045f1d40d5a1ac3257b.png)

Paramétrer ensuite les champs qui vont déterminer la taille, la position, la couleur de fond et la police de la première fenêtre Dashboard.

![](https://geotripad.herokuapp.com/uploads/upload_472163cd012ed9bbaf20f8722227beaa.png)

Au fur et à mesure des modifications des valeurs de champs, lorsque vous enregistrez, vous devez voir apparaitre la 1ere fenêtre Dashboard et les modifications apportées.

![](https://geotripad.herokuapp.com/uploads/upload_586e43c1102265c0a41945c633083e15.png)

Si aucune fenêtre n’apparait au niveau de votre projet qgis, jouez avec les différents champs (surtout label_ofset x, label_ofset y), cela peut être un problème de position de la fenêtre. Si elle n’apparait toujours pas, reprenez les étapes précédentes.


### Etape 6 : Créer de nouvelles fenêtres dashboard

Pour créer une nouvelle fenêtre dashboard, passer la table attributaire en mode édition. Copiez la première ligne et coller la dans la partie blanche de la table attributaire. Une deuxième ligne identique apparaît.

![](https://geotripad.herokuapp.com/uploads/upload_21391b8fa2eec9d362da82d0a60c03d2.png)

### Etape 7 : Paramétrer des requêtes dans les nouvelles lignes

Une fois la nouvelle entité crée, modifier les valeurs de champs de la seconde pour positionner la deuxième fenêtre sous la première.  Vous pouvez modifier le champs label_expression avec une requête sql qgis qui vous permettra d’afficher la valeur souhaitée dans cette deuxième fenêtre.

![](https://geotripad.herokuapp.com/uploads/upload_faa08b446c9835898f02af106eae2de0.png)

### Exemple de table attributaire Dashboard et rendu

Ci-dessous, nous avons organisé la table avec les unes après les autres des fenêtres affichant une valeur « titre » suivies de fenêtres affichant une valeur « expression ».

![](https://geotripad.herokuapp.com/uploads/upload_93728d2320a056b71e007dda2d12ec7f.png)
![](https://geotripad.herokuapp.com/uploads/upload_c90109265cb833632993d9c7344fd70c.png)

![](https://geotripad.herokuapp.com/uploads/upload_9f1e6ecb468949f35ffb9345877631e8.png)


### Exemple de requêtes utilisées

--total de la somme des valeurs de la collonne pt_total de la couche Infos Communes

aggregate(layer:= 'Infos Communes', aggregate:='sum', expression:=pt_total)

--total de la somme des valeurs de la collonne pt_total des entités séléctionnées sur la couche Infos Communes

aggregate(layer:= 'Infos Communes', aggregate:='sum', expression:=pt_total, filter:=is_selected('Infos Communes', $currentfeature )  )

--Nombre de communes accompagnées (champ : actif, valeur : oui) dans la couche Infos Communes

aggregate(layer:= 'Infos Communes', aggregate:='count', expression:= actif, filter:= actif LIKE 'Oui' )



## Limites de l’outil

Si cette solution semble adaptée « en local » pour le projet QGIS de gestion des données adresse utilisé par le chargé de mission SIG, nous avons pu constater des problèmes au niveau du « responsiv design » de l’outil : l’affichage n’est pas optimal sur certains formats d’écran et sur l’application cartographique lizmap (atlas-calvados.fr).

Pour pallier ces difficultés d’affichage sur atlas.calvados.fr, la disposition des items a été revue (position centrale), le design a été simplifié et le nombre de données affichées limité par rapport à l’application de gestion des données sur QGIS.

![](https://geotripad.herokuapp.com/uploads/upload_f90ce3f45ed4eb120dcbb688c7ea356f.png)


----

## Auteur {: data-search-exclude }

--8<-- "content/team/tgro.md"

{% include "licenses/default.md" %}
