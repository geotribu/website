---
title: Open Data Kit pour la collecte de données géographiques dans PostGIS (2/3)
authors:
    - Mathieu BOSSAERT
categories:
    - article
comments: true
date: 2021-06-22
description: Second article de présentation de la suite Open Data Kit (ODK) et son intégration au SI du CEN d'Occitanie et dans les processus métiers.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/open_data_kit_postgresql.png
license: CC-BY-SA
tags:
    - Android
    - collecte
    - ODK
    - Open Data Kit
    - PostGIS
    - PostgreSQL
---

# ODK pour la collecte de données géo dans PostGIS (2/3)

:calendar: Date de publication initiale : 22 juin 2021

![ODK PostGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/Central2PG.png "ODK + PostGIS"){: .img-thumbnail-left }

Aprés vous avoir présenté les outils proposés par ODK et la place qu'ils occupent dans notre SI centré sur PostGIS, ce second article illustre à travers notre formulaire généraliste l'utilisation des différents "widgets" à notre disposition.
Des extraits du "XLSForm" du formulaire complètent les captures d'écrans pour montrer l'utilisation des différentes colonnes de la feuille de calcul "survey" et de la feuille de calcul "choices".

Dans ces extraits, nous n'avons conservé que les colonnes renseignées pour en faciliter la lecture et nous avons numéroté les lignes.

