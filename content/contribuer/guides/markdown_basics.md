---
title: "Rédiger en Markdown : bases et spécimen"
categories:
    - article
    - contribution
    - tutoriel
date: 2020-09-14 14:20
description: "Maîtriser les bases de la rédaction en Markdown pour contribuer à Geotribu et exemples de mise en forme."
image: "https://cdn.geotribu.fr/img/internal/contribution/markdown_quick_exemple_rendu.png"
tags:
    - contribuer
    - HTML
    - lint
    - Markdown
    - rédaction
    - Python
    - tutoriel
# theme customizations
search:
  exclude: true
---

# Les bases de rédaction en Markdown

## Ressources

Compte-tenu de la popularité du [Markdown], inutile de réinventer la roue, autant pointer vers les bonnes ressources déjà disponibles en ligne :

### La syntaxe

Le _[markdown]_ est une syntaxe extensible et son rendu dépend de l'outil utilisé pour l'implémenter. Il existe donc des différences entre le rendu :

- dans l'onglet `Preview` de [GitHub],
- celui dans un éditeur de texte ([Visual Studio Code], Sublime Text, HackMD, Hedgedoc...)
- celui de l'outil utilisé pour le rendu final [MkDocs / Material](https://squidfunk.github.io/mkdocs-material/).

C'est **ce dernier qui fait foi**.

!!! tip
    Pour comprendre comment fonctionne le rendu des contenus, consulter [l'article dédié](/contribuer/internal/markdown_engine/).

#### Bien démarrer

- [rédiger en Markdown (OpenClassrooms)](https://openclassrooms.com/fr/courses/1304236-redigez-en-markdown/)
- [un guide pour bien commencer avec Markdown](https://blog.wax-o.com/2014/04/tutoriel-un-guide-pour-bien-commencer-avec-markdown/)
- [Mastering Markdown (GitHub)](https://guides.github.com/features/mastering-markdown/)

#### Aller plus loin

- [utiliser des blocs stylés](https://squidfunk.github.io/mkdocs-material/reference/admonitions/)
- [insérer du code](https://squidfunk.github.io/mkdocs-material/reference/code-blocks/)

### Editeurs

N'importe quel éditeur de texte suffit pour rédiger en [Markdown]. Ci-dessous, voici une liste très loin d'être exhaustive d'outils permettant de rédiger en Markdown.

#### Bureautique

- [Mark Text](https://github.com/marktext/marktext#download-and-installation)
- [Sublime Text](https://putaindecode.io/articles/sublime-text-en-tant-qu-editeur-markdown/)
- [Visual Studio Code](https://code.visualstudio.com/docs/languages/markdown)

#### En ligne

- [GitHub](https://docs.github.com/en/github/writing-on-github)
- [StackEdit]
- [Upmath]

!!! tip
    Le choix du Markdown pour Geotribu a été détaillé dans l'article [Du HTML au Markdown (et vice-versa)](/articles/2020/2020-09-11_html2markdown/). Il contient quelques éléments de compréhension sur la syntaxe et un petit TP pour s'exercer.

[Prochaine étape : respecter et valider la syntaxe :fontawesome-solid-forward:](/contribuer/guides/markdown_quality/){: .md-button }
{: align=middle }

----

## Spécimen

En plus des ressources, à suivre quelques exemples de base.

### Titres et paragraphes

<!-- markdownlint-disable MD046 -->
=== "Markdown"

    ```markdown
    # Titre de niveau 1

    Le titre de niveau 1 est le titre principal. Il doit être unique.

    ## De l'importance des sauts de ligne

    En Markdown, les sauts de ligne font foi. Avant d'entamer le paragraphe, il faut sauter une ligne. De même entre deux paragraphes, il faut laisser une ligne vide.
    ```

=== "Rendu"

    # Titre de niveau 1

    Le titre de niveau 1 est le titre principal. Il doit être unique.

    ## De l'importance des sauts de ligne

    En Markdown, les sauts de ligne font foi. Avant d'entamer le paragraphe, il faut sauter une ligne. De même entre deux paragraphes, il faut laisser une ligne vide.

### Mise en forme

=== "Markdown"

    ```markdown
    Pour mettre en forme le texte, c'est facile. Il s'agit surtout de se souvenir que les retours à ligne et les retraits font loi dans la syntaxe.

    Mettre un texte en italique avec une *astérisque*
    ou un _underscores (autrement appelés tiret du 8)_ de chaque côté.

    Mettre un texte en gras avec deux **astérisques**
    ou deux __underscores (autrement appelés tiret du 8)__ de chaque côté.

    Barrer un texte avec deux ~~tildes~~ de chaque côté.

    Combiner les différents styles est possible. Ainsi on peut obtenir un texte en italique, un texte en italique et gras, un texte en italique et barré avec : un _underscore, **deux astérisques** et ~~deux tildes~~_.
    ```

=== "Rendu"

    Pour mettre en forme le texte, c'est facile. Il s'agit surtout de se souvenir que les retours à ligne et les retraits font loi dans la syntaxe.

    Mettre un texte en italique avec une *astérisque*
    ou un _underscores (autrement appelés tiret du 8)_ de chaque côté.

    Mettre un texte en gras avec deux **astérisques**
    ou deux __underscores (autrement appelés tiret du 8)__ de chaque côté.

    Barrer un texte avec deux ~~tildes~~ de chaque côté.

    Combiner les différents styles est possible. Ainsi on peut obtenir un texte en italique, un texte en italique et gras, un texte en italique et barré avec : un _underscore, **deux astérisques** et ~~deux tildes~~_.

### Listes à puces

=== "Markdown"

    ```markdown
    Liste numérotée à plusieurs niveaux :

    1. premier élément de la liste
    2. deuxième élément de la liste
        1. indenter avec 4 espaces avant le chiffre permet de faire des sous-listes imbriquées
        2. deuxième élément de second niveau
    3. troisième élément de la liste de 1er niveau qui contient une sous-liste non ordonnée :
        * hip,
        * hop,

    Ou sans numéros :

    * on peut créer des puces avec différents caractères :
        * astérisque,
        - tiret
        + signe plus (\+)
    * mais, pour éviter les effets de bord (espacement de paragraphe, mauvais niveau de retrait...) et selon les règles établies, il est préférable de rester cohérent dans le caractère utilisé, au moins dans un même document
    * en général, on utilise l'astérisque ou alors le tiret.
    ```

=== "Rendu"

    Liste numérotée à plusieurs niveaux :

    1. premier élément de la liste
    2. deuxième élément de la liste
        1. indenter avec 4 espaces avant le chiffre permet de faire des sous-listes imbriquées
        2. deuxième élément de second niveau
    3. troisième élément de la liste de 1er niveau qui contient une sous-liste non ordonnée :
        * hip,
        * hop,

    Ou sans numéros :

    * on peut créer des puces avec différents caractères :
        * astérisque,
        - tiret
        + signe plus (\+)
    * mais, pour éviter les effets de bord (espacement de paragraphe, mauvais niveau de retrait...) et selon les règles établies, il est préférable de rester cohérent dans le caractère utilisé, au moins dans un même document
    * en général, on utilise l'astérisque ou alors le tiret.
<!-- markdownlint-enable MD046 -->

[Prochaine étape : respecter et valider la syntaxe :fontawesome-solid-forward:](/contribuer/guides/markdown_quality/){: .md-button }
{: align=middle }

<!-- Hyperlinks references -->
[Markdown]: https://daringfireball.net/projects/markdown/
[syntaxe]: https://daringfireball.net/projects/markdown/syntax
