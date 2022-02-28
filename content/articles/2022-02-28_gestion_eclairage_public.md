---
ltitle: "Eclairage Public - Gestion et visualisation du réseau avec QGIS et Postgresql/Postgis"
authors: ["Stéphane RITZENTHALER"]
categories: ["article"]
date: "2021-09-24 17:30"
description: "Création d'une base de données Postgresql/Postgis pour la visualisation et la gestion du réseau d'éclairage public sur QGIS par une collectivité."
license: "CC-BY-SA"
tags: "Eclairage,PostgreSQL,PostGIS,QGIS,sql"
---

# Eclairage Public - Gestion et visualisation du réseau avec QGIS et Postgresql/Postgis

:calendar: Date de publication initiale : 24 septembre 2021

**Mots-clés :** Eclairage | PostgresSQL | PostGIS | Collectivité| QGIS

## Est-ce possible d'utiliser QGIS pour gérer un réseau d'éclairage public ?

Cette question s'est posée dès lors que la solution précédente a affiché ses limites. Pourquoi pas customiser l'outil généraliste QGIS pour en faire une plateforme de gestion du réseau d'éclairage public.
Les besoins identifiés, par ordre de priorité, étaient les suivants : 
* Visualiser le réseau et les objets le composant sur un fond de plan
* Offrir la possibilité d'éditer des cartes dans le contexte de DT-DICT
* Proposer un réseau topographiquement correct où les objets sont en relations les uns avec les autres
* Faciliter les interventions sur le réseau (historique, identifications des objets sur lesquels intervenir, conséquence de l'intervention sur le réseau, etc...)
* Permettre la gestion des stocks et anticiper sur les commandes de matériel

Dans une démarche d'analyse de faisabilité, nous avons monté un projet pour étudier comment le duo Postgres/Postgis et QGIS pourrait répondre à ces enjeux.

Je partage ici ce travail car il pourrait, je l'espère, être utile à d'autres géomaticiens qui souhaitent utiliser ce genre de solution au sein de leur collectivité.
  

## La base de données relationnelle, un élément incontournable peu importe la solution future

La gestion de réseau ne peut que se faire de manière efficace si elle repose sur une base de données relationnelles solide. Le premier défi de cette étude fut de trouver la formule la plus adéquate pour nos besoins.
Et comme on ne ré-invente que très rarement quelque chose, il fallait observer ce qu'il pouvait se faire par ailleurs ! De nombreuses collectivités et IDG régionales ont réfléchi à la question du modèle de données.
Dans notre cas, nous nous sommes appuyés sur les travaux du CRIGE PACA, du département du Bas-Rhin, de la communauté de communes de la région de Molsheim Mutzig et de l'agglomération de la ville de Compiègne.

Voici le modèle de données que nous avons choisi poour notre test représenté grâce à [DBeaver](https://dbeaver.io/) :

![Image DB structure](https://user-images.githubusercontent.com/34446202/134654337-71c2f48c-94d6-4539-8611-cecce56a88d1.png)

Le dictionnaire de données avec description de chaque table et de son contenu sous format .csv est disponible via [ce repertoire](https://github.com/stephyritz/ep_structure/tree/main/dictionnaire_donnees)


Afin d'automatiser le déploiement de ce modèle de données sur des bases postgres/postgis, nous avons écrit un script sql à déployer sur une base de données dédiée à l'éclairage public. 

Il y a deux scripts publiés dans [ce projet] (https://github.com/stephyritz/ep_structure/tree/main/scripts_sql):

* "EP_init" permet de créer l'ensemble du schéma et des tables liées à la gestion de l'éclairage public. Il doit être executé dans une base de données précédemment créée.
* "EP_creatview" permet de générer des vues dans un schema spécifique. L'idée est de pouvoir ensuite exploiter ces "vues" à travers un client lourd type QGIS ou par le biais d'application web.


## Import et transformation de l'existant

Dans un deuxième temps, il était nécessaire de transformer et importer les données existantes depuis le système d'information existant vers la base de données postgresql que nous venons de créer.
Cette démarche est propre à chaque organisme et dépend de l'organissation des données de chacun. Je ne vais pas détailler plus le travail réalisé pour le compte de la Communauté de Communes Thann-Cernay.
Nous avons utilisé FME pour configurer l'import des données sources stockées "à plat" (sans relation entre les objets) depuis le logiciel GeoConcept vers Postgresql.

## Exploitation dans QGIS
Une fois la partie la plus complexe réalisée, à savoir organisation du stockage des données et transformation, place à un peu plus de fun avec notre logiciel SIG favori! 
A noter qu'il a été important, vu la complexité des premières phases, d'automatiser les traitements dans la mesures du possible. En effet, il est alors beaucoup plus facile de revenir sur certains points, d'appliquer des mises à jour ou des modifications sur un processus reproductible aisément. Le but est maintenant d'exploiter les données au sein de QGIS et de proposer des interfaces plaisantes aux utilisateurs pour interroger, créer ou modifier les données liées à l'éclairage public.

La réelle difficulté de l'exploitation de telles données relationnelles dans QGIS est, à mon sens, de "cacher" la manière dont est stockée l'information. En effet, l'utilisateur final trouve généralement lourd et complexe le fait de stocker les informations dans de multiples tables, bien que cela soit la meilleure solution en termes de bases de données..
Il faut donc veiller à ce que la personne du métier puisse créer/mettre à jour les données ou simplement les visualiser sans être obliger de jongler entre les différentes tables postgres.

Dans le cadre de cette étude, nous avons opté pour la création de 2 projets qgis distincts en fonction du type d'utilisateurs. Le premier projet est à destination des utilisateurs qui ne souhaitent que consulter les données. Le second projet est destiné au gestionaire du projet, avec un profil plus expert, qui s'occupera de la création et des mises à jours des données.

Le premier projet fait appel aux vues précédemment crées grâce au script sql. Ensuite, grâce à une symbologie particulière dans QGIS, nous pouvons proposé un visuel mettant en avant le type de lampe (led, Ballon fluorescent, Sodium Hate Pression, etc...), le nombre de point lumineux sur le mât ou encore si le réseau est aérien ou souterrain.
Voici un exemple de ce que nous pourrions voir à l'écran :
![Image visuel QGIS](https://user-images.githubusercontent.com/34446202/134685292-139cd864-bf10-4d41-a24e-f8f29df6dc47.png)

Un panel de style est proposé à l'observateur en fonction de son besoin. Un autre exemple serait de représenter de la même couleur tous les points lumineux qui dépendent d'une même armoire électrique. Nous pouvons ici utiliser toute la puissance de QGIS pour styliser la donnée telle que nous souhaitons la voir apparaître.

Au delà de l'aspect visuel, qui répond déjà a un besoin prioritaire de la collectivité, l'utilisation des formulaire customisables de QGIS, offre également la possibilité aux utilisateurs "d'interroger" de manière interractive chacun des objets constituant le réseau. Ainsi, grâce à un clic dans QGIS, nous pouvons traduire les relations entre les différents éléments du réseau. Par exemple, ce mât contient 2 points lumineux et un accessoire de type "indicateur de vitesse".


Ces mêmes formulaires, en intégrant les relations entre couches dans le projet QGIS, va permettre à l'utilisateur expert de saisir et modifier de l'information sans devoir éditer chacune des tables séparément.

 ## Conclusion
 
Le POC s'est arrêté à ce stade car la preuve a été faite que le duo QGIS/Postgresql pouvait bien répondre aux principaux besoins mentionnés. La suite des développements seraient déjà orientés vers une mise en production opérationnelle. Logiquement, il faudrai poursuivre en améliorant l'ergonomie des formulaires via QT par exemple. De même, des développements supplémentaires pourraient être fait pour créer des boutons dédiés aux actions d'édition réalisées le plus couramment, pourquoi pas un plugin spécifique à la gestion de l'éclairage public...

Enfin, l'aspect consultation pourrait être externalisée via une carte interactive directement accessible via le naviguateur. Cela permettrait aux utilisateurs de visualiser les données sans devoir passer par un client SIG. L'enjeu concernant la gestion des stocks n'a finalement pas été intégré à ce premier travail.

Une coopération entre collectivités locales rencontrant les mêmes besoins pourrait par exemple se traduire par un financement commun d'un outil adossé à QGIS plus soigné que ces premiers tests.   

Merci à la Communauté de Communes Thann-Cernay grâce à qui nous avons pu faire ce premier test. Celui-ci donne beaucoup de perspectives sur le sujet et témoigne de l'intérêt pour les collectivités de porter des projets opensources ensemble. 

[Lien vers le Github du projet](https://github.com/stephyritz/ep_structure)

## Auteur

--8<-- "content/team/mbos.md"

{% include "licenses/cc4_by-sa.md" %}
