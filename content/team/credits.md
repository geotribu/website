---
title: Crédits et remerciements
authors:
    - Geotribu
categories:
    - Geotribu
comments: true
date: 2020-04-10
description: L'aventure de Geotribu est rendue possible par le travail et le soutien de personnes et aussi d'outils et ressources libres. Crédits et remerciements.
image: https://cdn.geotribu.fr/img/internal/charte/geotribu_banner_600x300.png
tags:
    - Geotribu
    - crédits
    - remerciement
    - soutien
search:
    exclude: true
---

# Remerciements

L'aventure de Geotribu est rendue possible par l'existence de ressources et d'outils libres, pour la plupart gratuits, derrière lesquels il y a ~~beaucoup~~ une poignée d'humains qu'il nous faut remercier ici.

## Hébergement et domaine

- Code source : [Github](https://github.com/geotribu)
- Site web : [Github Pages](https://pages.github.com/)
- Contenus statiques (images, etc.) : [GeoRezo](https://georezo.net/) nous prête gracieusement un serveur depuis 2016 (utilisé jusqu'en 2020 principalement pour [El Géo Paso](https://elgeopaso.georezo.net/)). Mention spéciale à **Yves**, couteau-suisse technique de l'association, disponible autant que faire se peut.
- Noms de domaine : [Gandi](https://www.gandi.net/fr). Mention spéciale à **Fabien G.** qui a toujours soigneusement conservé (et payé) les noms de domaine.

## Outils libres

![icône open source](https://cdn.geotribu.fr/img/logos-icones/opensource.png "icône open source"){: .img-thumbnail-left }

Le site repose énormément sur des solutions libres et nous tenons à remercier les personnes mettant ainsi leur travail à la disposition de tout le monde :

- [Mkdocs](https://www.mkdocs.org/) : générateur de site web statique à partir de contenus rédigés en [markdown]. Simple et extensible, c'est un outil puissant. Le fait qu'il soit en [Python](https://www.python.org/) le rend compatible avec notre socle technique interne.
- [Material for Mkdocs] : thème pour Mkdocs qui utilise le framework graphique [Material](https://material.io/) conçu et utilisé par Google. C'est propre, moderne (du bon JS webpacké), orienté performances et facilement personnalisable. Mention spéciale à **Martin Donath**, qui maintient presque seul ce projet.
- [Tiny File Manager](https://tinyfilemanager.github.io/) : le gestionnaire de fichiers
petit (1 seul fichier PHP !) mais costaud que nous utilisons pour gérer nos contenus statiques.
- [Isso](https://posativ.org/isso/) système de commentaires minimaliste et open source

A noter qu'en dépit du fait que GitHub ne soit pas open source, nous tirons énormément parti de la plateforme et en particulier :

- [Github Actions](https://help.github.com/actions) : permet l'automatisation du _workflow_ de publication, réduisant énormément le travail technique à produire.
- [Github Release](https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github) et [GitHub CLI](https://cli.github.com/) : permet l'automatisation de la sauvegarde du site. Voir [la page sur la sauvegarde]({{ config.extra.url_contribuer }}internal/backup/).

### Nos contributions

Afin de couvrir nos besoins, nous sommes parfois amenés à contribuer aux outils cités plus haut :

- Isso : ajout des notifications via web hooks. [Voir l'article sur le sujet](../articles/2021/2021-05-14_commentaires_migration_disqus_isso.md).
- plugin RSS pour MkDocs : génère des flux RSS à partir de l'historique Git et/ou des en-têtes des contenus. [Voir le dépôt du projet](https://github.com/Guts/mkdocs-rss-plugin/).
- Tiny File Manager : complétion et amélioration de la traduction française ([voir la Pull Request](https://github.com/prasathmani/tinyfilemanager/pull/497)).

### Sponsoring

Afin de soutenir les projets open source sur lequel repose le site et le workflow de contribution, nous finançons certains d'entre eux via [GitHub](https://github.com/orgs/geotribu/sponsoring).

Pour supporter notre travail, vous pouvez donner, ponctuellement ou de manière récurrente, via Liberapy ou Tipee :

[Liberapay :fontawesome-solid-gift:](https://liberapay.com/Geotribu/){: .md-button }
[Tipee :fontawesome-solid-piggy-bank:](https://fr.tipeee.com/geotribu/){: .md-button }
{: align=middle }

----

## Autres

Merci aux différentes personnes/organismes qui nous motivent et nous aident. Tout d'abord, d'une manière générale, la communauté Open Source qui met à disposition les formidables applications que nous vous présentons. Mais aussi, les associations qui visent à la promotion du logiciel libre comme l'[OSGEO Fr](https://osgeo.asso.fr/) ainsi que celles comme [OSM-Fr](https://www.openstreetmap.fr/) œuvrant pour l'ouverture des données.

Enfin, cette aventure n'aurait jamais été possible sans le soutien de [Laurent Jégou](https://fr.linkedin.com/in/laurentjegou) qui pendant longtemps nous a offert l'infrastructure informatique nécessaire au fonctionnement de GéoTribu. Merci Laurent !
