# Installation pour l'édition locale

!!! tip
    Remplir d'abord [les prérequis](../../requirements).

## Git

La mise en ligne du contenu se fait via [Git]. Si vous n'êtes pas à l'aise avec la ligne de commande, il est possible d'utiliser [GitHub Desktop].

Cloner le dépôt, soit avec la commande ci-dessous, soit via [le bouton vert sur le dépôt avec GitHub Desktop](https://github.com/geotribu/website) :

```bash
cd ~/git-repos/geotribu/
git clone https://github.com/geotribu/website.git
```

## Python

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

    # activer l'environnement virtuel
    .\.venv\Scripts\activate

    # mettre à jour pip
    python -m pip install -U pip

    # installer les dépendances
    python -m pip install -U -r requirements.txt
    ```

## Servir en local

Puis de lancer la commande qui lance le site en local avec rechargement automatique :

```bash
# servir le site avec mkdocs
mkdocs serve -f src/mkdocs/mkdocs.yml

# il existe aussi un mode où le rechargement automatique est plus rapide mais ne concerne que la page modifiée
mkdocs serve -f src/mkdocs/mkdocs.yml --dirtyreload
```

Le site est accessible sur : <http://localhost:8000>

----

### Docker

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
