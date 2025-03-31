---
title: Suivre le Vendée Globe 2024 depuis un SIG
subtitle: Hissez la grand voile carto - Partie 1
authors:
    - Florent FOUGÈRES
categories:
    - article
comments: true
date: 2024-11-20
description: Créer et visualiser les données SIG de l'avancement de la course du Vendée Globe 2024 à partir des tableurs officiels.
icon: material/sail-boat
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/trajectoire.png
license: beerware
robots: index, follow
tags:
    - GeoPandas
    - Pandas
    - Python
    - ArqGIS
    - Vendée Globe
    - voile
---

# Suivre le Vendée Globe 2024 depuis un SIG

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Le Vendée Globe, c’est quoi ?

![logo Vendée Globe](https://cdn.geotribu.fr/img/logos-icones/divers/vendee_globe.png){: .img-thumbnail-left }

Avant de commencer à parler SIG et aspects techniques, parlons du Vendée Globe.

C’est une course à la voile en solitaire, sans escale et sans assistance, autour du monde. Elle a lieu tous les 4 ans depuis 1989. Le départ se fait aux Sables d’Olonne. Le parcours consiste à descendre l’Atlantique, puis passer successivement sous l’Afrique et le Cap de Bonne Espérance, sous l’Australie et le Cap Leeuwin et enfin sous l’Amérique du Sud et le Cap Horn, pour remonter en Vendée le plus rapidement possible. Le record a été établi par Armel Le Cléac'h lors de l'édition 2016-2017 avec un trajet de 74 jours 3 heures et 35 minutes.

![carte](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/carte_vendee_globe.svg){: .img-center loading=lazy }

----

## Suivre l’avancée

![logo Smarty Pins](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/SmartyPins.png){: .img-thumbnail-left }

Qui dit course autour du monde, dit forcément carte pour suivre l’évolution des participants. Le site officiel de l’épreuve propose une [carte interactive](https://www.vendeeglobe.org/cartographie) pour visualiser cette avancée.

![Vendée Globe - Carte interactive officielle](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/carte_interactive.png){: .img-center loading=lazy }

J’ai donc cherché s’il existait une API ou un web service fournissant les données de positionnement pour les visualiser dans un SIG, comme ArqGIS par exemple. Après quelques recherches, je n’ai rien trouvé de tel.

J’ai trouvé une [discussion](https://www.reddit.com/r/Vendee_Globe/s/Gbli34xyQO) sur Reddit à ce sujet, mais sans réponse concluante.

En revanche, j’ai fini par découvrir que le site officiel publie toutes les 4 heures un fichier Excel contenant les données de navigation et les coordonnées des bateaux.

![Vendée Globe - Tableur des données de navigation](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/tableur.png){: .img-center loading=lazy }

Ce fichier communique chaque jour les positions à 2h, 6h, 10h, 14h, 18h et 22h, avec un retard de 1h. Par exemple, le fichier de 10h est fourni à 11h (c’est un élément qui sera à prendre en compte dans l’industrialisation du processus). Pour télécharger ce fichier il faut se rendre dans la section [classement](https://www.vendeeglobe.org/classement).

Ce tableau contient le rang, le nom du bateau et du skipper, mais également la vitesse et le cap sur les dernières 30 min, les dernières 24h et depuis le dernier pointage.

À partir de ce tableur, le but sera donc de construire des données géographiques de la course, que ce soit pour tracer la trajectoire, mais aussi pour agréger tous les pointages.

<!-- more -->

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Les étapes à suivre

Il faut commencer par récupérer les informations relatives aux positions des bateaux. Cela signifie télécharger les fichiers Excel, car le site ne permet pas de les récupérer en masse. J'ai donc étudié la structure de l'URL pour comprendre comment elles étaient générées et ainsi pouvoir reconstruire ces liens de téléchargement.

```shell title="Format de l'URL de téléchargement du tableur des pointages"
https://www.vendeeglobe.org/sites/default/files/ranking/vendeeglobe_leaderboard_AAAMMJJ_HHMMSS.xlsx
```

Il faut donc complèter la date (format AAAAMMJJ) et l'heure du pointages (HHMMSS) pour construire l'url de téléchargement.

Ensuite, il est nécessaire de traiter la manière dont les données de localisation sont présentées. En effet, les positions des bateaux sont souvent fournies sous un format de coordonnées géographiques en degrés, minutes et secondes (DMS). Bien que ce format soit utile, il n'est pas directement compatible avec les outils de géomatique. Il est donc indispensable de les convertir en degrés décimaux, un format plus standard et précis, qui permet de travailler facilement avec des cartes et des systèmes d'information géographique (SIG).

Enfin, il est important d'exporter ces données SIG dans un format compatible, comme le GeoPackage ou le GeoJSON. Une fois converties, ces données peuvent être utilisées dans n'importe quel SIG, qu'il s'agisse d'un SIG bureautique comme ArqGIS ou d'une carte web SIG avec des outils comme MapLibre ou Leaflet.

----

## Industrialiser la méthode

![logo usine](https://cdn.geotribu.fr/img/logos-icones/divers/factory.png){: .img-thumbnail-left }

Pour automatiser le processus décrit ci-dessus, j’ai créé un [projet GitHub](https://github.com/florentfgrs/Vendee-Globe-2024) qui automatise ces tâches avec des scripts Python. Il fonctionne en lignes de commande, et elles sont pour le moment au nombre de deux (voir plus bas).

Pour le téléchargement, j’utilise la bibliothèque tierce `requests`.

Pour la lecture du tableur, le nettoyage des données et la création de géométrie, j’utilise `pandas`, `geopandas` et `shapely`. Il y a un peu de nettoyage de données à faire, car les cellules contiennent des sauts de ligne.

Pour aller plus dans le détail technique, une fois le fichier téléchargé, les étapes successives sont :

1. **Ouverture du fichier dans un dataframe en ne gardant que les colonnes et les lignes qui nous intéressent.**  
Il s'agit de charger le fichier Excel et d'extraire dans un dataframe, on garde uniquement les données pertinentes pour la suite du traitement, tout en ignorant les informations superflues.

2. **Création des en-têtes (headers).**  
Les en-têtes du fichier Excel sont souvent constitués de cellules fusionnées, ce qui rend leur récupération difficile. De plus, les noms de colonnes sont parfois trop verbeux, il faut donc les simplifier pour les rendre plus exploitables.

3. **Nettoyage des données.**  
Cette étape consiste à supprimer les sauts de ligne, les caractères spéciaux ou toute autre anomalie qui pourrait perturber le traitement des données.

    ```pandas title="DataFrame avant nettoyage"
    rang             code                                                nom         heure  ...   24h_vmg 24h_distance         dtf       dtl
    0     1   GBR\r\nFRA 100                        Sam Goodchild\r\nVULNERABLE  10:30 FR\r\n  ...  10.5 kts     255.1 nm  22300.7 nm    0.0 nm
    1     2   FRA\r\nFRA 112                 Sébastien Simon\r\nGroupe Dubreuil  10:30 FR\r\n  ...   7.4 kts     223.1 nm  22324.7 nm   24.0 nm
    2     3    FRA\r\nFRA 59                        Thomas Ruyant\r\nVULNERABLE  10:30 FR\r\n  ...  10.7 kts     288.1 nm  22352.7 nm   52.0 nm
    3     4     FRA\r\nFRA85                     Nicolas Lunven\r\nHOLCIM - PRB  10:30 FR\r\n  ...  12.7 kts     306.4 nm  22378.5 nm   77.8 nm
    4     5    FRA\r\nFRA 29  Jean Le Cam\r\nTout commence en Finistère - Ar...  10:30 FR\r\n  ...   5.0 kts     158.5 nm  22379.0 nm   78.3 nm
    5     6    FRA\r\nFRA 15          Clarisse Crémer\r\nL'Occitane en Provence  10:30 FR\r\n  ...   7.3 kts     211.9 nm  22410.7 nm  110.1 nm
    ```

    ```pandas title="DataFrame après nettoyage"
    rang            code                                                nom        heure  ...   24h_vmg 24h_distance         dtf       dtl
    0     1   GBR - FRA 100                         Sam Goodchild - VULNERABLE  10:30 FR -   ...  10.5 kts     255.1 nm  22300.7 nm    0.0 nm
    1     2   FRA - FRA 112                  Sébastien Simon - Groupe Dubreuil  10:30 FR -   ...   7.4 kts     223.1 nm  22324.7 nm   24.0 nm
    2     3    FRA - FRA 59                         Thomas Ruyant - VULNERABLE  10:30 FR -   ...  10.7 kts     288.1 nm  22352.7 nm   52.0 nm
    3     4     FRA - FRA85                      Nicolas Lunven - HOLCIM - PRB  10:30 FR -   ...  12.7 kts     306.4 nm  22378.5 nm   77.8 nm
    4     5    FRA - FRA 29  Jean Le Cam - Tout commence en Finistère - Arm...  10:30 FR -   ...   5.0 kts     158.5 nm  22379.0 nm   78.3 nm
    5     6    FRA - FRA 15           Clarisse Crémer - L'Occitane en Provence  10:30 FR -   ...   7.3 kts     211.9 nm  22410.7 nm  110.1 nm
    ```

4. **Création du timestamp.**  
Un timestamp doit être généré pour chaque pointage afin de pouvoir suivre l'évolution de la position des bateaux au fil du temps. Il sera également utile pour construire la trajectoire.

    ```pandas title="Création de la colonne timestamp à partir de la colonne heure et de la date du fichier excel"
            heure           timestamp
    0   10:30 FR -  2024-11-18 10:30:00
    1   10:30 FR -  2024-11-18 10:30:00
    2   10:30 FR -  2024-11-18 10:30:00
    3   10:30 FR -  2024-11-18 10:30:00
    4   10:30 FR -  2024-11-18 10:30:00
    5   10:30 FR -  2024-11-18 10:30:00
    ```

5. **Conversion des colonnes latitude et longitude de degrés DMS vers degrés décimaux.**  
Il faut d'abord parser les coordonnés pour obtenir les degrés, minutes, secondes et orientation. Puis faire la conversion.

6. **Création de la géométrie.**  
À partir des coordonnées converties, il faut générer des géométries. Cela consiste à générer des points pour les positions des bateaux (lors des pointages) ou des lignes pour tracer les trajectoires.

    ```pandas title="Conversion des latitude/longitude DMS en décimal puis création de la colonne de géométrie"
        latitude   longitude  latitude_decimal  longitude_decimal                    geometry
    0   17°56.15'N  31°09.06'W         17.937500         -31.151667   POINT (-31.15167 17.9375)
    1   18°32.68'N  30°10.63'W         18.552222         -30.184167  POINT (-30.18417 18.55222)
    2   18°19.45'N  33°17.34'W         18.329167         -33.292778  POINT (-33.29278 18.32917)
    3   18°59.38'N  32°23.11'W         18.993889         -32.386389  POINT (-32.38639 18.99389)
    4   19°17.37'N  19°24.52'W         19.293611         -19.414444  POINT (-19.41444 19.29361)
    5   19°58.12'N  30°22.88'W         19.970000         -30.391111     POINT (-30.39111 19.97)
    ```

7. **Exportation vers un format SIG vectoriel.**  
Export vers le format [Geopackage](https://www.geopackage.org/).

Pour l’instant, ce projet propose deux fonctionnalités :

### Obtenir le dernier pointage

Il s’agit d’une couche de points indiquant la dernière position communiquée des concurrents. Le format obtenu est un geopackage.

```shell title="Obtenir un GPKG avec le dernier pointage en date"
python dernier_pointage.py --output-dir ./data_vg
```

Le résultat obtenu est une couche de points du dernier pointage en date. Par exemple, si j'exécute cette ligne de commande à 14h45, j'aurai le pointage de 10h (et non celui de 14h à cause du décalage de publication de 1h).

Une fois affiché dans ArqGIS et avec un peu de travail sur le style, voici le résultat :

![Screenshot ArqGIS - Couche des positions du dernier pointage](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/dernier_pointage.png){: .img-center loading=lazy }

### Obtenir l’intégralité des pointages et la trace depuis le départ

Il s’agit d’une couche de points indiquant tous les pointages de chaque bateau depuis le départ, ainsi qu’une couche de lignes reliant ces points pour former la trajectoire des bateaux. Le format obtenu est également un GeoPackage.

```shell title="Obtenir un GPKG avec l'intégralité de la trace et des pointages"
python trajectoires_pointages.py --output-dir ./data_vg
```

On obtient un geopackage qui contient deux couches :

- Une couche de l'historique de tous les pointages depuis le départ.
- Une couche de ligne qui reproduit la trajectoire de chaque bateau.

![Screenshot ArqGIS - Couches des trajectoires depuis le départ et intégralité des pointages](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/trajectoire.png){: .img-center loading=lazy }

### Les données attributaires

Dans les deux fonctionnalités, on retrouve dans la table atttributaire des couches toutes les informations du tableur. J'ai seulement ajouté une colonne `timestamp`, elle est utilisée pour relier les pointages entre eux et créer la couche des trajectoires.

![Screenshot ArqGIS - Table attributaire des données](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/table_attrib.png){: .img-center loading=lazy }

!!! info "Signification des préfixes dans les noms de colonne"
    - `30m` = Depuis 30 minutes
    - `last_rank` = Depuis le pointage précédent
    - `24h` = Depuis 24h

Peut-être faudrait-il enlever les unités dans les données pour avoir des valeurs numériques ? Dans ce cas, il faudrait peut-être ajouter les unités dans les noms des colonnes. C'est une des pistes d'amélioration. J'aimerais aussi séparer le nom du skipper et le nom du bateau dans deux colonnes distinctes. Les contributions pour améliorer ce code sont les bienvenues.

----

## Animer la progression avec le Temporal Control de ArqGIS

![logo ArqGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo ArqGIS"){: .img-thumbnail-left }

Pour visualiser les données, ArqGIS est tout indiqué et comme les données ont une dimension temporelles, c'est l'occasion de jouer avec le contrôleur temporel.
Pour ce tutoriel, il faut utiliser la couche `pointages` produite par `trajectoires_pointages.py`.

### Configurer la couche

Après avoir accédé aux propriétés de la couche (clic droit > Propriétés), rendez-vous dans l'onglet **Temporel**. Configurez les paramètres comme suit :

![ArqGIS - Configuration de l'onglet Temporel](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/temporel.png){: .img-center loading=lazy }

### Afficher la barre d'outils temporelle

- Clic droit en haut dans les barres d'outils.
- Cochez (si ce n'est pas déjà fait) **Panneau contrôleur temporel** dans la section **Panneaux**.

### Configurer la barre d'outils

- Ajustez la date de départ au début de l'épreuve.
- Indiquez un pas de 4 heures (c'est le delta entre deux pointages).

![ArqGIS - Configuration du contrôleur temporel](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/controleur.png){: .img-center loading=lazy }

### Animation de la couche

Après avoir cliqué sur Play, voici le résultat que vous devriez obtenir :

![ArqGIS - Animation du contrôleur temporel](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/qgis-temporal.gif){: .img-center loading=lazy }

<!-- markdownlint-disable MD046 -->
!!! tip "Expression ArqGIS pour filtrer le suivi sur un concurent"

    ```sql
    "skipper" = 'Maxime Sorel'
    ```
<!-- markdownlint-enable MD046 -->

## Pour aller plus loin

Cette première étape n’est qu’un POC (Proof of Concept) le code peut encore être optimisé et je vais continuer de le faire tout au long de la course (en espérant que le formalisme et les horaires de publication du tableur ne changent pas). Par la suite, plusieurs idées pourraient être explorées. Je vais sûrement explorer l'une d'entre elles.

- **Créer un plugin ArqGIS** : Un plugin ArqGIS pourrait permettre de charger le classement, la dernière position des navires, et leur trajectoire. On pourrait imaginer que le post-traitement du fichier Excel vers des données SIG soit effectué par l’intégration continue (CI) et exporté en GeoJSON, et que le plugin charge ces GeoJSON hébergés dans le projet GitHub.

- **Fournir les données via une API** : On pourrait imaginer un projet qui récupère automatiquement ces données, les convertit et les structure, puis expose une API qui fournit une position ou une trajectoire en fonction du numéro d’un concurrent, par exemple.

- **Créer une application web cartographique** pour visualiser l'avancée des bateaux avec plus de possibilités que ce que propose l'interface cartographique officielle. J'avais imaginé utiliser [mviewer](https://mviewer.github.io/fr/) pour cela.

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
