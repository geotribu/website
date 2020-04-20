---
Title: Prérequis pour la contribution
Category: contribution
Date: 2020-03-20 10:20
Tags: contribuer,requirement,markdown,github
---

# Prérequis

## Compte GitHub

Le site (sources et contenu) sont hébergés sur Github : <https://github.com/geotribu/website>.

Pas de compte, pas de contribution : <https://github.com/join>.

## Markdown

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

<!-- Hyperlinks reference -->
[Git]: https://git-scm.com/download/
[GitHub Desktop]: https://desktop.github.com/
[GitHub]: https://help.github.com/en/github/writing-on-github
[markdown]: https://fr.wikipedia.org/wiki/Markdown
[MkDocs / Material]: https://squidfunk.github.io/mkdocs-material/specimen/
[Python]: http://help.isogeo.com/development-guidelines/languages/python/
[StackEdit]: https://stackedit.io/
[Visual Studio Code]: https://github.com/DavidAnson/vscode-markdownlint#intro
