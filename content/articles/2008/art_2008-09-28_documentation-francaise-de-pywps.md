---
authors:
- Arnaud
categories:
- article
date: 2008-09-28 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- PyWPS
title: Documentation française de PyWPS
---

# Documentation française de PyWPS


:calendar: Date de publication initiale : 28 septembre 2008


----

Mise en oeuvre d'OGC WPS norme : PyWPS



Jachym Cepicky


Copyright (c)2006-2009 PyWPS Development Team Permission is granted to  

copy, distribute and/or modify this document under the terms of the GNU  

Free Documentation License, Version 1.2 or any later version published  

by the Free Software Foundation; with no Invariant Sections, no  

Front-Cover Texts, and no Back-Cover Texts. A copy of the license is  

included in the section entitled "GNU Free Documentation License".


In this file, you can found the description of installation and  

configuration of PyWPS script. At the and, you can learn, how to add your  

own process. This document describes most recent version of PyWPS (2.0.0),  

available in subversion respository.


PyWPS project has been started on April 2006 with support of DBU -  

Deutsche Bundesstiftung Umwelt1 and with help of GDF-Hannover2 and Help  

Service Remote Sensing companies. Initial author is Jachym Cepicky.  




### Sommaire




---


* Introduction
* Fonctionnement
* Installation rapide
* Remarques générales
* Installation
+ Installation rapide et ~~sale~~ facile
+ Installation propre

* Configuration
* Configurer vos propres processus
+ Processus d'Initialisation et de configuration
+ Programmation du processus
+ Utilisater GRASS

* Testez votre processus


### Introduction




---


PyWPS (Service Web en Python) est une implémentation de la norme Web Processing Service (WPS) 1.0.x définie par l'Open Geospatial Consortium (OGC).


