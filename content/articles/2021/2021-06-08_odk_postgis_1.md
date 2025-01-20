---
title: Open Data Kit pour la collecte de données géographiques dans PostGIS (1/3)
authors:
    - Mathieu BOSSAERT
categories:
    - article
comments: true
date: 2021-06-08
description: Premier article de présentation de la suite Open Data Kit (ODK) et son intégration au SI du CEN d'Occitanie et dans les processus métiers.
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

# ODK pour la collecte de données géo dans PostGIS (1/3)

:calendar: Date de publication initiale : 08 juin 2021

![ODK PostGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/Central2PG.png "ODK + PostGIS"){: .img-thumbnail-left }

Cette série de 3 articles vise à présenter Open Data Kit, qui est une solution de recueil de données sur téléphone Android, utilisée par le [Conservatoire d'Espaces Naturels d'Occitanie], pour la collecte de données spatialisées de biodiversité, et leur intégration à une base de données PostGIS.

Ce premier article, introductif, présente le projet ODK, ses outils ainsi que les possibilités cartographiques.  
Le second détaillera les possibilités de création de formulaire à travers l'exemple détaillé du formulaire généraliste du [Conservatoire d'Espaces Naturels d'Occitanie].  
Le dernier sera consacré à la récupération des données collectées dans une base de données PostGIS.

