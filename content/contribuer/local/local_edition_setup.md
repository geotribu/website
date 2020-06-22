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

----

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
mkdocs serve -f mkdocs.yml

# il existe aussi un mode où le rechargement automatique est plus rapide mais ne concerne que la page modifiée
mkdocs serve -f mkdocs.yml --dirtyreload
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
[pre-commit]: https://pre-commit.com/
[Python]: https://docs.python.org/fr/3/tutorial/
[StackEdit]: https://stackedit.io/
[Visual Studio Code]: https://github.com/DavidAnson/vscode-markdownlint#intro
