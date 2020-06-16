---
title: "Python - Configuration sur Windows et outillage"
authors: Julien Moura
category: article
date: 2020-06-19 10:20
description: "Ma configuration et mon outillage pour Python en 2020."
hero: "Configuration de Python sous Windows et outillage de base."
tags: python,tooling,setup
---

# Python : configuration sur Windows et outillage

:calendar: Date de publication initiale : 19 juin 2020

**Mots-clés :** Python

Je travaille beaucoup avec Python sur Windows depuis quelques années. En comparaison avec des distributions Linux comme Debian où l'interpréteur est intégré au système (ce qui peut poser d'autres problèmes), cela a toujours été plus compliqué de se faire un environnement de travail confortable.
Avec le changement de braquet de la firme de Redmond par rapport à l'open source, les choses se sont grandement améliorées ces dernières années.

Ceci dit, cela fait toujours du bien de se noter quelque part les méthodes et étapes à ne pas oublier pour être rapidement confortable et efficace.

## Installation et configuration

### Modalités

Sur Windows, Python peut être installé de plusieurs manières :

* via les [installateurs traditionnels](https://www.python.org/downloads/windows/) : ça reste la meilleure option d'après moi
* via [Chocolatey](https://chocolatey.org/packages?q=python&moderatorQueue=&moderationStatus=all-statuses&prerelease=false&sortOrder=relevance) avec un simple `choco install python`
* via [le Windows Store](https://docs.python.org/fr/3/using/windows.html#the-microsoft-store-package) : pratique pour le déployer chez des utilisateurs mais il y a certaines limites bloquantes pour les usages avancés
* via [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/windows.html) : un peu _bourrin_ mais très pratique lorsque l'on travaille sur des thématiques de traitement scientifique
* via [_nuget_](https://docs.python.org/fr/3/using/windows.html#the-nuget-org-packages)
* bientôt via [winget](https://winstall.app/apps/Python.Python) : `winget install python`

### Activer les chemins de fichiers longs

Cette [limitation de longueur de chemin](https://docs.microsoft.com/fr-fr/windows/win32/fileio/naming-a-file?redirectedfrom=MSDN#maximum-path-length-limitation) a longtemps complexifié les développements et rendu fou/lles quelques développeur/ses (bon et, soyons bon joueur, aussi forcé les utilisateurs à une certaine forme de bonne pratique dans le nommage) !

Désormais c'est assez facile de réduire le risque d'AVC :

* soit en cochant l’option dans l’installateur Python
* soit en suivant [cette procédure](https://docs.python.org/fr/3/using/windows.html#removing-the-max-path-limitation) (ou [ici](https://www.it-connect.fr/windows-10-comment-activer-la-gestion-des-chemins-trop-long/))

![Installateur Python - Option pour les chemins longs](https://cdn.geotribu.fr/img/tuto/python_windows/python_windows_installer_path_length.jpg)

### Ajouter Python au PATH

De même, c'est désormais très bien géré :

* soit en cochant l’option dans l’installateur Python
* soit en ajoutant manuellement les chemins vers le dossier d'installation et le sous-dossier `Scripts`

Lorsque plusieurs versions sont installées, [utiliser le lanceur](#utiliser-le-launcher).

### Autoriser l’utilisation des environnements virtuels

Les environnements virtuels utilisent des scripts que Windows demande d'autoriser spécifiquement. Ouvrir Powershell en mode admin et entrer :

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

----

## Bonnes habitudes et astuces

### Utiliser Powershell

Cela peut paraître évident mais ça va mieux en le disant : **il faut arrêter avec cmd et utiliser Powershell**.
Sauf cas spécifiques (dont l'OSGeo4W...), il faut oublier `cmd` et configurer le système pour utiliser Powershell par défaut. Pourquoi ? Mais parce-que :

* `cmd` ne tient pas compte de toutes les subtilités apportées par les versions récentes du système (encodage, chemins,)
* certaines commandes `bash` sont prises en compte : `ls`, `rm`, `mkdir`...
* les chemins sont compris, quel que soit le séparateur utilisé : `/` ou `\`
* autocomplétion, modules, coloration, etc.

Et puis on ne peut décemment pas utiliser un outil désormais [daté au carbone 14](https://fr.wikipedia.org/wiki/Datation_par_le_carbone_14) et s'en servir pour pester contre le système. Donc utiliser Powershell permet de râler en toute honnêteté (la bonne foi n'est jamais obligatoire) sur Windows. Et il ne faut pas s'inquiéter, il y a encore largement de quoi :wink: !

### Utiliser le launcher

L'installation de plusieurs versions de Python finit toujours par arriver, notamment pour s'adapter aux différentes intégrations logicielles.

S'il est bien sûr possible de créer des profils pour Powershell à la manière d'un `.bashrc`, le lanceur intégré lors de l'installation de Python permet de gérer facilement les différentes versions. Un peu à la manière d'un [`update-alternatives`](https://manpages.debian.org/stretch/dpkg/update-alternatives.1) mais, à mon sens en tout cas, avec une meilleure flexibilité à l'usage.

Lister les versions installées :

```powershell
PS C:\Users\ingeoveritas> py --list
Installed Pythons found by C:\WINDOWS\py.exe Launcher for Windows
 -3.8-64 *
 -3.7-64
```

Mettre à jour `pip` pour une version en particulier :

```powershell
py -3.7 -m pip install -U pip
```

### Environnements virtuels

Les environnements virtuels (_virtual environment_) sont un des fondamentaux du développement en Python, car ils permettent de garantir l'isolation des dépendances (et leurs versions) entre les différents projets.

Tout développement, sur un projet nouveau ou existant, commence donc plus ou moins ar ces commandes :

```powershell
# créer l'environnement virtuel
py -3.7 -m venv .venv
# l'activer / y entrer
.venv/Scripts/activate
# MAJ pip, setuptools et wheel
python -m pip install -U pip setuptools wheel
# installer les prérequis
python -m pip install -U -r .\requirements.txt
```

Pour le développement d'un package, installer le projet en cours en mode éditable ([voir documentation officielle](https://pip.pypa.io/en/stable/reference/pip_install/#editable-installs))) :

```powershell
python -m pip install -e .
```

!!! info
    De nombreuses ressources existent en ligne :

    * [tutoriel dans la documentation officielle](https://docs.python.org/fr/3/tutorial/venv.html)
    * [configurer son environnement virtuel (Google)](https://cloud.google.com/python/setup?hl=fr#installing_and_using_virtualenv)
    * [prise en main de Python sur Windows pour les débutants](https://docs.microsoft.com/fr-fr/windows/python/beginners)

### Documentation _in-code_

Python est un langage qui se documente facilement avec les _docstrings_, utilisables par d'autres outils : IDE, génération de documentation en ligne (HTML) ou statique (PDF), etc.

!!! tip
    [L'extension Python Docstring Generator pour Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring) permet de générer automatiquement une structure type de docstring pour les fonctions, mais attention elle demande un fichier de cofniguration pour s'adapter à la convention utilisée à . Exemple ci-dessous d'un fichier `docstring-config.mustache` (généralement stocké dans le dossier `.vscode`) :

        {{! Sphinx Docstring Template }}
        {{summaryPlaceholder}}

        {{#parametersExist}}
        {{#args}}
        :param {{typePlaceholder}} {{var}}: {{descriptionPlaceholder}}
        {{/args}}
        {{#kwargs}}
        :param {{typePlaceholder}} {{var}}: {{descriptionPlaceholder}}. Defaults to: {{&default}} - optional
        {{/kwargs}}
        {{/parametersExist}}

        {{#exceptionsExist}}
        {{#exceptions}}
        :raises {{type}}: {{descriptionPlaceholder}}
        {{/exceptions}}
        {{/exceptionsExist}}

        {{#returnsExist}}
        {{#returns}}
        :return: {{descriptionPlaceholder}}
        :rtype: {{typePlaceholder}}
        {{/returns}}
        {{/returnsExist}}

        :example:

        .. code-block:: python

            # here comes an example in Python

### Tests

En Python, le code est généralement assez simple à tester, compte-tenu de l'orientation serveur / objet / fonctionnel du langage.

Les fichiers de tests sont :

* préfixés par le mot `test`
* stockés dans un sous-dossier `tests`

La configuration de `pytest` est gérée dans la section `[tool:pytest]` du fichier `setup.cfg` de chaque projet.

----

## Outillage

### La base

* [black](https://twine.readthedocs.io/en/latest/) : formatage et homogénéisation du code automatisés
* [flake8](https://flake8.pycqa.org) : analyse statique de code (_[linter](https://fr.wikipedia.org/wiki/Lint_(logiciel))_) qui permet de lever des incohérences ou des problèmes dans le code
* [setuptools](https://setuptools.readthedocs.io/en/latest/) : packaging et installation de dépendances
* [twine](https://twine.readthedocs.io/en/latest/) : publication sur PyPi
* [wheel](https://pythonwheels.com/) : packaging et installation de dépendances

### Protagonistes

* [click](https://palletsprojects.com/p/click/) : framework pour créer des outils en ligne de commande
* [PyInstaller](https://github.com/pyinstaller/pyinstaller/) : transforme les projets Python en exécutable (compatible avec la plateforme sur lequel il est utilisé)
* [requests](https://requests.readthedocs.io/en/master/) : requêtes HTTP/S faciles, à la base du SDK . Cependant, évolue peu donc envisager d'autres options : [httpx](https://www.python-httpx.org/).

### Seconds rôles

* [docx-tpl](https://docxtpl.readthedocs.io/en/latest/) : écriture de fichiers Word à l'aide de templates Jinja2
* [OpenPyXl](https://openpyxl.readthedocs.io/) : lecture/écriture de fichiers Excel
* [peewee](https://peewee.readthedocs.io/) : [ORM](https://fr.wikipedia.org/wiki/Mapping_objet-relationnel) SQL très léger et efficace (utilisé par [Flask](https://www.palletsprojects.com/p/flask/) par exemple)
* [pipenv](https://pipenv.kennethreitz.org/en/latest/) : gestion du workflow de développement (environnements virtuels, dépendances…). Optionnel, sans besoin spécifique, se contenter de `pip`. Envisager aussi [poetry](https://python-poetry.org/)
* [PyQt](https://www.riverbankcomputing.com/software/pyqt/intro) : bindings Python du framework d'interface graphique et tout le reste (réseau, _threads_, etc.)
* [pytest](https://docs.pytest.org/) : framework de tests.
* [python-dotenv](https://saurabh-kumar.com/python-dotenv/) : lecture/écriture de fichiers de configuration au format `.env`
* [requests-oauthlib](https://requests-oauthlib.readthedocs.io/) : outillage pour gérer les différents scénarios oAuth2 (basé sur `requests`)
* [sphinx](https://www.sphinx-doc.org/en/master/) : générateur de documentations rédigées en `.rst` dans différents formats (PDF? epub, HTML). Utilisé pour générer les docs en ligne à partir du code, par exemple avec Read The Docs. Beaucoup d'extensions, notamment :

### Figurants

* [LXML](https://lxml.de/) : outillage complet pour le XML et autres langages balisés (HTML...)
* [pre-commit](https://pre-commit.com/) : automatisation de certaines tâches liées à des étapes du [flow git](/git/workflow/). Par exemple : lancer le formatage du code avec `black` au moment de `git commit`.

----

## Auteur

--8<-- "content/team/jmou.md"
