---
title: Utiliser GDAL sous Windows avec WSL (Windows Subsystem for Linux)
authors:
    - Julien MOURA
categories:
    - article
    - tutoriel
comments: true
date: 2020-10-28
description: WSL ? Le Windows Subsystem for Linux permet depuis quelques années déjà de faire tourner un terminal bash sous Windows et ainsi bénéficier de l'usage des programmes populaires de l'écosystème Linux. Dans ce tutoriel, nous verrons comment installer et configurer WSL sur Windows 10, puis nous verrons les possibilités que cela ouvre en installant et utilisant GDAL dans le sous-système Linux.
image: https://cdn.geotribu.fr/img/tuto/gdal_wsl/ubuntu_wsl_landing_page.png
tags:
    - GDAL
    - OGR
    - Windows
    - WSL
---

# Utiliser GDAL sur Windows via le sous-système pour Linux

:calendar: Date de publication initiale : 28 octobre 2020

Pré-requis :

- un [Windows à jour](#version-minimale-de-windows)
- un compte avec les droits d'administrateur (au moins durant la phase d'installation)

## Introduction

![icône GDAL](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/gdal.png "logo GDAL"){: .img-thumbnail-left }

Récemment, j'ai eu à traiter des données particulièrement lourdes (millions d'objets) et imparfaites (mauvaises géométries dans un shapefiles) et mes outils habituels étaient tenus en échec : ArqGIS prend des plombes puis plante presque systématiquement lors des traitements de nettoyage et de restructuration, le GDAL sur mon ordinateur ou sur mon Google Colab sont cantonnés à la version 3.0.* liée au socle Ubuntu 18.04 alors que j'ai bien besoin des options de la branche 3.1 (`-nlt`, `-makevalid`...).

