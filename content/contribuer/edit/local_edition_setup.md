---
title: "Configurer l'environnement pour l'édition en local"
categories:
    - contribution
    - tutoriel
date: 2020-07-23 10:20
description: "Guide de contribution à Geotribu : comment déployer l'environnement local idéal pour contribuer tranquillement."
tags:
    - contribuer
    - git
    - guide
    - installation locale
    - Markdown
    - Python
    - Visual Studio Code
---

<!-- markdownlint-disable MD046 -->

# Installation pour l'édition locale

Après avoir rempli [les prérequis](/contribuer/requirements/) généraux, pour travailler sur le site en local, il faut donc :

- [Git](#git)
- [Python](#python)
- une connexion autorisée vers le [CDN de Geotribu]

Il est également recommandé de disposer de [Node.js (LTS)](https://nodejs.org) pour pouvoir utiliser markdownlint (voir [Rédiger en Markdown : enjeux de qualité et règles](/contribuer/guides/markdown_quality/#verifier-la-syntaxe-avec-markdownlint-cli)).

Cette page a pour but de vous guider dans les principales étapes mais il est probable que chacun/e doive ajuster selon son propre environnement de travail (chemins de fichiers, répertoires...).

!!! tip
    Pour aborder de façon sympathique le fonctionnement du site web, pourquoi ne pas commencer par suivre le tutoriel publié fin 2020 pour déployer Geotribu localement ?

    [Toi aussi, déploie le site Geotribu chez toi :fontawesome-solid-home:](/articles/2020/2020-12-30_deployer_geotribu_a_la_maison/){: .md-button }
    {: align=middle }

----

## Git

![logo Git](https://cdn.geotribu.fr/img/logos-icones/divers/git.png "logo Git"){: .img-rdp-news-thumb }

La gestion et la mise en ligne du contenu se font via [Git]. Si vous n'êtes pas à l'aise avec la ligne de commande, il est possible d'utiliser [GitHub Desktop].

### Installation

### Récupérer le site localement

Cloner le dépôt, soit avec la commande ci-dessous, soit via [le bouton vert sur le dépôt avec GitHub Desktop](https://github.com/geotribu/website) :

```bash
cd ~/git-repos/geotribu/
git clone --depth=1 https://github.com/geotribu/website.git
```

## Mettre à jour son dépôt local

Après qu'une branche ait été fusionnée (*merged*), elle est automatiquement supprimée sur le dépôt central (hébergé sur [GitHub]) afin d'éviter de garder un dépôt propre et lisible. Il faut alors mettre à jour le dépôt local sur votre machine :

=== "Linux (Bash)"
    ```bash
    # mettre le dépôt local en conformité avec le dépôt central (notamment en supprimant les branches locales déjà supprimées sur GitHub)
    git remote prune origin

    # supprimer les branches qui ont été fusionnées - sauf master
    git branch --merged | grep -i -v -E "master|gh-pages"| xargs git branch -d
    ```

=== "Windows (Powershell)"
    ```powershell
    # mettre le dépôt local en conformité avec le dépôt central (notamment en supprimant les branches locales déjà supprimées sur GitHub)
    git remote prune origin

    # ouvre une fenêtre de sélection des branches à supprimer
    git branch --format "%(refname:short)" --merged  | Out-GridView -PassThru | % { git branch -d $_ }
    ```

----

## Python

![logo Python](https://cdn.geotribu.fr/img/logos-icones/programmation/python.png "logo Python"){: .img-rdp-news-thumb }

Pour éditer localement et visualiser le résultat final avant de publier sur le dépôt, il faut installer [Python] 3.7 ou supérieure et les dépendances du projet.

### Installation de Python

=== "Linux (Bash)"
    ```bash
    # lister les versions de Python installées
    ls -1 /usr/bin/python* | grep '[2-3].[0-9]$'

    # si aucune version de Python supérieure ou égale à 3.7 n'est installée, installons la 3.8 par exemple
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.8
    ```

=== "Windows (Powershell)"
    Le mieux est encore de suivre l'article dédié :

    [Python : installation et configuration sur Windows :fontawesome-solid-home:](/articles/2020/2020-06-19_setup_python/#installation-et-configuration){: .md-button }
    {: align=middle }

### Création de l'environnement de travail

Pour travailler tranquillement sans risquer de casser quoi que ce soit dans l'installation de Python au niveau du système, on préfère utiliser un environnement virtuel.

=== "Linux (Bash)"
    ```bash
    # se rendre à la racine du dépôt local - adapter au dossier dans lequel vous avez cloné le dépôt
    cd ~/git-repos/geotribu/website/

    # créer un environnement virtuel
    python3 -m venv .venv
    source .venv/bin/activate

    # mettre à jour pip et les outils de packaging
    python -m pip install -U pip
    python -m pip install -U setuptools wheel

    # installer les dépendances
    python -m pip install -U -r requirements-free.txt
    ```

=== "Windows (Powershell)"
    ```powershell
    # se rendre à la racine du dépôt local - adapter au dossier dans lequel vous avez cloné le dépôt
    cd ~/git-repos/geotribu/website/

    # si besoin, autoriser l'utilisation des environnements virtuels
    # commande à exécuter dans Powershell en mode administrateur (puis quitter le mode admin avant de continuer)
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

    # lister les versions de Python installées - hors mode admin donc
    py --list

    # créer un environnement virtuel - Attention : ne fonctionne pas avec Python installé depuis le Windows Store
    py -3.7 -m venv .venv  

    # activer l'environnement virtuel
    .\.venv\Scripts\activate

    # mettre à jour pip
    python -m pip install -U pip
    python -m pip install -U setuptools wheel

    # installer les dépendances
    python -m pip install -U -r requirements-free.txt
    ```

!!! abstract "A exécuter régulièrement"
    Les dépendances du projet sont mises à jour mensuellement. Il est donc recommandé de mettre son environnement virtuel local à jour **avant** de contribuer, avec la commande :

    `python -m pip install -U -r requirements-free.txt`

<!-- markdownlint-enable MD046 -->

----

## Pre-commit

![icône news générique](https://cdn.geotribu.fr/img/internal/icons-rdp-news/news.png "News"){: .img-rdp-news-thumb }

Le projet vient avec une [configuration](https://github.com/geotribu/website/blob/master/.pre-commit-config.yaml) pour [pre-commit], qui permet d'appliquer des scripts (des [_git hooks_](https://git-scm.com/book/fr/v2/Personnalisation-de-Git-Crochets-Git)) de vérification et de nettoyage des fichiers avant qu'ils ne soit enregistrés dans le dépôt (d'où le nom).

L'installation est optionnelle mais recommandée car l'outil garantit :

- un socle minimal de qualité des contenus et codes sources
- une cohérence d'ensemble entre les contributions
- qu'une fois poussée sur le dépôt central, la contribution passe [les checks exécutés par Github Action](https://github.com/geotribu/website/actions?query=workflow%3A%22Code+Rules+Checker%22).

Installer [pre-commit] :

```bash
# depuis l'intérieur de l'environnement virtuel
pre-commit install
```

Une fois installés, les scripts s'exécuteront à chaque commit. Ne pas se laisser impressionner par les messages verbeux :wink: :

```bash
> git commit

[WARNING] Unstaged files detected.
[INFO] Stashing unstaged files to C:/Users/mPokora/.cache/pre-commit/patch1588143245.
Trim Trailing Whitespace.............................(no files to check)Skipped
Detect Private Key...................................(no files to check)Skipped
Fix End of Files.....................................(no files to check)Skipped
Check Yaml...........................................(no files to check)Skipped
Check for added large files..........................(no files to check)Skipped
[INFO] Restored changes from C:/Users/mPokora/.cache/pre-commit/patch1588143245.
```

Il est également possible de tous les exécuter manuellement :

```bash
pre-commit run -a
```

----

## Servir en local

Puis de lancer la commande qui lance le site en local avec rechargement automatique :

```bash
# servir le site avec mkdocs
mkdocs serve

# il existe aussi un mode où le rechargement automatique est plus rapide mais ne concerne que la page modifiée
mkdocs serve -f mkdocs-minimal.yml --dirtyreload

# si besoin, il est évidemment possible de spécifier le port
mkdocs serve -f mkdocs-minimal.yml --dirtyreload -a localhost:8085
```

Par défaut, le site est accessible sur : <http://localhost:8000> mais il est évidemment possible de spécifier le port à utiliser : `mkdocs serve -a localhost:8085`.

----

## Docker

![logo Docker](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/docker.png "logo Docker"){: .img-rdp-news-thumb }

Il est également possible d'utiliser Docker. L'avantage est que c'est alors la seule dépendance à installer (plus besoin de Python, NodeJS ou même de Git si vous téléchargez le dépôt). L'inconvénient est que c'est assez lourd pour un site qui se veut léger :wink: !

```bash
docker-compose -f "docker-compose-mkdocs.dev.yml" up --build
```

Le site est alors accessible sur : <http://0.0.0.0:8000>

<!-- Hyperlinks reference -->
[markdown]: https://fr.wikipedia.org/wiki/Markdown
[MkDocs / Material]: https://squidfunk.github.io/mkdocs-material/specimen/
[Python]: https://docs.python.org/fr/3/tutorial/
[StackEdit]: https://stackedit.io/
[Visual Studio Code]: https://github.com/DavidAnson/vscode-markdownlint#intro

<!-- Intègre le glossaire centralisé -->
--8<-- "content/toc_nav_ignored/snippets/glossaire.md"
