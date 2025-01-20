---
title: Installer QGIS sur Windows avec OSGeo4W et Powershell
authors:
    - Julien MOURA
categories:
    - article
    - tutoriel
comments: true
date: 2020-07-03
description: Comment déployer automatiquement (téléchargement et installation) QGIS sur Windows avec un script Powershell (ou via chocolatey), en tirant parti des capacités de l'installeur OSGeo4W.
image: https://cdn.geotribu.fr/img/tuto/qgis_deploy_windows/qgis_deploy_win_prog_postinstall.png
tags:
    - déploiement
    - OSGeo4W
    - PowerShell
    - QGIS
    - Windows
---

# Installer QGIS sur Windows en ligne de commande (OSGeo4W et Powershell)

:calendar: Date de publication initiale : 3 juillet 2020

L'installation et la mise à jour de QGIS peuvent être rébarbatives, notamment sous Windows où il n'est pas possible de profiter d'une mise à jour via une simple ligne de commande (`apt` mon amour :heart:)... Il y a quelques mois de cela, je cherchais à automatiser l'installation et la configuration de QGIS sur Windows et j'avais donc creusé du côté de [l'installateur de l'OSGeo](https://qgis.org/fr/site/forusers/download.html).

J'avais abouti à un petit script Powershell et vu que j'avais trouvé cela pratique, je me l'étais mis de côté sur [Gist](https://gist.github.com/Guts/6303dc5eb941eb24be3e27609cd46985). Fidèle au *Geotribu Spirit* :copyright:{: .copyleft }, pourquoi ne pas partager le résultat et (surtout) la démarche ? :wink:

!!! info "Prérequis"
    - une machine avec Windows et Powershell
    - droits administrateur
    - droits d'exécution de scripts, comme pour les environnements virtuels Python (voir [la doc Microsoft](https://docs.microsoft.com/fr-fr/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7) ou [cet article](2020-06-19_setup_python.md#autoriser-lutilisation-des-environnements-virtuels)) : `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
    - optionnellement : [Git]

## Comment L'Installateur (CLI) fonctionne

On l'oublie souvent (ou on ne le sait tout simplement pas, comme moi pendant de longues et heureuses années) mais les installateurs sont d'abord des outils en ligne de commande (des [CLIs](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande) comme disent les grandes personnes) qui proposent en prime une interface graphique... qui est rarement mieux qu'un concours de clics sur `Suivant`.

