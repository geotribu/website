---
Title: Prérequis pour la contribution
Category: contribution
Date: 2020-03-20 10:20
Tags: contribuer, markdown, git, team, compétences, outils
---

# Prérequis

## Globalement

### Compte GitHub

Le site (sources et contenu) sont hébergés sur Github : <https://github.com/geotribu/website>.

Pas de compte, pas de contribution : <https://github.com/join>.

### Markdown

La rédaction de contenu requiert la maîtrise de la syntaxe _[markdown]_ qui permet de rédiger du contenu en utilisant des caractères compatibles avec les balises HTML tout en permettant de nombreuses choses (liste non exhaustive) :

- niveaux de titres
- listes à puces (numérotées ou pas)
- images
- vidéos, via le support limité d'iFrame
- tableaux
- insertion de code

Il y a également certaines limites (dimensionnement ou alignement des images par exemple) mais qui sont parfois comblées soit par des [extensions](https://squidfunk.github.io/mkdocs-material/extensions/pymdown/) de la syntaxe de base (exemple d'[**attr_list**](https://python-markdown.github.io/extensions/attr_list/) qui permet d'ajouter des balises de style), soit par d'autres langages (CSS, HTML...).

!!! warning
    Le _[markdown]_ est une syntaxe extensible et son rendu dépend de l'outil utilisé pour l'implémenter. Il existe donc des différences entre le rendu :

    - dans l'onglet `Preview` de [GitHub],
    - celui dans un éditeur [Visual Studio Code]
    - celui de l'outil utilisé pour le rendu final [MkDocs / Material].

    C'est ce dernier qui fait foi, d'où l'intérêt de travailler en local.

Ressources :

- la page "spécimen" de [Mkdocs / Material]
- [astuces de rédaction spécifiques à MkDocs / Material (en)](https://yakworks.github.io/mkdocs-material-components/cheat-sheet/)
- le [markdown dans Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)

## Edition locale

### Git

La mise en ligne du contenu se fait via [Git]. Si vous n'êtes pas à l'aise avec la ligne de commande, il est possible d'utiliser [GitHub Desktop].

Cloner le dépôt, soit avec la commande ci-dessous, soit via [le bouton vert sur le dépôt avec GitHub Desktop](https://github.com/geotribu/website) :

```bash
cd ~/git-repos/geotribu/
git clone https://github.com/geotribu/website.git
```

### Python

Pour éditer localement et visualiser le résultat final avant de publier sur le dépôt, il faut installer [Python] 3.7+, les dépendances :

=== "Bash"

    ```bash
    # se rendre à la racine du dépôt local - adapter à son environnement
    cd ~/git-repos/geotribu/website/

    # créer un environnement virtuel
    virtualenv -p /usr/bin/python3.7 .venv
    source .venv/bin/activate

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

    # créer un environnement virtuel
    py -3.7 -m venv .venv   # attention ne fonctionne pas avec Python installé depuis le Windows Store

    # installer les dépendances
    python -m pip install -U -r requirements.txt
    ```

### Servir en local

Puis de lancer la commande qui lance le site en local avec rechargement automatique :

```shell
# servir le site avec mkdocs
mkdocs serve -f src/mkdocs/mkdocs.yml

# il existe aussi un mode où le rechargement ne concerne que la page modifiée
mkdocs serve -f src/mkdocs/mkdocs.yml --dirtyreload
```

Le site est accessible sur : <http://localhost:8000>

#### Docker

Il est possible de se passer de Python en utilisant Docker.

```bash
docker-compose -f "docker-compose-mkdocs.dev.yml" up --build
```

Le site est accessible sur : <http://localhost:8000>

<!-- Hyperlinks reference -->
[Git]: https://git-scm.com/download/
[GitHub Desktop]: https://desktop.github.com/
[GitHub]: https://help.github.com/en/github/writing-on-github
[markdown]: https://fr.wikipedia.org/wiki/Markdown
[MkDocs / Material]: https://squidfunk.github.io/mkdocs-material/specimen/
[Python]: http://help.isogeo.com/development-guidelines/languages/python/
[StackEdit]: https://stackedit.io/
[Visual Studio Code]: https://github.com/DavidAnson/vscode-markdownlint#intro
