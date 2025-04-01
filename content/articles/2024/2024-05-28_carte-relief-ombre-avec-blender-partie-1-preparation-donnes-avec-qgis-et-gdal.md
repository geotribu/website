---
title: Réaliser des cartes avec Blender - Partie 1
subtitle: Blindé jusqu’au relief 1
authors:
  - Thomas Szczurek-Gayant
categories:
  - article
comments: true
date: 2024-05-28
description: "Réaliser des cartes de relief avec le logiciel libre 3D Blender. Partie 1 : préparer les données avec GDAL et/ou QGIS."
icon: simple/blender
image:
license: default
robots: index, follow
tags:
  - 3D
  - Blender
  - cartographie
  - GDAL
  - relief
---

# Réaliser des cartes avec Blender - Partie 1 : préparer les données avec GDAL/QGIS

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

![logo Blender](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/blender.png){: .img-thumbnail-left }

Cet article se base sur celui initialement paru en anglais sur [somethingaboutmaps](https://somethingaboutmaps.wordpress.com/2017/11/16/creating-shaded-relief-in-blender/), dont on remerciera l'auteur Daniel Huffman pour l'article initial et l'aimable autorisation d'écrire celui-ci.

Ou comment faire des cartes qui ont la classe. Grossièrement, la technique consiste à déformer un plan avec un raster d'élévation.

Je vais ici utiliser le MNT à 1 mètre issu du [RGE ALTI](https://geoservices.ign.fr/rgealti) de l'IGN sur le département des Pyrénées-Atlantiques, ce qui permettra d'avoir du relief (ce qui rend bien avec cette technique) et de la mer (sacro-sainte règle des effets de manche pour avoir la classe : mettez de la flotte).

L'article est en **deux parties**.

![logo GDAL tshirt](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/gdal_logo_tshirt.webp){: .img-right width=20% }

Pour cette première partie on ne touchera pas à Blender mais on va s'attarder sur la préparation des données.  
Il y a plusieurs étapes de préparation et l'une d'entre elles nécessite obligatoirement l'utilisation de GDAL en ligne de commande. Restez ici ! Rien de bien compliqué et on vous explique tout (et on va profiter de cet article pour essayer de faire tous les pré-traitements raster en lignes de commande pour s'y familiariser. Au cazou j'indiquerai aussi comment faire avec QGIS).

Ceci implique d'avoir accès à GDAL. Sur Windows, ça se passe en se rendant dans votre répertoire d'installation de QGIS, puis en démarrant OSGeo4W.bat. Vous pouvez plus simplement consulter cet article de Geotribu [Installer Python et GDAL sous Windows](https://geotribu.fr/articles/2013/2013-09-26_installer_python_gdal_sous_windows) ou encore celui-ci [Utiliser GDAL sous Windows avec WSL](https://geotribu.fr/articles/2020/2020-10-28_gdal_windows_subsystem_linux_wsl/#). Je considère que les linuxiens sont assez aguerris pour se débrouiller (au pire faites-vous un environnement [mamba](https://mamba.readthedocs.io/en/latest/) qui va bien (miniconda réécrit en c/c++)) et je refuse par principe de parler aux apple-iens (sauf à ma cheffe de service car je suis bien obligé).

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

<!-- more -->

----

## Préparation des données

Après récupération du jeu de données, chargez une des dalles au format ASC dans QGIS. Le format ASC ne gère pas les projections et QGIS essayera par défaut de les positionner en WGS84 (ne vous inquiétez pas, les coordonnées sont les bonnes). Vous pouvez repositionner l'image en cliquant sur la petite icône de l'image ci-dessous et en spécifiant ce bon vieux Lambert 93.

![Ça arrive même aux meilleurs](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img1_lign.png){: .img-center loading=lazy }

Sur ces considérations on chargera plutôt la couche "dalles" [dans le format dont il ne faut pas prononcer le nom](http://switchfromshapefile.org/) située dans le dossier "3_SUPPLEMENTS_LIVRAISON" de l'archive. On active ensuite un fond de plan OpenStreetMap sous "xyz tiles" de l'explorateur de QGIS histoire de se repérer.

### Liste des tuiles et bases de la ligne de commandes

On va ici créer un fichier qui nous permettra de fusionner les dalles voulues pour notre carte.

1. Dans QGIS, on sélectionne les dalles de la région (rectangulaire) que l'on souhaite cartographier et on exporte la sélection au format CSV qu'on nommera select.csv.
1. On ouvre ce fichier dans LibreOffice Calc (ou logiciel propriétaire équivalent) et on supprime l'entête des colonnes ainsi que toutes les colonnes sauf celle contenant le nom des tuiles.
1. Dans la colonne adjacente on écrit cette formule :
    - Libre office : `=CONCAT(A1;".asc")`
    - Excel : `=CONCATENER(A1;".asc")`
1. On applique la formule sur l'ensemble de la colonne et on remplace par les valeurs "en dur " avec un collage spécial.
1. Puis on supprime la colonne d'origine.
1. Enfin on change à la brutasse l'extension du fichier en TXT ce qui nous donne une fois ouvert :

    ![exemple fichier tuile](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img2_tuiles.png){: .img-center loading=lazy }

1. On déplace ce fichier directement dans le répertoire contenant les tuiles ASC téléchargées.

Et maintenant GDAL coeuravélesdoigts :heart_hands:.

#### Le moment ligne de commandes

![logo console terminal](https://cdn.geotribu.fr/img/logos-icones/divers/ligne_commande.png "logo console terminal"){: .img-thumbnail-left }

Pour les non-initiés à la ligne de commande, on se déplace dans un répertoire avec la commande `cd` (pour _change directory_). On peut soit passer un répertoire situé dans le repertoire courant, soit une adresse complète.

Exemple :

- sur Linux : `cd /home/nabuchodonosor/Documents`
- sur Windows : `cd C://Users/nabuchodonosor/Documents`

Sur Windows, pour changer de lecteur, juste indiquer la lettre et les deux points, sans `cd` (exemple `D:`).

(on peut copier l'adresse dans l'explorateur et la coller pour se simplifier la vie)

Pour remonter d'un cran dans l'arborescence :

```sh
cd ..
```

!!! tip "le nommage des fichiers et dossiers"
    Vous vous souvenez de ces gens relous qui vous demandent des noms de dossiers/fichiers juste en alphanumériques et sans espaces mais avec des `_` ? C'est pour ça.

Les commandes GDAL sont accompagnées de `-` ou `--` et de lettres, ceci correspond aux options spécifiques du programme.

### Mosaïquage

On se déplace dans le dossier contenant les images. Exemple :

![exemple fichier tuile](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img3_cd.png){: .img-center loading=lazy }

On va ensuite utiliser [GDAL_merge.py](https://GDAL.org/programs/GDAL_merge.html), le programme de GDAL permettant de fusionner des images.

```sh
gdal_merge.py -o mosaic.tif -co BIGTIFF=YES --optfile select.txt
```

- l'option`-o` permet de spécifier le nom du fichier de sortie (c'est donc obligatoire). On ne caressera jamais assez dans le sens du poil les gens derrière GDAL donc on dit que c'est très fort et ça reconnait le type de fichier désiré juste avec l'extension.
- `-co` correspond aux options spécifiques non pas du programme mais du driver du type de fichier (ici geotiff). BIGTIFF permet de faire des tif de plus de 4gb. Ce n'est pas mon cas ici mais ça ne coûte rien de passer la commande par sécurité.

Il faut ensuite normalement spécifier un par un les noms de fichiers à fusionner, ce qui serait fastidieux, mais l'option `--optfile` nous permet de passer un fichier contenant une liste, d'où les étapes précédentes !

Dans le répertoire, vous trouverez votre geotiff `mosaic.tif` que je vous encourage à déplacer ailleurs pour vous y retrouver.

Dans ~~l'interface graphique de GDAL~~ QGIS cette étape est faisable via le menu `raster -> Divers -> fusion` (il faut au préalable charger l'ensemble des tuiles voulues dans QGIS).

### Reprojection

![icône projection](https://cdn.geotribu.fr/img/logos-icones/divers/projection.png){: .img-thumbnail-left }

On va maintenant reprojeter (vous vous souvenez des fichiers ASC ?) notre image avec [GDALwarp](https://GDAL.org/programs/GDALwarp.html) le programme servant à... reprojeter.

Se déplacer dans le répertoire où vous avez placé l'image et :

```sh
gdalwarp -t_srs EPSG:2154 -r near -co BIGTIFF=YES mosaic.tif mosaicl93.tif
```

- L'option `-t_srs` sert à indiquer le [SRID](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_coordonn%C3%A9es_(cartographie)) de sortie.
- `-r` permet de spécifier la méthode de rééchantillonnage. Le choix dépasse le cadre de cet article mais sachez que des methodes avancées comme `cubicspline` ou `lanczos` peuvent donner des résultats "floutés" car modifiant la valeur des pixels selon des courbes. On va donc rester sur la méthode par défaut : `nearest neighbour` (plus proche voisin) pour éviter ceci.

Pour celles et ceux à l'aise avec GDAL, vous pouvez compresser les images pour réduire la taille des fichiers de sortie au moins en `deflate` (pour les autres, ça se fait en passant une seconde option pour le driver de type de fichier : `-co COMPRESS=methode`, la plus couramment utilisée étant `-co COMPRESS=DEFLATE` pour s'assurer de la compatibilité avec tous les systèmes/logiciels).

Sinon, dans QGIS, ça se fait avec `Raster -> Projection -> Assigner une projection`.

### Fausser les données

Oui. Nous allons commettre ceci. Ne sortez pas les bidons d'essence tout de suite s'il vous plaît. Pour ce que nous allons en faire, Blender n'accepte que les images en entier 16 bits non signés (`UInt16`, on y reviendra), donc une plage de valeur pour les pixels comprise entre 0 et 65 535. Mais sans virgules, ce que contient notre raster initial donc on perdrait du détail. L'idée est donc de réattribuer aux pixels de notre image des valeurs sur l'ensemble de cette plage, ceci pour bénéficier de l'entièreté de cette finesse.

On fait ça avec [GDAL_calc.py](https://GDAL.org/programs/GDAL_calc.html) mais on peut aussi rester simple et faire ça avec la calculatrice raster de QGIS.

Tout d'abord, on normalise notre raster car certaines valeurs peuvent êtres en dessous de 0 (notamment quand il y a de l'eau). On va donc les mettre à 0.

```sh
gdal_calc.py -A moasicl93.tif --outfile=mosaic_cut.tif --calc="A*(A>=0)"
```

Avec `GDAL_calc.py`, les maths doivent être "[numpy](https://numpy.org/) style".

- `-A` permet d'attribuer un raster à une lettre qui sera ensuite utilisée dans la formule.
- `--outfile` le nom du fichier de sortie (ça dépend des programmes GDAL, souvent c'est la position du nom qui fait foi dans la commande).
- `--calc` la formule de calcul, entourée de `""`.

Ou dans QGIS : `raster -> calculatrice raster` puis :

![calc_raster](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img4_calc.png)

Où la formule se comprend ainsi : `if (condition, valeur si vrai, valeur si faux)`

On regarde les valeurs minimum et maximum de notre raster, soit dans les propriétés de la couche QGIS, soit avec [GDALinfo](https://GDAL.org/programs/GDALinfo.html).

```sh
gdalinfo -mm mosaic_cut.tif
```

- l'option `-mm` permet de forcer le calcul des valeurs min/max qui n'est pas donné par défaut par `gdalinfo`. Elles apparaitront tout en bas (dans mon cas, 0 et 196,8).

![Là](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img5_minmax.png){: .img-center loading=lazy }

Le calcul à faire pour réaffecter nos pixels est le suivant :

```math
(Valeur pixel – min) ÷ (max – min) * 65535
```

Dans mon cas cela donne :

```sh
gdal_calc.py -A mosaic_cut.tif --outfile=mosaic_rescale.tif --calc="(A - 0) / (196.8 - 0) * 65535"
```

Dans la calculatrice raster de QGIS, cela donnerait :

```math
("mosaic_cut@1" - 0) / (196.8 - 0) * 65535
```

Enfin, on va convertir notre raster en UInt16 pour l'importer dans Blender. C'est cette opération qui n'est pas réalisable dans QGIS sans circonvolutions. Donc on sort [GDAL_translate](https://GDAL.org/programs/GDAL_translate.html), le programme qui sert à faire des conversions.

```sh
gdal_translate -ot UInt16 mosaic_rescale.tif mnt.tif
```

- `-ot` est l'option qui permet de forcer le type de données de sortie.
- les fichiers d'entrée et de sortie se précisent par leur position dans la commande comme précisée dans la [**documentation**](https://GDAL.org/index.html) très complète de GDAL que je m'efforce de vous inciter à consulter depuis le début en vous en spammant le lien le plus de fois possible.

Voilà, nos données sont désormais fin prêtes !  
La suite sous Blender prochainement !

[Lire la deuxième partie :fontawesome-solid-forward:](2024-06-18_carte-relief-ombre-avec-blender-partie-2-modelisation-reglages-cartographie.md "Réaliser des cartes avec Blender - Partie 2"){: .md-button }
{: align=middle }

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-nc-sa.md" %}
