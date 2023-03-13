---
title: "Préparez la conférence QGIS FR avec QDT"
subtitle: Venez avec votre meilleur profil
authors:
    - Julien MOURA
categories:
    - article
date: "2023-03-12 18:20"
description: "Afin de suivre au mieux les rencontres 2023 des utilisateurs francophones de QGIS, je vous propose de déployer facilement un profil QGIS avec tout ce qu'il faut dedans pour suivre les ateliers et présentations. Bonne conférence !"
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/conf_qgis_2023_qdt/qgis_ecran_demarrage_conf_qgis_fr_2023.png
license: beerware
robots: index, follow
tags:
    - OSGeo-fr
    - QDT
    - QGIS Deployment Toolbelt
    - QGIS
---

# La conférence QGIS FR approche : préparez votre environnement avec QDT !

:calendar: Date de publication initiale : 12 mars 2023

Prérequis :

- QGIS
- une connexion internet autorisée vers <https://github.com>

## Introduction

![logo conf QGIS FR 2023](https://cdn.geotribu.fr/img/external/salons_conferences/qgis_fr/qgis_journees_francophones_2023_logo.svg){: .img-rdp-news-thumb }

Organisées par l'OSGeo-FR, les rencontres des utilisateurs francophones de QGIS sont clairement l'événement annuel à ne pas rater quand on travaille avec ce logiciel SIG, qu'on parle principalement français ou qu'on peut difficilement envisager des déplacements à l'étranger (le prochain [QGIS User meeeting se tiendra en avril aux Pays-Bas](https://uc2023.qgis.nl/)).

Cette année encore, malgré toute ma bonne volonté, je n'ai pas réussi à dégager suffisamment de temps pour m'impliquer réellement dans l'organisation en amont, même si je serai présent pour aider. Pour me rattraper, je me suis dit que j'allais faire un petit article, [à l'instar de celui de l'an dernier](/articles/2022/2022-01-12_rencontres_qgis_francophones_liens_utiles_ateliers/). Je profite de ce billet pour tirer mon chapeau aux bénévoles et au CRAIG pour le gros gros travail founi :clap:. Un événement comme celui-ci mobilise beaucoup d'énergie, d'idées, d'initiatives et de temps. Sur la base du seul bénévolat ou presque, c'est remarquable.

Prenez donc aussi le temps d'aller les remercier, que ce soit par un [toot](https://mapstodon.space/@JourneesQgis), [tweet](https://twitter.com/JourneesQgis/), [message sur le GitLab](https://gitlab.com/osgeo-fr/journees_qgis/-/issues), un mail ou un mot gentil en privé ou en live. Je vous attends ici pour la suite :wink:.

C'est bon ? bien, je reprends.

Une conférence QGIS donne à voir l'hétérogénéité des usages, fonctionnalités et outils de l'écosystème QGIS. Il y a donc beaucoup de plugins et autres configurations qui sont présentés et évoqués. Je vous propose donc de déployer facilement un profil QGIS dédié qui contient tout ce qui va être évoqué durant les ateliers et les présentations.

![Un profil QGIS tout en un](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/conf_qgis_2023_qdt/all_inclusive_qgis.webp){: .img-center loading=lazy }

C'est aussi l'occasion de dévoiler [QGIS Deployment Toolbelt](https://guts.github.io/qgis-deployment-cli/) (QDT pour les intimes), un projet sur lequel je travaille depuis un an à Oslandia et qui fera justement l'objet d'une présentation par Emilie Bigorne (EPT Loire) mardi.

2 modes d'installation et d'utilisation au choix dans cet article :

- [tout au clic sur des interfaces graphiques](#jaime-le-son-du-clic)
- [tout à la ligne de commande](#jaime-le-bruit-des-touches)

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## J'aime le son du clic

![Pour l'amour de la souris](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/conf_qgis_2023_qdt/souris_old_school.gif){: .img-center loading=lazy }

1. [Télécharger l'exécutable de QDT pour votre système d'exploitation depuis la page de documentation](https://guts.github.io/qgis-deployment-cli/usage/installation.html)
1. S'assurer qu'il soit autorisé à s'exécuter:
    - sur Linux : clic droit sur l'exécutable > `Propriétés` > onglet `Permissions` > Cocher la case `Autoriser l'exécution du fichier comme un programme`

    ![AUtoriser l'exécution sur Linux](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/conf_qgis_2023_qdt/qdt_linux_authorize_executable.webp){: .img-center loading=lazy }

    - sur Windows : un dialogue s'ouvre avec un message anxiogène indiquant que Windows a protégé votre ordinateur. C'est le moment où il faut nous faire confiance, cliquer sur `Informations complémentaires` > `Exécuter quand même`.

1. Télécharger le [fichier du scénario](https://raw.githubusercontent.com/geotribu/profils-qgis/main/qdt/scenario.qdt.yml) (clic droit -> `Enregistrer sous...`) dans le même dossier que l'exécutable
1. Double-cliquer sur l'exécutable
1. Chercher une icône avec le logo de l'événement sur le bureau ou `Conf QGIS` dans le menu Démarrer

<iframe width="100%" height="430" src="https://www.youtube-nocookie.com/embed/DgdfAf1GRa0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

## J'aime le bruit des touches

Prérequis complémentaires :

- Python 3.10 ou supérieur: avec pip
    - si vous êtes sur Windows, [voir notre article dédié](/articles/2020/2020-06-19_setup_python/ "Installer et configurer Python sur Windows")
    - si vous êtes sur Ubuntu il faut installer pip `sudo apt install python3-pip`
- une connexion internet autorisée vers <https://pypi.org>

![Pour l'amour du clavier](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/conf_qgis_2023_qdt/clavier_joie.gif){: .img-center loading=lazy }

### Installer

<!-- markdownlint-disable MD046 -->
=== ":fontawesome-brands-linux: Linux et assimilés"

    Exemple sur Ubuntu LTS (22.04 à date) :

    ```sh
    pip install --user --upgrade qgis-deployment-toolbelt
    ```

=== ":window: Windows"

    Dans une fenêtre PowerShell :

    ```powershell
    py -3 -m pip install --user --upgrade qgis-deployment-toolbelt
    ```

    Si un message d'avertissement comme celui-ci s'affiche :

    > WARNING: The scripts qdeploy-toolbelt.exe, qdt.exe and qgis-deployment-toolbelt.exe are installed in 'C:\Users\risor\AppData\Roaming\Python\Python310\Scripts' which is not on PATH.  
    > Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

    Il s'agit ajouter le chemin vers le dossier des scripts Python à la variable `PATH` qui liste les dossiers contenant des exécutables. Cela se fait toujours avec PowerShell (adapter avec le chemin de votre installation Python) :

    ```powershell
    $Env:PATH += ";$Env:APPDATA\Python\Python310\Scripts"
    ```

### Configurer

<!-- markdownlint-disable MD046 -->
=== ":fontawesome-brands-linux: Linux et assimilés"

    Si QGIS est installé avec les paquets officiels ([voir cet article](/articles/2023/2023-01-05_installer-qgis-sur-ubuntu/ "Installer QGIS sur Ubuntu avec apt")) et donc accessible sur `/usr/bin/qgis`, il n'y a rien à faire.  

    Sinon, par exemple dans le cas où plusieurs versions de QGIS sont installées sur la machine, il est possible de spécifier le chemin vers l'exécutable de la version à utiliser :

    ```sh
    export QDT_QGIS_EXE_PATH=/path/to/bin/qgis-custom
    ```

=== ":window: Windows"

    Si QGIS 3.28.4 est installé avec l'installateur officiel sans personnalisation du chemin d'installation (ne pas [voir cet article](/articles/2020/2020-07-03_deploy_qgis_windows/ "Installer QGIS avec PowerShell et l'OSGeo4W")) et donc accessible sur `C:\Program Files\QGIS 3.28.4\bin\qgis-ltr-bin.exe`, il n'y a rien à faire.

    Sinon, ouvrir une console PowerShell (++shift++ + clic droit) dans le même dossier et spécifier le chemin vers l'exécutable de QGIS à utiliser :

    ```powershell
    $env:QDT_QGIS_EXE_PATH="C:\\path\\to\\qgis-ltr-bin.exe"
    ```

### Exécuter QDT

=== ":fontawesome-brands-linux: Linux et assimilés"

    Exemple sur Ubuntu LTS (22.04 à date) :

    ```sh
    qdt --scenario https://github.com/geotribu/profils-qgis/raw/main/qdt/scenario.qdt.yml
    ```

    Un raccourci permettant de lancer QGIS avec le profil est créé dans le menu des Appications et sur le bureau. Pour que ce dernier soit fonctionnel, il faut faire un clic-droit et sélectionner `Autoriser l'exécution` :

    ![Autoriser l'exécution d'un raccourci sur le bureau GNOME](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/conf_qgis_2023_qdt/gnome_autoriser_racourci_bureau.webp){: .img-center loading=lazy }

=== ":window: Windows"

    Ouvrir une console PowerShell et taper :

    ```powershell
    qdt --scenario https://github.com/geotribu/profils-qgis/raw/main/qdt/scenario.qdt.yml
    ```

----

## Résulat

![Ecran de démarrage du profil conf QGIS FR 2023](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/conf_qgis_2023_qdt/qgis_ecran_demarrage_conf_qgis_fr_2023.png){: .img-center loading=lazy }

### Personnalisations intégrées

#### Interface

- un raccourci bureau et dans le menu Démarrer/Application
- un splash screen personnalisé
- les barres d'outils sont réorganisées

#### Plugins installés

- CRAIG
- Geotuileur
- ICEtool (désactivé par défaut pour cause de dépendances non présentes par défaut)
Land Survey Codes Import
- LizMap
- Mergin
- QField Sync
- QompliGIS
- QTribu :innocent:

Manquent à l'appel les plugins fermés (Espace Collaboratif de l'IGN...), ceux non déployés sur un dépôt accessible (AL4EO, PLU(i) Versioning, Topaze), ceux qui ne sont pas mentionnés explicitement et bien sûr ceux que j'ai zappés !

----

## Crédits

- le logo du profil est réalisé par Sylvain Beorchia pour l'OSGeo-FR avec l'accord du projet QGIS
- l'image utilisée pour le splash screen réutilise la montgolfière avec l'accord de son auteur (Sylvain Beorchia) et une carte libre de droits de la cartothèque de la BNF

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

{% include "licenses/beerware.md" %}
