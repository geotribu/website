---
title: "Titre principal"
subtitle: un sous-titre subtil
authors:
    - Prénom NOM
categories:
    - article
comments: true
date: 2021-08-09
description: "Description de 160 caractères maximum qui résume l'article qui est présente dans le flux RSS, la newsletter, les moteurs de recherche, en page d'accueil... "
icon: "icone à choisir parmi celles disponibles dans le thème : https://squidfunk.github.io/mkdocs-material/reference/#setting-the-page-icon. Cliquer sur le + pour dérouler un mini moteur de recherche"
image: "Image d'illustration de l'article qui sert ensuite dans la mise en avant : réseaux sociaux, flux RSS... 400x800 en PNG"
license: default
robots: index, follow
tags:
    - tag 1
    - tag 2
    - ...
---

# Titre principal

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

Texte.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Titre 2

Texte.

### Titre 3

Texte.

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
