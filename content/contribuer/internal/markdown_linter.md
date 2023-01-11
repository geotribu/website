---
title: "Linter Markdown"
authors:
    - Julien MOURA
categories:
    - article
    - meta
date: 2022-07-18 10:20
description: "Sous le GéoCapot : comment est utilisé markdownlint, l'outil de vérification de la syntaxe Markdown (linter) sur Geotribu."
icon : material/check-all
image: "https://cdn.geotribu.fr/img/internal/contribution/markdown/linter_code.webp"
robots: index, follow
tags:
    - coulisses
    - linter
    - Markdown
---

# Vérification automatisée de la syntaxe Markdown (linter)

![Gant blanc pour contrôler la poussière](https://cdn.geotribu.fr/img/internal/contribution/markdown/gant_blanc_poussiere.webp "Gant blanc pour contrôler la poussière"){: .img-rdp-news-thumb }

Parmi ses nombreux atouts, la syntaxe [Markdown] doit probablement sa forte adoption à sa simplicité d'utilisation et à sa flexibilité. Sur un site, tel Geotribu, ouvert aux 4 vents de la contribution c'est à la fois une force et un élément à gérer car les erreurs de syntaxe, a priori inoffensives, peuvent mener à une page mal formée ou pire à casser le site... bon ok ce dernier scénario est peu probable mais un peu drama c'est toujours bien pour mettre la pression :smile:.

Pour vérifier la syntaxe et le respect des [règles de rédaction définies](/contribuer/guides/markdown_quality/#regles), on utilise donc un [linter](https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Linter) dédié au Markdown : [markdownlint-cli](https://github.com/igorshubovych/markdownlint-cli).

![linter de code](https://cdn.geotribu.fr/img/internal/contribution/markdown/linter_code.webp "Un linter est littéralement un rouleau à poussière"){: .img-center loading=lazy }  

----

## Utilisation de markdownlint(-cli)

### En local

Pour utiliser l'outil, il faut disposer d'un interpréteur NodeJS :

```sh
# installation du package
yarn add markdownlint-cli --dev --non-interactive --no-lockfile --prefer-offline

# vérification des contenus
yarn markdownlint "content/**/*.md"

# vérification et auto-correction des problèmes mineurs
yarn markdownlint --fix "content/**/*.md"
```

Il est aussi possible d'utiliser markdownlint sous forme d'[extension dans Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=DavidAnson.vscode-markdownlint) et probablement dans d'autres IDE.

### Git hook

Le linter est aussi configuré comme crochet git ([voir la page dédiée](/contribuer/internal/git_hooks_precommit/)) via pre-commit. Cela présente plusieurs avantages :

- pas besoin d'installer NodeJS, pre-commit s'occupe de tout dans un environnement dédié
- ça repère les erreurs voire les corrige automatiquement lors du _commit_

On peut donc l'utiliser ainsi :

```sh
# sur les fichiers indexés pour le commit - git add
pre-commit run markdownlint

# sur tous les fichiers
pre-commit run markdownlint --all
```

### Exécution automatisée sur la CI

![icône GitHub Actions](https://cdn.geotribu.fr/img/logos-icones/divers/github_actions.png "GitHub Actions"){: .img-rdp-news-thumb }

Etant donné que la très grande majorité des contributeur/ices n'utilisent pas [l'édition locale](/contribuer/edit/local_edition_setup/) ou n'installent pas les git hooks, la vérification syntaxique est automatiquement appliquée sur chaque _commit_ publié sur [GitHub] dans une Pull Request.

----

## Gérer les faux positifs du linter

Le linter est un outil. Il peut donc faire des erreurs et signaler des faux-positifs ou se tromper sur des cas particuliers. On peut alors utiliser un commentaire pour désactiver certains contrôles sur certaines parties d'une page.

Désactiver une ou plusieurs règles avec leur code :

```markdown
<!-- markdownlint-disable MD046 -->
```

(Ré)activer une ou plusieurs règles dans une page :

```markdown
<!-- markdownlint-enable MD046 -->
```
