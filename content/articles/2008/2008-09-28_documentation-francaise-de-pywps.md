---
title: Documentation française de PyWPS
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-09-28
description: Documentation française de PyWPS
tags:
    - PyWPS
---

# Documentation française de PyWPS

:calendar: Date de publication initiale : 28 septembre 2008

## Mise en oeuvre d'OGC WPS norme : PyWPS

Jachym Cepicky

Copyright (c)2006-2009 PyWPS Development Team Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. A copy of the license is included in the section entitled "GNU Free Documentation License".

In this file, you can found the description of installation and configuration of PyWPS script. At the and, you can learn, how to add your own process. This document describes most recent version of PyWPS (2.0.0), available in subversion respository.

PyWPS project has been started on April 2006 with support of DBU - Deutsche Bundesstiftung Umwelt1 and with help of GDF-Hannover2 and Help Service Remote Sensing companies. Initial author is Jachym Cepicky.  

## Sommaire

- Introduction
- Fonctionnement
- Installation rapide
- Remarques générales
- Installation
    - Installation rapide et ~~sale~~ facile
    - Installation propre

- Configuration
- Configurer vos propres processus
    - Processus d'Initialisation et de configuration
    - Programmation du processus
    - Utilisater GRASS

- Testez votre processus

## Introduction

PyWPS (Service Web en Python) est une implémentation de la norme Web Processing Service (WPS) 1.0.x définie par l'Open Geospatial Consortium (OGC).

