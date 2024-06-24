---
title: "Intégrer facilement et rapidement une carte à votre site"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2011-04-13
description: "Intégrer facilement et rapidement une carte à votre site"
tags:
    - open source
---

# Intégrer facilement et rapidement une carte à votre site

:calendar: Date de publication initiale : 13 avril 2011

![icône globe](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "icône globe"){: .img-thumbnail-left }

Même si des API de plus en plus puissantes et faciles d'utilisation sont disponibles, l'intégration d'une carte au sein d'un site Internet requiert quelques compétences. Paradoxalement, les besoins des utilisateurs sont souvent limités à l'affichage de points et d'infobulles. De ce constat, sont nés différents services permettant d'ajouter facilement et rapidement une carte à votre site. Notre objectif n'est pas de présenter toutes les solutions possibles, néanmoins si vous en connaissez d'autres, les commentaires sont les bienvenus. Dans ce billet nous nous attacherons à présenter CartOsm qui utilise les données OpenStreetMap et Click2Map qui s'appuie sur les données de Google Maps.

## CartOsm

Réalisé par [Rodolphe Quiédeville](http://blog.rodolphe.quiedeville.org/), ce service vous permet de définir la zone à afficher, les options de la carte ainsi que le point d'intérêt que vous souhaitez mettre en évidence. Chaque option modifie ensuite le code iframe qu'il vous suffira d'insérer dans votre site.

Passons à l'étape de création, vous verrez cela ne prendra pas plus de 30 secondes. Tout d'abord, connectez-vous au site [CartOsm](http://cartosm.eu/#), sélectionnez ensuite la zone depuis la carte ou grâce au champ de recherche ainsi que le marqueur et il suffit maintenant de copier le code iframe automatiquement généré.

Voilà comment en trois clics de souris vous avez votre propre carte à insérer dans votre site. Par exemple, la ville où je réside :

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe width="400" height="350" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://cartosm.eu/map?lon=7.2684054&amp;lat=43.7009504&amp;zoom=14&amp;width=400&amp;height=350&amp;mark=true&amp;nav=true&amp;pan=true&amp;zb=inout&amp;style=default&amp;icon=up"></iframe>`

## Click2Map

Fondé par Antony Zanetti, [Click2Map](http://www.click2map.com/home) est un service complet et hautement paramétrable permettant l'intégration d'une carte sur son site web.

![Click2Map](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/create_map.png "Click2Map"){: .img-center loading=lazy }

Contrairement à CartOSM qui se base sur des iframes, Click2Map génère une application qu'il faudra ensuite ajouter vous même sur votre serveur. Bien que la mise en œuvre soit un poil plus compliqué, cela se traduit par de nombreuses options et une personnalisation poussée :

- Geocodage pour la recherche d'adresse
- Personnalisation des marqueurs et des infobulles
- Ajout de données depuis des fichiers CSV, KML, GeoRSS
- ...

A noter que la [version payante](http://www.click2map.com/business_services) vous permet d'héberger votre application sur les serveurs de Click2Map.

## Conclusion

Les deux services que nous vous avons présenté se proposent, avec des niveaux de technicité différents, d'intégrer une carte à votre site Internet.  
A l'heure où les applications cartographiques se résument bien souvent à n'afficher que quelques points sur une carte, ce type de service apporte une réelle plus-value. En effet, cela permet d'externaliser ou de faciliter l'intégration d'informations cartographiques pour des entreprises ou des personnes dont cela n'est pas le coeur de métier.  
Il existe certainement des services similaires. En connaissez-vous d'autres ? Les avez-vous testé ? Les commentaires sont ouverts !

----

<!-- geotribu:authors-block -->
