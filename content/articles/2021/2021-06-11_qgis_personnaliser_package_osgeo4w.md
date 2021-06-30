---
title: "Préconfigurer QGIS en entreprise"
authors: ["Régis HAUBOURG"]
categories: ["article", "tutoriel"]
date: "2021-07-06 10:20"
description: "vous voulez contrôler l'interface et les paramètres de QGIS dans votre organisation. Ne pas infliger à vos utilisateurs de trifouiller les réglages du proxy, ou connaître l'adresse IP des serveurs PostGIS? Suivez le guide pour industrialiser votre installation personnalisée"
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_customize_osgeo4w_rha/qgis_osgeo4w_voiture_rallye.png"
tags: "QGIS,personnalisation,osgeo4W,déploiement,configuration"
---

# Personnaliser l'image au lancement de QGIS

:calendar: Date de publication initiale : 1er juillet 2021

**Mots-clés :** QGIS | OSGEO4W | installeur

Pré-requis :

- être en charge de déployer QGIS sur des postes d'une organisation, grande ou petite
- ne pas avoir peur de petits scripts shell et batch

## Introduction

![logo QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/tuning_qgis.png){: .img-rdp-news-thumb }

Vous aimez que tout soit bien paramétré pour vos utilisateurs? Vous avez ce coté psycho rigide de l'admin SIG perfectionniste? Vous voulez déployer de manière transparente un jeu de plugins obligatoires? Ou vous aimeriez tout simplement que les connexions aux bases de données dans les projets QGIS soient toutes les mêmes?

Dans la série des articles parlant de l'installeur [OSGeo4W en ligne de commande](https://static.geotribu.fr/articles/2020/2020-07-03_deploy_qgis_windows/), ou de la personnalisation du [splashscreen](https://static.geotribu.fr/articles/2021/2021-06-11_qgis_personnaliser_splash_screen/), cet article vient faire un peu de publicité à une méthode pour préconfigurer tout votre environnement SIG préféré aux petits oignons.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Préconfigurez QGIS!

Ce n'est pas une suggestion, mais presque un ordre !

En effet, déployer un logiciel SIG en entreprise, c'est préparer les fondations d'un patrimoine de données, cartes et applications qui seront créées par vos utilisateurs.  Et comme tout bon administrateur SIG, vous voulez :

- que les nouvelles données soient dans la bonne projection
- que les utilisateurs utilisent la bonne connection à la base de données (sans la casser)
- que le proxy soit bien configuré (saletés de proxy)
- que vos utilisateurs n'aient pas à mettre les mains dans ce cambouis la, parce qu'ils n'ont pas que ça à faire
- que le cache internet ne fasse pas plus de 5 Mo sinon votre admin sys boude et ronchonne
- etc...

Bonne nouvelle, QGIS étant open source, et financé par des administrateurs SIG, la grande majorité de ces fonctionnalités sont déjà possibles.

Reste à les mettre en oeuvre chez vous, pour installer QGIS. Et industrialiser ça. Parce que vous n'avez pas que ça à faire non plus.

----

## Les installeurs, monde adoré d'une espèce rare, les packagerzs

On connaît volontiers le rôle des développeurs, qui oeuvrent dans le monde pur et merveilleux avec du code source pur.  
Ils codent de préférence sous linux, parfois sous MacOs ou BSD. Rarement sous Windows.

Ces développeurs ne seraient rien sans les "packagers", qui ont en charge la compilation des sources en binaires éxécutables sur les différentes plateformes. Et c'est un cauchemar le packaging, particulièrement sous Windows.
QGIS est multi-plateforme, ce qui veut dire qu'il est possible de le compiler sur la majorité des OS.
Le projet QGIS.org gère le packaging pour Ubuntu/Debian, et Windows. Les autres plateformes sont dans les mains d'autres volontaires.  

Pour Windows, Il n'existait pas (jusqu'en 2020) de véritable gestionnaire de paquet. On réinstalle donc pour chaque application une majorité de ses dépendances logicielles. C'est plus lourd, il faut tout faire rentrer dans un énorme installeur (parfois au chausse pied)

L'[OSGeo](https://www.osgeo.org) a développé un environnement de compilation et d'installation, basé sur [MinGW](https://fr.wikipedia.org/wiki/MinGW), le fameux [OSGEO4W](https://www.osgeo.org/projects/osgeo4w/) (prononcez "for Windows").

Cet utilitaire est à la base de tous les installeurs QGIS, mais il embarque également d'autres outils (GRASS, SAGA, etc.. ), des librairies (GDAL, PROJ), des framework de développement (python, Qt, etc.. ), dans une arborescence similaire à une plateforme linux.

Et donc, nous reposons tous les larges épaules d'un certain [Jurgen Fischer](https://qgis.org/lt/site/getinvolved/governance/governance.html#release-management), qui a la lourde charge de maintenir OSGEO4W et les releases de QGIS. Et non, ce n'est pas une tâche "fun". _Et non, c'est rarement payé (pensez éventuellement un jour à financer des choses de ce coté là. Ça c'est dit.)_

