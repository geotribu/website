---
title: "Open Data Kit pour la collecte de données géographiques dans PostGIS (1/3)"
authors: ["Mathieu BOSSAERT"]
categories: ["article"]
date: "2021-06-08 10:20"
description: "Premier article de présentation de la suite Open Data Kit (ODK) et son intégration au SI du CEN d'Occitanie et dans les processus métiers."
image: "Image d'illustration de l'article qui sert ensuite dans la mise en avant : réseaux sociaux, flux RSS..."
tags: "ODK,Open Data Kit,PostgreSQL,PostGIS,collecte,Android"
---

# ODK pour la collecte de données géo dans PostGIS (1/3)

:calendar: Date de publication initiale : 08 juin 2021

**Mots-clés :** ODK | PostgreSQL | PostGIS | Android

![ODK PostGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/Central2PG.png "ODK + PostGIS"){: .img-rdp-news-thumb }

Cette série de 3 articles vise à présenter Open Data Kit, qui est une solution de recueil de données sur téléphone Android, utilisée par le [Conservatoire d'Espaces Naturels d'Occitanie], pour la collecte de données spatialisées de biodiversité, et leur intégration à une base de données PostGIS.

Ce premier article, introductif, présente le projet ODK, ses outils ainsi que les possibilités cartographiques.  
Le second détaillera les possibilités de création de formulaire à travers l'exemple détaillé du formulaire généraliste du [Conservatoire d'Espaces Naturels d'Occitanie].  
Le dernier sera consacré à la récupération des données collectées dans une base de données PostGIS.

