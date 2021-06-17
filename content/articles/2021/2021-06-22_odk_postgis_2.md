---
title: "Open Data Kit pour la collecte de données géographiques dans PostGIS (1/3)"
authors: ["Mathieu BOSSAERT"]
categories: ["article"]
date: "2021-06-08 10:20"
description: "Premier article de présentation de la suite Open Data Kit (ODK) et son intégration au SI du CEN d'Occitanie et dans les processus métiers."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/odk_and_postgresql.png"
tags: "ODK,Open Data Kit,PostgreSQL,PostGIS,collecte,Android	"
---

# ODK pour la collecte de données géo dans PostGIS (2/3)

:calendar: Date de publication initiale : 22 juin 2021

**Mots-clés :** ODK | PostgresSQL | PostGIS | Android

![ODK PostGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/Central2PG.png "ODK + PostGIS"){: .img-rdp-news-thumb }

Aprés vous avoir présenté la place les outils proposés par ODK et la place qu'ils occupent dans notre SI centré sur PostGIS, ce second article illustre à travers notre formulaire généraliste l'utilisation des différents "widgets" à notre disposition.
Des extraits du "XLSForm" du formualaire complètent les captures d'écrans pour montrer l'utilisation des différentes colonnes de la feuille de calcul "survey" et de la feuille de calcul "Choices". Dans ces extraits, nous n'avons conservé que les colonnes renseignées pour en faciliter la lecture.
Le fichier XLSform de notre formulaire est disponible en [bas de l'article](#ressources_complémentaires).

Dans un dernier article, nous verrson comment les données collectées sur les téléphones grâce à ce formulaire intègrent notre base de données PostGIS et sont ainsi mises à disposition de l'ensemble de l'équipe à travers les différents outils que nous utilisons.

<!--[1ère partie : Introduction à ODK :fontawesome-solid-step-backward:](https://static.geotribu.fr/articles/2021/2021-06-08_odk_postgis_1/){: .md-button }
[3ème partie : Récupération des données dans notre SI :fontawesome-solid-step-forward:](#){: .md-button }
{: align=middle }-->

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

Traditionnellement, les naturalistes et les écologues du CEN notaient toutes leurs observations sur des carnets de terrain papier, et les informatisaient au retour au bureau, via une interface web, un tableur ou une couche SIG. Dans le cas des tableurs et couches SIG -fichiers-, une étape supplémentaire était nécessaire pour consolider les données saisies dans notre base de données PostGIS.

En conséquence, il pouvait s'écouler plusieurs mois avant que les observations d'un membre de l'équipe soient visibles dans le SI par les autres collègues. La création de notre outil web interne en 2009 a été un premier élément de réponse technique à cette difficulté de consolidation et de partage rapide des données.
Nous avions eu en 2007 une expérience de collecte de données sur PDA (avec ArcPad) et l'absence de double saisie nous avait beaucoup enthousiasmé.

Cette présentation faite au FOSS4G-fr de 2018 reprend l'historique de notre SI et présente notre utilisation d'ODK : 

[16mai_Cauchy_Bossaert-CENLR_0.pdf|attachment](upload://u9ABQjmft6uNNSniqHtUMPstwJz.pdf) (3.0 MB)

### Logique du formulaire

Le formulaire décrit ici est notre formulaire principal, initié en 2016. La version initiale permettait de collecter des informations basiques sur les espèces et les habitats. Chaque révision successive a apporté son lot d'amélioration, et des question "adaptatives" dont les réponses possibles dépendaient par exemple de l'espèce sélectionnée (ex. pas de têtard si on a vu un oiseau). EN 2019, avec le travail de Jean Baïsez, le formulaire est devenu une sorte de carnet de note, dans lequel on peut noter ses observations d'espèces et d'habitats, mais aussi des pressions ou des menaces sur les milieux naturels. Toutes ses données sont géoréférencées (point, lignes ou polygones) et peuvent être documentées de photos prise par le téléphone. Ces photos peuvent être annotées.

EN 2021, le système de préférences a été amélioré et les attentes évoquées par les collègues à la fin de la saison 2020 ont été satisfaites.

Notre formulaire est constitué de deux boucles imbriquées. Aprés avoir renseigné les informations de base du relevé (contexte, observateur...), il nous est proposé de renseigner une localité (objet géographique), puis de renseigner une ou plusieurs observations sur cette localité. Aprés la dernière observation de la localité courante, il est proposé de saisir une nouvelle localité...

Voici un schéma illustrant la logique du formulaire, que l'on peut résumer ainsi :

[![Logique du formulaire](https://si.cen-occitanie.org/wp-content/uploads/2021/05/geotribu/logique_formulaire.jpeg "Logique du formulaire"){: loading=lazy width=300 }](https://si.cen-occitanie.org/wp-content/uploads/2021/05/geotribu/logique_formulaire.jpeg){: data-mediabox="lightbox-gallery" data-title="Logique du formulaire"}

## Captures d'écran / collecte de données

### Ecran d'accueil d'ODK Collect 

[![écran d'accueil de Collect](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ecran_accueil_ODK_Collect.png "Ecran d'accueil d'ODK Collect"){: loading=lazy width=300 }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ecran_accueil_ODK_Collect.png){: data-mediabox="lightbox-gallery" data-title="Ecran d'accueil d'ODK Collect"}

### Choix du formulaire à renseigner -> SICEN

[![Choix du formulaire à renseigner](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/liste_des_formulaires.png "Choix du formuliare à renseigner"){: loading=lazy width=300 }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/liste_des_formulaires.png){: data-mediabox="lightbox-gallery" data-title="Choix du formulaire à renseigner"}

Les 3 premiers écrans présentent le paramétrage de l'application. A la première utilisation, les fonctionnalités seront toutes activées par défaut. Libre à chacun de désactiver celles qui lui semblent provisoirement ou définitivement inutiles.
A l'utilisation suivante, chacune des fonctionnalités sera proposée dans l'état d'activation qui était le sien lors de la précédente utilisation du formulaire. Il sera là encore possible de valider ou modifier chacun de ces choix.
Les fonctionnalités désactivées ici seront masquées pendant l'utilisation du formulaire. 

**Au fur et à mesure de la saisie, l’icône de la disquette permet d'enregistrer le formulaire en cours sur le téléphone.**

### Écran de paramétrage n°1 -> l'identité de l’utilisateur
Les champs sont remplis par défaut avec les valeurs saisies dans les paramètres généraux de l'application

[![Métadonnées relatives à l'utilisateur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/metadonnees_utilisateur.png){: loading=lazy width=300 }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/metadonnees_utilisateur.png){: data-mediabox="lightbox-gallery" data-title="Choix du formulaire à renseigner"}
[![Préférences de l'utilisateur - Choix des possibilités cartographiques](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/preferences_utilisateur_geo.png){: loading=lazy width=300 }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/preferences_utilisateur_geo.png){: data-mediabox="lightbox-gallery" data-title="Choix du formulaire à renseigner"}
[![Préférences de l'utilisateur - Types et thématiques des données à saisir](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/preferences_utilisateur_thematique.png){: loading=lazy width=300 }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/preferences_utilisateur_thematique.png){: data-mediabox="lightbox-gallery" data-title="Choix du formulaire à renseigner"}{: loading=lazy width=300 }]

### Écran de paramétrage n°2 -> types de géométries créées

 * points
 * lignes
 * polygones

Voici l'extrait correspondant de la feuille survey (le principe est le mêm pour l'écran précédent et le 3ème) : 
* le groupe (begin_group et end_group) permet de faire apparaitre les questions dans un même écran
* les questions sont des select_one (une seule option à choisir)
* la liste utilisée dans la feuille choicies s'appelle "boolean"
* et par défaut (colonne **default**) la question prend la dernière valeur enregistrée (**${last-saved#question_concernee**} elle existe, sinon "true"

| **type**           | **name**          | **label** | **required** | **default**                                      |
| ------------------ | ----------------- | --------- | ------------ | ------------------------------------------------ |
| select_one boolean | utiliser_geopoint | Points    | yes          | coalesce(${last-saved#utiliser_geopoint},’true’) |
| select_one boolean | utiliser_geotrace | Lignes    | yes          | coalesce(${last-saved#utiliser_geotrace},’true’) |
| select_one boolean | utiliser_geoshape | Polygones | yes          | coalesce(${last-saved#utiliser_geoshape},’true’) |
| end group          |                   |           |              |                                                  |

### Écran de paramétrage n°3 -> Types de données (thématiques) et paramétrage de l'autocomplétion

Le dernier écran permet de choisir le nombre de caractères à saisir dans le recherche des espèces avant de déclencher l'interrogation du référentiel. 3 est le minimum, 7 le maximum (pour permettre l'utilisation du "code taxon" par exemple "ERI RUB") . Notez que la dernière question n'est pas visible et nécessite de scroller l'écran. La version à paraitre de Collect va permettre de [regouper plusieurs questions proposant des réponses identiques sous la forme d'une grille](https://docs.getodk.org/form-question-types/#grid-of-selects-on-the-same-screen) et permettre ansi un gain de place.

L'ensemble de ces paramètres est concaténé dans une chaîne nommée "preferences_utilisateur". C'est un champ de type **calculate** qui réalise la concaténation dans la colonne **calculation**

| **type**  | **name**                | **calculation**                                              |
| --------- | ----------------------- | ------------------------------------------------------------ |
| calculate | preferences_utilisateur | concat(if(${utiliser_geopoint} = 'true','point',''),if(${utiliser_geotrace} = 'true','line',''),if(${utiliser_geoshape} = 'true','polygon',''),if(${animalia} = 'true','animalia',''),if(${plantae} = 'true','plantae',''),if(${fungi} = 'true','fungi',''),if(${habitat} = 'true','habitat',''),if(${pression_menace} = 'true','pression_menace',''),if(${observation_generale} = 'true','observation_generale',''),${nb_lettres}) |


Une fois les paramétrages vérifiés et ou modifiés l'utilisateur peut choisir l'étude pour laquelle le relevé est effectué.

### Choix de l'étude et du protocole

Ces deux référentiels sont gérés dans des fichiers csv externes associés au formulaire. Les fichiers sont mentionnés dans la colonne **appearence** des lignes 2 et 3 de l'extrait ci-dessous (search('etudes') et search('protocole')).
L'utilisation combinée de l'apparence **quick** permet de passer automatiquement à la question suivante quand une option est selectionnée.
La feuille de calcul choices nous renseigne sur la structure de ces fichiers csv. Les colonnes nom_etude_id et libelle_id contiennent les identifiants à stocker, tandis que les colonnes nom_etude et libelle contiennent les "noms" à afficher dans les listes.
Cela permet de les mettre à jour sur le téléphone sans avoir à mettre à jour le formulaire sur le serveur.
Nous verrons plus tard avec le référentiel taxonomique que le stockage externe de ces référentiels nous offre des possibilités de recherche intéressantes. 

[![choix de l'étude](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/liste_de_choix_etudes.png "choix de l'étude"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/liste_de_choix_etudes.png){: data-mediabox="lightbox-gallery" data-title="choix de l'étude"} 
[![métadonnées utilisateur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/liste_de_choix_protocole.png "métadonnées utilisateur"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/liste_de_choix_protocole.png){: data-mediabox="lightbox-gallery" data-title="métadonnées utilisateur"} 

#### Extrait de la feuille survey

|   | **type**                  | **name**        | **label**          | **required** | **appearance**             |
| - | ------------------------- | --------------- | ------------------ | ------------ | -------------------------- |
| 1 | begin group               | protocole_etude | Protocole et étude |              |                            |
| 2 | select_one list_etude     | id_etude        | Etude              | yes          | quick search('etudes')     |
| 3 | select_one list_protocole | id_protocole    | Protocole          | yes          | quick search('protocoles') |
| 4 | end group                 |                 |                    |              |                            |

#### Extrait de la feuille choices

| **list_name**  | **name**     | **label** |
| -------------- | ------------ | --------- |
| list_etude     | nom_etude_id | nom_etude |
| list_protocole | libelle_id   | libelle   |

A terme nous aimerions générer dynamiquement et régulièrement la listedes études pour ne faire apparaître que les études en cours et pourquoi pas seulement celles qui concernent l’utilisateur de l'application.
La même chose pourrait être envisagée pour les protocoles.
Une fois ces paramètres de "session" renseignés, nous pouvons commencer la saisie de données proprement dite.

### Création d'une localité
Il s'agira d'un point, d'une ligne ou d'un polygone. Cette fonctionnalité "géographique" du formulaire a été décrite dans la première partie de cet article.

[![Choix du type de géoréférencement de l'emplacement courant](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/georeferencement_choix_du_point.png "Choix du type de géoréférencement de l'emplacement courant"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/georeferencement_choix_du_point.png){: data-mediabox="lightbox-gallery" data-title="Choix du type de géoréférencement de l'emplacement courant"} 

Le GPS peut vous aider à dessiner automatiquement points, lignes et polygones, que vous pouvez aussi dessiner à la main sur l'écran. L'automatisation peut être paramétrée selon la distance maximale ou le temps de parcours entre deux points. Une précision minimale du GPS peut aussi être configurée dans le formualire pour interdire des localisation trop peu précises.
[![localisation assistée par le GPS du téléphone](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/cartographie_assistee_par_gps_affichage_precision.png "localisation assistée par le GPS du téléphone"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/cartographie_assistee_par_gps_affichage_precision.png){: data-mediabox="lightbox-gallery" data-title="localisation assistée par le GPS du téléphone"} 
[![coordonnées du point GPS collecté et précision du capteur lors de l'enregistrement](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/affichage_coordonnees_point_enregistre.png){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/affichage_coordonnees_point_enregistre.png){: data-mediabox="lightbox-gallery" data-title="coordonnées du point GPS collecté et précision du capteur lors de l'enregistrement"} 

#### Extrait de la fauille survey
  
| -- | **type**               | **name**                  | **label**                     | **calculation**                              | **required** | **appearance**      | **default** | **relevant**                                | **choice_filter**                           | **bind::odk:length** | **body::accuracyThreshold** |
| -- | ---------------------- | ------------------------- | ----------------------------- | -------------------------------------------- | ------------ | ------------------- | ----------- | ------------------------------------------- | ------------------------------------------- | -------------------- | --------------------------- |
| 1  | begin repeat           | emplacements              | Emplacements                  |                                              |              |                     |             |                                             |                                             |                      |                             |
| 2  | begin group            | localites                 | ${heure_localite}             |                                              |              |                     |             |                                             |                                             |                      |                             |
| 3  | begin group            | loc                       |                               |                                              |              | field-list          |             |                                             |                                             |                      |                             |
| 4  | calculate              | heure_localite            |                               | concat(‘à ‘,format-date-time(now(),"%H:%M")) |              |                     |             |                                             |                                             |                      |                             |
| 5  | select_one methode_geo | methode_geo               | méthode de géoréférencement ? |                                              | yes          |                     | point       |                                             | contains(${preferences_utilisateur},filter) |                      |                             |
| 6  | decimal                | longitude                 | longitude (WGS 84)            |                                              | yes          |                     |             | ${methode_geo} = 'long_lat'                 |                                             |                      |                             |
| 7  | decimal                | latitude                  | latitude (WGS 84)             |                                              | yes          |                     |             | ${methode_geo} = 'long_lat'                 |                                             |                      |                             |
| 8  | geopoint               | point_auto                | point automatique             |                                              | yes          |                     |             | ${methode_geo} = 'point_auto'               |                                             |                      | 5                           |
| 9  | geopoint               | point                     | point sur carte               |                                              | yes          | quick placement-map |             | ${methode_geo} = 'point'                    |                                             |                      |                             |
| 10 | geotrace               | ligne                     | ligne                         |                                              | yes          |                     |             | ${methode_geo} = 'ligne'                    |                                             | 10000                |                             |
| 11 | calculate              | longueur_ligne            |                               | distance(${ligne})                           |              |                     |             | ${methode_geo} = 'ligne’                    |                                             |                      |                             |
| 12 | calculate              | longueur_ligne_arrondie   |                               | round(${longueur_ligne},2)                   |              |                     |             | ${methode_geo} = 'ligne’                    |                                             |                      |                             |
| 13 | geoshape               | polygone                  | polygone                      |                                              | yes          |                     |             | ${methode_geo} = 'polygone’                 |                                             | 10000                |                             |
| 14 | calculate              | surface_polygone          |                               | area(${polygone})                            |              |                     |             | ${methode_geo} = 'polygone’                 |                                             |                      |                             |
| 15 | calculate              | surface_polygone_arrondie |                               | round(${surface_polygone}, 2)                |              |                     |             | ${methode_geo} = 'polygone’                 |                                             |                      |                             |
| 16 | end group              |                           |                               |                                              |              |                     |             |                                             |                                             |                      |                             |
| 17 |                        |                           |                               |                                              |              |                     |             |                                             |                                             |                      |                             |
| 18 | end group              |                           |                               |                                              |              |                     |             |                                             |                                             |                      |                             |
| 19 | end repeat             |                           |                               |                                              |              |                     |             |                                             |                                             |                      |                             |

Le **begin repeat** démarre une boucle de création de localités.
Le groupe qui suit directement ce repeat (ligne n°2) encapsule l'ensemble des éléments contenus dans la boucle et permettra de nommer chaque instance de la boucle, ici avec la valeur du champ calculé **heure_localite**.
Cela nous sera utile pour rerouver une donnée saisie plus tôt.
La colonne **choice_filter**, utilisée pour la question **methode_geo** permet de ne proposer que les options de la feuille **choices** pour lesquelles la valeur "filter" est contenue dans les "préferences utilisateur" calculée plus haut (écrans 2 et 3).
La colonne **relevant** permet de mentionner si la question est pertinente (à afficher), et dans quel contexte. Un test peut-être utilisé pour déterminer sa valeur (qui est 'true' par défaut). Ici donc seul le widget carto correpondant à la réponse donnée à la question "methode_geo" (ligne 5) sera affiché. 


#### Extrait de la feuille choices

| **list_name** | **name**   | **label**             | **filter** |
| ------------- | ---------- | --------------------- | ---------- |
| methode_geo   | point_auto | point automatique     | point      |
| methode_geo   | point      | point sur une carte   | point      |
| methode_geo   | ligne      | ligne                 | line       |
| methode_geo   | polygone   | polygone              | polygon    |
| methode_geo   | long_lat   | Saisie de coordonnées | point      |

### Saisie d'une ou plusieurs observations à cet endroit
Une fois l'emplacement créé, nous allons pouvoir y créer autant d'observations que nous le souhaitons, de chacun des types d'observations autorisés dans les paramétrages du formulaire.

[![choix du type d'observation à renseigner](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/choix_type_d_observation.png "choix du type d'observation à renseigner"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/choix_type_d_observation.png){: data-mediabox="lightbox-gallery" data-title="choix du type d'observation à renseigner"} 

Commençons par une espèce végétale

[![recherche d'une espèce végétale](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/recherche_d_une_espece_autocompletion.png "recherche d'une espèce végétale"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/recherche_d_une_espece_autocompletion.png){: data-mediabox="lightbox-gallery" data-title="recherche d'une espèce végétale"} 

### Propositions des taxons de référence et des synonymes qui correspondent aux lettres tapées
D'abord les taxons de rangs supérieurs puis les espèces et sous espèces.

[![propositions de taxons correspondant à la recherche](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/recherche_d_une_espece_propositions.png "propositions de taxons correspondant à la recherche"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/recherche_d_une_espece_propositions.png){: data-mediabox="lightbox-gallery" data-title="propositions de taxons correspondant à la recherche"} 

### Renseignement de l'effectif observé
L'espèce mentionnée a-t-elle été observée ?
[![l'espèce a-t-elle été observée ?](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/le_taxon_a_t_il_ete_observe.png "l'espèce a-t-elle été observée ?"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/le_taxon_a_t_il_ete_observe.png){: data-mediabox="lightbox-gallery" data-title="l'espèce a-t-elle été observée ?"}
Si oui, les écrans suivants (ou leurs homologues pour la Faune sont affichés)

Ici pour les espèces végétales il s'agit d'un effectif par classes d’abondance

[![abondance de l'espèce](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/renseignement_abondance_espece.png "abondance de l'espèce"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/renseignement_abondance_espece.png){: data-mediabox="lightbox-gallery" data-title="abondance de l'espèce"} 

### Informations sur la "qualité" de la donnée

L'observation pourra être retrouvée dans la navigation du formulaire, avec l’heure de l'emplacement et l’espèce observée.

[![éléments de qualité de la donnée](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/qualite_donnee_determination_sensibilite_fiabilite.png "éléments de qualité de la donnée"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/qualite_donnee_determination_sensibilite_fiabilite.png){: data-mediabox="lightbox-gallery" data-title="éléments de qualité de la donnée"} 

[![modalité de detrmination](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/modalite_de_determination.png "modalité de detrmination"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/modalite_de_determination.png){: data-mediabox="lightbox-gallery" data-title="modalité de detrmination"} 

### Renseignement de détails optionnels, prise de photo

[![prendre une photo ?](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/proposition_prise_de_photo_et_remarque.png "prendre une photo ?"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/proposition_prise_de_photo_et_remarque.png){: data-mediabox="lightbox-gallery" data-title="prendre une photo ?"} 

[![prendre un photo](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/prise_de_photo.png "prendre un photo"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/prise_de_photo.png){: data-mediabox="lightbox-gallery" data-title="prendre un photo"} 

### Annotation de la photo
Cela peut être utile pour les photos de site dans le cas d'observations de type pression/menace
[Photos mobilisables dans QGIS par la suite](https://si.cen-occitanie.org/?p=191) 

[![métadonnées utilisateur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/annotation_photo.png "métadonnées utilisateur"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/annotation_photo.png){: data-mediabox="lightbox-gallery" data-title="métadonnées utilisateur"} 

[![métadonnées utilisateur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/visualisation_image_finale.png "métadonnées utilisateur"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/visualisation_image_finale.png){: data-mediabox="lightbox-gallery" data-title="métadonnées utilisateur"} 

### Ajout d'une observation

Si oui on revient à la saisie d'une observation sur l'emplacement courant.

[![Ajouter une observation à l'emplacmeent courant ?](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/iteration_boucle_observation.png "Ajouter une observation à l'emplacmeent courant ?"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/iteration_boucle_observation.png){: data-mediabox="lightbox-gallery" data-title="Ajouter une observation à l'emplacmeent courant ?"} 

Si non il nous est proposé d'ajouter une nouvelle localité

[![Ajouter un nouvel emplacement au relevé ?](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/iteration_boucle_emplacement.png "Ajouter un nouvel emplacement au relevé ?"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/iteration_boucle_emplacement.png){: data-mediabox="lightbox-gallery" data-title="Ajouter un nouvel emplacement au relevé ?"} 

Si oui on revient à l'ajout d'une localité (point, ligne ou polygone)
Si non, on finalise le formulaire en renseignant la présence d'éventuels accompagnateurs 

### Renseignement des accompagnateurs éventuels

[![Ajouter un ou plusieurs accompagnateurs](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ajout_accompagnateur.png "Ajouter un ou plusieurs accompagnateurs"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ajout_accompagnateur.png){: data-mediabox="lightbox-gallery" data-title="Ajouter un ou plusieurs accompagnateurs"} 

Finalisation du formulaire.

[![Fin du formulaire](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/fin_du_formulaire.png "Fin du formulaire"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/fin_du_formulaire.png){: data-mediabox="lightbox-gallery" data-title="Fin du formulaire"}  

L’icône représentant une flèche montrant un point permet de naviguer dans les observations déjà saisie pour les vérifier ou les modifier.

[![Navigation dans les données collectées](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/accueil_navigation_donnees_collectees.png "Navigation dans les données collectées"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/accueil_navigation_donnees_collectees.png){: data-mediabox="lightbox-gallery" data-title="Navigation dans les données collectées"} 

En cliquant sur le groupe répétitif "Emplacements", on accède à la liste des emplacement du formualaire.

[![Liste des lieux](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/navigation_liste_emplacements_sessions.png "Liste des lieux"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/navigation_liste_emplacements_sessions.png){: data-mediabox="lightbox-gallery" data-title="Liste des lieux"} 

En cliquant sur l'emplacement désiré, on accède au détail le concernant.

[![métadonnées utilisateur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/resume_emplacement_anterieur.png "métadonnées utilisateur"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/resume_emplacement_anterieur.png){: data-mediabox="lightbox-gallery" data-title="métadonnées utilisateur"} 

Enfin en cliquant sur le groupe répétitif "Observations" nous accédons à la liste des observations ratachées à l'emplacement.

[![Observations rattachées à l'emplacement](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/navigation_liste_observations_emplacement_1.png "Observations rattachées à l'emplacement"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/navigation_liste_observations_emplacement_1.png){: data-mediabox="lightbox-gallery" data-title="Observations rattachées à l'emplacement"} 

et au détail de chacune d'elles : 

[![métadonnées utilisateur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/resume_observation_anterieure.png "métadonnées utilisateur"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/resume_observation_anterieure.png){: data-mediabox="lightbox-gallery" data-title="métadonnées utilisateur"} 

Une fois ceci fait on peut aller au bout du formulaire et le marquer comme finalisé.

### Finalisation du formulaire

[![Fin de la session](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/fin_du_formulaire.png "Fin de la session"){: .img-left }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/fin_du_formulaire.png){: data-mediabox="lightbox-gallery" data-title="Fin de la session"} 

Les données sont alors automatiquement (c'est le comportement par défaut désormais) envoyées à Central.

----

## Ressources complémentaires

- le formualaire complet, prêt à l'emploi.
- ...

----

## Auteur

### Mathieu Bossaert

![Portrait Mathieu Bossaert](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/mb.jpeg "Portrait Mathieu Bossaert"){: .img-rdp-news-thumb }

Aprés des études de biologie, d'écologie, et d'informatique, j'ai intégré le CEN en 2003 pour y occuper le poste de gestionnaire de bases de données, et suis devenu "géomaticien" par extension.

J'y suis désormais co-responsable de la "Geomateam" qui compte 5 personnes, pas toutes à temps plein sur la thématique, au sein d'une équipe "Occitane" de 80 salariés, répartis sur 14 sites.

PostgreSQL est le pillier strucurant de notre SI depuis 2006. Les besoins de la structure ont évolués avec elle et chacun d'eux a trouvé une solution robuste dans le monde du libre et les communautés des différents outils, à travers georezo notament, n'ont jamais été avares de conseils.
J'ai intégré il y a quelques années l'équipe de georezo et j'y assure la fonction de trésorier.

Enfin je contribue dans la mesure de mes compétences et de ma disponibilité aux forums techniques dédiés (principalement celui d'[ODK](https://forum.getodk.org))

Vous pouvez me contacter pour échanger sur le sujet via [twitter](https://twitter.com/MathieuBossaert), [linkedin](https://www.linkedin.com/in/mathieu-bossaert-08b73a205/) ou par courriel à l'adresse prenom.nom@...

<!-- Hyperlinks reference -->

[Conservatoire d'Espaces Naturels d'Occitanie]: https://www.cen-occitanie.org
["blog" géomatique du CEN]: https://si.cen-occitanie.org
[GetODK]: https://getodk.org/
[XLSForm]: https://xlsform.org/en/