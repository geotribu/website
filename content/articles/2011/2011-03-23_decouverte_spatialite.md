---
title: "A la découverte de Spatialite"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2011-03-23
description: "A la découverte de Spatialite"
tags:
    - database
    - open source
    - SpatiaLite
---

# A la découverte de Spatialite

:calendar: Date de publication initiale : 23 mars 2011

![logo SpatiaLite](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/spatialite.png "logo SpatiaLite"){: .img-thumbnail-left }

Cela fait plusieurs mois que j'avais envie de jouer un peu avec [spatialite](http://www.gaia-gis.it/spatialite/). Malheureusement, les impératifs et les architectures des projets sur lesquels je travaille ne me laissaient pas forcément beaucoup de temps pour découvrir de nouveaux horizons. C'est pourquoi, profitant d'un peu de temps libre, j'ai décidé de me pencher sur cette base de données.

Spatialite est une surcouche spatiale ajoutée à [SQLite](http://www.sqlite.org/) tout comme [PostGIS](http://postgis.refractions.net/) à [PostgreSQL](http://www.postgresql.org/). Contrairement aux bases de données classiques qui se basent sur une architecture client-serveur, SQLite est directement intégré aux applications. Toutes les données et informations sont stockées au sein d'un fichier accessible via des [API spécifiques](http://www.sqlite.org/cvstrac/wiki?p=SqliteWrappers) ([python](http://docs.python.org/library/sqlite3.html), [java](http://www.ch-werner.de/javasqlite/), [php](http://php.net/manual/fr/book.sqlite.php)). Du fait de ses caractéristiques et de sa légèreté elle a été rapidement adoptée comme moteur de référence dans tous les systèmes embarqués (iPhone, Android) mais aussi pour des programmes tels que Firefox, Skype etc. De plus, fait assez rare dans le monde de l'OpenSource, celle-ci dispose d'une [documentation riche](http://www.gaia-gis.it/spatialite-2.4.0-4/spatialite-cookbook-fr/index.html) sur laquelle s'appuyer.

Pour plus de détails, je vous conseille la lecture de l'excellent article de Martin Laloux sur le [PortailSIG](http://www.portailsig.org/content/sqlite-spatialite-le-pourquoi-du-comment). Mais, ne perdons pas plus de temps et partons immédiatement à la découverte de spatialite.

## Installation et premiers pas

### Installation

La magie d'Ubuntu fait que toute l'installation se fait en quelques secondes. Juste le temps de lancer Synaptic et de vérifier que les paquets sont disponibles. D'autres architectures et des extensions sont bien évidemment disponibles sur le site de [Spatialite](http://www.gaia-gis.it/spatialite/binaries.html).

### Premiers pas avec le terminal

L'accès aux bases de données SQLite et Spatialite peut se faire de différentes façons. Commençons par la plus courante, la ligne de commande via un terminal. Et là premiers déboires ! J'essaye tout d'abord de charger spatialite en tant qu'extensions de SQLite comme indiqué dans les différents tutoriels. Malheureusement, j'obtiens un erreur de segmentation.

```bash
sqlite> .load 'libspatialite.so.2'  
Erreur de segmentation  
```

Deuxième option, je tente alors un appel direct à spatialite. Là tout semble fonctionner et j'effectue donc ma première requête :

![Terminal, query Spatialite](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/terminal_query_spatialite.png "Terminal, query Spatialite"){: .img-center loading=lazy }

Bon, la ligne de commande c'est bien, mais cela ne serait pas mieux de disposer d'une interface à la [PGAdmin](http://www.pgadmin.org/) ? Rassurez-vous cela existe, abordons cela immédiatement.

### Premiers pas avec l'interface

Contrairement aux librairies, le GUI de spatialite n'est pas disponible dans les dépôts d'Ubuntu. [Téléchargeons](http://www.gaia-gis.it/spatialite-2.4.0-4/spatialite_gui-linux-x86-1.4.0.tar.gz) le programme et une fois décompressé lançons le immédiatement. Fait positif, il ne nécessite aucune installation. Fait négatif, j'obtiens tout d'abord un message d'erreur :

```bash
arnaud@arnaud:~/App/spatialite_gui-linux-x86-1.4.0/bin$ ./spatialite_gui  
./spatialite_gui: error while loading shared libraries: libgeos-3.0.0.so: cannot open shared object file: No such file or directory  
```

Cela ne semble pas bien méchant, c'est juste un appel à une librairie qui n'existe pas. Je fais un `locate libgeos qui m'indique que la version de geos que j'ai est la 3.2.2. Un simple`ln -s` devrait régler le problème :

`sudo ln -s /usr/lib/libgeos-3.2.2.so /usr/lib/libgeos-3.0.0.so`

Je tente une nouvelle fois de lancer le GUI qui s'ouvre cette fois correctement. Je charge alors un fichier Shapefile puis j'ouvre ensuite ma base avec QGIS pour vérifier que cela fonctionne :

![Interface graphique de spatialite](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/spatialite_gui.png "Interface graphique de spatialite"){: .img-center loading=lazy }

![Visualisation des données dans QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/qgis_spatialite.png "Visualisation des données dans QGIS"){: .img-center loading=lazy }

Tout semble parfait. Mettons maintenant les mains dans le cambouis et voyons comment associer programmation et spatialite.

## Programmer avec Spatialite

Comme nous l'avons déjà souligné, Sqlite et donc spatialite dispose de [nombreux "wrappers"](http://www.sqlite.org/cvstrac/wiki?p=SqliteWrappers) rendant ainsi possible l'utilisation de différents langages de programmation. Pour notre exemple, notre choix s'est porté sur la librairie [pysqlite](http://code.google.com/p/pysqlite/). Des lectures que j'ai pu faire, il semblerait que sqlite3 directement intégré à l'API python soit identique à pysqlite. Dans les faits, certaines fonctions ne sont pas disponibles dont celle que nous allons utiliser et qui permet de charger des extensions. Pour l'affichage des résultats c'est la librairie OpenLayers qui a été choisie. Arrêtons de tourner autour du pot et passons directement au code :

```python
# !/usr/bin/env python  

# -*- coding: UTF-8 -*-

from pysqlite2 import dbapi2 as sqlite  
import simplejson

def index():  
    conn = sqlite.connect("/var/www/geotribu/applications/tutoriaux/spatialite/WORLD.sqlite")  
    conn.enable_load_extension(True)  
    conn.execute('SELECT load_extension("/usr/lib/libspatialite.so.2.1.0")')  
    conn.enable_load_extension(False)  
    cursor = conn.cursor()  
    cursor.execute('SELECT "NAME", "AREA", AsText(SimplifyPreserveTopology("Geometry", 0.1)) AS GEOM FROM "TM_WORLD_BORDERS-0.3" WHERE "NAME" LIKE "France"')  
    fieldnames = [name[0] for name in cursor.description]  
    result = []  
    for row in cursor.fetchall():  
        rowset = []  
    for field in zip(fieldnames, row):  
        rowset.append(field)  
        result.append(dict(rowset))  
    cursor.close()  
    return simplejson.dumps(result)
```

Le code n'est pas très compliqué à comprendre je pense. La seule subtilité est le résultat que nous transformons au format JSON afin de pouvoir le manipuler plus facilement.

```javascript
function init() {  
  map = new OpenLayers.Map('map',{controls:[new OpenLayers.Control.MouseDefaults(), new OpenLayers.Control.LayerSwitcher()]});  
  ol_wms = new OpenLayers.Layer.WMS( "OpenLayers WMS","http://labs.metacarta.com/wms/vmap0?", {layers: 'basic'});  
  var vectorCountry = new OpenLayers.Layer.Vector("query result");  
  map.addLayers([ol_wms, vectorCountry]);  
  map.setCenter(new OpenLayers.LonLat(18.632,14.414));  
  map.zoomTo(3);

  function success(req){  
    JSONresponse = new OpenLayers.Format.JSON().read(req.responseText);  
    WKTreader = new OpenLayers.Format.WKT;  
    geom = WKTreader.read(JSONresponse[0].GEOM);  
    vectorCountry.addFeatures([geom]);  
  }

  function failure(){  
    alert("error during the process");  
  }

  var uri = '../spatialite2/getCountry.py';  
  var request = new OpenLayers.Ajax.Request(uri, {  
    method: 'get',  
    contentType: 'text/xml',  
    onComplete: success,  
    onFailure: failure  
  }  
);  
}  
```

Là aussi rien d’exceptionnel ! L'objet request est chargé d'effectuer la requête vers notre script python. Si tout s'est bien passé c'est la fonction success() qui est alors appelée. Celle-ci affiche ensuite la géométrie de la France comme cela est illustré par la copie d'écran ci-dessous :

![Spatialite - France](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/france_spatialite.png "Spatialite - France"){: .img-center loading=lazy }

## Conclusion

L'utilisation de SQLite et de Spatialite m'a impressionné par sa simplicité. Le fait de disposer d'une base de données "portable" que l'on peut déplacer à sa guise et intéressant. La question de spatialite comme futur remplaçant du format shapefile avait été soulevée dans la sphère géomaticienne. Même si [James Fee](http://www.spatiallyadjusted.com/2010/09/16/spatialite-is-not-the-shapefile-of-the-future/) ne semble pas lui accorder beaucoup de crédits, je trouve l'idée élégante. En effet, cela permettrait de disposer d'un format d'échange utilisable aussi bien dans le domaine des SIG bureautiques que des interfaces cartographiques web.

## Ressources complémentaires

- [Portail SIG : Python et les bases de données geospatiales](http://www.portailsig.org/content/python-les-bases-de-donnees-geospatiales-1-traitement-classique-principes-et-problemes)  
- [Portail SIG : SQLite - Spatialite le pourquoi du comment](http://www.portailsig.org/content/sqlite-spatialite-le-pourquoi-du-comment)

----

<!-- geotribu:authors-block -->
