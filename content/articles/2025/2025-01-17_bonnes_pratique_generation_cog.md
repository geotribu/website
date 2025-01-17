---
title: "Optimiser vos raster et générer vos mosaïques en format COG (Cloud Optimized GeoTIFF) avec GDAL"
authors:
    - Nicolas ROCHARD
categories:
    - article
comments: true
date: 2024-04-11
description: "Description de 160 caractères maximum qui résume l'article qui est présente dans le flux RSS, la newsletter, les moteurs de recherche, en page d'accueil... "
icon: "icone à choisir parmi celles disponibles dans le thème : https://squidfunk.github.io/mkdocs-material/reference/#setting-the-page-icon. Cliquer sur le + pour dérouler un mini moteur de recherche"
image: "Image d'illustration de l'article qui sert ensuite dans la mise en avant : réseaux sociaux, flux RSS... 400x800 en PNG"
license: default
robots: index, follow
tags:
    - raster
    - image
    - gdal
---

# Optimiser vos raster et générer vos mosaïques en format COG (Cloud Optimized GeoTIFF) avec GDAL

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

La génération de fichiers Cloud Optimized GeoTIFF (COG) est de plus en plus cruciale dans les domaines de la géomatique et des systèmes d'information géographique (SIG). Ces fichiers optimisés pour le cloud facilitent le traitement et la visualisation des données spatiales à grande échelle grâce à leur accessibilité rapide et leurs structures optimisées. 
S'il est conçu pour le cloud, il présente bien des avantages sur d'autres environnement : 

- gain de performances sur les flux WMS
- affiche quasi instantané dans le cadre d'une utilisation en réseau. Qui n'a jamais pesté contre des lenteurs réseaux que ce soit au bureau ou en télétravail ?
Dans cet article, nous allons explorer les meilleures pratiques pour générer des COG en utilisant GDAL, un incontournable de l'outillage SIG.
- N'avoir qu'une image uniquement même pour des surfaces importantes à charger. Pas besoin de VRT, organisation sous forme de fichiers bien plus simple (1 seul contre x centaines ou milliers de fichiers)

## Pré-requis

Avant de commencer avec la génération de COG, voici quelques pré-requis essentiels:

- **GDAL Version 3.1 ou supérieure**: Assurez-vous que votre installation de GDAL est à jour. Les versions plus récentes comprennent des améliorations et des fonctionnalités spécifiques pour le COG.
- **Types de Raster appropriés**: Pour les données raster à une bande (comme les Modèles Numériques de Terrain - MNT - ou d’Élévation - MNE), vous pourriez utiliser des fichiers au format TIF, ASC, bref tout ce que peux lire GDAL. Quant aux rasters à trois bandes, ceux-ci couvrent notamment les orthophotos.
- **Environnement Linux ou Windows**: Les commandes et opérations décrites ici ont été testées sur les deux systèmes d’exploitation.

## Construction du VRT pour Raster 1 Bande

Pour combiner plusieurs fichiers raster ASC en un VRT (Virtual Raster Tile), une étape nécessaire avant de générer le COG final, utilisez la commande suivante :

```bash
gdalbuildvrt my_dsm.vrt -addalpha -a_srs EPSG:2154 /dsm_directory/*.asc
```

Ici, le paramètre `-addalpha` sert à ajouter un canal alpha, et `-a_srs EPSG:2154` définit le système de référence spatiale à utiliser.

## Conversion en COG pour Raster 1 Bande

Une fois que le VRT est construit, transformez-le en un COG :

```bash
gdal_translate input_dsm.vrt my_dsm_output_cog.tif -of COG -co RESAMPLING=NEAREST -co OVERVIEW_RESAMPLING=NEAREST -co COMPRESS=DEFLATE -co PREDICTOR=2 -co NUM_THREADS=20 -co BIGTIFF=IF_NEEDED
```

Points clés à retenir:

