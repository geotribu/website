---
title: "Tutoriel de prise en main du logiciel de rendu 3D Aerialod"
authors: "Aurélien Chaumet"
categories: ["article", "tutoriel","3D"]
date: "2020-09-23 10:20"
description: "Concepts de base et exemples de paramétrage et de rendu sur aerialod"
image : "https://cdn.geotribu.fr/img/tuto/aerialod/oceania_aerialod.jpg"
tags: "carte3D,aerialod,rendu3D"
---

# Aerialod, un logiciel libre, léger et puissant de rendu de cartes 3D

:calendar: Date de publication initiale : 13 octobre 2020

**Mots-clés :** Aerialod | Cartes3D

[![oceania forest](https://cdn.geotribu.fr/img/tuto/aerialod/oceania_aerialod.jpg "exemple aerialod Oceania foret"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/oceania_aerialod.jpg){: data-mediabox="oceania forest" data-title="Couverture forestière d'une partie de l'Océanie" }

## Pourquoi utiliser un nouvel outil ?

Lorsqu'on parle de cartographie 3D, des choses arrivent pèle mêle en tête.

Un peu de technique, comme la technologie Lidar et sa capacité à générer des modèles numériques de terrain (MNT). GoogleMaps ou bien Maps d'Apple qui génèrent des vues 3D à partir de photo aériennes.
Côté logiciel, QGIS, avec le plug-in QGIS2threeJS qui permet depuis un moment de réaliser des blocs 3D et [maintenant nativement dans sa version 3](https://www.qgis.org/fr/site/forusers/visualchangelog30/index.html#d-features). Ou bien encore [Blender](https://www.blender.org/download/), qui est un logiciel libre de modélisation, d'animation et de rendu 3D. Et pêle-mêle [ArcGIS](https://www.esrifrance.fr/arcgis.aspx), [MapBox](https://www.mapbox.com/) ou [Kepler.gl](https://kepler.gl/) pour ne citer qu'eux.

Des noms et leurs créations viennent également :

- Sean Conway réalise des cartes visuellement impressionnantes. Il travail pour Quantum Spatial aux Etats-Unis, en tant que spécialiste orthophoto. Et au vu de ses créations, il a clairement un sacré sens artistique ! Il utilise notamment QGIS et Blender pour ses rendus. Vous pouvez admirer son travail [sur son profil Twitter](https://twitter.com/geo_spatialist?s=20).

[![france geologique](https://cdn.geotribu.fr/img/tuto/aerialod/sean_conway.png "Carte géologique France 3D"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/sean_conway.png){: data-mediabox="france géologique" data-title="Carte Géologique de la France, à l'échelle du millionième, Exécutée en utilisant les documents publiés par le Service de la Carte géologique détaillée de la France - Ministère des Travaux Publics - 1905" }

- [Alasdair Rae](https://twitter.com/undertheraedar?s=09), anciennement Professeur  des étude urbaines et de la planification et qui a fondé récemment [Automatic Knowledge](https://automaticknowledge.co.uk/), a notamment produit des cartes 3D avec la densité de population comme donnée entrante par exemple

[![population mondiale](https://cdn.geotribu.fr/img/tuto/aerialod/alasdair_rae.png "Population mondiale pics Alasdair Rae"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/sean_conway.png){: data-mediabox="population mondiale" data-title="Densité de population mondiale" }

Il utilise le logiciel libre Aerialod, développé par [ephtracy](https://twitter.com/ephtracy?s=09), plus connu pour être le créateur de MagicaVoxel, logiciel de création de voxels (pixels 3D) libre et léger.

----

Ce sont les créations d'Alasdair Rae qui m'ont vraiment donné envie de tester Aerialod, notamment [grâce à ses tutoriels](http://www.statsmapsnpix.com/2020/03/making-3d-landscape-and-city-models.html?m=1).

Le principe général du logiciel est d'afficher une extrusion s'appuyant sur la valeur des pixels d'une image. On peut naturellement utiliser un MNT pour réaliser cela, mais tout fichier raster peut être utilisé en théorie.

A la demande générale 🥁 (surtout celle de Julien Moura...), cet article a pour but d'expliquer en quoi ce "petit" logiciel est puissant et très simple d'utilisation, grâce à un côté hyper ludique. On peut rapidement passer du temps à jouer avec des angles de caméra, des couleurs, des ouvertures, des zooms et des rendus différents. Je ne prétends pas en être spécialiste, et ne pourrait donc pas apporter des détails poussés sur chaque fonctionnalité.
En revanche, cet article vous donnera une entrée en matière consistante, permettant de comprendre les principes de fonctionnement généraux de l'application. En espérant que cela vous inspire, et qu'il vous donnera envie, j'en suis sûr, de créer de beaux visuels !

[![oleron 3D](https://cdn.geotribu.fr/img/tuto/aerialod/oleron_v2.png "Oleron 3D render"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/oleron_v2.png){: data-mediabox="oleron 3D" data-title="Oleron 3D render" }

----

## Installation du logiciel

Afin d'installer Aerialod, vous devez [vous rendre sur le site d'ephtracy](https://ephtracy.github.io/index.html?page=aerialod) et téléchargez la version (Windows uniquement pour le moment) qui correspond à votre système.

Et puis c'est tout en fait !

Dézippez l'archive téléchargée, et vous trouverez directement à l'intérieur un exécutable se nommant Aerialod. Cliquez et c'est parti vers l'infini et l'au-delà 🚀 !!!

----

## Présentation de l'interface

A "petit" logiciel (30 Mo une fois dézippé...), interface hyper simple !

Elle se décompose en 3 parties : Le panneau de gauche gère les options principalement autour de la lumière, le panneau de droite gère plutôt le rendu caméra et le panneau central affiche le résultat.

[![interface ouverture](https://cdn.geotribu.fr/img/tuto/aerialod/interface_aerialod.png "Interface ouverture"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/interface_aerialod.png){: data-mediabox="interface ouverture" data-title="Interface ouverture" }

### Panneau de gauche

[![panneau de gauche](https://cdn.geotribu.fr/img/tuto/aerialod/fenetre_gauche_1bis.jpg "Panneau gauche"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/fenetre_gauche_1bis.jpg){: data-mediabox="panneau gauche" data-title="Panneau de gauche" }

### Panneau du centre

La partie centrale, en plus d'afficher le rendu, permet d'afficher le nom des options en bas et le paramétrage de la caméra : vue personnelle, freestyle, orthogonale ou isométrique.

[![panneau central](https://cdn.geotribu.fr/img/tuto/aerialod/fenetre_centre.png "Panneau central"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/fenetre_centre.png){: data-mediabox="panneau central" data-title="Panneau central" }

### Panneau de droite

[![panneau de droite](https://cdn.geotribu.fr/img/tuto/aerialod/fenetre_droite.jpg "Panneau de droite"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/fenetre_droite.jpg){: data-mediabox="panneau droite" data-title="Panneau de droite" }

Une dernière partie encore non évoquée se trouve en haut à droite du logiciel avec 4 boutons.

![boutons de droite](https://cdn.geotribu.fr/img/tuto/aerialod/boutons_droite.png "Boutons de droite"){: width=100px loading=lazy }

- Contrairement à ce que pourrait laisser penser le premier bouton, impossible pour l'instant d'enregistrer un projet Aerialod, il sert uniquement à enregistrer l'image de base en png
- Le 2ème en revanche est plus évocateur et permet d'afficher une image
- Le 3ème (stitch map) permet de charger un ensemble d'images, pratique !
- Et le 4ème permet de repartir d'une feuille blanche

Si tout ça n'est pour l'instant pas très clair, pas d'inquiétude, ça vient très vite avec la pratique !

Dans la suite de cet article, lorsque nous parlerons d'une fonctionnalité particulière, il sera indiqué *le nom* qui s'affiche au survol de la souris, en bas du panneau principal.
De plus, chaque capture d'écran affichera également les paramètres appliqués, afin que vous puissiez suivre et reproduire les manipulations.

[![nom fonction](https://cdn.geotribu.fr/img/tuto/aerialod/nom_fonction.png "Nom fonction"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/nom_fonction.png){: data-mediabox="nom fonction" data-title="Nom fonction" }

!!! check "Où trouver des données ?"
    Il est possible de trouver un certain nombre de MNT en open data sur internet, notamment sur [data.gouv.fr](https://www.data.gouv.fr/fr/search/?q=mnt) pour le territoire français.

## Prise en main

Ceci étant dit, allons-y avec notre première image importée dans Aerialod.
Le logiciel peut lire plusieurs types de fichiers (png, jpg, tif, dtm, asc). A ce jour, je n'ai testé que du tif, car c'est généralement dans ce genre de format, que les MNT sont enregistrés.

!!! warning "Taille des fichiers importés"
    Attention à la taille du fichier que vous souhaitez lire. Le logiciel ne permet pas de lire de très gros tif, avec des résolutions importantes.

Pour l'exercice, nous utiliserons le [MNT LIDAR de Bora Bora 🤤](https://www.data.gouv.fr/fr/datasets/r/92216da9-64a1-4522-8858-7e2537cab60d).

Pour l'afficher, vous pouvez l'ouvrir en cliquant sur le bouton en haut à droite *Open map* ou bien plus simplement en faisant un glisser-déposer depuis un explorateur.

Aerialod l'ouvre alors (s'il n'est pas trop gros).

[![import aerialod](https://cdn.geotribu.fr/img/tuto/aerialod/import.png "Import aerialod"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/import.png){: data-mediabox="import aerialod" data-title="Import aerialod" }

Quelques éléments de base pour la manipulation du rendu :

- Le clic molette de la souris + déplacement permet de bouger la carte
- Le clic droit de la souris + déplacement permet de changer l'angle de vue
- La molette de la souris zoome/dézoome par rapport au centre du panneau central

Avec ça, vous pouvez facilement gérer le déplacement de la caméra sur votre carte.

A noter que chaque modification d'un paramètre (fenêtre gauche ou droite, ou déplacement sur la carte) imposera un temps de chargement (assez rapide), afin que le logiciel recalcule le rendu. Cela rend le logiciel très réactif, car à chaque modification, vous verrez quasi-instantanément le résultat !

Dans un premier temps, vous pouvez modifier la couleur du terrain sur la fenêtre de droite *Base color*, ainsi que celle du terrain, dans la fenêtre de gauche *Ground color*.

Il est ensuite possible de jouer sur la hauteur de rendu des pixels grâce à l'option *Scale* (panneau de droite), afin d'exagérer un peu le relief. Cela peu donner quelque chose comme ça :

[![couleurs](https://cdn.geotribu.fr/img/tuto/aerialod/couleurs.png "Modification des couleurs"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/couleurs.png){: data-mediabox="couleurs" data-title="Modification des couleurs" }

Nous avons déjà une première idée (exagérée certes, mais c'est quand même beau comme ça 😎) du relief de Bora Bora.

On peut maintenant jouer sur les angles du soleil pour avoir un premier rendu différent, dans la fenêtre de gauche *Pitch Angle of Sun Light* / *Yaw Angle of Sun Light*.

[![scale](https://cdn.geotribu.fr/img/tuto/aerialod/scale.png "Scale"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/scale.png){: data-mediabox="scale" data-title="Scale" }

Il est possible de changer le mode de vue grâce au bouton en bas à droite du panneau central, pour avoir une idée de l'horizon, en passant par exemple sur la *Perspective camera*.

Si nous souhaitons nous rapprocher un peu de la "réalité", il faudrait que le niveau d'eau soit plus haut, car nous pouvons observer que le lidar a pris des mesures sous l'eau à l'intérieur du lagon. Même si cela est également intéressant ! On peut notamment observer des structures relativement organisées à certains endroits.

!!! question "GeoQuizz"
    Si un lecteur peut nous renseigner sur la nature de ces reliefs sous marins, il gagnera notre gratitude éternelle 😉.

Pour cela, il suffit de modifier l'*Offset* dans le panneau de droite.

[![relief sous marins](https://cdn.geotribu.fr/img/tuto/aerialod/reliefs_sous_marins.png "Reliefs sous-marins"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/reliefs_sous_marins.png){: data-mediabox="reliefs sous marins" data-title="Reliefs sous-marins" }

Bien, fini de jouer ! Diminuons l'*Offset* pour relever le niveau de la mer.

Etant donné que je connais très bien Bora-Bora 😂 (merci Google Maps...), "-77" apparait comme une valeur d'*Offset* pertinente pour cette représentation.

[![offset](https://cdn.geotribu.fr/img/tuto/aerialod/offset.jpg "Réglage de l'offset"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/offset.jpg){: data-mediabox="offset" data-title="Réglage de l'offset" }

Pour rappel, en réalisant un clic-droit souris et en la bougeant vers le haut vous devriez voir l'horizon apparaitre (si vous êtes bien passés auparavant en vue *Perspective* avec le bouton en bas à droite du panneau central).

Afin de rajouter un peu de réalisme, vous pouvez choisir un autre type de ciel appelé *Atmospheric Scattering*. Cela va jouer sur la lumière ambiante et le rendu, et nous avons maintenant la possibilité de rendre visible le soleil, ce qui peut donner un effet sympa. Pour ce faire, dans le panneau de gauche, activez le bouton rond *Show Sun Disk*.

[![soleil](https://cdn.geotribu.fr/img/tuto/aerialod/sun.jpg "Hou le beau soleil !"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/sun.jpg){: data-mediabox="soleil" data-title="Hou le beau soleil !" }

Ici l'azimut du soleil est assez faible, nous permettant de l'apercevoir, tout en créant des ombres dignes d'une aube peu éclairante. 2 solutions pour y voir un peu plus clair :

- vous souhaitez garder visible le soleil et vous modifiez l'exposition (panneau de droite *Exposure*)
- vous ne voyez pas d'intérêt à garder visible directement le soleil et vous modifiez son azimut. Plus celui-ci sera proche de 90 (degrés), et plus vous imiterez un moment de la journée proche de midi donc très exposé.

[![midi](https://cdn.geotribu.fr/img/tuto/aerialod/midi.jpg "Une meilleure exposition"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/midi.jpg){: data-mediabox="midi" data-title="Une meilleure exposition" }

La modification de la valeur *Rayleigh* (panneau de gauche) permet de jouer sur la diffusion de la lumière et certains effets peuvent être intéressants. [Pour en savoir plus sur la diffusion Rayleigh, une Wikipedia-pause s'impose](https://fr.wikipedia.org/wiki/Diffusion_Rayleigh) !

La partie du panneau de gauche appelé *Sample* est un ensemble d'effet permettant plus ou moins de lisser l'image et d'avoir un rendu plus "propre". Jusque là, je les coche tous...

L'option *Grid*" (panneau de gauche) permet l'affichage d'une grille sur le terrain de base ou sur le rendu directement. Vous pouvez sélectionner l'épaisseur du trait ainsi que son espacement.

[![grid](https://cdn.geotribu.fr/img/tuto/aerialod/grid.jpg "Une bien belle grille"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/grid.jpg){: data-mediabox="grid" data-title="Une bien belle grille" }

Si on zoome un peu, on peut s'apercevoir que le rendu est très cubique. On peut l'exagérer en modifiant le *Step* et le *Lod* (panneau de droite) par exemple. Mais nous pouvons également tenté de l'aplatir en sélectionnant le rendu *Bilinear Surface Mode* (panneau de droite toujours).

[![cube](https://cdn.geotribu.fr/img/tuto/aerialod/cube.jpg "Cube"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/cube.jpg){: data-mediabox="rendu surface" data-title="Mode cube on" }

[![cube exagere](https://cdn.geotribu.fr/img/tuto/aerialod/cube_exagere.jpg "Cube exagéré"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/cube_exagere.jpg){: data-mediabox="rendu surface" data-title="Cube exagéré" }

[![mode surface](https://cdn.geotribu.fr/img/tuto/aerialod/surface_mode.png "Mode surface on"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/surface_mode.png){: data-mediabox="rendu surface" data-title="Mode surface on" }

Tout ca fait partie des multiples paramètres sur lesquels il est possible de jouer, afin d'avoir des rendus relativement différents.

Dernière chose concernant les effets, il est possible de réaliser un focus sur un élément particulier que vous souhaiteriez mettre en valeur (et donc flouter les autres) en cliquant sur cet élément.
Vous pouvez ensuite paramétrer cet effet grâce à la partie *Lens* (panneau de droite).

[![lens](https://cdn.geotribu.fr/img/tuto/aerialod/lens.jpg "Effet d'ouverture"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/lens.jpg){: data-mediabox="lens" data-title="Effet d'ouverture" }

[![panorama](https://cdn.geotribu.fr/img/tuto/aerialod/panorama.jpg "Mais quel beau panorama !"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/panorama.jpg){: data-mediabox="panorama" data-title="Mais quel beau panorama !" }

Enfin, Aerialod offre la possibilité d'exporter vos rendus grâce à la partie Image du panneau de droite. Il ne vous reste qu'à sélectionner la hauteur et la largeur souhaitées, puis cliquez sur *Render* et attendez que le logiciel fasse le reste 👌.

[![rendu bora bora](https://cdn.geotribu.fr/img/tuto/aerialod/bora_bora.png "Un exemple de rendu de Bora-Bora"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/bora_bora.png){: data-mediabox="rendu bora bora" data-title="Un exemple de rendu de Bora-Bora" }

Deux autres types de rendu un peu différent :

[![population france](https://cdn.geotribu.fr/img/tuto/aerialod/france_pop.png "Population française"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/france_pop.png){: data-mediabox="population france" data-title="Population française" }

[![forets espagne](https://cdn.geotribu.fr/img/tuto/aerialod/espagne_foret.jpg "Forêts espagnoles"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/aerialod/espagne_foret.jpg){: data-mediabox="forets espagne" data-title="Forêts espagnoles" }

----

## Conclusion

En guise de conclusion, vous trouverez ci-dessous une liste rapide des avantages et inconvénients (que j'ai pu voir jusque là) à utiliser Aerialod :

### Avantages à utiliser Aerialod

- Logiciel libre, gratuit, de petite taille (<30 Mo) et très performant pour un rendu rapide ! (déjà 4 énormes avantages en un !)
- Vraiment simple d'utilisation, après seulement quelques heures de pratique autodidacte, on peut sortir des rendus intéressants
- Hyper ludique ! On se prend très rapidement au jeu de modifier les paramètres un par un et de tester différents angles de caméra. Tout en visualisant le résultat quasiment directement

### Inconvénients à utiliser Aerialod

- Pour l'instant, il n'existe pas de version Mac, désolé pour les 🍏 addict
- Impossible d'enregistrer des projets, et donc de revenir travailler dessus par la suite (gros inconvénient...)
- Le logiciel ne lit pas les fichiers trop grands
- Impossible de draper une texture sur un relief obtenu, comme Blender le propose par exemple
- Pas de Ctrl+Z ou un quelconque retour en arrière sur un paramètre modifié, donc faites attention lorsque vous commencez à être content de votre rendu et que vous continuez à faire des modifications. Ca peut être frustrant...
- Peu d'ajouts pour l'instant sur le logiciel, espérons et croisons les doigts qu'ephtracy lise les différents commentaires des personnes utilisant Aerialod 😉

Libre à vous de faire jouer votre imagination et votre sens artistique, et n'hésitez pas à interagir dans les commentaires ou sur Twitter !!!

----

## Auteur

--8<--
content/team/jmou.md
--8<--

<!-- Hyperlinks reference -->
[Markdown]: https://fr.wikipedia.org/wiki/Markdown
[Internet Archive]: https://archive.org
[Scrapy]: https://scrapy.org/
