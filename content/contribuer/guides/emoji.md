---
title: Utiliser des emojis
authors:
    - Geotribu
categories:
    - article
    - contribution
    - tutoriel
date: 2020-07-20 10:20
description: "Guide de contribution à Geotribu : comment insérer des émojis dans un contenu en Markdown."
image: "https://blog.emojipedia.org/content/images/size/w2000/2020/02/Emojipedia-Header-Image-JoyPixels-5.5.jpg"
tags:
    - contribuer
    - media
    - emoji
    - emoticone
    - intégration
    - Markdown
    - tutoriel
# theme customizations
search:
  exclude: true
---

# Utiliser des émojis

Web 2020 oblige, il est possible d'insérer des [émojis](https://fr.wikipedia.org/wiki/%C3%89moji) directement dans le texte en Markdown.

On utilise [l'extension dédiée de PyMdown](https://facelessuser.github.io/pymdown-extensions/extensions/emoji/) et en particulier l'index `Twemoji` :

- consulter [les informations spécifiques sur cet index dans la doc de l'extension](https://facelessuser.github.io/pymdown-extensions/extensions/emoji/#default-emoji-indexes)
- consulter les codes des émojis depuis la [table de correspondance unicode <--> emojis](https://github.com/joypixels/emoji-toolkit/blob/master/lib/joypixels-awesome/_joypixels-awesome.map.scss)

## Syntaxe

Elle est semblable à la plupart des outils de discussion : `:emoji_code:`.

<!-- markdownlint-disable MD046 -->
=== "Markdown"

    ```markdown
    Voici quelques exemples d'émojis : :beginner: :birthday: :boom: :candle: :earth_americas: :earth_africa: :earth_asia: :eyeglasses: :globe_with_meridians: :heart: :heart_eyes: :parachute: :pirate_flag: :pray: :smile: :smiley: :sweat_smile: :slight_smile: :unicorn: :woman_levitate:
    ```

=== "Rendu"

    Voici quelques exemples d'émojis : :beginner: :birthday: :boom: :candle: :earth_americas: :earth_africa: :earth_asia: :eyeglasses: :globe_with_meridians: :heart: :heart_eyes: :parachute: :pirate_flag: :pray: :smile: :smiley: :sweat_smile: :slight_smile: :unicorn: :woman_levitate:
<!-- markdownlint-enable MD046 -->

----

## Table de correspondance

:warning: La liste étant très grande, cela peut-être très long à afficher :warning:

[Tableau des codes de chaque emoji et leur aperçu :fontawesome-regular-eye:](/toc_nav_ignored/emojis_joypixels_preview/){: .md-button }
[Rechercher dans toutes les icônes (émojis inclus) :fontawesome-solid-magnifying-glass-location:](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/#search){: .md-button }
{: align=middle }
