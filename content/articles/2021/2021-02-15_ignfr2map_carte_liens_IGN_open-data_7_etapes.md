---
title: "ign2map : Du site à la carte"
authors: ["Florian Boret, Julien Moura"]
categories: ["article"]
date: 2021-02-15 11:11
description: ""
image: ""
tags: bash,ign,leaflet,github
---

# ign2map : du site à la carte en 7 étapes

:calendar: Date de publication initiale : 15 Février 2021

**Mots-clés :** bash | IGN | Leaflet | sed | awk

[Accéder à la carte :earth_africa:](https://geotribu.github.io/ign-fr-opendata-download-ui/index.html){: .md-button }
{: align=middle }

## How it started

![Slack GeoTribu](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_idea_slack.png "Slack GeoTribu"){: loading=lazy }
> Le 18 Janvier dans les coulisses de GéoTribu :shushing_face:
{: align=middle }

Sur le papier, la solution proposée paraissait relativement simple mais pour corser le tout on a décidé :

- De travailler en Bash
- De se répartir les tâches de la manière suivante :
    - @Flo sur la construction des scripts
    - @Ju l’enchainement des scripts et sur le déploiement

## 1. Scraping du site de l'IGN

[Le scraping](https://fr.wikipedia.org/wiki/Web_scraping) est une technique qui permet de récupérer le contenu d'une page web en vue de le réutiliser. On a donc scrapé le site de l'[IGN](https://geoservices.ign.fr/documentation/diffusion/telechargement-donnees-libres.html) pour en extraire tous les liens qui s'y trouvaient (ftp, https et http) et on les a ensuite stocké dans un fichier texte.

Solutions utilisées :

- [curl](https://fr.wikipedia.org/wiki/CURL) pour le téléchargement de la page.
- [grep](https://fr.wikipedia.org/wiki/Grep) pour extraire les liens.

```bash
curl "$SOURCE_URL" | \
  grep -oE '\b(https?|ftp|file)://[-A-Za-z0-9+&@# /%?=~_|!:,.;]*[-A-Za-z0-9+&@# /%=~_|]' > "$OUTPUT_FILE"
```

[Consulter le script complet](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/scripts/1_scraper.sh)

![Liens IGN](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_liens_ign.png "Liens IGN"){: loading=lazy .img-center }

## 2. Extraction des fichiers par département, région et pour la France

Une fois tous les liens extraits, on a :

1. lu notre fichier texte pour ne conserver que les liens possédant un identifiant par exemple pour les départements : D001, D976,...
2. exporté le résultat dans des fichiers csv séparés pour chacun des identifiant en prenant le soin d'ajouter une colonne avec l'identifiant.

*Cette étape a été répétée pour les régions et pour la France.*

```bash
grep -E "D$val|DEP_$val" $SOURCE_FILE | awk '{ printf("%s,D'$val_t'\n", $0); }' > "$OUTPUT_DIR/D$val_t.csv"
```

[Consulter le script complet](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/scripts/2_departements.sh)

![Liens IGN par id](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_liens_ign_id.png "Liens IGN par id"){: loading=lazy .img-center }

## 3. Nettoyage des liens (format, doublons)

Comme on peut le voir sur la capture précédente, il y a de nombreux doublons liés notamment à la structure de la page html puisque l'IGN affiche le lien complet sur sa page :

```html
<a href="https://url.com">https://url.com</a>
```

On a donc utilisé :

- [sort](https://fr.wikipedia.org/wiki/Sort_(Unix)) pour trier les liens et ne conserver qu'un seul lien unique.
- [grep](https://fr.wikipedia.org/wiki/Grep) pour ne garder que les liens ayant une extension .7z (extension utilisée par l'IGN pour compresser ses fichiers).

```bash
cat "$INPUT_DIR"/2_departements/*csv | sort -u | grep -F '.7z' > "$OUTPUT_DIR/3_liens_par_dep_clean_ext.csv"
```

[Consulter le script complet](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/scripts/3_filtered_csv.sh)

En sortie on obtient, on obtient un fichier csv propre par découpage géographique.

![Liens IGN propres](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_liens_propres.png "Liens IGN propres"){: loading=lazy .img-center }

## 4. Mise en forme des données avant jointure

Les liens étant proprement organisés, nous avons ensuite généré un fichier csv par produit IGN (BDORTHO, BDFORET,...) en réalisant également une transposition par identifiant géographique afin de faciliter la jointure prévue après.

[Consulter le script complet](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/scripts/4_csv_type.sh)

![Liens IGN type](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_liens_transposition.png "Liens IGN type"){: loading=lazy .img-center }

## 5. Création des topojson

[Mapshaper](https://mapshaper.org) a été utilisé pour créer les fichiers topojson en s'appuyant notamment sur la donnée [ADMIN EXPRESS de l'IGN](https://geoservices.ign.fr/documentation/diffusion/telechargement-donnees-libres.html#admin-express). Ces fichiers topojson utilisés par la suite comme des modèles ne sont générés qu'une seule fois.

A noter la donnée ADMIN EXPRESS n'intègre pas les collectivités d'outre mer (COM). On a donc du compléter ce manque en utilisant le fichier suivant disponible sur [Data.gouv.fr](https://www.data.gouv.fr/) : [Découpage administratif des COM St Martin et St Barthélemy "Format Admin-Express"](https://www.data.gouv.fr/fr/datasets/decoupage-administratif-des-com-st-martin-et-st-barthelemy-format-admin-express/) mis à disposition par R. Maziere.

## 6. Jointure avec les topojson

L'étape de la jointure en bash a sans aucun doute été l'étape la plus prise de tête. Pour faire simple on a utilisé [sed](https://fr.wikipedia.org/wiki/Stream_Editor) pour remplacer l'identifiant géographique de notre topojson source par notre identifiant géographique et les liens associés. En sortie, les nouveaux fichiers topojson ont ensuite été placés dans un répertoire utilisé par la page html de la carte.

[Consulter le script complet](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/scripts/5_join_csv_topojson.sh)

## 7. Création automatique du fichier index.html

Pour cette dernière étape, l'idée était de pouvoir générer automatiquement la page html pour être plus réactif en cas d'évolution des données libérées par l'IGN.

Après avoir écrit une première mouture de la page html, on a ensuite converti cette page en un modèle en introduisant des variables liées notamment à l'appel des fichiers topojson et à la configuration des popups. Une fois le template prêt, on s'est attaché à remplacer ces variables en utilisant une nouvelle fois [sed](https://fr.wikipedia.org/wiki/Stream_Editor) pour générer de manière dynamique la page index.html.

[Consulter le script complet](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/scripts/6_create_html.sh)

![ign2map html](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_html.png "ign2map html"){: loading=lazy .img-center }

!!! tip "Lire des topojson avec Leaflet"
  Dans Leaflet, il est possible de lire des fichiers topojson en utilisant l'extension [leaflet-omnivore](https://github.com/mapbox/leaflet-omnivore).

![ign2map](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_html_rendu.png "ign2map"){: loading=lazy .img-center }

----

## La publication

On doit avouer :

- que le couvre-feu, nous a un peu aidé car il ne nous aura fallu que 15 jours pour arriver au résultat publié et quelques jours de plus pour mettre tout ça au propre.
- qu'on ne s'attendait pas à un tel retentissement

![Tweet IGN](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_tweet_ign.png "Tweet IGN"){: loading=lazy .img-center }

----

## Auteurs

--8<-- "content/team/fbor.md"

--8<-- "content/team/jmou.md"

<!-- Hyperlinks reference -->
[GitHub Actions]: https://github.com/features/actions
[GitHub Pages]: https://guides.github.com/features/pages/
[YAML]: https://fr.wikipedia.org/wiki/YAML
