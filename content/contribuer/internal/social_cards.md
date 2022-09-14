---
title: "Cartes de partage"
categories:
    - article
    - Geotribu
date: 2022-09-15 14:20
description: "Sous le GéoCapot : comment l'en-tête des contenus est utilisé pour générer des 'cartes sociales', ces visuels accompagnés d'un résumé qui s'affichent sur les réseaux sociaux."
icon : material/card-text
image: "https://cdn.geotribu.fr/img/internal/contribution/social_cards/social_card_exemple_twitter_article.png"
tags:
    - coulisses
    - Jinja2
    - réseaux sociaux
# theme customizations
search:
  exclude: true
---

# Optimisation pour le partage des contenus (_social cards_)

Lors de la rédaction d'un contenu sur Geotribu, que ce soit une revue de presse, un article, un guide de contribution ou autre, on insiste beaucoup sur l'en-tête du fichier, comme [l'illustre ce guide](/contribuer/guides/metadata_yaml_frontmatter/).

Pourquoi ? car ces informations, des métadonnées en somme, sont utilisées pour enrichir la structuration des contenus et notamment générer les 'cartes sociales' (_social cards_) qui appraissent lors du partage d'un contenu sur d'autres media : réseaux sociaux, outils collaboratifs (Teams, Slack, Matrix...) et même emails.

## Cartes sociales (_social cards_)

![icône globe social](https://cdn.geotribu.fr/img/internal/icons-rdp-news/social.png "icône globe social"){: .img-rdp-news-thumb }

OpenGraph

### Pourquoi

> TO DOC

----

## Processus

![logo Jinja](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/jinja.png "logo Jinja"){: .img-rdp-news-thumb }

Le thème qu'on utilise, [Material for Mkdocs], propose de générer automatiquement des cartes sociales génériques (voir [la documentation](https://squidfunk.github.io/mkdocs-material/setup/setting-up-social-cards/)) en croisant les éléments graphiques du site (nom, police, couleur dominante) et ceux de chaque page (titre).

Mais le nombre de contenus gérés dans Geotribu rend le mécanisme assez lourd (une image générée par fichier Markdown) et trop générique alors que l'objet des contenus Geotribu (carte, dataviz...) se prête bien à des visuels personnalisés.

Au moment de la [transformation des fichiers markdown en fichiers HTML](/contribuer/internal/markdown_engine/), le site intègre les balises dédiées dans l'en-tête de la page HTML (`<head>`), à partir des informations présentes dans l'en-tête, notamment l'image d'illustration.

Les informations sont manipulées avec la syntaxe [Jinja](https://fr.wikipedia.org/wiki/Jinja_(moteur_de_template)), utilisée par [Mkdocs], dans le [template `main.html`](https://github.com/geotribu/website/blob/master/content/theme/main.html).

Voici le bloc en question :

{% raw %}

```jinja
[...]
  {# OpenGraph #}
  <meta property="og:description" content="{{ description }}">
  <meta property="og:image" content="{{ image }}">
  <meta property="og:locale" content="fr_FR" />
  <meta property="og:title" content="{{ title }}">
  <meta property="og:type" content="{{ type }}">
  <meta property="og:url" content="{{ page.canonical_url }}">
  {# Twitter #}
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:creator" content="@geotribu" />
  <meta name="twitter:description" content="{{ description }}">
  <meta name="twitter:dnt" content="on">
  <meta name="twitter:image" content="{{ image }}">
  <meta name="twitter:site" content="@geotribu" />
  <meta name="twitter:title" content="{{ title }}">
  <meta name="twitter:widgets:align" content="center">
[...]
```

{% endraw %}

## Exemple de rendu pour cet article sur Twitter

![Social card - Exemple de partage d'un contenu Geotribu sur Twitter](https://cdn.geotribu.fr/img/internal/contribution/social_cards/social_card_exemple_twitter_article.png "Social card - Exemple de partage d'un contenu Geotribu sur Twitter"){: .img-center loading=lazy }

----

## Ressources

- le site officiel du [protocole Open Graph](https://ogp.me/)
- avoir un aperçu du rendu sur différents services sur [metatags.io](https://metatags.io/)
- le [validateur de carte de Twitter](https://cards-dev.twitter.com/validator/)
- [l'équivalent de Facebook](https://developers.facebook.com/tools/debug/)
- [celui de LinkedIn](https://www.linkedin.com/post-inspector/)
