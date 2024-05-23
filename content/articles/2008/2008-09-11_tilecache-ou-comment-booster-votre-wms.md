---
title: TileCache ou comment booster votre WMS
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-09-11
description: TileCache ou comment booster votre WMS
tags:
    - GeoServer
    - TileCache
    - WMS
---

# TileCache ou comment booster votre WMS

:calendar: Date de publication initiale : 11 septembre 2008

## Qu'est ce que TileCache ?

Afin que la technologie WMS puisse réellement prendre une ampleur suffisante, il fallait avant tout que soit réglé son principal défaut, sa lenteur. C'est ainsi qu'est né, suite à une réflexion de toute la communauté OpenSource lors du FOSS4G 2006, tileCache. En effet, celui-ci vient s'interfacer entre le serveur cartographique et le client afin de garder en cache toutes les images générées. Si un utilisateur demande à nouveau la même ressource, l'image étant déjà produite l'affichage n'en sera que plus rapide.

![TileCache](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2008/tileCache_light2.png "TileCache"){: loading=lazy }
{: align=middle }

**En résumé, tileCache est fait pour vous si vous utilisez un serveur WMS et que vous souhaitez augmenter de manière significative (rapport de 1 à 10) le temps de chargement.**

## Installer et utiliser tileCache

Si cela n'est pas déjà fait téléchargez l'archive de [tileCache](http://tilecache.org/ "site internet tileCache").

Ensuite décompressez-la dans un répertoire accessible via un serveur web. Cela sera par exemple var/www/html (pour les linuxiens) ou votre répertoire htdocs si vous utilisez ms4w.

Vous devrez maintenant autoriser l'exécution de CGI pour le répertoire dans lequel tileCache est installé. Pour cela, éditez le fichier de configuration d'Apache (httpd.conf) et rajoutez-y les lignes suivantes :

```conf
AddHandler cgi-script .cgi  
Options +ExecCGI
```

Bien entendu le chemin défini dans Directory peut varier selon votre installation.

Le plus dur est fait et la configuration est presque fini ! Il vous suffit maintenant de visiter la page où vous avez placé tileCache. Vous devriez alors voir apparaitre l'interface d'OpenLayers avec la couche vmap0 de MetaCarta affichée. Si vous allez dans votre répertoire temp, vous retrouverez l'image qui a été mise en cache.

## Les différents modes d'utilisation de tileCache

TileCache peut être utilisé de plusieurs façons (CGI, FastCGI, Python...). Nous étudierons en particulier le mode CGI qui est le plus simple, ainsi que le mode CGI avec le mod_python d'activé.

La première option sera étudiée très rapidement puisque c'est celle proposée par défaut et qui normalement devrait déjà fonctionner. Dans ce mode, le client interrogera tileCache de la manière suivante (exemple utilisant la notation OpenLayers) :

```javascript
ol_map = new OpenLayers.Map('ol_map', {'controls': [], 'maxZoomLevel': 17} );  
wms_sigma = new OpenLayers.Layer.WMS(  
  "TIGER", "http://sigma.openplans.org/tilecache-1.3/tilecache.cgi?",  
  {layers: 'sigma' },  
  {numZoomLevels: 17}  
);  
ol_map.addLayer(wms_sigma);
```

Passons maintenant à l'optimisation. Les lignes qui suivront permettront d'améliorer sensiblement les performances de tileCache.

### tileCache avec apache en mode mod_python

TileCache est écrit en python, néanmoins le fonctionnement par défaut se fait en mode CGI. Cela entraine pour Apache, à chaque requête, un chargement de l'exécutable python afin de traiter le fichier tilecache.cgi. Il est plus intéressant de charger directement le mode python dans apache.

Différentes étapes sont nécessaires. Tout d'abord activer, dans la liste des modules, le mod_python (LoadModule python_module modules/mod_python.so). Une fois votre serveur Web redémarré (httpd restart) l'extension python sera alors directement chargée en mémoire. Si votre version d'apache ne propose pas par défaut le mode python celui-ci est téléchargeable [ici](http://httpd.apache.org/modules/python-download.cgi "Téléchargement apache mod_python") ou bien pour les linuxiens directement depuis votre gestionnaire de packages (apache-mod_python).

Pour cette seconde étape je n'ai trouvé aucune documentation s'y rapportant. Toutes remarques sont les bienvenues. En effet, pour réussir (de mon côté) à activer le mode python j'ai du auparavant compiler le script python ce qui a permis d'initialiser le service `TileCache/Service.py`. Pour cela taper la commande suivante (dans un shell) :

`pathToTileCache>py setup.py install`

Tout comme nous l'avons fait pour notre script cgi, il va falloir autoriser l'exécution par Apache de script python dans notre répertoire tileCache. Pour cela il faut ajouter dans httpd.conf les lignes suivantes :

```conf
AddHandler python-program .py  
PythonHandler TileCache.Service  
PythonOption TileCacheConfig /var/www/html/tilecache/tilecache.cfg
```

Il ne vous reste plus qu'une petite étape, modifier votre script pour qu'il ne pointe non plus vers tilecache.cgi mais vers tilecache.py. Si vous ne disposez pas de tilecache.py dans votre dossier tileCache, il vous suffit simplement de changer l'extension du .cgi en .py.

Voilà vous devriez être maintenant en mesure d'utiliser tileCache en mode full Python. L'appel côté client se fera de la manière suivante :

```javascript
ol_map = new OpenLayers.Map('ol_map', {'controls': [], 'maxZoomLevel': 17} );  
wms_sigma = new OpenLayers.Layer.WMS(  
  "TIGER", "http://sigma.openplans.org/tilecache-1.3/tilecache.py?",  
  {layers: 'sigma' },  
  {numZoomLevels: 17}  
);  
ol_map.addLayer(wms_sigma);
```

## Paramétrer le fichier de configuration

Maintenant que vous avez défini le mode d'exploitation que vous souhaitez nous allons passer à la configuration de tileCache. Dans un premier temps, nous étudierons les options générales, puis nous mettrons en pratique ce tutoriel en ajoutant une couche personnalisée.

### Configuration : tilecache.cfg

Tout le paramétrage de vos couches, la configuration de chacune d'entre elles s'effectuent dans le fichier tilecache.cfg. Il respecte une structure précise qu'il est important de comprendre.

### Structure du fichier tilecache.cfg

Bien que simple, le fichier tilecache.cfg respecte une architecture précise.  

Tout d'abord, vous devez prendre soin de bien séparer vos blocs de configuration. Ces derniers sont reconnaissables aux deux crochets qui les encadrent ex : [cache]. Chaque couche (ou groupe de couche) devra également être noté de la même manière ex : [macouche1], [monGroupeDeCouche]... Si vous faites l'essai avec une configuration valide vous verrez que tileCache utilise ce nom entre crochet pour créer un dossier du même nom dans le répertoire, définit dans [cache]. C'est dans ce dossier que seront entreposées toutes les tuiles.

!!! note
  A noter que pour changer le dossier de destination des couches, il vous suffit de modifier le chemin spécifié dans [cache].

### Option de configuration des couches

Il est important de comprendre que dans un même bloc il peut être défini une ou plusieurs couches. Vous pouvez par exemple choisir de les regrouper par thématique. Les options de configuration pour un bloc de couches sont les suivantes :

#### bbox

L'extension géographique de la couche. La tableau contenant la liste des résolution par défaut est égal à l'extension de la couche divisée par 512(deux tuiles standards)

#### debug  

Active ou non l'enregistrement des erreurs dans le fichier error.log (par défaut yes)

#### description

Description de la couche. Par défaut la valeur est nulle.

#### extension

Format (extension) de l'image générée. Paramètre utilisé lors de l'appel vers les serveurs WMS ainsi que lors de la sauvegarde des images générées.

#### layers

Chaine de caractère (string) où sont définies la ou les couches à afficher. C'est ce paramètre qui est utilisé lors des appels WMS.

#### levels

Nombre de niveaux de zoom. Si le paramètre résolution est également défini alors celui-ci est prioritaire.

#### mapfile

Chemin (absolu) ou est le mapFile. Obligatoire pour les couches de type MapServer et Mapnik.

#### maxResolution

Résolution maximale. Si celle-ci est définie, un tableau de résolutions intermédiaires est automatiquement calculé en se basant sur le nombre de "levels" défini.

#### metaTile

Ce paramètre permet d'améliorer la qualité des images générées. En effet, par cette méthode, lors de l'appel une seule tuile est demandée. Celle-ci est ensuite découpée grâce à la librairie [Python Imaging](http://www.pythonware.com/products/pil/ "Site internet Python Imaging"). Les valeurs possibles sont yes ou no. Attention en cas d'utilisation de ce paramètre l'installation de la librairie Python Imaging est obligatoire.

#### metaBuffer

Nombre de pixels supplémentaires qui seront ajoutés lors de la création de la tuile. Par défaut sa valeur est 10.

#### metaSize

Ce paramètre définit combien de (sous)tuiles seront générées lorsque le mode metaTile est activé. La notation se fait de la manière suivante integer,integer. Par défaut les valeurs sont 5,5.

#### resolutions

Liste de résolutions séparées par une virgule.

#### size

Définit la taille des tuiles à générer. La notation se fait de la manière suivante integer,integer. Par défaut les valeurs sont 256,256.

#### srs

Chaine de caractère (string) définissant la projection utilisée. La valeur par défaut est : "EPSG:4326".

#### type

Type de couche qui sera utilisé. Les options sont : WMSLayer, MapnikLayer, MapServerLayer,ImageLayer

#### url

URL à utiliser quand la requête porte sur un serveur WMS (type WMSLayer). Ce paramètre est obligatoire lorsque la requête est de type WMS.

#### watermarkImage

Ce paramètre permet, lors de la création des tuiles, d'ajouter une image définie. Cela pourrait être par exemple une image en philigrame comme le fait [GoogleMap](http://maps.google.fr/maps "Site internet GoogleMap") ou le [GéoPortail](http://www.geoportail.fr/). Ce paramètre prend en attribut le chemin où est entreposée votre image. Il est recommandé d'utiliser une image de la même taille (size) que les tuiles. Si vous n'avez défini aucun paramètre de taille la valeur par défaut est 256x256. A noter qu'il n'est pas possible d'utiliser des [images entrelacées](http://fr.wikipedia.org/wiki/Entrelacement "Définition image entrelacée") (interlaced).

#### watermarkOpacity

Le paramètre watermarkOpacity définit l'opacité à appliquer à l'image qui sera ajoutée. La valeur (flottant) varie entre 0 et 1.

#### extent_type

En définissant ce paramètre comme "loose" vous autoriserez TileCache a générer des images en dehors de l'extension géographique préalablement définie (bounding box). Ce paramètre peut être utile pour les personnes ne sachant pas à quelle extension il sera nécessaire d'arrêter la génération des tuiles.

#### tms_type

En définissant ce paramètre comme "google" cela intervertira la verticalité (pour utiliser le modèle x/y spécifique de google)

### Ajouter ses propres couches

Comme nous l'avons vu précédemment pour ajouter une nouvelle couche, il suffit de déclarer un bloc entre crochets avec à l'intérieur le nom de la couche. Une déclaration classique utilisant MapServer comme serveur WMS serait la suivante.

```ini
[myOwnLayer]  
type=WMSLayer  
url=http://localhost/cgi-bin/mapserv?map=/var/www/html/mapserver/monFichierMap.map  
bbox=55.185611724,-21.415085482499997,55.867049316,-20.8459795275 #Extension de la couche  
layers=fond_carto,niveau_2,niveau_0 #Nom des couches telles que définit dans le mapFile  
srs=EPSG:4326  
extent_type=loose  
maxResolutions=0.0013309327968750034  
levels=10  
extension=png  
metaTile=true
```

## Astuces d'utilisation et de configuration

* **Pré-remplir le cache**

Il peut être agréable d'avoir quelques (ou tout) les niveaux de zoom prégénérés. Pour cela tileCache est livré avec un petit "utilitaire" nommé `tilecache_seed.py`. Celui-ci prend trois arguments

* l'URL du serveur WMS  
* Le nom de la couche défini dans le fichier de configuration  
* les niveaux de zoom début et fin

Ce qui donne l'instruction suivante (à exécuter dans un shell) :

`python tilecache_seed.py ‘http://localhost/cgi-bin/mapserv?map=/var/www/html/mapserver/monFichierMap.map’ myOwnLayer 0 3`

Ici, nous allons pré-générés les niveaux de zoom compris entre 0 et 3 (en réalité 0 jusqu'à 2 effectif) pour la couche définie comme myOwnLayer dans le fichier de configuration qui s'appuit sur le mapfile dont l'adresse est `http: //localhost/cgi-bin/mapserv?map=/var/www/html/mapserver/monFichierMap.map`.

Il reste deux améliorations possibles :

* **Forcer le cache client** : il peut arriver que même si une image a déjà été générée le client la redemande à nouveau. Cela est dû au fait que le serveur Apache lors du premier appel n'a pas spécifié la durabilité de la "transaction". Cela peut être réglé par l'ajout du paramètre ExpiresActive.
* **Simuler plusieurs serveurs** : Deuxiémement, il est possible de simuler l'existence de plusieurs serveurs en se basant sur différents noms de domaine. Cela aura pour effet d'augmenter le nombre de requêtes envoyés et donc de diminuer le temps de chargement.

Pour ces deux dernières optimisations je vous conseille plus que vivement la consultation du site [NeoGeo](http://www.neogeo-online.net/blog/archives/84/ "NeoGeo - article TileCache"). Vous y trouverez les compléments d'information dont vous avez besoin. J'ajouterai également le site [SoftLibre](http://softlibre.gloobe.org/openlayers:tilecache "site internet SoftLibre") ou vous trouverez une traduction en français de l'article de [Chris Holmes](http://geoserver.org/display/GEOSDOC/TileCache+Tutorial "tutoriel en anglais tileCache").

## Conclusion

TileCache est l'outil indispensable pour tous projets utilisant comme source de données un serveur WMS. Il apportera une fluidité incontestable à vos applications sans nécessiter de profonds bouleversements technologiques.

A noter, que pour les personnes utilisant GéoServer il existe un équivalent nommé [GéoWebCache](http://geowebcache.org/trac "tileCache pour GéoServer").

----

<!-- geotribu:authors-block -->
