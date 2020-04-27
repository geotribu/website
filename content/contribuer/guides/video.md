---
title: Intégrer une vidéo
category: contribution
date: 2020-04-27 10:20
tags: contribuer,vidéo,youtube,vimeo,embed,intégration,tutoriel
---

# Intégrer une vidéo

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
