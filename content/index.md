---
title: "Bienvenue"
Category: global
Date: 2020-03-20 10:20
description: "Bienvenue sur Geotribu, le site indépendant de veille sur la géomatique libre. Retrouvez nos articles, tutoriels et nos revues de presse (#GeoRDP) sur l'information géographique, les SIG, la cartographie, la représentation des données géographiques... Globalement, tout ce qui mêle géographie et informatique."
hero: "Bienvenue sur Geotribu !"
tags: bienvenue,géomatique,sig,géographie,dataviz,geordp,accueil,geotribu
---

# Bienvenue

Bienvenue sur le site de Geotribu !

![Bannière Géotribu](https://cdn.geotribu.fr/images/internal/charte/geotribu_banner.jpg "Bannière Geotribu"){: loading=lazy }

----

## S'abonner aux contenus

### RSS

![logo globe RSS](https://cdn.geotribu.fr/img/logos-icones/divers/worldRSS.png){: .img-rdp-news-thumb }

Il est possible de suivre l'évolution de nos contenus via les deux flux RSS qui sont générés avec le [plugin RSS pour MkDocs](https://guts.github.io/mkdocs-rss-plugin/) à partir de l'historique Git :

- [l'un pour les derniers contenus créés](/feed_rss_created.xml)
- [l'autre pour les derniers contenus mis à jour](/feed_rss_updated.xml)

----

## Thème

Par défaut, le site utilise votre réglage système (clair ou sombre). Il est possible de forcer le thème utilisé le temps d'une session de navigation :

<button data-md-color-scheme="default"><code>Thème clair</code></button>
<button data-md-color-scheme="slate"><code>Thème sombre</code></button>

<script>
  var buttons = document.querySelectorAll("button[data-md-color-scheme]")
  buttons.forEach(function(button) {
    var attr = "data-md-color-scheme"
    button.addEventListener("click", function() {
      document.body.setAttribute(attr, this.getAttribute(attr))
    })
  })
</script>
