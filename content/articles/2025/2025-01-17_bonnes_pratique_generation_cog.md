---
title: "Optimiser vos rasters et générer des mosaïques au format COG (Cloud Optimized GeoTIFF) avec GDAL"
authors:
  - Nicolas ROCHARD
categories:
  - article
comments: true
date: 2025-02-11
description: "Découvrez comment optimiser vos rasters et créer des mosaïques au format COG avec GDAL pour une gestion efficace des données raster géospatiales."
icon: :material-grid:
image:
license: default
robots: index, follow
tags:
    - COG
    - GDAL
    - raster
---

# Optimiser vos rasters et générer des mosaïques au format COG (Cloud Optimized GeoTIFF) avec GDAL

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

Les données Raster sont une composante majeure des référentiels de nos systèmes d'information géographique. Ces fichiers sont bien plus volumineux que des données vectorielles et sont parfois fragmenté en plusieurs dalles rendant son chargement laborieux. Lorsque ces données sont disponibles en flux WMS ou WMTS, alors leur consultation est plus aisée mais présente des limitations (pas de possibilité d'affiner la radiométrie, lenteur d'affichage, problème d'impression, etc.). Il est alors indispensable d'avoir une donnée en locale ou sur le réseau de la structure. C'est là que le format COG intervient pour simplifier la vie des géomaticiens. Ces fichiers, optimisés pour le cloud, facilitent le traitement et la visualisation des données spatiales à grande échelle grâce à leur accessibilité rapide et leur structure efficiente. Conçus spécifiquement pour le cloud, les COG offrent de nombreux avantages sur d'autres environnements :

- **Performance améliorée** : affichage quasi-immédiat même sur des volumes importants évitant ainsi les frustrations liées aux lenteurs, que ce soit au bureau ou en télétravail.
- **Données peu ou pas alterées**_(en fonction des options de compression choisies)_ : vous pouvez modifier la radiométrie, l'ordre des bandes, l'utiliser dans des processus de geotraitements, etc.
- **Simplicité d'organisation** : une seule image à charger, éliminant le besoin de VRT peu performant, la génération de pyramides et réduisant la gestion de nombreux fichiers

Dans cet article, nous explorerons les meilleures pratiques pour générer des COG en utilisant GDAL, un outil incontournable dans l'arsenal SIG.

## Pré-requis

Avant de commencer la génération de COG, assurez-vous de disposer des éléments suivants :

- **GDAL Version 3.1 ou supérieure** : Vérifiez que votre installation de GDAL est à jour pour bénéficier des dernières améliorations et fonctionnalités spécifiques aux COG.
- **Types de Raster appropriés** : Pour les données raster à une bande (comme les Modèles Numériques de Terrain - MNT ou d’Élévation - MNE), utilisez des fichiers au format TIF, ASC ou tout autre format compatible avec GDAL. Pour les rasters à trois bandes, les orthophotos sont particulièrement adaptées.
- **Environnement Linux ou Windows** : Les commandes abordées ici ont été testées sur ces deux systèmes d’exploitation.

## Construction du VRT pour un Raster à 1 Bande

Pour combiner plusieurs fichiers raster ASC en un VRT (Virtual Raster Tile), une étape nécessaire avant de générer le COG final, utilisez la commande suivante :
:penguin:

```bash
gdalbuildvrt my_dsm.vrt -addalpha -a_srs EPSG:2154 /dsm_directory/*.asc
```

🪟

```powershell
gdalbuildvrt.exe C:\dsm\my_dsm.vrt C:\dsm_directory\*.asc -addalpha -a_srs EPSG:2154
```

- `-addalpha` : Ajoute un canal alpha.
- `-a_srs EPSG:2154` : Définit le système de référence spatiale à utiliser.

## Conversion en COG pour un Raster à 1 Bande

Une fois le VRT construit, transformez-le en COG avec cette commande :

:penguin:

```bash
gdal_translate input_dsm.vrt my_dsm_output_cog.tif -of COG \
  -co RESAMPLING=NEAREST \
  -co OVERVIEW_RESAMPLING=NEAREST \
  -co COMPRESS=DEFLATE \
  -co PREDICTOR=2 \
  -co NUM_THREADS=20 \
  -co BIGTIFF=IF_NEEDED
```

🪟

```powershell
ggdal_translate.exe C:\dsm\input_dsm.vrt C:\dsm\my_dsm_output_cog.tif -of COG -co BLOCKSIZE=512 -co OVERVIEW_RESAMPLING=NEAREST -co COMPRESS=DEFLATE -co PREDICTOR=2 -co NUM_THREADS=20 -co BIGTIFF=IF_NEEDED
```

### Points clés

- **Resampling** : Utilisez `RESAMPLING=NEAREST` pour préserver l'intégrité des données.
- **Optimisation des performances** : Ajustez `NUM_THREADS` en fonction de la capacité de votre machine.

## Processus pour un Raster à 3 Bandes

### Conversion de JP2 en TIF

Commencez par convertir chaque fichier JP2 en TIF en utilisant une boucle bash. Assurez-vous d'avoir créé un répertoire dédié pour les fichiers TIF :

:penguin:

```bash
for f in *.jp2; do
  gdal_translate -of GTiff \
    -co TILED=YES \
    -co BIGTIFF=YES \
    -co BLOCKXSIZE=512 \
    -co BLOCKYSIZE=512 \
    -co NUM_THREADS=20 \
    -co COMPRESS=ZSTD \
    -co PREDICTOR=2 \
    ${f} ../0_TIF/${f%.*}.tif
done
```

