---
title: "Reconstitution d'images aériennes historiques"
authors:
    - Florian Boret
categories:
    - article
    - tutoriel
date: 2023-03-07 14:20
description: "Reconstitution d'images aériennes historiques"
image: ""
license: beerware
tags:
    - OpenDroneMap
---

# Reconstitution d'images aériennes historiques

:calendar: Date de publication initiale : 13 janvier 2023

## Prérequis

- [OpenDroneMap](https://opendronemap.org/)
- bash
- [GDAL/OGR](https://gdal.org/)
- [ImageMagick](https://imagemagick.org)
- [Exiftool](https://exiftool.org/)

## Intro

Il y a des projets que tu as en tête depuis des mois pour ne pas dire plus. Et puis un jour, c’est le bon moment, un créneau s’ouvre, tu t’engouffres dans la brèche happé par l’envie. Je vous propose donc de découvrir comment j’ai reconstitué des images aériennes historiques sur mon territoire à partir des imagettes disponibles sur le site : [Remonter le temps](https://remonterletemps.ign.fr) de l’IGN.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Processus global

Le processus que je vous présente mélange du bash, de l'OGR,...

```mermaid

```

## Identifier les missions

### Depuis le site

Les images mises à disposition par l'IGN sur le site Remonter le temps peuvent être consultées par année de prise de vue ce qui dans les faits correspond plutôt aux différentes missions réalisées.

Pour trouver l'identifiant de la mission, il faut :

1. Se rendre dans la section `Télécharger` et renseigner une ville
2. Sélectionner une année et vous visualiserez la localisation des images produites
3. Cliquer sur une image
4. En haut à droite, vous verrez `Identifiant de la mission` mais l'identifiant correspond plutôt aux caractères entre le `C` et le premier `_`. Exemple : `C2844-0561_1937_NP4_1302`, l'identifiant est `2844-0561`

### A travers un script

Si vous préférez une méthode plus automatique pour identifier toutes les missions qui ont été réalisées sur votre territoire, vous pouvez opter l'option du script qui permet après avoir paramétré son environnement de travail (détail ci-dessous) de récupérer un fichier `json` des missions et de le convertir au format `csv`.

```bash
#!/bin/bash

# LECTURE DU FICHIER DE CONFIGURATION
. './config.env'

# REPERTOIRE DE TRAVAIL
cd $REPER
echo $REPER

# AFFICHER L'URL
echo $url

# RECUPERER LA LISTE DES MISSIONS CONCERNEES PAR L'EMPRISE
curl "$url" -H 'Host: wxs.ign.fr' --compressed > './1_missions/missions.json'

# CONVERTIR LE FICHIER JSON EN CSV
ogr2ogr -f CSV './1_missions/missions.csv' './1_missions/missions.json'

# TRIER LES MISSIONS PAR DATE
(tail -n +2 './1_missions/missions.csv' | sort -t, -k2n | cat <(head -1 './1_missions/missions.csv') - ) > './1_missions/missions_sort.csv'

# SUPPRESSION DES FICHIERS TEMPORAIRES
rm './1_missions/missions.csv'
rm './1_missions/missions.json'
```

[Consulter le script :fontawesome-regular-file-code:](https://github.com/igeofr/remonterletemps2img/blob/main/1_missions.sh){: .md-button }
{: align=middle }

#### Un environnement de travail : config.env

Avant de se lancer, il est bon de paramétrer le fichier de configuration que vous devrez adapter à votre organisation et qui sera utilisé par la suite pour télécharger et traiter les images. On y définit le répertoire de travail et différentes variables nécessaires à la bonne éxécution du script.

Voici le fichier `config.env` à adapter :

```ini
# CLEF IGN
key='x7yv499pbcguxhhxh8syehwe'

# REPERTOIRE DE TRAVAIL
REPER='XXXXXXXX'

# BBOX
bbox='BBOX(the_geom,43.66882,4.12714,43.6801,4.1434)'

# URL MISSIONS
url="https://wxs.ign.fr/search/layers?request=GetFeature&version=1.1.0&typeName=ign:missions&propertyName=jp2,kml_layer_id,pv_date,title&CQL_FILTER=demat_layer_id%20like%20%27%25DEMAT.PVA\$GEOPORTAIL:DEMAT;PHOTOS%25%27%20and%20$bbox&outputFormat=application/json"

# ID MISSIONS
id_mission='XXXXXXXX'

# PARAMETRES OGR
ENCODAGE='UTF-8'
```

[Consulter le fichier de configuration :fontawesome-regular-file-code:](https://github.com/igeofr/remonterletemps2img/blob/main/config.env){: .md-button }
{: align=middle }

## Identifier, télécharger et mettre en forme les images d'une mission

On ne peut pas dire que l'IGN nous facilite la tâche sur l'identification et le téléchargement en lot d'images mais on finit toujours par trouver une alternative.

### Identifier les images

Pour identifier les images d'une mission, il télécharger un premier fichier `kml` qui sert de point de départ pour chercher une filiation et trouver des enfants, petits enfants et arrières petits enfants.

```bash
# TELECHARGER LE FICHIER DE DEPART DE LA MISSION
curl "https://wxs.ign.fr/$key/dematkml/DEMAT.PVA/$id_mission/t.kml" > $folder_mission'/kml/'$id_mission'.kml'
```

Après avoir télécharger nos `X` fichiers `kml` et pour terminer, on va pouvoir les assembler recréer la mosaïque des prises de vue au format `shapefile` pour faciliter sa visualisation dans QGIS.

[Consulter le script :fontawesome-regular-file-code:](https://github.com/igeofr/remonterletemps2img/blob/main/2_mission_kml.sh){: .md-button }
{: align=middle }

### Télécharger les images et les convertir

Maintenant que l'on a récupéré l'emprise et la liste de toutes les images de la mission, on va devoir faire encore quelques opérations d'extraction et de mise en forme qui vont nous servir à filtrer les images qui se trouvent dans la BBOX que nous avons défini dans le fichier de configuration `config.env`.

Une fois le téléchargement des images en `jp2`, on doit les convertir au format `jpg` pour pouvoir les exploiter dans OpenDroneMap.

```bash
 while IFS="," read -r Name ; do
    echo ">>>>>>>" $Name
    echo "URL de téléchargement : https://wxs.ign.fr/$key/jp2/DEMAT.PVA/$id_mission/$Name.jp2"
    curl "https://wxs.ign.fr/$key/jp2/DEMAT.PVA/$id_mission/$Name.jp2" > $folder_mission'/img_jp2/'$Name'.jp2'
    gdal_translate -of JPEG $folder_mission'/img_jp2/'$Name'.jp2' $folder_mission'/img_jpg/'$Name'.jpg';
  done < <(cut -d "," -f${loc_col_a} -s $folder_mission'/csv_liste_img/liste_img.csv'| awk '{if (NR!=1) {print}}')
```

### Intégrer la localisation de l'image

A partir de l'emprise des images on va calculer le centroïde de chacune des images qui se trouvent dans notre BBOX et récupérer les informations sur la date de la prise de vue.

```bash
ogr2ogr \
    -f CSV \
    $folder_mission'/csv_exif/list_exif.csv' \
    $folder_mission'/couverture_bbox/captures_join.shp' \
    -dialect sqlite \
    -sql "SELECT '"$folder_mission'/img_jpg/'"'||img||'"'.jpg'"' as SourceFile, y(Centroid(geometry)) as GPSLatitude, x(Centroid(geometry)) as GPSLongitude, replace(date,'-',':')||' 00:00:00' AS DateTimeOriginal FROM captures_join"
```

Une fois le fichier des attributs nécessaires à `Exiftool` généré, il faut simplement lancer la commande permettant d'insérer ses attributs dans chacune des images.

```
exiftool -csv=$folder_mission'/csv_exif/list_exif.csv' $folder_mission'/img_jpg' -Overwrite_Original -m
```

### Découper le cadre autour des images

## Reconstituer une image aérienne

### Identifier des GCP

### Reconstituion avec OpenDroneMap

----

## Conclusion

----

## Auteur {: data-search-exclude }

--8<-- "content/team/fbor.md"

{% include "licenses/beerware.md" %}
