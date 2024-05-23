---
title: GeoDjango pas à pas
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2009-04-14
description: Ce tutoriel fait suite à une [première présentation de GeoDjango](http://geotribu.net/node/96). Il se veut plus concis et vous permettra d'appréhender ce framew...
tags:
    - GeoDjango
    - tutoriel
---

# GeoDjango pas à pas

:calendar: Date de publication initiale : 14 avril 2009

Ce tutoriel fait suite à une [première présentation de GeoDjango](http://geotribu.net/node/96). Il se veut plus concis et vous permettra d'appréhender ce framework d'une manière plus directe. Nous aborderons également plus en détails l'interrogation des données.

## Création du projet

La création d'un nouveau projet se fait via la commande shell startproject (documentation complète sur [Django-fr](http://www.django-fr.org/documentation/django-admin/)):

`django-admin startproject geoDjangoBasic`

Cette commande a pour effet de construire l'arborescence de fichiers nécessaires. Ces derniers sont (src [Django-fr](http://www.django-fr.org/documentation/tutorial01/#cr-ation-d-un-projet)):

* `__init__.py` : Un fichier vide que dit à Python que ce répertoire doit être considéré comme un paquetage Python
* `manage.py` : Un outil en ligne de commande que vous permet d'intéragir avec ce projet Django de différentes manières
* `settings.py` : Fichier de configuration de ce projet Django
* `urls.py` : Les déclarations d'URLs pour ce projet Django ; il s'agit d'une « table des matières » de votre site géré par Django.

### Paramétrage du fichier settings.py

Avant d'aller plus loin, il est nécessaire que nous renseignons un peu notre fichier `settings.py` et notamment la partie correspondant à la base de données utilisée. Pour une explication complète reportez-vous à ce [précédent tutoriel](http://geotribu.net/node/96#Configurerlefichiersettingspy), si la base que vous utilisez est de type PostGis il sera nécessaire que vous réalisiez également [cette étape](http://geotribu.net/node/96#Crationdelabasededonnes). N'oublions pas également d'ajouter le package `django.contrib.gis` dans `INSTALLED_APPS`. Profitons également pour nous avancer et ajouter toujours dans `INSTALLED_APPS` l'application que nous allons créer au chapitre suivant : `geoDjangoBasic.geoData`. De manière imagée, nous avons construit les fondations de notre bâtiment. Il reste maintenant à monter les murs, c'est ce que nous allons faire en créant notre application.

## Création de l'application

La création d'une application se déroule en plusieures étapes. Il sera nécessaire tout d'abord d'initialiser celle-çi à partir de Django, pour ensuite définir le modèle correspondant à nos données pour enfin les importer dans notre base.

### Amorce de la structure

Pour créer notre application django dispose d'un utilitaire disponible à partir du fichier manage.py. La commande à réaliser dans un shell est la suivante :

`python manage.py startapp geoData`

Ceci a pour effet de créer à nouveau une nouvelle arborescence de fichier :

* `__init__.py` : Un fichier vide qui dit à Python que ce répertoire doit être considéré comme un paquetage Python
* `models.py` : Décrit ou contient les données manipulées par l'application
* `views.py` : Interface avec laquelle l'utilisateur agit. Sa première tâche est de présenter les résultats renvoyés par le modèle

Nous retrouvons ici l'architecture de Django basée sur une logique Modèle-Vue-Contrôleur (plus de détails dans [Wikipedia](http://fr.wikipedia.org/wiki/Mod%C3%A8le-Vue-Contr%C3%B4leur)).

### Structuration du modèle de données

Nous utiliserons [les données disponibles](http://thematicmapping.org/downloads/TM_WORLD_BORDERS_SIMPL-0.3.zip) sur le site [thematicmapping.org](http://thematicmapping.org/). Il existe différentes manières de déterminer le modèle décrivant les données que nous allons importer. Nous utiliserons la manière qui me semble la plus simple, ogrinspect. La commande est la suivante :

`python manage.py ogrinspect geoData/data/TM_WORLD_BORDERS_SIMPL-0.3.shp GeoModel --srid=4326 --mapping --multi`

Celle-çi analyse les données et renvoie le modèle et le dictionnaire de données correspondant :

```python
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class GeoModel(models.Model):
  fips = models.CharField(max_length=2)
  iso2 = models.CharField(max_length=2)
  iso3 = models.CharField(max_length=3)
  un = models.IntegerField()
  name = models.CharField(max_length=50)
  area = models.IntegerField()
  pop2005 = models.IntegerField()
  region = models.IntegerField()
  subregion = models.IntegerField()
  lon = models.FloatField()
  lat = models.FloatField()
  geom = models.MultiPolygonField(srid=4326)
  objects = models.GeoManager()

  # Auto-generated `LayerMapping` dictionary for GeoModel model
  geomodel_mapping = {
  'fips' : 'FIPS',
  'iso2' : 'ISO2',
  'iso3' : 'ISO3',
  'un' : 'UN',
  'name' : 'NAME',
  'area' : 'AREA',
  'pop2005' : 'POP2005',
  'region' : 'REGION',
  'subregion' : 'SUBREGION',
  'lon' : 'LON',
  'lat' : 'LAT',
  'geom' : 'MULTIPOLYGON',
  }
```

Copions la classe GeoModel dans le fichier `models.py` de notre application :

```python
from django.db import models
from django.contrib.gis.db import models

class GeoModel(models.Model):
 fips = models.CharField(max_length=2)
 iso2 = models.CharField(max_length=2)
 iso3 = models.CharField(max_length=3)
 un = models.IntegerField()
 name = models.CharField(max_length=50)
 area = models.IntegerField()
 pop2005 = models.IntegerField()
 region = models.IntegerField()
 subregion = models.IntegerField()
 lon = models.FloatField()
 lat = models.FloatField()
 geom = models.MultiPolygonField(srid=4326)
 objects = models.GeoManager()
```

Lançons maintenant la commande `sqlall` puis `syncdb` du fichier `manage.py`. La première vous permettra de consulter le code SQL qui sera généré tandis que la seconde va créer concrètement les champs dans la base.

```sql
BEGIN;
CREATE TABLE "geoData_geomodel" (
    "id" serial NOT NULL PRIMARY KEY,
    "fips" varchar(2) NOT NULL,
    "iso2" varchar(2) NOT NULL,
    "iso3" varchar(3) NOT NULL,
    "un" integer NOT NULL,
    "name" varchar(50) NOT NULL,
    "area" integer NOT NULL,
    "pop2005" integer NOT NULL,
    "region" integer NOT NULL,
    "subregion" integer NOT NULL,
    "lon" double precision NOT NULL,
    "lat" double precision NOT NULL
)
;
SELECT AddGeometryColumn('geoData_geomodel', 'geom', 4326, 'MULTIPOLYGON', 2);
ALTER TABLE "geoData_geomodel" ALTER "geom" SET NOT NULL;
CREATE INDEX "geoData_geomodel_geom_id" ON "geoData_geomodel" USING GIST ( "geom" GIST_GEOMETRY_OPS );
COMMIT;
```

```sh
Creating table geoData_geomodel
Installing custom SQL for geoData.GeoModel model
```

## Import des données dans la base

Maintenant que nous avons préparé notre projet et notre application, structuré notre base il ne nous reste plus qu'à importer nos données. Pour cela nous utiliserons la classe LayerMapping de GeoDjango. Nous allons donc créer un fichier `load.py` et y ajouter le code suivant :

```python
import os
from django.contrib.gis.utils import LayerMapping
from models import GeoModel

# Auto-generated "LayerMapping" dictionary for GeoModel model
import os
from django.contrib.gis.utils import LayerMapping
from models import GeoModel

# Auto-generated `LayerMapping` dictionary for GeoModel model
geomodel_mapping = {
    'fips' : 'FIPS',
    'iso2' : 'ISO2',
    'iso3' : 'ISO3',
    'un' : 'UN',
    'name' : 'NAME',
    'area' : 'AREA',
    'pop2005' : 'POP2005',
    'region' : 'REGION',
    'subregion' : 'SUBREGION',
    'lon' : 'LON',
    'lat' : 'LAT',
    'geom' : 'MULTIPOLYGON',
}

world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/TM_WORLD_BORDERS_SIMPL-0.3.shp'))

def run(verbose=True):
    lm = LayerMapping(GeoModel, world_shp, geomodel_mapping,
                      transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
```

Nous retrouvons ci-dessus le dictionnaire de données que nous avons généré précédemment. Il ne reste plus ensuite qu'à instancier la classe [LayerMapping](http://geodjango.org/docs/layermapping.html) et sa méthode `save()`. Revenons à notre console shell et appelons notre fichier `load.py` :

```sh
$ python manage.py shell
>>> from world import load
>>> load.run()
```

Et voilà, nous avons intégré l'ensemble du fichier shape dans notre base de données. Juste par précaution verifions que l'import s'est bien passé. Cela nous permettra par la même occasion de manipuler l'API de la base de données de Django Et GeoDjango.

## interrogation des données

En plus des possibilités offertes par Django, GeoDjango enrichit considérablement l'API initiale concernant la base de données en permettant la réalisation d'interrogations et requêtes spatiales. Explorons un peu nos données. pour cela, ouvrons une console python (`$ python manage.py shell`) et exécutons les commandes suivantes :

```python
>>> from geoDjangoBasic.geoData.models import GeoModel
>>> from django.contrib.gis.gdal import *
>>>
>>> featz = GeoModel.objects.all()
>>> for i in featz :
...    print i.name
...
Antigua and Barbuda
Algeria
Azerbaijan
Albania
[...]
Guernsey
Jersey
South Georgia South Sandwich Islands
Taiwan
>>>
>>>
>>>feat = GeoModel.objects.get(name='Algeria')
>>>print feat.area
238174
>>>
>>>
>>> featPopSup = GeoModel.objects.filter(pop2005__gt=1000000000)
>>> for i in featPopSup :
...    print i.name
...
China
India
>>>
>>>
>>> gmlfeat = featz.gml()
>>> print gmlfeat[0].gml
<gml:MultiPolygon srsName="EPSG:4326"><gml:polygonMember><gml:Polygon><gml:outerBoundaryIs><gml:LinearRing><gml:coordinates>-61.686668,17.0244410000002 -61.887222,17.105274 -61.7944489999999,17.1633300000001 -61.686668,17.0244410000002</gml:coordinates></gml:LinearRing></gml:outerBoundaryIs></gml:Polygon></gml:polygonMember><gml:polygonMember><gml:Polygon><gml:outerBoundaryIs><gml:LinearRing><gml:coordinates>-61.7291719999999,17.608608 -61.853058,17.5830540000001 -61.873062,17.7038880000001 -61.7291719999999,17.608608</gml:coordinates></gml:LinearRing></gml:outerBoundaryIs></gml:Polygon></gml:polygonMember></gml:MultiPolygon>
>>>
>>>
```

## En résumé

Pour finir, ci-dessous est présenté un "road book" des différentes étapes nécessaires à la mise en place d'un projet GeoDjango :

1. Création du projet : Cmd django-admin startproject
2. Paramétrage du fichier settings.py
3. Création de l'application : Cmd manage.py startapp
4. Structuration du modèle de données : Cmd manage.py ogrinspect
5. Copie du modèle dans le fichier models.py de l'application
6. Génération de la table correspondant au modèle dans la BDD : manage.py syncdb
7. Import des données SIG dans la base : LayerMapping

----

<!-- geotribu:authors-block -->
