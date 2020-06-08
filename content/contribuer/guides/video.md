---
title: Intégrer une vidéo
category: contribution
date: 2020-04-27 10:20
tags: contribuer,vidéo,youtube,vimeo,embed,intégration,tutoriel
---

# Intégrer une vidéo

## Vidéo hébergée hors plateforme

Pour les vidéos qui ne sont pas hébergées sur une plateforme en particulier, il est toujours possible de les intégrer en utilisant [la balise dédiée de HTML 5](https://www.w3schools.com/tags/tag_video.asp).

Prenons cette vidéo pour exemple : <https://file-examples.com/wp-content/uploads/2017/04/file_example_MP4_1280_10MG.mp4>

=== "Markdown"

    ```html
    Une **vidéo** d'illustration de cette _webmap_ :

    <video width="700" controls>
  		<source src="https://file-examples.com/wp-content/uploads/2017/04/file_example_MP4_1280_10MG.mp4" type="video/mp4">
  		Votre navigateur ne supporte pas la balise video HTML 5.
	</video>
    ```

=== "Rendu"

    Une **vidéo** d'illustration de cette _webmap_ :

    <video width="700" controls>
  		<source src="https://file-examples.com/wp-content/uploads/2017/04/file_example_MP4_1280_10MG.mp4" type="video/mp4">
  		Votre navigateur ne supporte pas la balise video HTML 5.
	</video>

:bellhop_bell: Voilà, c'est prêt ! :tada:

----

## Youtube

Prenons cette vidéo pour exemple : <https://www.youtube.com/watch?v=St8ArwOa3yA>

1. Cliquer sur le `Partager` en bas de la vidéo puis sur `Intégrer` :

    ![Menu partage d'une vidéo de Youtube](https://cdn.geotribu.fr/images/internal/contribution/videos/embed_youtube_share_annotated.png)

2. Cocher `Activer le mode de confidentialité avancé` de façon à être _RGPD friendly_ autant que faire se peut :

    ![Copier le code d'intégration de la vidéo Youtube](https://cdn.geotribu.fr/images/internal/contribution/videos/embed_youtube_copy_annotated.png)

3. Cliquer sur `Copier`et coller le code d'intégration dans le markdown. Attention, les iframes ne doivent jamais être en retrait (tabulation, espace, etc.) pour ne pas être considérés comme du code :

=== "Markdown"

    ```html
    Une **vidéo** d'illustration de cette _webmap_ :

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/St8ArwOa3yA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    ```

=== "Rendu"

    Une **vidéo** d'illustration de cette _webmap_ :

    <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/St8ArwOa3yA" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

:bellhop_bell: Voilà, c'est prêt ! :tada:
