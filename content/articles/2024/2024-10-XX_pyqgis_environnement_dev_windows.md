---
title: "Créer un environnement virtuel Python pour le développement de plugin QGIS avec VSCode sous Windows"
subtitle: Protégeons notre environnement, pour nos enfants PyQGIS
authors:
    - Nicolas Godet
categories:
    - article
comments: true
date: 2021-08-09
description: "Pour le bonheur d'Intellisense"
icon: material/microsoft-visual-studio-code
image:
license: beerware
robots: index, follow
tags:
    - Plugin QGIS
    - PyQGIS
    - Python
    - VS Code
    - Windows
---

# Créer un environnement virtuel Python pour le développement de plugin QGIS avec VSCode sous Windows

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

Tout ceux qui s'y sont frottés le savent, configurer son environnement PyQGIS et PyQt pour développer des plugins Python pour QGIS est un réel parcours du combattant. À la fin, on est souvent perdant...

Et bien, plus maintenant ! Après avoir fouillé les archives d'internet et exploré les pistes fournies par [Julien](../../team/julien-moura.md), voici l'une des méthodes permettant d'avoir toutes (ou presque) les autocomplétions d'objets et méthodes PyQGIS, PyQt, etc. dans VS Code.

## Création de l'environnement virtuel

Je suppose dans la suite que vous avez QGIS installé via l'installateur réseau OSGeo4W et que l'installation est localisée dans `C:\OSGeo4W`.

1. Ouvrir un console OSGeo Shell et naviguer jusqu'à l'emplacement où vous souhaitez créer l'environnement virtuel.  
   Par exemple, un template de plugin fraîchement créé via l'outil [QGIS Plugin Templater](https://gitlab.com/Oslandia/qgis/template-qgis-plugin).

2. Exécuter les commandes suivantes :

    ```ps
    C:\OSGeo4W\bin\python-qgis.bat -m venv --system-site-packages .venv
    C:\OSGeo4W\bin\python-qgis.bat -c "import pathlib;import qgis;print(str((pathlib.Path(qgis.__file__)/'../..').resolve()))" > .venv\qgis.pth
    ```

    L'option `--system-site-packages` permet à l'environnement virtuel créé d'hériter des librairies spécifiques à l'environnement Python dans QGIS.

3. Pour que VSCode reconnaisse les imports `processing`, ajouter la ligne suivante dans le fichier _.venv\qgis.pth_ :  
    `C:\OSGeo4W\apps\qgis\python\plugins`

    Votre fichier devrait ressembler à ça :

    ```text
    C:\OSGeo4W\apps\qgis\python
    C:\OSGeo4W\apps\qgis\python\plugins
    ```

    Veiller à ce que l'encodage du fichier _.venv\qgis.pth_ soit bien en UTF-8.

4. Créer le fichier _sitecustomize.py_ dans le dossier _.venv\Lib\site-packages_ avec le contenu suivant :

    ```python title="venv\Lib\site-packages\sitecustomize.py"
    import os

    os.add_dll_directory("C:/OSGeo4W/bin")
    os.add_dll_directory("C:/OSGeo4W/apps/qgis/bin")
    os.add_dll_directory("C:/OSGeo4W/apps/Qt5/bin")
    ```

5. Dans le fichier _.venv\pyvenv.cfg_, modifier les occurences _C:\OSGeo4W\bin_ en _C:\OSGeo4W\apps\Python312_ :

    ```ini
    home = C:\OSGeo4W\apps\Python312
    include-system-site-packages = true
    version = 3.12.6
    executable = C:\OSGeo4W\apps\Python312\python.exe
    command = C:\OSGeo4W\apps\Python312\python.exe -m venv --system-site-packages <Le chemin complet vers votre venv>
    ```

## Dans VSCode

Si vous ouvrez VSCode dans le dossier où vous venez de créer l'environnement virtuel, VSCode détectera automatique l'environnement (sinon installer l'extension VSCode Python) et lorsque vous taperez des bouts de code, VSCode vous proposera les objets ou méthodes PyQGIS.

![Complétion des imports](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/pyqgis_environnement_dev_windows/vscode.webp){: .img-center loading=lazy }

![Complétion des méthodes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/pyqgis_environnement_dev_windows/vscode2.webp){: .img-center loading=lazy }

Pour également avoir l'ensemble des complétions associées à PyQt, il semble être nécessaire d'installer une librairie Python supplémentaire `PyQt5-stubs` (certes qui n'est plus maintenue mais qui a le mérite de fonctionner).  
Dans le terminal VSCode, exécuter la commande `pip install PyQt5-stubs`.

![PyQt](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/pyqgis_environnement_dev_windows/vscode_pyqt.webp){: .img-center loading=lazy }

Tout ça pour avoir un code coloré :smiley: !

![Contribuez GeoPF Altimétrie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/pyqgis_environnement_dev_windows/vscode_geopf.webp){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
