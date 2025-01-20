---
title: Exemple des différentes sources de données utilisables par MapServer
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2009-02-15
description: Exemple des différentes sources de données utilisables par MapServer
tags:
    - data
    - MapServer
---

# Exemple des différentes sources de données utilisables par MapServer

:calendar: Date de publication initiale : 15 février 2009

## Introduction

![logo MapServer](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/mapserver.png "logo MapServer"){: .img-thumbnail-left }

Ce tutoriel est une traduction d'un [billet](http://www.bostongis.com/?content_name=umn_datasources#19) parut sur l'excellent site [BostonGis](http://www.bostongis.com/). Au cours de celui-ci, nous apprendrons à utiliser l'une des fonctionnalités les plus intéressantes de MapServer qu'est la possibilité d'accéder à de multiples sources de données. Même si les exemples présentés ont été réalisés avec la version 4.6 de MapServer ils restent applicables pour les versions antérieures.

## Définir le chemin d'accès aux données

La localisation des sources de données telles que Esri Shp ou mapInfo tab sont définies dans le MapFile par le paramètre `SHAPEPATH` comme présenté ci-dessous :

```conf
#
# Debut du MapFile
#

NAME MYMAP

EXTENT  732193.725550 2904132.702662 799614.090681 2971466.288170

SIZE 500 500
SHAPEPATH "c:\mydata\"
:
:
```

## ESRI Shapefile

Les données de type **ShapeFile (*.shp)** sont, dans MapServer, **les plus simples à utiliser**. En effet il suffit, dans le bloc LAYER, de spécifier le nom du fichier Shape (il n'est pas obligatoire d'écrire l'extension). Ci-dessous un exemple de déclaration d'un Layer utilisant une couche ShapeFile :

```conf
LAYER
    NAME buildings
    TYPE POLYGON
    STATUS DEFAULT
    DATA buildings
    PROJECTION
          "init=epsg:2249"
    END
    CLASS
    OUTLINECOLOR 10 10 10
    END
END
```

## MapInfo Tab Files

Grâce au driver GDAL OGR de nombreuses sources de données sont utilisables par MapServer. Les données de type **MapInfo (*.tab)** font partie de celles-là. L'exemple ci-dessous présente la déclaration d'un LAYER utilisant une donnée Mapinfo. Bien entendu, la donnée doit prendre en compte le chemin spécifié auparavant dans le paramètre `SHAPEPATH`.

```conf
LAYER  
  NAME buildings  
  STATUS DEFAULT  
  MINSCALE 7000  
  CONNECTIONTYPE OGR  
  CONNECTION "buildings.tab"  
  TYPE POLYGON  
  PROJECTION  
  "init=epsg:2249"  
  END  
  # -- MapInfo has projection information built in the tab file  
  # -- so you can often auto read this information with the below  
  #PROJECTION  
  # AUTO  
  #END  
  CLASS  
    OUTLINECOLOR 10 10 10  
  END  
END
```

## PostGIS Layer

MapServer dispose de son propre driver permettant l'accès aux données stockées dans le **[SGBD PostGis](http://postgis.refractions.net/)**. Néanmoins, afin de pouvoir utiliser cette fonctionnalité il est nécessaire que le CGI MapServer ou MapScript soit compilé avec le driver PostGis. Ci-dessous un exemple utilisant une couche PostGis :

```conf
LAYER  
  CONNECTIONTYPE postgis  
  NAME "buildings"  
  CONNECTION "user=dbuser dbname=mydb host=myserver"  
  # the_geom column is the name of a spatial geometry field in the table buildings  
  DATA "the_geom from buildings"  
  STATUS DEFAULT  
  TYPE POLYGON  
  # Note if you use a filter statement - this is basically like a where clause of the sql statement  
  FILTER "storyhg > 2"  
  CLASS  
    OUTLINECOLOR 10 10 10  
  END  
END
```

Une couche PostGis plus complexe

```conf
LAYER  
    NAME "projects"  
    CONNECTIONTYPE postgis  
    CONNECTION "user=myloginuser dbname=mydbname host=mydbhost password=mypass"  
    DATA "the_geom FROM (SELECT a.projid, a.projname, a.projtype, a.projyear, a.pid, parc.the_geom  
          FROM projects a INNER JOIN parcels parc ON a.parcel_id = parc.pid  
          WHERE a.projyear = 2007) as foo USING UNIQUE projid USING SRID=2249"  
    STATUS OFF  
    TYPE POLYGON  
    CLASS  
      NAME "Business Projects"  
      EXPRESSION ('[projtype]' = 'Business')  
      STYLE  
        OUTLINECOLOR 204 153 51  
        WIDTH 3  
    END  
    END  
    CLASS  
      NAME "Community Projects"  
      EXPRESSION ('[projtype]' = 'Community')  
      STYLE  
        OUTLINECOLOR 204 0 0  
        WIDTH 3  
    END  
    END

    PROJECTION  
    "init=epsg:2249"  
    END  
    METADATA  
        "wms_title" "Projects"  
        "wfs_title" "Projects"  
        gml_include_items "all"  
        wms_include_items "all"  
    END  
    DUMP TRUE  
    TOLERANCE 10  
END  
```

## WMS Layer

MapServer peut utiliser le protocole **[WMS](http://geotribu.net/node/9)** aussi bien en tant que serveur que client. Ci dessous un exemple de couche WMS utilisant le server WMS Microsoft Terraservices.

```conf
LAYER  
    NAME "msterraservicedoq"  
    TYPE RASTER  
    STATUS DEFAULT  
    CONNECTION "http://terraservice.net/ogcmap.ashx?"  
    CONNECTIONTYPE WMS  
    MINSCALE 3000  
    MAXSCALE 20000  
    #DEBUG ON  
    METADATA  
      "wms_srs" "EPSG:26919"  
      "wms_name" "doq"  
      "wms_server_version" "1.1.1"  
      "wms_format" "image/jpeg"  
      "wms_style" "UTMGrid_Cyan"  
      "wms_latlonboundingbox" "-71.19 42.23 -71 42.40"  
    END  
END
```

----

<!-- geotribu:authors-block -->
