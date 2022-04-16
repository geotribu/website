---
title: "Configurer l'environnement pour l'édition en local"
categories:
    - contribution
    - tutoriel
date: 2020-07-23 10:20
description: "Guide de contribution à Geotribu : comment déployer l'environnement local idéal pour contribuer tranquillement."
image: "https://cdn.geotribu.fr/img/internal/contribution/geotribu_ide_vscode_local.png"
tags:
    - contribuer
    - git
    - guide
    - installation locale
    - Markdown
    - Python
    - Visual Studio Code
# theme customizations
search:
  exclude: true
---

<!-- markdownlint-disable MD046 -->

# Installation et configuration de l'environnement de travail pour l'édition locale

![logo markdown](https://cdn.geotribu.fr/img/logos-icones/markdown.png "logo Markdown"){: .img-rdp-news-thumb }

Cette page a pour but de vous guider dans les principales étapes afin de pouvoir gérer le site et ses contenus depuis une machine locale. Il est probable que chacun/e doive ajuster selon son propre environnement de travail (chemins de fichiers, répertoires...).

Après avoir rempli [les prérequis](/contribuer/requirements/) généraux, pour travailler sur le site en local, il faut donc :

- [Git](#git)
- [Python](#python)

Il est également recommandé :

- d'avoir une connexion autorisée vers le [CDN de Geotribu]
- d'installer [Node.js (LTS)](https://nodejs.org) pour pouvoir utiliser markdownlint (voir [Rédiger en Markdown : enjeux de qualité et règles](/contribuer/guides/markdown_quality/#verifier-la-syntaxe-avec-markdownlint-cli)).

!!! tip
    Pour aborder de façon sympathique le fonctionnement du site web, pourquoi ne pas commencer par suivre le tutoriel publié fin 2020 pour déployer Geotribu localement ?

    [Toi aussi, déploie le site Geotribu chez toi :fontawesome-solid-house-chimney-window:](/articles/2020/2020-12-30_deployer_geotribu_a_la_maison/){: .md-button }
    {: align=middle }

----

## Git

![logo Git](https://cdn.geotribu.fr/img/logos-icones/divers/git.png "logo Git"){: .img-rdp-news-thumb }

La gestion et la mise en ligne du contenu se font via [Git], une suite d'outils en ligne de commande ([CLI](https://fr.wikipedia.org/wiki/Interface_en_ligne_de_commande)). Si vous n'êtes pas à l'aise avec la ligne de commande, il est possible d'utiliser [GitHub Desktop] en suivant [la documentation officielle](https://docs.github.com/en/desktop).

### Installation

Il y a beaucoup de ressources sur la Toile pour installer et configurer [Git].  
Nous mettons ici une documentation minimaliste destinée à donner la trame globale de l'installation de Git, mais il y a fort à parier que cette documentation soit trop générique. A chacun/e de trouver tuto à son pied si besoin !

=== "Debian (Bash)"
    Pour avoir une version récente de Git, il faut ajouter les dépôts communautaires :

    ```bash
    sudo add-apt-repository ppa:git-core/ppa
    sudo apt update
    sudo apt install git
    ```

=== "Windows (Powershell)"
    Il "suffit" d'utiliser l'installateur à télécharger depuis le site officiel. Quelques ressources tout de même :

    - la [documentation Microsoft](https://docs.microsoft.com/fr-fr/devops/develop/git/install-and-set-up-git#windows)
    - le tutoriel d'[Astuces Informatiques](https://astuces-informatique.com/comment-installer-utiliser-git-sous-windows/)

### Récupérer le site localement

Cloner le dépôt :

- soit via [le bouton vert sur le dépôt avec GitHub Desktop](https://github.com/geotribu/website). Dans ce cas-là, ouvrez un terminal Powershell dans le dossier décompressé et passez à l'étape suivante.
- soit avec les commandes ci-dessous :

```bash
$ cd ~/git-repos/geotribu/
$ git clone --depth=1 https://github.com/geotribu/website.git
Clonage dans 'website'...
remote: Enumerating objects: 850, done.
remote: Counting objects: 100% (850/850), done.
remote: Compressing objects: 100% (780/780), done.
remote: Total 850 (delta 112), reused 202 (delta 60), pack-reused 0
Réception d'objets: 100% (850/850), 2.47 Mio | 8.84 Mio/s, fait.
Résolution des deltas: 100% (112/112), fait.
```

!!! question "Et le SSH alors ?!"
    Pourquoi je ne mentionne pas la possibilité de cloner par SSH ?
    Parce-que si vous vous posez cette question, c'est que vous n'avez pas du tout besoin de lire cette partie-là car, félicitations : vous avez un niveau en Git supérieur à un *quickstart* ! :partying_face:

### Configurer Git

Il s'agit d'indiquer le nom et l'adresse email qui seront utilisés pour les commits. Par exemple, si vous vous appelez Mona Lisa :

```bash
# on se déplace dans le dossier qui contient le sous dossier caché '.git'
cd website
git config user.name "Mona Lisa"
git config user.email "mona.lisa@devinci.com"
```

### Mettre à jour son dépôt local

Vérifier que votre dépôt local (sur votre ordinateur) soit à jour par rapport au dépôt central (sur GitHub) :

```bash
$ git status
Sur la branche master
Votre branche est à jour avec 'origin/master'.

rien à valider, la copie de travail est propre
```

Si la commande `git status` ne vous renvoie pas le même genre de message qu'au-dessus, cela signifie que vous n'êtes pas à jour. Il faut alors faire :

```bash
git pull
```

Après qu'une branche ait été fusionnée (*merged*), elle est automatiquement supprimée sur le dépôt central (hébergé sur [GitHub]) afin de garder un dépôt propre et lisible. Il faut alors mettre à jour le dépôt local sur votre machine :

=== "Debian (Bash)"
    ```bash
    git pull origin

    # mettre le dépôt local en conformité avec le dépôt central (notamment en supprimant les branches locales déjà supprimées sur GitHub)
    git remote prune origin

    # supprimer les branches qui ont été fusionnées - sauf master et gh-pages
    git branch --merged | grep -i -v -E "master|gh-pages"| xargs git branch -d

    # supprimer les branches qui n'existent plus sur GitHub
    git fetch --prune && git branch -v | grep -i -E "\[disparue|gone\]" | grep -v -E "\*|master|main|gh-pages" | awk '{print $1}' | xargs git branch -D
    ```

=== "Windows (Powershell)"
    ```powershell
    git pull origin

    # mettre le dépôt local en conformité avec le dépôt central (notamment en supprimant les branches locales déjà supprimées sur GitHub)
    git remote prune origin

    # supprimer les branches qui ont été fusionnées - sauf master et gh-pages
    git branch --merged | Select-String -Pattern '^(?!.*(master|gh-pages)).*$' | ForEach-Object { git branch -d $_.ToString().Trim() }

    # ou en ouvrant une fenêtre de sélection des branches à supprimer
    git branch --format "%(refname:short)" --merged  | Out-GridView -PassThru | % { git branch -d $_ }
    ```

----

## Python

![logo Python](https://cdn.geotribu.fr/img/logos-icones/programmation/python.png "logo Python"){: .img-rdp-news-thumb }

Pour éditer localement et visualiser le résultat final avant de publier sur le dépôt, il faut installer [Python] 3.7 ou supérieure et les dépendances du projet.

### Installation de Python

=== "Debian (Bash)"
    ```bash
    # lister les versions de Python installées
    ls -1 /usr/bin/python* | grep '[2-3].[0-9]$'

    # si aucune version de Python >= 3.7 n'est installée, installons la 3.8 par exemple
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt update
    sudo apt install python3.8
    ```

=== "Windows (Powershell)"
    Le mieux est encore de suivre l'article dédié :

    [Python : installation et configuration sur Windows :fontawesome-brands-windows:](/articles/2020/2020-06-19_setup_python/#installation-et-configuration){: .md-button }
    {: align=middle }

### Création de l'environnement de travail

Pour travailler tranquillement sans risquer de casser quoi que ce soit dans l'installation de Python au niveau du système, on préfère utiliser un environnement virtuel.

=== "Debian (Bash)"
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
    Si ça n'est pas encore fait, il faut [autoriser l'utilisation des environnements virtuels](/articles/2020/2020-06-19_setup_python/#autoriser-lutilisation-des-environnements-virtuels).  
    Puis :

    ```powershell
    # se rendre à la racine du dépôt local - adapter au dossier dans lequel vous avez cloné le dépôt
    cd ~/git-repos/geotribu/website/

    # lister les versions de Python installées
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

![logo pre-commit](https://cdn.geotribu.fr/img/logos-icones/programmation/precommit.png "logo pre-commit"){: .img-rdp-news-thumb }

Le projet vient avec une [configuration](https://github.com/geotribu/website/blob/master/.pre-commit-config.yaml) pour [pre-commit], qui permet d'appliquer des scripts (des [*git hooks*](https://git-scm.com/book/fr/v2/Personnalisation-de-Git-Crochets-Git)) de vérification et de nettoyage des fichiers avant qu'ils ne soit enregistrés dans le dépôt (d'où le nom).

L'installation est optionnelle mais recommandée car l'outil garantit :

- un socle minimal de qualité des contenus et codes sources
- une cohérence d'ensemble entre les contributions
- qu'une fois poussée sur le dépôt central, la contribution passe [les checks exécutés dans la CI](https://results.pre-commit.ci/repo/github/248722492).

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

## Mkdocs

![icône générateur de site web statique](https://cdn.geotribu.fr/img/logos-icones/divers/web_static_generator.webp "icône générateur de site web statique"){: .img-rdp-news-thumb }

C'est l'outil qui sert à générer le site web à partir des contenus rédigés en [markdown] et configuré dans le fichier `mkdocs.yml` et dérivés. Voici quelques bases pour l'utiliser... qui ne vous épargnent pas le droit de regarder l'aide `mkdocs --help` :wink:.

### Différentes configurations

Depuis la rentrée 2021, Geotribu sponsorise le thème [Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/insiders/) afin de pérenniser  le projet et tirer parti des fonctionnalités réservées aux financeurs. La clé de licence (en fait, un *token* GitHub lié au compte de Julien) devant rester secrète, nous gérons donc plusieurs fichiers de configuration afin de pouvoir s'adapter aux différents cas.

| Fichier | Fonctionnalités payantes | Complet | Commentaire |
| :------ | :-----: | :-----: | :---------- |
| `mkdocs.yml`         | **X** | **X** | Configuration complète utilisée pour le site en production. Utilisé par défaut. |
| `mkdocs-free.yml`    |       | **X** | Configuration sans les fonctioannlités payantes (tags, etc.) |
| `mkdocs-minimal.yml` |       |       | Configuration minimaliste qui n'active qu'un minimum de plugins et d'extensions pour obtenir de meilleures performances lors de l'édition en local. |

### Générer le site web

Version complète :

```bash
mkdocs build
```

Version complète gratuite :

```bash
mkdocs build -f mkdocs-free.yml
```

Version minimale :

```bash
mkdocs build --config-file mkdocs-minimal.yml
```

Le site généré est dans le répertoire : `{{ config.site_dir }}`.

### Avoir un rendu local mis à jour selon les modifications

Pour voir les changements en local sans les pousser sur le dépôt central, il est possible de servir le site et qu'il se recharge automatiquement quand on modifie les fichiers :

Version complète :

```bash
# regénération complète
mkdocs serve
# regénération rapide
mkdocs serve --dirtyreload
```

Version complète gratuite :

```bash
# regénération complète
mkdocs serve -f mkdocs-free.yml --dirtyreload
# regénération rapide
mkdocs serve --config-file mkdocs-free.yml --dirtyreload
```

Version minimale :

```bash
# regénération complète
mkdocs serve --config-file mkdocs-minimal.yml
# regénération rapide
mkdocs serve --config-file mkdocs-minimal.yml --dirtyreload
```

Par défaut, le site est accessible sur <http://localhost:8000> mais il est possible de spécifier le port à utiliser : `mkdocs serve -a localhost:8085`.

----

## Docker

![logo Docker](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/docker.png "logo Docker"){: .img-rdp-news-thumb }

Il est également possible d'utiliser Docker. L'avantage est que c'est alors la seule dépendance à installer (plus besoin de Python, NodeJS ou même de Git si vous téléchargez le dépôt). L'inconvénient est que c'est assez lourd pour un site qui se veut léger :wink: !

```bash
docker-compose -f "docker-compose-mkdocs.dev.yml" up --build
```

Le site est alors accessible sur : <http://0.0.0.0:8000>
