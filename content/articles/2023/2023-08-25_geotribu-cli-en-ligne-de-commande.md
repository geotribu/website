---
title: Geotribu dans le terminal
subtitle: geotribuGPT
authors:
    - Julien Moura
categories:
    - article
    - meta
comments: true
date: 2023-08-25
description: 'Consultez Geotribu en ligne de commande : rechercher et afficher nos contenus directement dans votre terminal.'
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

:calendar: Date de publication initiale : 25 août 2023

Prérequis :

- Python 3.9+
- un terminal gérant les hyperliens : Bash, PowerShell 5+, etc.
- une appétence pour la ligne de commande

## Introduction

![logo Geotribu CLI](https://cdn.geotribu.fr/img/internal/charte/geotribu_cli_logo.webp){: .img-thumbnail-left }

Que ce soit pour concevoir un (éphémère) [scan Isogeo hors-ligne](https://help.isogeo.com/scan/isogeo-scan-offline/), en tant qu'indépendant (notamment pour Tactis et des traitements liés à GraceTHD) et ces derniers mois pour la Géoplateforme de l'IGN ou [QDT](https://guts.github.io/qgis-deployment-cli/) en tant qu'Oslandien, j'ai eu l'occasion de développer pas mal d'outils en ligne de commande ([CLI](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande) pour les intimes).

Alors pourquoi pas pour Geotribu ? Comme ça, je peux expérimenter sans contrainte, proposer un nouveau moyen de consulter les contenus et surtout automatiser certaines tâches plus ou moins récurrentes.

Petite présentation pour les lecteur/ices qui considèrent qu'un terminal est une interface agréable ou pour celles/eux qui aimeraient se mettre à la ligne de commande pour briller en société de géogeeks !

<!-- markdownlint-disable MD040 -->
<!-- termynal -->

```
$ pip install geotribu
---> 100%
Bienvenue dans le GeoTipi !
Pour démarrer, taper : 'geotribu --help' ou 'geotribu rss'.
```

<!-- markdownlint-enable MD040 -->

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Prérequis et installation

Le plus simple est d'utiliser le gestionnaire de paquets Python (`pip`) depuis un terminal, il suffit de lancer la commande adaptée à votre système.

<!-- markdownlint-disable MD046 -->
=== ":fontawesome-brands-linux: Linux et assimilés"

    Exemple sur Ubuntu LTS (22.04 à date) :

    ```sh
    python3 -m pip install --upgrade geotribu
    ```

=== ":window: Windows"

    Dans une fenêtre PowerShell :

    ```powershell
    py -3 -m pip install --upgrade geotribu
    ```

    Si un message d'avertissement comme celui-ci s'affiche :

    > WARNING: The scripts geotribu.exe are installed in 'C:\Users\username\AppData\Roaming\Python\Python310\Scripts' which is not on PATH.  
    > Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

    Il s'agit d'ajouter le chemin vers le dossier des scripts Python à la variable `PATH`` qui liste les dossiers contenant des exécutables. Cela se fait toujours avec PowerShell (adapter le chemin en fonction de la version de votre installation Python) :

    ```powershell
    $Env:PATH += ";$Env:APPDATA\Python\Python310\Scripts"
    ```

    Puis allez lire [cet article](../2020/2020-06-19_setup_python.md#ajouter-python-au-path) :wink: !
<!-- markdownlint-enable MD046 -->

[Documentation d'installation détaillée :material-book-plus:](https://cli.geotribu.fr/usage/installation.html){: .md-button }
{: align=middle }

### Tester l'installation

![logo console terminal](https://cdn.geotribu.fr/img/logos-icones/divers/ligne_commande.png "logo console terminal"){: .img-thumbnail-left }

Comme pour tout autre outil, pour vérifier que l'installation s'est déroulée correctement, il est de bon ton d'exécuter les commandes de base : `--version` et `--help` (sorties non contractuelles :wink:) :

Par exemple, la commande :

```sh
geotribu --help
```

Donne quelque chose comme :

```sh
{% include "code/geotribu_cli_help.txt" %}
```

La plupart des options sont configurables en variable d'environnement :

[Consulter les options de configuration :material-book-cog:](https://cli.geotribu.fr/usage/configuration.html){: .md-button }
{: align=middle }

----

## Utilisation

Cette trousse à outils est destinée à évoluer au gré des besoins et surtout de mon temps disponible ou de celui que des contributeur/ices voudront bien y investir. Le champ fonctionnel n'est donc pas figé et c'est pour cela que la documentation est configurée pour être générée à la volée à partir du code et des commandes/sous-commandes disponibles.
Inutile donc de dupliquer ici avec une obsolescence programmée ce qui est automatiquement à jour ailleurs.

[Voir les exemples :material-book-cog:](https://cli.geotribu.fr/usage/examples.html){: .md-button }
{: align=middle }

Dans les grandes lignes :

- [x] lister les derniers contenus publiés (à partir du flux RSS) :

    ```sh
    geotribu rss
    # en spécifiant le nombre et le type de contenus (`article` ou `rdp`)
    geotribu rss -f rdp -n 10
    ```

- [x] chercher dans les articles et revues de presse

    ```sh
    geotribu sc orfeo*
    # en spécifiant la présence d’un mot dans le titre et lister les 5 premiers résultats
    geotribu sc -n 5 "+title:openstreetmap postgis"
    ```

- [x] ouvrir un contenu (soit dans le terminal, soit dans l'application par défaut)

    Après chaque commande de recherche, il est proposé d'ouvrir un contenu parmi les résultats. Mais il est également possible d'ouvrir un résultat depuis une commande passée.

    ```sh
    geotribu open 0
    ```

- [x] chercher une image parmi celles hébergées sur Geotribu

    ```sh
    geotribu si postgis
    # uniquement les icônes ou logos
    geotribu si postgis -f logo
    ```

- [x] optimiser une ou plusieurs images pour la publication (dimensions, format, nom...)[^1]

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

Sinon consulter la vidéo de présentation :

<iframe width="100%" height="415" src="https://www.youtube-nocookie.com/embed/eWNBpUVYakY?si=ridPSohVCs5232Gd" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Un outil déjà utilisé et ouvert

AU départ un _side-project_ perso, l'outil est finalement déjà en "production", utilisé à plusieurs étapes du cycle de vie de Geotribu :

- comme dépendance du site, pour la vérification de la structure des contenus
- bientôt pour amorcer la structure d'un nouveau contenu
- pour [republier les commentaires sur Mastodon](https://mapstodon.space/tags/Geotribot)

C'est évidemment open source et libre (licence MIT) donc si cela vous intéresse, si vous rencontrez un bug ou si vous souhaitez ajouter une fonctionnalité, n'hésitez pas à faire un tour sur le GitHub :

[Consulter le dépôt du code :fontawesome-regular-file-code:](https://github.com/geotribu/cli/){: .md-button }
{: align=middle }

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}

<!-- Notes de bas de page -->
[^1]: commandes nécessitant un jeton d'authentification à une API
