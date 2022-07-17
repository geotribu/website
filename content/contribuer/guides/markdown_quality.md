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

![logo markdown](https://cdn.geotribu.fr/img/logos-icones/markdown.png "logo Markdown"){: .img-rdp-news-thumb }

Pour rappel, la syntaxe [Markdown] a vocation à être transformée _in fine_ en HTML. Etant donné que c'est une syntaxe extensible aux multiples implémentations différentes, son rendu dépend donc de l'outil utilisé pour visualiser le résultat :

- l'onglet `Preview` de [GitHub],
- un éditeur de texte (Visual Studio Code, Sublime Text, HackMD, Hedgedoc, vim...)
- le générateur de site [MkDocs / Material](https://squidfunk.github.io/mkdocs-material/).

C'est **ce dernier qui fait foi**.

Cette page détaille les principes de la rédaction en [Markdown] pour Geotribu.

!!! info "En savoir plus"
    Consulter [l'article "Comprendre le rendu Markdown"](/contribuer/internal/markdown_engine/#specificites).

----

## Règles

La syntaxe est encadrée par un ensemble de règles :

- [règles de référence](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md)
- [règles configurées dans Geotribu]({{ config.repo_url }}/blob/master/.markdownlint.json)

Quelques règles de base sont listées ci-dessous, notamment celles pour lesquelles il y a fréquemment des erreurs.

### Unicité du titre de niveau 1

Le Markdown étant destiné à être du HTML, il ne peut y avoir qu'un titre de niveau 1 défini par balise `#`. Il peut cependant y avoir un titre alternatif défini dans [l'en-tête via la clé `title:`](/contribuer/guides/metadata_yaml_frontmatter/) et qui est utilisé dans le menu de navigation.

> Référence : [MD025 - Multiple top-level headings in the same document](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md025)

<!-- markdownlint-disable MD046 -->
=== "Bien"

    ```markdown
    ---
    title: "Titre de ma page dans l'en-tête"
    ---

    # Je suis l'unique titre de niveau 1

    ## C'est vrai ça, c'est le seul, l'unique

    Woa, quel titre !
    ```

=== "Pas bien"

    ```markdown
    ---
    title: "Titre de ma page dans l'en-tête"
    ---

    # Je suis l'unique titre de niveau 1

    # Ah ouais ? Eh bah moi aussi je peux être niveau 1 si je veux !

    Pfff, encore une guéguerre pour savoir qui a le plus gros niveau de titre :( !
    ```
<!-- markdownlint-enable MD046 -->

### Cohérence du caractère pour les listes à puces

S'il est techniquement possible d'utiliser différents caractères, il est préférable d'utiliser le même caractère (généralement l'astérisque ou le tiret). A minima le style doit être cohérent dans une même page.

Dans cet exemple, des astérisques (`*`) ont été utilisés après que des tirets (`-`) l'aient déjà été pour le même niveau de puces.

![erreur style puces](https://cdn.geotribu.fr/img/internal/contribution/markdown/markdown_error_list_style_lizmap..png "Signalement de l'erreur dans Visual Studio Code"){: .img-center loading=lazy }

> Référence : [MD004 - Unordered list style](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md004)

### Paragraphes

En markdown, selon les implémentations, il est important de laisser des lignes vides entre les différents paragraphes (ou ce qui deviendra une balise HTML différente une fois converti). Par exemple :

- entre le texte et le début d'une liste (ordonnée ou pas)
- entre un titre et un paragraphe
- entre une image et un texte

#### Interligne simple

Pour revenir à la ligne sans créer de nouveau paragraphe, il suffit d'ajouter deux espaces à la fin de la ligne.

<!-- markdownlint-disable MD046 -->
=== "Markdown"

    ```markdown
    Je suis la première ligne du paragraphe.
    Et moi la ligne suivante mais du coup, je suis à la suite !

    Je suis un nouveau paragraphe.  
    Je suis la deuxième ligne du deuxième paragraphe, séparée de la précédente avec un simple interligne car la ligne précédente a 2 espaces à la fin.  
    Surligne nous si tu me crois pas !
    ```

=== "Rendu"

    Je suis la première ligne du paragraphe.
    Et moi la ligne suivante mais du coup, je suis à la suite !

    Je suis un nouveau paragraphe.  
    Je suis la deuxième ligne du deuxième paragraphe, séparée de la précédente avec un simple interligne car la ligne précédente a 2 espaces à la fin.
<!-- markdownlint-enable MD046 -->

#### Listes à puces

Pour les mêmes raisons, le premier élément d'une liste à puces doit être précédé d'une ligne vide (ce n'est pas le cas pour GitHub, où les deux formes sont acceptées). Par exemple, si on n'insère pas de ligne vide entre le paragraphe et le premier élément d'une liste à puces, le rendu ne fonctionnera pas :

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

> Référence : [MD032 - Lists should be surrounded by blank lines](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md032)

### Déclaration explicite des liens hypertextes

Si la plupart des outils repèrent les liens dans le texte, il est recommandé de les déclarer explicitement, notamment si le document est destiné à être intégré dans un format plus exigeant en termes de formatage (mail, etc.).

> Référence : [MD034 - Bare URL used](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md#md034)

<!-- markdownlint-disable MD034 MD038 -->
=== "Markdown"
    ```markdown
    - pas bien : https://geotribu.fr/
    - bien : <https://geotribu.fr/>
    - encore mieux : [texte du lien qui apparaît](https://geotribu.fr/)
    ```

=== "Rendu"
    - pas bien : https://geotribu.fr/
    - bien : <https://geotribu.fr/>
    - bien : [texte du lien qui apparaît](https://geotribu.fr/)
<!-- markdownlint-enableMD034 -->

----

## Outillage

Pour favoriser l'adoption de ces règles et contrôler leur application, plusieurs outils sont mis en place dans le processus de contribution :

- l'outil de vérification de la syntaxe (_linter_) Markdown, [`markdownlint-cli` est configuré (voir la page dédiée)](/contribuer/internal/markdown_linter/)
- des scripts automatiques au moment des contributions : [les git hooks (voir la page dédiée)](/contribuer/internal/git_hooks_precommit/)
