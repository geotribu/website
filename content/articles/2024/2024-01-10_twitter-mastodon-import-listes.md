---
title: "De X Twitter à Mastodon, guide de migration pour les géomaticien/nes"
subtitle: En attendant l'avènement du Y
authors:
    - Julien Moura
categories:
    - article
comments: true
date: 2024-01-10 10:20:00
description: En 2024, faire de la veille en géomatique sur Twitter/X devient pénible voire malaisant. Guide à destination des géo* qui veulent embarquer dans l'aventure Mastodon.
image:
license: default
robots: index, follow
tags:
    - Mastodon
    - Twitter
---

# Embarquer dans Mastodon : guide pour les géo*

:calendar: Date de publication initiale : 10 janvier 2024

## Introduction

![logo Mastodon](https://cdn.geotribu.fr/img/logos-icones/social/mastodon.png){: .img-thumbnail-left }

Bonjour.  
Nous sommes en 2024 et il est temps de quitter le réseau X (Twitter).  
Peur de sauter par-dessus bord ? Je comprends.  
Voici un guide pour atterrir en douceur sur le réseau décentralisé Mastodon.  
Peur d'un énième guide ? Je comprends.  
Ce guide est fait sur-mesure pour les cartographes, géomaticiennes, géomaticiens et même pour les sigistes ! Oui, même pour les sigistes.
Impressionné/e ? Je comprends.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Choisir où créer son compte

Vous avez 3 options. Seulement 3 ? Oui, vous n'êtes pa là pour avoir trop de choix, vous éparpiller ou perdre du temps à tout piger le fediverse et tous les mots-clés qui nous excitent nous autres geeks de l'hyperespace !

Donc 3 options disais-je :

- [**mapstodon.space**](https://mapstodon.space/) : celle qu'il vous faut. Vous pouvez ignorer les deux suivantes si vous avez geo ou carto quelque part en haut de votre CV.
- [fosstodon.org](https://fosstodon.org/) : si vous êtes sous licence GPL2+.
- [mastodon.social](https://mastodon.social/) : l'instance principale, si vous voulez un max de liberté et un facteur de dispersion élevé.

![:material-sign-direction: Créer son compte sur Mapstodon.space](https://mapstodon.space/auth/sign_up){: .md-button .md-button--primary }
{: align=middle }

Pour la suite, c'est du très classique :

1. Lire et accepter les règles du serveur : pas de harcèlement, pas de prosélytisme idéologico-religieux, pas de pub commerciale excessive
1. Choisir son pseudo (spoiler : `geotribu` est déjà pris)
1. Choisir son mot de passe, par exemple :

    ```txt
    12345678motdepass
    ```

1. Si vous avez cliqué sur le bouton copier juste au-dessus, revenir sur vos pas, souffler et utiliser le générateur de mot de passe de votre navigateur ou gestionnaire idoine.
1. Mettre un court texte pour les modérateur/ices. Comme je suis sympa, copier le suivant :

    ```txt
    Je viens de la part de Julien, le gars qui écrit sur Geotribu.  
    Vu que je travaille et/ou m'intéresse à la géomatique, il semble que cette instance soit la meilleure option.
    ```

----

## Premiers pas

S'abonner à geotribu.

----

## Importer des listes de comptes à suivre

Pour éviter le sentiment de vide et remise à zéro de son réseau, il est recommandé d'importer des listes de comptes.  Pour cela, l'écosystème propose un générateur de micro site web, [Mastodon Sociologists](https://github.com/trutzig89182/Mastodon-Sociologists), qui permet d'exporter des listes de comptes. C'est minimaliste, ça prend littéralement 5 minutes et ça permet d'avoir un "kit de démarrage" sur le réseau.

Allez, petit tutoriel rapide pour les moins aventureux/ses :

1. Se rendre sur [le site de Florian Ledermann](https://cartolab.at/cartography-on-mastodon/).
1. Sélectionner les catégories qui vous intéressent. Il est aussi possible de sélectionner compte par compte mais si vous êtes rendus là c'est que vous n'êtes pas ce genre de forçat :grin:. Personnellement, je commence par tout déselectionner (`Select none`) puis je clique sur les `Select all` en regard des catégories `Cartography, geovisualization and visual aspects of GIS`, `GIS, geodata and geography` et `General information visualization & data science` ce qui, à date, représente 208 des 245 comptes répertoriés :

    ![Listes de comptes à suivre - Florian Ledermann](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_listes_Florian_Ledermann.webp){: .img-center loading=lazy }

1. Sur votre instance Mastodon, se rendre dans votre profil et dans le menu `Import et export` > `Import` ou directement <https://mapstodon.space/settings/imports> si vous êtes sur l'instance [Mapstodon]. Choisir `Liste de comptes suivis` en haut, sélectionner le fichier CSV téléchargé précédemment (a priori `cartography_on_mastodon.csv`) :

    ![Mastodon - Interface d'import des listes de comptes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_listes_import.webp){: .img-center loading=lazy }

1. Cliquer sur le gros bouton `Importer` et confirmer sur le dialogue suivant :

    ![Mastodon - Confirmation d'import de listes de comptes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_listes_import_confirmation.webp){: .img-center loading=lazy }

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

{% include "licenses/default.md" %}
