---
title: "Utiliser GDAL pour traiter les fichiers au standard Bases Adresses Locales"
authors: ["Julien MOURA"]
categories: ["article", "tutoriel"]
date: "2021-09-07 10:20"
description: "Travailler les données de la Base Adresse Nationale (BAN) avec GDAL/OGR."
image: ""
license: default
tags: "GDAL,OGR,CSV,Adresse,BAL,BAN"
---

# Un fichier GDAL/OGR VRT pour les Bases Adresses Locales

:calendar: Date de publication initiale : 7 septembre 2021

**Mots-clés :** Adresse | BAL | CSV | GDAL

Prérequis :

- GDAL > 3 - sur [Windows 10+, il est possible d'utiliser WSL](/articles/2020/2020-10-28_gdal_windows_subsystem_linux_wsl/)

## Introduction

![logo BAN](https://cdn.geotribu.fr/img/logos-icones/divers/ban.png "logo BAN"){: .img-rdp-news-thumb }

On parle beaucoup des données de la Base Adresse Nationale (BAN) ces dernières années. Peu complexes et facilement accessibles [ici](https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/) au format CSV (compressés avec GZIP), elles bénéficient d'un bon outillage et d'un usage largement diffusé. D'ailleurs, on en parle régulièrement [ici même sur Geotribu](/?q=adress).

Dans ce tutoriel, je vous propose de tirer parti de fonctionnalités de GDAL parfois méconnues pour automatiser les différents étapes:

1. télécharger les données
2. les décompresser
3. les analyser
4. les convertir et intégrer

Pour les besoins de ce tutoriel, on va utiliser les données du plus grand département de France métropolitaine, [la Gironde](https://fr.wikipedia.org/wiki/Gironde_(d%C3%A9partement)) dont la dernière version des données de la base adresses est : <https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz>.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Télécharger et décompresser : la magie du VSI

![logo GDAL](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/gdal.png "logo GDAL"){: .img-rdp-news-thumb }

Pour commencer, jetons un coup d'oeil à ces fameux CSV de la BAN accessibles [ici](https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/) au format CSV compressés avec GZIP. On doit donc :

1. télécharger les données
2. les décompresser
3. les analyser
4. les transformer

Pour gagneren tirant parti du [système de fichier virtuel (VSI)](https://gdal.org/user/virtual_file_systems.html) intégré à GDAL, qui permet de gérer l'accès à des fichiers stockés ailleurs que sur un disque local, dans différents protocoles (HTTP, FTP...), formats de compression (ZIP, GZIP, TAR...) et mécanismes d'abstraction (APIs, stockage objet...).

C'est parti pour notre `ogrinfo` des familles :

```bash
ogrinfo -ro -al -so \
    -oo AUTODETECT_TYPE=YES \
    -oo AUTODETECT_WIDTH=YES \
    /vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz
```

Ce qui nous donne :

```bash
INFO: Open of `/vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz'
      using driver `CSV' successful.

Layer name: adresses-33
Geometry: None
Feature Count: 775598
Layer SRS WKT:
(unknown)
id: String (23.0)
id_fantoir: String (10.0)
numero: Integer (4.0)
rep: String (6.0)
nom_voie: String (40.0)
code_postal: Integer (5.0)
code_insee: Integer (5.0)
nom_commune: String (19.0)
code_insee_ancienne_commune: String (0.0)
nom_ancienne_commune: String (0.0)
x: Real (9.2)
y: Real (10.2)
lon: Real (9.6)
lat: Real (9.6)
alias: String (0.0)
nom_ld: String (0.0)
libelle_acheminement: String (18.0)
nom_afnor: String (32.0)
source_position: String (8.0)
source_nom_voie: String (8.0)
```

En regardant du côté du [format BAL] qui est bien documenté grâce aux petits soins de l'[AITF] (merci entre autres à Maël Reboux et Chantal Arruti) et de [la documentation GDAL sur les CSV](https://gdal.org/drivers/vector/csv.html#open-options), on peut dès lors améliorer encore un peu les choses :

- demander à GDAL de déterminer les types des différents champs
- indiquer que la première ligne est un en-tête
- indiquer les champs à utiliser pour les coordonnées géographiques ([`lat` et `lon` en WGS84](https://github.com/etalab/adresse.data.gouv.fr/blob/master/public/schemas/adresses-csv.md?plain=1#L21-L22)) mais ne pas les garder dans le fichier final

Ce qui donne :

```bash
ogrinfo -ro -al -so \
    -oo AUTODETECT_TYPE=YES -oo AUTODETECT_WIDTH=YES \
    -oo HEADERS=YES \
    -oo X_POSSIBLE_NAMES=lon \
    -oo Y_POSSIBLE_NAMES=lat \
    -oo KEEP_GEOM_COLUMNS=NO \
    /vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz
```

On a donc gagné le type de géométrie et les types des attributs :

```bash hl_lines="5"
INFO: Open of `/vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz'
      using driver `CSV' successful.

Layer name: adresses-33
Geometry: Point
Feature Count: 775598
Warning 1: Value with a width greater than field width found in record 13777 for field nom_voie. This warning will no longer be emitted
Extent: (-1.256226, 44.202126) - (0.312561, 45.570345)
Layer SRS WKT:
(unknown)
id: String (23.0)
id_fantoir: String (10.0)
numero: Integer (4.0)
rep: String (6.0)
nom_voie: String (40.0)
code_postal: Integer (5.0)
code_insee: Integer (5.0)
nom_commune: String (19.0)
code_insee_ancienne_commune: String (0.0)
nom_ancienne_commune: String (0.0)
x: Real (9.2)
y: Real (10.2)
alias: String (0.0)
nom_ld: String (0.0)
libelle_acheminement: String (18.0)
nom_afnor: String (32.0)
source_position: String (8.0)
source_nom_voie: String (8.0)
```

On peut même convertir tout cela à la volée :

```bash
ogr2ogr \
  -f GPKG \
  -t_srs 'EPSG:2154' \
  -nln "gironde" \
  -oo AUTODETECT_TYPE=YES -oo AUTODETECT_WIDTH=YES \
  -oo HEADERS=YES \
  -oo X_POSSIBLE_NAMES=lon \
  -oo Y_POSSIBLE_NAMES=lat \
  -oo KEEP_GEOM_COLUMNS=NO \
  ban.gpkg \
  /vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz
```  

Mais on s'aperçoit que les types de champs ne sont pas corrects.

## Le format virtuel de GDAL à la rescousse

![logo BAL](https://cdn.geotribu.fr/img/logos-icones/divers/bal.png "logo BAL"){: .img-rdp-news-thumb }

On peut alors se créer un  fichier VRT qui va bien `adresses.vrt` :

```xml
<OGRVRTDataSource>
    <OGRVRTLayer name="adresses-33">
        <SrcDataSource>/vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz</SrcDataSource>
        <GeometryType>wkbPoint</GeometryType>
        <LayerSRS>EPSG:4326</LayerSRS>
        <GeometryField encoding="PointFromColumns" x="lon" y="lat"/>
        <Field name="id" />
        <Field name="id_fantoir" />
        <Field name="numero" type="integer" />
        <Field name="rep" />
        <Field name="nom_voie" />
        <Field name="code_postal" />
        <Field name="code_insee" />
        <Field name="nom_commune" />
        <Field name="code_insee_ancienne_commune" />
        <Field name="nom_ancienne_commune" />
        <Field name="alias" />
        <Field name="nom_ld" />
        <Field name="libelle_acheminement" />
        <Field name="nom_afnor" />
        <Field name="source_position" />
        <Field name="source_nom_voie" />
        <OpenOptions>
            <OOI key="AUTODETECT_TYPE">YES</OOI>
            <OOI key="AUTODETECT_WIDTH">YES</OOI>
        </OpenOptions>
    </OGRVRTLayer>
</OGRVRTDataSource>
```

Si on veut combiner les données d'un autre département, il faut duplicuer l'élément `<OGRVRTLayer>` :

```xml
<OGRVRTDataSource>
    <OGRVRTLayer name="gironde">
        <SrcDataSource>/vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz</SrcDataSource>
        <GeometryType>wkbPoint</GeometryType>
        <LayerSRS>EPSG:4326</LayerSRS>
        <GeometryField encoding="PointFromColumns" x="lon" y="lat"/>
        <Field name="id" />
        <Field name="id_fantoir" />
        <Field name="numero" type="integer" />
        <Field name="rep" />
        <Field name="nom_voie" />
        <Field name="code_postal" />
        <Field name="code_insee" />
        <Field name="nom_commune" />
        <Field name="code_insee_ancienne_commune" />
        <Field name="nom_ancienne_commune" />
        <Field name="alias" />
        <Field name="nom_ld" />
        <Field name="libelle_acheminement" />
        <Field name="nom_afnor" />
        <Field name="source_position" />
        <Field name="source_nom_voie" />
        <OpenOptions>
            <OOI key="AUTODETECT_TYPE">YES</OOI>
            <OOI key="AUTODETECT_WIDTH">YES</OOI>
        </OpenOptions>
    </OGRVRTLayer>
    <OGRVRTLayer name="landes">
        <SrcDataSource>/vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-40.csv.gz</SrcDataSource>
        <GeometryType>wkbPoint</GeometryType>
        <LayerSRS>EPSG:4326</LayerSRS>
        <GeometryField encoding="PointFromColumns" x="lon" y="lat"/>
        <Field name="id" />
        <Field name="id_fantoir" />
        <Field name="numero" type="integer" />
        <Field name="rep" />
        <Field name="nom_voie" />
        <Field name="code_postal" />
        <Field name="code_insee" />
        <Field name="nom_commune" />
        <Field name="code_insee_ancienne_commune" />
        <Field name="nom_ancienne_commune" />
        <Field name="alias" />
        <Field name="nom_ld" />
        <Field name="libelle_acheminement" />
        <Field name="nom_afnor" />
        <Field name="source_position" />
        <Field name="source_nom_voie" />
        <OpenOptions>
            <OOI key="AUTODETECT_TYPE">YES</OOI>
            <OOI key="AUTODETECT_WIDTH">YES</OOI>
        </OpenOptions>
    </OGRVRTLayer>
</OGRVRTDataSource>
```

## Utiliser le fichier VRT

Par exemple pour une conversion :

```bash
ogr2ogr \
  -f GPKG \
  -t_srs 'EPSG:2154' \
  ban33.gpkg \
  adresses.vrt
```



```xml
<OGRVRTDataSource>
    <OGRVRTLayer name="adresses-33">
        <SrcDataSource relativeToVRT="0" >/vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz</SrcDataSource>
        <GeometryType>wkbPoint</GeometryType>
        <LayerSRS>EPSG:4326</LayerSRS>
        <GeometryField encoding="PointFromColumns" x="lon" y="lat"/>
        <Field name="id" />
        <Field name="id_fantoir" />
        <Field name="numero" type="integer" />
        <Field name="rep" />
        <Field name="nom_voie" />
        <Field name="code_postal" />
        <Field name="code_insee" />
        <Field name="nom_commune" />
        <Field name="code_insee_ancienne_commune" />
        <Field name="nom_ancienne_commune" />
        <Field name="alias" />
        <Field name="nom_ld" />
        <Field name="libelle_acheminement" />
        <Field name="nom_afnor" />
        <Field name="source_position" />
        <Field name="source_nom_voie" />
        <OpenOptions>
            <OOI key="AUTODETECT_TYPE">YES</OOI>
            <OOI key="AUTODETECT_WIDTH">YES</OOI>
        </OpenOptions>
    </OGRVRTLayer>
</OGRVRTDataSource>
```

## Un petit CSVT pour la route

![icône CSV](https://cdn.geotribu.fr/img/logos-icones/divers/csv.png "icône CSV - CSV File by Eucalyp from the Noun Project"){: .img-rdp-news-thumb }

Tant qu'on y est, autant capitaliser sur ce travail pour faciliter les choses aux outils qui tirent parti des fichiers de définition des types de champs : les fichiers CSVT.  
C'est en tout cas utilisé par QGIS (voir [la doc officielle](https://docs.qgis.org/3.16/fr/docs/user_manual/managing_data_source/supported_data.html#using-csvt-file-to-control-field-formatting) et [ce billet de blog d'Anita Graser](https://anitagraser.com/2011/03/07/how-to-specify-data-types-of-csv-columns-for-use-in-qgis/))

```csv
fdfd,dfdfd
```

Si la ligne de commande vous effraie, il y a aussi des outils disponibles en ligne bien pratiques comme :

[CSVT Generator :fontawesome-solid-tools:](https://loicbcn.github.io/csvtgenerator/){: .md-button }
{: align=middle }

----

## Auteur

--8<-- "content/team/jmou.md"

{% include "licenses/default.md" %}

<!-- Hyperlinks reference -->
[AITF]: https://www.aitf.fr/
[format BAL]: https://schema.data.gouv.fr/etalab/schema-bal/latest.html