🪟

```powershell
FOR %%F IN (C:\ortho\jpg2\*.jp2) DO gdal_translate.exe -of GTiff -co TILED=YES -co BIGTIFF=YES -co BLOCKXSIZE=512 -co BLOCKYSIZE=512 -co NUM_THREADS=20 -co COMPRESS=ZSTD -co PREDICTOR=2 -a_srs EPSG:2154 %%F C:\ortho\0_TIF\%%~nxF.tif
```

- **Taille des blocs** : `BLOCKXSIZE` et `BLOCKYSIZE` impactent les performances de lecture.

### Construction du VRT pour un Raster à 3 Bandes

Créez un VRT pour votre ensemble de données TIFF avec la commande suivante :

:penguin:

```bash
gdalbuildvrt my_orthophotography.vrt 0_TIF/*.tif -addalpha -hidenodata -a_srs EPSG:2154
```

🪟

```powershell
gdalbuildvrt.exe C:\ortho\my_orthophotography.vrt C:\ortho\0_TIF\*.tif -addalpha -hidenodata -a_srs EPSG:2154
```

- `-hidenodata` : Masque les cellules nodata, rendant les zones correspondantes transparentes.

### Conversion du VRT en COG

Générez le COG à partir du VRT :

:penguin:

```bash
gdal_translate my_orthophotography.vrt my_orthophotography_output_cog.tif -of COG \
  -co BLOCKSIZE=512 \
  -co OVERVIEW_RESAMPLING=BILINEAR \
  -co COMPRESS=JPEG \
  -co QUALITY=85 \
  -co NUM_THREADS=12 \
  -co BIGTIFF=YES
```

🪟

```powershell
gdal_translate.exe C:\ortho\my_orthophotography.vrt C:\ortho\my_orthophotography_output_cog.tif -of COG -co BLOCKSIZE=512 -co OVERVIEW_RESAMPLING=BILINEAR -co COMPRESS=JPEG -co QUALITY=85 -co NUM_THREADS=12 -co BIGTIFF=YES
```

- **Compression JPEG** : Un bon compromis entre taille de fichier et qualité avec une `QUALITY` de 85.
- **Rééchantillonnage** : `BILINEAR` pour un rendu visuel optimal dans les visualisations géospatiales.

## Cas Particuliers et Bonnes Pratiques

### Découpe selon un Contour

Pour éliminer les pixels indésirables en bordure (non définis comme nodata), utilisez un shapefile d'emprise :

:penguin:

```bash
gdalwarp -of GTiff \
  -co TILED=YES \
  -co BIGTIFF=YES \
  -co BLOCKXSIZE=512 \
  -co BLOCKYSIZE=512 \
  -co NUM_THREADS=12 \
  -co COMPRESS=ZSTD \
  -co PREDICTOR=2 \
  -s_srs EPSG:2154 \
  -t_srs EPSG:2154 \
  -dstalpha \
  -cutline area_of_interest.shp \
  input_image.jp2 \
  image_output.tif
```

🪟

```powershell
gdalwarp.exe -of GTiff -co TILED=YES -co BIGTIFF=YES -co BLOCKXSIZE=512 -co BLOCKYSIZE=512 -co COMPRESS=ZSTD -co PREDICTOR=2 -s_srs EPSG:2154 -t_srs EPSG:2154 -dstalpha -cutline C:\data\area_of_interest.shp C:\ortho\input_image.jp2 C:\ortho\image_output.tif
```

### Conversion de JP2 en TIFF RVBA

Pour convertir un JP2 en TIFF RVBA tout en préservant l’unité colorimétrique :

:penguin:

```bash
gdal_translate -of GTiff \
  -co BIGTIFF=YES \
  -co TILED=YES \
  -co BLOCKXSIZE=512 \
  -co BLOCKYSIZE=512 \
  -co NUM_THREADS=12 \
  -co COMPRESS=ZSTD \
  -co PREDICTOR=2 \
  -b 1 -b 2 -b 3 -b mask \
  -colorinterp red,green,blue,alpha \
  -a_srs EPSG:2154 \
  input_image.jp2 \
  output_image.tif
```

🪟

```powershell
gdal_translate.exe -of GTiff -co BIGTIFF=YES -co TILED=YES -co BLOCKXSIZE=512 -co BLOCKYSIZE=512 -co NUM_THREADS=12 -co COMPRESS=ZSTD -co PREDICTOR=2 -b 1 -b 2 -b 3 -b mask -colorinterp red,green,blue,alpha -a_srs EPSG:2154 C:\ortho\input_image.jp2 C:\ortho\output_image.jp2
```

## Considérations Finales

- **Compression** :
    - Utilisez `JPEG` pour les fichiers RVB (3 bandes).
    - Préférez `DEFLATE` ou `ZSTD` pour les fichiers avec plus de 3 bandes ou en 16 bits.
- **Méthode de Rééchantillonnage** :
    - `BILINEAR` est idéal pour le rendu visuel.
    - `NEAREST` est recommandé pour les traitements analytiques afin de préserver l'intégrité des données.

En suivant ces bonnes pratiques, vous assurerez une génération efficace de COG, améliorant ainsi la manipulation et la visualisation de vos données spatiales quelque soit votre environnement.

Si vous souhaitez apporter votre expertise aux bonnes pratiques et astuces de GDAL et du COG, n'hésitez pas à contribuer à ce dépôt <https://github.com/geo2france/cog-tips>. Merci à Benjamin Chartier pour avoir proposé les commandes Windows.

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