![OSGeo4W QGIS](https://cdn.geotribu.fr/img/tuto/qgis_deploy_windows/osgeo4w_qgis.png "OSGeo for Windows et QGIS"){: .img-center loading=lazy }

### --help ex machina

En regardant [l'aide de l'exécutable](https://trac.osgeo.org/osgeo4w/wiki/CommandLine), on s'aperçoit qu'il est possible de passer un certain nombre d'arguments :

```powershell
# ô installateur, dis-moi quels sont tes secrets
osgeo4w-setup-x86_64.exe --help
```

Ce qui nous donne :

```txt
Command Line Options:
 -b --disable-buggy-antivirus      Disable known or suspected buggy anti virus
                                   software packages during execution.
 -g --upgrade-also                 also upgrade installed packages
 -o --delete-orphans               remove orphaned packages
 -n --no-shortcuts                 Disable creation of desktop and start menu
                                   shortcuts
 -N --no-startmenu                 Disable creation of start menu shortcut
 -d --no-desktop                   Disable creation of desktop shortcut
 -r --no-replaceonreboot           Disable replacing in-use files on next
                                   reboot.
 -k --autoaccept                   Accept all licenses
 -l --local-package-dir            Local package directory
 -m --menu-name                    Menu name
 -a --arch                         architecture to install (x86_64 or x86)
 -R --root                         Root installation directory
 -q --quiet-mode                   Unattended setup mode
 -M --package-manager              Semi-attended chooser-only mode
 -h --help                         print help
 -p --proxy                        HTTP/FTP proxy (host:port)
 -x --remove-packages              Specify packages to uninstall
 -c --remove-categories            Specify categories to uninstall
 -P --packages                     Specify packages to install
 -C --categories                   Specify entire categories to install
 -D --download                     Download from internet
 -L --local-install                Install from local directory
 -t --test                         Use setup_test.ini
 -A --advanced                     Advanced install (as opposed to Express)
 -S --safe                         Safe Mode (Skip some admin actions)
 -s --site                         Download site
 -O --only-site                    Ignore all sites except for -s
```

Avec tout ça, on a de quoi faire un joli script dont l'idée est de :

1. télécharger l'installateur
2. l'utiliser pour télécharger les packages de QGIS LTR
3. l'utiliser pour installer les packages

En avant :nerd_face: !

----

## Scriptons

A l'instar de beaucoup de choses dans Windows, le langage de script Powershell a une syntaxe très verbeuse plutôt lourde, du genre "Pourquoi faire simple quand on peut faire compliqué ?"... mais vient avec une interface graphique permettant de se repérer : [ISE].

Je détaille ici les étapes du script mais en cas d'empressement, voir la partie [Utiliser le script](#utiliser-le-script).

### Sudoku

Tout d'abord, on s'assure que le script est bien lancé en mode administrateur :

```powershell
#Requires -RunAsAdministrator
```

### Télécharger l'installateur

Histoire de respecter les bonnes pratiques du système, on va télécharger l'installateur dans le dossier `Téléchargements` de l'utilisateur :

```powershell
# on se met le chemin actif de côté pour y revenir en toute fin
$starter_path = Get-Location
# on se déplace dans le dossier téléchargement de l'utilisateur
Set-Location -Path "$env:USERPROFILE/Downloads"
```

Une fois au bon endroit, on télécharge l'installateur, sauf s'il existe déjà dans le dossier :

```powershell
if (-Not (Test-Path "osgeo4w-setup-x86_64.exe" -PathType leaf )) {
   Invoke-WebRequest -Uri "https://download.osgeo.org/osgeo4w/osgeo4w-setup-x86_64.exe" -OutFile "osgeo4w-setup-x86_64.exe"
}
```

### Lancer le téléchargement et l'installation

Après un avoir regardé de plus près les options de l'installateur [OSGeo4W], voici à quoi va ressembler notre commande que j'ai détaillée et mis en multi-lignes pour que ce soit plus lisible :

```powershell
.\osgeo4w-setup-x86_64.exe `
    --advanced `                # correspond à l'option Advanced Install
    --arch x86_64 `             # on est en 2020...
    --autoaccept `              # accepte toutes les licences
    --delete-orphans `          # supprime les paquets inutilisés
    --no-desktop `              # ne pas créer d'icône sur le bureau
    --packages qgis-ltr-full `  # le paquet (en fait le meta-paquet) souhaité
    --quiet-mode `              # ne pas demander d'action de l'utilisateur
    --site http://download.osgeo.org/osgeo4w `  # le serveur principal d'où télécharger les paquets
    --site http://osgeo4w-oslandia.com/mirror   # le miroir d'Oslandia
    --upgrade-also              # met à jour les paquets
```

Concrètement, les packages sont téléchargés dans le dossier temporaire de l'utilisateur (classiquement : `C:\Users\USERNAME\AppData\Local\Temp\{url_site}`) puis sont décompressés et déplacés vers le dossier habituel de l'installateur : `C:\OSGeo4W64`. Il est possible de modifier ces deux emplacements via respectivement les options `--local-package-dir` et `--root`.

!!! tip "Serveurs (sites) de téléchargement"
    L'option `-s/--site` est répétable afin de pouvoir passer plusieurs serveurs (comme dans l'interface graphique) et les URLs doivent faire partie de ce fichier `https://download.osgeo.org/osgeo4w/mirrors.lst`.

----

## Utiliser le script

Maintenant qu'on a compris les différentes étapes, voici comment utiliser le script que j'ai publié facilement.

### 1. Récupérer le script

Si vous avez installé [Git], lancer le terminal Powershell :

```powershell
# cloner le script
git clone https://gist.github.com/6303dc5eb941eb24be3e27609cd46985.git qgis-deploy-win
# entrer dans le répertoire ainsi créé
cd .\qgis-deploy-win\
```

Sinon il est possible de [télécharger le script via ce lien](https://gist.github.com/Guts/6303dc5eb941eb24be3e27609cd46985/archive/7d1bc758aa274f66ce0b0fd50529f2fa2ab4e9af.zip) et dézipper le tout.

En listant le contenu avec un bon `ls` des familles, voici ce que l'on obtient :

![Répertoire du gist du script powershell](https://cdn.geotribu.fr/img/tuto/qgis_deploy_windows/qgis_deploy_win_gist_overview.png "Contenu du répertoire du Gist")

### 2. Exécuter le script

Lancer le terminal en mode administrateur cette fois et exécuter le script :

```powershell
.\qgis_deploy_install_upgrade_ltr.ps1
```

Le téléchargement des packages se lance :

![Téléchargement des packages](https://cdn.geotribu.fr/img/tuto/qgis_deploy_windows/qgis_deploy_win_prog.png "Téléchargement des packages de QGIS LTR")

Puis l'installation :

![Installation](https://cdn.geotribu.fr/img/tuto/qgis_deploy_windows/qgis_deploy_win_prog_postinstall.png "Installation des packages de QGIS LTR")

Le temps d'un café (ou d'une bière) et hop, on est prêt pour de nouvelles aventures avec QGIS !

:coffee:/:beer: --> :rocket:

## Conclusion

On voit donc qu'il est possible d'automatiser l'installation et le déploiement de QGIS, mais aussi de tous les logiciels et packages auxquels l'installateur [OSGeo4W] donne accès.

----

<!-- markdownlint-disable MD046 -->
!!! tip "Pour la route"
    Pour info, il est également possible d'utiliser [Chocolatey](https://chocolatey.org/) :

    ```powershell
    choco install qgis-ltr
    ```
<!-- markdownlint-enable MD046 -->

----

<!-- geotribu:authors-block -->

<!-- Hyperlinks reference -->
[Git]: https://git-scm.com/
[ISE]: https://docs.microsoft.com/fr-fr/powershell/scripting/windows-powershell/ise/introducing-the-windows-powershell-ise
[OSGeo4W]: https://trac.osgeo.org/osgeo4w/wiki/OSGeo4W_fr
