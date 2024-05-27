---
title: 'ign2map : Du site à la carte en 7 étapes'
authors:
    - Florian Boret
    - Julien Moura
categories:
    - article
comments: true
date: 2021-02-15
description: 'ign2map : le petit projet de Geotribu pour rendre l’expérience de téléchargement des données ouvertes de l''IGN plus interactive.'
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_html_rendu.png
tags:
    - awk
    - Bash
    - GitHub
    - IGN
    - Leaflet
    - sed
---

# ign2map : du site à la carte en 7 étapes

:calendar: Date de publication initiale : 15 Février 2021

## Intro

![icône IGN](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/ign.png "IGN"){: .img-thumbnail-left }

A la surprise de tous, [l'IGN annonçait l'ouverture de ses données fin 2020 pour une libération au 1er Janvier 2021](../../rdp/2020/rdp_2020-12-11.md#ouverture-officielle-des-donnees-de-lign).  
Après des mois à attendre la refonte de l'espace professionnel, nous étions nombreux à penser que cette dynamique d'ouverture allait s'accompagner du lancement d'une plateforme ergonomique de téléchargement des données mais *que nenni*! Les liens ont continué à [s'accumuler sur une page unique](https://geoservices.ign.fr/documentation/diffusion/telechargement-donnees-libres.html).

Dans ce contexte, on s’interrogeait en coulisses sur une manière de rendre cette masse d'informations plus lisible par tous :point_down:.

## How it started

![Slack GeoTribu](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_idea_slack.png "Slack GeoTribu"){: loading=lazy }
> Le 18 Janvier dans les coulisses de GéoTribu :shushing_face:
{: align=middle }

La solution proposée par Julien ne paraissait pas trop complexe à mettre en oeuvre mais pour corser le tout on a décidé :

- De travailler en Bash
- De se répartir les tâches de la manière suivante :
    - [@Flo](../../team/florian-boret.md) sur la construction des scripts
    - [@Ju](../../team/julien-moura.md) l’enchainement des scripts et sur le déploiement

Et c'est parti pour une aventure en 7 étapes :rocket: !

----

## 1. Scraping du site de l'IGN

[Le scraping](https://fr.wikipedia.org/wiki/Web_scraping) est une technique qui permet de récupérer le contenu d'une page web en vue de le réutiliser (voir aussi [cet article](2021-02-09_statistiques_twitter.md) ou [celui-ci](../2020/2020-09-08_web-scraping_scrapy_geotribu.md)).  
On a donc scrapé le site de l'[IGN](https://geoservices.ign.fr/documentation/diffusion/telechargement-donnees-libres.html) pour en extraire tous les liens qui s'y trouvaient (ftp, https et http) et on les a ensuite stockés dans un fichier texte.

Solutions utilisées :

- [curl](https://fr.wikipedia.org/wiki/CURL) pour le téléchargement de la page.
- [grep](https://fr.wikipedia.org/wiki/Grep) pour extraire les liens.

```bash title="Scraping du site de l'IGN" linenums="1"
curl "$SOURCE_URL" | \
  grep -oE '\b(https?|ftp|file)://[-A-Za-z0-9+&@# /%?=~_|!:,.;]*[-A-Za-z0-9+&@# /%=~_|]' > "$OUTPUT_FILE"
```

![Liens IGN](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_liens_ign.png "Liens IGN"){: loading=lazy }
{: align=middle }

[Consulter le script complet :fontawesome-regular-file-code:](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/scripts/1_scraper.sh){: .md-button }
{: align=middle }

----

## 2. Extraction des fichiers par département, région et pour la France

Une fois tous les liens extraits, on a :

1. lu notre fichier texte pour ne conserver que les liens possédant un identifiant par exemple pour les départements : D001, D976,...
2. exporté le résultat dans des fichiers csv séparés pour chacun des identifiants en prenant le soin d'ajouter une colonne avec l'identifiant.

*Cette étape a été répétée pour les régions et pour la France.*

```bash title="Extraction des fichiers" linenums="1"
grep -E "D$val|DEP_$val" $SOURCE_FILE | awk '{ printf("%s,D'$val_t'\n", $0); }' > "$OUTPUT_DIR/D$val_t.csv"
```

![Liens IGN par id](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_liens_ign_id.png "Liens IGN par id"){: loading=lazy }
{: align=middle }

[Consulter le script complet :fontawesome-regular-file-code:](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/scripts/2_departements.sh){: .md-button }
{: align=middle }

----

## 3. Nettoyage des liens (format, doublons)

Comme on peut le voir sur la capture précédente, il y a de nombreux doublons liés notamment à la structure de la page html puisque l'IGN affiche le lien complet sur sa page :

```html title="Lien linenums="1"
<a href="https://url.com">https://url.com</a>
```

On a donc utilisé :

- [sort](https://fr.wikipedia.org/wiki/Sort_(Unix)) pour trier les liens et ne conserver qu'un seul lien unique.
- [grep](https://fr.wikipedia.org/wiki/Grep) pour ne garder que les liens ayant une extension .7z (extension utilisée par l'IGN pour compresser ses fichiers).

```bash title="Nettoyer les liens" linenums="1"
cat "$INPUT_DIR"/2_departements/*csv | sort -u | grep -F '.7z' > "$OUTPUT_DIR/3_liens_par_dep_clean_ext.csv"
```

En sortie, on obtient un fichier csv propre par découpage géographique.

![Liens IGN propres](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_liens_propres.png "Liens IGN propres"){: loading=lazy }
{: align=middle }

[Consulter le script complet :fontawesome-regular-file-code:](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/scripts/3_filtered_csv.sh){: .md-button }
{: align=middle }

----

## 4. Mise en forme des données avant jointure

Les liens étant proprement organisés, nous avons ensuite généré un fichier csv par produit IGN (BDORTHO, BDFORET,...) en réalisant également une transposition par identifiant géographique afin de faciliter la jointure prévue après.

![Liens IGN type](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_liens_transposition.png "Liens IGN type"){: loading=lazy }
{: align=middle }

[Consulter le script complet :fontawesome-regular-file-code:](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/scripts/4_csv_type.sh){: .md-button }
{: align=middle }

----

## 5. Création des topojson

[Mapshaper](https://mapshaper.org) a été utilisé pour créer les fichiers topojson en s'appuyant notamment sur la donnée [ADMIN EXPRESS de l'IGN](https://geoservices.ign.fr/documentation/diffusion/telechargement-donnees-libres.html#admin-express). Ces fichiers topojson utilisés par la suite comme des modèles ne sont générés qu'une seule fois.

A noter la donnée ADMIN EXPRESS n'intègre pas les collectivités d'outre mer (COM). On a donc du compléter ce manque en utilisant le fichier suivant disponible sur [Data.gouv.fr](https://www.data.gouv.fr/) : [Découpage administratif des COM St Martin et St Barthélemy "Format Admin-Express"](https://www.data.gouv.fr/fr/datasets/decoupage-administratif-des-com-st-martin-et-st-barthelemy-format-admin-express/) mis à disposition par R. Maziere.

----

## 6. Jointure avec les topojson

L'étape de la jointure en bash a sans aucun doute été l'étape la plus prise de tête. Pour faire simple on a utilisé [sed] pour remplacer l'identifiant géographique de notre topojson source par notre identifiant géographique et les liens associés. En sortie, les nouveaux fichiers topojson ont ensuite été placés dans un répertoire utilisé par la page html de la carte.

[Consulter le script complet :fontawesome-regular-file-code:](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/scripts/5_join_csv_topojson.sh){: .md-button }
{: align=middle }

----

## 7. Création automatique du fichier index.html

Pour cette dernière étape, l'idée était de pouvoir générer automatiquement la page html pour être plus réactif en cas d'évolution des données libérées par l'IGN.

Après avoir écrit une première mouture de la page html, on a ensuite converti cette page en un modèle en introduisant des variables liées notamment à l'appel des fichiers topojson et à la configuration des popups. Une fois le template prêt, on s'est attaché à remplacer ces variables en utilisant une nouvelle fois [sed] pour générer de manière dynamique la page index.html.

![ign2map html](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_html.png "ign2map html"){: loading=lazy }
{: align=middle }

[Consulter le script complet :fontawesome-regular-file-code:](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/scripts/6_create_html.sh){: .md-button }
{: align=middle }

!!! tip "Lire des topojson avec Leaflet"
    Dans Leaflet, il est possible de lire des fichiers topojson en utilisant l'extension [leaflet-omnivore](https://github.com/mapbox/leaflet-omnivore).

![ign2map](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_html_rendu.png "ign2map"){: loading=lazy }
{: align=middle }

[Accéder à la carte :earth_africa:](https://geotribu.github.io/ign-fr-opendata-download-ui/index.html){: .md-button }
{: align=middle }

----

## :rocket: La publication

On doit avouer :

- que le couvre-feu, nous a un peu aidé car il ne nous aura fallu que 15 jours pour arriver au résultat publié et quelques jours de plus pour mettre tout ça au propre.
- qu'on ne s'attendait pas à un tel retentissement (Quelques chiffres : plus de 40000 vues sur twitter, plus de 700 clics sur le lien du tweet, 250 likes et plus de 110 retweets).

<blockquote class="twitter-tweet tw-align-center" data-lang="fr"><p lang="fr" dir="ltr">Bravo et merci pour cette initiative, on valide 🙏 <a href="https://t.co/sKvEY8SPix">https://t.co/sKvEY8SPix</a></p>&mdash; IGN France (@IGNFrance) <a href="https://twitter.com/IGNFrance/status/1356272563152945154?ref_src=twsrc%5Etfw">1 février 2021</a></blockquote>

## La suite

Un autre article sera publié dans les prochains jours pour vous expliquer la partie sur l'automatisation et le déploiement depuis Github. Restez connectés à GeoTribu : [LinkedIn](https://www.linkedin.com/feed/hashtag/?keywords=geotribu) - [RSS]({{ config.site_url}}feed_rss_created.xml) - [Twitter](https://twitter.com/geotribu) :wink:.

[Suite : automatiser l'exécution et le déploiement :fontawesome-solid-forward:](2021-02-19_ignfr2map_automatisation_deploiement.md){: .md-button }
{: align=middle }

----

<!-- geotribu:authors-block -->

<!-- Hyperlinks reference -->
[sed]: https://fr.wikipedia.org/wiki/Stream_Editor