- Le resampling, défini ici avec `RESAMPLING=NEAREST`, est essentiel pour protéger l'intégrité des données.
- Ajustez `NUM_THREADS` en fonction de la capacité de votre machine pour une optimisation des performances.

## Processus pour Raster 3 Bandes

### Conversion de JP2 en TIF

Commencez par convertir chaque fichier JP2 en TIF grâce à une boucle bash. Avant cette opération, assurez-vous d'avoir créé un répertoire désigné pour les fichiers TIF :

```bash
for f in *.jp2; do gdal_translate -of GTiff -co TILED=YES -co BIGTIFF=YES -co BLOCKXSIZE=512 -co BLOCKYSIZE=512 -co NUM_THREADS=20 -co COMPRESS=ZSTD -co PREDICTOR=2 ${f} ../0_TIF/${f%.*}.tif; done
```

La taille des blocs (`BLOCKXSIZE` et `BLOCKYSIZE`) est primordiale pour les performances de lecture ultérieures.

### Construction du VRT pour Raster 3 Bandes

Utilisez la commande suivante pour créer un VRT de votre ensemble de données TIFF :

```bash
gdalbuildvrt my_orthophotography.vrt 0_TIF/*.tif -addalpha -hidenodata -a_srs EPSG:2154
```

L'option `-hidenodata` masque les cellules nodata, transformant toute zone nodata en transparente.

### Conversion du VRT en COG

Ensuite, générez le COG à partir du VRT :

```bash
gdal_translate my_orthophotography.vrt my_orthophotography_output_cog.tif -of COG -co BLOCKSIZE=512 -co OVERVIEW_RESAMPLING=BILINEAR -co COMPRESS=JPEG -co QUALITY=85 -co NUM_THREADS=ALL_CPUS -co BIGTIFF=YES
```

L'utilisation de `COMPRESS=JPEG` avec une `QUALITY` comprise entre 85 et 90 garantit un bon compromis entre taille de fichier et qualité.

## Cas Particuliers et Bonnes Pratiques

### Découpe selon un Contour

Pour éliminer les pixels indésirables en bordure (non définis comme nodata), utilisez un shapefile d'emprise :

```bash
gdalwarp -of GTiff -co TILED=YES -co BIGTIFF=YES -co BLOCKXSIZE=512 -co BLOCKYSIZE=512 -co NUM_THREADS=12 -co COMPRESS=ZSTD -co PREDICTOR=2 -s_srs EPSG:2154 -t_srs EPSG:2154 -dstalpha -cutline area_of_interest.shp input_image.jp2 image_output.tif
```

### Conversion de JP2 en TIFF RVBA

Utilisez la commande ci-dessous pour convertir un JP2 en TIFF RVBA, préservant ainsi l’unité colorimétrique :

```bash
gdal_translate -of GTiff -co BIGTIFF=YES -co TILED=YES -co BLOCKXSIZE=512 -co BLOCKYSIZE=512 -co NUM_THREADS=12 -co COMPRESS=ZSTD -co PREDICTOR=2 -b 1 -b 2 -b 3 -b mask -colorinterp red,green,blue,alpha -a_srs EPSG:2154 input_image.jp2 output_image.tif
```

## Considérations Finales

- **Compression**: Préférez la compression `JPEG` pour les fichiers RVB (3 bandes) et `DEFLATE` ou `ZSTD` pour les fichiers ayant plus de 3 bandes ou en 16 bits.
- **Méthode de Rééchantillonnage**: `BILINEAR` est habituellement choisi pour le rendu visuel dans les visualisations géospatiales, mais optez pour `NEAREST` lors de traitements analytiques pour préserver l'intégrité des données.

En suivant ces bonnes pratiques, vous garantirez une production efficace de COG, améliorant ainsi la manipulation et la visualisation de vos données spatiales dans un environnement cloud. Ces optimisations tirent pleinement parti des capacités de GDAL, vous permettant de livrer des solutions géospatiales plus robustes et efficaces.

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
