---
title: Intégrer un contenu audio
categories:
    - article
    - contribution
    - tutoriel
date: 2021-08-03 10:20
description: "Guide de contribution à Geotribu : comment intégrer un fichier audio (podcast, etc.) dans un contenu en Markdown."
image: "https://cdn.geotribu.fr/img/internal/contribution/audio/html_audio_tag.png"
license: default
tags:
    - contribuer
    - audio
    - musique
    - podcast
    - son
    - markdown
    - intégration
    - tutoriel
# theme customizations
search:
  exclude: true
---

# Intégrer un contenu audio (podcast, etc.)

## Fichier audio hébergé hors plateforme

Pour les fichiers de son qui ne sont pas hébergés sur une plateforme en particulier, il est toujours possible de les intégrer en utilisant [la balise dédiée de HTML 5](https://www.w3schools.com/html/html5_audio.asp).

Pour exemple, prenons ce son : <https://www.w3schools.com/html/horse.mp3>

<!-- markdownlint-disable MD046 -->
=== "Markdown"

    ```html
    Un hénissement de cheval issu du site W3Schools :

    <!-- markdownlint-disable MD033 -->
    <audio preload="metadata" width="100%" controls>
        <source src="https://www.w3schools.com/html/horse.mp3" type="audio/mpeg">
        Votre navigateur ne supporte pas la balise audio HTML 5.
    </audio>
    <!-- markdownlint-enable MD033 -->
    ```

=== "Rendu"

    Un hénissement de cheval issu du site W3Schools :

    <audio preload="metadata" width="100%" controls>
        <source src="https://www.w3schools.com/html/horse.mp3" type="audio/mpeg">
        Votre navigateur ne supporte pas la balise audio HTML 5.
    </audio>

:bellhop_bell: Voilà, c'est prêt ! :tada:

### Exemples déjà publiés

Voici quelques exemples de syntaxe markdown qui ont été publiés sur Geotribu :

- [intégration du podcast de l'April au format ogg](https://github.com/geotribu/website/blob/master/content/rdp/2021/rdp_2021-03-26.md?plain=1#L172-L181)

----

## Emissions Radio France

Il arrive que l'intégration des podcasts de Radio France pose un problème de rendu, lié à une mauvaise interprétation du mode mobile. Il faut donc forcer les dimensions pour faire apparaître le widget de lecture.

Par exemple, pour [l'épisode de cette émission](https://www.franceinter.fr/emissions/l-ete-comme-jamais/l-ete-comme-jamais-du-jeudi-29-juillet-2021), le code de partage donné par le site est :

```html
<iframe
    src="https://www.franceinter.fr/embed/player/aod/20d6704d-a414-44e8-a442-e5a354179ab1"
    width="100%"
    height="100%"
    layout="responsive"
    frameborder="0"
    scrolling="no"
    >
</iframe>
```

Il faut alors modifier les attributs `height` et `width` pour que le widget de lecture apparaisse correctement :

<!-- markdownlint-disable MD046 -->
=== "Markdown"

    ```html hl_lines="5 6"
    Un podcast sympa de France Inter :

    <iframe
        src="https://www.franceinter.fr/embed/player/aod/20d6704d-a414-44e8-a442-e5a354179ab1"
        height="375"
        width="350"
        layout="responsive"
        frameborder="0"
        scrolling="no"
        >
    </iframe>
    ```

=== "Rendu"

    Un podcast sympa de France Inter :

    <iframe
        src="https://www.franceinter.fr/embed/player/aod/20d6704d-a414-44e8-a442-e5a354179ab1"
        height="375"
        width="350"
        layout="responsive"
        frameborder="0"
        scrolling="no"
        >
    </iframe>

:bellhop_bell: Voilà, c'est prêt ! :tada:
