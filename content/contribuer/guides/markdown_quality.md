---
title: "Rédiger en Markdown : enjeux de qualité et régles"
categories:
    - article
    - contribution
    - tutoriel
date: 2020-09-14 14:20
description: "Rédiger en Markdown : règles partagées, erreurs fréquentes et mécanismes de validation."
image: "https://cdn.geotribu.fr/img/internal/contribution/markdown_quick_exemple_rendu.png"
tags:
    - contribuer
    - tutoriel
    - Markdown
    - rédaction
    - HTML
    - lint
    - Python
# theme customizations
search:
  exclude: true
---

# Rédiger en Markdown : règles et enjeux de qualité

!!! note
    Les règles à appliquer dépendent du moteur de rendu (conversion en HTML) utilisé. Consulter [l'article "Comprendre le rendu Markdown"](/contribuer/build_site/markdown_engine/#specificites) pour en savoir plus.

## Règles

L'outil markdownlint a défini un ensemble de règles dont nous utilisons une partie et des régales spécifiques :

- [règles de référence](https://github.com/DavidAnson/markdownlint/blob/main/doc/Rules.md)
- [règles configurées dans Géotribu](https://github.com/geotribu/website/blob/master/.markdownlint.json)

### Vérifier la syntaxe avec markdownlint-cli

On utilise [l'outil en ligne de commande développé en _node_](https://github.com/igorshubovych/markdownlint-cli) :

```bash
# installation du package
yarn add markdownlint-cli --dev --non-interactive --no-lockfile --prefer-offline

# vérification sur les fichiers contenus dans les dossiers commençant par '202'
yarn markdownlint -i "**/template_*.md" "content/*/202*/**/*.md"
```

Il est aussi possible d'utiliser markdownlint sous forme d'[extension dans Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint).

----

## Erreurs fréquentes

### Cohérence du caractère pour les listes à puces

S'il est techniquement possible d'utiliser différents caractères, il est préférable d'utiliser le même caractère (généralement l'astérisque ou le tiret) et a minima le style doit être cohérent dans une même page.

Dans cet exemple, des astérisques (`*`) ont été utilisés après que des tirets (`-`) l'aient déjà été pour le même niveau de puces.

![erreur style puces](https://user-images.githubusercontent.com/1596222/92222985-186a0200-eea0-11ea-9887-21fdbce10080.png "Signalement de l'erreur dans Visual Studio Code"){: .img-center loading=lazy }

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

<!-- Hyperlinks references -->
[Markdown]: https://daringfireball.net/projects/markdown/
[syntaxe]: https://daringfireball.net/projects/markdown/syntax
[StackEdit]: https://stackedit.io/
[Upmath]: https://upmath.me/
