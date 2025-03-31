---
title: "Installer Python et GDAL sous Windows"
authors:
    - Julien MOURA
categories:
    - article
comments: true
date: 2013-09-26
description: "Installer Python et GDAL sous Windows"
tags:
    - GDAL
    - OGR
    - Python
    - Windows
---

# Installer Python et GDAL sous Windows

:calendar: Date de publication initiale : 26 septembre 2013

Déjà un bout de temps sur GéoTribu et presqu'autant d'idées de tutoriels jamais concrétisées pour diverses raisons (manque de temps, flemme, etc.) et finalement je me suis dit que plutôt que de laisser ce blog mort-né, j'allais m'en servir pour y écrire des penses-bête de manipulations que je fais plus ou moins régulièrement pour d'autres et pour lesquelles il est toujours utile d'avoir un guide pas-à-pas sous la main pour éviter d'oublier un détail.

J'entame par l'installation sous Windows de Python et GDAL, langage et librairie emblématiques dans la géomatique. L'objectif étant de donner aux débutants coincés sur Windows, de quoi accéder aux nombreux tutoriels de [GéoTribu](http://geotribu.net/search/node/python) ou d'ailleurs, par exemple ceux du [PortailSIG](http://www.portailsig.org/search/node/python).

----

Niveau : débutant  
Pré-requis : aucun :wink:

![logo Python](https://cdn.geotribu.fr/img/logos-icones/programmation/python.png "logo Python"){: loading=lazy width=100px }![logo GDAL](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/gdal.png "logo GDAL"){: loading=lazy width=90px }
{: align=middle }

Pour se rappeler d'où vient le nom du langage :

<iframe width="100%" height="315" src="https://www.youtube-nocookie.com/embed/3g-g2yYR6Jk" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Le pourquoi du comment

Sous **Windows** parce-que n'en déplaise aux manchots, l'essentiel des êtres humains ne parle pas machine et que la grande majorité des professionnels utilise Windows et un logiciel SIG fonctionnant uniquement sur ce système (ESRI, MapInfo, GéoConcept, ...). D'ailleurs, même pour ArqGIS et gvSIG, je pense qu'il y a davantage d'utilisateurs sous Windows également.

D'autre part, si Python est aisément installable, il est toujours bon de peaufiner les détails pour travailler confortablement par la suite ; sans parler de GDAL dont l'utilisation indépendante (c'est-à-dire hors des packages du type OSGeo4W) est tout sauf une sinécure. C'est d'ailleurs un sujet récurrent sur [GIS StackExchange](http://gis.stackexchange.com/questions/2276/how-to-install-gdal-with-python-on-windows) et il est donc temps de donner leur chance aux anglophobes.

Il est certes facile de passer par OSGeo4W mais ce n'est pas vraiment intégré au système d'exploitation ni adapté aux usages d'un utilisateur moyen de Windows.

## Installer et configurer Python

Certes, c'est la base et ce n'est vraiment pas compliqué, mais il s'agit de pas manquer d'avoir de bonnes bases.

### Télécharger

La [dernière version de la série des 2.7.x](http://www.python.org/download/releases/2.7.5/) (à ce jour la 2.7.5 donc) et en 32 bits. C'est une recommandation personnelle. D'une part parce-que beaucoup de librairies ne sont toujours pas portées en 3.x et d'autre part pour des soucis de stabilité ou de compatibilité avec certaines dépendances (`arcpy` notamment). L'installation en mode administrateur et complète se déroule normalement sans souci.

### Paramétrer les variables de l'environnement Windows

Objectifs :

* qu'il (Windows) comprenne que les fichiers python (.py et .pyc) sont des programmes à exécuter ;
* pouvoir travailler directement avec la console Windows ;
* indiquer au système où se trouvent les dépendances et librairies quand elles sont appelées par un programme Python.

Assurez-vous donc d’avoir bien `c:\Python27;c:\Python27\Scripts;` à la fin de votre *System PATH*, auquel on accède via : Panneau de Configuration >> Système >> Paramètres systèmes avancés >> Variables d'environnement. Si vous ne savez pas faire, voici [une capture d'écran](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/Python-GDAL-Windows/Axx_VariablesEnvironnement_0.jpg) ou un [lien explicatif](http://sametmax.com/ajouter-un-chemin-a-la-variable-denvironnement-path-sous-windows/)).

![PATH Windows : Python Scripts](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/Python-GDAL-Windows/PATH_Python.jpg "PATH Windows : Python Scripts"){: .img-center loading=lazy }

### Pour les puristes

Redémarrer un coup, ça fait jamais de mal :wink:.

----

## Installer GDAL/OGR

Il y a [plusieurs façons d'installer GDAL/OGR](http://gdal.gloobe.org/install.html#windows) mais celle-ci est la plus "propre" selon moi, la plus adaptée à un usage avec Python et Windows et qui permet surtout de s'assurer de profiter de toutes les possibilités offertes par le couteau-suisse.

Sinon vous pouvez également vous tourner vers les [packages de Christoph Gohlke](http://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal), que je recommande d'ailleurs pour installer d'autres librairies Python.

### Dis-moi quel compilateur tu as et je te dirai quelle version télécharger

La façon la plus simple étant de lancer l'interpréteur fourni avec Python, IDLE de son joli nom :

![Interpréteur Python](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/Python-GDAL-Windows/MSVC_Version.jpg "Interpréteur Python"){: .img-center loading=lazy }

Sachez que si vous le souhaitez, vous pouvez disposer gratuitement de la dernière version des librairies C#/C++ sur Windows en installant [Visual Studio Express](http://www.microsoft.com/visualstudio/fra/downloads).

### Choisir ses installeurs

La librairie est régulièrement mise à jour et doit-être compilée mais heureusement pour nous, il y a des gens qui font un excellent travail de vulgarisation du processus et qui mettent à jour le fruit de leurs efforts.

Saluons donc ici [Tamas Szekeres de GIS Internals](http://szekerest.blogspot.fr/) grâce à qui nous disposons d'installeurs stables et à jour : <http://www.gisinternals.com/sdk/>.

Dans la section `GDAL and MapServer latest release versions`, cliquez sur la ligne correspondant aux caractéristiques de votre système, mises en évidence dans le point précédent. Dans mon cas, il s'agit donc de `MSVC2008 (Win32)`.

### Installer dans le bon ordre

Comme sur la capture :

1. Les fichiers du coeur de GDAL/OGR
2. Les headers Python
3. Les modules optionnels qui pourraient vous intéresser :
    * l'un pour pouvoir accéder aux FileGDB d'ESRI,
    * l'autre pour les fichiers ECW ou encore les MrSID ([format d'images compressées](http://gdal.gloobe.org/gdal/formats/mrsid.html)).
    * D'autres dépendent de licences propriétaires, comme celui d'Oracle.

![Capture d'écran de la partie téléchargement des installeurs sur GIS Internals](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/Python-GDAL-Windows/GISInternalsSDK_GDALdownloads_capture.jpg "Capture d'écran de la partie téléchargement des installeurs sur GIS Internals"){: .img-center loading=lazy }

### Ajouter GDAL aux variables d'environnement

Comme expliqué plus haut pour Python, ajouter à la fin du Path (donc après `c:\Python27\Scripts;` normalement) le chemin vers l'installation de GDAL (a priori : `C:\Program Files (x86)\GDAL`) :

![PATH Windows : dossier d'installation de GDAL](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/Python-GDAL-Windows/PATH_GDAL.jpg "PATH Windows : dossier d'installation de GDAL"){: .img-center loading=lazy }

Attention, certains utilisateurs ont fait remonter des erreurs du type `DLL load failed` et [recommandent](https://stackoverflow.com/a/10010835) de placer le chemin vers GDAL au début de la variable `Path`.

Si vous souhaitez également pouvoir utiliser des outils logiciels développés en Java (comme [Talend Data Integration](http://fr.talend.com/products/data-integration) par exemple), vous pouvez rajouter `C:\Program Files (x86)\GDAL\java` à la suite du Path.

### Créer une nouvelle variable système pour les données de GDAL

Toujours dans la fenêtre des variables d'environnement, cliquez sur "Nouvelle" pour affecter le chemin des données de GDAL, `C:\Program Files (x86)\GDAL\gdal-data` en théorie, à `GDAL_DATA` :

![PATH Windows : dossier des données GDAL](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/Python-GDAL-Windows/Variable_%20GDAL_Data.jpg "PATH Windows : dossier des données GDAL"){: .img-center loading=lazy }

### Répéter pour les modules de GDAL et le dossier des projections

![PATH Windows : dossier d'installation des plugins de GDAL](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/Python-GDAL-Windows/Variable_GDAL_Driver.jpg "PATH Windows : dossier d'installation des plugins de GDAL"){: .img-center loading=lazy }

![Ajout de la variable PROJ_LIB](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/Python-GDAL-Windows/Variable_GDAL_PROJ_LIB.jpg "Ajout de la variable PROJ_LIB"){: .img-center loading=lazy }

### Tester et apprécier

Après avoir redémarré (on n'est jamais trop prudent sous Windows...), ouvrez un terminal Windows (Démarrer >> Exécuter >> cmd) et vérifiez que vous obtenez quelque chose qui ressemble à ça :

![Résultat dans la console Windows](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/Python-GDAL-Windows/ResultatInstallation_PythonGDAL.jpg "Résultat dans la console Windows"){: .img-center loading=lazy }

On peut également tester son installation du côté de l'exécution d'un script et vérifier au passage les pilotes disponibles sur sa machine ([ce script est également sur GitHub](https://github.com/Guts/Metadator/blob/master/test/test_ogr_DriversDispos.py)) :

```python
#-*-coding: utf-8-*-
#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name:         OGR Drivers'availability
# Purpose:      Class to test if GDAL/OGR and their Python bindings are installed
#               and which drivers are installed. Could be imported as a submodule.
#
# Author:        Julien Moura (https://github.com/Guts)
# PyVersion:    2.7.x
# Created:       24/06/2013
# Updated:      16/07/2013
# Licence:        GPL 3
# Credits:        http://pcjericks.github.io/py-gdalogr-cookbook
#-------------------------------------------------------------------------------

################################################################################
######## Libraries import #########
###################################

# 3rd party libraries
try:
  from osgeo import ogr
  print u"Import des modules réussi. tout semble OK : en avant !!\n"
except:
  print u"L'import des modules a échoué. " \
    + "Merci de vérifier votre installation de GDAL/OGR.\n\n"


################################################################################
############# Classes #############
###################################

class OGR_DriversCheck:
    """ Main class """
    def __init__(self):
        """ """

    def check_shp(self):
        u""" Vérifie que le pilote pour les shapes est disponible"""
        driverName = "ESRI Shapefile"
        driver = ogr.GetDriverByName( driverName )
        if driver is None:
            print u"%s : pilote indisponible." % driverName
            return 0
        else:
            print  u"%s : pilote disponible." % driverName
            return 1

    def check_pg(self):
        u"""  Vérifie que le pilote pour PostgreSQL/PostGIS est disponible """
        driverName = "PostgreSQL"
        driver = ogr.GetDriverByName( driverName )
        if driver is None:
            print u"%s : pilote indisponible" % driverName
            return 0
        else:
            print  u"%s : pilote disponible." % driverName
            return 1

    def check_gdb(self):
        u""" Vérifie que le pilote pour les FileGDB (ESRI) est disponible """
        driverName = "FileGDB"
        driver = ogr.GetDriverByName( driverName )
        if driver is None:
            print u"%s : pilote indisponible" % driverName
            return 0
        else:
            print  u"%s : pilote disponible." % driverName
            return 1

    def list_drivers(self):
        u""" Renvoie une liste alphabétique des pilotes disponibles """
        cnt = ogr.GetDriverCount()  # nombre de pilotes disponibles
        driversList = []
        for i in range(cnt):
            driver = ogr.GetDriver(i)
            driverName = driver.GetName()
            if not driverName in driversList:
                driversList.append(driverName)
        # end of function
        return driversList

################################################################################
##### Stand alone execution #######
###################################

if __name__ == '__main__':
    """ Paramètres pour une utilisation en script """
    ogr_check = OGR_DriversCheck()
    ogr_check.check_shp()
    ogr_check.check_pg()
    ogr_check.check_gdb()
    print ogr_check.list_drivers()
```

Qui donne ceci sur ma propre installation (PostgreSQL n'est pas installé) :

```cmd
Import des modules réussi. tout semble OK : en avant !!
ESRI Shapefile : pilote disponible.
PostgreSQL : pilote indisponible.
FileGDB : pilote disponible.
['FileGDB', 'ESRI Shapefile', 'MapInfo File', 'UK .NTF', 'SDTS', 'TIGER', 'S57', 'DGN', 'VRT', 'REC', 'Memory', 'BNA', 'CSV', 'NAS', 'GML', 'GPX', 'KML', 'GeoJSON', 'GMT', 'SQLite', 'ODBC', 'PGeo', 'MSSQLSpatial', 'PCIDSK', 'XPlane', 'AVCBin', 'AVCE00', 'DXF', 'Geoconcept', 'GeoRSS', 'GPSTrackMaker', 'VFK', 'PGDump', 'OSM', 'GPSBabel', 'SUA', 'OpenAir', 'PDS', 'WFS', 'HTF', 'AeronavFAA', 'Geomedia', 'EDIGEO', 'GFT', 'SVG', 'CouchDB', 'Idrisi', 'ARCGEN', 'SEGUKOOA', 'SEGY', 'XLS', 'ODS', 'XLSX', 'ElasticSearch', 'PDF']
```

----

## Le tunning

Histoire de commencer avec le plus de confort de travail possible, voici quelques conseils supplémentaires en vrac :

### D'autres librairies que l'on retrouve très souvent dans l'univers géomatique

* [xlwt](https://pypi.python.org/pypi/xlwt)/[xlrd](https://pypi.python.org/pypi/xlrd), écriture/lecture de fichiers Excel entre autres ;
* les libraires scientifiques [scipy](http://www.lfd.uci.edu/~gohlke/pythonlibs/#scipy) et [numpy](http://www.lfd.uci.edu/~gohlke/pythonlibs/#numpy)
* [PyWin32](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pywin32) pour communiquer avec les APIs Windows
* [matplotlib](http://www.lfd.uci.edu/~gohlke/pythonlibs/#matplotlib) et [basemap](http://www.lfd.uci.edu/~gohlke/pythonlibs/#basemap) pour les graphiques de données
* [PyProj](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyproj) pour un accès à PROJ.4
* [Psycopg](http://www.lfd.uci.edu/~gohlke/pythonlibs/#psycopg) pour PostgreSQL
* [Shapely](http://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely) pour la manipulation facilitée des vecteurs
* [Fiona](http://www.lfd.uci.edu/~gohlke/pythonlibs/#fiona) qui rend GDAL/OGR à la fois plus Pythonnesque et surtout plus humain
* [DateUtil](http://www.lfd.uci.edu/~gohlke/pythonlibs/#python-dateutil)
* [Pillow](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pillow)

### Autres façons d'installer

* Quand un installeur Windows n'est pas disponible, pas de panique, les méthodes classiques de Python (`easy_install`, `pip`, `setup.py`) sont très simples à utiliser (mais sans inscription au registre Windows et donc non désinstallables via le panneau de configuration).

Sur le sujet, je recommande l'excellent tutoriel de Martin Laloux : [Python pour les sigistes](http://www.portailsig.org/content/python-pour-les-sigistes-comment-installer-un-module-externe-geojson-shapely-ou-gdalogr-par-).

### Un vrai terminal

[Console2](http://sourceforge.net/projects/console/). Si vous prenez le temps de le configurer correctement, comme détaillé dans l'article de Sam&Max cité dans les sources, ce petit utilitaire apporte un sacré paquet d'avantages, notamment les commandes [pip (installation et mise à jour facilitées des librairies)](http://www.xavierdupre.fr/blog/2013-05-10_nojs.html).

### Un éditeur de texte sympa

[Notepad++](http://notepad-plus-plus.org/fr/) (polyvalent et généraliste) et [PyScripter](https://code.google.com/p/pyscripter/) (dédié presque uniquement à Python) sont deux bonnes options. [Sublime Text](http://www.sublimetext.com/) ou [PyCharm](http://www.jetbrains.com/pycharm/) si vous avez besoin d'un vrai logiciel de développement.

### Un gestionnaire de version

Comme [GitHub for Windows](https://windows.github.com/) par exemple.

----

## Sources

* Le tutoriel pour GDAL/OGR en anglais sur [Cartometric](http://cartometric.com/blog/2011/10/17/install-gdal-on-windows/)
* L'article pour Python de [Sam&Max](http://sametmax.com/programmer-confortablement-en-python-sous-windows/)
* Les [recettes sur GDAL/OGR](https://pcjericks.github.io/py-gdalogr-cookbook/layers.html)

----

<!-- geotribu:authors-block -->
