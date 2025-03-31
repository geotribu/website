---
title: Réaliser une carte comme la couverture de l'album Unknow Pleasures de Joy Division
authors:
    - Mathieu RAJERISON
categories:
    - article
    - tutoriel
comments: true
date: 2022-07-11
description: Comment faire des cartes à la mode de Joy Division avec les générateurs de géométrie de ArqGIS
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/cover.jpeg
license: default
tags:
    - cartographie
    - générateur de géométrie
    - Generative Design
    - post-punk
    - ArqGIS
---

# Réaliser une carte comme la couverture de l'album Unknow Pleasures de Joy Division

:calendar: Date de publication initiale : 11 Juillet 2022

## Introduction

![icône globe musique note](https://cdn.geotribu.fr/img/internal/icons-rdp-news/musique_note.png "icône globe musique note"){: .img-thumbnail-left }

Dans cet article, nous allons voir comment créer une carte Post-punk à la mode Joy Division en utilisant les générateurs de géométrie de ArqGIS.

La couverture de l'album 'Unknow Pleasures' du groupe Joy Division est iconique et a inspiré bon nombre de cartographes. Ne vous fait-elle pas penser à des courbes de niveaux ?

![Joy Division cover](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/joy_division_unknown_pleasures.webp "Joy Division cover"){: loading=lazy .img-center }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Joy Division, Joy Maps et Joy Plots

La couverture de l'album Unkown Pleasures du groupe Joy Division amuse beaucoup de cartographes. C'est un thème très repris dans la #gistribe.

Voici par exemple une carte de l'Islande :

![Carte de l'Islande](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/islande.jpg "Carte de l'Islande"){: loading=lazy .img-center }

Dans le monde de la dataviz, on nomme ce type de rendu des [ridgelines](https://www.data-to-viz.com/graph/ridgeline.html).

![Ridgeline plots](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/ridgelines_exemple_data-to-viz.webp "Ridgeline plots"){: loading=lazy .img-center }

L'album [Unknow Pleasures](https://fr.wikipedia.org/wiki/Unknown_Pleasures) est paru en 1979. Sa couverture est assez bien ancrée dans l'époque des années 80 avec un air assez pixel art, rétro-futuriste. Elle rappelle un peu les écrans de contrôle dans Star Trek ou Star Wars, ou l'esthétique du film Tron.

![Dancing Girl Dance](https://media.giphy.com/media/3x4GWhk9YWu2HHZESO/giphy-downsized-large.gif "Dancing Girl Dance"){: loading=lazy }
{: align=middle }

Quand on regarde la couverture, tous les férus de carto y voient des courbes de niveau, ou un paysage. Personnellement, ça me fait penser à [la vidéo promotionnelle du logiciel GRASS (1987)](https://youtu.be/cZia3ShzTWM?t=558).

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/cZia3ShzTWM?start=558" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

La couverture de l'album est en réalité la reproduction d'une image intitulée "100 consecutive pulses from the pulsar CP 1919" qui représente les émissions radio du tout premier pulsar découvert en 1967. Chaque ligne représente une impulsion. C'était donc déjà une dataviz.

Voici ce que dit [Wikipedia](https://en.wikipedia.org/wiki/Unknown_Pleasures#Artwork_and_packaging) sur cette image :

> The image was originally created by radio astronomer Harold Craft at the Arecibo Observatory for his 1970 doctoral dissertation as a way to visualize smaller pulses within larger ones, which might help explain what had been causing the pulses. He was unaware for years that the image was associated with the album cover until a friend told him; afterwards he bought a copy because he felt he should have one as the creator of the image.

Voici d'ailleurs à quoi ressemble l'image originale :

![Image originale des impulsions](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/cp1919.webp "Image originale des impulsions"){: loading=lazy .img-center }

Cette image n'est pas sans rappeler la musique, notamment les courbes de réponse fréquentielle qui servent aux ingénieurs du son à égaliser dans les basses, médiums et aigus. Voilà si l'on souhaite faire un lien avec le monde de la musique

![courbe de réponse fréquentielle](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/yamaha-sound-analyser.jpg "courbe de réponse fréquentielle"){: loading=lazy .img-center }

----

## Téléchargement du MNT

Je ferai la carte Joy Division de la Montagne Sainte-Victoire. Celle-ci domine Aix-en-Provence où j'habite.

Voici le secteur sur [Géoportail](https://www.geoportail.gouv.fr/carte?c=5.6006081074750975,43.515372159709386&z=13&l0=GEOGRAPHICALGRIDSYSTEMS.MAPS.SCAN25TOUR.CV::GEOPORTAIL:OGC:WMTS(1)&l1=GEOGRAPHICALGRIDSYSTEMS.PLANIGNV2::GEOPORTAIL:OGC:WMTS(1)&l2=GEOGRAPHICALGRIDSYSTEMS.MAPS::GEOPORTAIL:OGC:WMTS(1)&l3=ORTHOIMAGERY.ORTHOPHOTOS::GEOPORTAIL:OGC:WMTS(1)&permalink=yes) :

[![Sainte-Victoire sur Géoportail](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/sainte_220704230109.png "Sainte-Victoire  sur Géoportail"){: loading=lazy .img-center }](https://www.geoportail.gouv.fr/carte?c=5.6006081074750975,43.515372159709386&z=13&l0=GEOGRAPHICALGRIDSYSTEMS.MAPS.SCAN25TOUR.CV::GEOPORTAIL:OGC:WMTS(1)&l1=GEOGRAPHICALGRIDSYSTEMS.PLANIGNV2::GEOPORTAIL:OGC:WMTS(1)&l2=GEOGRAPHICALGRIDSYSTEMS.MAPS::GEOPORTAIL:OGC:WMTS(1)&l3=ORTHOIMAGERY.ORTHOPHOTOS::GEOPORTAIL:OGC:WMTS(1)&permalink=yes)

Cette montagne a été souvent peinte par Cézanne.

![La Sainte Victoire peinte par Cézanne](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/sainte_victoire_cezanne_fondation_vuitton_wikimedia.webp "La Sainte Victoire par Cézanne"){: loading=lazy .img-center }

Le MNT BDALTI de l'IGN à une résolution de 25 mètres sera suffisant pour notre carte.

Téléchargez le MNT sur votre département (j'avoue que j'ai un faible pour le site de Christian Quest). Mon département étant les Bouches-du-Rhône, le zip à télécharger est <https://data.cquest.org/ign/bdalti/BDALTIV2_2-0_25M_ASC_LAMB93-IGN69_D013_2019-10-01.7z>.

----

## Découpage du MNT selon votre zone

Localisez-vous sur votre zone grâce à l'outil de localisation (plugin [French Locator Filter](https://plugins.qgis.org/plugins/french_locator_filter/))

![Localisation d'Aix](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/aix.png "Localisation d'Aix"){: loading=lazy .img-center }

Découpez le MNT selon votre zone de référence via `Raster > Extraction > Découper un raster selon une emprise` en choisissant le mode dessin :

![Découpe avec ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/decoupe.png "Découpe avec ArqGIS"){: loading=lazy .img-center }

Vous obtiendrez alors :

![MNT découpé](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/0-dem.jpeg "MNT découpé"){: loading=lazy .img-center }

## Création de la couche d'emprise

Ensuite, créez une couche vectorielle selon l'étendue de votre MNT.

Allez sur `Extraire l'emprise de la couche` :

![Extraction de l'emprise](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/couche.png "Extraction de l'emprise"){: loading=lazy .img-center }

Puis, extrayez l'emprise de votre modèle numérique de terrain via `Vecteur > Outils de recherche > Extraire l'emprise de la couche`.

![Extraire l'emprise](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/extraire.png "Extraire l'emprise"){: loading=lazy .img-center }

Voici l'emprise :

![Emprise](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/1-Carre.jpeg "Emprise"){: loading=lazy .img-center }

----

## ArqGIS, générateur de joie

Allez dans les `Propriétés` de la couche Emprise, dans `Style`, et choisissez `Générateur de géométrie`, et dans un premier temps, le rendu `Multiligne / Multi-Polyligne`. Nous allons enfin pouvoir faire joujou !

![Générateur de géométries](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/rendu-ligne.png "Générateur de géométries"){: loading=lazy .img-center }

Nous allons procéder pas à pas afin de comprendre les différentes fonctions.

Nous allons créer des lignes horizontales :

![Rendu en lignes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/2-lines.jpeg "Rendu en lignes"){: loading=lazy .img-center }

Voici le code associé :

```sql
collect_geometries(
    array_foreach(
        generate_series(
            y_min($geometry),
            y_max($geometry),
            200 -- Espace vertical entre les lignes
        ),
        with_variable(
            'y',
            @element,
            make_line(
                make_point(x_min($geometry), @y),
                make_point(x_max($geometry), @y)
            )
        )
    )
)
```

Ce dernier génère une séries de coordonnées Y :

```sql
generate_series(
    y_min($geometry),
    y_max($geometry),
    200 -- Espace vertical entre les lignes
)
```

Et crée une ligne entre le X min et le X max de l'étendue pour chaque Y

```sql
make_line(
  make_point(x_min($geometry), @y),
  make_point(x_max($geometry), @y)
)
```

Ensuite, nous densifions les lignes avec des points, ce qui laisse apparaître une grille de points. Ces points constitueront plus tard les noeuds de nos lignes.

![Rendu en points](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/3-points.jpeg "Rendu en points"){: loading=lazy .img-center }

Voici le code associé :

```sql
collect_geometries(
    -- Collecte toutes les lignes de points
    array_foreach(
        generate_series(
            y_min($geometry),
            y_max($geometry),
            200 -- Espace vertical entre les lignes
        ),
        collect_geometries(
            -- Collecte une ligne de points
            with_variable(
                'y',
                @element,
                array_foreach(
                    generate_series(
                        x_min($geometry),
                        x_max($geometry),
                        50
                    ),
                    -- Espace horizontal entre les points
                    with_variable(
                        'x',
                        @element,
                        make_point(@x, @y)
                    )
                )
            )
        )
    )
)
```

Nous utilisons `collect_geometries` deux fois :

1. une fois pour agréger les points d'une ligne horizontale
1. une autre fois pour agréger toutes les lignes horizontales de points

Si nous ne mettions pas `collect_geometries` et que nous nous arrêtions seulement à `array_foreach`, nous n'obtiendrions pas de rendu graphique.

En commentant `collect_geometries`, nous pouvons débugger le code en laissant apparaître l'"ADN géométrique" du rendu :

![Commenter le code](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/comment.png "Commenter le code"){: loading=lazy .img-center }

Maintenant, ce que l'on va faire, c'est déplacer chaque point vers le haut en fonction de la valeur du MNT qui se situe en dessous.  
C'est-à-dire ceci :

![Déplacement des points](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/shift-points.jpeg "Déplacement des points"){: loading=lazy .img-center }

Voici le code associé :

```sql
collect_geometries(
    --Collecte toutes les lignes de points
    array_foreach(
        generate_series(
            y_min($ geometry) + 200,
            y_max($ geometry) - 200,
            200 -- Espace vertical entre les lignes
        ),
        collect_geometries(
            -- Collecte une ligne de points
            with_variable(
                'y',
                @element,
                array_foreach(
                    generate_series(
                        x_min($ geometry) + 1,
                        x_max($ geometry) - 1,
                        50
                    ),
                    -- Espace horizontal entre les points
                    with_variable(
                        'x',
                        @element,
                        with_variable(
                            'point',
                            make_point(@x, @y),
                            with_variable(
                                'shift',
                                raster_value('dem', 1, @point) * 2,
                                translate(@point, 0, @shift)
                            )
                        )
                    )
                )
            )
        )
    )
)
```

Pour trouver la valeur du MNT, nous utilisons la fonction `raster_value` qui permet de croiser un point avec un raster.

```sql
raster_value('dem', 1, @point)
```

Nous exagérons la hauteur au point, en la doublant, comme ceci :

```sql
raster_value('dem', 1, @point) * 2
```

Pour déplacer le point en fonction de l'altitude au point, nous utilisons la fonction translate

```sql
translate(
    @point,
    0, -- Pas de translation en X
    raster_value('dem', 1, @point)*2
)
```

Si aucune valeur n'est trouvée sur un point, alors aucune géométrie ne sera retournée. On a dû affecter un petit offset aux X pour que les points croisent correctement le MNT.

```sql
generate_series(
    x_min($geometry) + 1, -- offset de 1 m
    x_max($geometry) - 1,
    50
)
```

Enfin, nous construisons une ligne qui relie chaque point qui a été déplacé.

Le rendu sera le suivant :

![Rendu basique](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/joy.jpeg "Rendu basique"){: loading=lazy .img-center }

![St Patricks Day Rainbow GIF](https://media.giphy.com/media/3o84U6421OOWegpQhq/giphy.gif "St Patricks Day Rainbow GIF"){: loading=lazy }
{: align=middle }

Si vous êtes un puriste de l'album, vous pouvez choisir de n'afficher que 100 lignes, comme les 100 impulsions du pulsar, et de conserver les proportions du graphique au maximum en augmentant la marge (ou l'offset) sur les bords droit et gauche (soit en X) :

![Rendu puriste](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/joy-puriste.jpeg "Rendu puriste"){: loading=lazy .img-center }

Voici le code associé :

```sql
smooth(
    collect_geometries(
        array_foreach(
            generate_series(
                y_min($ geometry) + 200,
                y_max($ geometry) - 200,
                (bounds_height($ geometry) - 400) / 100
            ),
            with_variable(
                'y',
                @element,
                make_line(
                    array_foreach(
                        generate_series(
                            x_min($ geometry) + 4000,
                            -- offset de 1 m
                            x_max($ geometry) - 4000,
                            50
                        ),
                        -- Un point tous les 50 m
                        with_variable(
                            'x',
                            @element,
                            with_variable(
                                'point',
                                make_point(@x, @y),
                                with_variable(
                                    'shift',
                                    raster_value('dem', 1, @point) * 2,
                                    translate(
                                        @point,
                                        0,
                                        -- Pas de translation en X
                                        @shift
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
    ),
    1000 -- Valeur de lissage pour les lignes
)
```

Pour créer une ligne depuis les points ou noeuds déplacés, on utilise la fonction `make_line`

```sql
make_line([point1, point2, point3, ...])
```

Pour avoir cent lignes, comme les 100 impulsions du pulsar, on utilise l'expression :

```sql
generate_series(
    y_min($geometry) + 200,
    y_max($geometry) - 200,
    (bounds_height($geometry) - 400) / 100
)
```

Enfin, nous avons ajouté un petit smoothing aux lignes pour un rendu plus doux.

```sql
smooth(..., 1000)
```

Voilà, le tutoriel est fini. On voit qu'il y a pas mal de choses intéressantes et possibles à faire en utilisant seulement les geometry generators. Après le design génératif, voici venue l'ère de la carto générative.

A vous de jouer !

![Dance Dancing GIF](https://media.giphy.com/media/U8RXSRKv8uMPS/giphy.gif "Dance Dancing GIF"){: loading=lazy }
{: align=middle }

![Mon T-Shirt Joy Division](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/joy-photo.jpeg "Mon T-Shirt Joy Division"){: loading=lazy .img-center }

Pas mal de variations sont possibles sur la base de ces lignes. Voici une petite variation avec Blender accomplie par Steven Kay :

<blockquote class="twitter-tweet tw-align-center" data-lang="fr" data-dnt="true"><p lang="en" dir="ltr">Manicougan Crater, ridgeplot syle. SRTM DEM, Blender. <a href="https://t.co/KGZQh7j57p">pic.twitter.com/KGZQh7j57p</a></p>&mdash; Steven Kay (@stevefaeembra) <a href="https://twitter.com/stevefaeembra/status/1543318675230543874?ref_src=twsrc%5Etfw">2 juillet 2022</a></blockquote>

----

## Petit livret de cuisine

Pour résumer, voici les ingrédients utilisés pour cette carte :

- `Raster > Extraction > Découper un raster selon une emprise`
- `Vecteur > Outils de recherche > Extraire l'emprise de la couche`

Les fonctions :

- `array_foreach`
- `bounds_height`
- `collect_geometries`
- `generate_series`
- `make_line`
- `make_point`
- `raster_value`
- `smooth`
- `translate`

## Crédits

- [Carte de l'Islande par Brian Suda](https://www.flickr.com/photos/suda/5384299394)
- [Courbe de réponse fréquentielle par Dominic Alves](https://www.flickr.com/photos/dominicspics/27777314569)
- [Image originale ayant inspiré la couverture de l'album](https://cococubed.com/images/unknown_pleasures/craft_fig537.jpg)

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