<!-- [2ème partie : Mise en oeuvre d'ODK avec la présentation détaillée de notre formulaire "généraliste" :fontawesome-solid-step-forward:](#){: .md-button }
[3ème partie : Récupération des données collectées dans notre base de données PostGIS :fontawesome-solid-fast-forward:](#){: .md-button }
{: align=middle } -->

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
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

![logo Open Data Kit (ODK)](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/odk_open_data_kit.png "logo Open Data Kit (ODK)"){: .img-rdp-news-thumb }

Du côté de la gouvernance, [GetODK], la société qui développe ODK, est une [équipe composée de 9 personnes](https://getodk.org/about/team.html) qui s'appuie sur un comité technique, appelé [TAB (Technical Advisory Board)](https://github.com/getodk/governance/blob/master/TAB-GOVERNANCE.md) impliquant des utilisateurs de toute la planète et de différents domaines. Ce TAB se réunit tous les 15 jours [de manière très transparente](https://forum.getodk.org/tag/tab-meeting).

![team ODK](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/Equipe_GetODK.png "équipe de GetODK" ){: .img-center loading=lazy }

Le forum est le principal lieu d'échange entre utilisateurs et développeurs. Il compte 14 000 inscrits !  
La communauté est assez exemplaire en ce sens qu'il y a beaucoup d'interactions entre utilisateurs qui y échangent conseils et bonnes pratiques. Le forum fait remonter les besoins des utilisateurs et les échanges sont riches avec les développeurs, toujours curieux de l'utilisation faite des outils.

C'est un lieu de discussion mondial, où il n'est pas rare d'échanger avec des utilisateurs de tous les continents en une journée. La bienveillance et l'entraide qui y règnent facilitent les échanges entre membres de tous niveaux et font de ce forum un "endroit" chaleureux !

----

## Les outils de la "suite" ODK

Les outils de la suite ODK sont sollicités en différents points du Système d'information géographiques (SIG) du Cen.
Le serveur nommé Central est au centre du système. Collect (sur les téléphones) et Enketo sur Firefox proposent les interfaces de collecte de données.

![place d'odk dans le SIG du Conservatoire d'espaces naturels](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/odk_dans_le_SIG_du_CEN_Occitanie.png "les outils d'ODK dans le SIG du Cen)"){: .img-center loading=lazy }

### Collect

C'est l'outil déployé sur les terminaux Android, qui sert les formulaires, permet de les remplir et envoie les données collectées au serveur.

### Central

C'est le serveur qui remplace désormais [Aggregate](https://forum.getodk.org/t/aggregate-is-no-longer-being-updated/33742). Il assure la gestion et la diffusion des formulaires, des utilisateurs, des droits de ces derniers et la collecte des "soumissions" (données envoyées par Collect). Il inclut aussi [enketo](https://enketo.org/), de sorte que les formulaires réalisés sont désormais aussi utilisables en ligne à travers un naviguateur, et en mode déconnecté.

[![ODK Central : page d'accueil](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/accueil_odk_central.png "Page d'accueil d'ODK Central"){: loading=lazy width=300 }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/accueil_odk_central.png){: data-mediabox="lightbox-gallery" data-title="Page d'accueil d'ODK Central"}
[![Page d'un projet dans ODK Central](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/formualire_et_soumissions_dans_odk_central.png "Quête : bornes de recyclage"){: loading=lazy width=300px }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/formualire_et_soumissions_dans_odk_central.png){: data-mediabox="lightbox-gallery" data-title="Page d'un projet dans ODK Central"}

Central embarque [Enketo](https://enketo.org) pour permettre le remplissage de formulaires dans un naviguateur. Et depuis la version 1.2 publiée en mai 2021, l’édition des données envoyées au serveur est possible à travers cet outil (à des fins de correction ou révision).

[![Enketo : formulaire d'enquête sur les usagers d'ODK](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/enketo_usages_odk.png "Enketo : formulaire d'enquête sur les usagers d'ODK"){: loading=lazy width=300 }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/enketo_usages_odk.png){: data-mediabox="lightbox-gallery" data-title="Enketo : formulaire d'enquête sur les usagers d'ODK"}
[![Enketo : formulaire sur les utilisations des voitures de service](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/enketo_formulaire_voiture_de_service.png "XLS-Form : feuille de calcul choices"){: loading=lazy width=300px }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/enketo_formulaire_voiture_de_service.png){: data-mediabox="lightbox-gallery" data-title="Enketo : formulaire sur les utilisations des voitures de service"}

### Tableur / XLSForm

ODK utilise un sous-ensemble de la norme XForms du W3C pour créer des formulaires (voir [ici la documentation relative à ODK XForms](https://getodk.github.io/xforms-spec/)).

Une norme intermédiaire nommée [XLSForm](https://xlsform.org/en/) permet de décrire très simplement le formulaire dans un tableur, selon un formalisme simple. C'est avec notre tableur (calc / Excel) préféré que nous allons décrire notre formulaire dans ce formalisme.

[XLSForm](https://xlsform.org/en/) est utilisé par de nombreuses solutions ([Enketo](https://enketo.org/), [Kobotoolbox](https://www.kobotoolbox.org/), [ONA](https://company.ona.io/products/ona-data/features/)). La plus connue des géomaticiens sera peut-être [la plateforme Survey123](https://doc.arcgis.com/fr/survey123/desktop/create-surveys/xlsformessentials.htm) d'ESRI.


[![XLS-Form : feuille de calcul survey](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/xlsform_feuille_de_calcul_survey.png "XLS-Form : feuille de calcul survey"){: loading=lazy width=300 }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/xlsform_feuille_de_calcul_survey.png){: data-mediabox="lightbox-gallery" data-title="XLS-Form : feuille de calcul survey"}
[![XLS-Form : feuille de calcul choices](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/xlsform_feuille_de_calcul_choices.png "XLS-Form : feuille de calcul choices"){: loading=lazy width=300px }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/xlsform_feuille_de_calcul_choices.png){: data-mediabox="lightbox-gallery" data-title="XLS-Form : feuille de calcul choices"}
[![XLS-Form : feuille de calcul settings](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/xlsform_feuille_de_calcul_settings.png "XLS-Form : feuille de calcul settings"){: loading=lazy width=300px }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/xlsform_feuille_de_calcul_settings.png){: data-mediabox="lightbox-gallery" data-title="XLS-Form : feuille de calcul settings"}

### [xlsform online](https://xlsform.getodk.org/)

C'est un outil en ligne, qui permet de transformer le fichier xlsform en xml à charger sur le téléphone. Il n'est pas utile si vous utilisez Central, car ce dernier accepte directement le fichier xls.

### [ODKBuild](https://docs.getodk.org/build-intro/)

C'est l'éditeur WYSIWYG de formulaires. Nous ne le présenterons pas dans la série d'article, car nous avons toujours créé nos formulaires avec xlsform.

### [Briefcase](https://docs.getodk.org/briefcase-intro/)

Il permet de pousser des formulaires sur le serveur, d'y récupérer les données et médias "soumis" et aussi de récupérer les données et médias directement depuis votre téléphone, et donc d'utiliser la solution sans avoir déployé Central.
[![ODK Briefcase : récupération des données depuis Collect](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ODK_briefcase_recuperation_de_donnees_depuis_le_telephone.png "ODK Briefcase : récupération des données depuis Central"){: loading=lazy width=300 }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ODK_briefcase_recuperation_de_donnees_depuis_le_telephone.png){: data-mediabox="lightbox-gallery" data-title="ODK Briefcase : récupération des données depuis Central"}
[![ODK Briefcase : récupération des données depuis Central](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ODK_briefcase_recuperation_de_donnees_depuis_central.png "ODK Briefcase : récupération des données depuis Central"){: loading=lazy width=140px }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ODK_briefcase_recuperation_de_donnees_depuis_central.png){: data-mediabox="lightbox-gallery" data-title="ODK Briefcase : récupération des données depuis Central"}
[![ODK Briefcase : paramétrage de l'export des données récupérées](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ODK_briefcase_parametres_d_export_des_donnees_recuperees.png "ODK Briefcase : paramétrage de l'export des données récupérées"){: loading=lazy width=3000px }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/formualire_et_soumissions_dans_odk_central.png){: data-mediabox="lightbox-gallery" data-title="ODK Briefcase : paramétrage de l'export des données récupérées"}

### Les outils communautaires

Voici deux outils qui ne sont pas développés par l'équipe d'ODK, mais par des membres de la communauté, et qui sont utiliés ou en passe de l'être au CEN. C'est pour ces deux raisons qu'ils apparaissent en transparence sur le schéma.

L'[extension QRealTime pour QGIS](https://shivareddyiirs.github.io/QRealTime/), développée par Shiva Reddy Koti et Prabhakar Alok Verma, permet d’afficher directement les données collectées et aussi de créer des formulaires vierges à partir de QGIS. Elle est disponible directement depuis le gestionnaire d'extensions de QGIS.

[ruODK](https://docs.ropensci.org/ruODK/) est un client R pour l'API d'ODK Central, developpé par un membre du TAB ([Florian Mayer](https://forum.getodk.org/u/florian_may/summary)), qui permet de mobiliser directement les données collectées dans R. Il est utilisé depuis peu dans la structure dans le cadre d'un travail de recherche  mené sur les vieilles forêts.

## XLSForm

Un fichier XLSForm est une tableur enregistré au format xls ou xlsx, respectant le standard XLSForm.

Il est composé d'au moins deux feuilles de calculs :

- survey
- choices
- settings (optionnelle)

La feuille de calcul "survey" décrit le formulaire, la feuille "choices" contient les listes de valeurs utilisées par les widgets de type "select".

Les colonnes utilisables dans chacune des feuilles sont normalisées, toutes ne sont pas obligatoires et vous pouvez ajouter des colonnes "personnelles" qui seront ignorées par l'application.

### la feuille de calcul "survey"

C'est dans cette feuille que sera décrite la logique du formulaire. Chaque question ou élément de structure (groupe de question, répétition) est typé (colonne *type* : quel *widget* sera utilisé pour afficher la question ? ) et nommé (colonne *name*) et étiquetté (colonne *label*). Ces trois colonnes sont obligatoires.

Les listes de choix peuvent être filtrées (colonne *choice_filter*)

L'apparence des widgets et des groupes de questions peut être précisée (colonne *appearance*) et son affichage conditionné (colonne *relevant*)

Des contraintes peuvent être associées à chaque question (colonne *constraint*). En cas de violation des contraintes, un message peut-être affiché (colonne *constraint_message*)

Enfin, chaque question peut afficher une astuce (colonne *hint*)

Les formulaires peuvent être affichés dans plusieurs langues et internationalisés.

Les types de questions qui peuvent être utilisés dans le formulaires sont décrits ici : <https://docs.getodk.org/form-question-types/>
Nous verrons plusieurs exemple de *widgets* dans la seconde volet de cette série sur ODK. Dans cet article, nous détaillons plus bas les *widgets* cartographiques.

### la feuille de calcul "choices"

Les listes de choix sont nommées (colonne *list_name*) et contiennent pour chaque élément de la liste une valeur (colonne *name*) et une étiquette (colonne *label*). Ces trois colonnes sont obligatoires dans la feuille de calcul *choices*.

Des colonnes personnelles peuvent être ajoutées et ainsi être utilisées comme critère dans la colonne *choice _filter* de la feuille *survey*. C'est par exemple dans une colonne "groupe" que je préciserai pour l'élément "têtard" la valeur "batracien" afin de ne pas proposer cette valeur à la saisie pour une observation d'oiseau.

### la feuille de calcul "settings"

Elle contient la version du formulaire ainsi que le nom que l'on souhaite donner à chacune des instances envoyées au serveur. Ce nom peut intégrer des variables issues du formulaire.

### Focus sur les widgets géographiques

Plusieurs interfaces (*widgets*) cartographiques de saisie vont nous être proposées par ODK. Toutes reposent sur l'utilisation d'un fond de carte et d'une librairie géographique. Pour simplifier la chose à l'utilisateur, le distinguo n'est plus fait à ce sujet dans les réglages de l'application.  
L'utilisateur doit simplement choisir le fond de carte à utiliser, et, quand ce dernier propose plusieurs "styles" (satellite, terrain...) choisir celui qui convient.

![Choix du fond de la librairie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/choix_du_fond_de_carte.png "Choix du fond de la librairie"){: .img-center loading=lazy }

![Choix du fond de la librairie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/preferences_carto_mapbox.png "Choix du fond de la librairie"){: .img-center loading=lazy }

Ce fond de carte pourra être surchargé par un fond "maison" en (fichier `.mbtiles`) généré avec QGIS par exemple.
Les tuiles vecteurs peuvent être utilisées aussi mais seulement avec le fond de carte Mapbox, et elle ne sont pour l'instant pas "stylées".

Les points et les sommets des lignes et des polygones sont décrits par 4 valeurs séparées par un espace : latitude longitude altitude précision

Une valeur par défaut peut être renseignée. Un point (latitude longitude altitude precision ) ou une série de points séparés par un point-virgule.

- [Geopoint (point)](https://docs.getodk.org/form-question-types/#geopoint)

  Par défaut le Geopoint enregistre la postion du GPS sans l'afficher sur une carte. La précision minimale requise pour enregistrer le point peut être précisée. Elle est par défaut de 5m.

![Recherche de point GPS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/recherche_point_automatique.png "calcul de la position du GPS"){: .img-center loading=lazy }

Dés que la précision du signal sera inférieure à la tolérance précisée dans le formulaire (5m par défaut), le point sera enregistré. L'utilisateur peut à tout moment outrepasser cette contrainte en enregistrant manuellement le "PointGéo".
Dans l'exemple ci-dessous, une précision minimale de 10 était requise.

![Affichage des propriétés du point enregistré](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/point_automatique_sous_precision_minimale.png "Affichage des coordonnées enregistrées automatiquement et de la précision du signal"){: .img-center loading=lazy }

- [Localisation GPS affichée sur une carte](https://docs.getodk.org/form-question-types/#geopoint-with-map-display)

    Si une apparence (colonne *appearence*) "maps" est mentionnée alors le point calculé sera montré sur une carte à l'utilisateur, qui pourra recapturer le point s'il ne convient pas.

    L'emplacement du GPS est matérialisé par une croix bleue autour de laquelle un disque transparent représente la précision du GPS. Si cela convient, on peut enregistrer le point. Il sera matérialisé par un petit cercle rouge.

- [Localisation entrée par l'utilisateur, carte centrée sur le GPS](https://docs.getodk.org/form-question-types/#geopoint-with-user-selected-location)

    Si une apparence (colonne *appearence*) "placement_maps" est mentionnée alors l'utilisateur pourra cliquer le point sur la carte ou enregistrer l'emplacement courant, matérialisé comme précédemment.

![Geopoint with placement map](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/localisation_par_defaut_sur_point_gps.png){: .img-center loading=lazy }

  Une valeur par défaut peut-être spécifiée. La carte s'ouvrira sur cette valeur. Ici de quoi afficher l'emplacement du siège Montpelliérain du CEN Occitanie :
  3.8934834 43.6089782 0 0

- [Geotrace (ligne)](https://docs.getodk.org/form-question-types/#geotrace-widget)

  C'est une série de points, au moins deux, formant une ligne, le premier et le dernier point sont différents.

  3 modes d'enregistrement sont possibles et proposés au lancement de la "Geotrace" :

![choix possible pour création de sommets](<https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/choix_enregistrement_manuel.png>){: .img-center loading=lazy }

- la saisie manuelle en cliquant (tapotant) chacun des points sur la carte

![saisie en tapotant](<https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/dessin_geometrie_en_tapotant.png>){: .img-center loading=lazy }

- l'enregistrement manuel des points constituant la ligne. La localisation du GPS apparaît sur la carte, l'utilisateur peut à tout moment enregistrer la position courante

![enregistrement manuel des points GPS](<https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/ecran_enregistrement_manuel_de_sommet.png>){: .img-center loading=lazy }

- l'enregistrement automatique des points au fil du déplacement de l'utilisateur, avec précision du pas de temps et de la précision requise pour enregistrer le sommet (par exemple ci-dessous 1 point toutes les 20 secondes avec une précision minimale requise de 10 mètres). La précision minimale du GPS requise pour créer le point peut-être spécifiée.

![enregistrement automatique de la trace](<https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/choix_enregistrement_auto_avec_precision_mini_et_intervalle_temps.png> ){: .img-center loading=lazy }

- [Geoshape (polygone)](https://docs.getodk.org/form-question-types/#geoshape)

  Identique à la Geotrace si ce n'est que le dernier point de la série est identique au premier. Les modes de saisie proposés à l'utilisateur sont les mêmes.

- [Bearing (boussole)](https://docs.getodk.org/form-question-types/#bearing-widget)

C'est une apparence pour un champ décimal, qui enregistre l'azimuth, l'angle entre la direction du téléphone et le Nord, de 0 à 360°. Nous ne l'avons jamais utilisé.

- [OpenMapKit](https://docs.getodk.org/form-question-types/#openmapkit-widget)

  Permet de poser des questions sur des objets OpenStreetMap dans un formulaire ODK. Voir la documentation d'[OpenMapKit](http://www.openmapkit.org/) pour plus d'information. Nous ne l'avons jamais utilisé.

----

## Contexte d'utilisation au CEN Occitanie

La présentation ci-dessous est une traduction du [retour fait en 2020 et 2021 sur le forum d'ODK](https://forum.getodk.org/t/odk-to-collect-species-and-habitats-localities-as-pressure-and-threats-to-ecosystems/26332) .

### Le SI du CEN

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

## A suivre

- La mise en oeuvre d'ODK avec la présentation détaillée de notre formulaire "généraliste"
- La récupération des données collectées dans notre base de données PostGIS

<!-- [Lire la deuxième partie :fontawesome-solid-step-forward:](#){: .md-button }
{: align=middle } -->

----

## Bibliographie / Ressources

- Une interview de Yaw Anokwa pour le podcast Aid, Evolved : <https://aidevolved.com/podcast/yaw-anokwa/>
- Global impact with open source - ODK for mobile data collection : <https://www.youtube.com/watch?v=jjSkMu0WFVI>
- Webinar - Innovations in ODK: Improving Data Collection for agriculture & Scaling to the Global Community <https://www.youtube.com/watch?v=rVb8voaN4Fg>
- Présentation de notre formulaire généraliste sur le forum d'ODK : <https://forum.getodk.org/t/odk-to-collect-species-and-habitats-localities-as-pressure-and-threats-to-ecosystems/26332>
- [sta4sd tutorials](https://stats4sd.org/resources/507)
- les vidéos de <https://www.humanitariandatasolutions.com/>

----

## Auteur

## Mathieu Bossaert

![Portrait Mathieu Bossaert]( "Portrait Mathieu Bossaert"){: .img-rdp-news-thumb }

<!-- Hyperlinks reference -->

[Conservatoire d'Espaces Naturels d'Occitanie]: https://www.cen-occitanie.org
["blog" géomatique du CEN]: https://si.cen-occitanie.org
[GetODK]: https://getodk.org/
