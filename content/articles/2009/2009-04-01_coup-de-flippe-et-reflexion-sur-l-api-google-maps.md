---
title: "Coup de flippe et réflexion sur l'API Google Maps"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-04-01
description: "Coup de flippe et réflexion sur l'API Google Maps"
tags:
    - API
    - Google
---

# Coup de flippe et réflexion sur l'API Google Maps

:calendar: Date de publication initiale : 01 avril 2009

![world absurde](https://cdn.geotribu.fr/img/internal/icons-rdp-news/absurde.png)

Aujourd'hui mercredi 1er avril - ça ne s'invente pas :wink: - j'ai eu la malencontreuse surprise de voir tous mes tutoriaux et projets [Google Maps](http://code.google.com/intl/fr/apis/maps/) ne plus répondre.

Voici l'erreur que me fournissait [Firebug](http://getfirebug.com/) : `window.jstiming is undefined` - autrement dit un gros charabia pour moi.

Le fichier incriminé : [main.js](http://maps.google.com/intl/fr_ALL/mapfiles/152d/maps2.api/main.js) de l'API (cf. la ligne 1115 où se trouve l'erreur) - je n'ai donc pas la main dessus.

Du coup, après avoir cherché la solution, je me suis posé la question de ma grande dépendance en utilisant cette API non libre. Et même si je regarde un peu (beaucoup) ailleurs depuis pas mal de temps, j'essayais de ne pas voir cette réalité - "Google ne peut pas modifier ses conditions d'utilisation, y'a trop de gens qui l'utilisent ..." - même si ce n'est pas le cas aujourd'hui, il y a une petite part d'incertitude.

Et bien, réflexion faite, je crois bien que nous sommes dépendants et qu'il faille développer sous Google Maps en connaissance de cause. Je risque donc dorénavant de me pencher plus sérieusement sur les API libres et les protocoles de diffusion de données de l'OGC. Je continuerai évidemment les tutoriaux sur Google Maps et sur Google Earth mais en gardant à l'esprit un risque potentiel.

Au fait, l'erreur... pas très compliquée et entièrement de ma faute (à toujours vouloir utiliser les dernières versions pour je ne sais quelle raison), je demandais lors de l'appel à l'API Google Maps la dernière version soit la 2.x : en modifiant v2.x par v2, tout est rentré dans l'ordre. Je corrige tous les tutoriaux en conséquence et en profite pour leur donner un petit coup de neuf.

----

<!-- geotribu:authors-block -->
