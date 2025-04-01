---
title: Effectuer un relevé de terrain avec QGIS et QField
authors:
    - Valérian LEBERT
categories:
    - article
comments: true
date: 2022-05-24
description: Retour d'expérience de l'utilisation de QField en milieu professionnel. Astuces et méthodes de synchronisation.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield.jpg
license: cc4_by-sa
tags:
    - collecte
    - Lizmap
    - QField
    - QGIS
---

# Relevé terrain avec QField et solutions de synchronisation (hors QField Cloud)

:calendar: Date de publication initiale : 24 mai 2022

## Introduction

![logo QField](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qfield.png "logo QField"){: .img-thumbnail-left }

Pour donner suite à [l’article récent sur Input](2022-03-11_releve_terrain_qgis_input.md), et pour répondre à une perche tendue par Julien, j’ai décidé de prendre ma plume pour vous livrer un petit retour d’expérience de mon utilisation intensive de QField ces dernières années avec le cabinet Tactis.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Terrain de jeu

Tout d’abord, quelques informations factuelles pour illustrer notre expérience avec QField  :

- **Utilisation en production depuis 2017**. J’ai pu mettre la main sur notre premier point QField créé le 21/12/2017 à Vaison-La-Romaine. On notera l’utilisation de captures annotées qui sont parfois un "entre deux" utiles entre une donnée SIG structurée et des informations complexes à restituer.

   [![Premier point](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_premier_point.png "Premier point"){: .img-center loading=lazy}

- Utilisation dans différents contextes
    - Suivi de travaux,
    - relevé/recensement,
    - audit de site pour implantation d’infrastructure,
- Utilisation par différents profils utilisateurs, y compris moins technophiles
- Utilisation sur différentes latitudes. Ici, c'est surtout le retour d’expérience hardware qui est intéressant : très compliqué d’utiliser des tablettes "classiques" en conditions de forte chaleur et ensoleillement.

   [![Cote d'Ivoire](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_cote_ivoire.png "Cote d'Ivoire"){: .img-center loading=lazy}

- Supervision d’**une vingtaine de tablettes** en utilisation régulière, ce qui nous a demandé d’industrialiser nos méthodes de support et de consolidation de la donnée.
- **Environ 100 000 points** créés avec QField

   [![Mass points](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_mass_point.png "Mass points"){: .img-center loading=lazy}

----

## Alternatives

Input est une alternative qui a été présentée dans [le précédent article](2022-03-11_releve_terrain_qgis_input.md).

Il y a aussi plusieurs solutions de collecte de donnée sans interface SIG (KoboCollect et ODK [aussi présenté ici même l'an dernier](../2021/2021-06-08_odk_postgis_1.md), par exemple). Si la collecte de donnée ne requiert pas d’affichage de référentiel SIG, ces dernières solutions peuvent être plus simple à mettre en œuvre.

La réelle force des applications Input et QField est donc

- De pouvoir produire et consulter de la donnée SIG sur le terrain, en s’appuyant sur un référentiel riche.
- De pouvoir si besoin produire de la donnée SIG complexe (lignes, polygones).

   [![QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_qgis_project.png "QGIS"){: .img-center loading=lazy}

----

## Avantages et inconvénients

### Avantages

- C’est un vrai outil SIG qui permet une restitution à l’identique de QGIS. Pas de limite dans la symbologie et les échelles de visibilité.
- Fluidité parfois meilleure que sur un QGIS-windows
- Le GPS couplé à un bon fond de plan permet une bonne précision dans le pointage.
- La possibilité de gérer des modèles de formulaires complexes (onglets, relations avec sous-formulaires...)
- La gestion des photos.

### Inconvénients

- Paramétrage un peu technique dans QGIS : impossible à déléguer à des non-sigistes.
- Quelques instabilités et plantages

----

## Mise en œuvre

### Montage du projet QGIS + dépendances

J’ai pris l’habitude de monter mes projets avec l’arborescence suivante :

![Files and folders](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_files_and_folders.png "Files and folders"){: .img-center loading=lazy}

### Astuces à savoir dans le paramétrage QGIS

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-thumbnail-left }

Penser aux échelles de visibilité (symboles et étiquettes) pour alléger au maximum l’affichage en mobilité.

Ne **pas** utiliser les effets d’ombrage qui font vraiment ramer le projet sous tablette.

Utiliser les thèmes pour basculer facilement entre différentes vues.

![Themes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_qgis_themes.png "Themes"){: loading=lazy}
{: align=middle }

Si certaines données sont particulièrement denses ainsi que pour les zones superposées (ex : zones techniques, parcelles, bâti...), veillez à ne pas mettre toutes les couches en "identifiable", car sinon l’identification des items utiles peut s’avérer polluée en mode tactile. Uniquement laisser les couches qui ont vocation à être interrogées.

![Identify](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_qgis_identify.png "Identify"){: .img-center loading=lazy}

Usez et abusez de toutes les fonctionnalités du formulaire d’attributs (onglets, valeurs par défaut, formules, contraintes, non nul, relations, etc.). Presque tout est supporté par QField.

![Forms](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_qgis_forms.png "Forms"){: .img-center loading=lazy}

Utilisez le générateur d’UUID pour faire des clés primaires uniques entre vos différents terminaux, ce qui permettra ensuite de consolider l’ensemble plus facilement.

### Gestion de la synchronisation des projets

!!! info
    Notre utilisation de QField remonte à bien avant l’ère de QField Cloud. C’est pourquoi nous avons développé nos propres solutions de synchronisation pour gérer les flux de données vers et depuis les terminaux.  
    Depuis, QField Cloud a bien évolué et mériterait probablement un test approfondi et un article dédié. Bientôt peut-être.  
    Enfin, depuis la version 2.0.15, QField a modifié ses modalités d’accès au système de fichier Android, ce qui rend les solutions ci-dessus inutilisables avec les dernières versions de QField ([https://docs.qfield.org/get-started/storage/](https://docs.qfield.org/get-started/storage/)). Heureusement, les APK des anciennes versions restent disponibles ici : [https://github.com/opengisch/QField/releases](https://github.com/opengisch/QField/releases)

#### PostGIS

![logo PostGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/postgis.png "logo PostGIS"){: .img-thumbnail-left }

Dans le meilleur des mondes (sauf pour les allergiques à la 5G), nous aurions de la connectivité partout et il suffirait de bâtir un projet 100% online, derrière un serveur PostGIS par exemple. Reste à gérer le partage des projets (.qgs), qui peut être fait avec un simple stockage cloud type Gdrive.

![Postgis](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_postgis.png "Postgis"){: .img-center loading=lazy}

#### Syncthing

![logo Syncthing](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/syncthing.png "logo Syncthing"){: .img-thumbnail-left }

Dans la vraie vie, on intervient encore sur des zones à faibles connectivités (surtout quand on travaille dans le déploiement du réseau télécoms, ce qui était mon cas, mais c’est aussi vrai pour bien d’autres secteurs). De plus, si la collecte implique des photos, PostGIS ne sera pas suffisant pour remonter les fichiers.

Il existe certainement plusieurs outils qui permettent de faire de la synchronisation de dossiers depuis des terminaux Android, mais après en avoir testé beaucoup, seul [Syncthing](https://syncthing.net/) s’est avéré vraiment fiable.

![Syncthing](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_syncthing.png "Syncthing"){: .img-center loading=lazy}

Pour gérer une administration d’utilisateurs (plusieurs utilisateurs, plusieurs projets, plusieurs droits) on peut ajouter un cloud personnel type Seafile (qui avait l’avantage jusqu’à la version 2.25 de télécharger les données dans un répertoire facilement accessible sous Android).

![Syncthing](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_syncthing_2.png "Syncthing"){: .img-center loading=lazy}

![Seafile](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_seafile_syncthing.png "Seafile"){: .img-center loading=lazy}

L’inconvénient est que cela nécessite tout de maintenir des applications serveur, ce qui est rigolo un temps et source de stress ensuite 🙂.

#### Git

![logo Git](https://cdn.geotribu.fr/img/logos-icones/divers/git.png "logo Git"){: .img-thumbnail-left }

Dernièrement, j’utilise [Git] pour gérer le partage et la synchronisation de projets QField sur une flotte de tablette. Le principe est le suivant :

- Hébergement sur Gitlab (10 Go par projet sur un compte gratuit !!)
- Une branche Master et N branches par tablette utilisatrices
    - L’administrateur peut commiter des MAJ du projet .qgs ou bien du référentiel (sous-dossier "etudes" dans mon arborescence plus haut). On évite de toucher au sous-dossier "controle", sauf si indispensable.
    - Les tablettes utilisatrices commit uniquement dans le sous-dossier "controle" dans leur branche (pour éviter de créer des conflits et continuer de recevoir les MAJ du master)
- Un serveur avec un script simple et périodique pour :
    - pull depuis origin
    - passer dans chaque branche et exécuter le script de synchronisation.

    Le script de synchronisation peut être très simple et dépend de vos outils de restitution. Par exemple pour une consolidation des données de N tablettes vers une table PostGIS + migration des photos vers un serveur web :

    ```bash
    # Requiert une variable d'environnement WS_FOLDER correspondant au dossier du serveur web pour les images
    # Le script doit être exécuté à partir du répertoire racine du [Git]
    PICTS_FOLDER=$WS_FOLDER/MB/RBAL

    # Copie des images
    rsync -av DCIM/* $PICTS_FOLDER
    ogr2ogr --config PG_USE_COPY YES -f PostgreSQL PG:" dbname='$PG_DBNAME' host=$PG_HOST port=$PG_PORT user='$PG_USER' password='$PG_PASSWORD' active_schema=qfield_mb " "controle/mb_controle_rbal.sqlite" controle_rbal -append -skipfailures -nln qfield_mb.mb_controle_rbal -sql "SELECT *, '$branch' AS source FROM controle_rbal"
    ogr2ogr --config PG_USE_COPY YES -f PostgreSQL PG:" dbname='$PG_DBNAME' host=$PG_HOST port=$PG_PORT user='$PG_USER' password='$PG_PASSWORD' active_schema=qfield_mb " "controle/mb_add_rbal.sqlite" t_adresse -append -skipfailures -nln qfield_mb.mb_add_rbal -sql "SELECT *, '$branch' AS source FROM t_adresse"
    ```

!!! warning
    Attention à bien mettre une contrainte d’unicité sur l’UUID pour éviter d’importer plusieurs fois les mêmes données. L’importation complète avec -skipfailures (pour les erreurs d’unicité) est un peu bourrin, mais infaillible.

Côté tablette, j’ai développé un ensemble de scripts bash utilisés avec termux, termux-widget et termux-api pour :

- Lister les projets existants
- Télécharger un nouveau projet
- Synchroniser un projet (réception des nouvelles données, et push des données + photos collectées). Au passage, on redimensionne les photos pour ne pas faire exploser le [Git] et le serveur de stockage.
- Affichage de l’avancement dans une notification.

Grâce à un semblant d’UI minimaliste (termux-widget), j’arrive à faire utiliser cette solution par des techniciens qui n’auront pas à mettre le nez dans la console. Cerise sur le gâteau : je gagne beaucoup de temps pour le paramétrage de nouvelles tablettes (il suffit de télécharger/installer 3 APK puis copier/coller une commande d’installation). Et [Git] a ce côté rassurant qu’on ne peut pas perdre de donnée et que la donnée est clonée sur différents terminaux.

----

## Restitution

Pour la restitution des données et leur vie après l’acquisition sur le terrain, j’utilise principalement Lizmap pour une vue WebSIG et Airtable (base de donnée interactive) pour une approche plus "ticketing". Parfois, les deux solutions peuvent être utilisées en parallèle.

![Airtable](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_airtable.png "Airtable"){: .img-center loading=lazy}

![Lizmap](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_qfield_synchronization/qfield_lizmap.png "Lizmap"){: .img-center loading=lazy}

----

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-sa.md" %}
