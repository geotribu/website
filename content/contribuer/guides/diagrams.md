---
title: Insérer des diagrammes
author: "Julien Moura"
categories: ["contribution", "tutoriel"]
date: 2020-07-20 10:20
tags: geotribu,contribuer,diagramme,schéma,mermaid
---

# Insérer des diagrammes

Le site intègre la bibliothèque [MermaidJS](https://mermaid-js.github.io/mermaid/#/) qui permet de générer des diagrammes en utilisant une extension de la syntaxe Markdown.

On utilise [l'extension SuperFences de PyMdown](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/#uml-diagram-example/).

## Syntaxe

Cela consiste en créant une balise de code pointant sur le langage `mermaid`.

### Exemple

```markdown

    ```mermaid
    graph TD;
        Z[master]-->A[Création d'une branche]-->B(Pull Request);
        C[Contributeur 1]-->B;
        D[Contributrice 2]-->B;
        E[Contributeur n]-->B;
        B-->F[Merge dans la branche principale];
        F-->G[Conversion en HTML];
        G-->H[Déploiement sur GitHub Pages];
        H-->Twitter;
        H-->LinkedIn;
    ```

```

### Rendu

```mermaid
graph TD;
    Z[master]-->A[Création d'une branche]-->B(Pull Request);
    C[Contributeur 1]-->B;
    D[Contributrice 2]-->B;
    E[Contributeur n]-->B;
    B-->F[Merge dans la branche principale];
    F-->G[Conversion en HTML];
    G-->H[Déploiement sur GitHub Pages];
    H-->Twitter;
    H-->LinkedIn;
```
