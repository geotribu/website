---
title: "Utiliser GDAL avec WSL"
authors: ["Julien MOURA"]
categories: ["article", "tutoriel"]
date: "2020-10-28 10:20"
description: "En restaurant les géogames de Geotribu, des mini-jeux sur la culture générale en cartographie et géomatique, j'ai trouvé un jeu qui n'avait jamais été publié qui consiste à associer les déserts à leurs continents. Saurez-vous ne pas finir privé/e de désert ?"
image: "https://cdn.geotribu.fr/img/tuto/gdal_wsl/ubuntu_wsl_landing_page.png"
tags: "gdal,ogr,windows,wsl"
---

# Utiliser GDAL sur Windows Subsystem for Linux

:calendar: Date de publication initiale : 28 octobre 2020

**Mots-clés :** GDAL | OGR | Windows | WSL | Linux

Pré-requis :

- un [Windows à jour](#version-minimale-de-windows)
- un compte avec les droits d'administrateur (au moins durant la phase d'installation)

## Introduction

![icône GDAL](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/gdal.png "logo GDAL"){: .img-rdp-news-thumb }

Deux étapes dans ce tutoriel :

- [installer et configurer le sous-système](#installer-wsl) Windows pour Linux
- utiliser le sous-système pour [utiliser GDAL 3.1.4 dans Ubuntu 20.04](#utiliser-gdal-dans-le-sous-systeme-linux-de-windows) sans quitter son terminal Windows

## Installer WSL

Même si [la documentation](https://docs.microsoft.com/fr-fr/windows/wsl/install-win10) est très bien faite et même traduite en français, on va un peu paraphraser pour ajouter quelques précisions au passage.

### Vérifier les pré-requis

#### Version minimale de Windows

Le sous-système est quelque chose d'encore récent (surtout la version 2), donc il faut vérifier qu'on est bien dans les clous. Dans Powershell :

```powershell hl_lines="3"
PS C:\Users\geojulien> systeminfo | findstr /B /C:"OS Name" /C:"OS Version" /C:"System Type"
OS Name:                   Microsoft Windows 10 Pro
OS Version:                10.0.19041 N/A Build 19041
System Type:               x64-based PC
```

Si le numéro du build est supérieur ou égal à `18362` (ou `19041` pour les socles ARM), c'est bon. Sinon, revenez après avoir fait vos mises à jour :wave:.

#### Un terminal moderne

Comme déjà évoqué dans [l'article sur l'environnement de travail Python sur Windows](/articles/2020/2020-06-19_setup_python/#utiliser-powershell), utiliser `cmd` n'est pas une option et il va falloir entrer quelques commandes Powershell pour ensuite profiter joyeusement de bash :partying_face:.

Avec WSL, les choses se compliquent car il devient nécessaire de pouvoir switcher d'un terminal à l'autre, par exemple d'un Powershell sur le Windows hôte vers le bash de l'une des distributions installées avec WSL. Le terminal intégré de Powershell en étant incapable, il nous faut donc installer le **nouveau terminal** :

- depuis [le Windows Store](https://aka.ms/terminal) - **méthode recommandée**
- avec winget : `winget install --id=Microsoft.WindowsTerminal -e`
- avec chocolatey : `choco install microsoft-windows-terminal`
- avec [le MSIX Bundle](https://github.com/microsoft/terminal/releases/download/v1.3.2651.0/Microsoft.WindowsTerminal_1.3.2651.0_8wekyb3d8bbwe.msixbundle) - mais attention, ça ne gère pas les futures mises à jour automatiques

??? "Le spot de pub d'inspiration éro-automobile :underage:"
    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/8gw0rXPMMPE" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Installer WSL

WSL faisant partie du bouquet de fonctionnalités avancées, il faut donc un accès administrateur pour l'activer (par la suite, ce sera ok pour un utilisateur de base) :

1. Activer WSL et la VM

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

Volà, désormais nous avons notre distribution Ubuntu 20.04 prête à être utilisée dans notre Windows. Allez, on s'arrrrête pas en si bon chemin : on continue vers l'installation de GDAL !

----

## Utiliser GDAL dans le sous-système Linux de Windows

Une fois notre distribution installée, continuons nos opérations sur notre nouveau terminal.

Avant d'aller plus loin, quelques commandes à retenir, qui sont évidemment disponibles (et même traduites !) via l'argument `--help` :

[![Onglets WSL dans Windows Terminal](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl_terminal_tabs.png "Titre image"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl_terminal_tabs.png){: data-mediabox="ligthbox-gallery" data-title="Changer de shell encore plus facilement que de chemise"}

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

Rien que du très classique, donc d'abord, on définit la version de GDAL que l'on souhaite :

```bash
export GDAL_VERSION=3.1.*
```

Ensuite, on ajoute le dépôt bien connu d'ubuntugis :

```bash
sudo add-apt-repository ppa:ubuntugis/ubuntugis-unstable && sudo apt-get update
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

1. télécharger une donnée ouverte (au hasard : [les bassin de mobilité scolaire en Normandie](https://www.data.gouv.fr/fr/datasets/bassins-de-mobilite-scolaire-normandie/), version convertie à la volée),
2. vérifier rapidement son état avec `ogrinfo`
3. convertir en couche de GeoPackage (parce-que c'est la hype), en appliquant des contrôles géométriques

Et tout ça, en lançant les commandes depuis Powershell !

#### Télécharger la donnée avec wget

A l'instar des autres utilitaires intégrés de base dans Ubuntu, `wget` n'attend que d'être utilisé via WSL :

```powershell
# wget est accessible, pourquoi se priver ?
wsl -d Ubuntu-20.04 -- wget https://www.data.gouv.fr/fr/datasets/r/931cb357-33e6-46d6-8d2c-a17be9038e90 -O test_gdal_wsl.shp.zip
```

Et voilà mon fichier dans mon explorateur Windows :

[![capture wget wsl](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl_test_wget_download.png "Résultat du téléchargement avec wget dans Windows"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl_test_wget_download.png){: data-mediabox="ligthbox-gallery" data-title="Résultat du téléchargement avec wget dans Windows"}

#### Un petit ogrinfo des familles

On peut donc regarder de plus près notre fichier téléchargé avec un bon vieux [ogrinfo] :

```powershell
# ogrinfo
wsl -d Ubuntu-20.04 -- ogrinfo -al -so test_gdal_wsl.shp.zip
```

[![capture wsl ogrinfo](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl_ogrinfo.png "ogrinfo dans Windows via WSL"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl_ogrinfo.png){: data-mediabox="ligthbox-gallery" data-title="ogrinfo dans Windows via WSL"}

#### Contribuons à la fin du règne du Shapefiles

Histoi

```powershell
wsl -d Ubuntu-20.04 -- ogr2ogr -t_srs EPSG:3857 -f GPKG "geotribu_gdal_wsl_gpkg.gpkg" "test_gdal_wsl.shp.zip" -nln "GDAL_Windows_SO_SIMPLE" -nlt POLYGON -dim 2 -overwrite -makevalid
```

[![capture qgis résultat ogr2ogr](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl_ogr2ogr_result_qgis.png "ogrinfo dans Windows via WSL"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/gdal_wsl/wsl_ogr2ogr_result_qgis.png){: data-mediabox="ligthbox-gallery" data-title="La couche du geopackage dans QGIS en sortie d'ogr2ogr via WSL"}

----

## Bonux stage

### Personnaliser le terminal

Dans le nouveau terminal, il est possible de [personnaliser chaque shell répertorié](https://docs.microsoft.com/fr-fr/windows/terminal/customize-settings/profile-settings) histoire de s'y retrouver facilement ou tout simplement de faire les choses à son goût.

??? "Ma configuration (objet `profiles/list`)"
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

Et j'ai commenté la partie correspondant au shell Azure.

----

## Ressources

- <https://docs.microsoft.com/fr-fr/windows/wsl/install-win10>

----

## Auteurs

--8<-- "content/team/jmou.md"
