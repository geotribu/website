---
Title: Prérequis pour la contribution
Category: contribution
Date: 2020-03-20 10:20
Tags: contribuer, compétences, outils
---

# Prérequis

## Compte GitHub

Le site (sources et contenu) sont hébergés sur Github : <https://github.com/geotribu/website>.

Pas de compte, pas de contribution : <https://github.com/join>.

## Markdown

La rédaction de contenu requiert la maîtrise de la syntaxe _[markdown]_.

!!! warning
    Le _[markdown]_ est une syntaxe extensible et son rendu dépend de l'outil utilisé pour l'implémenter. Il existe donc des différences entre le rendu dans l'onglet `Preview` de [GitHub], celui dans un éditeur [Visual Studio Code] et celui de l'outil utilisé pour le rendu final [MkDocs / Material].

    C'est bien le dernier qui fait foi, d'où l'intérêt de travailler en local.

## Logiciels

### Python

Pour éditer localement et visualiser le résultat final avant de publier sur le dépôt, il faut installer [Python] 3.7+ et installer les dépendances :

```powershell
# se rendre à la racine du dépôt local - adapter à son environnement
cd ~/git-repos/geotribu/website/
# créer un environnement virtuel
python -m venv .venv
# installer les dépendances
python -m pip install -U -r requirements.txt

# servir le site avec mkdocs
cd src/mkdocs
mkdocs serve
```

Le site est accessible sur : <http://locahost:8000>

### Docker

Il est possible de se passer de Python en utilisant Docker.

```bash
docker-compose -f "docker-compose-mkdocs.dev.yml" up --build
```

Le site est accessible sur : <http://locahost:8000>

<!-- Hyperlinks reference -->
[Git]: https://git-scm.com/download/win
[GitHub Desktop]: https://desktop.github.com/
[GitHub]: https://help.github.com/en/github/writing-on-github
[markdown]: https://fr.wikipedia.org/wiki/Markdown
[MkDocs / Material]: https://squidfunk.github.io/mkdocs-material/specimen/
[Python]: http://help.isogeo.com/development-guidelines/languages/python/
[StackEdit]: https://stackedit.io/
[Visual Studio Code]: https://github.com/DavidAnson/vscode-markdownlint#intro
