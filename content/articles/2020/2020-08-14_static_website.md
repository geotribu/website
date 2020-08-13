---
authors: "Julien Moura"
categories: ["tutoriel"]
date: 2020-08-14 11:11
description: "A l'instar de nombreux autres sites web, celui de Geotribu est un site statique. Mais c'est quoi exactement ?"
hero: "Publier facilement sur internet : l'ère des sites statiques."
tags: site web,geotribu,site statique,static website,mkdocs,hugo,markdown
title: "Publier un site web statique"
---

# Publier un site web : l'avènement des sites statiques

:calendar: Date de publication initiale : 14 août 2020

**Mots-clés :** web | astuces | Geotribu | contribution

## Intro

Avez-vous besoin d'un service d'authentification intégré (gestion des utilisateurs et des accès) ?
Avez-vous besoin d'une interface d'édition très complète ?

Exemples : documentations techniques, *landing pages*, événements (FOSS4G-FR), présentation de logiciel (GRASS)...

## C'est quoi un site statique

### Historique

rst -> markdown
sphinx

### Définition

Pas de base de données, pas de requêtes externes (même si...).
En gros : un dossier avec du html, du CSS et du JS. Le tout s'ouvre sur n'importe quel serveur web ou même un  navigateur.

la joie de la configuration

### la mode

<https://www.staticgen.com/>

<https://html5up.net/>

outillage : netlify, <https://staticman.net/>

----

## Le cas Geotribu

### Enjeu : la séparation des pouvoirs

> TO COMPLETE

### Toi aussi, déploie le site Geotribu chez toi

> TO COMPLETE

### Jouer avec les thèmes de MkDocs

Le contenu étant décorrelé du style  thème à appliquer, on peut alors

> TO COMPLETE

#### Read the Docs

Intégré par défaut dans MkDocs, on peut par exemple rendre le contenu dans le style du site Read The Docs qui est une plateforme d'hébergement de documentations techniques (QGIS, GDAL...), historiquement axé sur Sphinx (qu'il est d'ailleurs toujours possible d'utiliser)

```powershell
mkdocs serve -t readthedocs
```

![Geotribu - Read the Docs](https://cdn.geotribu.fr/img/tuto/static_web/static_theming_geotribu_rtd.png "Geotribu avec le thème Read the Docs")

#### Terminal

On peut aussi trouver des thèmes plus loufoques. Par exemple, si on souhaite s'adresser aux geeks nostalgiques, on optera pour le thème [bootstrap386](https://gitlab.com/lramage/mkdocs-bootstrap386) :

```powershell
pip install mkdocs-bootstrap386
mkdocs serve -t bootstrap386
```

![Geotribu - Vintage terminal](https://cdn.geotribu.fr/img/tuto/static_web/static_theming_geotribu_dos386.png "Geotribu avec le thème DOS i386")

Il y a même le curseur qui parcourt les lignes, donnant un petit côté Minitel !

### Jouer avec d'autres générateurs

#### Hugo

Parmi les générateurs de sites statiques les plus utilisés, Hugo est l'un des plus côtés récemment. Développé en Go, les performances

```powershell
hugo new site geotribu_hugo
cd geotribu_hugo
git init
git submodule add https://github.com/jpescador/hugo-future-imperfect.git themes/hugo-future-imperfect
```

![Geotribu - Hugo](https://cdn.geotribu.fr/img/tuto/static_web/static_theming_geotribu_hugo_future_imperfect.png "Geotribu avec le thème Future Imperfect du moteur Hugo")


----

## Déployer

## Localement

> TO COMPLETE

## Sur internet : mettre à profit les

> TO COMPLETE

----

## Auteur

--8<-- "content/team/jmou.md"

<!-- Hyperlinks reference -->
[Git]: https://git-scm.com/
[ISE]: https://docs.microsoft.com/fr-fr/powershell/scripting/windows-powershell/ise/introducing-the-windows-powershell-ise
[OSGeo4W]: https://trac.osgeo.org/osgeo4w/wiki/OSGeo4W_fr
