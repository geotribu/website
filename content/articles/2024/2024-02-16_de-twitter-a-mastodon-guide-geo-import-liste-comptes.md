---
title: "De Twitter (X) à Mastodon : guide pour les géomaticien/nes"
subtitle: En attendant l'avènement du Y
authors:
    - Julien Moura
categories:
    - article
comments: true
date: 2024-02-16
description: En 2024, faire de la veille en géomatique sur Twitter/X devient pénible. Guide à destination des géo* qui veulent embarquer dans l'aventure Mastodon.
icon: material/mastodon
image:
license: beerware
robots: index, follow
tags:
    - Mastodon
    - réseaux sociaux
    - Twitter
---

# Embarquer dans Mastodon : guide pour les géo*

:calendar: Date de publication initiale : 16 février 2024

## Introduction

![logo Mastodon](https://cdn.geotribu.fr/img/logos-icones/social/mastodon.png){: .img-thumbnail-left }

Bonjour.  
Nous sommes en 2024 et il est temps de faire de [X (Twitter)](https://x.com/geotribu) un réseau social secondaire.  
Peur de sauter par-dessus bord ? Je comprends.  
Voici un guide pour atterrir en douceur sur le réseau décentralisé Mastodon.  
Peur d'un énième guide ? Je comprends.  
Ce guide est fait sur mesure pour les cartographes, géomaticiennes, géomaticiens et même pour les sigistes ! Oui, même pour les sigistes.
Impressionné/e ? Je comprends.

Je comprends sincèrement que :

- l'inertie est forte,
- que sortir de sa zone de confort avec les habitudes et followers acquis ces dernières années est contre-nature,
- que maintenir une présence sur les réseaux sociaux est déjà suffisamment chronophage pour ne pas s'en rajouter,
- que l'émiettement des plateformes est douloureux et également chronophage,
- qu'il est tentant de faire de LinkedIn sa page d'accueil malgré la part toujours plus importante de contenus _bullshités_ à l'IA,
- que les concepts sous-jacents à Mastodon et tous ces machins de Fediverse font plus penser à un kif de geeks qui ont transposé leurs fantasmes des univers de super-héros dans leurs outils du quotidien mais qu'on n'a pas que ça à faire de configurer ceci, paramétrer cela, lancer telle commande, etc.

Je comprends. Vraiment. Oui, même si c'est contre ma propre nature de géogeek justement. :wink:  
Mais je suis persuadé qu'il y a un intérêt à peupler ce réseau social de gens plus diversifiés que ceux qui vont presque naturellement sur Mastodon au risque d'en faire justement une bulle d'écho entre technophiles plutôt de gauche ; comme BlueSky semble l'être pour le monde universitaire / CSP+... et t**X**itter celle des réactionnaires.

Essayez. Ça n'engage à rien. Vraiment.  
Laissez vous guider, ça va bien se passer.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Choisir où créer son compte

![icône poignée de main](https://cdn.geotribu.fr/img/internal/icons-rdp-news/lobby.png){: .img-thumbnail-left }

Vous avez 3 options. Seulement 3 ? Oui, vous n'êtes pas là pour avoir trop de choix, vous éparpiller ou perdre du temps à tout piger le fediverse et tous les mots-clés qui nous excitent nous autres geeks de l'hyperespace !

Donc 3 options disais-je :

- [**mapstodon.space**](https://mapstodon.space/) : celle qu'il vous faut (dont nous parlions dès [novembre 2022](../../rdp/2022/rdp_2022-11-18.md#mapstodonspace)). Vous pouvez ignorer les deux suivantes si vous avez geo ou carto quelque part en haut de votre CV.
- [fosstodon.org](https://fosstodon.org/) : si vous êtes sous licence GPL2+.
- [mastodon.social](https://mastodon.social/) : l'instance principale, si vous voulez un max de liberté et un facteur de dispersion élevé.

[:material-sign-direction: Créer son compte sur Mapstodon.space](https://mapstodon.space/auth/sign_up){: .md-button .md-button--primary }
{: align=middle }

Pour la suite, c'est du très classique :

1. Lire et accepter les règles du serveur : pas de harcèlement, pas de prosélytisme idéologico-religieux, pas de pub commerciale excessive
1. Choisir son pseudo (spoiler : `geotribu` est déjà pris)
1. Choisir son mot de passe, par exemple :

    ```txt
    12345678motdepasse
    ```

1. Si vous avez cliqué sur le bouton :material-content-copy: ou vraiment copié le texte ci-dessus, voici les étapes à suivre calmement : revenir sur vos pas, souffler et utiliser le générateur de mot de passe de votre navigateur ou gestionnaire idoine.
1. Mettre un court texte pour l'équipe de modération. Comme je suis sympa, copier le suivant :

    ```txt
    Je viens de la part de Julien (@geojulien@mapstodon.space), une des personnes qui écrit sur Geotribu (@geotribu@mapstodon.space).  
    Vu que je travaille ou m'intéresse à la géomatique, il semble que cette instance soit la meilleure option.
    ```

----

## Premiers pas

Quelques grandes étapes à suivre aveuglément (même si je ne suis pas borgne) pour bien démarrer dans votre nouvelle vie sociale.

### Définir la langue d'affichage et les paramètres généraux

1. Se rendre dans les préférences d'apparence ([raccourci Mapstodon](https://mapstodon.space/settings/preferences/appearance))
1. Boum, c'est juste là :

![Mastodon - Changer les paramètres d'affichage](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_langue_interface.webp){: .img-center loading=lazy }

!!! tip "Tankaf"
    Tant qu'à être sur cette page de réglages, vous pouvez aussi en profiter pour activer le mode "_TweetDeck_" :
    ![Mastodon - Activer le mode multicolonnes à la TweetDeck](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_interface_deck_option.webp){: .img-center loading=lazy }

### Filtrer sur les langues des posts

1. Se rendre dans les préférences dites "autres" ([raccourci Mapstodon](https://mapstodon.space/settings/preferences/other))
1. Cocher les cases des langues que vous souhaitez voir affichées (oui je sais, c'est la fête du scroll) :

![Mastodon - Filtrer les posts selon les langues](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_langues_posts.webp){: .img-center loading=lazy }

!!! tip "Tankaf"
    Tant qu'à être sur cette page de réglages, vous pouvez aussi en profiter pour régler la visibilité de vos publications :
    ![Mastodon - Régler la confidentialité des messages](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_option_confidentialite.webp){: .img-center loading=lazy }

----

## Importer des comptes et listes à suivre

![icône globe social](https://cdn.geotribu.fr/img/internal/icons-rdp-news/social.png "icône globe social"){: .img-thumbnail-left }

Pour éviter le sentiment de vide et remise à zéro de son réseau, il est recommandé d'importer des listes de comptes. C'est minimaliste, ça prend littéralement 5 minutes (Mastodon utilise le format CSV) et ça permet d'avoir un "kit de démarrage" sur le réseau.  
Je vous partage la _curated list_ de comptes et listes francophones prêts à l'emploi utilisés par le compte Geotribu. Je vous mets aussi ceux de comptes internationaux plus bas.

Parmi tous les comptes suivis par Geotribu (353 à date), on ajoute certains à des listes (voir ci-dessous) pour faciliter la veille sur la base de quelques critères arbitraires :

- les publications sont majoritairement francophones (sauf pour la liste "Outils, logiciels, bibliothèques...")
- les publications sont majoritairement liées à la géomatique (pour éviter la "pollution" avec les posts politiques, chats, photos de paysage, etc.)
- les publications sont majoritairement des contenus originaux ou du moins pas des liens vers des sites déjà suivis par ailleurs

![Mastodon - Listes du compte Geotribu](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_listes_geotribu.webp){: .img-center loading=lazy }

### _Curated_ par Geotribu : listes de comptes { #import-listes-geotribu }

Si en plus des comptes, vous avez envie d'importer les listes, c'est-à-dire comment les comptes sont organisés, c'est par ici que ça se passe :

1. Télécharger le fichier des listes :

    [:material-format-list-bulleted-type: Télécharger les listes de comptes de Geotribu](https://geotribu.github.io/geo-mastodon-comptes-listes/mastodon_listes_geotribu.csv){: target="_blank" download=mastodon_listes_geotribu.csv .md-button }
    {: align=middle }

1. Sur votre instance Mastodon, se rendre dans votre profil et dans le menu `Import et export` > `Import` ou directement <https://mapstodon.space/settings/imports> si vous êtes sur l'instance [Mapstodon].
1. Choisir **`Listes`** en haut, sélectionner le fichier CSV téléchargé précédemment (a priori `mastodon_listes_geotribu.csv`) :

    ![Mastodon - Interface d'import des listes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_import_listes.webp){: .img-center loading=lazy }

1. Cliquer sur le gros bouton `Importer` et confirmer sur le dialogue suivant :

    ![Mastodon - Confirmation d'import des listes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_import_listes_confirmation.webp){: .img-center loading=lazy }

### _Curated_ par Geotribu : comptes francophones { #import-comptes-geotribu }

Si vous voulez seulement suivre les comptes sans récupérer les listes, suivez ces étapes :

1. Télécharger le fichier des comptes suivis par Geotribu et ajoutés aux listes :

    [:material-account-eye: :material-format-list-bulleted-type: Télécharger les comptes sélectionnés dans les listes Geotribu](https://geotribu.github.io/geo-mastodon-comptes-listes/mastodon_comptes_des_listes_geotribu.csv){: target="_blank" download=mastodon_comptes_des_listes_geotribu.csv .md-button }
    {: align=middle }

1. Sur votre instance Mastodon, se rendre dans votre profil et dans le menu `Import et export` > `Import` ou directement <https://mapstodon.space/settings/imports> si vous êtes sur l'instance [Mapstodon].
1. Choisir **`Listes de comptes suivis`** en haut, sélectionner le fichier CSV téléchargé précédemment (a priori `mastodon_comptes_suivis_geotribu.csv`) :

    ![Mastodon - Interface d'import de comptes suivis](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_import_comptes.webp){: .img-center loading=lazy }

1. Cliquer sur le gros bouton `Importer` et confirmer sur le dialogue suivant :

    ![Mastodon - Confirmation d'import de comptes suivis](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mastodon_import_comptes_confirmation.webp){: .img-center loading=lazy }

Si vous êtes du genre sans filtre ou que notre sélection vous semble trop restreinte, vous pouvez aussi importer la liste de **tous les comptes** suivis par Geotribu avec la même procédure :

[:material-account-eye: Télécharger tous les comptes suivis par Geotribu](https://geotribu.github.io/geo-mastodon-comptes-listes/mastodon_comptes_suivis_geotribu.csv){: target="_blank" download=mastodon_comptes_suivis_geotribu.csv .md-button }
{: align=middle }

### Comptes internationaux

#### _Curated by_ Florian Ledermann

L'écosystème propose un générateur de micro site web, [Mastodon Sociologists](https://github.com/trutzig89182/Mastodon-Sociologists), qui permet d'exporter des listes de comptes en choisissant en amont. Florian Ledermann, compatriote autrichien d'Anita, a pris une initiative assez tôt pour héberger une copie focalisée sur les comptes liés à la cartographie !

Allez, petit tutoriel rapide pour les moins aventureux/ses :
<!-- markdownlint-disable MD051 -->
1. Se rendre sur [le site de Florian Ledermann](https://cartolab.at/cartography-on-mastodon/)
1. Sélectionner les catégories qui vous intéressent. Il est aussi possible de sélectionner compte par compte, mais si vous êtes rendus là c'est que vous n'êtes pas ce genre de forçat :grin:. Personnellement, je commence par tout désélectionner (`Select none`) puis je clique sur les `Select all` en regard des catégories `Cartography, geovisualization and visual aspects of GIS`, `GIS, geodata and geography` et `General information visualization & data science` ce qui, à date, représente 208 des 245 comptes répertoriés :

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

Le mieux est encore de consulter [l'article de son blog](https://anitagraser.com/2024/02/03/finding-geospatial-accounts-on-mastodon/ "Finding geospatial accounts on Mastodon")

----

## Suivre des mots-clés

En plus de suivre des gens ou personnes morales, il est possible de suivre des hashtags. Ce qui est pratique pour suivre des sujets en particulier. Par exemple, pour voir les posts qui intègrent le hashtag mot-dièse `#cartographie` :

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

## Soutenir l'initiative Mapstodon

Enfin, si vous pensez l'utiliser, sachez que [Mapstodon] a été créé par l'ami [Jérémy](https://mapper.fr/) et qu'à ce titre c'est son compte en banque qui est débité à chaque message posté, requête envoyée, etc. Si vous en avez les moyens, donnez donc 1€/mois pour contribuer à la viabilité de cet espace qui ne se finance ni tout seul, ni en revendant nos données personnelles ou de l'espace publicitaire.

[Aider financièrement à viabiliser Mapstodon :fontawesome-solid-hand-holding-heart:](https://fr.liberapay.com/mapper/?utm_medium=ref_geotribu&utm_source=copyLink&utm_campaign=geotribu_article&utm_content=join_link){: .md-button }
{: align=middle }

![Page Liberapay pour l'instance Mapstodon](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/transition_mastodon/mapstodon_liberapay.webp){: .img-center loading=lazy }

----

## À bientôt sur Mastodon

J'espère que ces quelques étapes vous auront aidé à franchir les premières barrières et que vous viendrez diversifier mon fil :smile:.

Si l'article vous a intéressé et aidé à embarquer, venez donc le dire en réponse au post sur Mapstodon qui le diffusera. Si vous êtes assez actif/ve et publiez principalement sur la géo ou la carto, on vous ajoutera à nos listes de comptes :wink:.

<iframe src="https://mapstodon.space/@geotribu/111940866730305818/embed" class="mastodon-embed" loading="lazy" style="max-width: 100%; border: 0; display: block" width="600" allowfullscreen="allowfullscreen"></iframe>

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}

<!-- Abbréviation -->
*[curated list]: une curated list désigne une liste triée avec soin en vue de fournir un ensemble de ressources ciblées aux utilisateurs.
*[Tankaf]: contraction "millenial" de "Tant qu'à faire"
