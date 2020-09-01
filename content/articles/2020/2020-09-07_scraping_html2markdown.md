---
title: "Web-scraping avec Scrapy"
authors: "Julien Moura"
categories: ["article", "tutoriel"]
date: "2020-09-07 10:20"
description: "Comment le web-scraping (Scrapy) a permis de récupérer les anciens contenus de Geotribu et de les convertir en Markdown."
hero: "Le web-scraping à la rescousse des anciens contenus."
tags: "Scrapy,Python,BeautifulSoup,geotribu,histoire"
---

# Récupérer les anciens contenus : le web-scraping à la rescousse

:calendar: Date de publication initiale : 7 septembre 2020

**Mots-clés :** Geotribu | histoire | Scrapy | Python | web-scraping

## Introduction

Après avoir disserté sur [la petite histoire de Geotribu](../2020-08-31_geotribu_histoire/), voici veni

## Le web-scraping, c'est quoi


### Scrapy

```bash
python -m pip install scrapy==2.3.*
```

```python
scrapy shell "http://localhost/geotribu_reborn/revues-de-presse"

# titre de la page
response.css('title::text').getall()[0]

# première rdp de la liste
t = response.css('div.title-and-meta')[0]
t = response.css('article')[0]

# date
rdp_date = t.css("div.date")
rdp_date_day = rdp_date.css("span.day::text").get()
rdp_date_month = rdp_date.css("span.month::text").get()
rdp_date_year = rdp_date.css("span.year::text").get()

# title
rdp_title_section = t.css("div.title-and-meta")
rdp_title = rdp_title_section.css("h2.node__title a::text").get()

# url
rdp_url_rel = rdp_title_section.css("h2.node__title a::attr(href)").get()

# -- Parcourir la revue de presse

fetch("http://localhost" + rdp_url_rel)

# contenu de la rdp
rdp = response.css('article')[0]

# title
rdp_title_section = t.css("div.title-and-meta")
rdp_title = rdp_title_section.css("h2.node__title a::text").get()

# sections
rdp_sections = rdp.css("p.typeNews::text").getall()
```

----

## Du HTML au Markdown

Avec tout cela, on a donc un beau cocktail *Web on The Beach* (HTML + CSS + JavaScript) :cocktail:. C'est bien mais ce qui nous intéresse c'est le contenu et la structure, les scripts et le rendu sont encore trop intimement liés.

Une fois le HTML et les ressources liées (images...) récupérés, j'ai opté pour un stockage sous forme de Markdown. Pour cela, j'ai utilisé le package [markdowinify](https://github.com/matthewwithanm/python-markdownify) qui permet de transformer du HTML en Markdown.

## La conversion par l'exemple : rendre lisible un article du CNIG

L'usage de _markdownify_ est simple. Pour s'en rendre compte, testons cela rapidement avec un petit objectif pour l'occasion : transformer en markdown [le dernier article du site du CNIG](http://cnig.gouv.fr/?p=23807) pour le lire sans saigner des yeux.

Au passage, on en profite pour essayer deux autres bibliothèques pour ce genre de cas de figure :

- [Beautifulsoup](https://www.crummy.com/software/BeautifulSoup/) : pour le parsing du HTML
- [urllib3](https://urllib3.readthedocs.io/) : pour facilement faire des requêtes HTTP ; _requests_ ou _httpx_ étant surdimensionnés pour notre besoin, mais avec la flemme de gérer les détails (décodage, etc.)

### Structure

En regardant [les sources de l'article](view-source:http://cnig.gouv.fr/?p=23807), on sait que le contenu intéressant est dans la div de class `post-content` :

[![Source HTML CNIG](https://cdn.geotribu.fr/img/articles-blog-rdp/scraping_cnig_art_source.png "Les sources de l'article du CNIG "){: loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/scraping_cnig_art_source.png){: data-mediabox="scraping" data-title="Sources d'un article du site du CNIG."}

### Prérequis

Avant de commencer, on installe ce qu'il nous manque :

```bash
python -m pip install beautifulsoup4==4.9.* markdownify==0.5.* urllib3==1.25.*
```

### Scraping et conversion à la volée

Puis cela tient en quelques lignes dûment commentées :

```python
#! python3

# -- Imports

# Bibliothèque standard
from pathlib import Path

# Packages tiers
import urllib3
from bs4 import BeautifulSoup
from markdownify import markdownify

# -- Variables

in_url = "http://cnig.gouv.fr/?p=23807"
out_filepath = Path("./cnig_23807.md")

# -- Programme principal

# d'abord on télécharge la page
http = urllib3.PoolManager()
page = http.request('GET', in_url)

# on parse le html
soup = BeautifulSoup(page.data, "html.parser")

# on extrait ce qu'il y a dans la classe post-content
post_content = soup.find("div", {"class": "post-content"})

# on transforme en markdown en spécifiant le style de titre avec des '#'
out_md = markdownify(post_content, heading_style="ATX", autolinks=False)

# on écrit notre fichier
with out_filepath.open("w", encoding="UTF8") as fifi:
    fifi.write(out_md)
```

Le résultat, ainsi que le code, sont disponibles dans [ce gist](https://gist.github.com/Guts/a77e9e378b7157f568077ab47937a9d9).

----

## Conclusion

Evidemment, le résultat est loin d'être parfait et cela demande quelques ajustements et améliorations : déterminer le nom du fichier selon le titre de la page, nettoyer les espacements avant les paragraphes, etc. D'ailleurs, ce nettoyage manuel est toujours en cours pour une partie des contenus de Geotribu.

Cela démontre bien à la fois la faisabilité et les limitations du traitement automatisé, qu'on peut résumer ainsi :

```mermaid
graph TD;
  A[Site archivé]-->B[Scraping];
  B-->C[HTML];
  B-->D[Images];
  C-->E[Markdown];
  D-->F[CDN];
```

[A suivre (14 septembre) : les sites statiques :fontawesome-solid-step-forward:](#){: .md-button }
{: align=middle }

----

## Auteur

--8<--
content/team/jmou.md
--8<--

<!-- Hyperlinks reference -->
[Scrapy]: https://scrapy.org/
[internet Archive]: https://archive.org
