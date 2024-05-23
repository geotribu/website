---
title: Utiliser OGR avec python
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2009-10-18
description: Utiliser OGR avec python
tags:
    - Python
    - OGR
---

# Utiliser OGR avec python

:calendar: Date de publication initiale : 18 octobre 2009

## Introduction

Gdal qui signifie "**G**eospatial **D**ata **A**bstraction **L**ibrary" est une bilbitothèque écrite en C++ permettant de lire, écrire et manipuler les principaux formats de données utilisés dans le monde du SIG et du géospatial (SIG-Web).  

En plus des nombreux utilitaires en ligne de commande, elle propose des interfaces de programmation pour les langages suivants : Perl, Python, VB6, Java, Ruby; C# /.Net.

Ce tutoriel permettra d'aborder l'API python de GDAL-OGR au travers d'exemples concret, nous n'utiliserons pour le moment qu'OGR (données vecteurs). Les bases essentielles seront présentées ainsi que la logique de construction des objets. Si vous découvrez quelques erreurs ou une écriture non pythonique, n'hésitez pas à me le faire remarquer.

## Premiers pas

La première chose à faire est bien évidemment d'installer gdal-ogr ainsi que son api python. Etant sur Ubuntu, je suis passé par un simple apt-get. Pour les Ubuntu géomaticien il existe également un dépôt regroupant les dernières versions des librairies : [UbuntuGIS](https://launchpad.net/~ubuntugis/+archive/ubuntugis-unstable)

Pour plus d'informations, je vous conseille la lecture du [trac de python pour Gdal/Ogr](http://trac.osgeo.org/gdal/wiki/GdalOgrInPython). Vous y trouverez notamment de nombreux exemples et particulièrement ceux de [Chris Garrard](http://www.gis.usu.edu/~chrisg/python) et de [Greg Petrie](http://cosmicproject.org/OGR).

Une fois l'installation faite vous devriez être en mesure d'appeler directement les classes GDAL-OGR en python. Pour cela, ouvrez une console et tapez l'instruction suivante :

`~$ python`

L'interpréteur python devrait alors se lancer. Il ne nous reste plus qu'à appeler les classes :

```python
Python 2.4.4 (#2, Oct 22 2008, 19:52:44)  
[GCC 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)] on linux2  
Type "help", "copyright", "credits" or "license" for more information.  
>>> from osgeo import gdal  
>>> from osgeo import ogr
```

:warning: L'appel des packages pour la nouvelle version se fait dorénavant avec le préfixe osgeo. Dans les versions antérieures, la notation était de ce type :

```python
>>> import gdal  
>>> import ogr
```

Nous avons maintenant les bases pour commencer réellement à travailler. Passons donc à l'exploration de nos données

## Ouverture d'un fichier Shape

Premièrement commençons par télécharger nos données. Pour ce tutoriel, j'ai utilisé celles de la [National GeoSpatial-Intelligence Agency](https://www1.nga.mil/Pages/Default.aspx) qui propose, au format ShapeFile, la [localisation des ports dans le monde](http://www.nga.mil/MSISiteContent/StaticFiles/NAV_PUBS/WPI/WPI_Shapefile.zip).

La logique de l'API Gdal-OGR se décompose en 3 étapes. Tout d'abord **l'identification du Driver** à utiliser. Dans notre cas cela sera le format Esri Shapefile. Ensuite équipé du bon driver, la **sélection de la source de données**. Cette source, selon les formats, peut être composée de plusieurs couches. Le format Shape ne contenant qu'une seule couche il n'est pas nécessaire de spécifier le numéro de couche à utiliser (0 par défaut). Enfin, une fois la couche identifiée, il est possible de **manipuler les données**.

Voici représenté schématiquement l'enchainement des étapes à réaliser :

![PyGIS - Schéma](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/Pygisde_001.jpg "PyGIS - Schéma"){: .img-center loading=lazy }

