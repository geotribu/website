---
title: Insérer des diagrammes
authors:
    - Geotribu
categories:
    - article
    - contribution
    - tutoriel
date: 2020-07-20 10:20
description: "Guide de contribution à Geotribu : comment intégrer des diagrammes Mermaid dans un contenu en Markdown."
tags:
    - contribuer
    - diagramme
    - MermaidJS
    - schéma
# theme customizations
search:
  exclude: true
---

# Insérer des diagrammes

Le site intègre la bibliothèque [MermaidJS](https://mermaid-js.github.io/mermaid/#/) qui permet de générer des diagrammes en utilisant une extension de la syntaxe Markdown.

On utilise [l'intégration dans le thème Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/reference/diagrams/).

## Syntaxe

Cela consiste en créant une balise de code pointant sur le langage `mermaid`, dans laquelle on insère notre syntaxe MermaidJS.

!!! tip
    Pour se faciliter les choses, il est conseillé d'utiliser [l'éditeur en ligne](https://mermaid-js.github.io/mermaid-live-editor/) pour préparer son diagramme.

### Exemple 1

````markdown
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
````

### Rendu 1

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

### Exemple 2

````markdown
```mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```
````

### Rendu 2

``` mermaid
graph LR
  A[Start] --> B{Error?};
  B -->|Yes| C[Hmm...];
  C --> D[Debug];
  D --> B;
  B ---->|No| E[Yay!];
```
