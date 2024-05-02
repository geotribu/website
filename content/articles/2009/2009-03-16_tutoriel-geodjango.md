---
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2009-03-16
description: GeoDjango est une brique supplémentaire du FrameWork Django lui permettant d'étendre les possibilités de ce dernier en autorisant la gestion de champs géométriq...
image: ''
license: default
robots: index, follow
tags:
    - GeoDjango
    - tutoriel
title: Tutoriel GeoDjango
---

# Tutoriel GeoDjango

:calendar: Date de publication initiale : 16 mars 2009

## Préambule

Ce document est une traduction du [tutorial de GeoDjango](http://geodjango.org/docs/tutorial.html). Malgré les efforts réalisés certaines coquilles ou erreurs peuvent s'être glissées. N'hésitez pas à nous contacter pour les corriger.

## Introduction

GeoDjango est une brique supplémentaire du FrameWork Django lui permettant d'étendre les possibilités de ce dernier en autorisant la gestion de champs géométriques et la réalisation de requêtes spatiales.

Afin de comprendre ce tutoriel une bonne connaissance de la logique de Django est nécessaire. Dans le cas contraire une documentation riche ainsi que de nombreux tutoriels et exemples sont disponibles sur le [site officiel](http://www.djangoproject.com/) ou celui en [français](http://www.django-fr.org/).

De plus, l'utilisation de GeoDjango nécessite l'installation de librairies supplémentaires (ex : geos, Gdal...). Pour plus de détails le [tutoriel d'installation de GeoDjango](http://geodjango.org/docs/install.html) est à votre disposition.

Nous aborderons au cours des paragraphes suivants la création de notre premier projet cartographique nous permettant de consulter [les frontières mondiales](http://thematicmapping.org/downloads/world_borders.php)[^1]. Certaines parties ou codes de ce tutoriel sont directement inspirés et/ou tirés du projet [GeoDjango basic apps](http://code.google.com/p/geodjango-basic-apps/)[^2].

## Paramétrages généraux

### Création de la base de données

Avant toute chose il est nécessaire de créer une base de données spatiale sur laquelle s'appuiera notre projet Django. Pour les utilisateurs de [PostgreSQL](http://www.postgresql.org/) et [PostGIS](http://postgis.refractions.net/) les commandes ci-dessous vous permettront d'instancier votre base en utilisant un [template spatial](http://geodjango.org/docs/install.html#spatialdb-template) :

```bash
sudo su - postgres
createdb -T template_postgis -O geo geodjango
exit
```

La commande `createdb` doit être effectuée par un super-utilisateur, dans notre cas postgres, qui possède tous les privilèges. L'option `-O` spécifie que cette nouvelle base appartiendra à l'utilisateur geo. Vous pouvez bien entendu remplacer geo par l'utilisateur de votre choix.

Les bases de données MySQL et Oracle n'ont pas besoin d'effectuer ces étapes ni de créer un template spatial.

### Création de notre projet Django

Comme cela se fait habituellement sous Django et donc sous GeoDjango, commencons par créer notre projet avec la commande `django-admin.py` (plus de détails sur cette commande sur [Django-fr](http://www.django-fr.org/documentation/tutorial01/#cr-ation-d-un-projet)) :

```sh
django-admin.py startproject geodjango
```

Une fois ce projet initialisé, nous allons créer une application nommée world (plus de détails sur cette commande sur [Django-fr](http://www.django-fr.org/documentation/tutorial01/#cr-ation-de-mod-les)).

```sh
cd geodjango
python manage.py startapp world
```

## Configurer le fichier settings.py

La configuration générale de notre projet GeoDjango est définie dans le fichier `settings.py`. Premièrement, commençons par renseigner les paramètres de la base que nous avons créés précédemment :

```p
INSTALLED_APPS
DATABASE_ENGINE = 'postgresql_psycopg2'
DATABASE_NAME = 'geodjango'
DATABASE_USER = 'geo'
```

Profitons-en pour ajouter dans `INSTALLED_APPS` les applications `django.contrib.admin`, `django.contrib.gis`, et `geodjango.world` (l'application que nous avons créé):

```python
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.gis',
    'geodjango.world'
)
```

## Données géographique

### Frontières mondiales

Les données que nous utiliserons dans ce tutoriel sont disponibles [ici au format zip](http://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip). Une fois téléchargées, créez un dossier data à l'intérieur de l'application world et dézippez les.

```bash
mkdir world/data
cd world/data
wget <http://thematicmapping.org/downloads/TM_WORLD_BORDERS-0.3.zip>
unzip TM_WORLD_BORDERS-0.3.zip
cd ../..$ mkdir world/data
```

Le jeu de données est au format ESRI Shapefile, l'un des format les plus populaires dans l'univers du SIG. Une fois dezippé vous devriez trouver dans votre dossier les fichiers suivants :

* .shp : Contient les données géométrique
* .shx : L'index spatial des données contenues dans le .shp
* .dbf : Base de données attributaire
* .prj : Description du système de référence spatial utilisé

### Étudions nos données avec l'utilitaire ogrinfo

La commande `ogrinfo` est idéale pour étudier les metadonnées d'une couche :

```sh
ogrinfo world/data/TM_WORLD_BORDERS-0.3.shp
```

```sh
INFO: Open of `world/data/TM_WORLD_BORDERS-0.3.shp'
using driver `ESRI Shapefile' successful.
1: TM_WORLD_BORDERS-0.3 (Polygon)
```

Ci-dessus, `ogrinfo` nous informe que le shapefile contient une couche de type polygone. En ajoutant les options `-so` nous obtiendrons des informations plus complètes :

```sh
ogrinfo -so world/data/TM_WORLD_BORDERS-0.3.shp TM_WORLD_BORDERS-0.3
```

```sh
INFO: Open of `world/data/TM_WORLD_BORDERS-0.3.shp'
using driver `ESRI Shapefile' successful.

Layer name: TM_WORLD_BORDERS-0.3
Geometry: Polygon
Feature Count: 246
Extent: (-180.000000, -90.000000) - (180.000000, 83.623596)
Layer SRS WKT:
GEOGCS["GCS_WGS_1984",
DATUM["WGS_1984",
SPHEROID["WGS_1984",6378137.0,298.257223563]],
PRIMEM["Greenwich",0.0],
UNIT["Degree",0.0174532925199433]]
FIPS: String (2.0)
ISO2: String (2.0)
ISO3: String (3.0)
UN: Integer (3.0)
NAME: String (50.0)
AREA: Integer (7.0)
POP2005: Integer (10.0)
REGION: Integer (3.0)
SUBREGION: Integer (3.0)
LON: Real (8.3)
LAT: Real (7.3)
```

Pour la partie géométrique les informations disponibles sont le nombre d'entités (256), l'emprise géographique, le système de référence spatial ("SRS WKT"). Pour la partie attributaire de nombreux détails sont disponibles. Par exemple FIPS: String (2.0) indique que FIPS est de type texte et de longueur 2. Toutes ces informations sont également disponibles sur le site [thematicmapping](http://thematicmapping.org/downloads/world_borders.php), néanmoins cela vous permet de comprendre la logique de votre couche cela même si aucune métadonnée n'est fournie.

## Modèle géographique

### Définir un modèle géographique

Maintenant que nous avons étudié nos données grâce à `ogrinfo`, nous pouvons définir et créer notre modèle GeoDjango qui représentera celles-ci. Cela se passe de la manière suivante :

```python
# -*- coding: utf-8 -*-
from django.contrib.gis.db import models

class WorldBorders(models.Model):
# Champs de Django correspondant
# aux attributs du ShapeFile
name = models.CharField(max_length=50)
area = models.IntegerField()
pop2005 = models.IntegerField('Population 2005')
fips = models.CharField('FIPS Code', max_length=2)
iso2 = models.CharField('2 Digit ISO', max_length=2)
iso3 = models.CharField('3 Digit ISO', max_length=3)
un = models.IntegerField('United Nations Code')
region = models.IntegerField('Region Code')
subregion = models.IntegerField('Sub-Region Code')
lon = models.FloatField()
lat = models.FloatField()

# Champs GeoDjango: Champ geometrique (MultiPolygonField),
# et remplacement du manager par défaut par une instance de GeoManager.
mpoly = models.MultiPolygonField()
objects = models.GeoManager()

# Ainsi le model est correctement definit dans admin.
class Meta:
verbose_name_plural = "World Borders"

# Retourne la chaîne de caractère définissant le modèle.
def __unicode__(self):
return self.name
```

Deux points importants à retenir :

1. Le module models est importé de django.contrib.gis.db
2. Le modèle GeoManager surcharge celui par défaut. Ce modèle est requis pour la réalisation des requêtes spatiales

Dans un modèle GeoDjango, lorsque un champ de type géométrique est déclaré le système de référence spatial par défaut est le WGS84 (dont le [SRID](http://en.wikipedia.org/wiki/SRID) est 4326) - Cela signifie que les champs qui contiendront les coordonnées géographiques seront de type longitude/latitude avec bien entendu des degrés comme unité. Bien entendu si vous souhaitez utiliser un système de coordonnés différent, il sera nécessaire de modifier le SRID en conséquence.

## Lancer syncdb

Une fois votre modèle défini, il est nécessaire de synchroniser votre base de données. Tout d'abord, regardons le code SQL qui sera généré par le modèle WorldBorders. Cela se passe grâce à la commande `sqlall` :

```sh
python manage.py sqlall world
```

Le résultat suivant est alors affiché :

```sql
BEGIN;
CREATE TABLE "world_worldborders" (
"id" serial NOT NULL PRIMARY KEY,
"name" varchar(50) NOT NULL,
"area" integer NOT NULL,
"pop2005" integer NOT NULL,
"fips" varchar(2) NOT NULL,
"iso2" varchar(2) NOT NULL,
"iso3" varchar(3) NOT NULL,
"un" integer NOT NULL,
"region" integer NOT NULL,
"subregion" integer NOT NULL,
"lon" double precision NOT NULL,
"lat" double precision NOT NULL
)
;
SELECT AddGeometryColumn('world_worldborders', 'mpoly', 4326, 'MULTIPOLYGON', 2);
ALTER TABLE "world_worldborders" ALTER "mpoly" SET NOT NULL;
CREATE INDEX "world_worldborders_mpoly_id" ON "world_worldborders" USING GIST ( "mpoly" GIST_GEOMETRY_OPS );
COMMIT;
```

Si le résultat vous paraît correct, il faut maintenant créer la base en lancant la commande syncdb :

```sh
python manage.py syncdb
Creating table world_worldborders
Installing custom SQL for world.WorldBorders model
```

La commande `syncdb` vous demandera également de créer un utilisateur administrateur. Vous pouvez bien entendu le faire immédiatement ou sinon plus tard en lancant la commande `createsuperuser`

## Importer des données spatiales

Dans cette partie nous apprendrons comment, grâce a l'utilitaire [LayerMapping](http://geodjango.org/docs/layermapping.html), ajouter les données du fichier shape world_borders dans notre modèle GeoDjango. Il existe différente manière de les importer dans la base de données spatiale. En effet en plus des utilitaires inclues dans GeoDjango vous pourrez également utiliser ceux ci-dessous :

* [ogr2ogr](http://www.gdal.org/ogr/ogr2ogr.html) : Inclue avec Gdal, cet utilitaire en ligne de commande supporte l'import de multiples sources de données vecteurs à l'intérieur de PostGis, MySQL et Oracle.
* [shp2pgsql](http://postgis.refractions.net/documentation/manual-1.3/ch04.html#id2986341) : Cet utilitaire inclue avec PostGis ne supporte que les sources de type ShapeFiles

## L'interface GDAL

Nous avions précédemment utilisé l'utilitaire ogrinfo pour explorer le contenu du ShapeFile world borders. GeoDjango inclue directement la librairie GDAL, vous pourrez donc, depuis l'API Pythonic, explorer tous les types de données supportés par OGR directement .

Premièrement, ouvrons un nouveau Django Shell :

```sh
python manage.py shell
```

Si vous avez dors et déjà téléchargé les données World Borders nous pouvons donc déterminer leur emplacement en utilisant le module python os :

```python
>>> import os
>>> from geodjango import world
>>> world_shp = os.path.abspath(os.path.join(os.path.dirname(world.__file__),
...                             'data/TM_WORLD_BORDERS-0.3.shp'))

```

Nous pouvons maintenant ouvrir les données world borders en utilisant l'interface DataSource de GeoDjango :

``` python
>>> from django.contrib.gis.gdal import *
>>> ds = DataSource(world_shp)
>>> print ds
/ ... /geodjango/world/data/TM_WORLD_BORDERS-0.3.shp (ESRI Shapefile)
```

Les objets de type sources de données peuvent avoir différents types d'objet géographique. Néanmoins, de part leur logique de conception les ShapeFiles n'en n'autorisent qu'un :

```python
>>> print len(ds)
1
>>> lyr = ds[0]
>>> print lyr
TM_WORLD_BORDERS-0.3
```

Il est également possible de connaître le type de géométrie de l'objet ou encore le nombre de données qu'il contient :

```python
>>> print lyr.geom_type
Polygon
>>> print len(lyr)
246
```

Note : malheureusement le format de données ShapeFile n'offre pas une grande spécificité des types de géométrie. Ce ShapeFile comme beaucoup d'autres est de type MultiPolygon. Vous devez faire attention au fait que lors de la création de vos modèles GeoDjango n'acceptera pas une géométrie de type MultiPolygon, c'est pourquoi à la place nous utilisons un MultiPolygonField. Il est possible à partir de GeoDjango de connaître le système de référence spatial associé à la couche, dans ce cas l'attribut `srs` retournera un objet SpatialReference :

```python
>>> srs = lyr.srs
>>> print srs
GEOGCS["GCS_WGS_1984",
DATUM["WGS_1984",
SPHEROID["WGS_1984",6378137.0,298.257223563]],
PRIMEM["Greenwich",0.0],
UNIT["Degree",0.0174532925199433]]
>>> srs.proj4 # PROJ.4 representation
'+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs '
```

Nous apprenons que le système de projection utilisé est le WGS84, les données seront donc en degrés.

En plus des champs géographiques, les shapefiles contiennent également des champs attributaires qui servent à caractériser la donnée. Ci-dessous les champs additionnels de la couche World Border :

```python
>>> print lyr.fields
['FIPS', 'ISO2', 'ISO3', 'UN', 'NAME', 'AREA', 'POP2005', 'REGION', 'SUBREGION', 'LON', 'LAT']
```

Nous allons maintenant examiner le type de donnée associé à chaque champs (est-ce que ce champ est de type chaîne de caractère, nombre entier...)

```python
>>> [fld.__name__ for fld in lyr.field_types]
['OFTString', 'OFTString', 'OFTString', 'OFTInteger', 'OFTString', 'OFTInteger',
'OFTInteger', 'OFTInteger', 'OFTInteger', 'OFTReal', 'OFTReal']
```

Il est possible, par une simple itération, d'accéder aux informations attributaires (avec la méthode get() ) et/ou géographiques (depuis l'attribut geom) de chaque objet :

```python
>>> for feat in lyr:
...    print feat.get('NAME'), feat.geom.num_points
...
Guernsey 18
Jersey 26
South Georgia South Sandwich Islands 338
Taiwan 363
```

La couche peut également être divisée :

``` python
>>> lyr[0:2]
[, ]
```

Chaque objet de la couche peut être retrouvé grâce à son ID :

```python
>>> feat = lyr[234]
>>> print feat.get('NAME')
San Marino
```

Ci-dessous la géométrie de la frontière de San Marino est extraite puis exportée au format WKT et GeoJSON :

```python
>>> geom = feat.geom
>>> print geom.wkt
POLYGON ((12.415798 43.957954,12.450554 ...
>>> print geom.json
{ "type": "Polygon", "coordinates": [ [ [ 12.415798, 43.957954 ], [ 12.450554, 43.979721 ], ...
```

### LayerMapping

Nous allons maintenant explorer un peu plus en profondeur GeoDjango. Pour cela créons un fichier `load.py` dans le dossier contenant l'application world et insérons le code suivant :

```python
# -*- coding: utf-8 -*-
import os
from django.contrib.gis.utils import LayerMapping
from models import WorldBorders

world_mapping = {
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
'mpoly' : 'MULTIPOLYGON',
}

world_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/TM_WORLD_BORDERS-0.3.shp'))

def run(verbose=True):
lm = LayerMapping(WorldBorders, world_shp, world_mapping,
transform=False, encoding='iso-8859-1')

lm.save(strict=True, verbose=verbose)
```

Quelques remarques concernant le code ci-dessus :

* Chaque clé du dictionnaire de données world_mapping correspond à un champ du modèle WorldBorders, les valeurs quant à elles correspondent aux champs du ShapeFile qui sera importé.
* La clé mpoly du champ géométrique est de type MULTIPOLYGON. Ce type géométrique correspond à celui que l'on souhaite stocker. Même si les données que l'on importera seront des polygones simples ils seront automatiquement converti avant d'être insérés dans la base
* Le chemin d'accès au ShapeFiles n'est pas absolu. En d'autres termes, si pour une raison quelconque vous devez par la suite déplacer le dossier contenant votre projet (ainsi que le dossier data) le script continuera de fonctionner.
* Le mot clé transform est défini à False car les données n'ont pas besoin d'être converties dans un système de coordonnées différent. Celles-ci sont déjà en WGS84 (SRID=4326) qui est la projection par défaut de GéoDjango
* Le mot clé encoding correspond à l'encodage des caractères du shapefile. Cela permet d'être sûr que les données seront lues et enregistrées dans le même format que leur système d'encodage original

Maintenant, appellez le Django Shell depuis votre projet GeoDjango :

```sh
python manage.py shell
```

Ensuite, il ne reste plus qu'à importer le module *load*, appeler la méthode run et laisser *LayerMapping* faire le travail :

```python
>>> from world import load
>>> load.run()
```

## Utiliser ogrinspect

Maintenant que nous savons comment définir notre modèle géographique et importer nos données grâce à l'utilitaire *LayerMapping*, nous verrons qu'il est possible d'automatiser cette étape grâce à la commande ogrinspect. En effet cette dernière permet de générer automatiquement le modèle et le dictionnaire LayerMapping associé à la donnée définit en entrée. Cette commande s'utilise de la manière suivante :

```sh
python manage.py ogrinspect <data_source> <model_name> [options]
```

Dans notre exemple, data_source est le chemin d'accès à la donnée et model_bame est le nom qui sera utilisé pour le modèle. Des options supplémentaires, permettant de définir le modèle généré, peuvent également être ajoutées. Ainsi en se basant sur nos données, la commande ci-dessous permettra de produire automatiquement le modèle et le dictionnaire de données WorldBorders :

```sh
python manage.py ogrinspect world/data/TM_WORLD_BORDERS-0.3.shp WorldBorders --srid=4326 --mapping --multi
```

Revenons-sur les options que nous avons ajoutées :

* L'option `--srid=4326` définit le SRID qui sera utilisé
* L'option `--mapping` spécifie à `ogrinspect` de générer également un dictionnaire cartographique qui sera utilisé conjointement à LayerMapping
* L'option `--multi` permet de spécifier que le champ géométrique sera de type MultiPolygonField plutôt que PolygonField

La commande `ogrinspect` retourne le résultat ci-dessous que vous pourrez ensuite être directement copier dans le fichier `models.py` :

```python
# -*- coding: utf-8 -*-
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class WorldBorders(models.Model):
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

# Auto-generated `LayerMapping` dictionary for WorldBorders model
worldborders_mapping = {
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

## Requêtes spatiales

### Interrogation spatiale

GeoDjango étend l'ORM (object-relational mapping) de Django permettant ainsi la réalisation de requêtes spatiales. Prenons un exemple simple où nous souhaiterions connaître l'objet du modèle WorldBorders contenant un point que nous allons créer. Pour cela, commencons par ouvrir notre shell python :

```sh
python manage.py shell
```

Définissons maintenant le point qui nous intéresse [^3] :

```sh
pnt_wkt = 'POINT(-95.3385 29.7245)'
```

La variable `pnt_wkt` correspond à un point de -95.3385 de longitude et 29.7245 degré de latitude. Le format géométrique utilisé est le [Well Known Text](http://en.wikipedia.org/wiki/Well-known_text) (WKT) définit par l'Open Geospatial Consortium (OGC)[^4]. Maintenant que notre point est créé nous allons ajouter notre modèle WorldBorders afin de réaliser une requête spatiale de type Contains qui utilisera `pnt_wkt` comme paramètre.

```python
>>> from world.models import WorldBorders
>>> qs = WorldBorders.objects.filter(mpoly__contains=pnt_wkt)
>>> qs
[]
```

Le résultat renvoyé par notre requête est **United States**. Nous aurions pu également arriver à ce même résultat en se basant cette fois sur la librairie [GEOS](http://geodjango.org/docs/geos.html). Librairie que nous utilisons dans l'exemple ci-dessous mais en réalisant cette fois une requête spatiale de type intersects

```python
>>> from django.contrib.gis.geos import Point
>>> pnt = Point(12.4604, 43.9420)
>>> sm = WorldBorders.objects.get(mpoly__intersects=pnt)
>>> sm
```

Les exemples Contains et Intersects sont juste un aperçu de ce qu'il est possible de réaliser. Vous trouverez une documentation complète en consultant L'[API GeoDjango Database](http://geodjango.org/docs/db-api.html)

## Reprojection automatique

Lors d'une requête spatiale, si les données sont dans des systèmes de coordonnées différents, GeoDjango les reprojette automatiquement. Dans l'exemple ci-dessous nos coordonnées sont exprimées en [EPSG SRID 32140](http://spatialreference.org/ref/epsg/32140/), un système de coordonnées **spécifique uniquement au sud du Texas** et dont les unités de mesure ne sont pas en degrés mais en **mètres**.

```python
>>> from django.contrib.gis.geos import *
>>> pnt = Point(954158.1, 4215137.1, srid=32140)
```

A noter que `pnt` peut également être construit au format EWKT, une extension du format WKT incluant directement le SRID de la couche :

```python
>>> pnt = GEOSGeometry('SRID=32140;POINT(954158.1 4215137.1)')
```

Lorsque vous utilisez l'ORM de GeoDjango celui-ci transforme automatiquement votre requête spatiale en une requête SQl interprétable par votre base de données. Cela permet ainsi de garder un niveau d'abstraction élevé :

```python
>>> qs = WorldBorders.objects.filter(mpoly__intersects=pnt)
>>> qs.query.as_sql() # Generating the SQL
('SELECT "world_worldborders"."id", "world_worldborders"."name", "world_worldborders"."area",
"world_worldborders"."pop2005", "world_worldborders"."fips", "world_worldborders"."iso2",
"world_worldborders"."iso3", "world_worldborders"."un", "world_worldborders"."region",
"world_worldborders"."subregion", "world_worldborders"."lon", "world_worldborders"."lat",
"world_worldborders"."mpoly" FROM "world_worldborders"
WHERE ST_Intersects("world_worldborders"."mpoly", ST_Transform(%s, 4326))',
(,))
>>> qs # printing evaluates the queryset
[]
```

## Lazy géométrie

Pour GeoDjango, la géométrie des objets arrive sous une forme textuelle standardisée. Ainsi pour utiliser un champ géométrique GeoDjango va créer un [objet géométrique GEOS](http://geodjango.org/docs/geos.html) ce qui nous permettra la réalisation de nombreux traitements comme par exemple de pouvoir le transformer dans les formats spatiaux les plus populaires :

```python
>>> sm = WorldBorders.objects.get(name='San Marino')
>>> sm.mpoly

>>> sm.mpoly.wkt # WKT
MULTIPOLYGON (((12.4157980000000006 43.9579540000000009, 12.4505540000000003 43.9797209999999978, ...
>>> sm.mpoly.wkb # WKB (as Python binary buffer)

>>> sm.mpoly.geojson # GeoJSON (requires GDAL)
'{ "type": "MultiPolygon", "coordinates": [ [ [ [ 12.415798, 43.957954 ], [ 12.450554, 43.979721 ], ...
```

Cela inclut également l'accès aux nombreuses opérations géométrique de la librairie GEOS :

```python
>>> pnt = Point(12.4604, 43.9420)
>>> sm.mpoly.contains(pnt)
True
>>> pnt.contains(sm.mpoly)
False
```

## Afficher vos données sur une carte

GeoDjango enrichit également l'interface d'administration originale de Django en autorisant les utilisateurs à créer et modifier les géométries des objets à partir d'une interface cartographique web basée sur openLayers. pour cela créons, dans notre application world,un fichier nommé admin.py et insérons le code suivant :

```python
# -*- coding: utf-8 -*-
from django.contrib.gis import admin
from models import WorldBorders

admin.site.register(WorldBorders, admin.GeoModelAdmin)
```

Ensuite, éditons notre fichier urls.py afin qu'il ressemble à ceci :

```python
from django.conf.urls.defaults import *
from django.contrib.gis import admin

admin.autodiscover()

urlpatterns = patterns('',
(r'^admin/(.*)', admin.site.root),
)
```

Démarrons maintenant le serveur de développement :

Enfin, rendons-nous à l'adresse <http://localhost:8000/admin/> et une fois enregistré vous devriez voir apparaître tout les pays de la couche WorldBorders. Leurs frontières peuvent être éditées, modifiées, déplacées...

## OSMGeoAdmin

Avec OSMGeoAdmin, GeoDjango utilise une couche OpenStreetMap comme couche principale offrant ainsi plus de détails que celle utilisée par défaut par GeoModelAdmin ( basé sur le WMS [Vector Map Level 0](http://earth-info.nga.mil/publications/vmap0.html) distribué par [Metacarta](http://metacarta.com/)). Néanmoins, cela entraîne d'importantes limitations :

* OSMGeoAdmin nécessite l'[ajout de la projection spherical mercator](http://geodjango.org/docs/install.html#addgoogleprojection) à la table spatial_ref_sys de PostGis
* OSMGeoAdmin ne fonctionne pas encore avec les base de données MySQL et Oracle spatial
* Le fichier PROJ.4 doit être installé (consulter les [instructions d'installations de PROJ.4](http://geodjango.org/docs/install.html#proj4) pour plus de détails)

Une fois ces pré-requis réalisés vous n'aurez plus qu'à remplacer, dans votre fichier `admin.py`, `admin.GeoModelAdmin` par `admin.OSMGeoAdmin` :

```python
admin.site.register(WorldBorders, admin.OSMGeoAdmin)
```

----

<!-- geotribu:authors-block -->

<!-- Notes de bas de page -->
[^1]: Un grand merci à Bjørn Sandvik de thematicmapping.org qui propose et entretient ce jeu de données.
[^2]: GeoDjango basic apps a été écrit par Dane Springmeyer, Josh Livni, et Christopher Schmidt.
[^3]: Le point ici correspond à l'université de droit de Houston.
[^4] Open Geospatial Consortium, Inc., OpenGIS Simple Feature Specification For SQL, Document 99-049.
