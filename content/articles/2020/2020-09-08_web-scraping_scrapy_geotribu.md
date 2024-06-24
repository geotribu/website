---
title: Le web-scraping avec Scrapy
authors:
    - Julien MOURA
categories:
    - article
    - tutoriel
comments: true
date: 2020-09-08
description: Utiliser le web-scraping (Scrapy) pour récupérer les anciens contenus de Geotribu depuis l'Internet Archive.
image: https://cdn.geotribu.fr/img/tuto/webscraping/web_scraping.png
tags:
    - Geotribu
    - Histoire
    - Python
    - Scrapy
---

# Récupérer les anciens contenus : le web-scraping à la rescousse

:calendar: Date de publication initiale : 7 septembre 2020

## Introduction

Après avoir disserté sur [la petite histoire de Geotribu](2020-08-31_geotribu_histoire.md), il est désormais temps de se pencher sur la méthode retenue pour récupérer les anciens contenus.

Pendant un temps, on a eu l'espoir de remonter le site depuis une ancienne sauvegarde, quitte à faire le deuil des contenus les plus récents. Techniquement faisable, l'idée de repartir sur un Drupal vieillot et difficile à maintenir n'a pas séduit grand monde.

Lorsque que le moment est venu, j'ai donc opté pour le web-scraping. L'occasion ici de partager mon expérience, comme d'habitude.

## Le web-scraping, c'est quoi