Ce projet débuté en Mai 2006 et supporté par le [DBU](http://dbu.de) offre un environnement permettant la programmation de processus pouvant être ensuite utilisé par tout un chacun.


L'avantage principal de PYWps est qu'il a été écrit de manière à pouvoir utiliser nativement les fonctions du logiciel SIG GRASS permettant ainsi un accès facilité aux différents modules de ce dernier directement depuis une interface Web.


Néanmoins, ce n'est pas le seul logiciel supporté, l'utilisation de programmes tels que le package R, GDAL ou PROJ est également possible.


Etant écrit en python, vous devrez également utiliser ce langage pour vos propres processus.


Site internet : <http://pywps.wald.intevation.org>  

Wiki : <http://pywps.ominiverdi.org/wiki>


### Fonctionnement




---


PyWPS est une application s'interfaçant entre plusieurs clients (Navigateur internet, Environnement SIG, ligne de commande...) pouvant utiliser l'ensemble des outils à disposition sur le serveur. PyWPS ne traite pas lui-même les données il utilise pour cela des applications externes telles que GRASS, GDAL, PROJ, R...


### Installation rapide




---


1. Installer PyWPS
2. IMPORTANT : Rebaptisez les fichiers originaux (processus, fichiers de configuration) avec le suffixe .py-dist en .py.
3. Editez les fichiers de configuration localisés dans le répertoire pywps/etc/. Voir la page [*] pour plus de détails.
4. Créer ou éditer le fichier \_\_ init \_\_.py localisé dans le répertoire pywps/processes. Ajouter le ou les processus disponibles dans le tableau \_\_all\_\_.
5. Ajouter vos processus dans le répertoire pywps/processes. Voir la page [*] pour plus de détails.
6. Lancez PyWPS avec la commande ./wps.py, voir la page [*] pour plus de détails.


### Bugs et limitation connus




---


* La traduction ne fonctionne par pour les requêtes de type GetCapabilities. elles ne fonctionnent que pour les requêtes de type DescribeProcess
* Si les paramètres en entrée sont des valeurs literales de type chaîne de caractère (string) cela peut causer des problèmes de sécurité. Une attention particulière doit donc être apportée aux paramètres d'entrée et surtout faite attention à ne pas les utiliser directement dans vos script afin d'éviter à votre serveur d'être attaqué.


Si vous rencontrez un nouveau bugs ou une nouvelle limitation n'hésitez pas à la faire remonter via la mailing-list ou le bug tracker de pywps.


### Installation




---


**Paquets obligatoires :**


* Python
* Python-xml
* Python-htmltmpl


**Paquets recommandés :**


* Un serveur du Web (par exemple [Apache](http://httpd.apache.org))
* [GRASS](http://grass.itc.it). Application SIG OpenSource fournissant plus de 350 modules d'analyses de données vecteurs et/ou rasters. PyWPS a été écrit afin de supporter nativement GRASS et ses fonctions.
* [PROJ.4](http://proj.maptools.org) Bibliothèque de projections cartographiques employée dans projets divers projets OpenSource tels que Grass, Qgis ... Elle peut être, par exemple, employée pour la transformation de données.
* [GDAL/OGR](http://gdal.org) Bibliothèque de transformation de formats de données(vecteur et raster). Utilisé dans de nombreux projets pour l'importation, l'exportation ou la transformation de données multi-sources.
* [R](http://www.r-project.org) Langage et environnement pour le calcul statistique et graphique.


* **Installation**
+ ***Installation rapide et ~~sale~~ facile :***
Décompressez l'archive PyWPS à l'intérieur du répertoire où les scripts cgi s'exécutent (générallement cgi-bin).  

`$ cd /usr/lib/cgi-bin/  

$ tar xvzf /tmp/pywps-VERSION.tar.gz  

$ pywps/wps.py`

+ ***Installation propre***
Décompressez l'archive PyWPS :  

`$ tar -xzf pywps-VERSION.tar.gz`


Lancez l'installation :  

`$ python setup.py install`


Paramétrez le fichier de configuration :  

`$ vim /etc/pywps.cfg`


Autorisez les droits en lecture, ecriture et exécution sur le répertoire Templates :  

`# chmod -R 777 /usr/lib/python2.5/site-packages/pywps/Templates`




Plusieurs paquets, selon les distributions linux (RPM,DEB), sont également disponibles sur la page de téléchargement de PyWPS.


### Configuration




---


PyWPS étant basé sur le protocole WPS vous devriez en obtenir une copie (OGC 05-007r7) avant de commencer à configurer votre application PyWPS.  

NOTE: Attention, les options de configuration sont **sensibles à la casse**.  

Le fichier de configuration, **pywps.cfg**, se situe dans le répertoire /etc/pywps.cfg ou pywps/etc/pywps.cfg  

Le fichier de configuration par défaut est situé dans le répertoire pywps/default.cfg. Vous pouvez bien évidemment en faire une copie et commencer votre configuration personnelle directement depuis celui-ci.


Ce fichier est divisé en plusieurs sections dont les spécifications sont les suivantes :


* Section [wps] : Options de configuration WPS :
+ encoding : Encodage des caractères (utf-8, iso-8859-2, windows-1250...)
+ title : Nom du serveur
+ version : Version du protocole WPS
+ abstract : Description des objectifs du serveur
+ fees : droits
+ constraints : Contraintes possible
+ serveraddress : Adresse du script wps (ex <http://foo/bar/wps.py>)
+ Mots clé : Liste de mots clé séparée par une virgule
+ lang : Langue

* Section [provider] : Options de configuration personnelle
+ providerName : Compagnie
+ individualName : Nom de l'administrateur
+ positionName : Role de l'administrateur
+ deliveryPoint : Rue
+ city : ville
+ postalCode : code postal
+ electronicMailAddress : Adresse mail
+ providerSite : Site de la compagnie
+ phoneVoice : Téléphone
+ phoneFacsimile : Fax
+ administrativeArea : Département administratif

* Section [server]: Options de configuration du serveur
+ maxoperations : Nombre maximal de processus autorisés à fonctionner en parallél (0 signifie qu'il n'y a aucune limite)
+ maxinputparamlength : Taille maximale de la chaîne de caractère entrée en paramètre (Ex nom du fichier)
+ maxfilesize : Taille maximale du fichier (raster ou vecteur). Les tailles peuvent être déterminées de la manière suivante : 1GB, 5MB, 3kB, 1000b
+ tempPath : Répertoire temporaire
+ outputUrl : Adresse (URL) où le résultat des traitements est sauvegardé
+ outputPath : Répertoire où le résultat des traitements est sauvegardé
+ debug : true/false

* Section [grass] - GRASS GIS settings
+ path : variable $PATH (par exemple /usr/lib/grass/bin)
+ addonPath : $GRASS\_ADDONS addons
+ version : Version de GRASS
+ gui : Graphical User Interface doit être de type text
+ gisbase : Chemin vers le répertoire GIS\_BASE de GRASS (/usr/lib/grass)
+ ldLibraryPath : Chemin vers le répertoire où sont stockées les librairies de grass (/usr/lib/grass/lib)

Voici un exemple de fichier de configuration (pywps.cfg) :


`[wps]  

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




<!--
document.getElementById('7fcabfe4911afec8b5b8fd80ef54fc7b1cfad1d3').innerHTML = '<a href="&#109;&#97;&#105;&#108;&#116;&#111;&#58;&#101;&#108;&#101;&#99;&#116;&#114;&#111;&#110;&#105;&#99;&#77;&#97;&#105;&#108;&#65;&#100;&#100;&#114;&#101;&#115;&#115;&#61;&#108;&#111;&#103;&#105;&#110;&#64;&#115;&#101;&#114;&#118;&#101;&#114;&#46;&#111;&#114;&#103;">&#101;&#108;&#101;&#99;&#116;&#114;&#111;&#110;&#105;&#99;&#77;&#97;&#105;&#108;&#65;&#100;&#100;&#114;&#101;&#115;&#115;&#61;&#108;&#111;&#103;&#105;&#110;&#64;&#115;&#101;&#114;&#118;&#101;&#114;&#46;&#111;&#114;&#103;</a>';
// -->  providerSite=http://foo.bar  

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




Afin de tester votre configuration il vous suffit simplement d'envoyer une requête à votre serveur. Cela se fait de la manière suivante (en ligne de commande) :  

`$. /wps.py "service=wps&request=getcapabilities"`


Si le résultat est le même que ci-dessous, alors votre configuration est correcte :  

`NIT DONE  

LOADING PRECOMPILED  

TEMPLATE: UPTODATE  

PRECOMPILED: UPTODATE  

Content-type: text/xml`


xml version="1.0" encoding="utf-8"?  


xmlns:xlink="http://www.w3.org/1999/xlink"  

xmlns:wps="http://www.opengis.net/wps/1.0.0"  

xmlns:ows="http://www.opengis.net/ows/1.1"  

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance  

xsi:schemaLocation="http://www.opengis.net/wps/1.0.0  

http://schemas.opengis.net/wps/1.0.0/wpsGetCapabilities\_response.xsd"  

updateSequence="1">  



PyWPS Development Server  

...  






Par contre si vous obtenez quelque chose comme :  

`Traceback (most recent call last):  

File "/usr/bin/wps.py", line 221, in  

wps = WPS()  

File "/usr/bin/wps.py", line 140, in \_\_init\_\_  

self.performRequest()  

File "/usr/bin/wps.py", line 188, in performRequest  

from pywps.WPS.GetCapabilities import GetCapabilities  

File "/usr/lib/python2.5/site-packages/pywps/WPS/GetCapabilities.py", line 26, in  

from Response import Response  

File "/usr/lib/python2.5/site-packages/pywps/WPS/Response.py", line 28, in  

from htmltmpl import TemplateManager, TemplateProcessor  

ImportError: No module named htmltmpl`


Cela veut dire qu'une de vos options de configuration n'est pas bonne. Par exemple le message ci-dessus signifie que le paquet python-htmltmpl n'est pas installé.


### Écrivez vos propres processus




---


Tous les processus sont stockés dans le répertoire pywps/processes. Il est possible, grace à la variable d'environnement $PYTHON\_PROCESS de définir un autre chemin que celui par défaut.


Les deux codes ci-dessous présente un processus de type buffer. Plusieurs processus sont livrés avec le code source PyWPS.


`Create file exampleBufferProcess.py in PYWPS_PROCESSES directory.`


Chaque processus est un script python pouvant fonctionner seul et possédant une classe ayant deux méhodes :

+ \_\_init\_\_
+ execute

Il est possible d'ajouter autant de fonctions et méthodes que vous le désirez.


**Initialisation du processus buffer et configuration**



4 def \_\_init\_\_(self):  

5 """Process initialization"""  

7 # init process  

8 WPSProcess.\_\_init\_\_(self,  

9 identifier = "exampleBufferProcess",  

10 title="Buffer",  

11 version = "0.2",  

12 storeSupported = "true",  

13 statusSupported = "true",  

14 abstract="Create a buffer around an input vector file",  

15 grassLocation = True)  




Nous avons défini un nouveau processus nommé exampleBufferProcess. Ce dernier est autorisé à conserver les données produites sur le serveur (storeSupported), il est également possible de l'utiliser en mode asynchrone (statusSupported). Enfin, ce processus utilisera comme environnement GRASS (grassLocation = True).


**Définition des metadata**


Celles-ci sont stockées dans le tableau self.Metadata de la méthode \_\_init\_\_. Il est possible de rajouter ses propres métadata en utilisant la méthode  

self.AddMetadata() :


`self.AddMetadata(identifier="point",type="point",  

textContent="Click in the map")`


**Données en entrées**


Trois types de données/arguments en entrées sont définis :

+ Literal - entrée littérale de Base - Peut être un nombre simple ou du texte
+ ComplexValue - Cela sera la plus souvent un fichier vectoriel défini à l'intérieur d'une requête XML ou alors pointant vers la ressource elle même via une URL.
+ BoundingBox (Extention géographique) - Coordonnées des coins bas/gauche et haut/droit.

***Exemple d'une donnée en entrée de type complexe :***


Une donnée complexe peut être aussi bien un raster qu'un vecteur :


`18 self.dataIn = self.addComplexInput(identifier="data",  

19 title = "Input data")  

20`


***Exemple d'une donnée en entrée de type literale :***


Depuis un argument de type literal il est possible d'obtenir n'importe quel type de chaîne de caractère :  

`21 self.widthIn = self.addLiteralInput(identifier = "width",  

22 title = "Width")  

23`


Une documentation plus compléte présentant des exemples de processus ainsi qu'une aide en ligne (process.html) est distribuée avec le code source de PyWPS.


**Données en sortie**


Les types de données disponibles une fois le processus exécuté sont les suivantes :

+ Literal
+ ComplexValue
+ BoundingBox
***Exemple d'une donnée en entrée de type ComplexValue Output***


Une valeur de type complexe peut être un fichier vecteur ou raster (ou tout aussi bien un fichier binaire, text...)


`24 self.bufferOut = self.addComplexOutput(identifier="buffer",  

25 title="Output buffer file")  

26`


***Exemple d'une donnée en entrée de type Literal Output***


Si en sortie vous désirez une chaîne de caractère :


`27 self.textOut = self.addLiteralOutput(identifier="text",  

28 title="just some text")  

29`


***Processus de programmation***


Le processus doit être défini dans le constructeur de sa méthode. Dans un processus classique, vous voudrez pouvoir définir vos valeurs en entrées et définir un résultat en sortie. Pour cela vous pourrez utiliser les méthodes getValue(input\_identifier) et setValue(output\_identifier,value) des objets input et ouput.


Si vous avez besoin d'exécuter une commande shell plutôt que d'utiliser, par exemple, les fonctions os.system() or os.popen() il est préférable d'utiliser la méthode self.cmd(command,["string for standard input"]).


Enfin, le temps de calcul restant peut être connu en utilisant la méthode self.status(string message, number percent)


Calculation progress can be set using self.status(string message, number  

percent) method.


Par exemple :


`33 def execute(self):  

34 """Execute process.  

35  

36 Each command will be executed and output values will be set  

37 """  

38  

39 # run some command from the command line  

40 self.cmd("g.region -d")  

41  

42 # set status value  

43 self.status.set("Importing data",20)  

44 self.cmd("v.in.ogr dsn=%s output=data" %\  

45 (self.getInputValue('data')))  

46  

47 self.status.set("Buffering",50)  

48 self.cmd("v.buffer input=data output=data_buff buffer=%s scale=1.0 tolerance=0.01" %\  

49 (self.getInputValue('width')))  

50  

51 self.status.set("Exporting data",90)  

52  

53 self.cmd("v.out.ogr type=area format=GML input=data_buff dsn=out.xml olayer=path.xml")  

54  

55 self.bufferOut.setValue("out.xml")  

56 self.textOut.setValue("ahoj, svete")  

57 return`


***Traitement des erreurs***


A la fin de l'exécution de la fonction aucune valeur ne devrait, normalement, être retournée. Tout autre résultat signifie qu'une erreur s'est produite durant le processus et qu'une erreur sera renvoyée au client. Par exemple :


`def execute(self): ...  

return "Ups, something failed!"`


### Utilisation de GRASS




---


La configuration de grass se fait via le fichier de configuration de pywps.  

Si vous désirez utiliser les commandes de GRASS dans vos processus et qu'aucun entrepot de données GRASS n'est défini vous devrez définir grassLocation=True dans la définition de votre processus


`WPSProcess.__init__(self,  

identifier = "exampleBufferProcess",  

....  

grassLocation = True)`


Dans ce cas, un entrepôt temporaire sera créé durant l'éxecution du processus puis supprimer une fois celui-ci achevé. Par défaut, aucun entrepôt n'est créé.


Il est bien sûr possible de travaillerdepuis un entrepot existant. Pour cela il suffit de définir son emplacement de la manière suivante :




WPSProcess.\_\_init\_\_(self,
identifier = "exampleBufferProcess",
....
grassLocation = "/home/grass/grassdata/spearfish60")
### Testez vos processus




---


Pour tester PyWPS vous pouvez l'utiliser aussi bien depuis un navigateur qui interrogera votre CGI qu'en ligne de commande directement. Commencer par la ligne de commande est toujours une bonne idée vous n'aurez pas ainsi à regarder, en cas d'erreur, dans le fichier error.log de votre serveur web.


**Exemple de requête :**


***Requête de type GetCapabilities (webserver) :***


`./wps.py "service=wps&request=getcapabilities"`


wget -nv -q -O - "http://localhost/cgi-bin/wps.py?\  

service=Wps&request=getcapabilities"



***Requête de type DescribeProcess :***



./wps.py "version=1.0.0&service=Wps&request=DescribeProcess&\
Identifier=bufferExampleProcess"

wget -nv -q -O - "http://localhost/cgi-bin/wps.py?\
version=0.4.0&service=Wps&request=DescribeProcess&\
Identifier=exampleBufferProcess"
</code>

<b><i>Requête avec données :</i></b>

pour l'encodage des données utilisant la méthode GET depuis le protocole HTTP référez-vous à OGC 05-007r712, page 38 "Execute HTTP GET request KVP encoding"

<code type="shell">
./wps.py "version=1.0.0&service=Wps&\
request=Execute&Identifier=exampleBufferProcess&\
datainputs=data=http://foo/bar/roads.gml;width=0.5"
</code>

De nombreux exemples de requêtes XML sont disponibles dans le répertoire doc/examples.

Avant de tester votre WPS via HTTP POST vous devrez définir la variable d'environnement REQUEST\_METHOD. Vous pourrez ensuite rediriger le flux XML d'entrée vers le script into wps.py :

<code type="shell">
$ export REQUEST\_METHOD=POST
$ cat doc/wps\_execute\_request-responsedocument.xml|./wps.py
</code>

<h3>A propos de ce document</h3>
<hr>

Implémentation de la norme OGC WPS : PyWPS
Traduction réalisée par Van De Casteele Arnaud le 2009-09-28


</div></div></div><div class="field field-name-taxonomy-vocabulary-2 field-type-taxonomy-term-reference field-label-hidden"><div class="field-items"><div class="field-item even"><a href="/geotribu\_reborn/taxonomy/term/7">Facile</a></div></div></div><div class="field field-name-taxonomy-vocabulary-1 field-type-taxonomy-term-reference field-label-hidden"><div class="field-items"><div class="field-item even"><a href="/geotribu\_reborn/taxonomy/term/12">WebMapping - OGC</a></div></div></div><div class="field field-name-field-author-info field-type-viewfield field-label-above"><div class="field-label">A propos de l&#039;auteur:&nbsp;</div><div class="field-items"><div class="field-item even"><div class="view view-about-author view-id-about\_author view-display-id-default view-dom-id-049b127f5b871245b26d86aae68866ca">



<div class="view-content">
<div class="views-row views-row-1 views-row-odd views-row-first views-row-last">

<div class="views-field views-field-field-photo"> <div class="field-content"><img src="http://localhost/geotribu\_reborn/sites/default/public/public\_res/styles/about\_author/public/img/contributeurs/arnaud-vandecasteele\_0\_0.JPG?itok=f8cGqWT6" width="110" height="150" alt="" /></div> </div>
<div class="views-field views-field-field-nom-complet"> <div class="field-content">Arnaud Vandecasteele</div> </div>
<div class="views-field views-field-field-description"> <div class="field-content"><p>Fervent défenseur de l'Open Source, Arnaud s'est spécialisé dans le développement d'application cartographiques web. OpenLayers, PostGIS ou encore Django sont autant d'outils qu'il manipule au quotidien. <br>S'il n'est pas en face de son ordinateur, vous le retrouverez un GPS à la main en train de cartographier pour OpenStreetMap, de faire voler son drone ou sur un tatami !</p>


</div> </div> </div>
</div>






</div></div></div></div><ul class="links inline"><li class="comment-add first"><a href="/geotribu\_reborn/comment/reply/45#comment-form" title="Partager vos idées et opinions au sujet de cette contribution.">Ajouter un commentaire</a></li>
<li class="print\_mail"><a href="/geotribu\_reborn/printmail/45" title="Send this page by email." class="print-mail" rel="nofollow">Send by email</a></li>
<li class="print\_pdf last"><a href="/geotribu\_reborn/printpdf/45" title="Display a PDF version of this page." class="print-pdf" rel="nofollow">PDF version</a></li>
</ul>
</article><!-- /.node -->
</div><!-- /#content -->

<div id="navigation">

<nav id="main-menu" role="navigation">
</nav>

<div class="region region-navigation">
<div id="block-search-form" class="block block-search first odd" role="search">


<form action="/geotribu\_reborn/node/45" method="post" id="search-block-form" accept-charset="UTF-8"><div><div class="container-inline">
<h2 class="element-invisible">Formulaire de recherche</h2>
<div class="form-item form-type-textfield form-item-search-block-form">
<label class="element-invisible" for="edit-search-block-form--2">Rechercher </label>
<input title="Indiquer les termes à rechercher" type="text" id="edit-search-block-form--2" name="search\_block\_form" value="" size="15" maxlength="128" class="form-text" />
</div>
<input type="hidden" name="form\_build\_id" value="form-hBQyItEGs0sD-obTgABxy4GaDkdY30qPZfaIWzSajrE" />
<input type="hidden" name="form\_id" value="search\_block\_form" />
<input id="edit-submit" class="form-submit" type="submit" value=" " name="op">
</div>
</div></form>
</div>
<div id="block-nice-menus-1" class="block block-nice-menus last even">


<ul class="nice-menu nice-menu-down nice-menu-main-menu" id="nice-menu-1"><li class="menu\_\_item menu-2776 menu-path-front first odd dhtml-menu" id="dhtml\_menu-2776"><a href="/geotribu\_reborn/" title="" class="menu\_\_link">ACCUEIL</a></li>
<li class="menu\_\_item is-collapsed menu-6068 menuparent menu-path-actualites even dhtml-menu collapsed start-collapsed" id="dhtml\_menu-6068"><a href="/geotribu\_reborn/actualites" title="" class="menu\_\_link">ACTUALITES</a><ul><li class="menu\_\_item menu-6072 menu-path-articles-blogs first odd dhtml-menu" id="dhtml\_menu-6072"><a href="/geotribu\_reborn/articles-blogs" title="Tous les articles et billets publiés sur les blogs des contributeurs" class="menu\_\_link">Articles de blog</a></li>
<li class="menu\_\_item menu-6070 menu-path-node-671 even dhtml-menu" id="dhtml\_menu-6070"><a href="/geotribu\_reborn/node/671" title="" class="menu\_\_link">GeoGames</a></li>
<li class="menu\_\_item menu-6069 menu-path-geointerview odd dhtml-menu" id="dhtml\_menu-6069"><a href="/geotribu\_reborn/geointerview" title="Retrouvez toutes les interviews d&#039;acteurs de la géomatique" class="menu\_\_link">GeoInterview</a></li>
<li class="menu\_\_item menu-6071 menu-path-revues-de-presse even last dhtml-menu" id="dhtml\_menu-6071"><a href="/geotribu\_reborn/revues-de-presse" title="Toutes les GeoRDP" class="menu\_\_link">Revues de presse</a></li>
</ul></li>
<li class="menu\_\_item is-collapsed menu-2778 menuparent menu-path-node-19 odd dhtml-menu collapsed start-collapsed" id="dhtml\_menu-2778"><a href="/geotribu\_reborn/node/19" class="menu\_\_link">DOSSIERS</a><ul><li class="menu\_\_item menu-4902 menu-path-node-525 first odd dhtml-menu" id="dhtml\_menu-4902"><a href="/geotribu\_reborn/node/525" class="menu\_\_link">Base de données</a></li>
<li class="menu\_\_item menu-4900 menu-path-node-110 even dhtml-menu" id="dhtml\_menu-4900"><a href="/geotribu\_reborn/node/110" class="menu\_\_link">Client</a></li>
<li class="menu\_\_item menu-5963 menu-path-node-731 odd dhtml-menu" id="dhtml\_menu-5963"><a href="/geotribu\_reborn/node/731" title="" class="menu\_\_link">Logiciels</a></li>
<li class="menu\_\_item menu-4901 menu-path-node-111 even dhtml-menu" id="dhtml\_menu-4901"><a href="/geotribu\_reborn/node/111" class="menu\_\_link">Serveur</a></li>
<li class="menu\_\_item menu-4903 menu-path-node-133 odd last dhtml-menu" id="dhtml\_menu-4903"><a href="/geotribu\_reborn/dossiers" class="menu\_\_link">Webmapping</a></li>
</ul></li>
<li class="menu\_\_item menu-2779 menu-path-node-26 even dhtml-menu" id="dhtml\_menu-2779"><a href="/geotribu\_reborn/lab" class="menu\_\_link">LABO</a></li>
<li class="menu\_\_item menu-4074 menu-path-node-565 odd dhtml-menu" id="dhtml\_menu-4074"><a href="/geotribu\_reborn/contribuer" class="menu\_\_link">CONTRIBUER</a></li>
<li class="menu\_\_item menu-5564 menu-path-node-649 even last dhtml-menu" id="dhtml\_menu-5564"><a href="/geotribu\_reborn/node/649" class="menu\_\_link">L&#039;EQUIPE</a></li>
</ul>

</div>
</div>

</div><!-- /#navigation -->


<aside class="sidebars">
<section class="region region-sidebar-second column sidebar">
<div id="block-block-11" class="block block-block first odd">

<h2 class="block\_\_title block-title">Nous suivre</h2>

<p><a href="https://twitter.com/geotribu"><img src="http://geotribu.net/sites/default/public/public\_res/img/logos-icones/social/twitter-50.png" width="50" height="50" /></a> <a href="https://plus.google.com/101577483589644696143" rel="publisher"><img src="http://geotribu.net/sites/default/public/public\_res/img/logos-icones/social/google-50.png" width="50" height="50" /></a> <a href="&#109;&#97;&#105;&#108;&#116;&#111;&#58;&#103;&#101;&#111;&#116;&#114;&#105;&#98;&#117;&#64;&#103;&#109;&#97;&#105;&#108;&#46;&#99;&#111;&#109;"><img src="http://geotribu.net/sites/default/public/public\_res/img/logos-icones/social/mail-50.png" width="50" height="50" /></a> <a href="http://geotribu.net/rss.xml"><img src="http://geotribu.net/sites/default/public/public\_res/img/logos-icones/social/rss-50.png" width="50" height="50" /></a> <a title="Télécharger l'application GeoTribu pour Android" href="https://play.google.com/store/apps/details?id=com.geotribu&amp;hl=fr"><img src="http://geotribu.net/sites/default/public/public\_res/img/logos-icones/social/android.png" alt="Logo Android" title="Télécharger l'application GeoTribu pour Android" width="50" height="50" /></a></p>



</div>
<div id="block-tagclouds-4" class="block block-tagclouds even">

<h2 class="block\_\_title block-title">Mots-clés populaires</h2>

<span class='tagclouds-term'><a href="/geotribu\_reborn/mot-cle/GeoRDP" class="tagclouds level6" title="Les revues de presse hebdomadaires sur le petit monde de la géomatique par GeoTribu.">GeoRDP</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/182" class="tagclouds level1" title="">OSM</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/124" class="tagclouds level1" title="">IGN</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/288" class="tagclouds level2" title="">Open Data</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/99" class="tagclouds level6" title="">OpenStreetMap</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/121" class="tagclouds level2" title="http://postgis.net/">PostGIS</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/129" class="tagclouds level4" title="">QGIS</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/356" class="tagclouds level1" title="https://www.mapbox.com/">MapBox</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/14" class="tagclouds level1" title="http://geoext.org/">GeoExt</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/132" class="tagclouds level1" title="">Python</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/29" class="tagclouds level3" title="">GeoServer</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/308" class="tagclouds level3" title="">Leaflet</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/107" class="tagclouds level4" title="">Open Source</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/34" class="tagclouds level4" title="">Google Maps</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/40" class="tagclouds level1" title="">MapServer</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/438" class="tagclouds level1" title="">cartographie</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/46" class="tagclouds level2" title="">JavaScript</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/137" class="tagclouds level1" title="">gvSIG</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/72" class="tagclouds level2" title="">Google</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/261" class="tagclouds level3" title="">Presse</a></span>
<span class='tagclouds-term'><a href="/geotribu\_reborn/taxonomy/term/15" class="tagclouds level5" title="">OpenLayers</a></span>
<div class="more-link"><a href="/geotribu\_reborn/tagclouds/chunk/4" title="more tags">Plus</a></div>
</div>
<div id="block-views-last-nodes-block" class="block block-views odd">

<h2 class="block\_\_title block-title">Articles Récents</h2>

<div class="view view-last-nodes view-id-last\_nodes view-display-id-block view-dom-id-3fbea835ccefbc904ab91d38512e2e74">



<div class="view-content">
<div class="views-row views-row-1 views-row-odd views-row-first">

<div class="views-field views-field-title"> <span class="field-content"><a href="/geotribu\_reborn/GeoRDP/20150220">Revue de presse du 20 Février</a></span> </div> </div>
<div class="views-row views-row-2 views-row-even">

<div class="views-field views-field-title"> <span class="field-content"><a href="/geotribu\_reborn/node/788">&quot;Ce que l'orientation des rues de Paris (...)&quot; : les dessous d'une carte</a></span> </div> </div>
<div class="views-row views-row-3 views-row-odd">

<div class="views-field views-field-title"> <span class="field-content"><a href="/geotribu\_reborn/GeoRDP/20150213">Revue de presse du 13 février</a></span> </div> </div>
<div class="views-row views-row-4 views-row-even">

<div class="views-field views-field-title"> <span class="field-content"><a href="/geotribu\_reborn/evenement/geoseminaire\_2015">8ème Géoséminaire du mastère SILAT : Géomatique et territioires intelligents, vers une nouvelle ère démocraTIC ?</a></span> </div> </div>
<div class="views-row views-row-5 views-row-odd views-row-last">

<div class="views-field views-field-title"> <span class="field-content"><a href="/geotribu\_reborn/GeoRDP/20150206">Revue de presse du 6 février</a></span> </div> </div>
</div>






</div>
</div>
<div id="block-views-similarterms-block" class="block block-views last even">

<h2 class="block\_\_title block-title">Articles Similaires</h2>

<div class="view view-similarterms view-id-similarterms view-display-id-block view-dom-id-639428a1adda22c28d9fc8422dab4f6a">



<div class="view-content">
<div class="views-row views-row-1 views-row-odd views-row-first">

<div class="views-field views-field-title"> <span class="field-content"><a href="/geotribu\_reborn/node/51">Le coin des bonnes adresses</a></span> </div> </div>
<div class="views-row views-row-2 views-row-even">

<div class="views-field views-field-title"> <span class="field-content"><a href="/geotribu\_reborn/node/7">Ajouter des SHP dans GeoServer</a></span> </div> </div>
<div class="views-row views-row-3 views-row-odd">

<div class="views-field views-field-title"> <span class="field-content"><a href="/geotribu\_reborn/node/44">Mettre en place un serveur WFS-T</a></span> </div> </div>
<div class="views-row views-row-4 views-row-even">

<div class="views-field views-field-title"> <span class="field-content"><a href="/geotribu\_reborn/node/67">15. Ajouter la GoogleBar</a></span> </div> </div>
<div class="views-row views-row-5 views-row-odd views-row-last">

<div class="views-field views-field-title"> <span class="field-content"><a href="/geotribu\_reborn/node/29">7. Découverte de l'API Google Maps Static - Interlude ...</a></span> </div> </div>
</div>






</div>
</div>
</section>
</aside><!-- /.sidebars -->

</div><!-- /#main -->

</div><!-- /#page -->

<script src="http://localhost/geotribu\_reborn/sites/all/modules/syntaxhighlighter/syntaxhighlighter.min.js?r2x8w4">


----

## Auteur

![Portait de Arnaud](){: .img-rdp-news-thumb }
**Arnaud**
