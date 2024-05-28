---
title: OpenStreetMap dans le terminal, en braille et en ASCII
authors:
    - Jérémy Garniaux
categories:
    - article
comments: true
date: 2021-12-31
description: Présentation de MapSCII, une application Node.js permettant de naviguer dans un version ASCII d'OpenStreetMap depuis le terminal.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/mapscii/mapscii_0.png
license: default
robots: index, follow
tags:
    - mapscii
    - nodejs
    - terminal
    - OpenStreetMap
---

# OpenStreetMap dans le terminal, en braille et en ASCII

:calendar: Date de publication initiale : 31 décembre 2021

![logo OpenStreetMap](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/Openstreetmap.png "logo OpenStreetMap"){: .img-thumbnail-left }

[Publié sur Github](https://github.com/rastapasta/mapscii) en 2017 par le développeur allemand Michael Straßburger, MapSCII est une application Node.js qui propose de naviguer dans la carte mondiale d'OpenStreetMap... depuis un [terminal](https://fr.wikipedia.org/wiki/Terminal), avec un style cartographique détonnant construit en braille et en [ASCII](https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange) !  
Le projet, qui nous avait échappé jusqu'ici, dispose d'une démo rapidement consultable, mais peut aussi être téléchargé et personnalisé.

Petit tour d'horizon.

![MapSCII 1](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/mapscii/mapscii_1.png "MapSCII 1"){: .img-center loading=lazy }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Lancer la démo

### Linux et MacOS

MapSCII est accessible via le protocole [telnet](https://fr.wikipedia.org/wiki/Telnet). Si vous êtes sous Debian/Ubuntu, telnet devrait être installé par défaut. Sous MacOS, vous pouvez utiliser le gestionnaire de paquets [Homebrew](https://brew.sh/index_fr) pour installer telnet en rentrant la commande suivante dans une fenêtre de Terminal :

```bash
brew install telnet
```

Ensuite, la commande pour lancer MapSCII dans le terminal sous Linux ou MacOS est :

```bash
telnet mapscii.me
```

[![asciicast](https://asciinema.org/a/117813.svg)](https://asciinema.org/a/117813)

### Windows

Sous Windows, telnet est accessible avec le logiciel client [PuTTY](https://www.putty.org/). Au lancement de PuTTY, Il faut indiquer `mapscii.me` comme nom d'hôte, `telnet` comme type de connexion, avant d'ouvrir la connexion.

![MapSCII Putty](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/mapscii/mapscii_putty.png "MapSCII Putty Windows"){: .img-center loading=lazy }

----

## Installation locale

Il est possible d'installer MapSCII en local, via[Node.js](https://nodejs.org/fr/download/) :

```sh
npm install -g mapscii
```

Un snap dédié est aussi disponible sous Ubuntu : `sudo snap install mapscii`.

MapSCII se lance ensuite avec`mapscii`.

![MapSCII_screenshot_3](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/mapscii/mapscii_3.png "MapSCII 3"){: .img-center loading=lazy }

----

## Personnalisation

Vous pouvez également personnaliser différents aspects de MapSCII : changer le style (l'application est fournie avec deux styles Mapbox au choix, Bright ou Dark), ou bien explorer d'autres services d'autres lots de tuiles vecteurs, en local ou en se connectant à un service distant.
Ces éléments sont assez faciles à identifier dans le code source : par exemple, le fichier [`/src/config.js`](https://github.com/rastapasta/mapscii/blob/2315a3515c8870b8f88b1aa7978922fc7d426777/src/config.js#L10) permet d'indiquer, ligne 10, le fichier de style au format JSON à utiliser.

![MapSCII_screenshot_5](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/mapscii/mapscii_5.png "MapSCII 5"){: .img-center loading=lazy }

Ces aspects de personnalisation dépassent un peu, pour le moment, les compétences de l'auteur de ces lignes, qui fera de son mieux pour développer ce dernier point quand il aura percé les secrets des packages Node.js... N'hésitez pas à compléter cet article si vous le souhaitez, et bonne exploration de MapSCII en attendant !

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
