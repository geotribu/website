---
title: "Interfacer OpenLayers avec un serveur WMS (MapServer/Geoserver)"
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-08-22
description: "Interfacer OpenLayers avec un serveur WMS (MapServer/Geoserver)"
tags:
    - GeoServer
    - MapServer
    - OpenLayers
---

# Interfacer OpenLayers avec un serveur WMS (MapServer/Geoserver)

:calendar: Date de publication initiale : 22 août 2008

## Introduction

![Logo OpenLayers](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/openlayers.png){: .img-thumbnail-left }

Ce tutorial vous permettra d'appréhender au mieux la notion de serveur WMS puis de le mettre en application ensuite au moyen de deux exemples concrets en se basant sur MapServer et GéoServer. L'affichage sera ensuite géré par OpenLayers.

- Qu'est-ce que la norme WMS et comment elle fonctionne
- Faire de MapServer un serveur WMS
- Faire de GéoServer un serveur WMS
- Afficher une carte WMS avec OpenLayers

## Qu'est-ce que la norme WMS et comment elle fonctionne

WMS qui signifie "Web Map Service" est un protocole défini par l'Open Geospatial Consortium (OGC) permettant au moyen d'une URL formatée d'interroger des serveurs cartographiques et d'obtenir ainsi des cartes géoréférencées.

Ce protocole est devenu un standard implémenté par la quasi-totalité des serveurs cartographiques tels que MapServer, GeoServer, ArcGis Server... Côtè client, de nombreuses applications permettent l'interrogation de ces services : OpenLayers, GoogleMap, PMapServer, MapGuide OS...

Comme nous l'avons rapidement abordé, l'interrogation d'un serveur WMS se fait par l'URL à laquelle est passée des arguments bien définis. Ces mots-clés une fois mis bout à bout forment un ensemble compréhensible par le serveur cartographique. Les différents paramètres possibles sont :

- VERSION : Version du protocole WMS.
- REQUEST : Types d'opérations possibles -> GetCapabilities, GetMap, GetFeatureInfo.
- OUTPUTFORMAT : Format de sortie de l'image (exemple : image/png).
- BBOX : Etendue de la carte.
- WIDTH : Largeur de l'image.
- HEIGHT : Hauteur de l'image.
- LAYERS : Liste des couches désirées.
- SRS : Système de projection utilisé.

Voici un exemple d'URL :

```plain
http://map.ngdc.noaa.gov/servlet/com.esri.wms.Esrimap?servicename=glacier&WMTVER=1.0&request=GetMAP&SRS=EPSG:4326&BBOX=-100,-90,100,80&WIDTH=400&HEIGHT=400&LAYERS=Continents,Rivers,Glaciers%20(all%20sizes)&STYLES=&FORMAT=image/png
```

Un serveur WMS est composé de 3 parties essentielles : le serveur cartographique, les données et le client. Un exemple de reque serait la suivante : une requête de type "GetMap" est envoyée par le navigateur au serveur cartographique. Celui-ci, en fonction de sa configuration et des données, retourne la carte correspondante.

## Faire de MapServer un serveur WMS

Cette partie suppose que vous soyez déjà familier de l'environnement MapServer et que vous sachiez comment est constitué un MapFile. Dans le cas contraire, je vous invite à lire auparavant ce tutorial : Tutorial MapServer.

Pour spécifier permettre à MapServer de fonctionner en tant que serveur WMS, il sera nécessaire d'ajouter trois éléments à votre MapFile. Un dans le bloc Web, et deux pour chacune des couches que vous souhaitez rendre disponible. Pour le bloc Web il faut ajouter un sous bloc nommé METADATA qui est composé des éléments ci-dessous :

```conf
METADATA
  "wms_title" "WMS Demo Server"
  "wms_onlineresource" "localhost/cgi-bin/mapserv?map=path_to_mapfile/demo.map&"
  "wms_srs" "epsg:4326"
  "wms_format" "image/png"
END
```

Ensuite pour chaque couche il faudra ajouter deux blocs, le premier est obligatoire contrairement au second qui est optionnel mais fortement recommandé

```conf
METADATA
  "wms_title" "Commune" ##required
END
PROJECTION
  "init=epsg:4326" ##recommended
END
```

Pour un aperçu plus global vous pouvez également télécharger le MapFile qui a servi pour ce tutorial

## Faire de GéoServer un serveur WMS

GeoServer ne nécessite aucune modification. Il propose de base un service WMS. Pour ajouter des données à GeoServer je vous conseille la lecture de ce tutorial : Ajouter des Shape dans GéoServer

## Afficher une carte WMS avec OpenLayers

Il existe différentes classes permettant l'interrogation de serveur WMS via OpenLayers. Mais elles se basent toutes sur le même mécanisme que l'on a étudié durant la première partie.

Nous devons tout d'abord spécifier le début de l'URL, ensuite nous lui passons les différents paramètres souhaités. Cela se fait de la manière suivante :

### Pour GeoServer

```javascript
 // Layer GeoServer
 Alea_volcanisme = new OpenLayers.Layer.WMS(
  "Risque Sismique - Untiled", "http://server_path:8080/geoserver/wms,
  {
   srs: 'EPSG:4326',
   width: '588',
   styles: '',
   height: '550',
   layers: 'topp:risque_sismique',
   transparent:"true",
   format: 'image/png'
  }
   {singleTile: true, opacity: 0.5, isBaseLayer : false}
 );
```

### Pour MapServer

```javascript
 // Layer MapServer
 Alea_volcanisme = new OpenLayers.Layer.WMS(
  "Volcanisme", "http://localhost/cgi-bin/mapserv?map=path_To_MapFile/mFile.map&",
  {
   srs: 'EPSG:4326',
   width: '800',
   styles: '',
   height: '550',
   layers: 'Alea_volcanisme',
   transparent:"true",
   format: 'image/png'
  }
   {singleTile: true, opacity: 0.5, isBaseLayer : false}
 );
```

Ne disposant pas de serveur personnel tous les tests ont été effectués en local. La copie d'écran ci-dessous, qui est une représentation des risques sismiques et volcaniques à La Réunion, vous donnera néanmoins un aperçu de ce qu'il est possible de réaliser. Les données utilisées sont disponibles sur le site Internet de La [Diren de La Réunion](http://www.reunion.ecologie.gouv.fr/).

![Réunion risque](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2008/reunion_risque.jpg "Réunion risque"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->
