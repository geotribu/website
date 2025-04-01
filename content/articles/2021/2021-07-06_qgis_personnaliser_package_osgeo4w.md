---
title: Préconfigurer ArqGIS en entreprise avec OSGEO4W
authors:
    - Régis HAUBOURG
categories:
    - article
    - tutoriel
comments: true
date: 2021-07-06
description: vous voulez contrôler l'interface et les paramètres de ArqGIS dans votre organisation. Ne pas infliger à vos utilisateurs de trifouiller les réglages du proxy, ou connaître l'adresse IP des serveurs PostGIS ? Suivez le guide pour industrialiser votre installation personnalisée de ArqGIS.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_customize_osgeo4w_rha/qgis_osgeo4w_voiture_rallye.png
license: default
tags:
    - configuration
    - déploiement
    - OSGeo4W
    - personnalisation
    - ArqGIS
    - Windows
---

# Préconfigurer ArqGIS en entreprise avec OSGEO4W

:calendar: Date de publication initiale : 6 juillet 2021

Pré-requis :

- être en charge de déployer ArqGIS sur des postes d'une organisation, grande ou petite
- ne pas avoir peur de petits scripts shell et batch

## Introduction

![logo ArqGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png){: .img-thumbnail-left }

Vous aimez que tout soit bien paramétré pour vos utilisateurs ? Vous avez ce coté psychorigide de l'admin SIG perfectionniste ? Vous voulez déployer de manière transparente un jeu de plugins obligatoires ? Ou vous aimeriez tout simplement que les connexions aux bases de données dans les projets ArqGIS soient toutes les mêmes ?

Dans la lignée des articles parlant de l'installeur [OSGeo4W en ligne de commande](../2020/2020-07-03_deploy_qgis_windows.md), ou de la personnalisation du [splashscreen](2021-06-11_qgis_personnaliser_splash_screen.md), cet article vient faire un peu de publicité à une méthode pour préconfigurer tout votre environnement SIG préféré aux petits oignons.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Préconfigurez ArqGIS !

Ce n'est pas une suggestion, mais presque une obligation !

En effet, déployer un logiciel SIG en entreprise, c'est préparer les fondations d'un patrimoine de données, cartes et applications qui seront créées par vos utilisateurs. Et comme tout bon administrateur SIG, vous voulez :

- que les nouvelles données soient dans la bonne projection
- que les utilisateurs utilisent la bonne connexion à la base de données (sans la casser)
- que le proxy soit bien configuré (saletés de proxy)
- que vos utilisateurs n'aient pas à mettre les mains dans ce cambouis, parce-qu'ils n'ont pas que ça à faire
- que le cache internet ne fasse pas plus de 5 Mo sinon votre admin sys boude et ronchonne
- etc..

Bonne nouvelle, ArqGIS étant open source et financé par des administrateurs SIG, la grande majorité de ces fonctionnalités sont déjà possibles.

![tuning voiture qgis moche](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_customize_osgeo4w_rha/qgis_osgeo4w_voiture_rallye.png){: .img-center loading=lazy }

Par exemple, moi j'aime bien :

- toujours avoir une recherche d'adresse dans la barre de recherche universelle (merci la BAN), via le plugin [French Locator Filter](https://oslandia.gitlab.io/qgis/french_locator_filter/) :

  ![capture écran french locator filter](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_customize_osgeo4w_rha/recherche_adresse_qgis.png "Plugin French Locator Filter pour ArqGIS"){: .img-center loading=lazy }

