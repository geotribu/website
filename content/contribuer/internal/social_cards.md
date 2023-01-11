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

![icône globe social](https://cdn.geotribu.fr/img/internal/icons-rdp-news/social.png "icône globe social"){: .img-rdp-news-thumb }

Lors de la rédaction d'un contenu sur Geotribu, que ce soit une revue de presse, un article, un guide de contribution ou autre, on insiste beaucoup sur l'en-tête du fichier, comme [l'illustre ce guide](/contribuer/guides/metadata_yaml_frontmatter/).

Pourquoi ? car ces informations, des métadonnées en somme, sont utilisées pour enrichir la structuration des contenus et notamment générer les 'cartes sociales' (_social cards_) qui appraissent lors du partage d'un contenu sur d'autres media : réseaux sociaux, outils collaboratifs (Teams, Slack, Matrix...) et même emails.

## Les cartes sociales (_social cards_)

![logo Open Graph Protocol](https://cdn.geotribu.fr/img/logos-icones/divers/open_graph_protocol.png "logo Open Graph Protocol"){: .img-rdp-news-thumb }

Les _social cards_ désignent les visuels formatés qui apparaissent lors du partage des liens sur les réseaux sociaux principalement mais aussi dans des outils de tchat (Matrix, Slack, Teams...) ou plus généralement dans les outils capables de tirer parti des métadonnées des pages (Google Docs, clients mails...) et notamment du protocole Open Graph... ou de celui poussé par chaque plateforme ([Twitter Cards](https://developer.twitter.com/en/docs/twitter-for-websites/cards/overview/abouts-cards), etc.).

C'est lié au web sémantique et similaire aux [extraits enrichis](/contribuer/internal/seo_extraits_enrichis/) dans la mesure où ça utilise les mêmes informations mais structurées d'une autre manière (ici du simple HTML).

C'est assez important pour un site comme Geotribu, d'abord car ça rend le partage des contenus plus esthétique mais surtout plus rapide et donc moins fastidieux pour les bénévoles que nous sommes !

----

## Processus

![logo Jinja](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/jinja.png "logo Jinja"){: .img-rdp-news-thumb }

Le thème qu'on utilise, [Material for Mkdocs], propose de générer automatiquement des cartes sociales génériques (voir [la documentation](https://squidfunk.github.io/mkdocs-material/setup/setting-up-social-cards/)) en croisant les éléments graphiques du site (nom, police, couleur dominante) et ceux de chaque page (titre).

Mais le nombre de contenus gérés dans Geotribu rend le mécanisme assez lourd (une image générée par fichier Markdown) et trop générique alors que la diversité et l'objet des contenus Geotribu (carte, dataviz...) se prête bien à des visuels personnalisés.

Au moment de la [transformation des fichiers markdown en fichiers HTML](/contribuer/internal/markdown_engine/), le site intègre donc les balises dédiées dans l'en-tête de la page HTML (`<head>`), à partir des informations présentes dans l'en-tête, notamment l'image d'illustration.

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

## Exemple de rendu sur Twitter

Par exemple, il suffit d'insérer le lien vers [cet article](/articles/2022/2022-08-02_API_Python_FME_travailler_avec_GDAL/) lors de la rédaction d'un tweet pour que Twitter ajoute automatiquement sa _card_ avec l'image, le titre et la description du contenu, ce qui évite de devoir les mettre manuellement et homogénéise les partages :

![Social card - Exemple de partage d'un contenu Geotribu sur Twitter](https://cdn.geotribu.fr/img/internal/contribution/social_cards/social_card_exemple_twitter_article.png "Social card - Exemple de partage d'un contenu Geotribu sur Twitter"){: .img-center loading=lazy }

----

## Ressources

- le site officiel du [protocole Open Graph](https://ogp.me/)
- avoir un aperçu du rendu sur différents services sur [metatags.io](https://metatags.io/)
- le [validateur de carte de Twitter](https://cards-dev.twitter.com/validator/)
- [l'équivalent de Facebook](https://developers.facebook.com/tools/debug/)
- [celui de LinkedIn](https://www.linkedin.com/post-inspector/)
