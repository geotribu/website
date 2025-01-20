---
title: 'API Python de FME : comment travailler avec des rasters et GDAL'
authors:
    - Humbert FIORINO
categories:
    - article
    - tutoriel
comments: true
date: 2022-08-02
description: Comment travailler avec des librairies Python dans FME. Illustration avec GDAL.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/fme_gdal_raster/fme_gdal_python.png
license: default
tags:
    - FME
    - GDAL
    - Python
    - raster
---

# API Python de FME : comment travailler avec des rasters et GDAL

:calendar: Date de publication initiale : 2 août 2022

## Introduction

![logo FME](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/FME.png "logo FME"){: .img-thumbnail-left }

FME Workbench est un fantastique ETL, très populaire dans la communauté de la géomatique. Il permet d'assembler par de simples "glisser/déposer" dans une interface graphique des "transformateurs" opérant sur toutes sortes de flux de données (fichiers, bases de données, services web, etc.). Avec ces transformateurs, on réalise les opérations classiques d'un SIG, d'une base de données : sélection de données attributaires, jointures spatiales, modification du style d'une couche vectorielle, etc.

![Workspace FME](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/fme_gdal_raster/fme_screenshot.png "Workspace FME"){: .img-center loading=lazy }

L'intérêt de FME est qu'on peut concevoir un workflow structuré, documenté, automatisable et ré-utilisable de transformateurs en mode "plug & play", en ajoutant ou en retirant les transformateurs puis en les interconnectant par des flux de données. Mais, bien que la bibliothèque de transformateurs soit très fournie, il est parfois impossible de trouver son bonheur ! On doit alors faire appel à ses propres librairies ou utiliser des librairies externes open-source.

Par exemple, il n'y a pas de moyen simple de générer des rasters de proximité dans FME, alors que c'est un jeu d'enfant avec la ligne de commande `gdal_proximity.py` de la librairie GDAL. Dans un raster de proximité, à partir de pixels cibles, par exemple des routes dans l'exemple ci-dessous, on produit des pixels dont les valeurs représentent les distances minimales à ces pixels cibles. Dans le cas des routes, le raster de proximité peut ainsi servir de carte d'exposition aux nuisances engendrées par ces routes (bruit, pollution etc.)

![Raster de proximité](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/fme_gdal_raster/gdal_proximity.png "Raster de proximité"){: .img-center loading=lazy }

La question est donc : comment obtenir le même résultat avec FME Workbench ?

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Le transformateur `PythonCaller`

