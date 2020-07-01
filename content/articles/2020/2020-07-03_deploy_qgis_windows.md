---
title: "Installer QGIS sur Windows avec Powershell"
authors: Julien Moura
category: article
date: 2020-07-03 10:20
description: "Comment déployer QGIS sur Windows avec Powershell, via chocolatey ou un script."
hero: "Déploiement de QGIS sur Windows avec Powershell."
tags: qgis,installation,osgeo,powershell,deploiement,setup,windows,chocolatey
---

# Installer QGIS sur Windows avec Powershell

:calendar: Date de publication initiale : 3 juillet 2020

**Mots-clés :** QGIS | Windows | Déploiement | Installation | Powershell

## Prérequis

- une machine avec Windows installé
- droits administrateur
- droits d'exécution de scripts
- optionnellement : [Git]

## Comment L'Installateur (CLI) fonctionne

On l'oublie souvent (ou on ne le sait tout simplement pas, comme moi pendant de longues et heureuses années) mais les installateurs sont d'abord des outils en ligne de commande (des [CLIs](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande) comme disent les grandes personnes) qui proposent en prime une interface graphique... qui est rarement mieux qu'un concours de clics sur `Suivant`.

### --help ex machina

Il y a quelques mois de cela, je cherchais à automatiser l'installation et la configuration de QGIS sur Windows et j'avais donc creusé du côté de [l'installateur de l'OSGeo](https://qgis.org/fr/site/forusers/download.html). En regardant [l'aide de l'exécutable](https://trac.osgeo.org/osgeo4w/wiki/CommandLine), on s'aperçoit qu'il est possible de passer un certain nombre d'arguments :

```powershell
# ô installateur, dis-moi quels sont tes secrets
.\osgeo4w-setup-x86_64.exe --help
```

Ce qui nous donne :

```txt
Command Line Options:
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
Ending OSGeo4W install
```

Avec tout ça, on a de quoi faire !

### Scriptons

A l'instar de beaucoup de choses dans Windows, le langage de script Powershell a une syntaxe très verbeuse plutôt lourde, du genre "Pourquoi faire simple quand on peut faire compliqué ?"... mais vient avec une interface graphique permettant de se repérer : [ISE].

#### Définir le niveau de droits


----

## Utiliser le

### 1. Récupérer le script

Si vous avez installé [Git], lancer le terminal Powershell :

```powershell
# cloner le script
git clone https://gist.github.com/6303dc5eb941eb24be3e27609cd46985.git qgis-deploy-win
# entrer dans le répertoire ainsi créé
cd .\qgis-deploy-ltr-win\
```

En listant le contenu avec un bon `ls` des familles, voici ce que l'on obtient :

![Répertoire du gist du script powershell](https://cdn.geotribu.fr/img/tuto/qgis_deploy_windows/qgis_deploy_win_gist_overview.png "Contenu du répertoire du Gist")

### 2. Exécuter le script

Lancer le terminal en mode administrateur cette fois et exécuter le script :

```powershell
.\qgis_deploy_install_upgrade_ltr.ps1
```

![Installation](https://cdn.geotribu.fr/img/tuto/qgis_deploy_windows/qgis_deploy_win_gist_overview.png "Contenu du répertoire du Gist")

Le temps d'un café (ou d'une bière) et hop, on est prêt pour de nouvelles aventures avec QGIS !

:coffee:/:beer: --> :rocket:

----

## Pour la route

Pour info, il est également possible d'utiliser [Chocolatey](https://chocolatey.org/) :

```powershell
choco install qgis-ltr
```

----

## Auteur

--8<-- "content/team/jmou.md"

<!-- Hyperlinks reference -->
[Git]: https://git-scm.com/
[ISE]: https://docs.microsoft.com/fr-fr/powershell/scripting/windows-powershell/ise/introducing-the-windows-powershell-ise
