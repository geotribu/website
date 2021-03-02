---
title: "Configurer l'environnement pour l'édition en local"
category: tutoriel
date: 2020-07-23 10:20
description: "Guide de contribution à Geotribu : comment déployer l'environnment local idéal pour la contribuer."
tags: contribution,édition,markdown,guide
---

# Installation pour l'édition locale

!!! tip
    Remplir d'abord [les prérequis](../../requirements).
    Les chemins de fichiers et répertoires sont à adapter à votre environnement.

## Git

La mise en ligne du contenu se fait via [Git]. Si vous n'êtes pas à l'aise avec la ligne de commande, il est possible d'utiliser [GitHub Desktop].

Cloner le dépôt, soit avec la commande ci-dessous, soit via [le bouton vert sur le dépôt avec GitHub Desktop](https://github.com/geotribu/website) :

```bash
cd ~/git-repos/geotribu/
git clone --depth=1 https://github.com/geotribu/website.git
```

----

## Python

Pour éditer localement et visualiser le résultat final avant de publier sur le dépôt, il faut installer [Python] 3.7 ou supérieure et les dépendances du projet. Exemple avec Ubuntu 18. 04 et Windows 10 (quelques adaptations peuvent être nécessaires):

<!-- markdownlint-disable MD046 -->
=== "Bash"
    ```bash
    # se rendre à la racine du dépôt local - adapter à son environnement
    cd ~/git-repos/geotribu/website/

    # lister les versions de Python installées
    ls -1 /usr/bin/python* | grep '[2-3].[0-9]$'

    # si aucune version supérieure ou égale à 3.7 n'est installée, installons la dernière
    sudo apt install python3.8

    # créer un environnement virtuel
    python3.8 -m venv .venv
    source .venv/bin/activate

    # mettre à jour pip et les outils de packaging
    pip install -U pip setuptools wheel

    # installer les dépendances
    python -m pip install -U -r requirements.txt
    ```

=== "Powershell"
    ```powershell
    # se rendre à la racine du dépôt local - adapter à son environnement
    cd ~/git-repos/geotribu/website/

    # si besoin, autoriser l'utilisation des environnements virtuels
    # commande à exécuter dans Powershell en mode administrateur (puis quitter le mode admin avant de continuer)
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

    # lister les versions de Python installées
    py --list

    # créer un environnement virtuel
    py -3.7 -m venv .venv   # attention ne fonctionne pas avec Python installé depuis le Windows Store

    # activer l'environnement virtuel
    .\.venv\Scripts\activate

    # mettre à jour pip
    python -m pip install -U pip

    # installer les dépendances
    python -m pip install -U -r requirements.txt
    ```
<!-- markdownlint-enable MD046 -->

!!! tip
    Le projet est configuré pour mettre semi-automatiquement à jour certaines dépendances. Il est donc recommandé de  mettre son environnement virtuel local à jour avant de contribuer : `pip install -U -r requirements.txt`.

----

## Pre-commit

Le projet vient avec une [configuration](https://github.com/geotribu/website/blob/master/.pre-commit-config.yaml) pour [pre-commit], qui permet d'appliquer des scripts (des [_git hooks_](https://git-scm.com/book/fr/v2/Personnalisation-de-Git-Crochets-Git)) de vérification et de nettoyage des fichiers avant qu'ils ne soit enregistrés dans le dépôt (d'où le nom).

L'installation est optionnelle mais recommandée car l'outil garantit :

- un socle minimal de qualité des contenus et codes sources
- une cohérence d'ensemble entre les contributions
- qu'une fois poussée sur le dépôt central, la contribution passe [les checks exécutés par Github Action](https://github.com/geotribu/website/actions?query=workflow%3A%22Code+Rules+Checker%22).

Installer [pre-commit] :

```bash
# installer
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

Il est également possible de les exécuter manuellement :

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

### Docker

Il est possible de se passer de Python en utilisant Docker.

```bash
docker-compose -f "docker-compose-mkdocs.dev.yml" up --build
```

Le site est accessible sur : <http://localhost:8000>

----

## Mettre à jour son dépôt local

Après qu'une branche ait été fusionnée (*merged*), elle est automatiquement supprimée par GitHub afin d'éviter de garder un trop grand nombre de branches. Il faut alors mettre à jour le dépôt local sur votre machine :

<!-- markdownlint-disable MD046 -->
=== "Bash"
    ```bash
    # mettre le dépôt local en conformité avec le dépôt central (notamment en supprimant les branches locales déjà supprimées sur GitHub)
    git remote prune origin

    # supprimer les branches qui ont été fusionnées - sauf master
    git branch --merged | grep -i -v -E "master|gh-pages"| xargs git branch -d
    ```

=== "Powershell"
    ```powershell
    # mettre le dépôt local en conformité avec le dépôt central (notamment en supprimant les branches locales déjà supprimées sur GitHub)
    git remote prune origin

    # ouvre une fenêtre de sélection des branches à supprimer
    git branch --format "%(refname:short)" --merged  | Out-GridView -PassThru | % { git branch -d $_ }
    ```
<!-- markdownlint-enable MD046 -->

<!-- Hyperlinks reference -->
[Git]: https://git-scm.com/download/
[GitHub Desktop]: https://desktop.github.com/
[GitHub]: https://help.github.com/en/github/writing-on-github
[markdown]: https://fr.wikipedia.org/wiki/Markdown
[MkDocs / Material]: https://squidfunk.github.io/mkdocs-material/specimen/
[pre-commit]: https://pre-commit.com/
[Python]: https://docs.python.org/fr/3/tutorial/
[StackEdit]: https://stackedit.io/
[Visual Studio Code]: https://github.com/DavidAnson/vscode-markdownlint#intro