[2 : Création d'un formulaire](2021-06-22_odk_postgis_2.md){: .md-button }
[3 : Récupération des données dans PostGIS](2021-09-22_odk_postgis_3.md){: .md-button }
{: align=middle }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Introduction à Open Data Kit

### Historique

Projet initié en 2008 par Yaw Anokwa, l'actuel CEO de [GetODK], [ODK (Open Data Kit)](https://getodk.org) est un ensemble d'outils open source pour la collecte de données sur téléphone, fonctionnant en mode déconnecté et dans des environnements contraints en terme de ressource et de connectivité.

ODK permet de réaliser des formulaires identiques à ce que vous feriez sur papier pour noter du texte et des nombres. Il permet aussi d’y ajouter des captures de son, d’images, de vidéo, de QR Code ou code-barre et d’interagir avec des applications externes et des capteurs, au milieu de nulle part, sans connexion. A tous ces types de données s’ajoutent les données géographiques (coordonnées GPS, points, lignes et polygones).  
Les données collectées au sein des formulaires sont envoyées au serveur (ODK Central) dés lors qu’une connexion (GSM, WIFI) est disponible, parfois plusieurs semaines ou mois après le début de la campagne de terrain.

### Exemples de cas d'utilisation significatifs

Voici quelques exemples emblématiques d'utilisation Open Data Kit qui font office de référence :

- Le ministère de l'agriculture nigérian a organisé la cartographie de 2 millions de fermes par 70 000 collecteurs, qui vont de ferme en ferme pour mesurer la ressource herbagère disponible et quantifier les intrants nécessaires au maintien de la fertilité des terres, afin d'assurer la disponibilité locale de nourriture pendant la pandémie.

- ODK a été utilisé au Honduras, par 85 000 enseignants, pendant la pandémie afin d'évaluer la progression "académique" des étudiants pendant la période d'enseignement à distance  avec ODK.

- ODK est utilisé par des acteurs majeurs de l'aide humanitaire et de l'aide au développement tels que la Fédération Internationale de la Croix Rouge ou l'UNICEF (cas du [suivi de la campagne de vaccination contre la rougeole et la polyomyélite en Ouganda](https://www.unicef.org/media/93781/file/gavi-unicef-digital-technology-immunization-2021.pdf)).

- L'Organisation Mondiale de la Santé l'utilise pour suivre l'évolution des maladies et faire du "contact tracking" pendant les épidémies

<blockquote class="twitter-tweet tw-align-center" data-lang="fr" data-dnt="true"><p lang="fr" dir="ltr"><a href="https://twitter.com/hashtag/COVID__19?src=hash&amp;ref_src=twsrc%5Etfw">#COVID__19</a> Niger – Intégration de la surveillance COVID-19 dans la plateforme ODK Collect, utilisée pour la surveillance de la polio : une opportunité pour renforcer la recherche active des cas suspects dans les formations sanitaires et la communauté <a href="https://twitter.com/OMS_Afrique?ref_src=twsrc%5Etfw">@OMS_Afrique</a> <a href="https://twitter.com/BlancheAnya?ref_src=twsrc%5Etfw">@BlancheAnya</a></p>&mdash; OMS Niger (@OMSNiger) <a href="https://twitter.com/OMSNiger/status/1272940020169674752?ref_src=twsrc%5Etfw">16 juin 2020</a></blockquote>

- ODK fait partie de la [boite à outils d'HotOSM](https://toolbox.hotosm.org/fr/pages/field-mapping-management/4.2_using_odk_collect/)

- des structures bien plus "petites" comme les Conservatoires d'Espaces Naturels (CEN) utilisent la solution pour collecter des données relatives à la conservation de la nature.

Du côté des anecdotes chiffrées  :

- En 2020 ODK a été utilisé dans tous les pays du monde excepté au Groenland et en Corée du Nord !
- ODK Collect a été téléchargé plus d'un million de fois sur le playstore de google.

### Gouvernance et communauté

![logo Open Data Kit (ODK)](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/odk_open_data_kit.png "logo Open Data Kit (ODK)"){: .img-thumbnail-left }

Du côté de la gouvernance, [GetODK], la société qui développe ODK, est une [équipe composée de 9 personnes](https://getodk.org/about/team.html) qui s'appuie sur un comité technique, appelé [TAB (Technical Advisory Board)](https://github.com/getodk/governance/blob/master/TAB-GOVERNANCE.md) impliquant des utilisateurs de toute la planète et de différents domaines. Ce TAB se réunit tous les 15 jours [de manière très transparente](https://forum.getodk.org/tag/tab-meeting).

![team ODK](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/Equipe_GetODK.png "équipe de GetODK"){: .img-center loading=lazy }

Le forum est le principal lieu d'échange entre utilisateurs et développeurs. Il compte 14 000 inscrits !  
La communauté est assez exemplaire en ce sens qu'il y a beaucoup d'interactions entre utilisateurs qui y échangent conseils et bonnes pratiques. Le forum fait remonter les besoins des utilisateurs et les échanges sont riches avec les développeurs, toujours curieux de l'utilisation faite des outils.

C'est un lieu de discussion mondial, où il n'est pas rare d'échanger avec des utilisateurs de tous les continents en une journée. La bienveillance et l'entraide qui y règnent facilitent les échanges entre membres de tous niveaux et font de ce forum un "endroit" chaleureux !

----

## Contexte d'utilisation au CEN Occitanie

### Le SI du CEN

![Cen Occitanie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/logo_CEN_Occitanie.jpg "Cen Occitanie"){: .img-thumbnail-left }

Les conservatoires d'espaces naturels sont des structures associatives composées d'équipe pluri-disciplinaires (Ecologie, Botanique, Faunistique, Phytosociologie, Agriculture, Gestion administrative et financière, Informatique et Systèmes d'information). L'action des Cen se décline selon 5 axes : Connaître, Protéger, Gérer, Valoriser, Accompagner. La connaissance est la base de notre action.

Elle requiert des compétences techniques de reconnaissances des espèces et des habitats et des compétences dans la mise en œuvre d'outils de collecte, de consolidation et d'analyse des données collectées.

Notre SI se développe depuis 2007 autour d'une base de données PostgreSQL/PostGIS. Il s'est enrichi au fur et à mesure que nous y avons intégré des outils supportant PostgreSQL, qui est donc bien le cœur et la colonne vertébrale de notre SI :

- [JasperStudio](https://community.jaspersoft.com/project/jaspersoft-studio)
- [QGIS](https://qgis.org/)
- [QGIS Server](https://docs.qgis.org/3.16/fr/docs/server_manual/)
- [LizMap](https://www.3liz.com/lizmap.html)

### Choix et intégration d'ODK

En 2015, après que la solution nous avait été présentée par le CEN Rhône-Alpes, nous avons entrepris de mettre en place un formulaire de saisie mobile, correspondant aux données collectées dans notre appli web métier (SiCen).

Quelques arguments de poids nous ont convaincus d'utiliser ODK :

- la possibilité de générer des formulaires très facilement, sans développement
- l'utilisation par ODK de PostgreSQL comme base de données.
- les zones dans lesquelles nous intervenons ne sont pas toujours bien connectées. L'outil utilisé devait donc permettre de travailler sans connexion et fournir un système de stockage stable et fiable.
- il devait également être aussi facile à utiliser que possible et devait permettre une saisie contrôlée (vocabulaires contraints et données typées).

L'intégration de la solution à notre SI s'est faite naturellement. Les possibilités de PostgreSQL (triggers, FDW) ont assuré l'interaction entre le serveur Aggregate d'ODK et les autres outils et bases de données en place.

Depuis c'est la plateforme de reporting web [Redash](https://redash.io/) qui complète le SI.

### La place d'ODK aujourd'hui

ODK est devenu l'outil principal de collecte de données de terrain au sein du CEN Languedoc-Roussillon et prend le même chemin à l'échelle de l'Occitanie.

Les utilisateurs d'ODK chez nous sont initialement des naturalistes, spécialistes de diverses disciplines (botanique, faunistique, phytosociologie).

La saison de terrain est dense, les journées longues et le temps à consacrer à la saisie des données collectées est contraint. ODK nous a permis d'économiser ce temps de saisie (environ 4 jours/expert/an) pour en passer plus sur le terrain, ou à l'analyse de données et à la rédaction de documents.

Le SI actuel du CEN Occitanie peut-être schématisé ainsi :

![Schéma SI CEN Occitanie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/galaxie_sicen.png "Schéma SI CEN Occitanie"){: .img-center loading=lazy }

Nous utilisons actuellement une quinzaine de formulaires ODK pour :

- des suivis naturalistes répondant à divers protocoles,
- le [suivi des paramètres physico-chimiques des lagunes](https://si.cen-occitanie.org/suivi-des-parametres-physico-chimiques-des-lagunes-un-formualire-de-terrain-avec-odk/),
- le suivi des ouvrages de gestion hydraulique,
- ou encore le suivi de l'utilisation des voitures de service.

----

## Les outils de la "suite" ODK

Les outils de la suite ODK sont sollicités en différents points du Système d'information géographiques (SIG) du Cen.
Le serveur nommé Central est au centre du système. Collect (sur les téléphones) et Enketo sur Firefox proposent les interfaces de collecte de données.

![place d'odk dans le SIG du Conservatoire d'espaces naturels](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/odk_dans_le_SIG_du_CEN_Occitanie.png "Les outils d'ODK dans le SIG du Cen"){: .img-center loading=lazy }

### Collect

C'est l'outil déployé sur les terminaux Android, qui sert les formulaires, permet de les remplir et envoie les données collectées au serveur.

### Central

C'est le serveur qui remplace désormais [Aggregate](https://forum.getodk.org/t/aggregate-is-no-longer-being-updated/33742). Il assure la gestion et la diffusion des formulaires, des utilisateurs, des droits de ces derniers et la collecte des "soumissions" (données envoyées par Collect).

![ODK Central : page d'accueil](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/accueil_odk_central.png "Page d'accueil d'ODK Central"){: loading=lazy width=300 }
![Page d'un projet dans ODK Central](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/formulaire_et_soumissions_dans_odk_central.png "Central, projets et soumissions"){: loading=lazy width=300px }
{: align=middle }

[Documentation ODK Central :fontawesome-solid-book:](https://docs.getodk.org/central-intro/){: .md-button }
{: align=middle }

#### Enketo

Central embarque [Enketo](https://enketo.org) de sorte que les formulaires réalisés sont désormais aussi utilisables en ligne à travers un navigateur et en mode déconnecté. A noter que depuis la version 1.2 publiée en mai 2021, l’édition des données envoyées au serveur est possible à travers cet outil (à des fins de correction ou révision).

![Enketo : formulaire d'enquête sur les usagers d'ODK](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/enketo_usages_odk.png "Enketo : formulaire d'enquête sur les usagers d'ODK"){: .img-center loading=lazy }
{: align=middle }

### Tableur / XLSForm

ODK utilise un sous-ensemble de la norme XForms du W3C pour créer des formulaires (voir [ici la documentation relative à ODK XForms](https://getodk.github.io/xforms-spec/)).

Une norme intermédiaire nommée [XLSForm] permet de décrire très simplement le formulaire dans un tableur, selon un formalisme simple. C'est avec notre tableur (Calc, Excel, AirTable, NocoDB...) préféré que nous allons décrire notre formulaire dans ce formalisme.

[XLSForm] est utilisé par de nombreuses solutions ([Enketo](https://enketo.org/), [Kobotoolbox](https://www.kobotoolbox.org/), [ONA](https://company.ona.io/products/ona-data/features/)). La plus connue des géomaticiens sera peut-être [la plateforme Survey123](https://doc.arcgis.com/fr/survey123/desktop/create-surveys/xlsformessentials.htm) d'ESRI.

[XLS Form est détaillé plus bas :fontawesome-solid-circle-down:](#xlsform){: .md-button }
{: align=middle }

### XLSForm Online

C'est un outil en ligne, qui permet de transformer le fichier xlsform en xml à charger sur le téléphone. Il n'est pas utile si vous utilisez Central, car ce dernier accepte directement le fichier xls.

[Ouvrir XLSForm Online](https://xlsform.getodk.org/){: .md-button }
{: align=middle }

### ODK Build

C'est l'éditeur WYSIWYG de formulaires. Nous ne le présenterons pas dans la série d'article, car nous avons toujours créé nos formulaires avec xlsform.

[Documentation ODK Build :fontawesome-solid-book:](https://docs.getodk.org/build-intro/){: .md-button }
{: align=middle }

### Briefcase

Il permet de pousser des formulaires sur le serveur, d'y récupérer les données et médias "soumis" et aussi de récupérer les données et médias directement depuis votre téléphone, et donc d'utiliser la solution sans avoir déployé Central.

[Documentation Briefcase :fontawesome-solid-book:](https://docs.getodk.org/briefcase-intro/){: .md-button }
{: align=middle }

![ODK Briefcase : récupération des données depuis Collect](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ODK_briefcase_recuperation_de_donnees_depuis_le_telephone.png "ODK Briefcase : récupération des données depuis Central"){: loading=lazy width=350px }
![ODK Briefcase : récupération des données depuis Central](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ODK_briefcase_recuperation_de_donnees_depuis_central.png "ODK Briefcase : récupération des données depuis Central"){: loading=lazy width=350px }
{: align=middle }

![ODK Briefcase : paramétrage de l'export des données récupérées](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ODK_briefcase_parametres_d_export_des_donnees_recuperees.png "ODK Briefcase : paramétrage de l'export des données récupérées"){: .img-center loading=lazy }

### Les outils communautaires

Voici deux outils qui ne sont pas développés par l'équipe d'ODK, mais par des membres de la communauté, que nous commençons seulement à utiliser au CEN. C'est pour ces deux raisons qu'ils apparaissent en transparence sur le schéma.

#### QReal Time

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-thumbnail-left }

L'extension [QRealTime pour QGIS](https://shivareddyiirs.github.io/QRealTime/), développée par Shiva Reddy Koti et Prabhakar Alok Verma, permet d’afficher directement les données collectées dans QGIS depuis Central et aussi de créer des formulaires vierges à partir d'une couche. Elle est disponible directement depuis le gestionnaire d'extensions de QGIS.

![QReal Time](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/qrealtime_schema.webp "QRealTime schéma"){: .img-center loading=lazy }

#### ruODK

![logo R](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/r.png "logo R"){: .img-thumbnail-left }

[ruODK](https://docs.ropensci.org/ruODK/) est un client R pour l'API d'ODK Central, developpé par un membre du TAB ([Florian Mayer](https://forum.getodk.org/u/florian_may/summary)), qui permet de mobiliser directement les données collectées dans R. Il est utilisé depuis peu dans la structure dans le cadre d'un travail de recherche  mené sur les vieilles forêts.

----

## XLSForm

![logo Excel](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/excel_2013.png "logo Excel"){: .img-thumbnail-left }

Un fichier [XLSForm] est un tableur enregistré au format XLS ou XLSX, respectant le standard [XLSForm].

Il est composé d'au moins deux feuilles de calculs obligatoires :

- [survey](#la-feuille-de-calcul-survey) : décrit le formulaire
- [choices](#la-feuille-de-calcul-choices) : contient les listes de valeurs utilisées par les widgets de type "select"
- [settings](#la-feuille-de-calcul-settings) (optionnelle)

Les colonnes utilisables dans chacune des feuilles sont normalisées, toutes ne sont pas obligatoires et vous pouvez ajouter des colonnes "personnelles" qui seront ignorées par l'application.

### La feuille de calcul "survey"

C'est dans cette feuille que sera décrite la logique du formulaire. Chaque question ou élément de structure (groupe de question, répétition) est typé (colonne *type* : quel *widget* sera utilisé pour afficher la question ? ) et nommé (colonne *name*) et étiquetté (colonne *label*). Ces trois colonnes sont obligatoires.

![XLS-Form : feuille de calcul survey](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/xlsform_feuille_de_calcul_survey.png "XLS-Form : feuille de calcul survey"){: .img-center loading=lazy }

Les listes de choix peuvent être filtrées (colonne *choice_filter*)

L'apparence des widgets et des groupes de questions peut être précisée (colonne *appearance*) et son affichage conditionné (colonne *relevant*)

Des contraintes peuvent être associées à chaque question (colonne *constraint*). En cas de violation des contraintes, un message peut-être affiché (colonne *constraint_message*)

Enfin, chaque question peut afficher une astuce (colonne *hint*)

Les formulaires peuvent être affichés dans plusieurs langues et internationalisés.

Les types de questions qui peuvent être utilisés dans le formulaires sont décrits ici : <https://docs.getodk.org/form-question-types/>.  
Dans cet article, nous détaillons plus bas [les *widgets* cartographiques](#focus-sur-les-widgets-geographiques). Nous verrons plusieurs exemples de *widgets* dans le second volet de cette série sur ODK.

### La feuille de calcul "choices"

Les listes de choix sont nommées (colonne *list_name*) et contiennent pour chaque élément de la liste une valeur (colonne *name*) et une étiquette (colonne *label*). Ces trois colonnes sont obligatoires dans La feuille de calcul *choices*.

![XLS-Form : feuille de calcul choices](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/xlsform_feuille_de_calcul_choices.png "XLS-Form : feuille de calcul choices"){: .img-center loading=lazy }

Des colonnes personnelles peuvent être ajoutées et ainsi être utilisées comme critère dans la colonne *choice _filter* de la feuille *survey*. C'est par exemple dans une colonne "groupe" que je préciserai pour l'élément "têtard" la valeur "batracien" afin de ne pas proposer cette valeur à la saisie pour une observation d'oiseau.

### La feuille de calcul "settings"

Elle contient la version du formulaire ainsi que le nom que l'on souhaite donner à chacune des instances envoyées au serveur. Ce nom peut intégrer des variables issues du formulaire.

![XLS-Form : feuille de calcul settings](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/xlsform_feuille_de_calcul_settings.png "XLS-Form : feuille de calcul settings"){: .img-center loading=lazy }

### Focus sur les widgets géographiques

![icône globe](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "icône globe"){: .img-thumbnail-left }

Plusieurs interfaces (*widgets*) cartographiques de saisie vont nous être proposées par ODK. Toutes reposent sur l'utilisation d'un fond de carte et d'une librairie géographique. Pour simplifier la chose à l'utilisateur, le distinguo n'est plus fait à ce sujet dans les réglages de l'application.  
L'utilisateur doit simplement choisir le fond de carte à utiliser, et, quand ce dernier propose plusieurs "styles" (satellite, terrain...) choisir celui qui convient.

![Choix du fond de carte](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/choix_du_fond_de_carte.png "Choix du fond de carte"){: loading=lazy align=left clear=right width=350px }
![Choix du style du fond de carte](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/preferences_carto_mapbox.png "Choix du style fond de carte"){: loading=lazy align=left clear=right width=350px }
{: align=middle }

Ce fond de carte pourra être surchargé par un fond "maison" en (fichier `.mbtiles`) généré avec QGIS par exemple.
Les tuiles vecteurs peuvent être utilisées aussi mais seulement avec le fond de carte Mapbox, et elle ne sont pour l'instant pas "stylées".

Les points et les sommets des lignes et des polygones sont décrits par 4 valeurs séparées par un espace : latitude longitude altitude précision

Une valeur par défaut peut être renseignée. Un point (latitude longitude altitude precision ) ou une série de points séparés par un point-virgule.

#### Geopoint

Par défaut le [Geopoint](https://docs.getodk.org/form-question-types/#geopoint) enregistre la postion du GPS sans l'afficher sur une carte. La précision minimale requise pour enregistrer le point peut être précisée. Elle est par défaut de 5m.

Dés que la précision du signal sera inférieure à la tolérance précisée dans le formulaire (5m par défaut), le point sera enregistré. L'utilisateur peut à tout moment outrepasser cette contrainte en enregistrant manuellement le "PointGéo".
Dans l'exemple ci-dessous, une précision minimale de 10 était requise.

![Recherche de point GPS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/recherche_point_automatique.png "Calcul de la position du GPS - Recherche de point GPS"){: loading=lazy width=350px }
![Propriétés du point enregistré](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/point_automatique_sous_precision_minimale.png "ODK Geopoint - Affichage des coordonnées enregistrées automatiquement et de la précision du signal"){: loading=lazy width=350px }
{: align=middle }

#### Localisation GPS affichée sur une carte

Si une [apparence (colonne *appearance*) `maps`](https://docs.getodk.org/form-question-types/#geopoint-with-map-display) est mentionnée alors le point calculé sera montré sur une carte à l'utilisateur, qui pourra recapturer le point s'il ne convient pas.

L'emplacement du GPS est matérialisé par une croix bleue autour de laquelle un disque transparent représente la précision du GPS. Si cela convient, on peut enregistrer le point. Il sera matérialisé par un petit cercle rouge.

#### Localisation entrée par l'utilisateur, carte centrée sur le GPS

![Geopoint with placement map](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/localisation_par_defaut_sur_point_gps.png "Geopoint with placement map"){: loading=lazy align=left clear=right width=150px }

Si une [apparence (colonne *appearance*) `placement_maps`](https://docs.getodk.org/form-question-types/#geopoint-with-user-selected-location) est mentionnée alors l'utilisateur pourra cliquer le point sur la carte ou enregistrer l'emplacement courant, matérialisé comme précédemment.

Une valeur par défaut peut-être spécifiée. La carte s'ouvrira sur cette valeur. Ici de quoi afficher l'emplacement du siège Montpelliérain du CEN Occitanie : `3.8934834 43.6089782 0 0`.

#### Geotrace

Il s'agit d'une [série de points, au moins deux, formant une ligne](https://docs.getodk.org/form-question-types/#geotrace-widget), le premier et le dernier points étant différents.

3 modes d'enregistrement sont possibles et proposés au lancement de la "Geotrace" :

- la saisie manuelle en cliquant (tapotant) chacun des points sur la carte
- l'enregistrement manuel des points constituant la ligne. La localisation du GPS apparaît sur la carte, l'utilisateur peut à tout moment enregistrer la position courante
- l'enregistrement automatique des points au fil du déplacement de l'utilisateur, avec précision du pas de temps et de la précision requise pour enregistrer le sommet (par exemple ci-dessous 1 point toutes les 20 secondes avec une précision minimale requise de 10 mètres). La précision minimale du GPS requise pour créer le point peut-être spécifiée.

![ODK Geotrace/Geoshape : options disponibles pour la création de sommets](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/choix_enregistrement_manuel.png){: loading=lazy width=175px }
![ODK Geotrace/Geoshape : saisie en tapotant sur la carte](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/dessin_geometrie_en_tapotant.png){: loading=lazy width=175px }
![ODK Geotrace/Geoshape : enregistrement manuel des points GPS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ecran_enregistrement_manuel_de_sommet.png){: loading=lazy width=175px }
![ODK Geotrace/Geoshape : enregistrement automatique de la trace](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/choix_enregistrement_auto_avec_precision_mini_et_intervalle_temps.png){: loading=lazy width=175px }
{: align=middle }

#### Geoshape

[Geoshape (polygone)](https://docs.getodk.org/form-question-types/#geoshape) est similaire à la #geotrace si ce n'est que le dernier point de la série est identique au premier. Les modes de saisie proposés à l'utilisateur sont les mêmes.

#### Bearing

[Bearing (boussole)](https://docs.getodk.org/form-question-types/#bearing-widget) est une apparence pour un champ décimal, qui enregistre l'azimuth, l'angle entre la direction du téléphone et le Nord, de 0 à 360°. Nous ne l'avons jamais utilisé.

#### OpenMapKit

[OpenMapKit](https://docs.getodk.org/form-question-types/#openmapkit-widget) permet de poser des questions sur des objets OpenStreetMap dans un formulaire ODK. Voir la documentation d'[OpenMapKit](http://www.openmapkit.org/) pour plus d'information. Nous ne l'avons jamais utilisé.

----

## A suivre

- La mise en oeuvre d'ODK avec la présentation détaillée de notre formulaire "généraliste"
- La récupération des données collectées dans notre base de données PostGIS

[Lire la deuxième partie :fontawesome-solid-forward:](2021-06-22_odk_postgis_2.md){: .md-button }
{: align=middle }

----

## Quelques ressources en ligne

- Une interview de Yaw Anokwa pour le podcast Aid, Evolved : <https://aidevolved.com/podcast/yaw-anokwa/>
- Un webinaire organisé par la Fédération Internationale de la Croix Rouge et du Croissant Rouge sur l'impact de leur usage d'ODK : <https://www.youtube.com/watch?v=jjSkMu0WFVI>
- Un autre sur les inovations dans ODK et leurs impacts sur la collecte de données dans le domaine de l'agriculture <https://www.youtube.com/watch?v=rVb8voaN4Fg>
- Présentation de notre formulaire généraliste sur le forum d'ODK : <https://forum.getodk.org/t/odk-to-collect-species-and-habitats-localities-as-pressure-and-threats-to-ecosystems/26332>
- Les tutoriels de "Statistics for Sustainable Development : <https://stats4sd.org/resources/507>
- Les vidéos de <https://www.humanitariandatasolutions.com/>

----
<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-sa.md" %}

<!-- Hyperlinks reference -->
[Conservatoire d'Espaces Naturels d'Occitanie]: https://www.cen-occitanie.org
[GetODK]: https://getodk.org/
[XLSForm]: https://xlsform.org/en/
