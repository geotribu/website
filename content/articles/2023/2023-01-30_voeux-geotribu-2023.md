---
title: Voeux 2023 et bilan 2022
subtitle: Calmement, se remémorant chaque changement
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2023-01-30
description: La tribu vous adresse ses meilleurs voeux à toutes et tous les visiteurs du géotipi. Petit retour sur 2022 pour attaquer au mieux 2023.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/bonne_annee/geotribu_2023.png
license: default
tags:
    - Geotribu
---

# Voeux 2023 et bilan 2022

:calendar: Date de publication initiale : 30 janvier 2023

## Introduction

![logo tipi Geotribu](https://cdn.geotribu.fr/img/internal/charte/geotribu_logo_tipi_seul_carre.png){: .img-thumbnail-left }

Bienvenue sur le traditionnel, mais non moins irrégulier (du moins à Geotribu), billet de bilan de l'année passée et de projection sur l'année qui s'amorce.

On continue notre petit bonhomme de chemin, à coups de veille sur notre écosystème, d'articles plus ou moins légers sur des sujets plus ou moins lourds, mais souvent techniques. On aime à croire que nous documentons ici une partie, certes partiale, émergée et infime, de ce qu'est la géomatique aujourd'hui en regardant vers ce qu'elle sera demain.

On peut ainsi voir dans nos contenus et dans leur audience comme un miroir des tendances notre géo-époque, où les outils de saisie terrain, les vues immersives et les tableaux de bord (_dashboard_) occupent les esprits. Les thématiques sociétales impactent également comme toujours un secteur d'activité au plus proche du réel : environnement, intelligence artificielle... mais aussi la guerre en Europe avec les répliques qu'elle a occasionnées jusque dans les communautés open source (Leaflet) et open data (OpenStreetMap).  

Malgré tout, le flux continu apporte son lot de projets excitants et pour certains attendus depuis longtemps (coucou la Géoplateforme) et on aborde donc 2023 plein d'entrain et d'envie, en route vers nos 15 ans d'existence... Putain. 15 ans.

Merci à toustes de nous suivre et en particulier à celles et ceux qui prennent le temps de saluer le travail bénévole qui est fait ici, à travers les commentaires ou autres moyens. Cela fait toujours plaisir aussi de voir autant de personne venir contribuer ou simplement consulter et partager nos contenus !

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Meilleurs voeux pour 2023 de la part de Geotribu !

![Bonne année 2023](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/bonne_annee/geotribu_2023.png "Bonne année 2023"){: .img-center loading=lazy }

!!! info
    Carte de voeux réalisée avec [PostgreSQL/PostGIS (fonction ST_Letters)](https://www.crunchydata.com/blog/fun-with-letters-in-postgis-33) et QGIS.

----

## Rétrospective 2022

Découvrez la rétrospective des contributions réalisée à partir de l'historique Git du dépôt Geotribu :

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/mbDAz9aAVW8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### Contenus

![Top 10 des contenus 2022](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/bonne_annee/analytics_2022_contenus_1.webp){: .img-right loading=lazy width=40% }

- 16 articles publiés de 13 auteurs différents, mais dont 1 seule autrice
- 23 revues de presse publiées, conformément à notre rythme d'une toutes les 2 semaines modulo les vacances
- 43 news proposées par des personnes externes via [le formulaire](https://github.com/geotribu/website/issues/new?assignees=Guts&labels=contribution+externe%2Crdp%2Ctriage&template=RDP_NEWS.yml). Un remerciement chaleureux et particulier à Delphine Montagne qui s'est tellement emparée de cet outil qu'elle a plus de news à son actif que des membres "internes" !
- tous les nouveaux contenus liés au guide de contribution et à l'outillage interne (série "[sous le #GéoCapot](https://twitter.com/hashtag/G%C3%A9oCapot?src=hashtag_click&f=live)")
- tous les contenus historiques republiés et qu'on a tenté de valoriser via [la série #GéoSouvenir](https://twitter.com/hashtag/G%C3%A9oSouvenir?src=hashtag_click&f=live) sur Twitter

### Audience

![Seuil des 1500 clics par mois dans les résultats Google Search](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/bonne_annee/seo_google_search_1500_mois.webp){: .img-left loading=lazy width="30%" }

- même tronquées par les bloqueurs de pubs/trackers (oui on utilise toujours Google Analytics), les statistiques de fréquentation sont en légère hausse +/- constante et vont en stabilisant
- grosse progression du côté du référencement, notamment grâce à la correction des contenus et à leur mise en conformité avec les standards actuels
- à noter que les contenus sont de moins en moins repartagés au moment de la diffusion sur les réseaux sociaux. En gros, les gens cliquent sur le lien mais ne repartagent que plus rarement. L'éclatement de la bulle Twitter au profit de Mapstodon a également réduit la portée des mesures.

![Sources des visites Geotribu 2022](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/bonne_annee/analytics_2022_sources_acquisitions.webp){: .img-center loading=lazy }
![Nombre de visiteurs](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/bonne_annee/analytics_2022_audience.webp){: loading=lazy width="30%" } ![Pages vues Geotribu 2022](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/bonne_annee/analytics_2022_contenus_2.webp){: loading=lazy width=30% }
{: align=middle }

![Evolution abonnés à la newsletter Geotribu sur 2022](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/bonne_annee/newsletter_mailchimp_1_an_apres.webp){: .img-right loading=lazy width="30%" }

- :incoming_envelope: on a passé la barre des 250 inscrits à [la newsletter](../../newsletter/signup.md) dont 215 à l'envoi hebdomadaire. Pour rappel :
    - si vous vous êtes abonné/e et que vous ne lisez plus, ne cliquez jamais ou n'êtes plus intéressé/e : prenez 5 minutes pour vous [désabonner](https://geotribu.us5.list-manage.com/unsubscribe/post). Sérieusement, ça fera des mails perdus en moins :pray:.
    - si vous pensez que vos collègues pourraient être intéressé/es, faites tourner :wink:

### Fonctionnalités

- :fontawesome-solid-signature: les avatars GitHub des principaux contributeur/ices d'une page sont automatiquement ajoutés en bas de page
- :frame_photo: ajout du [plugin mkdocs-glightbox](https://blueswen.github.io/mkdocs-glightbox/) pour appliquer un mode galerie à toutes les images par défaut. Vous savez, quand on clique sur une image et que ça l'agrandit en floutant le site à l'arrière-plan et en permettant de naviguer d'une image à l'autre ? Avant c'était ~~galère~~ exigeant de faire ça dans un contenu Geotribu, maintenant y'a rien à faire. Plus d'information dans [le guide de contribution]({{ config.extra.url_contribuer }}/guides/image/#lightbox-mode-galerie).
- :heartpulse: il est désormais possible de montrer son amour d'un contenu sans avoir à écrire de commentaire. Idéal pour les timides qui souhaiteraient quand même remercier les auteur/ices :wink:.
- :material-puzzle: notre [plugin QGIS](https://plugins.qgis.org/plugins/qtribu/) est désormais publié dans le dépôt officiel des extensions pour que son installation soit plus facile
- :robot: un robot pré-mâche le travail d'intégration des news proposées via le formulaire GitHub ([voir cet exemple](https://github.com/geotribu/website/issues/703#issuecomment-1256246426))
- :label: ajout d'icônes aux mots-clés (travail en cours) et légère amélioration du design
- :factory_worker: des évolutions sous le capot du site notamment liées au thème [Material for Mkdocs](https://squidfunk.github.io/mkdocs-material/insiders/) dont on contribue à financer la version payante (_Insiders_) via notre [Tipeee](https://fr.tipeee.com/geotribu).
- les prévisualisations générées automatiquement pour chaque nouveau contenu sont désormais supprimées dès que le contenu est publié.
- :carousel_horse: Julien a également travaillé sur la compatibilité des contenus Géotribu avec le web sémantique en générant automatiquement des données structurées au format JSON-LD dans les pages HTML. Pour en savoir plus sur [ce qui se passe sous le géocapot c'est par ici]({{ config.extra.url_contribuer }}internal/seo_extraits_enrichis/).

![Widget en bas d'article pour soutenir](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/bonne_annee/widget_feedback.webp){: .img-center loading=lazy }

### Architecture et coûts de fonctionnement

- :mirror: pour améliorer notre résilience et réduire notre adhérence à GitHub, on a mis en place [un site miroir](https://fr.wikipedia.org/wiki/Site_miroir#Nom_de_domaine) sur <https://www2.geotribu.fr> (synchronisé quotidiennement), hébergé sur le serveur prêté par GeoRezo
- :fontawesome-solid-server: migration de serveur (merci GeoRezo !) : CDN, commentaires et mécanisme de sauvegarde sont déjà sur le nouveau serveur. Au passage, on en profite pour rendre le déploiement de notre infrastructure reproductible avec Ansible. Pour les curieux, ça se passe sur [ce dépôt GitHub](https://github.com/geotribu/infra).

Pour rappel, une grande partie de nos ressources informatiques est fournie par l'association GeoRezo. Prenez donc 5 minutes et 10€ pour soutenir tout ce que ce portail fait depuis longtemps et encore aujourd'hui :

[Faire un don à GeoRezo :fontawesome-solid-hand-holding-heart:](https://www.helloasso.com/associations/georezo-le-portail-geomatique/formulaires/1/widget){: .md-button }
{: align=middle }

Vous pouvez également [nous soutenir directement, ponctuellement ou de façon récurrente](https://fr.tipeee.com/geotribu/) ou [sur Liberapay](https://liberapay.com/Geotribu/). L'an passé, principalement grâce à Arnaud, Gabriel, Florian et Julien, nous avons récolté à peine plus que nos frais de fonctionnement :

[![Contreparties Tipeee Geotribu](https://cdn.geotribu.fr/img/internal/sponsoring/tipeee_contreparties.webp){: .img-center .off-glb loading=lazy }](https://fr.tipeee.com/geotribu/)

### Nettoyage et historique

Fin 2021, nous attaquions l'homogénéisation et l'assainissement des contenus anciens. Ce travail de reprise chronophage s'est échelonné tout au long de l'année 2022 avec de nombreux ajustements sur :

- le markdown : niveau des titres, mise en valeur du code, suppression des anciennes ancres, retraits en début de ligne
- l'intégration des icônes et images manquantes.

![Réduction des erreurs 404 sur le dernier trimestre 2022](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/bonne_annee/seo_404_nettoyage_2023.webp){: loading=lazy width=30% }
![Ergonomie mobile Geotribu 2022](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/bonne_annee/ergonomie_mobile_2022.webp){: loading=lazy width=30% } ![Ergonomie ordinateur Geotribu 2022](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/bonne_annee/ergonomie_ordinateur_2022.webp){: loading=lazy width=30% }
{: align=middle }

----

## Perspectives 2023

### Objectifs

- [ ] tenir le rythme d'une revue de presse toutes les 2 semaines (hors déserts vacanciers français)
- [ ] trouver des autrices d'articles
- [ ] diversifier les auteurs
- [ ] publier plus d'un article par mois
- [ ] intégrer les derniers contenus historiques manquants
- [ ] harmoniser les tags et les textes de remplacement sur les icônes

### Evolutions

On a d'ores et déjà quelques annonces à faire :

- le site changera d'adresse d'ici le printemps : fin du sous-domaine `static`, le site retourne à la racine `https://geotribu.fr/` ou peut-être sur le sous-domaine `www`. Préparez vos favoris, marque-pages, etc.
- la section dédiée à la contribution a désormais son propre site web : <https://contribuer.geotribu.fr/>
- optimiser automatiquement les images hébergées (redimensionnement et compression) pour réduire la friction lors de la contribution

----

<!-- geotribu:authors-block -->
