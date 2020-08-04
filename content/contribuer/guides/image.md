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
    ![Image de Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Coronelli_globe_terrestre.jpg/360px-Coronelli_globe_terrestre.jpg "Globe terrestre de Coronelli (Wikipedia)")
    ```

=== "Rendu"

    ![Image de Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Coronelli_globe_terrestre.jpg/360px-Coronelli_globe_terrestre.jpg "Globe terrestre de Coronelli (Wikipedia)")

!!! tip

    On note que la légende est ajoutée en infobulle qui apparaît au survol prolongé de la souris sur l'image.

## Style, position et dimension

Par défaut, les images sont :

- centrées
- détourées d'une fine bordure gris foncé

Le site utilise l'extension [`Attribute Lists`](https://python-markdown.github.io/extensions/attr_list/) permettant d'affecter dynamiquement des attributs HTML en utilisant la syntaxe Markdown.

L'idée étant que l'attribut corresponde à un style CSS défini dans le fichier [extra.css](https://github.com/geotribu/website/blob/master/content/theme/assets/stylesheets/extra.css).

### Vignette

C'est le style appliqué pour les icônes des news des revues de presse : `{: .img-rdp-news-thumb }`.

=== "Markdown"

    ```markdown
    ![Geotribu logo](https://cdn.geotribu.fr/img/internal/charte/geotribu_logo_254x254.png "Logo de Geotribu"){: .img-rdp-news-thumb }

    La balise `{: .img-rdp-news-thumb }` permet d'appliquer automatiquement le style vignette à l'image : pas de bordure, taille limitée à 75px, alignement à gauche et texte autour.
    ```

=== "Rendu"

    ![Geotribu logo](https://cdn.geotribu.fr/img/internal/charte/geotribu_logo_254x254.png "Logo de Geotribu"){: .img-rdp-news-thumb }

    La balise `{: .img-rdp-news-thumb }` permet d'appliquer automatiquement le style vignette à l'image : pas de bordure, taille limitée à 75px, alignement à gauche et texte autour.

### Aligner à droite

Pour aligner une image à droite, utiliser : `{: .img-right }`.

=== "Markdown"

    ```markdown
    ![Geotribu old logo](https://cdn.geotribu.fr/img/internal/charte/old_geotribu_logo.png "Ancien logo de Geotribu"){: .img-right }

    La balise `{: .img-right }` permet d'aligner l'image à droite en laissant le texte autour, sans changer les dimensions.
    ```

=== "Rendu"

    ![Geotribu old logo](https://cdn.geotribu.fr/img/internal/charte/old_geotribu_logo.png "Ancien logo de Geotribu"){: .img-right }

    La balise `{: .img-right }` permet d'aligner l'image à droite en laissant le texte autour, sans changer les dimensions.

----

## Héberger une image sur le CDN de Geotribu

Traditionnellement, nous hébergeons les images sur notre propre serveur pour plusieurs raisons :

- ça évite de surcharger les serveurs des autres sites en pointant dessus
- ça évite les restrictions liées au "partage de ressources entre origines multiples", enfin le [CORS](https://fr.wikipedia.org/wiki/Cross-origin_resource_sharing) quoi
- ça permet de garantir de toujours disposer des images, même si elles n'existent plus à l'adresse originale (site supprimé, refonte du site, etc.)

!!! warning

    L'accès au CDN de Geotribu est réservé à l'équipe. Même si nous laissons les liens vers les images en public, merci de ne pas pointer dessus abusivement depuis d'autres sites.

### Bonnes pratiques

Sur le site historique de Geotribu, la difficile gestion des images a laissé un héritage chaotique : doublons en pagaille (jusqu'à 10 exemplaires dans certains cas...), noms d'images abscons rendant impossible la recherche, caractères spéciaux, dimensions démesurées (qui avait même provoqué un crash du serveur à l'époque :boom: !), etc.

Merci de suivre au mieux ces recommandations qui permettent de garantir une utilisation sereine des mêmes ressources par plusieurs personnes :pray: :

- chercher d'abord si l'image n'existe pas déjà (voir structure du CDN)
- redimensionner les images avant de les téléverser (= _uploader_) : 800px maximum en largeur ou en hauteur sont largement suffisants pour illustrer un article ou une news sur Geotribu.
- utiliser des formats avec de bons niveaux de compression :
    - JPEG ou mieux [JFIF](https://fr.wikipedia.org/wiki/JPEG_File_Interchange_Format), [PNG](https://fr.wikipedia.org/wiki/Portable_Network_Graphics), [WebP](https://fr.wikipedia.org/wiki/WebP).
    - à éviter Bitmap, Tiff, etc.
- nommer proprement les fichiers :
    - choisir un nom explicite qui permette la recherche par d'autres : `carte_densite_nyt.jpg` plutôt que `0f1f4706b8f1ea520747e3fd231a5bd0.jpg` (ce dernier exemple n'est pas une invention spontanée, il correspond réellement à une image stockée dans le CDN...)
    - pas de caractères spéciaux (espaces, accents, etc.)

Ce n'est évidemment pas exhaustif et il n'y a pas de brigade des images dans l'équipe, on s'en remet donc au bon sens de chacun/e :slightly_smiling_face:.

### Structure

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

### Pas à pas

1. Se connecter au gestionnaire de fichiers en ligne : <https://cdn.geotribu.fr/>

    ![Tiny File Manager - Formulaire d'authentification](https://cdn.geotribu.fr/img/internal/contribution/embed_image/cdn_filemanager_authform.png "Tiny File Manager - Formulaire d'authentification")

    > l'identifiant et mot de passe sont transmis sur demande sur le [Slack de l'équipe](https://geotribu.slack.com)

2. Utiliser la recherche pour savoir si jamais une image correspond au besoin
3. Se positionner dans le dossier souhaité
4. Cliquer sur :cloud: `Envoyer`
5. Glisser/déposer ou sélectionner l'image

    ![Téléverser une image](https://cdn.geotribu.fr/img/internal/contribution/embed_image/cdn_filemanager_upload.png)

6. Cliquer `Retour` et récupérer l'URL de l'image. Par exemple, avec un clic droit sur l'icône de lien ou en cliquant sur l'imahge puis sur `Ouvrir``

    ![Clic doit copier l'adresse du lien](https://cdn.geotribu.fr/img/internal/contribution/embed_image/cdn_filemanager_get_image_url.png "Clic doit copier l'adresse du lien")

<!-- Hyperlinks reference -->
[CDN de Geotribu]: https://cdn.geotribu.fr/images/
[markdown]: https://fr.wikipedia.org/wiki/Markdown
