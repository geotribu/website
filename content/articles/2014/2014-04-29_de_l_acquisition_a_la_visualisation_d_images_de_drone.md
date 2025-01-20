---
title: "De l'acquisition à la visualisation d'images prises à partir d'un drone"
authors:
    - Arnaud VANDECASTEELE
categories:
    - article
comments: true
date: 2014-04-29
description: "De l'acquisition à la visualisation d'images prises à partir d'un drone"
tags:
    - drone
    - images aériennes
---

# De l'acquisition à la visualisation d'images prises à partir d'un drone

:calendar: Date de publication initiale : 29 avril 2014

Il m'arrive régulièrement de tomber sur des innovations qui auraient le potentiel de changer considérablement nos habitudes métiers. L'une des plus récentes, et pour laquelle je me suis pris de passion, est celle des drones. Contrairement à ce qui se fait majoritairement, mon objectif n'est pas d'utiliser ces vecteurs aériens pour faire de l'événementiel, mais pour acquérir des images aériennes géoréférencées exploitables au sein d'une interface cartographique (logiciel SIG, interface web, etc.).

 Je vous livre ici le résultat d'une expérimentation réalisée en collaboration avec [Drones Adventures](http://www.droneadventures.org/) sur la région de Fukushima ainsi que différentes autres études de cas. Le logiciel [Pix4Dmapper](http://pix4d.com/products/) produit par la société [Pix4D](http://pix4d.com/) a été utilisé pour réaliser le traitement des images obtenues à l'aide d'un drone [eBee](https://www.sensefly.com/drones/ebee.html) de la société [SenseFly](https://www.sensefly.com/).

----

