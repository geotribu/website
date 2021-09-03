---
title: "Utiliser GDAL pour traiter les fichiers au standard Bases Adresses Locales"
authors: ["Julien MOURA"]
categories: ["article", "tutoriel"]
date: "2021-09-07 10:20"
description: "Travailler les données de la Base Adresse Nationale (BAN) avec GDAL/OGR."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/gdal_bal/gdal_bal.png"
license: beerware
tags: "GDAL,OGR,CSV,Adresse,BAL,BAN"
---

# Utiliser GDAL VSI et VRT pour intégrer les fichiers au standard BAL

:calendar: Date de publication initiale : 7 septembre 2021

**Mots-clés :** Adresse | BAL | CSV | GDAL

Prérequis :

- GDAL > 3 - sur [Windows 10+, il est possible d'utiliser WSL](/articles/2020/2020-10-28_gdal_windows_subsystem_linux_wsl/)

## Introduction

![logo BAN](https://cdn.geotribu.fr/img/logos-icones/divers/ban.png "logo BAN"){: .img-rdp-news-thumb }

On parle beaucoup des données de la Base Adresse Nationale (BAN) ces dernières années. Peu complexes et facilement accessibles [ici](https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/) au format CSV (compressé avec GZIP), elles bénéficient d'un bon outillage et d'un usage largement diffusé. D'ailleurs, on en parle régulièrement [ici même sur Geotribu](/?q=adress).

Dans ce tutoriel, je vous propose de tirer parti de fonctionnalités de GDAL parfois méconnues pour automatiser les différentes étapes:

1. télécharger les données
2. les décompresser
3. les analyser
4. les convertir et intégrer dans notre format préféré (ici le GeoPackage)

Pour les besoins de ce tutoriel, on va utiliser les données du plus grand département de France métropolitaine, [la Gironde](https://fr.wikipedia.org/wiki/Gironde_(d%C3%A9partement)) dont la dernière version des données de la base adresses est donc : <https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz>.

!!! tip
    Les commandes du tutoriel sont écrites en [Bash](https://en.wikipedia.org/wiki/Bash_(Unix_shell)). Elles peuvent être exécutées avec [WSL](https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux) sur Windows 10+ (cf. le tuto de l'an dernier). Si vous utilisez GDAL avec PowerShell, remplacez le caractère multi-ligne \\ par `.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Télécharger et décompresser

### La magie du VSI

![logo GDAL](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/gdal.png "logo GDAL"){: .img-rdp-news-thumb }

Voilà bien 2 étapes répétitives qu'il est facile d'automatiser en tirant parti de la gestion des [systèmes de fichiers virtuels](https://gdal.org/user/virtual_file_systems.html) intégré à GDAL (VSI).  
Le couteau-suisse de la géomatique intègre en effet des outils comme cURL et permet donc de gérer l'accès à des fichiers stockés ailleurs que sur un disque local, dans différents protocoles (HTTP, FTP...), formats de compression (ZIP, GZIP, TAR...) et mécanismes d'abstraction (APIs, stockage objet...). Très pratique pour qui n'a pas le temps d'apprendre à utiliser de multiples outils et surtout à les articuler.

La syntaxe est simple (préfixer le chemin d'accès avec `/vsi[protocole]/`) et puissante (chaînage possible). Quelques exemples rapides :

```bash
# lire un fichier zippé
gdalinfo /vsizip/my.zip/my.tif

# lire un fichier accessible en HTTP
gdalinfo /vsicurl/https://github.com/qgis/QGIS-Training-Data/blob/master/exercise_data/forestry/basic_map.tif?raw=true

# lire un fichier zippé accessible en HTTP
ogrinfo /vsizip/vsicurl/https://download.geofabrik.de/south-america/suriname-latest-free.shp.zip

# lire une couche en particulier d'un fichier zippé accessible en HTTP
ogrinfo -ro -al -so /vsizip/vsicurl/https://download.geofabrik.de/south-america/suriname-latest-free.shp.zip/gis_osm_buildings_a_free_1.shp
```

### Utilisons le VSI pour nos données BAL

C'est parti pour notre `ogrinfo` des familles :

```bash
ogrinfo -ro -al -so \
    /vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz
```

Ce qui nous donne :

```bash
INFO: Open of `/vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz'
      using driver `CSV' successful.

Layer name: adresses-33
Geometry: None
Feature Count: 775577
Layer SRS WKT:
(unknown)
id: String (0.0)
id_fantoir: String (0.0)
numero: String (0.0)
rep: String (0.0)
nom_voie: String (0.0)
code_postal: String (0.0)
code_insee: String (0.0)
nom_commune: String (0.0)
code_insee_ancienne_commune: String (0.0)
nom_ancienne_commune: String (0.0)
x: String (0.0)
y: String (0.0)
lon: String (0.0)
lat: String (0.0)
alias: String (0.0)
nom_ld: String (0.0)
libelle_acheminement: String (0.0)
nom_afnor: String (0.0)
source_position: String (0.0)
source_nom_voie: String (0.0)
```

"Mieux faire n'est pas une option" comme dirait M. Barréda, mon instituteur de CE2. Ah bah ça tombe bien, en parlant d'option...

### Le bal des options

![logo GDAL next](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/gdal_next_logo.png "logo GDAL next"){: .img-rdp-news-thumb }

En regardant du côté du [format BAL] qui est bien documenté grâce aux petits soins de l'[AITF] (merci entre autres à Maël Reboux et Chantal Arruti) et de [la documentation GDAL sur les CSV](https://gdal.org/drivers/vector/csv.html#open-options), on peut dès lors améliorer encore un peu les choses :

- demander à GDAL de déterminer les types et la longueur des différents champs
- indiquer que la première ligne est un en-tête
- indiquer les champs à utiliser pour les coordonnées géographiques ([`lat` et `lon` en WGS84](https://github.com/etalab/adresse.data.gouv.fr/blob/master/public/schemas/adresses-csv.md?plain=1#L21-L22)) mais ne pas les garder dans le fichier final

Ce qui donne :

```bash
ogrinfo -ro -al -so \
    -oo AUTODETECT_TYPE=YES \
    -oo AUTODETECT_WIDTH=YES \
    -oo HEADERS=YES \
    -oo X_POSSIBLE_NAMES=lon \
    -oo Y_POSSIBLE_NAMES=lat \
    -oo KEEP_GEOM_COLUMNS=NO \
    /vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz
```

On y gagne certes au change...

```bash hl_lines="5"
INFO: Open of `/vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz'
      using driver `CSV' successful.

Layer name: adresses-33
Geometry: Point
Feature Count: 775577
Warning 1: Value with a width greater than field width found in record 11503 for field nom_voie. This warning will no longer be emitted
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

... mais on s'aperçoit que les types de champs ne sont pas corrects. Par exemple, les champs `code_insee_*` devraient être de type `String` et non `Integer`. De même, les longueurs de champs sont trop liées à ce jeu de données et lèvent des avertissements (ligne 6).

Notez que ça n'est pas bloquant, même pour la conversion :

```bash
ogr2ogr \
    -f GPKG \
    -s_srs 'EPSG:4326' \
    -t_srs 'EPSG:2154' \
    -nln "gironde" \
    -oo AUTODETECT_TYPE=YES \
    -oo HEADERS=YES \
    -oo X_POSSIBLE_NAMES=lon \
    -oo Y_POSSIBLE_NAMES=lat \
    -oo KEEP_GEOM_COLUMNS=NO \
    ban.gpkg \
    /vsigzip//vsicurl/https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-33.csv.gz
```  

Mais on est là pour automatiser et ce serait quand même BALlot de se rajouter du travail post-traitement rébarbatif !

----

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
        <Field name="code_insee" type="string" />
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

### Utiliser le XSD pour valider le schéma

![icône XML](https://cdn.geotribu.fr/img/logos-icones/divers/xml.png "icône XML - XML File by Eucalyp from the Noun Project"){: .img-rdp-news-thumb }

Comme indiqué dans la documentation, le [schéma du format VRT est défini par un XSD](https://github.com/OSGeo/gdal/blob/master/gdal/data/ogrvrt.xsd) ([XML Schema Definition](https://fr.wikipedia.org/wiki/XML_Schema)) qu'il peut être utile d'indiquer dans l'espace de nommage :

```xml
<OGRVRTDataSource
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:noNamespaceSchemaLocation="https://raw.githubusercontent.com/OSGeo/gdal/master/gdal/data/ogrvrt.xsd"
    >
```

Par exemple, si comme moi vous utilisez Visual Studio Code, vous pouvez profiter de l'auto-complétion et de la validation via une extension comme [XML Complete](https://marketplace.visualstudio.com/items?itemName=rogalmic.vscode-xml-complete) :

![VS Code XSD GDAL VRT](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/gdal_bal/vscode_gdal_vrt_help.png "Visual Studio Code - XML Complete"){: .img-center loading=lazy }

----

## Conclusion

![GDAL BAL](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/gdal_bal/gdal_bal.png "GDAL c'est de la BAL"){: .img-center loading=lazy }

Blague à part, en rédigeant ce tuto, je me dis que ce serait pertinent d'intégrer le CSVT aux côtés des CSV téléchargeables :thinking:. Qu'en pensez-vous ? On pourrait le suggérer aux équipes Etalab/ANCT et/ou à l'AITF ?

----

## Auteur

--8<-- "content/team/jmou.md"

{% include "licenses/beerware.md" %}

## Crédits

- nouveau logo GDAL proposé sur ce [ticket GitHub](https://github.com/OSGeo/gdal/issues/2117)
- illustration de [GDAL issue du T-Shirt](https://teespring.com/gdal) par [Joe Morisson](https://twitter.com/mouthofmorrison/status/1326556800997527557?lang=fr)
- [balle de tennis](https://fr.wikipedia.org/wiki/Balle#/media/Fichier:Tennis_ball.svg) de MesserWoland, [CC BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0/), via Wikimedia Commons
- icônes [CSV](https://thenounproject.com/term/csv-file/3148375 ) et [XML](https://thenounproject.com/term/xml/3148395) de Eucalyp from the Noun Project

<!-- Hyperlinks reference -->
[AITF]: https://www.aitf.fr/
[format BAL]: https://schema.data.gouv.fr/etalab/schema-bal/latest.html