Ce projet débuté en Mai 2006 et supporté par le [DBU](http://dbu.de) offre un environnement permettant la programmation de processus pouvant être ensuite utilisé par tout un chacun.

L'avantage principal de PYWps est qu'il a été écrit de manière à pouvoir utiliser nativement les fonctions du logiciel SIG GRASS permettant ainsi un accès facilité aux différents modules de ce dernier directement depuis une interface Web.

Néanmoins, ce n'est pas le seul logiciel supporté, l'utilisation de programmes tels que le package R, GDAL ou PROJ est également possible.

Etant écrit en python, vous devrez également utiliser ce langage pour vos propres processus.

- Site internet : [http://pywps.wald.intevation.org](http://pywps.wald.intevation.org)
- Wiki : [http://pywps.ominiverdi.org/wiki](http://pywps.ominiverdi.org/wiki)

## Fonctionnement

PyWPS est une application s'interfaçant entre plusieurs clients (Navigateur internet, Environnement SIG, ligne de commande...) pouvant utiliser l'ensemble des outils à disposition sur le serveur. PyWPS ne traite pas lui-même les données il utilise pour cela des applications externes telles que GRASS, GDAL, PROJ, R...

## Installation rapide

1. Installer PyWPS
2. IMPORTANT : Rebaptisez les fichiers originaux (processus, fichiers de configuration) avec le suffixe .py-dist en .py.
3. Editez les fichiers de configuration localisés dans le répertoire pywps/etc/. Voir la page [*] pour plus de détails.
4. Créer ou éditer le fichier `__ init __.py` localisé dans le répertoire pywps/processes. Ajouter le ou les processus disponibles dans le tableau `__all__`.
5. Ajouter vos processus dans le répertoire pywps/processes. Voir la page [*] pour plus de détails.
6. Lancez PyWPS avec la commande ./wps.py, voir la page [*] pour plus de détails.

## Bugs et limitation connus

- La traduction ne fonctionne par pour les requêtes de type GetCapabilities. elles ne fonctionnent que pour les requêtes de type DescribeProcess
- Si les paramètres en entrée sont des valeurs littérales de type chaîne de caractère (string) cela peut causer des problèmes de sécurité. Une attention particulière doit donc être apportée aux paramètres d'entrée et surtout faite attention à ne pas les utiliser directement dans vos script afin d'éviter à votre serveur d'être attaqué.

Si vous rencontrez un nouveau bugs ou une nouvelle limitation n'hésitez pas à la faire remonter via la mailing-list ou le bug tracker de pywps.

## Installation

### Paquets obligatoires

- Python
- Python-xml
- Python-htmltmpl

### Paquets recommandés

- Un serveur du Web (par exemple [Apache](http://httpd.apache.org))
- [GRASS](http://grass.itc.it). Application SIG OpenSource fournissant plus de 350 modules d'analyses de données vecteurs et/ou rasters. PyWPS a été écrit afin de supporter nativement GRASS et ses fonctions.
- [PROJ.4](http://proj.maptools.org) Bibliothèque de projections cartographiques employée dans projets divers projets OpenSource tels que Grass, Qgis ... Elle peut être, par exemple, employée pour la transformation de données.
- [GDAL/OGR](http://gdal.org) Bibliothèque de transformation de formats de données(vecteur et raster). Utilisé dans de nombreux projets pour l'importation, l'exportation ou la transformation de données multi-sources.
- [R](http://www.r-project.org) Langage et environnement pour le calcul statistique et graphique.

### Installation rapide et ~~sale~~ facile

Décompressez l'archive PyWPS à l'intérieur du répertoire où les scripts cgi s'exécutent (générallement cgi-bin).  

```bash
cd /usr/lib/cgi-bin/  
tar xvzf /tmp/pywps-VERSION.tar.gz  
pywps/wps.py
```

### Installation propre

Décompressez l'archive PyWPS : `tar -xzf pywps-VERSION.tar.gz`

Lancez l'installation : `python setup.py install`

Paramétrez le fichier de configuration : `vim /etc/pywps.cfg`

Autorisez les droits en lecture, écriture et exécution sur le répertoire Templates : `chmod -R 777 /usr/lib/python2.5/site-packages/pywps/Templates`

Plusieurs paquets, selon les distributions linux (RPM,DEB), sont également disponibles sur la page de téléchargement de PyWPS.

----

## Configuration

PyWPS étant basé sur le protocole WPS vous devriez en obtenir une copie (OGC 05-007r7) avant de commencer à configurer votre application PyWPS.  

NOTE: Attention, les options de configuration sont **sensibles à la casse**.  

Le fichier de configuration, **pywps.cfg**, se situe dans le répertoire /etc/pywps.cfg ou pywps/etc/pywps.cfg  

Le fichier de configuration par défaut est situé dans le répertoire pywps/default.cfg. Vous pouvez bien évidemment en faire une copie et commencer votre configuration personnelle directement depuis celui-ci.

Ce fichier est divisé en plusieurs sections dont les spécifications sont les suivantes :

- Section [wps] : Options de configuration WPS :
    - encoding : Encodage des caractères (utf-8, iso-8859-2, windows-1250...)
    - title : Nom du serveur
    - version : Version du protocole WPS
    - abstract : Description des objectifs du serveur
    - fees : droits
    - constraints : Contraintes possible
    - serveraddress : Adresse du script wps (ex [http://foo/bar/wps.py](http://foo/bar/wps.py))
    - Mots clé : Liste de mots clé séparée par une virgule
    - lang : Langue

- Section [provider] : Options de configuration personnelle
    - providerName : Compagnie
    - individualName : Nom de l'administrateur
    - positionName : Role de l'administrateur
    - deliveryPoint : Rue
    - city : ville
    - postalCode : code postal
    - electronicMailAddress : Adresse mail
    - providerSite : Site de la compagnie
    - phoneVoice : Téléphone
    - phoneFacsimile : Fax
    - administrativeArea : Département administratif

- Section [server]: Options de configuration du serveur
    - maxoperations : Nombre maximal de processus autorisés à fonctionner en parallèle (0 signifie qu'il n'y a aucune limite)
    - maxinputparamlength : Taille maximale de la chaîne de caractère entrée en paramètre (Ex nom du fichier)
    - maxfilesize : Taille maximale du fichier (raster ou vecteur). Les tailles peuvent être déterminées de la manière suivante : 1GB, 5MB, 3kB, 1000b
    - tempPath : Répertoire temporaire
    - outputUrl : Adresse (URL) où le résultat des traitements est sauvegardé
    - outputPath : Répertoire où le résultat des traitements est sauvegardé
    - debug : true/false

- Section [grass] - GRASS GIS settings
    - path : variable $PATH (par exemple /usr/lib/grass/bin)
    - addonPath : $GRASS_ADDONS addons
    - version : Version de GRASS
    - gui : Graphical User Interface doit être de type text
    - gisbase : Chemin vers le répertoire GIS_BASE de GRASS (/usr/lib/grass)
    - ldLibraryPath : Chemin vers le répertoire où sont stockées les librairies de grass (/usr/lib/grass/lib)

Voici un exemple de fichier de configuration (pywps.cfg) :

```ini
[wps]  
encoding=utf-8  
title=PyWPS Server  
version=1.0.0  
abstract=See http://pywps.wald.intevation.org and http://www.opengeospatial.org/standards/wps  
fees=None  
constraints=none  
serveraddress=http://localhost/cgi-bin/wps  
keywords=GRASS,GIS,WPS  
lang=eng`

[provider]
providerName=Your Company Name  
individualName=Your Name  
positionName=Your Position  
role=Your role  
deliveryPoint=Street  
city=City  
postalCode=000 00  
country=eu  
electronicMailAddress=login@server.org
providerSite=http://foo.bar  
phoneVoice=False  
phoneFacsimile=False  
administrativeArea=False

[server]
maxoperations=3  
maxinputparamlength=1024  
maxfilesize=3mb  
tempPath=/tmp  
outputUrl=http://localhost/wps/wpsoutputs  
outputPath=/var/www/wps/wpsoutputs  
debug=true

[grass]
path=/usr/lib/grass/bin/:/usr/lib/grass/scripts/  
addonPath=  
version=6.2.1  
gui=text  
gisbase=/usr/lib/grass/  
ldLibraryPath=/usr/lib/grass/lib  
```

Afin de tester votre configuration il vous suffit simplement d'envoyer une requête à votre serveur. Cela se fait de la manière suivante (en ligne de commande) :  

`. /wps.py "service=wps&request=getcapabilities"`

Si le résultat est le même que ci-dessous, alors votre configuration est correcte :  

```sh
NIT DONE  
LOADING PRECOMPILED  
TEMPLATE: UPTODATE  
PRECOMPILED: UPTODATE

Content-type: text/xml
xml version="1.0" encoding="utf-8"?  
xmlns:xlink="http://www.w3.org/1999/xlink"  
xmlns:wps="http://www.opengis.net/wps/1.0.0"  
xmlns:ows="http://www.opengis.net/ows/1.1"  
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance  
xsi:schemaLocation="http://www.opengis.net/wps/1.0.0  
http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities_response.xsd"  
updateSequence="1">  

PyWPS Development Server  
...

```

Par contre si vous obtenez quelque chose comme :  

```sh
Traceback (most recent call last):  
File "/usr/bin/wps.py", line 221, in  
wps = WPS()  
File "/usr/bin/wps.py", line 140, in __init__  
self.performRequest()  
File "/usr/bin/wps.py", line 188, in performRequest  
from pywps.WPS.GetCapabilities import GetCapabilities  
File "/usr/lib/python2.5/site-packages/pywps/WPS/GetCapabilities.py", line 26, in  
from Response import Response  
File "/usr/lib/python2.5/site-packages/pywps/WPS/Response.py", line 28, in  
from htmltmpl import TemplateManager, TemplateProcessor  
ImportError: No module named htmltmpl
```

Cela veut dire qu'une de vos options de configuration n'est pas bonne. Par exemple le message ci-dessus signifie que le paquet python-htmltmpl n'est pas installé.

## Écrivez vos propres processus

Tous les processus sont stockés dans le répertoire pywps/processes. Il est possible, grace à la variable d'environnement `$PYTHON_PROCESS` de définir un autre chemin que celui par défaut.

Les deux codes ci-dessous présente un processus de type buffer. Plusieurs processus sont livrés avec le code source PyWPS.

`Create file exampleBufferProcess.py in PYWPS_PROCESSES directory.`

Chaque processus est un script python pouvant fonctionner seul et possédant une classe ayant deux méhodes :

- `__init__`
- `execute`

Il est possible d'ajouter autant de fonctions et méthodes que vous le désirez.

### Initialisation du processus buffer et configuration

```python
from pywps.Process.Process import WPSProcess  
class Process(WPSProcess):
  """Main process class"""
  def __init__(self):  
    """Process initialization"""  
    # init process  
    WPSProcess.__init__(self,  
    identifier = "exampleBufferProcess",  
    title="Buffer",  
    version = "0.2",  
    storeSupported = "true",  
    statusSupported = "true",  
    abstract="Create a buffer around an input vector file",  
    grassLocation = True)  
```

Nous avons défini un nouveau processus nommé exampleBufferProcess. Ce dernier est autorisé à conserver les données produites sur le serveur (storeSupported), il est également possible de l'utiliser en mode asynchrone (statusSupported). Enfin, ce processus utilisera comme environnement GRASS (grassLocation = True).

### Définition des metadata

Celles-ci sont stockées dans le tableau self.Metadata de la méthode `__init__`. Il est possible de rajouter ses propres métadata en utilisant la méthode `self.AddMetadata() :`

```python
self.AddMetadata(identifier="point",type="point",  
textContent="Click in the map")
```

### Données en entrées

Trois types de données/arguments en entrées sont définis :

- Literal - entrée littérale de Base - Peut être un nombre simple ou du texte
- ComplexValue - Cela sera la plus souvent un fichier vectoriel défini à l'intérieur d'une requête XML ou alors pointant vers la ressource elle même via une URL.
- BoundingBox (Extention géographique) - Coordonnées des coins bas/gauche et haut/droit.

#### Exemple d'une donnée en entrée de type complexe

Une donnée complexe peut être aussi bien un raster qu'un vecteur :

```python
self.dataIn = self.addComplexInput(identifier="data",  
title = "Input data")  
```

#### Exemple d'une donnée en entrée de type literale

Depuis un argument de type literal il est possible d'obtenir n'importe quel type de chaîne de caractère :  

```python
self.widthIn = self.addLiteralInput(identifier = "width",  
title = "Width")  
```

Une documentation plus complète présentant des exemples de processus ainsi qu'une aide en ligne (process.html) est distribuée avec le code source de PyWPS.

### Données en sortie

Les types de données disponibles une fois le processus exécuté sont les suivantes :

- `Literal`
- `ComplexValue`
- `BoundingBox`

#### Exemple d'une donnée en entrée de type ComplexValue Output

Une valeur de type complexe peut être un fichier vecteur ou raster (ou tout aussi bien un fichier binaire, text...)

```python
self.bufferOut = self.addComplexOutput(identifier="buffer",  
title="Output buffer file")  
```

#### Exemple d'une donnée en entrée de type Literal Output

Si en sortie vous désirez une chaîne de caractère :

```python
self.textOut = self.addLiteralOutput(identifier="text",  
title="just some text")  
```

### Processus de programmation

Le processus doit être défini dans le constructeur de sa méthode. Dans un processus classique, vous voudrez pouvoir définir vos valeurs en entrées et définir un résultat en sortie. Pour cela vous pourrez utiliser les méthodes `getValue(input_identifier)` et `setValue(output_identifier,value)` des objets input et ouput.

Si vous avez besoin d'exécuter une commande shell plutôt que d'utiliser, par exemple, les fonctions `os.system() or os.popen()` il est préférable d'utiliser la méthode `self.cmd(command,["string for standard input"])`.

Enfin, le temps de calcul restant peut être connu en utilisant la méthode `self.status(string message, number percent)`

Calculation progress can be set using `self.status(string message, number percent)` method.

Par exemple :

```python
def execute(self):  
    """Execute process.  
    Each command will be executed and output values will be set  
    """  

    # run some command from the command line  
    self.cmd("g.region -d")  

    # set status value  
    self.status.set("Importing data",20)  
    self.cmd("v.in.ogr dsn=%s output=data" %\
    (self.getInputValue('data')))  

    self.status.set("Buffering",50)  

    self.cmd("v.buffer input=data output=data_buff buffer=%s scale=1.0 tolerance=0.01" %\
    (self.getInputValue('width')))  

    self.status.set("Exporting data",90)  

    self.cmd("v.out.ogr type=area format=GML input=data_buff dsn=out.xml olayer=path.xml")

    self.bufferOut.setValue("out.xml")  
    self.textOut.setValue("ahoj, svete")  
    return
```

### Traitement des erreurs

A la fin de l'exécution de la fonction aucune valeur ne devrait, normalement, être retournée. Tout autre résultat signifie qu'une erreur s'est produite durant le processus et qu'une erreur sera renvoyée au client. Par exemple :

```python
def execute(self):
    [...]
    return "Ups, something failed!"
```

## Utilisation de GRASS

La configuration de grass se fait via le fichier de configuration de pywps.  

Si vous désirez utiliser les commandes de GRASS dans vos processus et qu'aucun entrepôt de données GRASS n'est défini vous devrez définir grassLocation=True dans la définition de votre processus

```python
WPSProcess.__init__(self,  
    identifier = "exampleBufferProcess",  
    [...]  
    grassLocation = True)
```

Dans ce cas, un entrepôt temporaire sera créé durant l'exécution du processus puis supprimer une fois celui-ci achevé. Par défaut, aucun entrepôt n'est créé.

Il est bien sûr possible de travailler depuis un entrepôt existant. Pour cela il suffit de définir son emplacement de la manière suivante :

```python
WPSProcess.__init__(self,
    identifier = "exampleBufferProcess",
    [...]
    grassLocation = "/home/grass/grassdata/spearfish60")
```

## Testez vos processus

Pour tester PyWPS vous pouvez l'utiliser aussi bien depuis un navigateur qui interrogera votre CGI qu'en ligne de commande directement. Commencer par la ligne de commande est toujours une bonne idée vous n'aurez pas ainsi à regarder, en cas d'erreur, dans le fichier error.log de votre serveur web.

### Exemples de requête

#### Requête de type GetCapabilities (webserver)

```bash
./wps.py "service=wps&request=getcapabilities"
wget -nv -q -O - "http://localhost/cgi-bin/wps.py?service=Wps&request=getcapabilities"
```

#### Requête de type DescribeProcess

```bash
./wps.py "version=1.0.0&service=Wps&request=DescribeProcess&Identifier=bufferExampleProcess"
wget -nv -q -O - "http://localhost/cgi-bin/wps.py?version=0.4.0&service=Wps&request=DescribeProcess&Identifier=exampleBufferProcess"
```

#### Requête avec données

pour l'encodage des données utilisant la méthode GET depuis le protocole HTTP référez-vous à OGC 05-007r712, page 38 "Execute HTTP GET request KVP encoding"

```bash
./wps.py "version=1.0.0&service=Wps&request=Execute&Identifier=exampleBufferProcess&datainputs=data=http://foo/bar/roads.gml;width=0.5"
```

De nombreux exemples de requêtes XML sont disponibles dans le répertoire doc/examples.

Avant de tester votre WPS via HTTP POST vous devrez définir la variable d'environnement `REQUEST_METHOD`. Vous pourrez ensuite rediriger le flux XML d'entrée vers le script into `wps.py` :

```bash
export REQUEST_METHOD=POST
cat doc/wps_execute_request-responsedocument.xml|./wps.py
```

## A propos de ce document

Implémentation de la norme OGC WPS : PyWPS

Traduction réalisée par Van De Casteele Arnaud le 2009-09-28

----

<!-- geotribu:authors-block -->