Avant de commencer notre tour d'horizon, je vous propose de consulter [le billet](http://www.droneadventures.org/2014/04/02/fukushima-a-drones-eye-view/) sur le même sujet paru sur le site de [Drones Adventures](http://www.droneadventures.org/) qui retrace l'origine de cette collaboration et surtout les implications de ce projet. Très rapidement, l'association Drones Adventures intervient dans des régions sinistrées afin de proposer un système de cartographie d'urgence réalisé à l'aide de drones. Une récente mission a amené l'équipe de [Drones Adventures](http://www.droneadventures.org/) à poser leurs bagages (ou plutôt les ailes de leur eBee) à Fukushima afin d'obtenir une carte permettant une meilleure estimation des dégâts et surtout de la reconstruction 3 ans après le tsunami.

En collaboration avec Adam Klaptocz, coordinateur du projet, nous avons eu l'occasion d'effectuer le traitement des images obtenues pour la région de Tomioka. Ce traitement servira d'exemple pour illustrer les différentes phases nécessaires pour obtenir une image géoréférencée utilisable dans votre SIG.

<iframe title="vimeo-player" src="https://player.vimeo.com/video/90951639?h=f64aa47ed2" width="100%" height="360" frameborder="0" allowfullscreen></iframe>

## Côté équipement

Fan d'Open Source ? Vous serez malheureusement déçu. En effet, il n'existe à l'heure actuelle aucune réelle solution permettant de rivaliser en terme d'interface ou de résultats avec les deux principaux logiciels propriétaires du domaine que sont [Pix4Dmapper](http://pix4d.com/products/) et [PhotoScan](http://www.agisoft.ru/products/photoscan). Quelques projets sont néanmoins à souligner, tel que le logiciel [Mic Mac](http://logiciels.ign.fr/?-Micmac,3-) développé par l'IGN ou encore le Web Service [Drone Mapper](http://dronemapper.com/). La suite de ce billet portera sur [Pix4Dmapper](http://pix4d.com/products/) qui a été utilisé pour réaliser les différents traitements.

## Présentation de Pix4Dmapper

Développé par [Pix4D](http://pix4d.com/), le logiciel [Pix4Dmapper](http://pix4d.com/products/) permet la création d'orthoimages géoréférencées et de MNT obtenus à partir d'un vecteur aérien (drones, avions, etc.). En plus de cela, il possède des fonctionnalités particulièrement intéressantes comme la sélection d'images pour la mosaïque permettant par exemple d'éliminer les objets en mouvement, la mesure de surfaces et de volumes à l'aide du [rayCloud Editor](http://pix4d.com/raycloud/) ou encore l'export dans différents formats (GeoTiff, Google Tiles, LAS, XYZ, etc.). Si vous êtes intéressés par le fonctionnement de ce logiciel, sachez que simplement en vous [enregistrant sur leur site](https://mapper.pix4d.com/mapper/trial/1/) vous pouvez disposer d'une version d'évaluation ainsi que de différents jeux de données.

## Traitement des images dans Pix4Dmapper

D'une manière simplifiée, les phases nécessaires au traitement d'images obtenues à partir d'un drone sont au nombre de trois. La première consiste à aligner les différentes images entre elles, la seconde à en extraire les informations pertinentes sous la forme d'un nuage de points ou d'un maillage et enfin vient l'étape de reconstruction et d'export du GeoTiff ou du MNT. Détaillons chacune d'entre elles.

### Alignement d'images

Contrairement aux techniques d'acquisition classiques par capteurs sophistiqués, les drones utilisent pour la plupart les mêmes appareils photo que vous pouvez trouver dans le commerce. L'altitude de vol et l'angle de prise de vues nécessitent l'acquisition de plusieurs images se chevauchant afin de couvrir une zone.

![Acquisition d'images](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/superposition-vol-uav.jpg "Acquisition d'images"){: .img-center loading=lazy }

Il sera alors nécessaire d'aligner (ou autrement dit de fusionner) ces différentes prises de vue afin d'obtenir une seule image continue. Pour cela, différentes techniques existent, mais globalement l'idée est de rechercher les entités correspondantes (keypoints) entre les différentes photos afin de construire l'image finale. Le code couleur utilisé permet de rapidement identifier les images dont l'alignement n'a pu être réalisé pour cause de mauvaise calibration du capteur ou de mauvais paramétrage de la mission:

- Le rond bleu correspond à la position initiale de l'image obtenue à partir des coordonnées GPS initiales
- Le rond vert est la position optimisée de l'image calculée par Pix4D Mapper prenant en compte le système de coordonnées géographiques de référence des points de calage
- Un rond rouge correspond à une caméra non calibrée et elle ne peut donc être utilisée

L'image ci-dessous présente le résultat de cette opération et comme vous pouvez le constater, un grand nombre d'images n'ont pu être alignées du fait d'une erreur de paramétrage lors de la mission. Ce n'est pas le but de ce billet, mais sachez que la nouvelle version de Pix4D permet de spécifier manuellement des points de correspondance afin d'améliorer le résultat final.

![Alignement d'images](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/alignement-images.png "Alignement d'images"){: .img-center loading=lazy }

### Génération du nuage de points

Une fois les images correctement calibrées, il est possible d'en extraire des points contenant différentes informations comme notamment la couleur de celui-ci, mais aussi sa position en 3 dimensions (X,Y et Z) grâce à la stéréoscopie. Ce processus va alors générer un ensemble de ces points plus communément appelé "nuage de points". Ce sont ces derniers qui seront utilisés lors de la création de l'ortophographie et du MNT.

L'image ci-dessous présente la sélection d'un des points dans le nuage de points. Ce point est relié visuellement aux images correspondantes par les différents traits rouges.

![Nuage de points](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/point_cloud.png "Nuage de points"){: .img-center loading=lazy }

### Export du résultat

Nous arrivons au bout de ce processus et c'est certainement celui qui vous intéresse le plus ! Aucune difficulté technique à cette étape, il vous suffit de spécifier le format d'export désiré et au bout de quelques minutes vous obtenez le fichier désiré. Plusieurs options sont disponibles comme notamment un classique fichier GeoTiff ou un MNT mais aussi la génération de tuiles à "la Google" pour une diffusion web.

Il ne vous reste plus qu'à importer le résultat dans votre SIG favoris. Ci-dessous, l'image de Tomioka a été importée dans QGIS.

![QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/qgis.png "QGIS"){: .img-center loading=lazy }

Comme je le mentionnais, il est également possible d'exporter ce résultat sous la forme de tuiles afin de créer une application cartographique sur internet. L'exemple ci-dessous est le résultat de cet export.

### Les petits (gros) plus de Pix4D Mapper

Si vous êtes dans le domaine, vous me direz que les fonctionnalités précédemment présentées ne sont pas différentes de celles que l'on retrouve dans les autres logiciels similaires tels que [PhotoScan](http://www.agisoft.ru/products/photoscan). Sur ce point vous aurez tout à fait raison. Mais (oui y'a toujours un mais), [Pix4Dmapper](http://pix4d.com/products/) possède d'autres options qui font sa particularité. Si les deux premières sont assez courantes, les deux dernières sont spécifiques à [Pix4Dmapper](http://pix4d.com/products/) ce qui lui donne son caractère unique !

#### Mesure de distances, surface volumes

Imaginez que vous ayez réalisé la prise de vue d'une carrière, à partir du nuage de points, il vous sera alors possible de calculer la volumétrie d'un monticule de pierres, communément appellé "stockpile" dans le domaine. Pour cela, rien de plus simple, vous dessinez sur l'interface 3D la zone désirée et une fois la précision améliorée en remplaçant vos points sur les images de référence 2D, la volumétrie est calculée automatiquement.

![Mesure de volumétrie](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/calcul-volumetrie.png "Mesure de volumétrie"){: .img-center loading=lazy }

#### Export 3D

Bien que cette fonctionnalité soit disponible dans [Pix4Dmapper](http://pix4d.com/products/), celle-ci est encore en mode bêta contrairement à [PhotoScan](http://www.agisoft.ru/products/photoscan) qui la propose depuis longtemps. Bien qu'intéressante pour certaines applications, celle-ci est moins importante dans notre domaine car cet export s'accompagne d'une perte de la composante spatiale. En résultat vous aurez une belle représentation 3D mais celle-ci restera simplement visuelle. Différents formats de sortie sont supportés vous permettant de visualiser cet export dans des logiciels comme [Meshlab](http://meshlab.sourceforge.net/), [Blender](http://www.blender.org/) ou encore [Meshmixer](http://www.meshmixer.com/). A noter que [PhotoScan](http://www.agisoft.ru/products/photoscan), permet tout cela mais aussi l'export dans d'autres plateformes web populaires comme et [Stetchfab](https://sketchfab.com/) et [Verold](http://verold.com/).

#### Création d'objet 3D pour la DAO

Via l'interface de [Pix4Dmapper](http://pix4d.com/products/) vous allez pouvoir très précisément dessiner les objets contenus dans l'image (ex: un poteau électrique) afin de générer ensuite un fichier compatible avec un logiciel de DAO (ex: autodesk). Entre l'ortophoto, le modèle numérique de terrain et ces objets vectoriels 3D, vous obtenez alors une représentation fidèle de votre territoire.

#### Choix de l'image

C'est à mon sens une des fonctionnalités qui rend [Pix4Dmapper](http://pix4d.com/products/), complètement unique dans le domaine. Pour illustrer l'intérêt de celle-ci, imaginez que vous ayez pris des images au-dessus de routes. Entre les différentes prises de vue, des objets mobiles (voitures, moto, etc.) se seront déplacés. En utilisant l'éditeur de mosaïque vous pourrez alors sélectionner les images sans véhicules afin de les utiliser lors de la génération de l'ortophoto et obtenir ainsi une image sans véhicule ou autre artefact ! Bon certes ça demande un gros boulot manuel, mais faut avouer que le résultat final est irréprochable.

## En conclusion

Ainsi s'achève ce billet qui j'espère vous aura convaincu des potentialités des drones et de la maturité des technologies associées. Nous nous sommes essentiellement concentrés sur l'utilisation de [Pix4Dmapper](http://pix4d.com/products/) qui est certainement à l'heure actuelle la solution la plus aboutie et facile à prendre en main. Par souci de compréhension, nous sommes volontairement restés très général, mais sachez que [Pix4Dmapper](http://pix4d.com/products/) recèle de fonctionnalités qui n'ont pas été abordées comme le calcul de l'index de végétation (NDVI), les courbes de niveau ou encore la définition de masques au sein des images. Cela fera certainement l'objet d'un prochain billet !

----

<!-- geotribu:authors-block -->