C'est une technique visant à aspirer le contenu d'un site web pour le stocker dans un format pivot en vue d'une réutilisation, prévue ou non par l'éditeur initial. Pour plus de détails, [la page Wikipédia sera certainement plus complète](https://fr.wikipedia.org/wiki/Web_scraping).

Si le nom ne vous dit rien, c'est pourtant une technique qui est largement utilisée de façon sous-jacente à de nombreux services : référencement automatisé des sites par les moteurs de recherche, tests automatisés d'applications webs (_headless_), comparateurs de prix, agrégateurs de contenus (actualités par exemple) etc.

Le fonctionnement global est schématisé de la façon suivante :

![web scraping schéma](https://cdn.geotribu.fr/img/tuto/webscraping/web_scraping.png "Le web-scraping schématisé. Crédits : Web Harvy"){: .img-center loading=lazy }

----

## Aspirons l'ancien Geotribu

:cup_with_straw: Si on en croit cette simplification, on a donc besoin de 3 ingrédients :

- un site web qui tourne
- un logiciel (ou un service) de web-scraping
- un/des formats de destination

### Le site : local et Internet Archive

Pour ce premier point, je suis d'abord parti de la dernière sauvegarde dont disposait Fabien mais qui datait. Après quelques batailles homme-machine, je gagnai la guerre et déployai l'ancien Geotribu en local. Pour l'anecdote, travaillant alors sur Windows, j'ai même eu le toupet de faire tourner le site sur [WAMP](https://fr.wikipedia.org/wiki/WampServer) !

Pour les contenus les plus récents, je me suis tourné vers l'[Internet Archive] sur les conseils de [Vincent Picavet](https://www.linkedin.com/in/vincentpicavet/) (merci à lui !), d'où j'ai tiré les captures d'écran du précédent article.

Le projet permet bien un accès via des [APIs REST](https://archive.org/services/docs/api/) et ne se prête pas trop au web-scraping intensif pour qui souhaite respecter le [_fair-use_](https://fr.wikipedia.org/wiki/Fair_use), mais cela aurait demandé de faire du développement spécifique et _one-shot_ qui plus est.

L'une des difficultés étant que l'archivage (qui utilise lui-même du web-scraping) n'est ni régulier, ni exhaustif ; un contenu étant donc potentiellement absent ou présent selon les dates d'archives. Après quelques manipulations, j'ai donc retenu : [l'archive du 22 février 2017](https://web.archive.org/web/20170222060359/http://www.geotribu.net/).

![Internet Archive serveurs](https://cdn.geotribu.fr/img/tuto/webscraping/internet_archive_server.jpg "Serveurs de l'Internet Archive "){: .img-center loading=lazy }

### Le logiciel : Scrapy

Python étant à la fois mon langage de prédilection et l'un de ceux tout indiqués pour le web-scraping, j'ai donc opté pour [Scrapy]. En avant pour l'installation dans un joli environnement virtuel avec Python 3.8 :

```bash
python -m pip install scrapy==2.3.*
```

Une fois installé, Scrapy permet de générer rapidement une structure de projet et aussi un shell interactif qui permet de "jouer" avec le site web visé : `scrapy shell`.

#### Scrapy shell

Un site web c'est un ensemble plus ou moins organisé de pages parmi lesquelles on navigue à la souris ou au clavier. La première étape du web-scraping est donc de reproduire ce comportement sans interaction : naviguer dans le site web. Dans notre cas, on souhaite savoir parcourir la liste des revues de presse et déterminer comment on "ouvre" une revue de presse.

On passe donc notre URL cible au Scrapy shell :

```bash
scrapy shell "https://web.archive.org/web/20170222025421/http://www.geotribu.net/revues-de-presse"
```

Scrapy réalise alors déjà un gros travail de requêtes, mise en cache, etc. qui se traduit par un bon paquet de messages. La page est stockée dans un objet attaché à la variable `response` :

```python
>>> response
<200 https://web.archive.org/web/20170222025421/http://www.geotribu.net/revues-de-presse>

>>> dir(response)
[... 'body', 'body_as_unicode', 'cb_kwargs', 'certificate', 'copy', 'css', 'encoding', 'flags', 'follow', 'follow_all', 'headers', 'ip_address', 'json', 'meta', 'replace', 'request', 'selector', 'status', 'text', 'url', 'urljoin', 'xpath']
```

Parmi les méthodes de `response`, 2 en particulier nous intéressent pour se balader dans la structure de la page : `css` et `xpath`. Il s'agit des deux langages que Scrapy appelle les `selectors`. Le premier, CSS, est donc la façon dont une page est présentée/rendue ; le second, [XPath](https://fr.wikipedia.org/wiki/XPath), moins connu, est conçu spécifiquement pour se balader dans les documents XML et consorts (donc HTML par extension).

Si j'ai déjà eu à faire à XPath (ô joie des métadonnées mal formatées...), il est plus facile de repérer la structure cible avec le CSS. Surtout quand on a contribué au site web cible.

#### Parcourir le site web

On garde en tête notre objectif : parcourir la page des revues de presse pour extraire les informations de chaque revue de presse à explorer séparément par la suite. Pour y parvenir, pas de secret : il faut identifier et suffisamment discriminer les styles CSS souhaités. Et Drupal 6 ne nous a pas vraiment préparé à cela...

![Sources Geotribu Drupal](https://cdn.geotribu.fr/img/tuto/webscraping/scraping_geotribu_css.png "La cascade de styles dans l'ancien site : un passage obligé"){: .img-center loading=lazy }

Après quelques litres de collyre en lisant le HTML/CSS et les messages d'erreur de Scrapy, voici ce à quoi on arrive :

```python
# titre de la page
>>> response.css('title::text').getall()[0]
'GeoTribu | Revues de presse'

# première rdp de la liste
>>> t = response.css('div.title-and-meta')[0]

# titre
>>> rdp_title_section = t.css("div.title-and-meta")
>>> rdp_title = rdp_title_section.css("h2.node__title a::text").get()
>>> rdp_title
'Revue de presse du 27 janvier'

# url
>>> rdp_url_rel = rdp_title_section.css("h2.node__title a::attr(href)").get()
>>> rdp_url_rel
'/web/20170222025421/http://www.geotribu.net/GeoRDP/20170127'
```

On a donc compris comment isoler l'url relative de chaque revue de presse :v: !

#### Décortiquer les contenus

Une fois la navigation résolue, on peut alors procéder de même avec le contenu des pages ciblées :

```python
# -- Parcourir la revue de presse choisie
fetch("https://web.archive.org/" + rdp_url_rel)

# contenu de la rdp
rdp = response.css('article')[0]

# sections
>>> rdp_sections
['Client', 'Serveur', 'Représentation Cartographique', 'Conférences', 'Divers']
```

Inutile de détailler davantage, je pense que tout le monde a compris le principe et cet article est déjà bien long !

#### Mise en musique

Une fois que l'on a démêlé la structure des contenus ciblés, on met tout cela en musique dans le projet Scrapy :

- à chaque type de contenu, son _item_ : un objet dont les attributs correspondent à ce que l'on attend de récupérer d'un contenu (titre, introduction, etc.)
- un _spider_ chargé d'extraire les informations ciblées dans un ensemble de pages : par exemple, les articles et les revues de presse n'ont pas la même structure, il faut donc adapter le _crawling_. De plus, cela permet de cibler un certain type de contenus
- concevoir les _pipeline_ qui traiteront les données récuprées : nettoyage des balises, exclusion, conversion dans le ou les formats de destination, etc.
- éventuellement jouer avec les couches intermédiaires (_middlewares_) pour gérer des cas particuliers ou personnaliser des comportements : redimensionnement des images, etc.
- le tout orchestré par un fichier de configuration `settings.py` dont les options sont nombreuses, sans compter les éventuelles extensions.

![Architecture Scrapy](https://cdn.geotribu.fr/img/tuto/webscraping/scrapy_architecture.png "Schéma d'architecture des modules de Scrapy."){: .img-center loading=lazy }

Bref, à ce stade, le travail est loin d'être terminé. Soyons réaliste : ça n'est pas très "rentable" lorsqu'il s'agit, comme dans notre cas, de faire tourner notre programme de scraping que quelques fois seulement, le temps en fait de le peaufiner et de gérer les cas particuliers.

Mais l'idée est bien là : parcourir un site web de façon automatisée pour en extraire les contenus.

### Aller plus loin

Si vous souhaitez aller au bout de la démarche, vous pouvez lancer le projet que j'ai développé et utilisé pour Geotribu. Je n'ai pas la prétention de dire que c'est un modèle du genre mais ça a le mérite de tourner (sinon dites-le moi) et d'illustrer le propos :

- [le code source](https://github.com/geotribu/scraping_old_site/)
- [la documentation](https://geotribu-web-scraping-resurrection.readthedocs.io/)

Une fois le projet installé, il est aisé de lancer le scraping via une simple ligne de commande, en spécifiant  :

```bash
# pour les revues de presse
scrapy crawl geotribu_rdp -L WARNING
# pour les articles
scrapy crawl geotribu_articles -L WARNING
```

----

## Conclusion

Les plus minutieux auront remarqué que tous les contenus n'ont pas été récupérés ou intégrés dans le site actuel. En effet, plusieurs raisons à cela.

D'abord par manque de temps : par principe, je suis plus fervent d'investir dans le futur que dans le passé. Au-delà d'une certaine limite, autant consacrer du temps à des nouveaux contenus et à l'actualisation de la dynamique.

Ensuite, cela fatigue les serveurs de l'[Internet Archive] : c'est pas très fair-play et de toute façon ça renvoie des [429](https://developer.mozilla.org/fr/docs/Web/HTTP/Status/429) en chaîne. Il aurait fallu passer par des instances cloud permettant de simuler des connexions de différents endroits ([Crawlera de ScrapingHub](https://www.scrapinghub.com/crawlera/) par exemple), mais nous n'avons pas sassez de public ou de demande pour que le jeu en vaille la chandelle.

Maintenant on sait comment moissonner un site web, en l'occurence l'ancien Geotribu. Dans le prochain article, on verra quoi faire de tous cette soupe de HTML/CSS/Javascript/Images.

[Suite : convertir des fichiers HTML en Markdown :fontawesome-solid-forward:](2020-09-11_html2markdown.md){: .md-button }
{: align=middle }

----

<!-- geotribu:authors-block -->

<!-- Hyperlinks reference -->
[Scrapy]: https://scrapy.org/
[Internet Archive]: https://archive.org
