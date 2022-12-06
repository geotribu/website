---
title: "Intégrer une image"
subtitle: "Gérer l'alignement, le chargement, etc."
authors:
    - Julien Moura
categories:
    - article
    - contribution
    - tutoriel
date: 2020-04-20 10:20
description: "Guide de contribution à Geotribu : comment intégrer une image dans un article ou une revue de presse et gérer le stockage commun."
icon: material/image-frame
tags:
    - contribuer
    - media
    - image
    - intégration
    - tutoriel
    - Markdown
    - cdn
# theme customizations
search:
  exclude: true
---
<!-- markdownlint-disable MD046 -->

# Intégrer une image

Prenons deux exemples :

- une image _externe_, c'est-à-dire hébergée ailleurs que sur le [CDN de Geotribu] : <https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Coronelli_globe_terrestre.jpg/360px-Coronelli_globe_terrestre.jpg> du **globe terrestre** de Coronelli, issue de cette page Wikipedia <https://fr.wikipedia.org/wiki/Globes_de_Coronelli>
- une image _interne_, hébergée sur le [CDN de Geotribu] : <https://cdn.geotribu.fr/img/internal/contribution/embed_image/coronelli_globe_celeste.jpg> du **globe céleste** de Coronelli, issue de la même page Wikipedia mais téléversée sur le [CDN de Geotribu]

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

!!! tip "Infobulle"
    On note que la légende est ajoutée en infobulle qui apparaît au survol prolongé de la souris sur l'image.

## Style, position et dimension

Par défaut, les images sont détourées d'une fine bordure gris foncé mais il est possible d'ajuster ce comportement :

- soit en utilisant les balises pré-configurées
- soit de personnaliser les attributs et classes CSS individuellement pour chaque image

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

### Centrer

C'est le style le plus appliqué pour les images d'illustration des contenus : `{: .img-center }`.

=== "Markdown"

    ```markdown
    ![Image de Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Coronelli_globe_terrestre.jpg/360px-Coronelli_globe_terrestre.jpg){: .img-center }

    La balise `{: .img-center }` centre l'image par rapport au contenu.
    ```

=== "Rendu"

    ![Image de Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ab/Coronelli_globe_terrestre.jpg/360px-Coronelli_globe_terrestre.jpg){: .img-center }

    La balise `{: .img-center }` centre l'image par rapport au contenu.

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

### Lightbox (mode galerie)

Grâce au plugin [Mkdocs GLightbox](https://blueswen.github.io/mkdocs-glightbox/), les images sont automatiquement visibles dans un mode galerie (communément appelé _[lightbox]_) sans syntaxe additionnelle (depuis cette [_Pull Request_ d'octobre 2022](https://github.com/geotribu/website/pull/720)).

Par défaut, toutes les images sont concernées sauf :

- les vignettes, donc les images avec la balise `{: .img-rdp-news-thumb }`
- les emojis

Il est possible de désactiver le mode galerie sur une image en particulier en lui attribuant la balise `{: .off-glb }`.  
Il est possible de désactiver le mode galerie sur tout une page en ajoutant `glightbox: false` à [l'en-tête du fichier](/contribuer/guides/metadata_yaml_frontmatter/)

=== "Markdown"

    Par exemple, dans l'exemple suivant, la première image aura le mode galerie mais pas la seconde :

    ```markdown
    ![Texte de remplacement](https://cdn.geotribu.fr/img/internal/charte/geotribu_banner.jpg){: loading=lazy width=200px }

    ![FOSS4G-FR 2016](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/foss4g-geotribu.JPG "Une partie de l'équipe Geotribu au FOSS4G-FR 2016"){ loading=lazy width="200" .off-glb }
    ```

=== "Rendu"

    Par exemple, dans l'exemple suivant, la première image aura le mode galerie mais pas la seconde :

    ![Texte de remplacement](https://cdn.geotribu.fr/img/internal/charte/geotribu_banner.jpg){: loading=lazy width=200px }

    ![FOSS4G-FR 2016](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/foss4g-geotribu.JPG "Une partie de l'équipe Geotribu au FOSS4G-FR 2016"){ loading=lazy width="200" .off-glb }

### Style personnalisé

Au-delà des styles prédéfinis, il est évidemment possible de personnaliser à la volée :

=== "Markdown"

    ```markdown
    ![Bannière Geotribu](https://cdn.geotribu.fr/img/internal/charte/geotribu_banner.jpg "Bannière de Geotribu"){: width=100px loading=lazy align=middle }.
    Par exemple, appliquer une largeur maximum, appliquer un centrage du texte et activer le chargement asynchrone sur une image. Ou centrer tout un paragraphe.
    {: text-align="center" }
    ```

=== "Rendu"

    ![Bannière Geotribu](https://cdn.geotribu.fr/img/internal/charte/geotribu_banner.jpg "Bannière de Geotribu"){: width=100px loading=lazy align=middle }.
    Par exemple, appliquer une largeur maximum, appliquer un centrage du texte et activer le chargement asynchrone sur une image. Ou centrer tout un paragraphe.
    {: text-align="center" }

----

<!-- Hyperlinks reference -->
[lightbox]: https://en.wikipedia.org/wiki/Lightbox_(JavaScript)
