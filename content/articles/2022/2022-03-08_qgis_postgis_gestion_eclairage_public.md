---
title: Éclairage Public - Gestion et visualisation du réseau avec QGIS et PostGIS
authors:
    - Stéphane RITZENTHALER
categories:
    - article
comments: true
date: 2022-03-08
description: Création d'une base de données PostgreSQL/PostGIS pour la visualisation et la gestion du réseau d'éclairage public sur QGIS par une collectivité.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_postgis_eclairage_public/qgis_postgis_EP.png
license: CC-BY-SA
tags:
    - éclairage public
    - PostGIS
    - PostgreSQL
    - QGIS
    - SQL
---

# Éclairage Public - Gestion et visualisation du réseau avec QGIS et PostgreSQL/PostGIS

:calendar: Date de publication initiale : 8 mars 2022

## Introduction

Au sein de la Communauté de Communes de Thann-Cernay (68), nous avons mené une réflexion sur la possibilité d'utiliser QGIS pour gérer un réseau d'éclairage public après que le progiciel utilisé historiquement soit arrivé en fin de vie. En effet, la maintenance de cette solution n'étant plus assurée, les dysfonctionnements se sont multipliés jusqu'à ce qu'elle ne soit tout simplement plus opérationnelle. Ceci nous a conduit à réfléchir à de nouveaux outils de gestion de l'éclairage public, plus pérennes et mieux maîtrisés par les agents en interne. Après ce constat, nous nous sommes dit : et pourquoi pas QGIS ?

### Est-ce possible d'utiliser QGIS pour gérer un réseau d'éclairage public ?

Les besoins identifiés, par ordre de priorité, étaient les suivants :

