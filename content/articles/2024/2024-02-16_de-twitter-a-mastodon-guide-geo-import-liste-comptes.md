---
title: "De X Twitter à Mastodon, guide de migration pour les géomaticien/nes"
subtitle: En attendant l'avènement du Y
authors:
    - Julien Moura
categories:
    - article
comments: true
date: 2024-02-16 10:20:00
description: En 2024, faire de la veille en géomatique sur Twitter/X devient pénible voire malaisant. Guide à destination des géo* qui veulent embarquer dans l'aventure Mastodon.
icon: material/mastodon
image:
license: beerware
robots: index, follow
tags:
    - Mastodon
    - Twitter
---

# Embarquer dans Mastodon : guide pour les géo*

:calendar: Date de publication initiale : 16 février 2024

## Introduction

![logo Mastodon](https://cdn.geotribu.fr/img/logos-icones/social/mastodon.png){: .img-thumbnail-left }

Bonjour.  
Nous sommes en 2024 et il est temps de quitter le réseau X (Twitter) ou du moins d'en faire un réseau social secondaire.  
Peur de sauter par-dessus bord ? Je comprends.  
Voici un guide pour atterrir en douceur sur le réseau décentralisé Mastodon.  
Peur d'un énième guide ? Je comprends.  
Ce guide est fait sur-mesure pour les cartographes, géomaticiennes, géomaticiens et même pour les sigistes ! Oui, même pour les sigistes.
Impressionné/e ?  
Je comprends.

Je comprends sincèrement que la force de l'inertie est forte, que sortir de sa zone de confort avec les habitudes et followers acquis ces dernières années est contre-nature, que maintenir une présence sur les réseaux sociaux est déjà suffisamment chronophage pour ne pas s'en rajouter, que l'émiettement des plateformes est douloureux, qu'il est tentant de faire de LinkedIn le nouveau Twitter, que les concepts sous-jacents à Mastodon et tous ces machins de fediverse font plus penser à un kif de geeks qui ont transposé leurs fantasmes des univers de super-héros dans les outils mais qu'on n'a pas que ça à faire de configurer ceci, paramétrer cela, lancer telle commande, etc.

Je comprends. Vraiment. Oui, même si c'est contre ma propre nature de geek justement :wink:. Mais je suis persuadé qu'il y a un intérêt à peupler ce réseau social de gens plus diversifiés que ceux qui vont presque naturellement sur Mastodon au risque d'en faire justement une bulle d'écho entre technophiles plutôt de gauche ; comme BlueSky semble l'être pour le monde universitaire / CSP+... et t**X**itter celle des réactionnaires.

Essayez. Ça n'engage à rien. Vraiment.  
Laissez vous guider, ça va bien se passer.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Choisir où créer son compte

Vous avez 3 options. Seulement 3 ? Oui, vous n'êtes pas là pour avoir trop de choix, vous éparpiller ou perdre du temps à tout piger le fediverse et tous les mots-clés qui nous excitent nous autres geeks de l'hyperespace !

Donc 3 options disais-je :

- [**mapstodon.space**](https://mapstodon.space/) : celle qu'il vous faut. Vous pouvez ignorer les deux suivantes si vous avez geo ou carto quelque part en haut de votre CV.
- [fosstodon.org](https://fosstodon.org/) : si vous êtes sous licence GPL2+.
- [mastodon.social](https://mastodon.social/) : l'instance principale, si vous voulez un max de liberté et un facteur de dispersion élevé.

[:material-sign-direction: Créer son compte sur Mapstodon.space](https://mapstodon.space/auth/sign_up){: .md-button .md-button--primary }
{: align=middle }

Pour la suite, c'est du très classique :

1. Lire et accepter les règles du serveur : pas de harcèlement, pas de prosélytisme idéologico-religieux, pas de pub commerciale excessive
1. Choisir son pseudo (spoiler : `geotribu` est déjà pris)
1. Choisir son mot de passe, par exemple :

    ```txt
    12345678motdepass
    ```

1. Si vous avez cliqué sur le bouton :material-content-copy: ou vraiment copié le texte ci-dessus, voici les étapes à suivre calmement : revenir sur vos pas, souffler et utiliser le générateur de mot de passe de votre navigateur ou gestionnaire idoine.
1. Mettre un court texte pour l'équipe de modération. Comme je suis sympa, copier le suivant :

    ```txt
    Je viens de la part de Julien, le gars qui écrit sur Geotribu.  
    Vu que je travaille ou m'intéresse à la géomatique, il semble que cette instance soit la meilleure option.
    ```

----

## Premiers pas

Quelques grandes étapes à suivre aveuglément (même si je ne suis pas borgne) pour bien démarrer dans votre nouvelle vie sociale.

### Définir la langue d'affichage et les paramètres généraux

1. Se rendre dans les préférences d'apparence ([raccourci Mapstodon](https://mapstodon.space/settings/preferences/appearance))
1. Boum, c'est juste là :

![Mastodon - Changer les paramètres d'affichage](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_langue_interface.webp){: .img-center loading=lazy }

### Filtrer sur les langues des posts

1. Se rendre dans les préférences dites "autres" ([raccourci Mapstodon](https://mapstodon.space/settings/preferences/other))
1. Cocher les cases des langues que vous souhaitez voir affichées (oui je sais, c'est la fête du scroll) :

![Mastodon - Filtrer les posts selon les langues](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_langues_posts.webp){: .img-center loading=lazy }

### Suivre des mots-clés

Par exemple, pour voir les posts qui intègrent le hashtag mot-dièse `#cartographie` :

1. Se rendre sur <https://mapstodon.space/tags/cartographie>
1. Cliquer sur le bouton `Suivre le hashtag`

![Mastodon -Suivre un hashtag](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_hashtags_suivre_cartographie.webp){: .img-center loading=lazy }

Renouveler l'opération avec d'autres hashtags. Par exemple :

- [géographie](https://mapstodon.space/tags/g%C3%A9ographie)
- [GIS](https://mapstodon.space/tags/GIS)
- [SIG](https://mapstodon.space/tags/SIG)
- [géomatique](https://mapstodon.space/tags/g%C3%A9omatique)
- [saucisse](https://mapstodon.space/tags/saucisse), mais non il ne fallait pas cliquer sur celui-là !

Enfin bref, vous avez compris l'idée quoi.

----

## Remplir la vacuité : importer des comptes et listes à suivre

![icône globe social](https://cdn.geotribu.fr/img/internal/icons-rdp-news/social.png "icône globe social"){: .img-thumbnail-left }

Pour éviter le sentiment de vide et remise à zéro de son réseau, il est recommandé d'importer des listes de comptes. C'est minimaliste, ça prend littéralement 5 minutes (Mastodon utilise le format CSV) et ça permet d'avoir un "kit de démarrage" sur le réseau.  
Je vous partage la _curated list_ de comptes et listes francophones prêts à l'emploi. Je vous mets aussi ceux de comptes internationaux.

### _Curated_ par Geotribu : option comptes francophones { #import-comptes-geotribu }

Si vous voulez seulement suivre les comptes sans récupérer les listes, suivez ces étapes :

1. Télécharger le fichier des comptes suivis par Geotribu :

    [:material-account-eye: Télécharger le CSV des comptes sélectionnés par Geotribu](https://cdn.geotribu.fr/img/download/mastodon_comptes_suivis_geotribu.csv){: target="_blank" download=mastodon_comptes_suivis_geotribu.csv .md-button }
    {: align=middle }

1. Sur votre instance Mastodon, se rendre dans votre profil et dans le menu `Import et export` > `Import` ou directement <https://mapstodon.space/settings/imports> si vous êtes sur l'instance [Mapstodon].
1. Choisir **`Listes de comptes suivis`** en haut, sélectionner le fichier CSV téléchargé précédemment (a priori `mastodon_comptes_suivis_geotribu.csv`) :

    ![Mastodon - Interface d'import de comptes suivis](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_import_comptes.webp){: .img-center loading=lazy }

1. Cliquer sur le gros bouton `Importer` et confirmer sur le dialogue suivant :

    ![Mastodon - Confirmation d'import de comptes suivis](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_import_comptes_confirmation.webp){: .img-center loading=lazy }

### _Curated_ par Geotribu : option listes de comptes { #import-listes-geotribu }

Si en plus des comptes, vous avez envie d'importer les listes, c'est-à-dire comment les comptes sont organisés, c'est par ici que ça se passe :

![Mastodon - Listes du compte Geotribu](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_listes_geotribu.webp){: .img-center loading=lazy }

1. Télécharger le fichier des listes :

    [:material-format-list-bulleted-type: Télécharger les listes de comptes de Geotribu](https://cdn.geotribu.fr/img/download/mastodon_listes_geotribu.csv){: target="_blank" download=mastodon_listes_geotribu.csv .md-button }
    {: align=middle }

1. Sur votre instance Mastodon, se rendre dans votre profil et dans le menu `Import et export` > `Import` ou directement <https://mapstodon.space/settings/imports> si vous êtes sur l'instance [Mapstodon].
1. Choisir **`Listes`** en haut, sélectionner le fichier CSV téléchargé précédemment (a priori `mastodon_listes_geotribu.csv`) :

    ![Mastodon - Interface d'import des listes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_import_listes.webp){: .img-center loading=lazy }

1. Cliquer sur le gros bouton `Importer` et confirmer sur le dialogue suivant :

    ![Mastodon - Confirmation d'import des listes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_import_listes_confirmation.webp){: .img-center loading=lazy }

### Comptes internationaux

#### _Curated by_ Florian Ledermann

L'écosystème propose un générateur de micro site web, [Mastodon Sociologists](https://github.com/trutzig89182/Mastodon-Sociologists), qui permet d'exporter des listes de comptes en choisissant en amont. Florian Ledermann, compatriote autrichien d'Anita, a pris une initiative assez tôt pour héberger une copie focalisée sur les comptes liés à la cartographie !

Allez, petit tutoriel rapide pour les moins aventureux/ses :
<!-- markdownlint-disable MD051 -->
1. Se rendre sur [le site de Florian Ledermann](https://cartolab.at/cartography-on-mastodon/)
1. Sélectionner les catégories qui vous intéressent. Il est aussi possible de sélectionner compte par compte mais si vous êtes rendus là c'est que vous n'êtes pas ce genre de forçat :grin:. Personnellement, je commence par tout déselectionner (`Select none`) puis je clique sur les `Select all` en regard des catégories `Cartography, geovisualization and visual aspects of GIS`, `GIS, geodata and geography` et `General information visualization & data science` ce qui, à date, représente 208 des 245 comptes répertoriés :

    ![Listes de comptes à suivre - Florian Ledermann](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_listes_Florian_Ledermann.webp){: .img-center loading=lazy }

1. Cliquer sur `Download selected as CSV`
1. Suivre la [procédure d'import décrite plus haut](#import-comptes-geotribu) à partir du point 2 mais en sélectionnant le fichier CSV téléchargé ici
<!-- markdownlint-enable MD051 -->

#### _Curated by_ Anita Graser

Il n'y a pas si longtemps, [Anita Graser](https://fr.wikipedia.org/wiki/Anita_Graser) a également publié la liste des comptes qu'elle recommande [sous forme de Gist](https://gist.github.com/anitagraser/a37118d74b839602e0f474375f548dfd) :

<!-- markdownlint-disable MD051 -->
1. Cliquer sur `Download ZIP` en haut à droite
1. Dézipper puis refaire la [procédure d'import décrite plus haut](#import-comptes-geotribu) à partir du point 2 mais en sélectionnant le fichier CSV téléchargé ici
<!-- markdownlint-enable MD051 -->

Le mieux est encore de consulter [l'article de son blog](https://anitagraser.com/2024/02/03/finding-geospatial-accounts-on-mastodon/ "Finding geospatial accounts on Mastodon").

----

## Soutenir l'instance Mapstodon

Enfin, si vous pensez l'utiliser, sachez que [Mapstodon] a été créé par l'ami [Jérémy](https://mapper.fr/) et qu'à ce titre c'est son compte en banque qui est débité à chaque message posté, requête envoyée etc. Si vous en avez les moyens, donnez donc 1€/mois pour contribuer à la viabilité de cet espace qui ne se finance ni tout seul, ni en revendant nos données personnelles ou de l'espace publicitaire.

![Page Patreon pour l'instance Mapstodon](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mapstodon_patreon.webp){: .img-center loading=lazy }

[Aider à financer Mapstodon :fontawesome-solid-hand-holding-heart:](https://patreon.com/mapstodon?utm_medium=ref_geotribu&utm_source=copyLink&utm_campaign=geotribu_article&utm_content=join_link){: .md-button }
{: align=middle }

----

## À bientôt sur Mastodon

J'espère que ces quelques étapes vous auront aidé à franchir les premières barrières et que vous viendrez diversifier mon fil.

Si l'article vous a intéressé et aidé à embarquer, venez donc le dire en réponse au post sur Mapstodon qui le diffusera. Si vous êtes assez actif/ve et publiez principalement sur la géo ou la carto, on vous ajoutera à nos listes de comptes :wink:.

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

{% include "licenses/beerware.md" %}

<!-- Abbréviation -->
*[curated list]: une curated list désigne une liste triée avec soin en vue de fournir un ensemble de ressources ciblées aux utilisateurs.
