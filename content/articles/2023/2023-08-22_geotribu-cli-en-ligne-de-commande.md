---
title: Geotribu dans le terminal
subtitle: geotribuGPT
authors:
    - Julien Moura
categories:
    - article
    - meta
date: "2023-08-22 10:20"
description: Consultez Geotribu en ligne de commande
icon: octicons/terminal-24
image:
license: beerware
robots: index, follow
tags:
    - cli
    - Geotribu
    - Python
---

# Le CLI Geotribu : cherchez dans nos contenus et images en ligne de commande

:calendar: Date de publication initiale : 22 août 2023

## Introduction

Que ce soit pour [Isogeo](https://help.isogeo.com/scan/isogeo-scan-offline), en tant qu'indépendant (notamment pour Tactis) et ces derniers mois pour la Géoplateforme de l'IGN ou [QDT](https://github.com/Guts/qgis-deployment-cli/) en tant qu'Oslandien, j'ai eu l'occasion de développer pas mal d'outils en ligne de commande.

Alors pourquoi pas pour Geotribu ? Comme ça je peux expérimenter sans contrainte, proposer un nouveau moyen de consulter les contenus et surtout automatiser certaines tâches plus ou moins récurrentes.

<!-- markdownlint-disable MD040 -->
<!-- termynal -->

```
$ pip install geotribu
---> 100%
Accès au GeoTipi ajouté à votre terminal.
```

<!-- markdownlint-enable MD040 -->

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Prérequis et installation

Le plus simple reste avec un terminal où l'interpréteur Python est installé avec le gestionnaire de packages `pip` :

<!-- markdownlint-disable MD046 -->
=== ":fontawesome-brands-linux: Linux et assimilés"

    Exemple sur Ubuntu LTS (22.04 à date) :

    ```sh
    python3 -m pip install --user --upgrade geotribu
    ```

=== ":window: Windows"

    Dans une fenêtre PowerShell :

    ```powershell
    py -3 -m pip install --user --upgrade geotribu
    ```

    Si un message d'avertissement comme celui-ci s'affiche :

    > WARNING: The scripts qdeploy-toolbelt.exe, qdt.exe and qgis-deployment-toolbelt.exe are installed in 'C:\Users\risor\AppData\Roaming\Python\Python310\Scripts' which is not on PATH.  
    > Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

    Il s'agit ajouter le chemin vers le dossier des scripts Python à la variable `PATH` qui liste les dossiers contenant des exécutables. Cela se fait toujours avec PowerShell (adapter avec le chemin de votre installation Python) :

    ```powershell
    $Env:PATH += ";$Env:APPDATA\Python\Python310\Scripts"
    ```
<!-- markdownlint-enable MD046 -->

[Documentation d'installation détaillée :material-book-plus:](https://cli.geotribu.fr/usage/installation.html){: .md-button }
{: align=middle }

### Tester l'installation

![logo console terminal](https://cdn.geotribu.fr/img/logos-icones/divers/ligne_commande.png "logo console terminal"){: .img-rdp-news-thumb }

Comme pour tout autre outil, pour vérifier que l'installation s'est déroulée correctement, il est de bon ton d'exécuter les commandes de base : `--version` et `--help` (sorties non contractuelles :wink:) :

```sh
> geotribu --version
0.15.0
> geotribu --help
USAGE: geotribu [-v] [-h] [--version] {read-latest,récents,latest,rl,rss,search-content,contenus,sc,search-image,images,img,si,upgrade,auto-update,maj,update} ...

Geotribu Toolbelt 0.15.0 - Des outils pour faciliter les tâches récurrentes des contributeur/ices de Geotribu.

OPTIONS:
  -v, --verbose         Niveau de verbosité : None = WARNING, -v = INFO, -vv = DEBUG. Réglable avec la variable d'environnement GEOTRIBU_LOGS_LEVEL.
  -h, --help            Affiche l'aide et s'arrête là.
  --version             Affiche la version du CLI et s'arrête là.

SOUS-COMMANDES:
  {read-latest,récents,latest,rl,rss,search-content,contenus,sc,search-image,images,img,si,upgrade,auto-update,maj,update}
    read-latest (récents, latest, rl, rss)
                        Consulter les derniers contenus du site
    search-content (contenus, sc)
                        Rechercher dans les contenus du site
    search-image (images, img, si)
                        Rechercher dans les images de Geotribu
    upgrade (auto-update, maj, update)
                        Mettre à jour Geotribu CLI.

Des outils pour les administrateur/ices, contributeur/ices ou les lecteur/ices de Geotribu.

Développé par Julien Moura (Geotribu)
Documentation : https://cli.geotribu.fr/
```

La plupart des options sont configurables en variable d'environnement :

[Consulter les options de configuration :material-book-cog:](https://cli.geotribu.fr/usage/configuration.html){: .md-button }
{: align=middle }

----

## Utilisation

Cette trousse à outils est destinée à évoluer au gré des besoins et surtout de mon temps disponible ou de celui que des contributeur/ices voudront bien y investir. Le champ fonctionnel n'est donc pas figé et c'est pour cela que la documentation est configurée pour être générée à la volée à partir du code et des commandes/sous-commandes disponibles.
Inutile donc de dupliquer ici avec une obsolescence programmée ce qui est automatiquement à jour ailleurs.

[Voir les exemples :material-book-cog:](https://cli.geotribu.fr/usage/exemples.html){: .md-button }
{: align=middle }

- [x] lister les derniers contenus publiés (à partir du flux RSS) :

    ```sh
    geotribu rss
    # en spécifiant le nombre et le type de contenus (article ou rdp)
    geotribu rss -f rdp -n 10
    ```

- [x] chercher dans les articles et revues de presse

    ```sh
    geotribu sc orfeo
    # en spécifiant la présence d’un mot dans le titre et lister les 5 premiers résultats
    geotribu sc -n 5 "+title:openstreetmap postgis"
    ```

- [x] ouvrir un contenu (soit dans le terminal, soit dans l'application par défaut)

    Après chaque commande de recherche, il est proposé d'ouvrir un contenu parmi les résultats.

    ```sh
    geotribu sc orfeo
    # en spécifiant la présence d’un mot dans le titre et lister les 5 premiers résultats
    geotribu sc -n 5 "+title:openstreetmap postgis"
    ```

- [x] chercher une image parmi celles hébergées sur Geotribu

    ```sh
    geotribu si postgis
    # uniquement les icônes ou logos
    geotribu si postgis -f logo
    ```

- [x] optimiser une ou plusieurs images pour la publication (dimensions, format, nom...)*

    ```sh
    # depuis un chemin local ou une URL distante
    geotribu img optimize {URL_OU_CHEMIN_IMAGE}
    # tout un dossier
    geotribu images optimize {CHEMIN_VERS_DOSSIER_LOCAL_AVEC_IMAGES_A_OPTIMISER}
    ```

- [x] lister les derniers commentaires

    ```sh
    geotribu comments latest
    ```

- [x] poster le dernier commentaire publié sur Mastodon (instance Mapstodon)[^1]

    ```sh
    geotribu comments broadcast -t mastodon
    ```

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

{% include "licenses/beerware.md" %}

<!-- Notes de bas de page -->
[^1]: commandes nécessitant un jeton d'authentification à l'API
