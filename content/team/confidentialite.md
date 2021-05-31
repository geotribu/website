---
title: "Confidentialité des données "
authors: ["Geotribu"]
categories: ["meta"]
date: "2021-05-20 10:20"
description: "Cette page détaille les dispositifs de traçage que l'utilisateur/ice final/e peut rencontrer sur le site Geotribu."
image: "https://cdn.geotribu.fr/img/internal/charte/geotribu_banner_600x300.png"
tags: "GeoTribu,confidentialité,données personnelles,vie privée,tracking"
---

# Données personnelles et confidentialité

:calendar: Date de publication initiale : 20 mai 2021

**Mots-clés :** tracking | confidentialité | RGPD

Cette page détaille les dispositifs de traçage que l'utilisateur/ice final/e peut rencontrer sur le site Geotribu. Si la liste paraît longue c'est qu'elle est le fruit d'un effort de transparence :slightly_smiling_face:, mais pour faire court :

> Quand c'est gratuit, c'est moi le produit !

C'est pas faux ! Mais Geotribu se veut le fruit d'un travail bénévole, passionné et désintéressé.

> Vous faites quoi avec nos données ?

Pas grand chose d'utile et rien de mercantile ! On s'en sert pour :

- avoir une idée globale de la fréquentation, principale source de reconnaissance après les commentaires
- agrémenter les [bilans annuels publics](/articles/2021/2021-01-04_bilan_2020_perspectives_2021/)
- avoir du matériau pour des [articles d'analyse statistique](/articles/2021/2021-02-09_statistiques_twitter/)

Question ? Souci ? Angoisse ? Si vous souhaitez en savoir plus sur les données collectées, merci de [nous contacter par email](mailto:geotribu+rgpd@gmail.com).

----

## Google Analytics

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-rdp-news-thumb }

Parce-que c'était plus simple et intégré à MkDocs, nous utilisons Google Analytics pour mesurer la fréquentation du site en mode minimal. Compte-tenu de la typologie de notre audience technophile et sensibilisée aux [bloqueurs de pubs](https://fr.wikipedia.org/wiki/Logiciel_antipub), [opt-outs](https://tools.google.com/dlpage/gaoptout/index.html?hl=fr) et autres [VPNs](https://fr.wikipedia.org/wiki/R%C3%A9seau_priv%C3%A9_virtuel), les données sont certainement incomplètes voire faussées.

Mais l'objectif n'étant pas de faire du marketing, cela importe peu. L'idée est surtout de suivre les tendances.

----

## Twitter

![logo Twitter](https://cdn.geotribu.fr/img/logos-icones/social/twitter.png "logo Twitter"){: .img-rdp-news-thumb }

Une partie non négligeable de la veille technologique passe par le réseau social de micro-blogging. Afin de pouvoir intégrer les tweets dans nos pages, nous embarquons le code de la plateforme pour que le rendu soit conforme à ses règles ([voir cette documentation](https://help.twitter.com/fr/using-twitter/how-to-embed-a-tweet)).

A noter que le rendu est complètement différent selon si le navigateur bloque ou non le code Twitter : [voir le guide d'intégration d'un Tweet](/contribuer/guides/twitter/#pistage-blocage-et-fallback).

----

## Flux RSS

![icône RSS](https://cdn.geotribu.fr/img/logos-icones/rss.png "icône RSS"){: .img-rdp-news-thumb }

Dans le but d'identifier la part des visites liée aux abonnés à notre [flux RSS] sans recourir à des dispositifs de traçage supplémentaires (tels [feedburner](https://feedburner.google.com/)), nous ajoutons des paramètres *Urchin Tracking Module* ([UTM]).

Les paramètres utilisés sont :

- `utm_source` : "rss-feed"
- `utm_medium` : "RSS"
- `utm_campaign` : "feed-syndication"

----

## Commentaires

![icône commentaire](https://cdn.geotribu.fr/img/logos-icones/astuce.png "icône commentaire"){: .img-rdp-news-thumb }

Les commentaires sont gérés avec [Isso], une solution libre, gratuite et auto-hébergée sur le même serveur où sont stockées les images. Aucun dispositif de traçage n'est associé.

Néanmoins, les commentaires sont publics et certaines données sont enregistrées à des fins de suivi juridique dans la base de données :

- le nom d'utilisateur (obligatoire) renseigné
- l'adresse email (obligatoire) renseignée
- le site web (optionnel) renseigné
- l'adresse IP lors de la soumission du formulaire

[Consulter l'article sur la migration vers Isso](/articles/2021/2021-05-14_commentaires_migration_disqus_isso/){: .md-button }
{: align=middle }

<!-- Hyperlinks reference -->
[flux RSS]: https://static.geotribu.fr/feed_rss_created.xml
[Isso]: https://posativ.org/isso/
[UTM]: https://fr.wikipedia.org/wiki/Param%C3%A8tres_UTM
