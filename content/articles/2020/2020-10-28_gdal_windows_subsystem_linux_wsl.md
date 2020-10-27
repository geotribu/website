---
title: "Utiliser GDAL avec WSL"
authors: ["Julien MOURA"]
categories: ["article"]
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

Deux étapes dans cet article :

- [installer et configurer le sous-système](#installer-wsl)
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

2. Redémarrer
3. [Télécharger](https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi) et installer la version 2 de WSL
4. Définir la version à utiliser : `wsl --set-default-version 2`

En cas de doute, se référer à [la documentation officielle](https://docs.microsoft.com/fr-fr/windows/wsl/install-win10) et/ou harceler votre DSI.

### Installer une ou plusieurs distributions

Une fois le sous-système prêt, il est temps d'installer une ou plusieurs distributions Linux parmi celles disponibles (voir [la liste ici](https://docs.microsoft.com/fr-fr/windows/wsl/install-win10#step-6---install-your-linux-distribution-of-choice)).

Pour ce tutoriel, on a besoin d'[Ubuntu 20.04](https://www.microsoft.com/store/apps/9n6svws3rx71).

----

## Utiliser GDAL dans le sous-système Linux de Windows

----

## Bonux stage

### Personnaliser le terminal

Dans le nouveau terminal, il est possible de [personnaliser chaque shell répertorié](https://docs.microsoft.com/fr-fr/windows/terminal/customize-settings/profile-settings) histoire de s'y retrouver facilement ou tout simplement de faire les choses à son goût.

??? "Ma configuration (objet `profiles/list`)"
    ```json
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
