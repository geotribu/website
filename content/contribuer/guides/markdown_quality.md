---
title: "Rédiger en Markdown : guide des régles de rédaction applicables à Geotribu."
categories:
    - article
    - contribution
date: 2020-09-14 14:20
description: "Rédiger en Markdown : règles partagées, erreurs fréquentes et mécanismes de validation."
image: "https://cdn.geotribu.fr/img/internal/contribution/markdown_quick_exemple_rendu.png"
robots: index, follow
tags:
    - contribuer
    - HTML
    - Markdown
    - Python
    - rédaction
---

# Rédiger en Markdown : règles et enjeux de qualité

Le _[markdown]_ est une syntaxe extensible et son rendu dépend de l'outil utilisé pour l'implémenter et générer le HTML. Il existe donc des différences entre le rendu :

- dans l'onglet `Preview` de [GitLab],
- celui dans un éditeur de texte ([Visual Studio Code], Sublime Text, HackMD, Hedgedoc, vim...
- celui de l'outil utilisé pour le rendu final [MkDocs / Material](https://squidfunk.github.io/mkdocs-material/).

C'est **ce dernier qui fait foi**. Cette page recense les principes de la rédaction pour Geotribu.

!!! info "En savoir plus"
    Consulter [l'article "Comprendre le rendu Markdown"](/contribuer/build_site/markdown_engine/#specificites).

## Règles

La syntaxe est encadrée par un ensemble de règles :

- [règles de référence](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md)
- [règles configurées dans Geotribu]({{ config.repo_url }}/blob/master/.markdownlint.json)

Quelques règles de base sont listées ci-dessous, notamment celles pour lesquelles il ya  fréquemment des erreurs :

### Unicité du titre de niveau 1

Le Markdown étant destiné à être du HTML, il ne peut y avoir qu'un titre de niveau 1 défini par balise `#`. Il peut y avoir un titre alternatif défini dans l'en-tête via la clé `title:`.

### Cohérence du caractère pour les listes à puces

S'il est techniquement possible d'utiliser différents caractères, il est préférable d'utiliser le même caractère (généralement l'astérisque ou le tiret) et a minima le style doit être cohérent dans une même page.

Dans cet exemple, des astérisques (`*`) ont été utilisés après que des tirets (`-`) l'aient déjà été pour le même niveau de puces.

![erreur style puces](https://cdn.geotribu.fr/img/internal/contribution/markdown/markdown_error_list_style_lizmap..png "Signalement de l'erreur dans Visual Studio Code"){: .img-center loading=lazy }

> Référence : [MD004 - Unordered list style](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md)

### Sauts de ligne et lignes vides

En markdown, selon les implémentations, il est important de laisser des lignes vides entre les différents paragraphes (ou ce qui deviendra une balise HTML différente une fois converti). Par exemple :

- entre le texte et le début d'une liste (ordonnée ou pas)
- entre un titre et un paragraphe
- entre une image et un texte

Par exemple, si on n'insère pas de ligne vide entre le paragraphe et le premier élément d'une liste à puces, le rendu ne fonctionnera pas :

<!-- markdownlint-disable MD046 -->
=== "Markdown"

    ```markdown
    Lizmap est un ensemble de composants logiciels permettant de publier facilement et rapidement un projet QGIS sur le Web. Lizmap se décompose en :
    * une extension QGIS permettant de paramétrer le rendu final sur le web
    * une application web permettant notamment d'afficher les projets configurés et gérer les utilisateurs
    ```

=== "Rendu"

    ![capture liste à puces](https://cdn.geotribu.fr/img/internal/contribution/markdown/markdown_list_broken.png "Rendu de la liste à puces cassé"){: .img-center loading=lazy }
<!-- markdownlint-enable MD046 -->

> Référence : [MD032 - Lists should be surrounded by blank lines](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md032---lists-should-be-surrounded-by-blank-lines)


### Déclaration explicite des liens hypertextes

Si la plupart des outils repèrent les liens dans le texte, il est recommandé de les déclarer explicitement, notamment si le document est destiné à être intégré dans un format plus exigeant en termes de formatage (mail, etc.).

> Référence : [régle MD 34](https://github.com/DavidAnson/markdownlint/blob/v0.25.1/doc/Rules.md#md034)

<!-- markdownlint-disable MD034 -->
=== "Markdown"
    ```markdown
    - pas bien : https://oslandia.com/
    - bien : <https://oslandia.com/>
    - encore mieux : [texte du lien qui apparaît](https://oslandia.com/)
    ```

=== "Rendu"
    - pas bien : https://oslandia.com/
    - bien : <https://oslandia.com/>
    - bien : [texte du lien qui apparaît](https://oslandia.com/)
<!-- markdownlint-enableMD034 -->

----

## Outillage

### Utiliser les git hooks

Afin de garantir un minimum de qualité entre les différentes contributions, une série de _git hooks_ (à travers l'outil [pre-commit](https://pre-commit.com/)) est disponible. Pour les installer, il faut disposer de Python puis :

```bash
# installer pre-commit
pip install -U pre-commit
# installer les git hooks
pre-commit install
```

Le vérificateur de la syntaxe Markdown (markdownlint-cli, voir ci-dessous) est d'ailleurs configuré.

!!! tip "Astuce dont il ne faut pas abuser"
    Pour committer en outre-passant les git hooks ajouter l'option `--no-verify` à la commande `git commit`.

### Vérifier la syntaxe avec markdownlint-cli

On utilise [l'outil en ligne de commande développé en _node_](https://github.com/igorshubovych/markdownlint-cli) :

```bash
# installation du package
yarn add markdownlint-cli --dev --non-interactive --no-lockfile --prefer-offline

# vérification des contenus
yarn markdownlint "content/**/*.md"

# auto-correction des problèmes mineurs
yarn markdownlint --fix "content/**/*.md"
```

Il est aussi possible d'utiliser markdownlint sous forme d'[extension dans Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) et probablement dans d'autres IDE.
