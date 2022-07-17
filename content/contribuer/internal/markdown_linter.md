---
title: "Linter, vérification automatisée de la syntaxe Markdown"
authors:
    - Julien MOURA
categories:
    - article
    - meta
date: 2022-07-18 10:20
description: "Sous le GéoCapot : comment est utilisé markdownlint, l'outil de vérification de la syntaxe Markdown (linter) sur Geotribu."
icon : material/check-all
image: "https://cdn.geotribu.fr/img/internal/contribution/git_hooks/pre-commit_ci_result_master.png"
robots: index, follow
tags:
    - coulisses
    - linter
    - Markdown
---

# Vérification automatique de la syntaxe Markdown

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

----

## Gérer les faux positifs du linter

Le linter est un simple outil, il peut donc faire des erreurs et signaler des faux-positifs ou se tromper sur des cas particuliers. On peut alors utiliser un commentaire pour désactiver certains contrôles sur certaines parties d'une page.

Désactiver une ou plusieurs règles avec leur code :

```markdown
<!-- markdownlint-disable MD046 -->
```

(Ré)activer une ou plusieurs règles dans une page :

```markdown
<!-- markdownlint-enable MD046 -->
```
