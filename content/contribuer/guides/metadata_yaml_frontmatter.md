---
title: "Rédiger en Markdown : comprendre l'en-tête"
categories: ["contribution"]
date: "2021-01-05 20:20"
description: "Rédiger en Markdown : de l'importance de l'en-tête (YAML front-matter) pour définir les métadonnées, la navigation et le référencement."
image: "https://cdn.geotribu.fr/img/internal/contribution/markdown/markdown_yaml_frontmatter.png"
tags: contribuer,tutoriel,markdown,rédaction,yaml frontmatter,seo,head
---

# L'en-tête des contenus (*YAML frontmatter*)

Les sites statiques basés sur du contenu en Markdown (ou autre syntaxe *flat* comme rst ou autre) ont recours à un en-tête en YAML, appelé aussi *YAML front-matter*, qui contient des métadonnées sur la page voire carrément des instructions spécifiques à son rendu (template à utiliser, activation/désactivation de fonctionnalités...).

Le site Geotribu tire également profit de ce mécanisme.

## Syntaxe

L'en-tête est défini en haut de la page par un ensemble de clés/valeurs encadré par `---`. Chaque élément a un rôle ou une réutilisation :

- `title` : utilisé dans le menu de navigation de gauche, le RSS et le SEO (référencement). Cela autorise par exemple un titre différent que celui affiché dans l'article
- `authors` : liste des contributeurs réutilisée dans les meta-tags de la page et le SEO (via schema.org)
- `categories` : contient la typologie du contenu permettant des comportements adaptés. Pour l'instant c'est utilisé pour définir le schéma JSON-LD  à utiliser, mais c'est prévu dans le RSS aussi,
- `date` : date de création publique de l'article, correspondant à la date de première publication. Utilisée dans le RSS, le SEO et certains moteurs d'affichage.
- `description` : SEO, recherche interne du site, meta-tag, RSS
- `image` : RSS et partage des articles dans les réseaux sociaux (c'est ce qui fait qu'on a un jouli rendu quand on partage dans Twitter ou LinkedIn par exemple). Dimensions : entre 300x600 et 400x800.
- `tags` : pour l'instant ça ne sert à rien mais c'est prévu pour permettre un classement des contenus par mots-clés.

## Exemple

Exemple pour la GeoRDP de Noël 2020 :

```yaml
---
title: "Revue de presse du 25 décembre 2020"
authors: ["Geotribu"]
categories: ["Revues de presse"]
date: 2020-12-25 14:20
description: "GeoRDP du 25 décembre 2020 : la revue de presse géomatique de Geotribu pour souhaiter Joyeux Noël et bonnes fêtes !"
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/merry_christmas_blender.png"
tags: rdp,ign,geoserver,nominatim,opendata,cerema,fig,georezo,drone,postgis,mapbox,openlayers
---
```
