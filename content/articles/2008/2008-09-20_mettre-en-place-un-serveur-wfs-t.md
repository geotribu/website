---
title: Mettre en place un serveur WFS-T
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-09-20
description: Mettre en place un serveur WFS-T
tags:
    - MapServer
    - WFS-T
---

# Mettre en place un serveur WFS-T

:calendar: Date de publication initiale : 20 septembre 2008

## Qu'est ce que FeatureServer ?

Dans un [précédent tutoriel](2008-09-15_interfacer-openlayers-avec-un-serveur-wfs-mapserver.md) nous avions appris que les serveurs WFS, en fonction de leurs capacités, peuvent être regroupés en différentes catégories. Si la plupart permettent l'affichage des objets géographiques sous forme de vecteur, peu d'entre eux permettent de réaliser des opérations de mises à jour, suppression ou création sur ces mêmes objets.  

C'est là tout l'intérêt de "Feature Server". En effet, basé sur la même logique que TileCache, il permet au moyen d'un simple fichier de configuration de disposer d'un serveur WFS transactionnel.  

Les sources de données qu'il est capable de lire sont les suivantes (**R/W** pour accessible en lecture/écriture et **R** pour seulement en lecture):

- [DBM](http://en.wikipedia.org/wiki/AnyDBM "Wikipedia AnyDBM")- Utilisation d'ANYDBM comme base de données (sous forme de fichiers). L'avantage est sa facilité d'installation et sa portabilité (marche sur toutes les plateformes) **(R/W)**
- [BerkleyDB](http://fr.wikipedia.org/wiki/Berkeley_DB "Wikipedia BerkleyDB") - Basé sur la même logique que DBM, BerkleyDB est une base de données embarquée **(R/W)**
- [PostGIS](http://fr.wikipedia.org/wiki/PostGIS "Wikipedia PostGIS") - Base de données spatiale basée sur PostgreSQL **(R/W)**
- [WFS](http://fr.wikipedia.org/wiki/WFS "Wikipedia WFS") - Permets l'affichage de données provenant d'un serveur WFS **(R)**
- [OGR](http://www.gdal.org/ogr/ "Site internet OGR/GDAL") - Permets l'accès à tous [les formats](http://www.gdal.org/ogr/ogr_formats.html) (PostGIS, GML, SHP...) gérés par OGR (plus d'une trentaine). Les possibilités des accès en lecture ou en écriture dépendent des spécifications d'OGR
- [Flickr](http://www.flickr.com/ "site internet Flickr") - Permets l'affichage d'image provenant du site de partage Flickr (géotagg)
- [OSM](http://www.openstreetmap.org/ "Site internet OpenStreet Map") - Permets l'affichage des données provenant d'Open Street Map

Les formats de données (service) qu'il est capable de lire sont les suivants (**R/W** pour accessible en lecture/écriture, **W** pour accessible en écriture):

- [GeoJSON](http://geojson.org/ "Site Internet GeoJSON") - Encodage des données géographiques au format JSON. Accessible en **R/W** pour tous les types d'objets (lignes, polygones, points...)
- [GeoRSS Atom (Simple)](http://georss.org/simple "Site Internet GeoRSS Atom (Simple)") - Encodage des données géographiques au format GeoRSS Atom (Simple). Accessible en **R/W** pour tous les types d'objets (lignes, polygones, points...)
- [KML](http://earth.google.fr/kml/ "Site Internet Google Earth") - Encodage des données géographiques au format KML. Accessible en **R/W** pour tous les types d'objets (lignes, polygones, points...)
- [WFS/GML](http://fr.wikipedia.org/wiki/WFS "Wikipedia WFS") - Encodage des données géographiques au format KML/GML. Support uniquement en écriture (W)
- [HTML](http://fr.wikipedia.org/wiki/Hypertext_Markup_Language "Wikipedia HTML")- Support uniquement en écriture. Utilise [Cheetah templates](http://www.cheetahtemplate.org/ "Cheetah templates")
- [OSM](http://www.openstreetmap.org/ "Site internet OpenStreet Map") - Support uniquement en écriture. Permets la création de fichiers '.osm' qui peuvent être directement utilisés ou envoyés au serveur carto d'OSM

**En résumé, FeatureServer est fait pour vous si vous utilisez un serveur WFS et que vous souhaitez pouvoir modifier vos données.**

## Installer et utiliser FeatureServer

Si cela n'est pas déjà fait télécharger l'archive de [Feature Server](http://featureserver.org/ "site internet Feature Server").

Ensuite décompressez-la dans un répertoire accessible via un serveur web. Cela sera `var/www/html` (pour les linuxiens) ou votre répertoire `htdocs` si vous utilisez ms4w.

Vous devrez maintenant autoriser l'exécution de CGI pour le répertoire dans lequel FeatureServer est installé. Pour cela, éditez le fichier de configuration d'Apache (httpd.conf) et rajoutez-y les lignes suivantes :

```conf
AddHandler cgi-script .cgi  
Options +ExecCGI
```

Bien entendu le chemin défini dans Directory peut varier selon votre installation. Et n'oubliez pas surtout une fois votre fichier enregistré de **redémarrer votre serveur apache**.

Le plus dur est fait et la configuration est presque fini ! Pour vérifier que tout s'est bien passé il vous suffit maintenant de visiter la page [http://localhost/featureserver.cgi/scribble/all.atom](http://localhost/featureserver.cgi/scribble/all.atom). Si une page de flux vide s'affiche alors tout est bien configuré.

Rendez-vous maintenant sur la page d'index de featureServer ([http://localhost/featureserver/](http://localhost/featureserver/)) vous devriez alors voir apparaitre l'interface d'OpenLayers avec la couche vmap0 de MetaCarta affichée avec sur la droite un formulaire permettant le paramétrage des objets géographiques.

![FeatureServer](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2008/featureServer.png "FeatureServer"){: .img-center loading=lazy }

Si vous dessinez un objet sur la carte puis que vous le sauvegarder celui-ci sera enregistré dans la base **featureserver.scribble** située (si vous n'avez pas modifié le fichier de config) dans le répertoire `/tmp/`.  

Quittez votre navigateur, revenez l'objet est toujours là ! Pour le moment cet objet est sauvegardé dans une base DBM. Nous apprendrons dans le paragraphe suivant à utiliser d'autre moyen de sauvegarde et d'autres sources de services.

## Les différents modes d'utilisation de FeatureServer

FeatureServer peut être utilisé de différentes façons. Nous en étudierons deux, le mode CGI qui est le plus simple, ou alors le mode CGI avec le `mod_python` activé.

La première option sera très rapidement étudiée ici puisque c'est celle que vous avez déjà normalement réussi à faire fonctionner. Dans ce mode, le client interrogera FeatureServer de la manière suivante (exemple utilisant la notation OpenLayers) :

```javascript
wfs = new OpenLayers.Layer.WFS(  
  "WFS", "featureserver.cgi/scribble?format=WFS",  
  {maxfeatures: "100"},  
  {extractAttributes: true}  
);
```

Passons maintenant à l'optimisation. Les lignes qui suivront permettront d'améliorer sensiblement les performances de Feature Server.

### Feature Server apache en mode mod_python

Feature Server est écrit en python, néanmoins le fonctionnement par défaut se fait en mode CGI. Cela entraine pour Apache, à chaque requête, un chargement de l'exécutable python afin de traiter le fichier featureserver.cgi. Il est plus intéressant de charger directement le mode python dans apache.

Différentes étapes sont nécessaires. Tout d'abord activer, dans la liste des modules, le `mod_python` (`LoadModule python_module modules/mod_python.so`). Une fois votre serveur Web redémarré (httpd restart) l'extension python sera alors directement chargée en mémoire. Si votre version d'apache ne propose pas par défaut le mode python celui-ci est téléchargeable [ici](http://httpd.apache.org/modules/python-download.cgi "Téléchargement apache mod_python") ou bien pour les linuxiens directement depuis votre gestionnaire de packages (apache-mod_python).

Il ne vous reste plus qu'une petite étape, modifier votre script pour qu'il ne pointe non plus vers featureserver.cgi mais vers featureserver.py. Si vous ne disposez pas de featureserver.py dans votre dossier featureserver, il vous suffit simplement de changer l'extension du .cgi en .py.

Voilà vous devriez être maintenant en mesure d'utiliser featureserver en mode full Python. L'appel côté client se fera de la manière suivante :

```javascript
wfs = new OpenLayers.Layer.WFS(  
  "WFS", "featureserver.py/scribble?format=WFS",  
  {maxfeatures: "100"},  
  {extractAttributes: true, displayInLayerSwitcher: false}  
);
```

## Paramétrer le fichier de configuration

Maintenant que vous avez défini le mode d'exploitation que vous souhaitez nous allons passer à la configuration de featureserver. Dans un premier temps nous étudierons les options générales, puis nous mettrons en pratique ce tutorial en ajoutant une couche personnalisée.

### Configuration : featureserver.cfg

Tout le paramétrage de vos couches ainsi que la configuration de chacune d'entre elles s'effectuent dans le fichier featureserver.cfg. Il respecte une structure précise qu'il est important de comprendre.

- Structure du fichier featureserver.cfg

Bien que simple, le fichier featureserver.cfg respecte une architecture précise.  

Tout d'abord vous devez prendre soin de bien séparer vos blocs de configuration. Ces derniers sont reconnaissables aux deux crochets qui les encadrent ex : [metadata]. Chaque couche (ou groupe de couche) devra également être noté de la même manière ex : [macouche1], [monGroupeDeCouche]... C'est ce nom de groupe entre crochets que vous utiliserez ensuite lors de vos appels.

- Configurer le service que vous souhaitez utiliser

Le service utilisé est défini par l'attribut `default_service` du bloc [metadata]. Celui par défaut est GeoJSON. Vous pouvez néanmoins changer celui-ci pour qu'il fonctionne avec l'un des services que l'on a vu précédemment.

- Configurer le format de stockage de vos couches (DataSource)

Le format de stockage de vos données est défini par l'attribut type du bloc [layer] (layer étant le nom de votre couche).

- Ajouter vos propres données

Nous étudierons la configuration et l'ajout de trois formats de stockage ci-dessous :

- DBM
- OGR
- OSM

- Attributs globaux

Ce sont des attributs que l'on retrouvera quelle que soit le type de stockage/source utilisé :

type => Représente le type de stockage qui sera utilisé  

`gaping_security_hole` => signifie que vous autorisez, sans restriction, le chargement de ces données depuis des appels JSON. Les utilisateurs pourront accéder à vos données et ce même si elles sont protégées par un firwall.

- DBM

C'est le format de stockage par défaut. Si vous avez réussi à configurer correctement featureServer c'est le mode de fonctionnement qui est utilisé dans l'exemple.  

Les arguments nécessaires sont :

```ini
[DBM]  
type=DBM  
file=/tmp/featureserver.scribble  
gaping_security_hole=yes
```

`file` => l'endroit où sera stockée votre base.

- OGR

Permet d'accéder à n'importe quel type de données géré par la librairie OGR (nécessite bien sûr de disposer de la librairie OGR)

```ini
[myshape]  
type=OGR  
dsn=/home/example/myshape.shp  
layer=myshape
```

`dsn` => le chemin absolu où est stocké vos données  
`layer` => le nom de la couche (sans son extension)

- OSM

Vous pouvez accéder aux données d'OpenStreetMap directement depuis featureServer.

```ini
[osm]  
type=OSM  
osmxapi=no
```

`osmxapi` => Permet d'utiliser l'API étendu d'OpenStreetMap

![OpenStreetMap](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2008/osm.png "OpenStreetMap"){: .img-center loading=lazy }

A noter que si vous utilisez `featureserver.py` vous ne pourrez pas accéder au stockage OSM. De plus les données ne sont accessibles qu'à un certain niveau d'echelle. N'hésitez donc pas à zoomer.

### Les filtres qu'il est possible d'utiliser

Le protocole WFS permet depuis l'URL d'ajouter certains paramètres qui permettront de filtrer les données renvoyées :

- `bbox` => Emprise spatiale des données (gauche, bas, haut, droite)
- `maxfeatures` => Nombre maximal de données renvoyé au client
- `startfeature` => Spécifie à partir de quelle entité vous souhaitez commencer la requête (efficace par exemple avec un `maxfeatures`)
- `queryable` => liste des colonnes attributaires de la couche pouvant être interrogée (Peut êre également défini dans le fichier de configuration)
- `key` => Nom des attributs sur lequel portera la requête (seuls les attributs dont le numéro est défini dans le paramètre queryable seront interrogeables)

Un exemple d'URL utilisant des filtres serait la suivante : `http://myfeatureserver.com/featureserver.cgi/mylayer/all?maxfeatures=25&bbox=-124.1,47.2,-123.9,47.5&queryable=category,species&category=fun&species=mongoose&color=brown`

## Conclusion

Et voilà, vous devriez être maintenant en capacité de configurer votre propre serveur WFS-T. Peu de serveur carto sont aujourd'hui capables de réaliser ce genre de service. Néanmoins, vous n'aurez besoin de le mettre en place que si vous avez à réaliser des manipulations (géographiques, attributaires) sur des objets géographiques.  

Si vous vous limitez à de l'affichage de données vecteur, GéoServer et MapServer sont très largement suffisants.

----

<!-- geotribu:authors-block -->