Le lien vers le fichier [XLSForm] de notre formulaire est disponible en [bas de l'article](#ressources-complementaires).

Vous pouvez utiliser ODK pour la collecte de données sur le terrain même si vous n'avez pas installé le serveur. Vous pouvez simplement créer votre fichier [XLSForm], le transformer via [XLSForm Online](https://getodk.org/xlsform/) et transférer le xml et les éventuels médias associés sur votre téléphone.
Vous pourrez ensuite récupérer les données collectées avec [Briefcase](https://docs.getodk.org/briefcase-intro/), rapidement évoqué dans le premier épisode de cette série.

Dans un dernier article, nous verrons comment les données collectées sur les téléphones grâce à ce formulaire intègrent notre base de données PostGIS et sont ainsi mises à disposition de l'ensemble de l'équipe, à travers les différents outils présentés dans l'article précédent.

[1 : Introduction à ODK](2021-06-08_odk_postgis_1.md){: .md-button }
[3 : Récupération des données dans notre SI](2021-09-22_odk_postgis_3.md){: .md-button }
{: align=middle }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Introduction

Traditionnellement, les naturalistes et les écologues du CEN notaient toutes leurs observations sur des carnets de terrain papier, et les informatisaient au retour au bureau, via une interface web, un tableur ou une couche SIG. Dans le cas des tableurs et fichiers SIG, une étape supplémentaire était nécessaire pour consolider les données saisies dans notre base de données PostGIS.

En conséquence, il pouvait s'écouler plusieurs mois avant que les observations d'un membre de l'équipe soient visibles dans le SI par les autres collègues. La création de notre outil web interne en 2009 a été un premier élément de réponse technique à cette difficulté de consolidation et de partage rapide des données.
Nous avions eu en 2007 une expérience de collecte de données sur PDA (avec ArcPad) et l'absence de double saisie nous avait beaucoup enthousiasmé.

La présentation ci-dessous faite au [FOSS4G-fr de 2018](https://www.osgeo.asso.fr/foss4gfr-2018/) reprend l'historique de notre SI et présente notre utilisation d'ODK (cliquer sur l'image pour télécharger le PDF de la présentation) :

[![présentation d'ODK au FOSS4G-fr 2018](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/presentation_odk_foss4gfr_2018.png "présentation d'ODK au FOSS4G-fr 2018"){: loading=lazy }](http://si.cen-occitanie.org/wp-content/uploads/2019/11/16mai_Cauchy_Bossaert-CENLR_0.pdf)
{: align=middle }

## Logique du formulaire

![icône collecte smartphone](https://cdn.geotribu.fr/img/logos-icones/divers/smartphone_mobile_map.svg "icône collecte smartphone - Crédits The Noun Project"){: .img-thumbnail-left }

Le formulaire décrit ici est notre formulaire principal, initié en 2016. La version initiale permettait de collecter des informations basiques sur les espèces et les habitats. Elle résultait d'un atelier (_workshop_) organisé avec les collègues du CEN Rhône-Alpes (Rémy Clément, Laurent Poulin et Guillaume Costes) qui maitrisaient la création de formulaire. Je m'étais alors occupé de la récupération des données collectées dans PostGIS.

Chaque révision successive a apporté son lot d'améliorations et les questions sont devenues plus "adaptatives". Les réponses possibles dépendaient par exemple de l'espèce sélectionnée (ex. pas de têtard si on a vu un oiseau).

En 2019, avec le travail de Jean Baïsez, le formulaire s'est enrichi : aux observations d'espèces et d'habitats, ont été ajoutées la description des pressions ou des menaces sur les milieux naturels.

Toutes ces données sont géoréférencées (point, lignes ou polygones) et peuvent être documentées par des photos prises par le téléphone. Ces dernières peuvent être annotées.

En 2021, le système de préférences a été amélioré et les attentes évoquées par les collègues à la fin de la saison 2020 ont été satisfaites (navigation dans les données collectées, recherche des taxons dans le référentiel taxonomique).

Aucune de ces évolutions n'a nécessité de développement de notre part, elles ont certes été possibles grace aux évolutions de _Collect_, mais surtout par l'appropriation du standard [XLSForm].

Notre formulaire est constitué de deux boucles imbriquées : aprés avoir renseigné les informations de base du relevé (contexte, observateur...), il nous est proposé de créer une localité (objet géographique), puis d'y renseigner une ou plusieurs observations.

Aprés la dernière observation de la localité courante, il est proposé de saisir une nouvelle localité... Si c'était la dernière localité, le formulaire est "finalisé" et peut être envoyé au serveur.

Voici un schéma illustrant la logique du formulaire :

![Logique du formulaire](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/logique_formulaire.jpeg "Logique du formulaire"){: .img-center loading=lazy }

## Collecte de données

C'est parti pour la collecte : on lance ODK Collect qui nous propose plusieurs options. On choisit donc de remplir notre formulaire :

![écran d'accueil de Collect](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ecran_accueil_ODK_Collect.png "Ecran d'accueil d'ODK Collect"){: loading=lazy width=250 }
![Choix du formulaire à renseigner](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/liste_des_formulaires.png "Choix du formulaire à renseigner"){: loading=lazy width=250 }
{: align=middle }

### Choix du formulaire à renseigner --> SICEN

Les 3 premiers écrans du formulaire à proprement parler permettent de le paramétrer et demandent à l'utilisateur ses préférences pour la session qu'il démarre.

A la première utilisation du formulaire, les fonctionnalités seront toutes activées par défaut. Libre à chacun de désactiver celles qui lui semblent inutiles.

A l'utilisation suivante, chacune des options sera proposée dans l'état d'activation qui était le sien lors de la précédente utilisation du formulaire. Il sera là encore possible de valider ou modifier chacun de ces choix.  
Les fonctionnalités à cette étape seront masquées pendant l'utilisation du formulaire.

![Métadonnées relatives à l'utilisateur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/metadonnees_utilisateur.png){: loading=lazy width=175 }
![Préférences de l'utilisateur - Choix des possibilités cartographiques](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/preferences_utilisateur_geo.png){: loading=lazy width=175 }
![Préférences de l'utilisateur - Types et thématiques des données à saisir](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/preferences_utilisateur_thematique.png){: loading=lazy width=175 }
{: align=middle }

!!! info
    Au fur et à mesure de la saisie, l’icône de la disquette (:floppy_disk:) permet d'enregistrer le formulaire en cours sur le téléphone.

### Écran de paramétrage n°1 -->  l'identité de l’utilisateur

Le nom de l'utilisateur et son adresse email sont demandés. L'adresse email nous sert à identifier l'utilisateur dans notre SI métier.  
Ces deux champs sont remplis par défaut avec les valeurs saisies dans les paramètres généraux de l'application. Si l'utilisateur ne les a pas renseignés dans l'application, il devra les saisir ici.

### Écran de paramétrage n°2 -->  types de géométries créées

Quels types de géométrie sont susceptibles d'être créés au cours de la session ? Des points ? Des lignes ? Des polygones ?

Voici l'extrait correspondant de la feuille **survey** (le principe est le même pour l'écran précédent et le 3ème) :

- le groupe (_begin_group_ et _end_group_) permet de faire apparaitre les questions dans un même écran
- les questions sont des _select_one_ (une seule option à choisir)
- la liste utilisée dans la feuille **choices** s'appelle *boolea
- et par défaut (colonne **default**) la question prend la dernière valeur enregistrée (_${last-saved#utiliser_geopoint}_), sinon _true_ :

| **type**           | **name**          | **label** | **required** | **default**                                      |
| ------------------ | ----------------- | --------- | :----------: | ------------------------------------------------ |
| select_one boolean | utiliser_geopoint | Points    | yes          | coalesce(${last-saved#utiliser_geopoint},’true’) |
| select_one boolean | utiliser_geotrace | Lignes    | yes          | coalesce(${last-saved#utiliser_geotrace},’true’) |
| select_one boolean | utiliser_geoshape | Polygones | yes          | coalesce(${last-saved#utiliser_geoshape},’true’) |
| end group          |                   |           |              |                                                  |

### Écran de paramétrage n°3 -->  Types de données (thématiques) et paramétrage de l'autocomplétion

Le dernier écran permet de choisir le nombre de caractères à saisir dans le recherche des espèces pour déclencher l'interrogation du référentiel ("auto-complétion").  
3 est le minimum, 7 le maximum (pour permettre l'utilisation du "code taxon" par exemple "ERI RUB" pour _Erithacus rubecula_ qui est le rouge-gorge) :bird:.
Notez que la dernière question n'est pas visible et nécessite de "scroller" l'écran.

L'ensemble de ces paramètres est concaténé dans une chaîne nommée "preferences_utilisateur" (champ de type _calculate_ et fonction _concat_ dans la colonne **calculation**).

| **type**  | **name**                | **calculation**                                              |
| --------- | ----------------------- | ------------------------------------------------------------ |
| calculate | preferences_utilisateur | concat(if(${utiliser_geopoint} = 'true','point',''),if(${utiliser_geotrace} = 'true','line',''),if(${utiliser_geoshape} = 'true','polygon',''),if(${animalia} = 'true','animalia',''),if(${plantae} = 'true','plantae',''),if(${fungi} = 'true','fungi',''),if(${habitat} = 'true','habitat',''),if(${pression_menace} = 'true','pression_menace',''),if(${observation_generale} = 'true','observation_generale',''),${nb_lettres}) |

Une fois les paramétrages vérifiés et/ou modifiés, l'utilisateur peut choisir l'étude pour laquelle le relevé est effectué ainsi que le protocole de collecte utilisé.

### Choix de l'étude et du protocole

Ces deux référentiels sont gérés dans des fichiers csv externes associés au formulaire. Les fichiers sont mentionnés dans la colonne **appearence** des lignes 2 et 3 de l'extrait ci-dessous (_search('etudes')_ et _search('protocole')_).
Cela permet de les mettre à jour sur le téléphone sans avoir à mettre à jour le formulaire sur le serveur.
Nous verrons plus tard avec le référentiel taxonomique que le stockage externe de ces référentiels nous offre des possibilités de recherche intéressantes.

L'utilisation combinée de l'apparence _quick_ permet de passer automatiquement à la question suivante quand une option est sélectionnée.
La feuille de calcul **choices** nous renseigne sur la structure de ces fichiers csv. Les colonnes _nom_etude_id_ et _libelle_id_ contiennent les valeurs à stocker, les colonnes _nom_etude_ et _libelle_ contiennent les "noms" à afficher dans les listes.

![choix de l'étude](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/liste_de_choix_etudes.png "choix de l'étude"){: loading=lazy width=175px }
![métadonnées utilisateur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/liste_de_choix_protocole.png "métadonnées utilisateur"){: loading=lazy width=175px }
{: align=middle }

#### Extrait de la feuille **survey**

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

A terme nous aimerions générer dynamiquement et régulièrement la liste des études pour ne faire apparaître que les études en cours et pourquoi pas seulement celles qui concernent l’utilisateur de l'application.
La même chose pourrait être envisagée pour les protocoles.

Une fois ces paramètres de "session" renseignés, nous pouvons commencer la saisie de données.

### Création d'une localité

Il s'agira d'un point, d'une ligne ou d'un polygone. Cette fonctionnalité "géographique" du formulaire a été décrite dans [la première partie de cet article](2021-06-08_odk_postgis_1.md).

![Choix du type de géoréférencement de l'emplacement courant](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/georeferencement_choix_du_point.png "Choix du type de géoréférencement de l'emplacement courant"){: loading=lazy width=175px }
{: align=middle }

Le GPS peut nous aider à dessiner automatiquement points, lignes et polygones, que nous pouvons aussi dessiner à la main sur l'écran. L'automatisation peut être paramétrée selon la distance maximale ou le temps de parcours entre deux points. Une précision minimale du GPS peut aussi être configurée dans le formulaire pour interdire des localisations trop peu précises.

![localisation assistée par le GPS du téléphone](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/cartographie_assistee_par_gps_affichage_precision.png "localisation assistée par le GPS du téléphone"){: loading=lazy width=175px }
![coordonnées du point GPS collecté et précision du capteur lors de l'enregistrement](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/affichage_coordonnees_point_enregistre.png){: loading=lazy width=175px }
{: align=middle }

<!-- markdownlint-disable MD024 -->
#### Extrait de la feuille **survey**
<!-- markdownlint-enable MD024 -->

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
| 12 | geoshape               | polygone                  | polygone                      |                                              | yes          |                     |             | ${methode_geo} = 'polygone’                 |                                             | 10000                |                             |
| 13 | calculate              | surface_polygone          |                               | area(${polygone})                            |              |                     |             | ${methode_geo} = 'polygone’                 |                                             |                      |                             |
| 14 | end group              |                           |                               |                                              |              |                     |             |                                             |                                             |                      |                             |
| 15 |                        |                           |                               |                                              |              |                     |             |                                             |                                             |                      |                             |
| 16 | end group              |                           |                               |                                              |              |                     |             |                                             |                                             |                      |                             |
| 17 | end repeat             |                           |                               |                                              |              |                     |             |                                             |                                             |                      |                             |

Le _begin repeat_ démarre une boucle de création de localités.

Le groupe qui suit directement ce repeat (ligne n°2) encapsule l'ensemble des éléments contenus dans la boucle et permettra de nommer chaque instance de la boucle, ici avec la valeur du champ calculé _heure_localite_ (ligne 4).

L'observation pourra ainsi être retrouvée dans la navigation du formulaire, avec l’heure de l'emplacement et l’espèce observée.

La colonne **choice_filter**, utilisée pour la question _methode_geo_ permet de ne proposer que les options de la feuille **choices** pour lesquelles la valeur **filter** est contenue dans les "préférences utilisateur" calculée plus haut (écrans 2 et 3).

La colonne **relevant** permet de mentionner si la question est pertinente (à afficher), et dans quel contexte. Un test peut-être utilisé pour déterminer sa valeur (qui est 'true' par défaut). Ici donc seul le widget carto correspondant à la réponse donnée à la question "methode_geo" (ligne 5) sera affiché.

Des fonctions, appelées dans la colonne **calculation** permettent de réaliser des calculs pendant la saisie, ici l'heure courante, la longueur d'un ligne et la surface d'un polygone.
<!-- markdownlint-disable MD024 -->
#### Extrait de la feuille choices
<!-- markdownlint-enable MD024 -->
La liste des choix proposés pour la méthode de localisation des observations est décrite comme ceci :

| **list_name** | **name**   | **label**             | **filter** |
| ------------- | ---------- | --------------------- | ---------- |
| methode_geo   | point_auto | point automatique     | point      |
| methode_geo   | point      | point sur une carte   | point      |
| methode_geo   | ligne      | ligne                 | line       |
| methode_geo   | polygone   | polygone              | polygon    |
| methode_geo   | long_lat   | Saisie de coordonnées | point      |

### Saisie d'une ou plusieurs observations à cet endroit

Une fois l'emplacement créé, nous allons pouvoir y créer autant d'observations que nous le souhaitons, de chacun des types autorisés dans les paramétrages du formulaire. Ici une observation de plante.

![choix du type d'observation à renseigner](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/choix_type_d_observation.png "choix du type d'observation à renseigner"){: loading=lazy width=175px }
![recherche d'une espèce végétale](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/recherche_d_une_espece_autocompletion.png "recherche d'une espèce végétale"){: loading=lazy width=175px }
{: align=middle }

### Propositions des taxons de référence et des synonymes qui correspondent aux lettres tapées

Les collègues ont fait remonter des besoins d'amélioration de cette fonctionnalité. Nous proposions dans les versions précédentes du formulaire une simple liste avec une saisie prédictive.

Ils ont souhaité que cette liste propose d'abord les noms de référence, classés du rang taxonomique le plus élevé (famille, genre) au plus bas (espèce, sous-espèce...).

![propositions de taxons correspondant à la recherche](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/recherche_d_une_espece_propositions.png "propositions de taxons correspondant à la recherche"){: loading=lazy width=175px }
{: align=middle }

#### Extrait de la feuille de calcul **survey**

|      | **type**               | **name**          | **label**                  | **hint**                       | **calculation**                                              | **required** | **appearance**                                               | **relevant**                                              |
| ---- | ---------------------- | ----------------- | -------------------------- | ------------------------------ | ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ | --------------------------------------------------------- |
| 1    | begin group            | plantae_selection | ${lb_nom_plantae}          |                                |                                                              |              | field-list                                                   | ${type_observation} = 'plantae'                           |
| 2    | text                   | recherche_plantae | Nom de l’espèce végétale : | au moins ${nb_lettres} lettres |                                                              | yes          |                                                              |                                                           |
| 3    | select_one list_espece | lb_nom_plantae    | Sélectionnez l'espèce :    |                                |                                                              | yes          | quick search('espece_plante', 'startswith', 'code_espece_key,lb_nom_key', ${recherche_plantae}) | string-length(${recherche_plantae}) > (${nb_lettres} - 1) |
| 4    | calculate              | cd_nom_plantae    |                            |                                | pulldata('espece_plante','cd_nom_key','lb_cd_nom_key',${lb_nom_plantae}) |              |                                                              |                                                           |
| 5    | end group              |                   |                            |                                |                                                              |              |                                                              |                                                           |

Nous utilisons ici aussi un référentiel externe (les entrées de la "liste déroulante" ne sont pas stockées dans la feuille **choices** mais dans un fichier csv).

Nous voyons (ligne n°3) que le fichier s'appelle _espece_plante_, et que nous allons y chercher les lignes pour lesquelles les colonnes **code_espece_key** ou **lb_nom_key** commencent (_startswith_) par les caractères tapés dans la question précédente (ligne 2).

```excel
quick search('espece_plante', 'startswith', 'code_espece_key,lb_nom_key', ${recherche_plantae})
```

Les propositions n'apparaitront que si le nombre de caractères saisis est supérieur ou égal au nombre de lettres requises, spécifié dans les préférences utilisateur (colonne **relevant** de la ligne 3).
Elles seront ordonnées selon la valeur stockée dans la colonne **orderby** du fichier csv. Cette colonne est optionnelle, si elle n'est pas présente, les propositions seront affichées dans l'ordre alphabétique.

Cela nous permet de calculer un ordre a priori, lors de la génération du référentiel, qui tient compte du caractère valide du taxon puis de son niveau taxonomique.

Le suffixe __key_ utilisé dans les noms de colonnes des fichiers csv force la création d'un index lors de leur transformation en base de données sqlite sur le téléphone.
C'est trés utile pour interroger efficacement les référentiels taxonomiques (faune et flore) issus de [TAXREF](https://inpn.mnhn.fr/programme/referentiel-taxonomique-taxref) de l'[INPN](https://inpn.mnhn.fr), qui comptent chacun plusieurs dizaines de milliers de lignes.
Le lien vers le script SQL de génération du référentiel csv à partir de taxref est proposé dans la section "ressources" de l'article

### Renseignement de l'effectif observé

L'espèce mentionnée a-t-elle été observée ? Cette question est posée car il est important dans certains protocoles de mentionner l'absence d'un taxon recherché.

Si oui, les écrans suivants (ou leurs homologues pour la Faune sont affichés)

Ici pour les espèces végétales il s'agit d'un effectif par classes d’abondance

![l'espèce a-t-elle été observée ?](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/le_taxon_a_t_il_ete_observe.png "l'espèce a-t-elle été observée ?"){: loading=lazy width=175px }
![abondance de l'espèce](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/renseignement_abondance_espece.png "abondance de l'espèce"){: loading=lazy width=175px }
{: align=middle }

### Informations sur la "qualité" de la donnée

![éléments de qualité de la donnée](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/qualite_donnee_determination_sensibilite_fiabilite.png "éléments de qualité de la donnée"){: loading=lazy width=175px }
![modalité de determination](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/modalite_de_determination.png "modalité de determination"){: loading=lazy width=175px }
{: align=middle }

### Renseignement de détails optionnels, prise de photo :camera:, annotation

ODK peut mobiliser l'ensemble des capteurs de votre téléphone. La prise de photo peut-être utile, pour confirmer une détermination d'espèce ou documenter la dégradation d'un milieu.

L'annotation de la photo peut être utile par exemple pour les observations de type "pression/menace" ou "observation générale"

[Ces photos seront mobilisables par la suite dans QGIS ou dans nos tableaux de bord.](https://si.cen-occitanie.org/?p=191)

![prendre un photo](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/prise_de_photo.png "prendre un photo"){: loading=lazy width=175px }
![Annotation de la photo](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/annotation_photo.png "Annotation de la photo"){: loading=lazy width=300px }
![Visualisation de l'image annotée](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/visualisation_image_finale.png "Visualisation de l'image annotée"){: loading=lazy width=175px }
{: align=middle }
<!-- markdownlint-disable MD024 -->
#### Extrait de la feuille de calcul **survey**
<!-- markdownlint-enable MD024 -->
| **type**                 | **name**      | **label**           | **appearance** | **relevant**           | **parameters**  |
| ------------------------ | ------------- | ------------------- | -------------- | ---------------------- | --------------- |
| select_one prendre_image | prendre_image | Prendre une photo ? |                |                        |                 |
| image                    | prise_image   | Prendre une photo   | annotate       | ${prendre_image}='oui' | max-pixels=2000 |

La question est de type _image_, elle ne sera affichée que si l'utilisateur souhaite prendre une photo (_${prendre_image}='oui'_).

Les photos peuvent être annotées (_annotate_), et leur taille est limitée pour éviter l'envoi d'images trop grandes pour l'usage qui en sera fait (_max-pixels=2000_).

### Ajout d'une nouvelle observation ? d'une nouvelle localité ?

Souhaitons nous ajouter une observation sur l'emplacement courant ?

- Si oui nous redémarrons une boucle de saisie d'observation.
- Si non il nous est proposé d'ajouter une nouvelle localité.
    - Si nous acceptons nous redémarrons une boucle de localité (point, ligne ou polygone)
    - Si nous refusons nous pouvons finaliser le formulaire aprés avoir renseigné d'éventuels accompagnateurs

![Ajouter une observation à l'emplacement courant ?](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/iteration_boucle_observation.png "Ajouter une observation à l'emplacement courant ?"){: loading=lazy width=175px }
![Ajouter un nouvel emplacement au relevé ?](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/iteration_boucle_emplacement.png "Ajouter un nouvel emplacement au relevé ?"){: loading=lazy width=175px }
![Ajouter un ou plusieurs accompagnateurs](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ajout_accompagnateur.png "Ajouter un ou plusieurs accompagnateurs"){: loading=lazy width=175px }
{: align=middle }

### Fin du formulaire, parcours et révision des données collectées

![Fin du formulaire](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/fin_du_formulaire.png "Fin du formulaire"){: loading=lazy width=175px }
{: align=middle }

L’icône représentant une flèche montrant un point permet de naviguer dans les observations déjà saisies pour les vérifier ou les modifier.

En cliquant sur le groupe répétitif "Emplacements", on accède à la liste des emplacements du formulaire.

En cliquant sur l'emplacement désiré, on accède au détail le concernant.

Enfin un clic sur le groupe répétitif "Observations" nous donne accès à la liste des observations rattachées à l'emplacement et au détail de chacune d'elles :

![Navigation dans les données collectées](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/accueil_navigation_donnees_collectees.png "Navigation dans les données collectées"){: loading=lazy width=175px }
![Liste des lieux](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/navigation_liste_emplacements_sessions.png "Liste des lieux"){: loading=lazy width=175px }
![Résumé d'un emplacement antérieur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/resume_emplacement_anterieur.png "métadonnées utilisateur"){: loading=lazy width=175px }
![Observations rattachées à l'emplacement](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/navigation_liste_observations_emplacement_1.png "Observations rattachées à l'emplacement"){: loading=lazy width=175px }
![Résumé d'une observation antérieure](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/resume_observation_anterieure.png "métadonnées utilisateur"){: loading=lazy width=175px }
{: align=middle }

Une fois ceci fait on peut aller au bout du formulaire et le "finaliser".

### Finalisation du formulaire

![Fin de la session](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/fin_du_formulaire.png "Fin de la session"){: loading=lazy width=175px }
{: align=middle }

Les données sont alors automatiquement envoyées ("soumises") à Central (c'est le comportement par défaut désormais).

Nous verrons dans le prochain article comment les données sont récupérées et intégrées à notre base de données PostGIS.

## Perspectives

Les perspectives sont nombreuses au regard des discussions en cours au sein du TAB (_Technical Advisory Board_) d'ODK.

Notamment celles concernant les "entity based data collection" et les "longitudinal data collection" qui laissent entrevoir des possibilités très intéressantes de suivis récurrents d'objets définis sur le terrain : placettes, ouvrages, parcelles agricoles...

Des évolutions des widgets cartographiques seraient intéressantes : pouvoir cliquer un objet de la carte pour le décrire, afficher de manière différenciée les objets présents sur la carte...

Le forum est le lieu de discussion privilégié pour interagir avec la communauté et l'équipe de développement sur ces questions :

- <https://forum.getodk.org/t/entity-based-data-capture-workflow-site-based-survey-with-opportunistic-encounters/33353>
- <https://forum.getodk.org/t/selecting-a-map-feature-to-collect-data-about/28466/8>
- <https://forum.getodk.org/t/geo-using-the-mapbox-sdk-for-android/19223/17>

ODK était la porte d'entrée principale des données métiers dans le SI de l'ex CEN Languedoc-Roussillon. La fusion en septembre dernier avec le CEN Midi-Pyrénées ne semble pas remettre en cause cela.

Et certains formulaires spécifiques à des projets de l'ex-région Midi-Pyrénées voient le jour, développés par des collègues non géomaticiens !

Le graphique ci-dessous montre pour l'année 2021 le nombre de données d'observations d'espèces intégrées chaque mois selon leurs modalités de saisie.
Nous pourrons faire un bilan plus juste à la fin de l'année quand les carnets de terrain papier auront été numérisés.

[![Modalité de saisie des données de biodiversité dans notre SI en 2021](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/modalite_de_saisie_des_donnees_de_biodiversite_en_2021.png "modalités de saisie en 2021"){: .img-center loading=lazy }](https://dashboards.cen-occitanie.org/embed/query/403/visualization/872?api_key=n0qV6a6FX6DyKCGtOBZQ1mPmw8wNfLHnha1SmDsO&)
{: align=middle }

Enfin ce graphique, basé sur la nouvelle base de donnée "Occitanie" montre l'évolution des modes de saisie. 2015 marque l'arrivée d'ODK dans le SI, 2020 la création du CEN Occitanie.

[![Evolution des modalités d'entrée des données de biodiversité dans le SI du CEN Occitanie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/evolution_des_modes_de_saisie.png "évolution des modes de saisie"){: .img-center loading=lazy }](https://dashboards.cen-occitanie.org/embed/query/150/visualization/490?api_key=k6q0e0T0CPfE2ceVJz4uaaCfapg4VHio2dTlmsoK&)
{: align=middle }

----

## A suivre

[Lire la troisième partie :fontawesome-solid-forward:](2021-09-22_odk_postgis_3.md){: .md-button }
{: align=middle }

----

## Ressources complémentaires

- [le formulaire complet, prêt à l'emploi](https://forum.getodk.org/uploads/short-url/dqspKIp4h5YmKJhGCe6ZgOL85R7.zip)
- [le script sql de génération du référentiel](https://forum.getodk.org/uploads/short-url/vBGcLFxLAjCACOLbrC7F2xaMV4X.txt)
- [la documentation de chaque type de question](https://docs.getodk.org/form-question-types/)
- [le fichier XLSFform présentant l'ensemble des types de questions disponibles](https://docs.google.com/spreadsheets/d/1af_Sl8A_L8_EULbhRLHVl8OclCfco09Hq2tqb9CslwQ/edit#gid=0)
- [utiliser ODK sans serveur Central](https://www.youtube.com/watch?v=F4tntbcdGI0)
- [la liste des cours de stats4sd sur ODK](https://forum.getodk.org/t/great-resources-from-stats4sd-team/31045)

----

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-sa.md" %}

<!-- Hyperlinks reference -->
[XLSForm]: https://xlsform.org/en/