Source : [PyGis](http://www.pygis.de/index.php/GDAL)

Passons maintenant au code :

```python
>>> import ogr  
>>> driver = ogr.GetDriverByName("ESRI Shapefile")  
>>> datasource = driver.Open("Documents/gis_data/Port_mondiaux/WPI.shp")  
>>> layer = datasource.GetLayer() #equivalent a datasource.GetLayer(0)  
>>> dir(layer)  
['CommitTransaction', 'CreateFeature', 'CreateField', 'DeleteFeature', 'Dereference', 'GetExtent', 'GetFeature', 'GetFeatureCount', 'GetFeaturesRead', 'GetLayerDefn', 'GetName', 'GetNextFeature', 'GetRefCount', 'GetSpatialFilter', 'GetSpatialRef', 'Reference', 'ResetReading', 'RollbackTransaction', 'SetAttributeFilter', 'SetFeature', 'SetNextByIndex', 'SetSpatialFilter', 'SetSpatialFilterRect', 'StartTransaction', 'SyncToDisk', 'TestCapability', '__doc__', '__init__', '__len__', '__module__', '_o']`
```

La méthode [GetDriveByName()](http://www.gdal.org/ogr/classOGRSFDriverRegistrar.html#d214c51c2e38d486388f77fb9314143c) va à partir de la classe [DriverRegistrar](http://www.gdal.org/ogr/classOGRSFDriverRegistrar.html) instancier un nouvel objet nous permettant de lire les données dont le format à été spécifié en argument.

Ensuite nous accédons concrètement à notre couche via la méthode [GetLayer()](http://www.gdal.org/ogr/classOGRDataSource.html#618c2fdb1067c9357ca2de9fa6cd5962) qui nous retourne alors un objet de type [layer](http://www.gdal.org/ogr/classOGRLayer.html).

La méthodes `dir()` et utilisé en exemple, elle fait partie des classes natives python. Celle-ci permet de lister les méthodes de l'objet passé en paramètre. Ici nous l'appliquons à l'objet layer.

## Lecture d'un fichier Shape

Nous pouvons maintenant accéder aux propriétés de notre fichier ShapeFile. Nous allons ci-dessous afficher successivement le nom du fichier, ainsi que l'extent et le nombre de données :

```python
>>> print layer.GetName()  
WPI  
>>> print layer.GetExtent()  
(-178.1333333, 179.3666667, -77.849999999999994, 78.916666669999998)  
>>> print layer.GetFeatureCount()  
4275
```

## Accéder aux informations de la couche

Pour avoir plus d'informations sur notre couche nous allons utiliser la méthode [GetLayerDefn()](http://www.gdal.org/ogr/classOGRLayer.html#80473bcfd11341e70dd35bebe94026cf). Ensuite, pour connaitre le nom des champs, nous utiliserons la méthode [GetFieldDefn()](http://www.gdal.org/ogr/classOGRFeatureDefn.html#43b95ce699bbca73acb453cc959378e7). Celle-ci retourne le champs dont l'index est passé en argument. Au moyen d'une simple boucle, nous allons afficher le nom des 10 premiers champs :

```python
>>> layerDef= layer.GetLayerDefn()  
>>> i=0  
>>> while i < 10 :  
... layerDef.GetFieldDefn(i).GetName()  
... i=i+1  
...  
'WORLD_PORT'  
'REGION_IND'  
'MAIN_PORT_'  
'WPI_COUNTR'  
'LATITUDE'  
'LONGITUDE'  
'PUBLICAT_1'  
'CHART'  
'HARBOR_SIZ'  
'HARBOR_TYP'
```

## Accéder aux données

Maintenant que nous avons accédé à la couche et aux champs, il ne nous reste plus qu'a consulter les données contenues. Pour cela nous utiliserons la méthode `GetFeature()` qui créé un pointeur vers l'objet géographique spécifié en index. Affichons le nom des dix premiers ports :

```python
>>> for i in range(10) :  
... print layer.GetFeature(i).GetFieldAsString("MAIN_PORT_")  
...  
NANOK  
ESKIMONAES  
SCORESBY SUND  
KEFLAVIK  
STRAUMSVIK  
HAFNARFJORDUR  
SKERJAFJORDUR  
REYKJAVIK  
GRUNDARTANGI  
BORGARNES
```

## Conclusion

Les exemples ci-dessus ne sont qu'un très faible aperçu des possibilités de l'API python de GDAL-OGR. SEn effet, il est également possible de créer et/ou supprimer des couches, créer de nouveaux champs... Cela fera surement l'objet d'un prochain tutoriel.

----

<!-- geotribu:authors-block -->
