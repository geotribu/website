---
title: "Réaliser une carte comme la couverture de l'album Unknow Pleasures de Joy Division"
authors:
    - Mathieu RAJERISON
categories:
    - article
date: "2022-07-02 20:00"
description: "Comment faire des cartes à la mode de Joy Division avec les générateurs de géométrie de QGIS"
image: ![](images/joy-puriste.jpeg)
license: default
tags:
    - QGIS
    - Geometry Generators
    - Generative Design
    - Cartography
    - Post-Punk
---

# Réaliser une carte comme la couverture de l'album Unknow Pleasures de Joy Division

:calendar: Date de publication initiale : 2 Juillet 2022

## Introduction
Dans cet article, nous allons voir comment créer une carte Post-punk à la mode Joy Division en utilisant les générateurs de géométrie de QGIS.

![joy division cover](https://upload.wikimedia.org/wikipedia/commons/5/5f/Radio_joy_division.jpg "joy division cover"){: loading=lazy .img-center }

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Joy Division, Joy Maps et Joy Plots
La couverture, iconique, de l'album Unkown Pleasures du groupe Joy Division, inspire bon nombre de cartographes.

Voici par exemple une carte de l'Islande :

![carte de l'islande](https://www.flickr.com/photos/suda/5384299394 "carte de l'islande"){: loading=lazy .img-center }

Dans le monde de la dataviz, on nomme ce type de rendu des [ridgelines](https://www.data-to-viz.com/graph/ridgeline.html).

![ridgeline plots](https://www.data-to-viz.com/graph/ridgeline_files/figure-html/unnamed-chunk-1-1.png "ridgeline plots"){: loading=lazy .img-center }

L'album [Unknow Pleasures](https://fr.wikipedia.org/wiki/Unknown_Pleasures) est paru en 1979. Sa couverture est assez bien ancrée dans l'époque des années 80 avec un air assez pixel art, rétro-futuriste. Elle rappelle un peu les écrans de contrôle dans Star Trek ou Star Wars, ou l'esthétique du film Tron.

<iframe src="https://giphy.com/embed/3x4GWhk9YWu2HHZESO" width="480" height="378" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/justin-80s-1980s-eighties-3x4GWhk9YWu2HHZESO">via GIPHY</a></p>

Quand on regarde la couverture, tous les férus de carto y voient des courbes de niveau, ou un paysage. Personnellement, ça me fait penser à [la vidéo promotionnelle du logiciel GRASS (1987)](https://youtu.be/cZia3ShzTWM?t=558).

[![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/grass.png){: loading=lazy .img-center }](https://youtu.be/cZia3ShzTWM?t=558)

La couverture est en réalité la reproduction d'une image intitulée "100 consecutive pulses from the pulsar CP 1919" qui représente les émissions radio du tout premier pulsar découvert en 1967. Chaque ligne représente une impulsion. C'était donc déjà une dataviz.

Voici ce que dit [Wikipedia](https://en.wikipedia.org/wiki/Unknown_Pleasures#Artwork_and_packaging) de cette image :
> The image was originally created by radio astronomer Harold Craft at the Arecibo Observatory for his 1970 doctoral dissertation as a way to visualize smaller pulses within larger ones, which might help explain what had been causing the pulses. He was unaware for years that the image was associated with the album cover until a friend told him; afterwards he bought a copy because he felt he should have one as the creator of the image.

Voici d'ailleurs à quoi ressemble l'image originale :

![image originale des impulsions](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/cp1919.jpg "image originale des impulsions"){: loading=lazy .img-center }

Cette image n'est pas sans rappeler la musique, notamment les courbes de réponse fréquentielle dans les basses, médiums et aigus qui servent à égaliser la musique

![courbe de réponse fréquentielle](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/yamaha-sound-analyser.jpg "courbe de réponse fréquentielle"){: loading=lazy .img-center }

## Téléchargement du MNT
Je ferai la carte Joy Division de la Montagne Sainte-Victoire. Cette montagne qui domine Aix-en-Provence où j'habite a été souvent peinte par Cézanne.

![La Sainte Victoire peinte par Cézanne](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/La_Montagne_Sainte-Victoire_de_P._C%C3%A9zanne_%28Fondation_Vuitton%2C_Paris%29_%2833539038628%29.jpg/640px-La_Montagne_Sainte-Victoire_de_P._C%C3%A9zanne_%28Fondation_Vuitton%2C_Paris%29_%2833539038628%29.jpg "La Sainte Victoire par Cézanne"){: loading=lazy .img-center }

Le MNT BDALTI de l'IGN à une résolution de 25 mètres sera suffisant pour notre carte.

Téléchargez le MNT sur votre département (j'avoue que j'ai un faible pour le site de Christian Quest). Pour moi, c'est https://data.cquest.org/ign/bdalti/BDALTIV2_2-0_25M_ASC_LAMB93-IGN69_D013_2019-10-01.7z

## Découpage du MNT selon votre zone
Localisez-vous sur votre zone grâce à l'outil de localisation (plugin [French Locator Filter](https://plugins.qgis.org/plugins/french_locator_filter/))

![Localisation d'Aix](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/aix.png "Localisation d'Aix"){: loading=lazy .img-center }

Découpez le MNT selon votre zone de référence en choisissant le mode dessin :

![Découpe avec QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/decoupe.png "Découpe avec QGIS"){: loading=lazy .img-center }

Vous obtiendrez alors :

![MNT découpé](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/0-dem.jpeg "MNT découpé"){: loading=lazy .img-center }

La voici, ma chère montagne !

## Création de la couche d'emprise
Ensuite, créez une couche selon l'étendue de votre MNT.

Allez sur 'Extraire l'emprise de la couche' :

![Extraction de l'emprise](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/couche.png "Extraction de l'emprise"){: loading=lazy .img-center }

Puis, extrayez l'emprise de votre modèle numérique de terrain.

![Extraire l'emprise](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/extraire.png "Extraire l'emprise"){: loading=lazy .img-center }

Voici l'emprise :

![Emprise](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/1-Carre.jpeg "Emprise"){: loading=lazy .img-center }

## QGIS, générateur de joie
Allez dans les `Propriétés` de la couche Emprise, dans `Style`, et choisissez `Générateur de géométrie`, et dans un premier temps, le rendu Ligne. Nous allons enfin pouvoir faire joujou !

![Générateur de géométries](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/rendu-ligne.png "Générateur de géométries"){: loading=lazy .img-center }

Nous allons procéder pas à pas afin de comprendre les différentes fonctions.

Nous allons créer des lignes horizontales :

![Rendu en lignes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/2-lines.jpeg "Rendu en lignes"){: loading=lazy .img-center }

Pour ce faire, il faut utiliser le code suivant :

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

Ce dernier génère une séries de coordonnées Y

	generate_series(
		y_min($geometry),
	 	y_max($geometry),
		200 -- Espace vertical entre les lignes
	)

Et crée une ligne entre le X min et le X max de l'étendue pour chaque Y

	make_line(
		make_point(x_min($geometry), @y),
		make_point(x_max($geometry), @y)
	)

Ensuite, nous densifions les lignes avec des points, ce qui laisse apparaître une grille de points. Ces points constitueront plus tard les noeuds de nos lignes.

![Rendu en points](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/3-points.jpeg "Rendu en points"){: loading=lazy .img-center }

Voici le code associé.

	collect_geometries( -- Collecte toutes les lignes de points
		array_foreach(
			generate_series(
				y_min($geometry),
				y_max($geometry),
				200 -- Espace vertical entre les lignes
			),
			collect_geometries( -- Collecte une ligne de points
				with_variable(
					'y',
					@element,
					array_foreach(
						generate_series(
							x_min($geometry),
							x_max($geometry),
							50), -- Espace horizontal entre les points
						with_variable(
							'x',
							@element,
							make_point(@x, @y))
					)
				)
			)
		)
	)


Nous utilisons `collect_geometries` deux fois :

1. une fois pour agréger les points d'une ligne
- une autre fois pour agréger toutes les lignes de points

Si nous ne mettions pas `collect_geometries` et que nous nous arrêtions seulement à `array_foreach`, nous n'obtiendrions pas de rendu graphique.

Maintenant, ce qu'il faut faire, c'est déplacer chaque point vers le haut en fonction de la valeur du MNT qui se situe en dessous et de construire une ligne qui relie chaque point qui a été déplacé.

Le rendu sera le suivant :

![Rendu basique](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/joy.jpeg "Rendu basique"){: loading=lazy .img-center }

Si vous êtes un puriste de l'album, vous pouvez choisir de n'afficher que 100 lignes, comme les 100 impulsions du pulsar, et de conserver les proportions du graphique au maximum en augmentant la marge (ou l'offset) sur les bords droit et gauche (soit en X) :

![Rendu puriste](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-07-02-qgis-joy-division/joy-puriste.jpeg "Rendu puriste"){: loading=lazy .img-center }

Voici le code associé à ce rendu :

	smooth(
		collect_geometries(
			array_foreach(
				generate_series(
					y_min($geometry) + 200,
					y_max($geometry) - 200,
					(bounds_height($geometry) - 400) / 100
				),

				with_variable(
					'y',
					@element,

					make_line(
						array_foreach(
							generate_series(
								x_min($geometry) + 1, -- offset de 1 m
								x_max($geometry) - 1,
								50), -- Un point tous les 50 m
								with_variable(
									'x',
									@element,

									with_variable(
										'point',
										make_point(@x, @y),
										translate(
											@point,
											0, -- Pas de translation en X
											raster_value('dem', 1, @point)*2 -- On déplace le point vers le haut en fonction de l'altitude au point multipliée par deux
									)
								)
							)
						)
					)
				)
			)
		),
		200 -- Valeur de lissage pour les lignes
	)

Pour trouver la valeur du MNT, nous utilisons la fonction `raster_value` qui permet de croiser un point avec un raster.

	raster_value('dem', 1, @point)

Nous exagérons la hauteur au point, en la doublant, comme ceci :

	raster_value('dem', 1, @point) * 2

Pour déplacer le point en fonction de l'altitude au point, nous utilisons la fonction translate

	translate(
		@point,
		0, -- Pas de translation en X
		raster_value('dem', 1, @point)*2
	)

Pour avoir cent lignes, comme les 100 impulsions du pulsar, on utilise l'expression :

	generate_series(
		y_min($geometry) + 200,
		y_max($geometry) - 200,
		(bounds_height($geometry) - 400) / 100
	)

Si aucune valeur n'est trouvée sur un point, alors aucune géométrie ne sera retournée. On a dû affecter un petit offset aux X pour que les points croisent correctement le MNT.

	generate_series(
		x_min($geometry) + 1, -- offset de 1 m
		x_max($geometry) - 1,
		50
	)

Nous avons ajouté un petit smoothing aux lignes pour un rendu plus doux.

	smooth(..., 200)

Voilà, le tutoriel est fini. On voit qu'il y a pas mal de choses intéressantes et possibles à faire en utilisant seulement les geometry generators. Après le design génératif, voici venue l'ère de la carto générative.

A vous de jouer !

<iframe src="https://giphy.com/embed/U8RXSRKv8uMPS" width="480" height="360" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/dancing-dance-wtf-U8RXSRKv8uMPS">via GIPHY</a></p>


Pas mal de variations sont possibles sur la base de ces lignes. Voici une petite variation avec Blender accomplie par Steven Kay :

https://twitter.com/stevefaeembra/status/1543318675230543874/photo/1

## Crédits
- Carte de l'Islande par Brian Suda : https://www.flickr.com/photos/suda/5384299394
- Courbe de réponse fréquentielle par Dominic Alves : https://www.flickr.com/photos/dominicspics/27777314569
- Image originale ayant inspiré la couverture de l'album : https://cococubed.com/images/unknown_pleasures/craft_fig537.jpg

----

## Auteur {: data-search-exclude }

--8<-- "content/team/mraj.md"

{% include "licenses/default.md" %}