* Visualiser le réseau et les objets le composant sur un fond de plan
* Offrir la possibilité d'éditer des cartes dans le contexte de DT-DICT
* Proposer un réseau topographiquement correct où les objets sont en relation les uns avec les autres
* Faciliter les interventions sur le réseau (historique, identification des objets sur lesquels intervenir, conséquences de l'intervention sur le réseau...)
* Permettre la gestion des stocks et anticiper sur les commandes de matériel

Dans une démarche d'analyse de faisabilité, nous avons monté un projet pour étudier comment le duo PostgreSQL/PostGIS et QGIS pourrait répondre à ces enjeux.

Je partage ici ce travail car il pourrait, je l'espère, être utile à d'autres géomaticiens qui souhaitent utiliser ce genre de solution au sein de leur collectivité.

![Eclairage public - Crédits : PxHere](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_postgis_eclairage_public/qgis_postgis_EP.png "Éclairage public - Crédits : PxHere"){: .img-center loading=lazy }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## La base de données relationnelle, un élément incontournable peu importe la solution future

![logo PostGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/postgis.jpg "logo PostGIS"){: .img-thumbnail-left }

La gestion de réseau ne peut se faire de manière efficace que si elle repose sur une base de données relationnelle solide. Le premier défi de cette étude fut de trouver la formule la plus adéquate pour nos besoins.

Et comme on ne ré-invente que très rarement quelque chose, il fallait observer ce qu'il pouvait se faire par ailleurs ! De nombreuses collectivités et IDG régionales ont réfléchi à la question du modèle de données.
Dans notre cas, nous nous sommes appuyés sur les travaux du CRIGE PACA, du département du Bas-Rhin, de la communauté de communes de la région de Molsheim Mutzig et de l'agglomération de la ville de Compiègne.

Voici le modèle de données que nous avons choisi pour notre test représenté grâce à [DBeaver](https://dbeaver.io/) :

![Diagramme du modèle de données exporté via DBeaver](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_postgis_eclairage_public/bdd_modele_dbeaver.png "Diagramme du modèle de données exporté via DBeaver"){: .img-center loading=lazy }

Le dictionnaire de données avec description de chaque table et de son contenu sous format .csv est disponible via [ce répertoire](https://github.com/stephyritz/ep_structure/tree/main/dictionnaire_donnees).

Afin d'automatiser le déploiement de ce modèle de données sur des bases PostgreSQL/PostGIS, nous avons écrit un script SQL à déployer sur une base de données dédiée à l'éclairage public.

Il y a deux scripts publiés dans [ce projet](https://github.com/stephyritz/ep_structure/tree/main/scripts_sql):

* `EP_init` permet de créer l'ensemble du schéma et des tables liés à la gestion de l'éclairage public. Il doit être exécuté dans une base de données précédemment créée.
* `EP_creatview` permet de générer des vues dans un schema spécifique. L'idée est de pouvoir ensuite exploiter ces "vues" à travers un client lourd type QGIS ou par le biais d'applications web.

## Import et transformation de l'existant

Dans un deuxième temps, il était nécessaire de transformer et importer les données existantes vers la base de données PostgreSQL que nous venons de créer.  
Cette démarche est propre à chaque organisme et dépend de l'organisation initiale des données de chacun. Le détail de cette étape  n'est pas décrit ici car non ré-utilisable pour d'autres cas d'usage. Pour information, nous avons utilisé FME pour configurer l'import des données sources stockées initialement "à plat" (sans relation entre les objets) depuis le logiciel GeoConcept vers PostgreSQL.

----

## Exploitation dans QGIS

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-thumbnail-left }

Une fois la partie la plus complexe réalisée, à savoir l'organisation du stockage des données et transformation, place à un peu plus de fun avec notre logiciel SIG favori !  
A noter qu'il a été important, vu la complexité des premières phases, d'automatiser les traitements dans la mesure du possible. En effet, il est alors beaucoup plus facile de revenir sur certains points, d'appliquer des mises à jour ou des modifications. C'est pourquoi nous avons par exemple utilisé des scripts SQL et des jobs FME afin de rendre le processus aisément reproductible. Le but est maintenant d'exploiter les données au sein de QGIS et de proposer des interfaces plaisantes aux utilisateurs pour interroger, créer ou modifier les données liées à l'éclairage public.

La réelle difficulté de l'exploitation de telles données relationnelles dans QGIS est, à mon sens, de "cacher" la manière dont est stockée l'information. En effet, l'utilisateur final trouve généralement lourd et complexe le fait de stocker les informations dans de multiples tables, bien que cela soit la meilleure solution en termes de bases de données...  
Il faut donc veiller à ce que la personne du métier puisse créer/mettre à jour les données ou simplement les visualiser sans être obligé de jongler entre les différentes tables de postgreSQL.

Dans le cadre de cette étude, nous avons opté pour la création de 2 projets QGIS distincts en fonction du type d'utilisateurs. Le premier projet est à destination des utilisateurs qui ne souhaitent que consulter les données. Le second projet est destiné au gestionnaire du projet, avec un profil plus expert, qui s'occupera de la création et des mises à jours des données.

Le premier projet fait appel aux "vues" précédemment créées grâce au script SQL. Ensuite, grâce à une symbologie particulière dans QGIS, nous pouvons proposer un visuel mettant en avant le type de lampe (led, Ballon fluorescent, Sodium Hate Pression, etc...), le nombre de points lumineux sur le mât ou encore si le réseau est aérien ou souterrain.  
Voici un exemple de ce que nous pourrions voir à l'écran :

![Exemple de rendu sur QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_postgis_eclairage_public/qgis_exemple_rendu.png "Exemple de rendu sur QGIS"){: .img-center loading=lazy }

Un panel de styles est proposé à l'observateur en fonction de son besoin. Un autre exemple serait de représenter de la même couleur tous les points lumineux qui dépendent d'une même armoire électrique. Nous pouvons ici utiliser toute la puissance de QGIS pour styliser la donnée telle que nous souhaitons la voir apparaître.

Au delà de l'aspect visuel, qui répond déjà à un besoin prioritaire de la collectivité, l'utilisation des formulaires personnalisables de QGIS offre également la possibilité aux utilisateurs "d'interroger" de manière interactive chacun des objets constituant le réseau. Ainsi, grâce à un clic dans QGIS, nous pouvons traduire les relations entre les différents éléments du réseau. Par exemple, ce mât contient 2 points lumineux et un accessoire de type "indicateur de vitesse".

Ces mêmes formulaires, en intégrant les relations entre couches dans le projet QGIS, vont permettre à l'utilisateur expert de saisir et modifier de l'information sans devoir éditer chacune des tables séparément.

----

## Conclusion

Le POC s'est arrêté à ce stade car la preuve a été faite que le duo QGIS/PostgreSQL pouvait bien répondre aux principaux besoins mentionnés. La suite des développements se serait orientée vers une mise en production opérationnelle.  Logiquement, il faudrait poursuivre en améliorant l'ergonomie des formulaires grâce [aux outils intégrés dans QGIS](http://piece-jointe-carto.developpement-durable.gouv.fr/NAT002/QGIS/formations/FOAD_PERF_QGIS34/pdf/M09_Formulaires_papier.pdf) ou [via QT comme dans cet exemple](https://archeomatic.wordpress.com/2012/03/06/qgis-qtcreator-creer-son-formulaire-dans-qgis/). De même, des développements supplémentaires pourraient être fait pour créer des boutons dédiés aux actions d'édition réalisées le plus couramment, pourquoi pas un plugin spécifique à la gestion de l'éclairage public...

Enfin, l'aspect consultation pourrait être externalisé via une carte interactive directement accessible via le navigateur. Cela permettrait aux utilisateurs de visualiser les données sans devoir passer par un client SIG. La gestion des stocks n'a finalement pas été intégrée à ce premier travail. Pour poursuivre dans cette direction, il faudrait probablement enrichir le modèle de données par des tables liées au matériel.

Une coopération entre collectivités locales rencontrant les mêmes besoins pourrait par exemple se traduire par un financement commun d'un outil adossé à QGIS plus soigné que ces premiers tests.

Merci à la Communauté de Communes Thann-Cernay grâce à qui nous avons pu faire ce premier test. Celui-ci donne beaucoup de perspectives sur le sujet et témoigne de l'intérêt pour les collectivités de porter des projets open source ensemble.

[Lien vers le Github du projet :fontawesome-brands-github:](https://github.com/stephyritz/ep_structure/){: .md-button }
{: align=middle }

----

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-sa.md" %}
