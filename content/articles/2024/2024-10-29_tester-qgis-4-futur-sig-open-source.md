---
title: Testez QGIS 4
subtitle: Une histoire de dépendance
authors:
    - Julien MOURA
categories:
    - article
comments: true
date: 2024-11-09
description: Essayez QGIS 4 en avant-première ! Comme tout logiciel, open source ou propriétaire, QGIS repose sur d'autres logiciels ou biblioth, es dépendances et principalement Qt.
icon: material/crystal-ball
image: "Image d'illustration de l'article qui sert ensuite dans la mise en avant : réseaux sociaux, flux RSS... 400x800 en PNG"
license: default
robots: index, follow
tags:
    - OSGeo4W
    - PyQGIS
    - QGIS
    - Qt
    - vcpkg
---

# QGIS 4 : un QGIS basé sur Qt6

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## L'architecture de QGIS pour les nuls

![icône briques différentes](https://cdn.geotribu.fr/img/logos-icones/divers/briques_lego.webp){: .img-thumbnail-left }

Allez, on n'est pas là pour trop entrer dans les détails alros je vous ai fait un schéma simplifié de ce qui compose le logiciel QGIS. Oui, oui il est simplifié.

```mermaid
flowchart TD
    Q{QGIS} ====> |Dépend de| B(((Qt)))
    Q -->|Dépend de| C(API géospatiales)
    Q <--->|Optionnellement| P[Python]
    M(plugins) -->|Dépendent de| P:::pointilles
    B:::blocimportant --> S{"Interface graphique et système exploitation<br/>(et donc toutes les API système)"}
    C -->|dépend de| E[GEOS]
    C -->|dépend de| T[/Autres trucs moins connus\]
    Q --> T
    C -->|dépend de| D[/GDAL\]
    D -->|dépend de| E
    D -->|dépend de| G
    D -->|dépend de| F
    D -->|dépend de| Z@{ shape: docs, label: "Environ 73% des <br/>bibliothèques de drivers <br/>de formats de données <br/>géo-quelque-chose"}
    C -->|dépend de| F[PROJ]
    C -->|dépend de| G@{ shape: cyl, label: "Clients BDD<br/>liboci, libpq, <br/>libspatialite..." }

    classDef blocimportant fill:#ff0000,font-weight:bold
    classDef pointilles fill:stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
```

Vous avez remarqué le rond rouge au milieu ? Eh bien c'est le [cadriciel (_framework_) Qt](https://www.qt.io/) (prononcez "kuté" ou comme "_cute_" qui signifie mignon en anglais) retenu par le projet QGIS pour s'interfacer avec les API graphiques et techniques des différents systèmes d'exploitation.

Actuellement, c'est la version 5 de Qt qui est utilisée dans QGIS 3. Il se trouve qu'elle est arrivée en fin de vie en... mai 2025 selon [la documentation officielle](https://doc.qt.io/qt-6/supported-platforms.html#supported-qt-versions). La dernière fois que QGIS a changé de version majeure de Qt, QGIS est aussi passé à la version majeure supérieure (donc oui `QGIS 2 = Qt 4` et `QGIS 3 = Qt 5`)...

![Planning des versions de Qt](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qgis_4_qt6/qt_versions_planning.webp){: .img-center loading=lazy }

Dans cet article, je vous propose donc

----

## Installer QGIS basé sur Qt6

### Sur Windows

#### Niveau aventurier dominical : le package dév de l'OSGeo4W

![logo OSGeo4W](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/osgeo4w.webp){: .img-thumbnail-left }

On ne présente plus l'installateur "réseau" (_OSGeo4W Network Installer_ comme on dit sur les sites non traduits de projets internationaux) que nous avons mis en avant à plusieurs reprises [ici](../2020/2020-07-03_deploy_qgis_windows.md "Installer QGIS en ligne de commande avec OSGeo4W") et [là](../2021/2021-07-06_qgis_personnaliser_package_osgeo4w.md "Utiliser OSGeo4W pour déployer QGIS en entreprise").

Ce petit coquin d'inspiration linuxienne infiltré derrière les lignes windowsiennes pour permettre une installation de tout ~~et n'importe quoi ~~ ce qui a trait ~~aux projets OSGeo~~ à QGIS sur Windows avec une finesse de sélection des dépendances justement.

Allez c'est parti !

[Télécharger l'installateur OSGeo4W](https://download.osgeo.org/osgeo4w/v2/osgeo4w-setup.exe){: .md-button }
{: align=middle }

Lancer en mode administrateur puis suivre les étapes :

1. _Advanced Install_
1. Choisir _Install from Internet_
1. _All Users_
1. Choisir un dossier convenable pour l'installation car on n'est pas des bêtes quand même. Par exemple, soyons civilisés et mettons cela dans `%PROGRAMFILES%/QGIS/OSGeo4W`
1. Tant pis pour l'avertissement. Si en 2024 on doit encore s'embêter avec des espaces dans les chemins de fichiers, surtout pour un emplacement système variabilisé, c'est que le problème n'est pas du côté de l'utilisateur final. Ignorons et continuons donc.
1. Laissons les valeurs par défaut
1. Dans le champ Search, taper `qt6-dev-full`
1. Dérouler `Desktop`
1. Cliquer sur `Skip` en regard de `qgis-qt6-dev-full` jusqu'à obtenir un numéro de version (probablement impair et supérieur d'un chiffre à la version courante.)
1. suivant, suivant
1. cocher les licences (ERDAS, MrSID, ORacle, SZIP...). Notez qu'il est aussi possible de les imprimer de façon à les étudier en détail.
1. :coffee:
1. Il y aura peut-être des erreurs mais qu'importe, vous êtes arrivés jusqu'ici car vous vouliez un goût d'aventure dans la bouche ? Il n'est plus temps de reculer pour si peu.

En images :

![QGIS - OSGeo4W Qt6 - Capture d'écran du menu À propos](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qgis_4_qt6/QGIS_Qt6_OSGeo4W_about.webp){: .img-center loading=lazy }

#### Niveau aventurier/ère de l'Arche Perdue : l'autoporteur de vcpkg

![logo vcpkg](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/vcpkg.webp){: .img-thumbnail-left }

[OPENGIS.ch](https://www.opengis.ch/fr/), en tête de pont sur le packaging Windows avec [vcpkg](https://vcpkg.io), diffusait un [lien de téléchargement](https://download.opengis.ch/qgis-qt6.zip) sur [leurs réseaux sociaux](https://fosstodon.org/@opengisch/112155006378447452) dès mars dernier. Depuis, l'entreprise Suisse à qui l'on doit QField a continué son travail autour d'une chaîne de compilation et packaging plus moderne et multi-plateforme dans le cadre de la [proposition communautaire d'évolution (QEP) n°292](https://github.com/qgis/QGIS-Enhancement-Proposals/issues/292) pour aboutir le mois dernier. Le [compte-rendu dans la liste de mail au PSC](https://lists.osgeo.org/pipermail/qgis-psc/2024-October/010340.html) donne une idée du travail accompli.

Depuis les choses ont bien avancé et QGIS est compilé/packagé avec Qt6 à chaque modification du code source (_commit_) sur GitHub.

[:simple-githubactions: Aller télécharger un exécutable depuis GitHub](https://github.com/qgis/QGIS/actions/workflows/windows-qt6.yml?query=is%3Asuccess){: .md-button }
{: align=middle }

Notez qu'il est possible de filtrer sur une branche en particulier. Par exemple, pour n'afficher que [les jobs Windows Qt6 pour QGIS 3.40 ayant réussi](https://github.com/qgis/QGIS/actions/workflows/windows-qt6.yml?query=is%3Asuccess+branch%3Arelease-3_40).

!!! note "Dans l'ombre de la DSI"
    Notez que cette version téléchargeable et autoporteuse est idéale pour les environnements où les droits d'installation sont limités.
    Si on vous demande d'où ça sort, dites que vous avez lu ça sur [arcOrama](https://www.arcorama.fr/) :zipper_mouth:.

Une fois le téléchargement terminé :

1. on dézippe
1. on va dans le dossier `bin`
1. et on lance le fichier `qgis.exe` (pensez à activer l'affichage des extensions de fichiers sur Windows, la vie est plus belle).

    ![Lancer QGIS Qt6 OPENGIS.CH](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qgis_4_qt6/OPENGIS-CH_binaire_QGIS.webp){: .img-center loading=lazy }

Si tout se passe bien, on admire le [splash screen](../2021/2021-06-11_qgis_personnaliser_splash_screen.md "Personnaliser l'image au lancement de QGIS") personnalisé pour l'occasion :

![QGIS - Splashscreen Qt6 by OPENGIS.ch](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qgis_4_qt6/qgis_Qt6_OPENGIS-CH_splashscreen.webp){: .img-center loading=lazy }

----

### Sur Linux

Comment vous dire... c'est moins fluide, c'est plus... Linux quoi !
Donc attachez vos ceintures de lignes de commande, préparez vos merguez électroniques, ça va basher et faire chauffer vos CPU et barrettes de ~~sh~~RAM ! Téléguidé par la bonne fée Cabieces, je vous livre une recette pour Debian/Ubuntu. Je passe les détails car on n'est pas ici sur [le guide pour développeurs barbus](https://github.com/qgis/QGIS/blob/master/INSTALL.md).

#### Prérequis

- make et build essentials
- Git
- 8 Go de RAM mais 12 c'est bien, 16 très bien et 32 c'est mieux
- 6,5 Go d'espace disque. Notez qu'avec un SSD, tu gagnes un bonnus de vitesse.

Globalement, ça doit se régler avec un :

```sh
sudo apt install cmake build-essentials git
```

#### Lancer le jeu de construction

Sur un malentendu, la suite de commandes pourrait bien marcher du premier coup :

```sh title="Builder QGIS avec Qt6 à partir d'une branche"
mkdir -p ~/Git/
cd ~/Git
git clone https://github.com/qgis/QGIS.git -b release-3_38 --single-branch --depth 1
cd QGIS
CXX=clang++-14 && CC=clang-14 && cmakeQGIS -DWITH_QTWEBKIT=FALSE -DWITH_SERVER=FALSE -DBUILD_WITH_QT6=ON -DCMAKE_PREFIX_PATH="$DEPENDS_DIR/qwt/install" -DCMAKE_INSTALL_PREFIX=/usr/local/bin/qgis-build/
```

----

### Sur MacOS

!!! warning ""
    Compte-tenu des coûts associés pour l'obtention d'un [MacBook Pro M3 Max](https://www.apple.com/fr/shop/buy-mac/macbook-pro/14-pouces-m4-pro), forcément indispensable pour ce tutoriel, cette section est réservée aux [abonnés premium de Geotribu](../../about/sponsoring.md). :face_with_hand_over_mouth:

----

## Quoi de neuf dans QGIS Qt 6 ?

Allez, on lance, on prend le temps d'essayer de reconnaître des têtes connues sur le splash screen de dév

et hop !

Alors, qu'est-ce que ça change ?

- le thème de l'interface s'aligne automatiquement sur les paramètres du système (sombre ou clair)
- on peut choisir des couleurs en CMJN et qu'elles soient conservées dans les PDF générés par QGIS, ainsi que le profil d'impression
- peu de plugins sont compatibles et on ne peut pas filtrer dessus donc c'est assez compliqué de savoir lequel on peut installer
- on peut voter sur un plugin directement depuis l'interface
- on a une sensation de vitesse à l'utilisation mais c'est peut-être lié au fait qu'il n'y a aucun plugin d'installé
- il y a parfois des messages d'erreur mais c'est bon pour le karma d'aventurier
- sur Linux, le système d'affichage Wayland est désormais pleinement supporté

![QGIS - ColorPicker CMJN](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qgis_4_qt6/QGIS_Qt6_CMJN.webp){: width=20% loading=lazy } ![QGIS - Plugin incompatible avec Qt 6](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/qgis_4_qt6/QGIS_Qt6_installation_plugins_LMFP.webp){: width=20% loading=lazy }

### Je maintiens un plugin, comment faire pour qu'il soit compatible ?

![logo PyQGIS](https://cdn.geotribu.fr/img/logos-icones/programmation/pyqgis.png){: .img-thumbnail-left }

Si votre plugin n'utilise pas ou peu Qt ou vous avez suivi de bonnes pratiques de développement pour votre plugin, notamment l'import de tout ce qui est PyQt via PyQGIS et non directement, il n'y aura pas grand chose à faire. Sinon, il faut prévoir un travail de migration et de tests. Plus tôt vous commencez, mieux ce sera.

Une procédure de migration a été ajoutée il y a quelques semaines dans le ~~cookbook PyQGIS~~ [wiki du projet GitHub de QGIS](https://github.com/qgis/QGIS/wiki/Plugin-migration-to-be-compatible-with-Qt5-and-Qt6/) pour documenter l'usage d'un script de migration et rendre un plugin compatible à la fois avec QGIS Qt5 and Qt6 :

1. Dans votre environnement Python de développement :

  ```sh
  pip install astpretty tokenize-rt
  ```

1. Si vous êtes sur Linux, il faut installer des dépendances supplémentaires :

    ```sh
    sudo apt install python3-pyqt6 python3-pyqt6.qtsvg python3-pyqt6.qsci
    ```

1. Télécharger le [script sur le projet QGIS sur GitHub](https://github.com/qgis/QGIS/blob/master/scripts/pyqt5_to_pyqt6/pyqt5_to_pyqt6.py)
1. L'exécuter en pointant sur le dossier de votre plugin :

    ```sh
    python pyqt5_to_pyqt6.py /path/to/plugin
    ```

1. Tester votre plugin sur une installation de QGIS avec Qt5 **et** sur une installation de QGIS avec Qt6 en faisant les adaptations nécessaires.
1. Éditer le fichier `metadata.txt` et ajouter la ligne :

    ```ini title="metadata.txt d'un plugin explicitement compatible avec Qt6"
    [...]
    supportsQt6=True
    [...]
    ```

Il y a forcément quelques limites au script, notamment :

- la gestion des imports : il recommande souvent d'importer Qt depuis PyQGIS (`from qgis.PyQt.QtCore import Qt`) mais c'est rarement pertinent. Ceci dit, si vous utilisez des outils classiques de contrôle statique du code (flake8, ruff, isort, etc.), ils se chargeront de nettoyer le superflu.
- il ne gère pas bien les imports de PyQt qui sont hors du scope de PyQGIS. Par exemple, si vous utilisez `QtMultimedia` il va forcer l'import via `qgis.PyQt` alors que ce module là de PyQy n'y est pas référencé.

La documentation sur cette migration est inextistante ou très difficile à trouver. Quand on m'a répondu "la seule documentation, à ce jour, hormis le wiki d'Étienne, c'était [la description de la PR de Nyall](https://github.com/qgis/QGIS/pull/55912)", je me suis dit qu'on est proche du délit d'initiés :grin: ! Mais cela n'a finalement rien d'étonnant pour l'instant car cela ne concerne encore que les développeurs actuellement autour duquel gravite l'écosystème QGIS.

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
