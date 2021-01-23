---
title: Utiliser des emojis
category: contribution
date: 2020-07-20 10:20
description: "Guide de contribution à Geotribu : comment insérer des émojis dans un contenu en Markdown."
tags: geotribu,contribuer,media,emoji,emoticone,intégration,tutoriel
---

# Utiliser des émojis

Web 2020 oblige, il est possible d'insérer des [émojis](https://fr.wikipedia.org/wiki/%C3%89moji) directement dans le texte en Markdown.

On utilise [l'extension dédiée de PyMdown](https://facelessuser.github.io/pymdown-extensions/extensions/emoji/) et en particulier l'index `Twemoji` :

- consulter [les informations spécifiques sur cet index dans la doc de l'extension](https://facelessuser.github.io/pymdown-extensions/extensions/emoji/#default-emoji-indexes)
- consulter les codes des émojis depuis la [table de correspondance unicode <--> emojis](https://github.com/joypixels/emoji-toolkit/blob/master/lib/joypixels-awesome/_joypixels-awesome.map.scss)

## Syntaxe

Elle est semblable à la plupart des outils de discussion : `:emoji_code:`.

=== "Markdown"

    ```markdown
    Voici quelques exemples d'émojis : :beginner: :birthday: :boom: :candle: :earth_americas: :earth_africa: :earth_asia: :eyeglasses: :globe_with_meridians: :heart: :heart_eyes: :parachute: :pirate_flag: :pray: :smile: :smiley: :sweat_smile: :slight_smile: :unicorn: :woman_levitate:
    ```

=== "Rendu"

    Voici quelques exemples d'émojis : :beginner: :birthday: :boom: :candle: :earth_americas: :earth_africa: :earth_asia: :eyeglasses: :globe_with_meridians: :heart: :heart_eyes: :parachute: :pirate_flag: :pray: :smile: :smiley: :sweat_smile: :slight_smile: :unicorn: :woman_levitate:
