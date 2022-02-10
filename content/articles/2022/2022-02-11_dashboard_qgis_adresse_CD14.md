---
title: "Dashboard QGIS : suivi des indicateurs adresse du Département du Calvados"
authors:
    - Théo GRONDIN
categories:
    - article
date: "2022-02-07 10:20"
description: "Mise en place d'un tableau de bord QGIS par manipulation d'étiquettes de couches dans le cadre du suivi de projet adressage - Pôle SIG du Département du Calvados."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/intro.png "
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

:calendar: Date de publication initiale : 7 février 2022

Depuis 2019, le Département accompagne les communes pour la saisie et la diffusion de leurs adresses vers la Base adresse Nationale. Après plus de 2 ans de projet, et avec l’augmentation constante du nombre de demandes d’accompagnements par les communes, les membres du pôle SIG du Département ont souhaité se doter d’un tableau de bord de suivi des indicateurs clés du projet, intégré aux logiciels SIG utilisés quotidiennement par les équipes et les partenaires.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/intro.png  "QGIS - intro vue Dashboard")

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Accompagnement à l’adressage du Département

L’adressage est obligatoire pour les communes de plus de 2000 habitants et le deviendra pour l'ensemble des communes avec l'entrée en vigueur prochaine de la loi 3DS*.

Pour permettre aux communes de diffuser leurs adresses, la Direction du numérique de l’État a mis en place la Base Adresse Nationale (BAN), une base qui référence l’ensemble des adresses locales à l’échelle nationale. Depuis octobre 2019, les adresses de « sources communales » publiées sur la BAN ont la priorité sur les autres sources.

Afin d’accompagner les communes dans cette démarche, le Département du Calvados met à disposition des communes une application cartographique de gestion des adresses <https://atlas.calvados.fr/index.php/view/map/?repository=04&project=52_bac_14> (base adresse du calvados), permettant de consulter la BAN, dénommer des voie, créer des nouvelles adresses et modifier ou supprimer des adresses existantes. Cette application a été développée à partir des logiciels open sources Lizmap/PostGIS/QGIS serveur.

En janvier 2022, le département accompagnait ainsi plus de 200 communes et avait publié près de 47 000 adresses sur la BAN. Cet accompagnement, réalisé par 2 agents du pôle SIG, implique des interventions sur le terrain, des formations aux normes de l’adressage, la résolution des problématiques terrain complexes, un support pour la saisie des adresses dans l’application, le contrôle des voies et des points adresses saisis.

> **_*_**  <https://www.legifrance.gouv.fr/dossierlegislatif/JORFDOLE000043496065/>

## Un outil de suivi intégré

Au sein du pôle SIG, nous souhaitions obtenir une vue d’ensemble des données produites au fur et à mesure de l’avancement du projet. Il fallait donc identifier une solution SIG permettant d’assurer un suivi interactif des données (contrôle des erreurs de saisies et bilan de l'avancement du projet).
Elle devait s’intégrer au logiciel QGIS utilisé par le chargé de mission SIG du Département et sur l’application cartographique Lizmap à disposition des communes et des partenaires.

Sur le logiciel QGIS aucun module additionnel (plugin) ne propose à ce jour de solution complète de dashboarding. Nous nous nous sommes donc appuyer sur une méthodologie publiée sur le site <https://plugins.QGIS.org/geopackages/5/> (Sutton, 2020) , afin de développer un « Dashboard » par manipulation des étiquettes de couches QGIS.

Cette méthode permet, en créant une couche spécifique de tableau de bord, de paramétrer le style des étiquettes de la couche et via requêtes sql d’agrégation, de produire un tableau interactif de suivi des données présentes dans le projet QGIS.

## Les étapes de construction du Dashboard

### Etape 1 : création de la couche dashboard

Créer une couche « dashboard » de polygone composée des champs suivant :

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/1_champs_dashboard.png "QGIS - Champs table Dashboard")

### Etape 2 : créer un polygone

Éditer la couche « dashboard » et créer un polygone suivant l’emprise du projet.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/2_polygon_dashboard.png "QGIS - Création polygone Dashboard")

### Etape 3 : symbologie de la couche

Ouvrir les propriétés de la couche dashboard et dans l’onglet symbologie sélectionner ‘aucun symbole’.

Le polygone doit disparaître à l’écran.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/3_symbologie_dashboard.png "QGIS - Symbologie couche Dashboard")

### Etape 4 : paramétrer les étiquettes

Sélectionner ‘Etiquettes simples’ dans l’onglet Étiquettes. Dans le sous onglet valeur, faites une sélection par expression et inscrivez le code suivant : eval( "label_expression")

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/4_etiquettes_dashboard.png "QGIS - Étiquette simple Dashboard")

Dans le sous-onglet texte cliquer sur l’icône à droite de la police. Aller chercher type de champs et pointer vers le champ **font** de la table « dashboard » crée à l’étape 1.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/6_etiquettes_dashboard.png "QGIS - Étiquette font Dashboard")

Faire de même avec le **style** et pointer sur le champs style.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/6_etiquettes_dashboard.png "QGIS - Étiquette style Dashboard")