![icône Python](https://cdn.geotribu.fr/img/logos-icones/programmation/python.png "logo Python"){: .img-thumbnail-left }

Une possibilité consiste à utiliser le transformateur `PythonCaller` qui permet de créer son propre transformateur à partir d'un script Python et d'importer la librairie [GDAL](https://gdal.org/tutorials/). J'ai mis en ligne [le "template" FME](http://blog.fiorino.fr/wp-content/uploads/2022/05/TransportationRoads.fmwt) correspondant à cet article.

Dans ce template, les transformateurs sont reliés séquentiellement, à la suite les uns des autres. Tout d'abord, le "lecteur" `TransportationRoads` ouvre un geopackage contenant la couche vectorielle des routes. `FeatureColorSetter` change ensuite la couleur des routes dans une couleur différente du noir. C'est un détail important car la prochaine étape consiste à rasteriser avec `ImageRasterizer` les routes avec des pixels différents de 0 (valeur du noir).

La partie marrante commence avec `PythonCaller` et l'utilisation de la fonction `ComputeProximity` de l'API Python de GDAL.

```python
import fmeobjects
import numpy as np
from osgeo import gdal
```

Si nécessaire, la [documentation FME](https://docs.safe.com/fme/html/FME_Desktop_Documentation/FME_Desktop/Workbench/Installing-Python-Packages.htm) explique comment installer des packages Python, mais `osgeo` et `numpy` sont normalement installés par défaut.

----

## Stocker les données de la bande raster

La classe Python suivante est principalement un copier/coller de la documentation [Python FME API](http://docs.safe.com/fme/html/fmepython/getting_started.html#working-with-rasters). J'ai juste changé le type de tuile en `FMEUInt16Tile` afin d'être compatible avec l'interprétation du raster dans `ImageRasterize` (Gray16).  
En ce qui concerne la classe elle-même, la documentation de FME est un peu laconique. Cette classe est utilisée pour stocker les données de la bande raster ainsi que pour caractériser la manière dont ses données peuvent être renvoyées avec la méthode `getTile`.

```python hl_lines="26"
class MyBandTilePopulator(fmeobjects.FMEBandTilePopulator):
    """
    This is a subclass of the FMEBandTilePopulator superclass.
    It will be used when data is requested to create a new tile and
    and populate it to a new FMEBand.
    """
    def __init__(self, rasterData):
        self._rasterData = rasterData

    # required method
    def clone(self):
        """
        This method is used to create a copy of the data
        multiple times while creating a new band
        """
        return MyBandTilePopulator(self._rasterData)

    # required method
    def getTile(self, startRow, startCol, tile):
       """
       Creates a new tile that's sized based on the input tile.
       Populates that tile using this populator's raster data beginning
       at the startRow and startCol.
       """
       numRows, numCols = tile.getNumRows(), tile.getNumCols()
       newTile = fmeobjects.FMEUInt16Tile(numRows, numCols)
       data = newTile.getData()
       for row in range(startRow, startRow + numRows):
           for col in range(startCol, startCol + numCols):
               if row < len(self._rasterData) and col < len(self._rasterData[0]):
                   data[row - startRow][col - startCol] = self._rasterData[row][col]
       newTile.setData(data)
       return newTile
```

----

## Passer les données de bande de FME à GDAL pour créer le raster de proximité

![logo GDAL](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/gdal.png "logo GDAL"){: .img-thumbnail-left }

L'entrée de `PythonCaller` est le raster à une bande contenu dans l'objet FME `feature` et que s'échangent les transformateurs. Cette bande possède de nombreuses propriétés telles que la taille des pixels (`SpacingX` et `SpacingY`) en mètres dans le système de coordonnées projeté choisi, les coordonnées d'origine de la bande (`originX` et `originY`) et sa taille (`numRows` et `numCols`).

Dans cette partie de code, les lignes suivantes sont très importantes et, à ma connaissance, non documentées dans l'API de FME :

```python
tile = fmeobjects.FMEGray16Tile(numRows, numCols)
bandData = band.getTile(0, 0, tile).getData()
```

Elles permettent d'obtenir les données de la bande en définissant une tuile ayant la même taille que la bande. Le reste est conforme à la documentation de GDAL. Les données des bandes sont placées dans un tableau `Numpy` (conformément à la documentation GDAL) et deux fichiers, `raster_transportation_roads.tiff` et `proximity_transportation_roads.tiff` sont générés dans le dossier du template de FME. Ceci n'est pas obligatoire mais pratique pour vérifier la transformation des données. Pour calculer le raster de proximité, j'utilise la fonction `ComputeProximity` de GDAL (celle qui est utilisée dans le script `gdal_proximity.py`), et je place les données correspondantes dans la liste Python `rasterData` (`ReadAsArray` retourne un tableau `Numpy`).

```python hl_lines="29 30 59"
class FeatureProcessor(object):
    def __init__(self):
        self.rasterData = []

    def input(self, feature):

        self.sysRef = feature.getCoordSys()
        raster = feature.getGeometry()
        rp = raster.getProperties()
        band = raster.getBand(0)

        bp = band.getProperties()
        print("=== FME Input Raster ===")
        print("Coordinate System = " + self.sysRef)
        self.pixelWidth = rp.getSpacingX()
        print("pixelWidth = " + str(self.pixelWidth))
        self.pixelHeight = rp.getSpacingY()
        print("pixelHeight = " + str(self.pixelHeight))
        self.originX = rp.getOriginX()
        print("originX = " + str(self.originX))
        self.originY = rp.getOriginY()
        print("originY = " + str(self.originY))
        numRows = rp.getNumRows()
        print("numRows = " + str(numRows))
        numCols = rp.getNumCols()
        print("numCols = " + str(numCols))
        print("===")

        tile = fmeobjects.FMEGray16Tile(numRows, numCols)
        bandData = band.getTile(0, 0, tile).getData()
        array = np.array(bandData)

        driver = gdal.GetDriverByName('GTiff')
        num_of_bands = 1
        print("Creating file raster_transportation_roads.tiff")
        srcRaster = driver.Create('raster_transportation_roads.tiff', numCols, numRows, num_of_bands, gdal.GDT_UInt16)
        srcRaster.SetGeoTransform((self.originX, self.pixelWidth, 0, self.originY, 0, self.pixelHeight))
        srcBand = srcRaster.GetRasterBand(1)
        srcBand.WriteArray(array)
        srcBand.FlushCache()
        srcBand = None
        srcRaster = None

        src_ds = gdal.Open('raster_transportation_roads.tiff')
        geotransform = src_ds.GetGeoTransform()
        srcBand = src_ds.GetRasterBand(1)
        print("Origin = ({}, {})".format(geotransform[0], geotransform[3]))
        print("Pixel Size = ({}, {})".format(geotransform[1], geotransform[5]))
        print("===")

        print("Creating file proximity_transportation_roads.tiff with GDAL")
        dst_filename='proximity_transportation_roads.tiff'
        drv = gdal.GetDriverByName('GTiff')
        dst_ds = drv.Create(dst_filename, numCols, numRows, num_of_bands, gdal.GetDataTypeByName('UInt16'))
        dst_ds.SetGeoTransform(geotransform)  
        dst_ds.SetProjection(src_ds.GetProjectionRef())
        dstBand = dst_ds.GetRasterBand(1)

        gdal.ComputeProximity(srcBand, dstBand, ["DISTUNITS=PIXEL"])
        self.rasterData = dstBand.ReadAsArray().tolist()

        dstBand.FlushCache()
        dstBand = None
        srcBand = None
        print("===")
```

----

## Création du raster de sortie à partir du raster de proximité

Dans cette dernière partie du code Python, je crée un nouveau raster avec les mêmes propriétés que le raster initial. Je remplis une nouvelle bande avec les données de proximité et je la rattache au raster. La sortie de `PythonCaller` est ensuite générée par la méthode `pyoutput(feature)` et le raster de proximité ainsi produit peut être utilisé par d'autres transformateurs du workflow.

```python
def close(self):

        # creating the raster data and specifying the formatting of the new raster
        rasterData = self.rasterData


        # specifying all of the properties for the new FMERaster
        numRows, numCols = len(rasterData), len(rasterData[0])
        xCellOrigin, yCellOrigin = 0.5, 0.5
        xSpacing, ySpacing = self.pixelWidth, self.pixelHeight
        xOrigin, yOrigin = self.originX, self.originY
        xRotation, yRotation = 0.0, 0.0

        # creating the new FMERaster
        rasterProperties = fmeobjects.FMERasterProperties(numRows, numCols,
                                                          xSpacing, ySpacing,
                                                          xCellOrigin, yCellOrigin,
                                                          xOrigin, yOrigin,
                                                          xRotation, yRotation)
        raster = fmeobjects.FMERaster(rasterProperties)

        # Populating the contents of the band and appending it to the raster
        bandTilePopulator = MyBandTilePopulator(rasterData)
        bandName = ''
        bandProperties = fmeobjects.FMEBandProperties(bandName,
                                                      fmeobjects.FME_INTERPRETATION_UINT16,
                                                      fmeobjects.FME_TILE_TYPE_FIXED,
                                                      numRows, numCols)
        band = fmeobjects.FMEBand(bandTilePopulator, rasterProperties,
                                  bandProperties)
        raster.appendBand(band)

        # creating a new feature with the FMERaster geometry to be output
        feature = fmeobjects.FMEFeature()
        feature.setGeometry(raster)
        feature.setCoordSys(self.sysRef)
        self.pyoutput(feature)

    def process_group(self):
        """When 'Group By' attribute(s) are specified, this method is called
        once all the FME Features in a current group have been sent to input().

        FME Features sent to input() should generally be cached for group-by
        processing in this method when knowledge of all Features is required.
        The resulting Feature(s) from the group-by processing should be emitted
        through self.pyoutput().

        FME will continue calling input() a number of times followed
        by process_group() for each 'Group By' attribute, so this
        implementation should reset any class members for the next group.
        """
        pass
```

!!! note "Traduction d'un article"
    Une version préliminaire en anglais de cet article a été initialement publiée sur mon [blog](https://blog.fiorino.fr).

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