Maintenant vous [saCHez](https://twitter.com/ComplotsFaciles/status/1276808463809753088?s=20), vous ne pourrez plus négliger cet aspect des choses.

----

## Partageons nos recettes

Il existe une grande diversité de méthodes pour faire des installeurs et préconfigurer QGIS.

Pour rendre hommage aux recettes existantes, il y a :

- Une série de recettes souvent obsolètes comme [l'installation alternative par Frederikssund (obsolète)](https://github.com/Frederikssund/Alternativ-QGIS-installation), ou cette [version de l'université d'Edinburgh](https://fr.slideshare.net/RossMcDonald1/installing-qgis-on-a-network)
- [Les installeurs du ministère en charge de l'écologie](http://www.geoinformations.developpement-durable.gouv.fr/qgis-r625.html)
- Le vénérable et désormais obsolète installeur [NSIS](https://github.com/qgis/QGIS/blob/master/ms-windows/QGIS-Installer.nsi), que l'on peut bricoler
- Le fringant installeur [MSI](https://qgis.org/downloads/QGIS-OSGeo4W-3.20.0-4.msi) qui permet de passer la limitation des 2 Go. Les recettes sont [ici](https://github.com/jef-n/OSGeo4W)
- et certainement beaucoup d'autres méthodes ad-hoc à chaque organisation

A la différence de ces solutions qui réalisaient un paquet 'tout en un', long à compresser, long à installer, et qui ne permet pas de gérer finement les versions des différents sous paquets, l'idée ici est de faire un paquet logiciel dédié à la configuration uniquement.

Cette idée lumineuse est née dans l'esprit de Sébastien Peillet, Hugo Mercier, et grâce à des travaux successifs pour le Ministère de l'écologie, la gendarmerie nationale, la Métropole de Grenoble, etc... Merci à eux d'avoir permis d'aboutir à la recette de cuisine qui suit.

Et donc... roulement de tambours ...

**J'ai le plaisir d'annoncer la naissance du projet:**

<https://github.com/haubourg/custom-osgeo4w-qgis>

C'est un modèle qui a simplement pour vocation de vous aider à construire vos propres paquets OSGEO4W dans ce cas d'utilisation bien particulier.

Copiez le, modifiez le, partagez le. Et si vous pensez pouvoir l'améliorer, proposez donc une [modification de code](https://github.com/haubourg/custom-osgeo4w-qgis/pulls) !

## Choisir sa configuration

Voilà la structure type du paquet de configuration :

```ascii
qgis-yourorganizationname/
├── apps
│   ├── qgis-yourorganizationname
│   │   ├── WMTS_scales.xml  -- some default scales (optional)
│   │   ├── layout_checks.py  -- some layout checks (copyright, citations, etc..) (optional)
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
├── setup.hint   -- package metadat - Change here the package name and the version only
```

Il est possible d'embarquer des extensions, des symboles, du code, des ressources fichiers diverses, et d'ajouter de la logique applicative à l'installation et la désinstallation du paquet.
Il est même possible de changer l'[écran de démarrage](https://static.geotribu.fr/articles/2021/2021-06-11_qgis_personnaliser_splash_screen/), ou de forcer l'utilisation de version très simplifiées de l'interface de QGIS.

Si vous combinez cela avec, les [options de démarrage](https://docs.qgis.org/3.16/fr/docs/user_manual/introduction/qgis_configuration.html#running-qgis-with-advanced-settings) ou les différentes [possibilités de configuration](https://docs.qgis.org/3.16/fr/docs/user_manual/introduction/qgis_configuration.html#deploying-qgis-within-an-organization), il y a finalement peu de limites.

Suivant vos contraintes, vous pouvez choisir d'embarquer toutes les ressources dans l'installeur, par exemple si vous n'avez pas de lecteur réseau partagé, ou si vous travaillez avec des machines déconnectées. A l'opposé, une bonne partie des ressources, plugins, SVG, settings, peuvent être déplacé sur un lecteur réseau (avec des problèmes potentiels de latence ou de non montage de disque réseau).

Donc, on vous laisse faire votre tuning ! L'idée étant de paramétrer une autre instance de QGIS à la main, piocher dans le profil utilisateur les ressources, et paramètres dans le QGIS3.ini et de reporter uniquement le minimum dans votre paquet.  

N'oubliez pas que QGIS a une logique permissive. Si on propose des paramètres par défaut, l'utilisateur peut à tout moment les écraser.
Si vous souhaitez contraindre certains de ces paramètres, par exemple en forçant le chargement d'une extension, ou un paramètre proxy, jetez un coup d'oeil sur le projet [QGIS Constrained settings](https://github.com/Oslandia/qgis-constrained-settings), financé par l'ami Alain Ferraton et le ministère de l'écologie.

(On vous a déjà dit qu'on s'appuie sur les épaules des géants dans l'open source?)

## Créer votre paquet

Ici, on travaille sous Windows, mais on a besoin d'une ligne de commande linux. Vous pouvez utiliser WSL2, la console MSYS de l'OSGEO4W, une machine virtuelle.

Le paquet est un fichier .tar.bz2 standard, bien décrit sur la [documentation OSGEO4W](https://trac.osgeo.org/osgeo4w/wiki/PackagingInstructions).

Pensez à incrémenter la version à chaque évolution, en suivant [Semver](https://semver.org/lang/fr/). Le chiffre après le `-` est dédié à la version du package, mais pas au contenu métier.

Le script `make.sh` fait la compression pour vous.

## Récupérer vos sources d'installation hors ligne

L'installeur OSGEO4W permet de [récupérer](https://trac.osgeo.org/osgeo4w/wiki/FAQ#HowdoIperformanofflineorcomputerlabinstall) les paquets d'installation, sans faire l'installation. Ces paquets peuvent ensuite servir de miroir interne pour dérouler les installations sur vos milliers de postes informatiques.
Cela permet de contrôler exactement les versions déployées, tout en contrôlant les mises à jour précisément. Indispensable selon moi.

## Insérer votre paquet dans ces sources

Le script `deploy.sh` va déplacer l'archive `tar.bz2` dans votre miroir local et adapter les métadonnées de l'installeur (fichier `setup.ini`) pour y ajouter les métadonnées de votre paquet, le md5 et la taille de l'archive. Sans quoi OSGEO4W ignorera superbement votre paquet

Vous devriez trouver à la fin du fichier ce genre de chose :

```ini
@qgis-custom
sdesc: "QGIS LTR configuration package"
ldesc: "QGIS LTR custom configuration package"
maintainer: RHaubourg
category: Desktop
requires: qgis-ltr
version: 0.9-2
install: x86_64/release/qgis/qgis-custom/qgis-custom-0.9-2.tar.bz2 4891963 80c5d2d743718e4c4472f983e4972dbe
```

## Tester votre déploiement

On rebascule ici dans le monde Windows. (au passage, je vous conseille moi aussi vivement WSL2 pour avoir linux et Windows sur une même machine et vous simplifier la vie.)

Vous pouvez soit utiliser l'interface graphique, soit la ligne de commande à ce stade. Et comme le but est de déployer automatiquement QGIS en masse, voilà une commande type qui va installer, mettre à jour et nettoyer tous les paquets disponibles :

Pensez à changer les noms de variables hein.

```batch
.\osgeo4w-setup.exe  --menu-name "WINDOWS_MENU_NAME" --root "X:\OSGEO4W_DEPLOY_TEST\INSTALL" --advanced  --quiet-mode --local-install --local-package-dir "X:\OSGEO4W_DEPLOY_TEST\PAQUETS\http%3a%2f%2fwww.norbit.de%2fosgeo4w%2f" --autoaccept  --delete-orphans --upgrade-also -C Libs -C Desktop -C Commandline_Utilitiesinstall
```

C'est incrémental, donc la première installation prendra quelques minutes, les suivantes, quelques secondes.

Il est possible d'installer et désinstaller chaque paquet et ses dépendances finemement, allez lire le README :smile:.

## Déployer !

A ce stade, rapprochez vous de votre DSI pour voir la meilleur méthode de déploiement chez vous.
La plupart des outils de déploiement logiciel (SCCm, OCS INventory, WApt, etc...) accepte un script .bat qui déroule l'installation.
Restera à choisir votre stratégie de versionnement de méta-paquet logiciel, et les méthodes d'accès aux fichiers du miroir d'installation.

Je ne vous mets pas d'image, rien de moins spectaculaire qu'un QGIS avec les bonnes barres d'outils, les bons paramètres et des templates de mise en page tout prêt. :)

----

## Auteur

--8<-- "content/team/rha.md"