Faire de même avec la **couleur** et pointer sur le champ _**font_color**_.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/7_etiquettes_dashboard.png "QGIS - Étiquette couleur Dashboard")

Aller maintenant dans l’onglet **arrière-plan.**

Faire de même que précédemment avec la **taille X** et pointer sur le champ _**width**_.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/8_etiquettes_dashboard.png "QGIS - Étiquette X Dashboard")

Faire de même que précédemment avec la **taille Y** et pointer sur le champ _**height**_.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/9_etiquettes_dashboard.png "QGIS - Étiquette Y Dashboard")

Faire de même avec la **couleur de remplissage** et pointer sur le champ _**bg_colour**_.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/10_etiquettes_dashboard.png "QGIS - Étiquette remplissage Dashboard")

Aller maintenant dans l’onglet **position**.

Choisir l’option quadrant de l’image ci-dessous.

Cliquer sur l’icône à droite de **décalage X,Y**. Choisissez cette fois ci la sélection par expression.

Dans le constructeur de requête qui s’ouvre, indiquer la variable suivante : _**array( "label_offset_x" , "label_offset_y")**_
Appuyer sur ok.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/11_etiquettes_dashboard.png "QGIS - Étiquette décalage Dashboard")

### Etape 5 : Remplir les champs de la table attributaire

Revenir à la table attributaire de « dashboard ».

Donner un nom qui mette en évidence l’action. Ici le titre de la première étiquette que nous appellerons fenêtre dashboard. Dans le champs **geometry_generator** inscrire la valeur _**point_n(  @map_extent, 4  )**_.

Puis indiquer dans le champs label expression l’expression qui s’affichera dans la première fenêtre dashboard, ici, simplement le titre _***'nbr pt total'**_

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/12_1rst_fenetre_dashboard.png "QGIS - Paramétrage fenêtre 1")

Paramétrer ensuite les champs qui vont déterminer la taille, la position, la couleur de fond et la police de la première fenêtre Dashboard.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/12_1rst_fenetre_suite_dashboard.png "QGIS - Paramétrage fenêtre 1 suite")

Au fur et à mesure des modifications des valeurs de champs, lorsque vous enregistrez, vous devez voir apparaître la 1ere fenêtre Dashboard et les modifications apportées.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/12_1rst_fenetre_vue.png "QGIS - Rendu fenêtre 1")

Si aucune fenêtre n’apparaît au niveau de votre projet QGIS, jouez avec les différents champs (surtout label_offset x, label_offset y), cela peut être un problème de position de la fenêtre. Si elle n’apparaît toujours pas, reprenez les étapes précédentes.

### Etape 6 : Créer de nouvelles fenêtres dashboard

Pour créer une nouvelle fenêtre dashboard, passer la table attributaire en mode édition. Copiez la première ligne et coller la dans la partie blanche de la table attributaire. Une deuxième ligne identique apparaît.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/13_2nd_fenetre_dashboard.png "QGIS - Paramétrage fenêtre 2")

### Etape 7 : Paramétrer des requêtes dans les nouvelles lignes

Une fois la nouvelle entité crée, modifier les valeurs de champs de la seconde pour positionner la deuxième fenêtre sous la première.  Vous pouvez modifier le champs label_expression avec une requête sql qgis qui vous permettra d’afficher la valeur souhaitée dans cette deuxième fenêtre.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/14_2nd_fenetre_vue.png "QGIS - Rendu fenêtre 2")

### Exemple de table attributaire Dashboard et rendu

Ci-dessous, nous avons organisé la table avec une fenêtre par ligne comme suit : une 1ère fenêtre avec valeur « titre » suivie d'une fenêtre affichant une valeur « expression ».

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/15_ex_table_attrib.png "Table attributaire Dashboard partie 1")
![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/16_ex_table_attrib_suite.png "Table attributaire Dashboard partie 2")

### Exemple de requêtes utilisées

1- total de la somme des valeurs de la colonne pt_total de la couche Infos Communes

```sql
aggregate(layer:= 'Infos Communes', aggregate:='sum', expression:=pt_total)
```

2- total de la somme des valeurs de la collonne pt_total des entités sélectionnées sur la couche Infos Communes

```sql
aggregate(layer:= 'Infos Communes', aggregate:='sum', expression:=pt_total, filter:=is_selected('Infos Communes', $currentfeature )  )
```

3- Nombre de communes accompagnées (champ : actif, valeur : oui) dans la couche Infos Communes

```sql
aggregate(layer:= 'Infos Communes', aggregate:='count', expression:= actif, filter:= actif LIKE 'Oui' )
```

## Exemple de rendu

Le Dashboard est utilisé par le pôle SIG afin de contrôler les erreurs de saisies en temps réel par les communes et présenter un bilan général de l'avancement du projet.

Ci-dessous, un exemple d'affichage des bilans adresses (en haut à droite) après sélection d'une commune sous QGIS.

![QGIS label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_dashboard_calvados/gif_dashboard.gif "Table attributaire Dashboard partie 2")

----

## Auteur {: data-search-exclude }

--8<-- "content/team/tgro.md"

{% include "licenses/default.md" %}
