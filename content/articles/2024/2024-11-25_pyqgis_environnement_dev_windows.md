---
title: "Créer un environnement virtuel Python pour le développement de plugin QGIS avec VS Code sous Windows"
subtitle: Protégeons notre environnement, pour nos enfants PyQGIS
authors:
    - Nicolas Godet
    - Julien MOURA
categories:
    - article
comments: true
date: 2024-11-25
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

# Créer un environnement virtuel Python pour le développement de plugin QGIS avec VS Code sous Windows

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

![logo PyQGIS](https://cdn.geotribu.fr/img/logos-icones/programmation/pyqgis.png){: .img-thumbnail-left }

Tout ceux qui s'y sont frottés le savent, configurer son environnement Python, PyQGIS et PyQt sous Windows pour développer des plugins pour QGIS est un réel parcours du combattant. À la fin, on est souvent perdant...

Et bien, plus maintenant ! Après avoir fouillé les archives d'internet et exploré les pistes fournies par [Julien](../../team/julien-moura.md), voici l'une des méthodes permettant d'avoir toutes (ou presque) les autocomplétions d'objets et méthodes PyQGIS, PyQt, etc. dans VS Code.

<!-- more -->

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Création de l'environnement virtuel

Je suppose dans la suite que vous avez installé QGIS dans le répertoire `C:\OSGeo4W` (la procédure est identique que QGIS soit installé via l'installateur réseau OSGeo4W ou via le package MSI, les chemins indiqués dans la suite de l'article sont simplement à adapter selon votre installation).

1. Ouvrir une console OSGeo4W Shell et naviguer jusqu'à l'emplacement où vous souhaitez créer l'environnement virtuel.  
   Par exemple, un template de plugin fraîchement créé via l'outil [QGIS Plugin Templater](https://gitlab.com/Oslandia/qgis/template-qgis-plugin).

1. Exécuter les commandes suivantes :

    ```cmd title="Création d'un environnement virtuel dans l'OSGeo4W Shell"
    C:\OSGeo4W\bin\python-qgis.bat -m venv --system-site-packages .venv
    C:\OSGeo4W\bin\python-qgis.bat -c "import pathlib;import qgis;print(str((pathlib.Path(qgis.__file__)/'../..').resolve()))" > .venv\qgis.pth
    ```

    L'option `--system-site-packages` permet à l'environnement virtuel créé d'hériter des librairies spécifiques à l'environnement Python dans QGIS.

1. Pour que VSCode reconnaisse les imports `processing`, ajouter la ligne suivante dans le fichier `.venv\qgis.pth` :  
    `C:\OSGeo4W\apps\qgis\python\plugins`

    Votre fichier devrait ressembler à ça :

    ```text title="Contenu du fichier .venv\qgis.pth"
    C:\OSGeo4W\apps\qgis\python
    C:\OSGeo4W\apps\qgis\python\plugins
    ```

    Veiller à ce que l'encodage du fichier `.venv\qgis.pth` soit bien en UTF-8.

1. Créer le fichier `sitecustomize.py` dans le dossier `.venv\Lib\site-packages` avec le contenu suivant :

    ```python title=".venv\Lib\site-packages\sitecustomize.py"
    import os

    os.add_dll_directory("C:/OSGeo4W/bin")
    os.add_dll_directory("C:/OSGeo4W/apps/qgis/bin")
    os.add_dll_directory("C:/OSGeo4W/apps/Qt5/bin")
    ```

1. Dans le fichier `.venv\pyvenv.cfg`, modifier les occurences `C:\OSGeo4W\bin` en `C:\OSGeo4W\apps\Python312` :

    ```ini title=".venv\pyenv.cfg"
    home = C:\OSGeo4W\apps\Python312
    include-system-site-packages = true
    version = 3.12.6
    executable = C:\OSGeo4W\apps\Python312\python.exe
    command = C:\OSGeo4W\apps\Python312\python.exe -m venv --system-site-packages <Le chemin complet vers votre venv>
    ```

### Avec l'utilitaire _qgis-venv-creator_

> Paragraphe ajouté en janvier 2025

![logo Gispo](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/Gispo.webp){: .img-thumbnail-left }

Juste après que cet article soit publié, on découvrait [le projet create-qgis-venv](https://github.com/GispoCoding/qgis-venv-creator) de GispoCoding.

Il se présente comme un outil en ligne de commande (CLI) multi-plateforme. Il est recommandé de l'installer avec [pipx](https://pipx.pypa.io/stable/#on-windows) qui gère la plupart des paramètres un peu sioux et qui est compatible avec Windows. C'est désormais l'outil recommandé dans la communauté Python pour gérer les outils en ligne de commande (CLI), c'est donc une bonne occasion de s'y mettre. Une fois pipx installé, paramétré (`ensurepath`...) et une nouvelle session PowerShell lancée, l'installation se passe comme un charme :

```powershell title="Installation de qgis-venv-creator avec pipx"
pipx install qgis-venv-creator
```

![Installation de qgis-venv-creator avec pipx](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/pyqgis_environnement_dev_windows/powershell_pipx_qgis-venv-creator.webp){: .img-center loading=lazy }

L'outil qgis-venv-creator est désormais accessible depuis n'importe quelle session PowerShell avec la commande suivante :

```powershell title="Commande de base de qgis-venv-creator"
create-qgis-venv --venv-name ".venv"
```

L'outil a besoin d'identifier l'installation de QGIS à utiliser pour la génération de l'environnement de développement et cherche dans les emplacements par défaut (`C:\OSGeo4W` et `C:\PROGRAMFILES\QGIS X.y.z`). Mais si vous êtes quelqu'un de bien, soigneux et utilisez QGIS dans un monde professionnel, vous l'installez probablement dans un emplacement correct au regard de ce que recommande le système d'exploitation, `%PROGRAMFILES%/QGIS/X_y` par exemple. Il est possible de passer un _pattern_ pour lui indiquer où chercher :

```powershell title="qgis-venv-creator avec un chemin d'installation de QGIS personnalisé"
create-qgis-venv --qgis-installation-search-path-pattern "C:\Program Files\QGIS\*\apps\qgis*" --venv-name ".venv"
```

<iframe title="qgis-venv-creator demonstration" width="100%" height="400" src="https://video.osgeo.org/videos/embed/9b5806ca-d489-443f-8edc-d6be9b9a83c6" frameborder="0" allowfullscreen="" sandbox="allow-same-origin allow-scripts allow-popups allow-forms"></iframe>

Il suffit d'activer son environnement virtuel `.venv/Scripts/activate` et de continuer ce tutoriel !  
Merci Gispo !

----

## Dans VS Code

Si vous ouvrez VS Code dans le dossier où vous venez de créer l'environnement virtuel, VS Code détectera automatiquement l'environnement (sinon installer [l'extension VS Code Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)) et lorsque vous taperez des bouts de code, VS Code vous proposera les objets ou méthodes PyQGIS.

![Complétion des imports](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/pyqgis_environnement_dev_windows/vscode_intellisense_completion_imports.webp){: .img-center loading=lazy }

![Complétion des méthodes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/pyqgis_environnement_dev_windows/vscode_intellisense_completion_methodes.webp){: .img-center loading=lazy }

Pour également avoir l'ensemble des complétions associées à PyQt, il semble être nécessaire d'installer une librairie Python supplémentaire `PyQt5-stubs` (certes qui n'est plus maintenue mais qui a le mérite de fonctionner).  
Dans le terminal VS Code, exécuter la commande :

```powershell title="Installer la complétion PyQT dans l'environnement virtuel"
pip install PyQt5-stubs
```

![PyQt](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/pyqgis_environnement_dev_windows/vscode_pyqt.webp){: .img-center loading=lazy }

Tout ça pour avoir un code coloré :smiley: !

![Contribuez GeoPF Altimétrie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/pyqgis_environnement_dev_windows/vscode_geopf.webp){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
