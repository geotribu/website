---
title: "Extraits enrichis et 'cartes sociales'"
categories:
    - article
    - Geotribu
date: 2022-06-15 14:20
description: "Sous le GéoCapot : comment l'en-tête des contenus est utilisé pour générer des extraits enrichis et les 'cartes sociales'."
image: "https://cdn.geotribu.fr/img/internal/contribution/markdown_exemple.png"
tags:
    - coulisses
    - Jinja2
    - réseaux sociaux
# theme customizations
search:
  exclude: true
---

# Utilisation de l'en-tête pour le SEO et le partage des contenus

Lors de la rédaction d'un contenu sur Geotribu, que ce soit une revue de presse, un article, un guide de contribution ou autre, on insiste beaucoup sur l'en-tête du fichier, comme [l'illustre ce guide](/contribuer/guides/metadata_yaml_frontmatter/).

Pourquoi ? car c'est ainsi que le site génère des extraits enrichis et les 'cartes sociales' (_social cards_) qui appraissent lors du partage d'un contenu sur d'autres media : réseaux sociaux, outils collaboratifs (Teams, Slack, Matrix...) et même emails.

## Extraits enrichis

![logo JSON-LD](https://cdn.geotribu.fr/img/logos-icones/programmation/json-ld.webp "logo JSON-LD"){: .img-rdp-news-thumb }

La structuration des données géographiques, ça vous semble important ? Eh bien, c'est la même chose quand il s'agit des pages webs. C'est d'ailleurs le principe fondateur de ce qu'on appelle plus communément le **web sémantique** : intégrer des données structurées dans le contenu des pages de façon à faciliter le travail d'indexation et de mise en relation des contenus.

D'ailleurs, si vous êtes amenés à travailler sur les

 on travaille sur les données structurées  Le référencement des contenus sur les  sont toujours plus complexes. Dans ce sens, en dehors des optimisations classiques et bien connues de tous, arrive la nécessité de décrire des données structurées dans les pages web des sites internet via différentes syntaxes (microdonnées, microformats, RDFa).

Ces données sont également utilisées par les moteurs de recherche et favorisent le référencement ou plutôt permettent un affichage enrichi dans les pages de résultats, d'où le nom donné par Google : extrait enrichi (_rich snippet_ en anglais).

Connus sous le nom de rich snippets en anglais, ceux-ci ont de nombreux avantages en plus de représenter un pas vers la recherche sémantique : accès rapide à l’information via un affichage dans les SERPS, augmentation du taux de clic, etc.

### Données structurées générées

#### Page d'accueil

```jsonld
{
  "@context": "http://www.schema.org",
  "@type": "WebSite",
  "name": "Geotribu",
  "alternateName": "Géotribu",
  "url": "{{ config.site_url }}",
  "sameAs": [
    "http://geotribu.fr",
    "http://geotribu.net",
    "https://github.com/geotribu/",
    "https://facebook.com/geotribu",
    "https://twitter.com/geotribu"
  ],
  "potentialAction": {
    "@type": "SearchAction",
    "target": "{{ config.site_url }}?q={search_term}",
    "query-input": "required name=search_term"
  }
}
```

#### Article

Exemple pour [cet article](/articles/2021/2021-02-15_ignfr2map_carte_liens_IGN_open-data_7_etapes/) :

```jsonld
{
  "@context": "https://schema.org",
  "@type": "Article",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{ config.site_url }}articles/2021/2021-02-15_ignfr2map_carte_liens_IGN_open-data_7_etapes/"
  },
  "headline": "Geotribu - ign2map : Du site à la carte en 7 étapes",
  "abstract": "ign2map : le petit projet de Geotribu pour rendre l’expérience de téléchargement des données ouvertes de l'IGN plus interactive.",
  "datePublished": "2021-02-15 11:11",
  "image": "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_html_rendu.png","author": [
    {
      "@type": "Person",
      "name": "Florian Boret",
      "url": "{{ config.site_url }}team/fbor"
    },
    {
      "@type": "Person",
      "name": "Julien Moura",
      "url": "{{ config.site_url }}team/jmou"
    }
  ],
  "publisher": {
    "@type": "Organization",
    "name": "Geotribu",
    "logo": {
      "@type": "ImageObject",
      "url": "https://cdn.geotribu.fr/img/internal/charte/geotribu_logo_64x64.png"
    }
  }
}
```

#### Revue de presse

Exemple pour [cette GeoRDP](/rdp/2022/rdp_2022-06-03/) :

```jsonld
{
  "@context": "https://schema.org",
  "@type": "Article",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "{{ config.site_url }}rdp/2022/rdp_2022-06-03/"
  },
  "headline": "{{ config.site_name }} - Revue de presse du 3 juin 2022",
  "abstract": "Cette semaine on vous propose une déambulation autour de divers sujets : traduction de logiciels libres, une carte de bruit, le programme Lidar HD, la donnée OSO, la détection de bâtiments et les logiciels libres en thèse",
  "datePublished": "2022-06-03 14:20",
  "image": "https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/carte_bruit_Paris.jpg",
  "author": {
    "@type": "Organization",
    "name": "Geotribu",
    "url": "{{ config.site_url }}"
    },
  "publisher": {
    "@type": "Organization",
    "name": "Geotribu",
    "logo": {
      "@type": "ImageObject",
      "url": "https://cdn.geotribu.fr/img/internal/charte/geotribu_logo_64x64.png"
    }
  }
}
```

### Ressources

- le [schéma d'un article sur schema.org](https://schema.org/Article)
- le [validateur de schéma](https://validator.schema.org/)
- [description de l'extrait enrichi de type Article dans la documentation de Google](https://developers.google.com/search/docs/advanced/structured-data/article/)
- Google propose un [site pour tester les extraits enrichis](https://search.google.com/test/rich-results).

----

## Cartes sociales (_social cards_)

![icône globe social](https://cdn.geotribu.fr/img/internal/icons-rdp-news/social.png "icône globe social"){: .img-rdp-news-thumb }

> TO DOC

### Ressources

- le site officiel du [protocole Open Graph](https://ogp.me/)
- le [validateur de carte de Twitter](https://cards-dev.twitter.com/validator/)
