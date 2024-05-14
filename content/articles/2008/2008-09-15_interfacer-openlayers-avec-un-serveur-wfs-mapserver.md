---
title: Interfacer OpenLayers avec un serveur WFS (MapServer)
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-09-15
description: Interfacer OpenLayers avec un serveur WFS (MapServer)
tags:
    - WFS
    - MapServer
---

# Interfacer OpenLayers avec un serveur WFS (MapServer)

:calendar: Date de publication initiale : 15 septembre 2008

## Introduction

Ce tutoriel vous permettra d'appréhender au mieux la notion de serveur WFS puis de la mettre en application au moyen d'un exemple concret en vous basant sur MapServer et OpenLayers.

- Qu'est-ce que la norme WFS et comment elle fonctionne  
- Faire de MapServer un serveur WFS  
- Afficher une carte WFS avec OpenLayers

## Qu'est-ce que la norme WFS et comment elle fonctionne

Contrairement au format WMS (Web Map Service) orienté image (carte), le format WFS (Web Feature Service) permet au moyen d'une URL formatée d'interroger des serveurs cartographique afin de manipuler des objets géographiques.

Ce protocole initié par l'[Open Géospatial Consortium (OGC)](http://www.opengeospatial.org/standards/wfs "OGC") est devenu un standard implémenté par la quasi-totalité des serveurs cartographiques. L'objectif du WFS est de permettre un accès en édition aux données géographiques afin de pouvoir les modifier, les créer ou les supprimer.

L'interrogation d'un serveur WFS se fait via une URL envoyée au serveur à laquelle sont passés des arguments bien définis. Ces mots-clés une fois mis bout à bout forment un ensemble compréhensible par le serveur cartographique.

Pour un serveur cartographique le seul paramètre obligatoire est (associé à une opération de type GetFeature) :

- **NAME** : nom de la couche à interroger.

Mais il en existe d'autres telles que :

- **BBOX** : Etendue des données
- **VERSION** : version du protocole
- **SERVICE** : Type de service à utiliser (WFS)
- **SRS** : Projection utilisée

Les différentes opérations qu'il est possible de réaliser sont les suivantes :

- **GetCapabilities** : Description des capacités du serveur WFS. Il indiquera les type de données ainsi que les opérations supportées sur chacune d'entre elles.
- **DescribeFeatureType** : Description de la structure de la donnée.
- **GetFeature** : Récupère un (ou les) objet géographique de la couche. Il est également possible de spécifier l'objet désiré au travers de requête attributaire ou spatiale.
- **GetGmlObject** : A web feature service may be able to service a request to retrieve element instances by traversing XLinks that refer to their XML IDs. In addition, the client should be able to specify whether nested XLinks embedded in returned element data should also be retrieved.
- **Transaction** : Support des requêtes transactionnelles. Une transaction peut être composée d'un ensemble d'opérations sur les objets (création, modification, mise à jour, suppression).
- **LockFeature** : Possibilité de bloquer l'accès à un objet géographique durant une transaction par la pose d'un verrou.

En se basant sur les opérations ci-dessus, il est possible de classer les serveurs WFS en 3 catégories :

- **Basic WFS** : Celui-ci doit, au moins, implémenter les opérations suivantes : GetCapabilities, DescribeFeatureType and GetFeature operations.
- **XLink WFS** : Celui-ci doit, en plus des opérations d'un Serveur WFS basique, supporter l'opération GetGmlObject
- **WFS Transactionnel** : Celui-ci doit, en plus des opérations d'un Serveur WFS basique, apporter un support transactionnel. Même si cela n'est pas obligatoire, il pourra également être capable de réaliser des opérations de type GetGmlObject et/ou LockFeature opérations

Voici un exemple d'URL :

[http://localhost/cgi-bin/mapserv?map=/var/www/html/wms/africa.map&**typename**=Africa&**SERVICE**=WFS&**VERSION**=1.0.0&  **REQUEST**=GetFeature&**SRS**=EPSG%3A4326&**BBOX**=-67.851625,-85.0776875,107.929625,108.2816875](http://localhost/cgi-bin/mapserv?map=/var/www/html/wms/africa.map&typename=Africa&SERVICE=WFS&VERSION=1.0.0&REQUEST=GetFeature&SRS=EPSG%3A4326&BBOX=-67.851625,-85.0776875,107.929625,108.2816875)

Une application WFS est composée de 3 parties essentielles : le **serveur cartographique**, les **données** et le **client**.

Un exemple de requête serait la suivante : une requête de type "GetFeature" est envoyée par le navigateur au serveur cartographique. Celui-ci, en fonction de sa configuration et des données vérifie la validité de cette requête en fonction de sa configuration et des données qu'il possède; ensuite, celui-ci retourne le ou les objets géographiques demandés.

![Image WFS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2008/wfs.png "Image WFS"){: loading=lazy }
{: align=middle }

## Faire de MapServer un serveur WFS

Cette partie suppose que vous soyez déjà familier de l'environnement MapServer et que vous sachiez comment est constitué un MapFile. Dans le cas contraire, je vous invite à lire auparavant ce tutoriel : [Tutorial MapServer](2008-08-22_initiation-a-mapserver.md).

Pour spécifier à MapServer de fonctionner en tant que serveur WMS, il sera nécessaire d'ajouter différents attributs à votre MapFile. Les blocs à modifier sont les suivants :

- Un dans le bloc Web
- Trois dans le bloc Layer
    - Le bloc Metadata
    - Le bloc Projection
    - L'attribut Dump

Pour le bloc **Web** il faut ajouter un sous bloc nommé `METADATA` qui est composé des éléments ci-dessous :

```conf
WEB  
  METADATA  
  "wfs_title" "WFS Demo Server"  
  "wfs_onlineresource" "localhost/cgi-bin/mapserv?map=/pathToMapFile/africa.map&?" ## Recommended  
  "wfs_srs" "epsg:4326" ## Recommended  
  END  
END
```

Ensuite pour chaque **couche** il faudra ajouter deux blocs, le premier est obligatoire contrairement au second qui est optionnel mais fortement recommandé ainsi qu'un troisième attribut `DUMP` :

```conf
LAYER  
  METADATA  
    ### WFS  
    "wfs_title" "Africa"  
    "gml_featureid" "NAME"  
    "gml_include_items" "all"  
  END  
  PROJECTION  
    "init=epsg:4326" ##recommended  
  END  
  DUMP TRUE  
  ...  
END
```

Pour un aperçu plus global vous pouvez également [télécharger le MapFile](http://geotribu.net/applications/tutoriaux/tuto_wms_wfs/wms_wfs/africa.map "MapFile") qui a servi pour ce tutoriel.

## Afficher une carte WFS avec OpenLayers

Pour interroger un serveur WFS vous devrez utiliser la classe OpenLayers.Layer.WFS.  

Celle-ci prend en arguments obligatoires l'URL du serveur cartographique ainsi que le nom de la couche. Cela se fait de la manière suivante :

```javascript
africaWFS = new OpenLayers.Layer.WFS(  
"Africa WFS", "http://pathToMapServ/cgi-bin/mapserv?map=/pathToMapFile/africa.map&",  
{typename: 'Africa'},  
{ extractAttributes: true}  
);
```

A noter que si vous désirez pouvoir utiliser les données attributaires de la couche vous devrez ajouter la propriété `extractAttributes` (true).

## Exemple avec une carte de l'Afrique

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/tuto_wms_wfs/wms_wfs/ol_wfs.htm" width="100%" height="700px" frameborder="0"></iframe>`

----

<!-- geotribu:authors-block -->