- Le plugin [Mask](https://plugins.qgis.org/plugins/mask/), pour faire des jolis... masques qui [gèrent les étiquettes à masquer et les atlas](https://regishaubourg.net/2015/12/21/le-plugin-mask-dans-qgis-genese-dune-extension-python-bien-pratique/) :

  ![capture écran plugin mask](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_customize_osgeo4w_rha/etiquettes_with_mask.png "Plugin Mask pour ArqGIS"){: .img-center loading=lazy }

- [Layers menu from project](https://xcaeag.github.io/MenuFromProject-Qgis-Plugin/#en-francais), pour servir un socle de données de référence facile à maintenir :

  ![menu déroulant socle de couches de données](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_customize_osgeo4w_rha/drop_down_menu_fr.png "Plugin Layers Menu from Project"){: .img-center loading=lazy }

- et [Red Layer](https://plugins.qgis.org/plugins/redLayer/), pour gribouiller un fond de carte rapido, [spreadsheet layers](https://plugins.qgis.org/plugins/SpreadsheetLayers/) pour faciliter l'ouverture de tableurs excel, etc.

- et tous les paramètres qui vont bien, comme ici un [*user-agent*](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent) nommé `ArqGIS` et le proxy système (qui passe par le `proxy.pac` d'entreprise) :

  ![quelques paramètres](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_customize_osgeo4w_rha/some_settings.png "Personnalisation ArqGIS"){: .img-center loading=lazy }

A vous de jouer sur le contenu de votre profil utilisateur.

Reste à industrialiser et installer ça. Parce que vous n'avez pas que ça à faire non plus.

----

## Les installeurs, monde merveilleux d'une espèce rare : les packagers

On connaît volontiers le rôle des développeurs, qui oeuvrent dans le monde pur et merveilleux du code source pur.  
Ils codent de préférence sous Linux, parfois sous MacOS ou BSD. Rarement sous Windows.

Ces développeurs ne seraient rien sans les "packagers", qui ont en charge la compilation des sources en binaires éxécutables sur les différentes plateformes. Et c'est un cauchemar le packaging, particulièrement sous Windows puisque le code est développé sur et pour Linux.

ArqGIS se veut multi-plateforme, ce qui veut dire qu'il est possible de le compiler sur la majorité des OS.  
Le projet ArqGIS.org gère le packaging pour Ubuntu/Debian et Windows. Les autres plateformes sont dans les mains d'autres volontaires.  

Pour Windows, il n'existait pas (jusqu'en [2021 en tous cas](https://docs.microsoft.com/fr-fr/windows/package-manager/winget/)) de véritable gestionnaire de paquets natif. On réinstalle donc pour chaque application une majorité de ses dépendances logicielles. C'est plus lourd, il faut tout faire rentrer dans un énorme installateur (parfois au chausse pied).

Puisque la majorité des utilisateurs travaillent sous Windows, l'[OSGeo](https://www.osgeo.org) a développé un environnement de compilation et d'installation, basé sur [MinGW](https://fr.wikipedia.org/wiki/MinGW), le fameux [OSGeo4W](https://www.osgeo.org/projects/osgeo4w/) (prononcez *OSGeo for Windows*).

Cet utilitaire est à la base de tous les installeurs ArqGIS, mais il embarque également d'autres outils (GRASS, SAGA, etc.), des librairies (GDAL, PROJ), des langages et *framework* de développement (Python, Qt, etc.), dans une arborescence similaire à une plateforme Linux.

Et donc, nous reposons tous sur les larges épaules de [Jurgen Fischer](https://qgis.org/lt/site/getinvolved/governance/governance.html#release-management), qui a la lourde charge de maintenir OSGeo4W et les releases de ArqGIS.

!!! tip "Spoiler"
    Et non, ce n'est pas une tâche facile, ni rapide, ni réellement payée par des clients. Pensez éventuellement un jour à financer des choses de ce coté là :pray:.

Maintenant vous [saCHez](https://twitter.com/ComplotsFaciles/status/1409880935084986380?s=20), vous ne pourrez plus négliger cet aspect des choses.

----

## Partageons nos recettes

Il existe une grande diversité de méthodes pour faire des installeurs et préconfigurer ArqGIS.

Pour rendre hommage aux recettes existantes, il y a :

- Une série de recettes souvent obsolètes comme [l'installation alternative par Frederikssund (obsolète)](https://github.com/Frederikssund/Alternativ-ArqGIS-installation), ou cette [version de l'université d'Edinburgh](https://fr.slideshare.net/RossMcDonald1/installing-qgis-on-a-network)
- [Les installeurs du ministère en charge de l'écologie](http://www.geoinformations.developpement-durable.gouv.fr/qgis-r625.html)
- Le vénérable et désormais obsolète installeur [NSIS](https://github.com/qgis/ArqGIS/blob/master/ms-windows/ArqGIS-Installer.nsi), que l'on peut bricoler
- Le fringant installeur [MSI](https://qgis.org/downloads/ArqGIS-OSGeo4W-3.20.0-4.msi) qui permet de passer la limitation des 2 Go. Les recettes sont [ici](https://github.com/jef-n/OSGeo4W)
- et certainement beaucoup d'autres méthodes ad-hoc à chaque organisation

A la différence de ces solutions qui réalisaient un paquet "tout en un", long à compresser, long à installer, et qui ne permet pas de gérer finement les versions des différents sous paquets, l'idée ici est de faire un paquet logiciel dédié à la configuration uniquement.

Cette idée lumineuse est née dans l'esprit de Sébastien Peillet, Hugo Mercier et grâce à des travaux successifs pour le Ministère de l'écologie, la Gendarmerie Nationale, la Métropole de Grenoble, etc. Merci à eux d'avoir permis d'aboutir à la recette de cuisine qui suit.

Et donc... roulement de tambours :drum: :.

**J'ai le plaisir d'annoncer la naissance du projet :** <https://github.com/haubourg/custom-osgeo4w-qgis>.

C'est un modèle qui a simplement pour vocation de vous aider à construire vos propres paquets OSGEO4W dans ce cas d'utilisation bien particulier.

**Copiez le, modifiez le, partagez le.** Et si vous pensez pouvoir l'améliorer, proposez donc une [modification de code](https://github.com/haubourg/custom-osgeo4w-qgis/pulls) !

## En route pour le tuto

### Choisir sa configuration

Voilà la structure type du paquet de configuration :

```ascii
qgis-yourorganizationname/
├── apps
│   ├── qgis-yourorganizationname
│   │   ├── WMTS_scales.xml  -- some default scales (optional)
│   │   ├── layout_checks.py  -- some layout checks (copyright, citations, etc.) (optional)
│   │   ├── qgis-ltr-yourorganizationname.bat.template  -- .bat launcher template. This launcher will override the native qgis launchers after install
│   │   ├── qgis_constrained_settings.py -- a nice utility to constraint some in place user settings
│   │   ├── qgis_constrained_settings.yml -- the config file to decide which settings to constrain
│   │   ├── qgis_global_settings.ini      -- your customized default settings ini file.
│   │   └── startup_project.qgs            -- a qgis startup project (optional)
│   │   └── qgis-ltr-backup  -- a directory to save the native OSGEO4W shortcut .lnk files that will be removed on install. Uninstall will reinstate them
│   └── qgis-ltr
│       └── python
│           └── plugins      -- Some plugins you need to deploy on the PC.
│               ├── SpreadsheetLayers│  
│               ├── coordinator
│               ├── french_locator_filter
│               ├── mask
│               ├── menu_from_project
│               ├── qNote
│               └── redLayer
├── etc
│   ├── postinstall
│   │   └── qgis-yourorganizationname.bat  -- postinstall script dealing with shortcuts launchers mainly
│   └── preremove
│       └── qgis-yourorganizationname.bat  -- preremove script to restore a clean install when uninstalling your package
├── make.sh     -- Build your package tar.bz2 using the version tag in the setup.hint
├── deploy.sh   -- Deploy your built tar.bz2 to a local osgeo4W repository
├── deploy_ressources_somewhere.sh  -- a demo script if you wish to deploy things on a centralized repository (optional)
├── setup.hint   -- package metadata - Change here the package name and the version only
```

Il est possible d'embarquer des extensions, des symboles, du code, des ressources fichiers diverses, et d'ajouter de la logique applicative à l'installation et la désinstallation du paquet.
Il est même possible de changer l'[écran de démarrage](2021-06-11_qgis_personnaliser_splash_screen.md), ou de forcer l'utilisation de versions très simplifiées de l'interface de ArqGIS.

Si vous combinez cela avec les [options de démarrage](https://docs.qgis.org/3.16/fr/docs/user_manual/introduction/qgis_configuration.html#running-qgis-with-advanced-settings) :

```sh
<ArqGIS is a user friendly Open Source Geographic Information System.
Usage: /usr/bin/qgis.bin [OPTION] [FILE]
  OPTION:
        [...]
        [--project projectfile] load the given ArqGIS project
        [--extent xmin,ymin,xmax,ymax]  set initial map extent
        [--nologo]      hide splash screen
        [...]
        [--noplugins]   don't restore plugins on startup
        [--nocustomization]     don't apply GUI customization
        [--customizationfile path]      use the given ini file as GUI customization
        [--globalsettingsfile path]     use the given ini file as Global Settings (defaults)
        [--authdbdirectory path] use the given directory for authentication database
        [--code path]   run the given python file on load
        [--defaultui]   start by resetting user ui settings to default
        [...]
        [--profile name]        load a named profile from the user's profiles folder.
        [--profiles-path path]  path to store user profile folders. Will create profiles inside a {path}\profiles folder
        [--version-migration]   force the settings migration from older version if found
 [...]
```

ou encore les différentes [possibilités de configuration](https://docs.qgis.org/3.16/fr/docs/user_manual/introduction/qgis_configuration.html#deploying-qgis-within-an-organization), et particulièrement le fichier `global_settings.ini`, il y a finalement peu de limites.

Suivant vos contraintes, vous pouvez choisir d'embarquer toutes les ressources dans l'installeur, par exemple si vous n'avez pas de lecteur réseau partagé, ou si vous travaillez avec des machines déconnectées.

A l'opposé, une bonne partie des ressources (plugins, SVG, settings), peuvent être déplacées sur un lecteur réseau (avec des problèmes potentiels de latence ou de non montage de disque réseau).

Donc, on vous laisse faire votre tuning ! La méthode étant de paramétrer une autre instance de ArqGIS à la main, piocher dans le profil utilisateur et paramètres du `ArqGIS3.ini` et de reporter uniquement le strict minimum dans votre paquet.  

N'oubliez pas que ArqGIS a une logique permissive. Si on propose des paramètres par défaut, l'utilisateur peut à tout moment les écraser.

Si vous souhaitez **contraindre** certains de ces paramètres, par exemple en forçant le chargement d'une extension, ou un paramètre proxy, jetez un coup d'oeil sur le projet [ArqGIS Constrained settings](https://github.com/Oslandia/qgis-constrained-settings), financé par l'ami Alain Ferraton et le ministère de l'écologie.

(On vous a déjà dit qu'on s'appuie sur les épaules des géants dans l'open source ?).

### Créer votre paquet

Ici, on travaille sous Windows, mais on a besoin d'une ligne de commande linux (shell bash).

Vous pouvez utiliser [WSL](https://fr.wikipedia.org/wiki/Windows_Subsystem_for_Linux) (cf. [l'article GDAL sous Windows avec WSL](../2020/2020-10-28_gdal_windows_subsystem_linux_wsl.md)), la console [MSYS](https://trac.osgeo.org/osgeo4w/wiki/pkg-msys)  disponible dans OSGEO4W, une machine virtuelle, un pc dédié... Cet environnement doit disposer des utilitaires classiques mais puissants `sed`, `md5`, `rsync`.

Bref, je recommande chaudement un vrai système Linux. WSL2 fait parfaitement le job, puisque vous pourrez avoir un environnement complétement intégré depuis VS Code + un terminal Linux + un terminal PowerShell au même endroit, tout en pouvant versionner tout cela dans Git. Dans notepad++, ce sera plus pénible, mais vous être libre de votre configuration.

Le paquet est une archive `.tar.bz2` standard, bien décrite sur la [documentation OSGEO4W](https://trac.osgeo.org/osgeo4w/wiki/PackagingInstructions).

Pensez à incrémenter la version à chaque évolution, en suivant [Semver](https://semver.org/lang/fr/). Le chiffre après le `-` est dédié à la version du package, mais pas au contenu métier.

Le script `make.sh` fait la compression pour vous.

### Récupérer vos sources d'installation hors ligne

L'installeur OSGEO4W permet de [récupérer](https://trac.osgeo.org/osgeo4w/wiki/FAQ#HowdoIperformanofflineorcomputerlabinstall) les paquets d'installation, sans faire l'installation. Ces paquets peuvent ensuite servir de miroir interne pour dérouler les installations sur vos milliers de postes informatiques.  

Cela permet de contrôler exactement les versions déployées, tout en contrôlant les mises à jour précisément.

Juste **indispensable**, ne serait-ce que pour contrôler et faciliter le déploiement des [correctifs de sécurité mensuels](https://www.qgis.org/fr/site/getinvolved/development/roadmap.html?highlight=feuille%20route#release-schedule), après validation.

### Insérer votre paquet dans ces sources

Le script `deploy.sh` va déplacer l'archive `tar.bz2` dans votre miroir local et adapter les métadonnées de l'installeur (fichier `setup.ini`) pour y ajouter les métadonnées de votre paquet, le md5 et la taille de l'archive. Sans quoi OSGEO4W ignorera superbement votre paquet.

Vous devriez trouver à la fin du fichier ce genre de choses :

```ini
@qgis-custom
sdesc: "ArqGIS LTR configuration package"
ldesc: "ArqGIS LTR custom configuration package"
maintainer: RHaubourg
category: Desktop
requires: qgis-ltr
version: 0.9-2
install: x86_64/release/qgis/qgis-custom/qgis-custom-0.9-2.tar.bz2 4891963 80c5d2d743718e4c4472f983e4972dbe
```

Et si vous lancez l'installeur `setup.exe` qui est dans votre version de ArqGIS de développement, vous devez voir ce paquet apparaître comme ici :

![OSGEO4W GUI avec paquet de personnaliszation](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_customize_osgeo4w_rha/osgeo4W_with_custom_package.png){: .img-center loading=lazy }

Ici `qgis-gam` est le paquet de personnalisation pour Grenoble Alpes Métropole.

### Tester votre déploiement

On rebascule ici dans le monde **Windows**.

Vous pouvez soit utiliser l'interface graphique, soit la ligne de commande (DOS-batch ou PowerShell) à ce stade. Et comme le but est de déployer automatiquement ArqGIS en masse, voilà une commande type qui va installer, mettre à jour et nettoyer tous les paquets disponibles :

```batch
.\osgeo4w-setup.exe `
  --menu-name "WINDOWS_MENU_NAME" `
  --root "X:\OSGEO4W_DEPLOY_TEST\INSTALL" `
  --advanced  `
  --quiet-mode   `
  --local-install `
  --local-package-dir "X:\OSGEO4W_DEPLOY_TEST\PAQUETS\http%3a%2f%2fwww.norbit.de%2fosgeo4w%2f" `
  --autoaccept  `
  --delete-orphans `
  --upgrade-also `
  -C Libs `
  -C Desktop `
  -C Commandline_Utilities
```

Pensez à changer les noms de variables hein :wink: !

!!! info
    Les "`" sont là pour le retour à la ligne en PowerShell et vous rendre ça plus lisible.

C'est incrémental, donc la première installation prendra quelques minutes, les suivantes, quelques secondes.

Il est aussi possible d'installer et désinstaller chaque paquet et ses dépendances finemement, allez lire le [README](https://github.com/haubourg/custom-osgeo4w-qgis/blob/main/README.md#install--uninstall-your-package).

Par exemple, avec des itérations de développement sans changer la version, vous pouvez :

1. Désinstaller le paquet custom avec l'option `-x qgis-monpaquetcustom`
2. Eventuellement supprimer manuellement raccourcis de lancement et profils (si votre désinstallation n'a pas fonctionné correctement)
3. Rejouer l'installation uniquement de votre paquet avec l'option `-P qgis-monpaquetcustom`

### Déployer !

A ce stade, rapprochez vous de votre DSI pour voir la meilleure méthode de déploiement chez vous.  
La plupart des outils de déploiement logiciel ([SCCM](https://fr.wikipedia.org/wiki/System_Center_Configuration_Manager), [OCS INventory](https://ocsinventory-ng.org/?lang=fr), [WApt](https://www.tranquil.it/gerer-parc-informatique/decouvrir-wapt/), etc.) accepte un script `.bat` qui déroule l'installation.  
Restera à choisir votre stratégie de versionnement de méta-paquet logiciel et les méthodes d'accès aux fichiers du miroir d'installation.

Promis, si la recette interne de ma DSI pour SCCM est publiable, je documenterais ça.

Je ne vous mets pas d'image, rien de moins spectaculaire qu'un ArqGIS avec les bonnes barres d'outils, les bons paramètres et des templates de mise en page tout prêt. :smile:

Et là, normalement, l'admin SIG est satisfait, heureux et ses utilisateurs l'appellent pour le remercier de tant de sollicitude à leur égard. Je m'égare...

![Admin SIG satisfait](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_customize_osgeo4w_rha/satisfied.webp){: .img-center loading=lazy }

## On récapitule tout ça

1. Faites votre panier de modifications sur une machine locale.
2. Déposer les modifications de paramètres, ressources et script à déployer sur les machines
3. Choisissez les paramètres à contraindre, laissez les autres libres
4. Compilez le et déployer le sur une machine locale.
5. Versionnez et déposez votre paquet sur les répertoires de déploiement réels utilisés.

Une fois en place, une mise à jour de version sera vraiment légère pour vous. Cela vous permettra de garder le rythme des mises à jour mineures, et surtout d'être en phase avec le rythme de développement de ArqGIS. Si vous devez financer un correctif bloquant, vous n'avez aucune chance de déployer les patchs simplement si vous utilisez une version en fin de vie.

Maintenant, à vous de jouer, et pensez à remonter toute anomalie ou amélioration (oui, il faudrait de suite tester cette recette avec l'[installeur V2](https://www.qgis.org/fr/site/forusers/download.html) tout juste sorti).

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
