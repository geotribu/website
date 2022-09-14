---
title: "Cartes de partage"
categories:
    - article
    - Geotribu
date: 2022-09-15 14:20
description: "Sous le GéoCapot : comment l'en-tête des contenus est utilisé pour générer des 'cartes sociales', ces visuels accompagnés d'un résumé qui s'affichent sur les réseaux sociaux."
icon : material/card-text
image: "https://cdn.geotribu.fr/img/internal/contribution/markdown_exemple.png"
tags:
    - coulisses
    - Jinja2
    - réseaux sociaux
# theme customizations
search:
  exclude: true
---

# Utilisation de l'en-tête pour le partage des contenus

Lors de la rédaction d'un contenu sur Geotribu, que ce soit une revue de presse, un article, un guide de contribution ou autre, on insiste beaucoup sur l'en-tête du fichier, comme [l'illustre ce guide](/contribuer/guides/metadata_yaml_frontmatter/).

Pourquoi ? car ces informations, des métadonnées en somme, sont utilisées pour enrichir la structuration des contenus et notamment générer les 'cartes sociales' (_social cards_) qui appraissent lors du partage d'un contenu sur d'autres media : réseaux sociaux, outils collaboratifs (Teams, Slack, Matrix...) et même emails.

## Cartes sociales (_social cards_)

![icône globe social](https://cdn.geotribu.fr/img/internal/icons-rdp-news/social.png "icône globe social"){: .img-rdp-news-thumb }

> TO DOC

### Pourquoi

> TO DOC

### Comment

Le thème qu'on utilise, [Material for Mkdocs], propose de générer automatiquement des cartes sociales génériques (voir [la documentation](https://squidfunk.github.io/mkdocs-material/setup/setting-up-social-cards/)) en croisant les éléments graphiques du site (nom, police, couleur dominante) et ceux de chaque page (titre).

Mais le nombre de contenus gérés dans Geotribu rend le mécanisme assez lourd (une image générée par fichier Markdown) et trop générique alors que l'objet des contenus Geotribu (carte, dataviz...) se prête bien à des visuels personnalisés.

----

## Ressources

- le site officiel du [protocole Open Graph](https://ogp.me/)
- avoir un aperçu du rendu sur différents services sur [metatags.io](https://metatags.io/)
- le [validateur de carte de Twitter](https://cards-dev.twitter.com/validator/)
- [l'équivalent de Facebook](https://developers.facebook.com/tools/debug/)
- [celui de LinkedIn](https://www.linkedin.com/post-inspector/)