J'ai à ma disposition un ordinateur puissant sous Windows, mais l'accès à GDAL via l'[OSGeo4W](2020-07-03_deploy_qgis_windows.md) n'est pas idéal et complexe (cmd, proxy, politique de sécurité...), j'ai pas le coeur à [l'installer au niveau du système](../2013/2013-09-26_installer_python_gdal_sous_windows.md#installer-gdalogr) (effets de bord, conflits...) et utiliser conda revient à télécharger la moitié du Web (troll).

Alors pourquoi ne pas essayer de mettre à profit WSL que [j'utilise déjà pour le développement ou le test](https://twitter.com/geojulien/status/1139811447414775808) ?

![Architecture WSL 2](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl2_architecture.png "UArchitecture WSL 2"){: .img-center loading=lazy }

WSL ? Le Windows Subsystem for Linux (dont [le code du noyau est sous GPL-2](https://github.com/microsoft/WSL2-Linux-Kernel)) permet depuis quelques années déjà de faire tourner un terminal bash sous Windows et ainsi bénéficier de l'usage des programmes populaires de l'écosystème Linux. Dans ce tutoriel, nous verrons comment installer et configurer WSL sur Windows 10, puis nous verrons les possibilités que cela ouvre en installant et utilisant GDAL dans le sous-système Linux.

Deux étapes dans ce tutoriel :

- [installer et configurer le sous-système](#installer-wsl) Windows pour Linux
- [utiliser GDAL 3.1.* dans Ubuntu 20.04](#utiliser-gdal-dans-le-sous-systeme-linux-de-windows) sans quitter son terminal Windows, ni déployer une grosse VM ou autre

## Installer ou activer WSL

Même si [la documentation](https://docs.microsoft.com/fr-fr/windows/wsl/install-win10) est très bien faite et même traduite en français, il me semble intéressant de paraphraser la documentation, me permettant d'y apporter quelques précisions au passage.

### Vérifier les pré-requis

#### Version minimale de Windows

Il existe actuellement deux versions différentes du sous-système Windows pour Linux. La version 2 est une fonctionnalité très récente, il faut donc s'assurer que la version de Windows est bien dans les clous.

On ouvre son terminal Powershell :

```powershell
[System.Environment]::OSVersion.Version
```

On obtient un tableau :

```powershell
Major  Minor  Build  Revision
-----  -----  -----  --------
10     0      19044  0
```

Si le numéro du build est supérieur ou égal à `18362` (ou `19041` pour les socles ARM), c'est bon. Sinon, revenez après avoir fait vos mises à jour :wave:.

#### Un terminal moderne

Comme déjà évoqué dans [l'article sur l'environnement de travail Python sur Windows](2020-06-19_setup_python.md#utiliser-powershell), utiliser `cmd` n'est pas une option et il va falloir entrer quelques commandes Powershell pour ensuite profiter joyeusement de bash :partying_face:.

Avec WSL, les choses se compliquent car il devient nécessaire de pouvoir switcher d'un terminal à l'autre, par exemple d'un Powershell sur le Windows hôte vers le bash de l'une des distributions installées avec WSL. Le terminal intégré de Powershell en étant incapable, il nous faut donc installer le **nouveau terminal** :

- depuis [le Windows Store](https://aka.ms/terminal) - **méthode recommandée**
- avec winget : `winget install --id=Microsoft.WindowsTerminal -e`
- avec chocolatey : `choco install microsoft-windows-terminal`
- avec [le MSIX Bundle](https://github.com/microsoft/terminal/releases/download/v1.3.2651.0/Microsoft.WindowsTerminal_1.3.2651.0_8wekyb3d8bbwe.msixbundle) - mais attention, ça ne gère pas les futures mises à jour automatiques

??? danger "Regarder le spot de pub d'inspiration éro-automobile :underage:"
    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/8gw0rXPMMPE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    {: align=middle }

### Installer WSL

WSL faisant partie du bouquet de fonctionnalités avancées, il faut donc un accès administrateur pour l'activer (par la suite, ce sera ok pour un utilisateur de base) :

1. Activer WSL et la VM

    Si votre numéro de build >= 19041 :

    ```powershell
    wsl --install
    ```

    Sinon, à l'ancienne :

    ```powershell
    # activer la fonctionnalité
    dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
    # activer la machine virtuelle
    dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
    ```

2. Redémarrer l'ordinateur
3. [Télécharger](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi) et installer la version 2 du noyau WSL
4. Définir la version à utiliser : `wsl --set-default-version 2`

En cas de doute, se référer à [la documentation officielle](https://docs.microsoft.com/fr-fr/windows/wsl/install-win10) et/ou harceler votre DSI.

### Installer une ou plusieurs distributions

Une fois le sous-système prêt, il est temps d'installer une ou plusieurs distributions Linux parmi celles disponibles (voir [la liste ici](https://docs.microsoft.com/fr-fr/windows/wsl/install-win10#step-6---install-your-linux-distribution-of-choice)).

1. pour ce tutoriel, on a besoin de télécharger [Ubuntu 20.04](https://www.microsoft.com/store/apps/9n6svws3rx71)
2. au premier lancement, créer son utilisateur (voir [page dédiée de la doc](https://docs.microsoft.com/fr-fr/windows/wsl/user-support))
3. Mettre à jour les paquets avec un bon vieux `sudo apt update && sudo apt upgrade`
4. Fermer la fenêtre

Voilà, désormais nous avons notre distribution Ubuntu 20.04 prête à être utilisée dans notre Windows. Allez, on ne s'arrête pas en si bon chemin : on continue vers l'installation de GDAL !

----

## Utiliser GDAL dans le sous-système Linux de Windows

Une fois notre distribution installée, continuons nos opérations sur notre nouveau terminal.

Avant d'aller plus loin, quelques commandes à retenir, qui sont évidemment disponibles (et même traduites !) via l'argument `--help` :

![Onglets WSL dans Windows Terminal](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl_terminal_tabs.png "Titre image"){: .img-center loading=lazy }

### Lister les distributions installées

```powershell
wsl --list
```

Chez moi, cela donne :

```powershell
Distributions du sous-système Windows pour Linux :
Ubuntu-20.04 (par défaut)
docker-desktop
docker-desktop-data
Debian
Ubuntu-18.04
```

### Entrer/sortir dans une distribution

Cela se passe avec l'option `-d / --distribution` avec le nom de la distribution souhaitée. Dans notre cas :

```powershell
wsl -d Ubuntu-20.04
```

Pour en sortir, il suffit de taper `exit`.

### Installer GDAL sur notre Ubuntu 20.04

Nous voilà enfin dans notre environnement bash chéri :heart_eyes: !

Rien que du très classique, donc d'abord, on définit la version de GDAL que l'on souhaite. Dans mon cas, c'est donc :

```bash
export GDAL_VERSION=3.1.*
```

Ensuite, on ajoute le dépôt bien connu d'ubuntugis (privilégier le stable si la version dont vous avez besoin s'y trouve) :

```bash
sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable && sudo apt update
```

Puis, on installe GDAL :

```bash
sudo apt install gdal-bin=$GDAL_VERSION libgdal-dev=$GDAL_VERSION
export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal
```

Et enfin, on vérifie que tout va bien :

```bash
$ ogrinfo --version
GDAL 3.1.3, released 2020/09/01
```

### Lancer des commandes, des vraies

L'un des atouts de ce système est de pouvoir exécuter GDAL (ou tout autre commande propre à la distribution) à l'intérieur de la VM (Ubuntu) mais en pointant de façon transparente sur le système de fichiers hôte (Windows).

Par exemple, on peut directement lancer la commande précédente depuis Powershell :

```powershell
PS C:\Users\geojulien> wsl -d Ubuntu-20.04 -- ogrinfo --version
GDAL 3.1.3, released 2020/09/01
```

Pour aller plus loin, considérons un petit scénario d'exemple dans lequel on souhaite :

1. télécharger une donnée ouverte (au hasard : [les bassins de mobilité scolaire en Normandie](https://www.data.gouv.fr/fr/datasets/bassins-de-mobilite-scolaire-normandie/), version convertie à la volée),
2. vérifier rapidement son état avec [ogrinfo]
3. convertir en couche de GeoPackage (parce-que c'est la hype), en appliquant des contrôles géométriques

Et tout ça, en lançant les commandes depuis Powershell !

#### Télécharger la donnée avec wget

A l'instar des autres utilitaires intégrés de base dans Ubuntu, `wget` n'attend que d'être utilisé via WSL :

```powershell
# wget est accessible, pourquoi se priver ?
wsl -d Ubuntu-20.04 -- wget https://www.data.gouv.fr/fr/datasets/r/931cb357-33e6-46d6-8d2c-a17be9038e90 -O test_gdal_wsl.shp.zip
```

![capture wget wsl](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl_wget_from_datagouv.png "Une commande wget comme on les aime"){: .img-center loading=lazy }

Et voilà mon fichier dans mon explorateur Windows :

![capture wget wsl file explorer](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl_wget_result_explorer.png "Résultat du téléchargement avec wget dans Windows"){: .img-center loading=lazy }

#### Un petit ogrinfo des familles

On peut donc regarder de plus près notre fichier téléchargé avec un bon vieux [ogrinfo] :

```powershell
# ogrinfo
wsl -d Ubuntu-20.04 -- ogrinfo -al -so test_gdal_wsl.shp.zip
```

![capture wsl ogrinfo](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl_ogrinfo.png "ogrinfo dans Windows via WSL"){: .img-center loading=lazy }

#### Contribuons à la fin du règne du Shapefiles

Histoire de faire les choses jusqu'au bout, on veut alors lancer un traitement sur nos données :

- convertir le shapefiles en couche de geopackage
- s'assurer qu'il n'y ait qu'un seul type de géométrie et que les polygones soient valides
- supprimer les Z et M
- reprojeter en 3857 (web map en ligne de mire)

On lance donc [ogr2ogr] :

```powershell
wsl -d Ubuntu-20.04 -- ogr2ogr -t_srs EPSG:3857 -f GPKG "geotribu_gdal_wsl_gpkg.gpkg" "test_gdal_wsl.shp.zip" -nln "GDAL_Windows_SO_SIMPLE" -nlt POLYGON -dim 2 -overwrite -makevalid
```

Et on ouvre notre couche dans ArqGIS :

![capture qgis résultat ogr2ogr](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl_ogr2ogr_result_qgis.png "ogrinfo dans Windows via WSL"){: .img-center loading=lazy }

----

## Bonux stage

### Personnaliser le terminal

Dans le nouveau terminal, il est possible de [personnaliser chaque shell répertorié](https://docs.microsoft.com/fr-fr/windows/terminal/customize-settings/profile-settings) histoire de s'y retrouver facilement ou tout simplement de faire les choses à son goût.

??? example "Ma configuration (objet `profiles/list`)"
    <!-- markdownlint-disable MD046 -->
    ```jsonc
    {
    "list":
        [
            {
                // Make changes here to the powershell.exe profile.
                "guid": "{61c54bbd-c2c6-5271-96e7-009a87ff44bf}",
                "name": "Windows PowerShell",
                "commandline": "powershell.exe",
                "hidden": false
            },
            {
                // Make changes here to the cmd.exe profile.
                "guid": "{0caa0dad-35be-5f56-a8ff-afceeeaa6101}",
                "name": "Invite de commandes",
                "commandline": "cmd.exe",
                "hidden": false
            },
            {
                "guid": "{b453ae62-4e3d-5e58-b989-0a998ec441b8}",
                "hidden": true,
                "name": "Azure Cloud Shell",
                "source": "Windows.Terminal.Azure"
            },
            {
                "guid": "{58ad8b0c-3ef8-5f4d-bc6f-13e4c00f2530}",
                "hidden": false,
                "name": "Debian",
                "source": "Windows.Terminal.Wsl"
            },
            {
                "guid": "{c6eaf9f4-32a7-5fdc-b5cf-066e8a4b1e40}",
                "hidden": false,
                "name": "Ubuntu-18.04",
                "source": "Windows.Terminal.Wsl",
                // personnalisation
                "acrylicOpacity": 0.9,
                "antialiasingMode": "cleartype",
                "colorScheme": "Solarized Dark",
                "cursorColor": "#FFFFFD",
                "fontFace": "Cascadia Code PL",
                "suppressApplicationTitle": true,
                "useAcrylic": true  
            },
            {
                "guid": "{07b52e3e-de2c-5db4-bd2d-ba144ed6c273}",
                "hidden": false,
                "name": "Ubuntu-20.04",
                "source": "Windows.Terminal.Wsl",
                // personnalisation
                "acrylicOpacity": 0.9,
                "antialiasingMode": "cleartype",
                "colorScheme": "One Half Dark",
                "cursorColor": "#FFFFFD",
                "fontFace": "Cascadia Code PL",
                "suppressApplicationTitle": true,
                "useAcrylic": true
            }

        ]
    },
    ```
    <!-- markdownlint-enable MD046 -->

Et j'ai commenté la partie correspondant au shell Azure.

----

## Conclusion

Il arrive souvent que l'on rencontre des soucis à utiliser l'outillage géomatique libre sous Windows et les solutions existantes peuvent ne pas être adaptées au besoin (lire notre [article sur les possibilités d'automatisation de l'installateur OSGeo4W](2020-07-03_deploy_qgis_windows.md)). S'il ne faut pas oublier que WSL est pensé pour le développement et le test, on a pu voir que c'est une alternative souple et solide à la fois ((c) [Les Inconnus](https://www.youtube.com/watch?v=TpRNInscPdE)).

Pourquoi alors ne pas imaginer déployer [une distribution personnalisée](https://docs.microsoft.com/fr-fr/windows/wsl/build-custom-distro) comme l'[OSGeo Live](https://live.osgeo.org/) via le Windows Store ?

![OSGeo Live 13](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/osgeolive_menu_v13.png "Menu de l'OSGeo Live 13"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->

<!-- Hyperlinks reference -->
[ogr2ogr]: https://gdal.org/programs/ogr2ogr.html
[ogrinfo]: https://gdal.org/programs/ogrinfo.html
