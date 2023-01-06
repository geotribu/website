---
title: "Structure d'une news"
authors:
    - Geotribu
categories:
    - contribution
date: "2021-09-30 10:20"
description: "Ajouter une actualité à la prochaine revue de presse de Geotribu (GeoRDP)."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/collaboration_world.png"
license: default
tags:
    - contribuer
    - guide
    - GeoRDP
    - workflow
---
# Description d'une news

Une news est constituée d'éléments obligatoires :

- une [catégorie](#sections-categories) qui correspond aux [sections de la revue de presse](#sections-categories) et qui est un titre de niveau 2 (`##` en Markdown, `h2` en HTML)
- un titre de niveau 3 (`###` en Markdown, `h3` en HTML)
- une [icône](#icones-de-news)
- un texte

Et d'éléments facultatifs :

- d'un media d'illustration (captures d'écran, vidéo, tweet etc.)
- d'une source
- d'une note particulière (par exemple pour avertir le lectorat que l'auteur/e de la news est lié/e à son contenu)

Pour avoir une idéé concrète de ce à quoi ressemble une news en Markdown, consulter le template :

[Voir le modèle d'une news](https://github.com/geotribu/website/blob/master/content/rdp/templates/template_rdp_news.md?plain=1){: .md-button }
{: align=middle }

----

## Bonnes pratiques

- [x] Ne pas utiliser de balises HTML brutes dans le texte, exception faite des `iframe` et des intégrations tierces (tweets...)
- [x] Ne pas abuser des mises en évidence (**gras**, *italique*...) afin de garder l'équite de lisibilité entre les contenus

[Consulter les règles de rédaction de Geotribu :material-ruler-square:](/contribuer/guides/markdown_quality/){: .md-button .md-button--primary }
{: align=middle }

----

## Sections (= catégories)

![icône voronoi](https://cdn.geotribu.fr/img/logos-icones/divers/voronoi.png "icône voronoi"){: .img-rdp-news-thumb }

Les news sont ventilées dans des sections (= catégories) qui constituent également les titres de niveau 2 de la page. S'il peut surprendre voire n'avoir pas beaucoup de sens, le découpage est historique et permet de conserver la cohérence de la revue de presse à travers les ~~âges~~ années.

Il n'est parfois pas évident de savoir où placer son actualité. Dans ce cas, l'équipe se chargera (ou pas) de replacer la news au bon endroit.

| Catégorie                     | Description | Exemples |
| :---------------------------- | :---------- | :------- |
| Vie du site                   | Précédée du logo rectangulaire du site, il s'agit généralement d'une simple liste à puces dans laquelle on retrouve les derniers contenus publiés ou les récentes évolutions de Geotribu. On a pris l'habitude de préfixer chaque élément par un [emoji](/contribuer/guides/emoji/). |  |
| Sorties de la semaine         | Pour relayer les nouveautés dans les outils de la géomatique. Attention, il ne s'agit pas de paraphraser les notes de version ou les communiqués de presse, mais d'apporter une valeur ajoutée personnelle. | |
| Client                        | **section dépréciée, éviter d'utiliser** | |
| Serveur                       | **section dépréciée, éviter d'utiliser** | |
| Logiciel                      | Découverte, cas d'usage d'un logiciel pas forcément nouveau mais intéressant.  | |
| Représentation cartographique | Dataviz, cartographies, art... | "30DayMapChallenge", "[Francepixel (Bâti)](/rdp/2021/rdp_2021-06-18/#francepixel-bati)" |
| OpenStreetMap                 | Toute news liée au plus grand projet de cartographie collaborative mondiale. | |
| Google                        | Idem mais pour la plus grande agence de publicité numérique mondiale. :wink: | |
| Open Data                     | Tout ce qui a trait aux données ouvertes. | "[Ouverture officielle des données de l'IGN](/rdp/2020/rdp_2020-12-11/#open-data)", "Le libre accès aux données implique t'il leur gratuité ?" |
| Geo-event                     | Evénements et conférences. | SAGEO, GéoDataDays, CartoMob, "[Rencontres des utilisateurs francophones de QGIS](/rdp/2020/rdp_2020-12-11/#rencontres-des-utilisateurs-francophones-de-qgis)"... |
| Divers                        | Tout ce qui ne rentre pas dans les autres sections. | "[Des globes made in France](/rdp/2020/rdp_2020-12-11/#des-globes-made-in-france)", "[Les villes sont-elles un corps ?](/rdp/2021/rdp_2021-03-26/#les-villes-ont-elles-un-corps)"   |
| En bref                       | Liste à puces d'informations mineures ou récurrentes.  | Lettre d'informations de la communauté OSM ; version mineure d'un logiciel qui ne nécessite pas un commentaire. |

----

## Icônes

![icône news générique](https://cdn.geotribu.fr/img/internal/icons-rdp-news/news.png "icône news générique"){: .img-rdp-news-thumb }

Afin de respecter la cohérence globale des revues de presse, chaque news démarre par une icône carrée dimensionnée sous forme de vignette. L'auteur/e peut évidemment appliquer l'icône de son choix en l'hébergeant sur le [CDN de Geotribu].  
Si aucune image n'est spécifiée, c'est l'icône générique historique qui est appliquée (celle-la même qui illustre cette section).

!!! tip "Voir aussi"
    - la [syntaxe pour appliquer le style vignette à une image](/contribuer/guides/image/#vignette)
    - [héberger une image ou parcourir les images existantes sur le pseudo-CDN](/contribuer/guides/cdn-images-hebergement/)

### Tableau des icônes génériques { data-search-exclude }

Afin de faciliter la saisie, voici le tableau des icônes génériques avec la syntaxe correspondate à copier/coller :

| Icône | Syntaxe |
| :---: | :-----: |
| ![icône news générique](https://cdn.geotribu.fr/img/internal/icons-rdp-news/news.png "icône news générique"){: .img-rdp-news-thumb } | `#!markdown ![icône news générique](https://cdn.geotribu.fr/img/internal/icons-rdp-news/news.png "icône news générique"){: .img-rdp-news-thumb }` |
| ![icône globe retourné](https://cdn.geotribu.fr/img/internal/icons-rdp-news/absurde.png "icône globe retourné"){: .img-rdp-news-thumb } | `#!markdown ![icône globe retourné](https://cdn.geotribu.fr/img/internal/icons-rdp-news/absurde.png "icône globe retourné"){: .img-rdp-news-thumb }` |
| ![icône globe ancien](https://cdn.geotribu.fr/img/internal/icons-rdp-news/ancien.png "icône globe ancien"){: .img-rdp-news-thumb } | `#!markdown ![icône globe ancien](https://cdn.geotribu.fr/img/internal/icons-rdp-news/ancien.png "icône globe ancien"){: .img-rdp-news-thumb }` |
| ![icône globe video](https://cdn.geotribu.fr/img/internal/icons-rdp-news/animation_video.png "icône globe video"){: .img-rdp-news-thumb } | `#!markdown ![icône globe video](https://cdn.geotribu.fr/img/internal/icons-rdp-news/animation_video.png "icône globe video"){: .img-rdp-news-thumb }` |
| ![icône globe flux](https://cdn.geotribu.fr/img/internal/icons-rdp-news/flux.png "icône globe flux"){: .img-rdp-news-thumb } | `#!markdown ![icône globe flux](https://cdn.geotribu.fr/img/internal/icons-rdp-news/flux.png "icône globe flux"){: .img-rdp-news-thumb }` |
| ![icône globe genre](https://cdn.geotribu.fr/img/internal/icons-rdp-news/genre.png "icône globe genre"){: .img-rdp-news-thumb } | `#!markdown ![icône globe genre](https://cdn.geotribu.fr/img/internal/icons-rdp-news/genre.png "icône globe genre"){: .img-rdp-news-thumb }` |
| ![icône globe boule cristal divination](https://cdn.geotribu.fr/img/internal/icons-rdp-news/globe_boule_cristal_divination.jpg "icône globe boule cristal divination"){: .img-rdp-news-thumb } | `#!markdown ![icône globe boule_cristal_divination](https://cdn.geotribu.fr/img/internal/icons-rdp-news/globe_boule_cristal_divination.jpg "icône globe boule cristal divination"){: .img-rdp-news-thumb }` |
| ![icône globe virus masque](https://cdn.geotribu.fr/img/internal/icons-rdp-news/globe_virus_mask.jpg "icône globe virus masque"){: .img-rdp-news-thumb } | `#!markdown ![icône globe boule_cristal_divination](https://cdn.geotribu.fr/img/internal/icons-rdp-news/globe_virus_mask.jpg "icône globe virus masque"){: .img-rdp-news-thumb }` |
| ![icône globe heatmap](https://cdn.geotribu.fr/img/internal/icons-rdp-news/heatmap.png "icône globe heatmap"){: .img-rdp-news-thumb } | `#!markdown ![icône globe heatmap](https://cdn.geotribu.fr/img/internal/icons-rdp-news/heatmap.png "icône globe heatmap"){: .img-rdp-news-thumb }` |
| ![icône globe itineraire](https://cdn.geotribu.fr/img/internal/icons-rdp-news/itineraire.png "icône globe itineraire"){: .img-rdp-news-thumb } | `#!markdown ![icône globe itineraire](https://cdn.geotribu.fr/img/internal/icons-rdp-news/itineraire.png "icône globe itineraire"){: .img-rdp-news-thumb }` |
| ![icône globe journalisme](https://cdn.geotribu.fr/img/internal/icons-rdp-news/journalisme.png "icône globe journalisme"){: .img-rdp-news-thumb } | `#!markdown ![icône globe journalisme](https://cdn.geotribu.fr/img/internal/icons-rdp-news/journalisme.png "icône globe journalisme"){: .img-rdp-news-thumb }` |
| ![icône globe lobby](https://cdn.geotribu.fr/img/internal/icons-rdp-news/lobby.png "icône globe lobby"){: .img-rdp-news-thumb } | `#!markdown ![icône globe lobby](https://cdn.geotribu.fr/img/internal/icons-rdp-news/lobby.png "icône globe lobby"){: .img-rdp-news-thumb }` |
| ![icône globe matiere](https://cdn.geotribu.fr/img/internal/icons-rdp-news/matiere.png "icône globe matiere"){: .img-rdp-news-thumb } | `#!markdown ![icône globe matiere](https://cdn.geotribu.fr/img/internal/icons-rdp-news/matiere.png "icône globe matiere"){: .img-rdp-news-thumb }` |
| ![icône globe mentale](https://cdn.geotribu.fr/img/internal/icons-rdp-news/mentale.png "icône globe mentale"){: .img-rdp-news-thumb } | `#!markdown ![icône globe mentale](https://cdn.geotribu.fr/img/internal/icons-rdp-news/mentale.png "icône globe mentale"){: .img-rdp-news-thumb }` |
| ![icône globe metro](https://cdn.geotribu.fr/img/internal/icons-rdp-news/metro.png "icône globe metro"){: .img-rdp-news-thumb } | `#!markdown ![icône globe metro](https://cdn.geotribu.fr/img/internal/icons-rdp-news/metro.png "icône globe metro"){: .img-rdp-news-thumb }` |
| ![icône globe microworld](https://cdn.geotribu.fr/img/internal/icons-rdp-news/microworld.png "icône globe microworld"){: .img-rdp-news-thumb } | `#!markdown ![icône globe microworld](https://cdn.geotribu.fr/img/internal/icons-rdp-news/microworld.png "icône globe microworld"){: .img-rdp-news-thumb }` |
| ![icône globe musique disque](https://cdn.geotribu.fr/img/internal/icons-rdp-news/musique_disque.png "icône globe musique disque"){: .img-rdp-news-thumb } | `#!markdown ![icône globe musique disque](https://cdn.geotribu.fr/img/internal/icons-rdp-news/musique_disque.png "icône globe musique disque"){: .img-rdp-news-thumb }` |
| ![icône globe musique note](https://cdn.geotribu.fr/img/internal/icons-rdp-news/musique_note.png "icône globe musique note"){: .img-rdp-news-thumb } | `#!markdown ![icône globe musique note](https://cdn.geotribu.fr/img/internal/icons-rdp-news/musique_note.png "icône globe musique note"){: .img-rdp-news-thumb }` |
| ![icône globe mystique](https://cdn.geotribu.fr/img/internal/icons-rdp-news/mystique.png "icône globe mystique"){: .img-rdp-news-thumb } | `#!markdown ![icône globe mystique](https://cdn.geotribu.fr/img/internal/icons-rdp-news/mystique.png "icône globe mystique"){: .img-rdp-news-thumb }` |
| ![icône globe night](https://cdn.geotribu.fr/img/internal/icons-rdp-news/night.png "icône globe night"){: .img-rdp-news-thumb } | `#!markdown ![icône globe night](https://cdn.geotribu.fr/img/internal/icons-rdp-news/night.png "icône globe night"){: .img-rdp-news-thumb }` |
| ![icône globe noel](https://cdn.geotribu.fr/img/internal/icons-rdp-news/noel.png "icône globe noel"){: .img-rdp-news-thumb } | `#!markdown ![icône globe noel](https://cdn.geotribu.fr/img/internal/icons-rdp-news/noel.png "icône globe noel"){: .img-rdp-news-thumb }` |
| ![icône globe pointillisme](https://cdn.geotribu.fr/img/internal/icons-rdp-news/pointillisme.png "icône globe pointillisme"){: .img-rdp-news-thumb } | `#!markdown ![icône globe pointillisme](https://cdn.geotribu.fr/img/internal/icons-rdp-news/pointillisme.png "icône globe pointillisme"){: .img-rdp-news-thumb }` |
| ![icône globe social](https://cdn.geotribu.fr/img/internal/icons-rdp-news/social.png "icône globe social"){: .img-rdp-news-thumb } | `#!markdown ![icône globe social](https://cdn.geotribu.fr/img/internal/icons-rdp-news/social.png "icône globe social"){: .img-rdp-news-thumb }` |
| ![icône globe triste](https://cdn.geotribu.fr/img/internal/icons-rdp-news/triste.png "icône globe triste"){: .img-rdp-news-thumb } | `#!markdown ![icône globe triste](https://cdn.geotribu.fr/img/internal/icons-rdp-news/triste.png "icône globe triste"){: .img-rdp-news-thumb }` |
| ![icône globe usa](https://cdn.geotribu.fr/img/internal/icons-rdp-news/usa.png "icône globe usa"){: .img-rdp-news-thumb } | `#!markdown ![icône globe usa](https://cdn.geotribu.fr/img/internal/icons-rdp-news/usa.png "icône globe usa"){: .img-rdp-news-thumb }` |
| ![icône globe générique](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "icône globe générique"){: .img-rdp-news-thumb } | `#!markdown ![icône globe world](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "icône globe générique"){: .img-rdp-news-thumb }` |

----

## Crédits

Les icônes génériques ont été créées pour Geotribu par [Mathieu Rajerison](/team/mraj/).
