---
title: "Effectuer un relevé de terrain avec QGIS et QField"
authors:
    - Valérian LEBERT
categories:
    - article
date: "2022-05-10"
description: "Retour d'expérience de l'utilisation de Qfield en milieu professionnel. Astuces et méthodes de synchronisation."
image: "XXX.png"
license: cc4_by-sa
tags:
    - collecte
    - QField
    - QGIS
    - Lizmap
---

# Relevé terrain avec Qfield et solutions de synchronisation (hors Qfield Cloud)

Pour donner suite à [l’article récent sur Input](https://static.geotribu.fr/articles/2022/2022-03-11_releve_terrain_qgis_input/), et pour répondre à une perche tendue par Julien, j’ai décidé de prendre ma plume pour vous livrer un petit retour d’expérience de mon utilisation intensive de Qfield ces dernières années avec le cabinet Tactis.

## Terrain de jeu

Tout d’abord, quelques informations factuelles pour illustrer notre expérience avec Qfield  :

- **Utilisation en production depuis 2017**. J’ai pu mettre la main sur notre premier point Qfield créé le 21/12/2017 à Vaison-La-Romaine. On notera l’utilisation de captures annotées qui sont parfois un “entre deux” utiles entre une donnée SIG structurée et des informations complexes à restituer.

    ![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled.png)

- Utilisation dans différents contextes
    - Suivi de travaux,
    - relevé/recensement,
    - audit de site pour implantation d’infrastructure,
- Utilisation par différents profils utilisateurs, y compris moins technophiles
- Utilisation sur différentes latitudes. Ici, c'est surtout le retour d’expérience hardware qui est intéressant : très compliqué d’utiliser des tablettes “classiques” en conditions de forte chaleur et ensoleillement.

    ![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled%201.png)

- Supervision d’u**ne vingtaine de tablettes** en utilisation régulière, ce qui nous a demandé d’industrialiser nos méthodes de support et de consolidation de la donnée.
- **Environ 100 000 points** créés avec Qfield

    ![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled%202.png)

## Alternatives

Input est une alternative qui a été présenté dans le précédent article.

Il y a aussi plusieurs solutions de collecte de donnée sans interface SIG (KoboCollect et ODK par exemple). Si la collecte de donnée qui ne requiert pas d’affichage de référentiel SIG ces dernières solutions peuvent être plus simple à mettre en œuvre.

La réelle force des applications Input et Qfield est donc

- De pouvoir produire et consulter de la donnée SIG sur le terrain, en s’appuyant sur un référentiel riche.
- De pouvoir si besoin produire de la donnée SIG complexe (lignes, polygones).

    ![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled%203.png)

## Avantages et inconvénients

### Avantages

- C’est un vrai outil SIG qui permet une restitution à l’identique de QGIS. Pas de limite dans la symbologie et les échelles de visibilité.
- Fluidité parfois meilleure que sur un QGIS-windows ‣
- Le GPS couplé à un bon fond de plan permet une bonne précision dans le pointage.
- La possibilité de gérer des modèles de formulaires complexes (onglets, relations avec sous-formulaires...)
- La gestion des photos.

### Inconvénients

- Paramétrage un peu technique dans QGIS : impossible à déléguer à des non-sigistes.
- Quelques instabilités et plantages

## Mise en œuvre

### Montage du projet Qgis + dépendances

J’ai pris l’habitude de monter mes projets avec l’arborescence suivante :

![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled%204.png)

### Astuces à savoir dans le paramétrage Qgis

Penser aux échelles de visibilité (symboles et étiquettes) pour alléger au maximum l’affichage en mobilité.

Ne **pas** utiliser les effets d’ombrage qui font vraiment ramer le projet sous tablette.

Utiliser les thèmes pour basculer facilement entre différentes vues.

![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled%205.png)

Si certaines sonnées sont particulièrement denses ainsi que pour les zones superposées (ex : zones techniques, parcelles, bâti...), veillez à ne pas mettre toutes les couches en “identifiable”, car sinon l’identification des items utiles peut s’avérer polluée en mode tactile. Uniquement laisser les couches qui ont vocation à être interrogées.

![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled%206.png)

Usez et abusez de toutes les fonctionnalités du formulaire d’attributs (onglets, valeurs par défaut, formules, contraintes, non nul, relations, etc.). Presque tout est supporté par Qfield.

![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled%207.png)

Utiliser le générateur d’UUID pour faire des clés primaires uniques entre vos différents terminaux, ce qui permettra ensuite de consolider l’ensemble plus facilement.

### Gestion de la synchronisation des projets

💡 Notre utilisation de Qfield remonte à bien avant l’ère de Qfield Cloud. C’est pourquoi nous avons développé nos propres solutions de synchronisation pour gérer les flux de données vers et depuis les terminaux.
Depuis, Qfield Cloud a bien évolué et mériterait probablement un test approfondi et un article. Bientôt peut-être.
Enfin, depuis la version 2.0.15, Qfield a modifié ses modalités d’accès au système de fichier Android, ce qui rend les solutions ci-dessus inutilisables avec les dernières versions de Qfield ([https://docs.qfield.org/get-started/storage/](https://docs.qfield.org/get-started/storage/)). Heureusement, les APK des anciennes versions restent disponibles ici : [https://github.com/opengisch/QField/releases](https://github.com/opengisch/QField/releases)

### PostGIS

Dans le meilleur des mondes (sauf pour les allergiques à la 5G), nous aurions de la connectivité partout et il suffirait de bâtir un projet 100% online, derrière un serveur PostGIS par exemple. Reste à gérer le partage des projets (.qgs), qui peut être fait avec un simple stockage cloud type Gdrive.

![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled%208.png)

### Syncthing

Dans la vraie vie, on intervient encore sur des zones à faibles connectivités (surtout quand on travaille dans le déploiement du réseau télécoms, ce qui était mon cas, mais c’est aussi vrai pour bien d’autres secteurs). De plus, si la collecte implique des photos, PostGIS ne sera pas suffisant pour remonter les fichiers.

Il existe certainement plusieurs outils qui permettent de faire de la synchronisation de dossiers depuis des terminaux Android, mais après en avoir testé beaucoup, seul [Syncthing](https://syncthing.net/) s’est avéré vraiment fiable.

![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled%209.png)

Pour gérer une administration d’utilisateurs (plusieurs utilisateurs, plusieurs projets, plusieurs droits) on peut ajouter un cloud personnel type Seafile (qui avait l’avantage jusqu’à la version 2.25 de télécharger les données dans un répertoire facilement accessible sous Android)

![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled%2010.png)

![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled%2011.png)

L’inconvénient est que cela nécessite tout de maintenir des applications serveur, ce qui est rigolo un temps et source de stress ensuite 🙂.

### GIT

Dernièrement, j’utilise GIT pour gérer le partage et la synchronisation de projets Qfield sur une flotte de tablette. Le principe est le suivant :

- Hébergement sur Gitlab (10 Go par projet sur un compte gratuit !!)
- Une branche Master et N branches par tablette utilisatrices
    - L’administrateur peut commiter des MAJ du projet .qgs ou bien du référentiel (sous-dossier “etudes” dans mon arborescence plus haut). On évite de toucher au sous-dossier “controle”, sauf si indispensable.
    - Les tablettes utilisatrices commit uniquement le sous-dossier “controle” dans leur branche (pour éviter de créer des conflits et continuer de recevoir les MAJ du master)
- Un serveur avec un script simple et périodique pour :
    - pull depuis origin
    - passer dans chaque branche et exécuter le script de synchronisation.

    Le script de synchronisation peut être très simple et dépend de vos outils de restitution. Par exemple pour une consolidation des données de N tablette vers une table PostGIS + migration des photos vers un serveur web :

    ```bash
    # Requiert une variable d'environnement WS_FOLDER correspondant au dossier du serveur web pour les images
    # Le script doit être exécuté à partir du répertoire racine du GIT
    PICTS_FOLDER=$WS_FOLDER/MB/RBAL

    # Copie des images
    rsync -av DCIM/* $PICTS_FOLDER
    ogr2ogr --config PG_USE_COPY YES -f PostgreSQL PG:" dbname='$PG_DBNAME' host=$PG_HOST port=$PG_PORT user='$PG_USER' password='$PG_PASSWORD' active_schema=qfield_mb " "controle/mb_controle_rbal.sqlite" controle_rbal -append -skipfailures -nln qfield_mb.mb_controle_rbal -sql "SELECT *, '$branch' AS source FROM controle_rbal"
    ogr2ogr --config PG_USE_COPY YES -f PostgreSQL PG:" dbname='$PG_DBNAME' host=$PG_HOST port=$PG_PORT user='$PG_USER' password='$PG_PASSWORD' active_schema=qfield_mb " "controle/mb_add_rbal.sqlite" t_adresse -append -skipfailures -nln qfield_mb.mb_add_rbal -sql "SELECT *, '$branch' AS source FROM t_adresse"
    ```

!!! warning inline end
    Attention à bien mettre une contrainte d’unicité sur l’UUID pour éviter d’importer plusieurs fois les mêmes données. L’importation complète avec -skipfailures (pour les erreurs d’unicité) est un peu bourrin, mais infaillible.

Côté tablette, j’ai développé un ensemble de scripts bash utilisés avec termux, termux-widget et termux-api pour

- Lister les projets existants
- Télécharger un nouveau projet
- Synchroniser un projet (réception des nouvelles données, et push des données + photos collectées). Au passage, on redimensionne les photos pour ne pas faire exploser le GIT et le serveur de stockage.
- Affichage de l’avancement dans une notification.

Grâce à un semblant d’UI minimaliste (termux-widget), j’arrive à faire utiliser cette solution par des techniciens qui n’auront pas à mettre le nez dans la console. Cerise sur le gâteau : je gagne beaucoup de temps pour le paramétrage de nouvelles tablettes (il suffit de télécharger/installer 3 APK puis copier/coller une commande d’installation). Et GIT a ce côté rassurant qu’on ne peut pas perdre de donnée et que la donnée est clonée sur différents terminaux.

## Restitution

Pour la restitution des données et leur vie après l’acquisition sur le terrain, j’utilise principalement Lizmap pour une vue WebSIG, et Airtable (base de donnée interactive) pour une approche plus “ticketing”. Parfois, les deux solutions peuvent être utilisées en parallèle.

![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled%2012.png)

![Untitled](Releve%CC%81%20terrain%20avec%20Qfield%2086dd76c070b2498ebc7cf27b5618ce66/Untitled%2013.png)
