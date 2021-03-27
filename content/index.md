---
title: "Geotribu - Page d'accueil"
Category: global
date: 2020-03-20 10:20
description: "Page d'accueil de Geotribu, site indépendant de veille sur la géomatique libre. Articles, tutoriels et revues de presse (#GeoRDP) sur l'information géographique."
tags: home,géomatique,sig,géographie,dataviz,geordp,accueil,geotribu
hide:
  - navigation
  - toc
---

# Bienvenue

```
       o                 o  
                  o  
         o   ______      o  
           _/  (   \_  
 _       _/  (       \_  O  
| \_   _/  (   (    0  \  
|== \_/  (   (          |  
|=== _ (   (   (        |  
|==_/ \_ (   (          |  
|_/     \_ (   (    \__/  
          \_ (      _/  
            |  |___/  
           /__/  
```

Bienvenue sur le site de Geotribu !

![Bannière Géotribu](https://cdn.geotribu.fr/img/internal/charte/geotribu_banner_1000x760.jpg "Bannière Geotribu"){: loading=lazy }
{: align=middle }

----

## S'abonner aux contenus

### RSS

![logo globe RSS](https://cdn.geotribu.fr/img/logos-icones/divers/worldRSS.png){: .img-rdp-news-thumb }

Il est possible de suivre l'évolution de nos contenus via les deux flux RSS qui sont générés avec le [plugin RSS pour MkDocs](https://guts.github.io/mkdocs-rss-plugin/) à partir de l'historique Git :

| Derniers contenus créés | Derniers contenus mis à jour |
| :---------------------: | :--------------------------: |
| [feed_rss_created.xml](/feed_rss_created.xml) | [feed_rss_updated.xml](/feed_rss_updated.xml) |
| [![Feedly button](https://s3.feedly.com/img/follows/feedly-follow-rectangle-flat-big_2x.png "Follow us on Feedly"){: width=130 height= 50 loading=lazy }](https://feedly.com/i/subscription/feed%2Fhttps%3A%2F%2Fstatic.geotribu.fr%2Ffeed_rss_created.xml) | [![Feedly button](https://s3.feedly.com/img/follows/feedly-follow-rectangle-flat-big_2x.png "Follow us on Feedly"){: width=130 height= 50 loading=lazy }](https://feedly.com/i/subscription/feed%2Fhttps%3A%2F%2Fstatic.geotribu.fr%2Ffeed_rss_updated.xml) |

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
