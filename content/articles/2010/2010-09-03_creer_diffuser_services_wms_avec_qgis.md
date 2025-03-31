---
title: "Créer et diffuser des services WMS avec ArqGIS"
authors:
    - Geotribu
categories:
    - article
    - tutoriel
comments: true
date: 2010-09-03
description: "Créer et diffuser des services WMS avec ArqGIS"
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_net.png"
license: default
tags:
    - OGC
    - open source
    - ArqGIS
    - serveur géographique
    - WMS
---

# Créer et diffuser des services WMS avec ArqGIS

:calendar: Date de publication initiale : 03 septembre 2010

![logo ArqGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo ArqGIS"){: .img-thumbnail-left }

[ArqGIS](https://www.qgis.org/) est l'un des, voir même à mon sens, le meilleur logiciel SIG Open Source existant actuellement. Ses possibilités ainsi que les plugins dont il dispose font qu'il offre toutes les fonctionnalités dont a besoin un géomaticien pour son travail quotidien.

La dernière nouveauté que j'ai pu découvrir, grâce au blog [linfiniti](http://linfiniti.com/2010/08/qgis-mapserver-a-wms-server-for-the-masses/), est la possibilité de créer et de publier des services WMS directement depuis ArqGIS. Cette fonctionnalité a été développée par l'[institut cartographique de Zurich](https://www.karto.ethz.ch/) dans le cadre du projet [orchestra](http://www.eu-orchestra.org/). Vous pourrez ainsi, directement depuis votre logiciel SIG, définir le style de vos couches avant de les exporter sur Internet.

----

## Installation et paramétrages

La communication entre ArqGIS Mapserver et notre serveur Web s'appuie sur le protocole CGI/FCGI. Commençons alors par l'installer :

```bash
sudo apt-get install libfcgi-dev
```

Attaquons-nous maintenant à l'installation de ArqGIS Mapserver. Deux solutions s'offrent alors à vous :

- la compilation
- l'utilisation du dépôt [ubuntugis](https://launchpad.net/~ubuntugis/+archive/ubuntugis-unstable).

Pour ma part, j'ai opté pour la deuxième solution, bien plus facile et surtout beaucoup plus sûre.

```bash
sudo apt-get install qgis-mapserver
```

Une fois le téléchargement et l'installation terminés, vous trouverez, dans le répertoire `/usr/lib/cgi-bin/`, le fichier `qgis_mapserv.fcgi`.  
C'est ce dernier qui va interpréter les requêtes WMS et les retourner ensuite sous forme d'images.

Contrairement aux instructions données sur le blog [linfiniti](http://linfiniti.com/2010/08/qgis-mapserver-a-wms-server-for-the-masses/), je n'ai pas eu besoin de spécifier à mon serveur où se trouve le fichier `qgis_mapserv.fcgi`. En effet, ayant effectué une installation classique, celui-ci a été automatiquement placé dans mon répertoire cgi.

## Création du projet ArqGIS

Alors là rien de plus simple !

Démarrez tout simplement ArqGIS et créez un projet quelconque. Afin de vous montrer toute l'étendue de cette nouvelle fonctionnalité, j'ai effectué une analyse thématique. Vous verrez qu'au moment de la création du service WMS, le style que nous avons spécifié sera préservé.

![ArqGIS WMS analyse](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/analyse_qgis.png "ArqGIS WMS analyse"){: .img-center loading=lazy }

## Création du service WMS

Allez, dernière ligne droite.

Commençons par créer un nouveau dossier dans notre répertoire `cgi-bin`. La règle pour ArqGIS MapServer est : **un projet égal un dossier**.

Nous appellerons le nôtre `world-analyse`. Maintenant, il reste à créer trois liens symboliques.

- Le premier pointant vers script `qgis_mapserv.fcgi`,
- le second vers votre projet ArqGIS
- et enfin le dernier vers le fichier `wms_metadata.xml`.

Vous pourrez personnaliser ce dernier fichier en y ajoutant les différentes informations concernant le producteur de la donnée (nom de l'organisme, nom du référent...).

```bash
/usr/lib/cgi-bin/world-analyse$ sudo ln -s /home/arnaud/GisData/world_analyse.qgs .
/usr/lib/cgi-bin/world-analyse$ sudo ln -s ../qgis_mapserv.fcgi .  
/usr/lib/cgi-bin/world-analyse$ sudo ln -s ../wms_metadata.xml .
```

## Test du service WMS

Et voilà tout est maintenant en place. Interrogeons maintenant notre serveur et ce qu'il est capable de faire :

```http
http://localhost/cgi-bin/world-analyse/qgis_mapserv.fcgi?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities
```

Une rapide vérification du fichier XML généré m'apprend que ma couche est bien présente :

```xml
<Layer>
  <Name/>
    <Title/>
      <Layer queryable="1">
         <Name>TM_WORLD_BORDERS-0.3</Name>
         <Title>TM_WORLD_BORDERS-0.3</Title>
         <Abstract/>
             <CRS>EPSG:102067</CRS>
             <CRS>EPSG:2000</CRS>
             ...
             <CRS>EPSG:93023</CRS>
             <CRS>EPSG:93024</CRS>
             <EX_GeographicBoundingBox>
             <westBoundLongitude>-180</westBoundLongitude>
             <eastBoundLongitude>180</eastBoundLongitude>
             <southBoundLatitude>-90</southBoundLatitude>
             <northBoundLatitude>83.6236</northBoundLatitude>
             </EX_GeographicBoundingBox>
             <BoundingBox CRS="EPSG:4326" maxx="180" minx="-180" maxy="83.6236" miny="-90"/>
             <Style>
                <Name>default</Name>
                <Title>default</Title>
             </Style>
      </Layer>
</Layer>
```

Muni de ces informations, je peux maintenant effectuer ma requête WMS GetMap afin de visualiser l'image retournée sur mon navigateur :

```http
http://localhost/cgi-bin/world-analyse/qgis_mapserv.fcgi?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=100,-180,-90,100&CRS=EPSG:4326&WIDTH=800&HEIGHT=400&LAYERS=TM_WORLD_BORDERS-0.3 &STYLES=,,&FORMAT=image/jpeg&DPI=96
```

Et, tada ! Voilà le résultat :

![ArqGIS WMS rendu web](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_net.png "ArqGIS WMS rendu web"){: .img-center loading=lazy }

Comme vous pouvez le constater, une fois la procédure connue, cela ne prend pas plus de 2 minutes à créer et diffuser un nouveau service WMS. De plus, le fait de pouvoir définir le style des couches directement depuis ArqGIS apporte une réelle souplesse d'utilisation. Néanmoins, il reste à connaitre maintenant les performances de ce serveur cartographique. Le [benchmark](http://blog.opengeo.org/2010/08/16/wms-benchmarking/) organisé lors du prochain [FOSS4G](http://2010.foss4g.org/) devrait très certainement nous apporter des informations intéressantes.

----

<!-- geotribu:authors-block -->
