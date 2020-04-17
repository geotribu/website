---
title: Intégrer une image
category: contribution
date: 2020-04-20 10:20
tags: contribuer,media,image,intégration,tutoriel,cdn
---

# Intégrer une image

Prenons deux exemples :

- une image _externe_, c'est-à-dire hébergée ailleurs que sur le [CDN de Geotribu] : <https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Coronelli_globe_terrestre.jpg/360px-Coronelli_globe_terrestre.jpg> du **globe terrestre** de Coronelli, issue de cette page Wikipedia <https://fr.wikipedia.org/wiki/Globes_de_Coronelli>
- une image _interne_, hébergée sur le [CDN de Geotribu] : <https://cdn.geotribu.fr/images/internal/contribution/embed_image/coronelli_globe_celeste.jpg> du **globe céleste** de Coronelli, issue de la même page Wikipedia mais téléversée sur le [CDN de Geotribu]

## Syntaxe générale

En `markdown`, intégrer une image se fait via la syntaxe suivante :

=== "Markdown"

    ```markdown
    ![Texte de remplacement au cas où l'image ne soit pas accessible](https://url_de_l_image.extension "Légende de l'image")

    <!-- avec notre image externe, ça donne donc -->
    ![Image de Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Coronelli_globe_terrestre.jpg/360px-Coronelli_globe_terrestre.jpg "Globe terrestre de Coronelli (Wikipedia")
    ```

=== "Rendu"

    ![Image de Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Coronelli_globe_terrestre.jpg/360px-Coronelli_globe_terrestre.jpg "Globe terrestre de Coronelli (Wikipedia")`

!!! tip

    On note que la légende est ajoutée en infobulle qui apparaît au survol prolongé de la souris sur l'image.

----

## Héberger une image sur le CDN de Geotribu

Traditionnellement, nous hébergeons les images sur notre propre serveur pour plusieurs raisons :

- ça évite de surcharger les serveurs des autres sites en pointant dessus
- ça évite les restrictions liées au "partage de ressources entre origines multiples", enfin le [CORS](https://fr.wikipedia.org/wiki/Cross-origin_resource_sharing) quoi
- ça permet de garantir de toujours disposer des images, même si elles n'existent plus à l'adresse originale (site supprimé, refonte du site, etc.)

!!! warning

    L'accès au CDN de Geotribu est réservé à l'équipe. Même si nous laissons les liens vers les images en public, merci de ne pas pointer dessus abusivement depuis d'autres sites.

### Bonnes pratiques

Sur le site historique de Geotribu, la difficile gestion des images a laissé en héritage chaotique : doublons en pagaille (jusqu'à 10 exemplaires dans certains cas...), noms d'images abscons rendant impossible la recherche, caractèrs spéciaux, dimensions démesurées (qui avait même provoqué un crash du serveur à l'époque :boom: !), etc.

Merci de suivre au mieux ces recommandations qui permettent de garantir une utilisation sereine des mêmes ressources par plusieurs personnes :pray: :

- chercher d'abord si l'image n'existe pas déjà (voir structure du CDN)
- redimensionner les images avant de les téléverser (= uploader) : 800px maximum en largeur ou en hauteur sont largement suffisants pour illustrer un article ou une news sur Geotribu.
- utiliser des formats avec de bons niveaux de compression :
    - JPEG ou mieux [JFIF](https://fr.wikipedia.org/wiki/JPEG_File_Interchange_Format), [PNG](https://fr.wikipedia.org/wiki/Portable_Network_Graphics), [WebP](https://fr.wikipedia.org/wiki/WebP).
    - à éviter Bitmap, Tiff, etc.
- nommer proprement les fichiers :
    - choisir un nom explicite qui permette la recherche par d'autres : `carte_densite_nyt.jpg` plutôt que `0f1f4706b8f1ea520747e3fd231a5bd0.jpg` (ce dernier exemple n'est pas une invention spontanée, il correspond réellement à une image stockée dans le CDN...)
    - pas de caractères spéciaux (espaces, accents, etc.)

Ce n'est évidemment pas exhaustif et il n'y a pas de brigade des images dans l'équipe, on s'en remet donc au bon sens de chacun/e :slightly_smiling_face:.

### Pas à pas

> Coming soon

<!-- Hyperlinks reference -->
[CDN de Geotribu]: https://cdn.geotribu.fr/images/
[markdown]: https://fr.wikipedia.org/wiki/Markdown
