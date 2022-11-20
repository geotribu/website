---
title: "Héberger des images"
subtitle: Guide d'utilisation de notre service d'hébergement des images
authors:
    - Julien MOURA
categories:
    - article
    - meta
date: 2022-11-22 10:20
description: "Sous le GéoCapot : gérer l'hétérogénéité des contributions et garantir une qualité minimale, des git hooks sont à l'oeuvre sur Geotribu. Explication de leur fonctionnement."
icon: material/image-search
image: "https://cdn.geotribu.fr/img/internal/contribution/git_hooks/pre-commit_ci_result_master.png"
robots: index, follow
tags:
    - cdn
    - coulisses
    - images
---

# Héberger des images sur Geotribu

Le terme CDN est ici bien sûr abusif mais c'est ainsi que nous désignons notre hébergement et gestionnaire de fichiers medias statiques.

Traditionnellement, nous hébergeons les images sur notre propre serveur pour plusieurs raisons :

- ça évite de surcharger les serveurs des autres sites en pointant dessus
- ça évite les restrictions liées au "partage de ressources entre origines multiples", enfin le [CORS](https://fr.wikipedia.org/wiki/Cross-origin_resource_sharing) quoi
- ça permet de garantir de toujours disposer des images, même si elles n'existent plus à l'adresse originale (site supprimé, refonte du site, etc.)

!!! important "Fair-use"
    L'accès au CDN de Geotribu est réservé à l'équipe. Même si nous laissons les liens vers les images en public, merci de ne pas pointer dessus abusivement depuis d'autres sites.

----

## Structure

Globalement, voici comment les images sont organisées :

- racine : :rotating_light: éviter d'ajouter de nouvelles images ici :rotating_light:
- articles-blog-rdp :
    - captures d'écrans utilisées pour illustrer une revue de presse
- external
- internal : ressources propres au site.
    - charte graphique
    - photos des contributeurs : nommage avec initiale du prénom et 3 premières lettres du nom
    - images liées à la section contribution du site, de cet article entre autres (captures d'écran, exemples, etc.)
    - icônes créées par Geotribu pour symboliser le sujet d'une news d'une revue de presse
- logos-icones : entreprises, associations, logiciels, librairies, technologies, etc. Idéales pour l'icône d'une news de revue de presse.
- projets-geotribu
- slideshow : images du diaporama sur l'ancien site de Geotribu. Elles étaient pour la plupart pré-découpées en rectangle mais ça peut toujours servir à ds fins d'illustration. :rotating_light: éviter d'ajouter de nouvelles images ici :rotating_light:.
- tuto : contenus liés aux tutoriels publiés. Un sous-dossier par tutoriel.

----

## Bonnes pratiques

Sur le site historique de Geotribu, la difficile gestion des images a laissé un héritage chaotique : doublons en pagaille (jusqu'à 10 exemplaires dans certains cas...), noms d'images abscons rendant impossible la recherche, caractères spéciaux, dimensions démesurées (qui avait même provoqué un crash du serveur à l'époque :boom: !), etc.

Merci de suivre au mieux ces recommandations qui permettent de garantir une utilisation sereine des mêmes ressources par plusieurs personnes :pray: :

- chercher d'abord si l'image n'existe pas déjà (voir structure du CDN)
- redimensionner les images avant de les téléverser (= _uploader_) : 800px maximum en largeur ou en hauteur sont largement suffisants pour illustrer un article ou une news sur Geotribu.
- utiliser des formats avec de bons niveaux de compression :
    - [SVG](https://fr.wikipedia.org/wiki/Scalable_Vector_Graphics)
    - [WebP](https://fr.wikipedia.org/wiki/WebP)
    - [PNG](https://fr.wikipedia.org/wiki/Portable_Network_Graphics)
    - [JPEG](https://fr.wikipedia.org/wiki/JPEG)
    - :no_entry_sign: à éviter Bitmap, Tiff, etc.
- nommer proprement les fichiers :
    - choisir un nom explicite qui permette la recherche par d'autres : `carte_densite_nyt.jpg` plutôt que `0f1f4706b8f1ea520747e3fd231a5bd0.jpg` (ce dernier exemple n'est pas une invention spontanée, il correspond réellement à une image stockée dans le CDN...)
    - pas de caractères spéciaux (espaces, accents, etc.)

Ce n'est évidemment pas exhaustif et il n'y a pas de brigade des images dans l'équipe, on s'en remet donc au bon sens de chacun/e :slightly_smiling_face:.

----

## Pas à pas

1. Se connecter au gestionnaire de fichiers en ligne : <https://cdn.geotribu.fr/>

    ![Tiny File Manager - Formulaire d'authentification](https://cdn.geotribu.fr/img/internal/contribution/embed_image/cdn_filemanager_authform.png "Tiny File Manager - Formulaire d'authentification")

    > l'identifiant et mot de passe sont transmis sur demande par mail, MP Mastodon/Twitter, etc.

2. Utiliser la recherche pour savoir si jamais une image correspond au besoin
3. Se positionner dans le dossier souhaité
4. Cliquer sur :cloud: `Envoyer`
5. Glisser/déposer ou sélectionner l'image

    ![Téléverser une image](https://cdn.geotribu.fr/img/internal/contribution/embed_image/cdn_filemanager_upload.png)

6. Cliquer `Retour` et récupérer l'URL de l'image. Par exemple, avec un clic droit sur l'icône de lien ou en cliquant sur l'image puis sur `Ouvrir``

    ![Clic doit copier l'adresse du lien](https://cdn.geotribu.fr/img/internal/contribution/embed_image/cdn_filemanager_get_image_url.png "Clic doit copier l'adresse du lien")

----

## Ressources

- [EzGIF](https://ezgif.com/resize/) pour manipuler, redimensionner et optimiser les GIF en ligne
- [ImageOptim](https://imageoptim.com/), opimisation des JPEG et PNG
- [Reshot](https://www.reshot.com/), icônes et images libres de droits
- [TinyPNG](https://tinypng.com/), optimisation des images JPEG, PNG, WebP...
