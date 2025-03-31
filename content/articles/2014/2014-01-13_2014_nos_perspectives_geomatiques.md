---
title: "2014, nos prospectives géomatiques"
authors:
    - Thomas GRATIER
categories:
    - article
comments: true
date: 2014-01-13
description: "2014, nos prospectives géomatiques"
tags:
    - prospectives
---

# 2014, nos prospectives géomatiques

:calendar: Date de publication initiale : 13 janvier 2014

Quoi de neuf pour 2014

Comme chaque année, nous vous présentons les visions qu'ont les autres sur l'évolution de l'usage de la cartographie.  
Nous vous invitons à lire nos suppositions sur l'avenir avec 7 propositions.

----

## 1) Les horizons cartographiques vont encore s'élargir

Beaucoup de métiers sous-utilisent les possibilités offertes par la cartographie. On va voir encore des usages inédits des cartes. Ce changement va aller de pair avec la diversification des profils qui utilisent la cartographie. Par exemple, le mouvement des humanités numériques est [en développement](http://www.martingrandjean.ch/association-francophone-humanites-numeriques/) et des personnes comme sociologues, historiens, archivistes, bibliothécaires vont s'emparer des cartes comme [dans ce cas](http://blog.cod-rennes.fr/2013/04/26/une-cartographie-des-livres-en-bibliotheque/). On n'aura plus une majorité de géographes/cartographes comme le montre encore [l'enquête métiers sur les Géomaticiens](http://www.rencontres-sig-la-lettre.fr/wp-content/uploads/2013/06/R2013-geomaticiens-Isenmann.pdf) à la page 26 mais une pluralité de profils.

## 2) L'intégration entre bureautique et cartographie web dans la partie opensource va avoir lieu

En effet, l'environnement technique commence à le permettre alors que ce changement est déjà présent chez des éditeurs comme Esri:

- Complémentarité de ArqGIS avec OpenGeoSuite: un plugin permet de publier facilement depuis ArqGIS vers GeoServer
- Publication bureautique via "ArqGIS RestAPI Plugin" facilitée vers GeoServer et MapServer via les API REST native de GeoServer et pour MapServer avec la [REST API](https://github.com/neogeo-technologies/mra)
- ArqGIS server va continuer son développement soit en direct (avec Lizmap) soit via des IHM du type LizMap Web. D'autres besoins vont apparaître malgré le support WMS, WFS-T et WCS. Cela semble déjà se confirmer avec le plugin [qgis2threejs](http://www.portailsig.org/content/plugin-qgis-visualisez-facilement-toutes-vos-couches-en-3d-dans-un-navigateur-avec-qgis2thre)

## 3) La cartographie en ligne va enfin passer à HTML 5

La sortie de OpenLayers 3, le fort développement de Leaflet depuis le passage de son développeur principal chez MapBox et la disparition progressive des versions obsolètes de IE vont/sont des éléments de ce changement.  
Ce changement va s'accompagner de l'adoption de nouveaux paradigmes de développement apportés par le mobile avec des outils comme Angular JS, BackBone ou bien tous les outils du développement Front-End (Grunt, Yeoman, ...)

## 4) Une convergence avec certaines complémentarités des librairies JavaScript de cartographie va avoir lieu

Certaines librairies cartographiques plus que des librairies concurrentes vont pouvoir se compléter telles que Kartograph.js, D3, Leaflet, OpenLayers 3. Ce développement va se combiner avec une utilisation plus importante des outils de la dataviz pour réaliser des tableaux de bord et autres visualisations.

## 5) La complémentarité DIY et SIG va se renforcer

On assiste à un développement croissant de capteurs installés par exemple pour la météo basée sur [Raspberry Pi](http://www.raspberrypi.org). Cette présence des capteurs va d'autant plus être importante que de nouvelles manières d'aborder la géolocalisation sont en plein développement. Il est possible par exemple de regarder du côté du [Geofencing](https://fr.wikipedia.org/wiki/Gardiennage_virtuel) qui permet par exemple de voir si son enfant ne s'est pas trop éloigné même si l'application la plus visible est pour [le marketing](http://www.e-marketing.fr/Thematique/Tendances-1000/Breves/Mobile-le-bel-avenir-du-geofencing-230896.htm) en envoyant de la publicité ciblée lors du passage à proximité d'un magasin.

## 6) Des nouveaux périphériques de manipulation (Leap Motion, ...) comme d'acquisition (drones ou Google Glasses par exemple) vont pousser des usages différents en cartographie

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/lACxJrXBJOw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## 7) Le domaine satellitaire va prendre son envol dans tous les sens du terme

Des nouveaux venus vont bousculer la donne dans le petit monde des satellites dominés par des gros consortiums, anciennement présents. Pour preuve, [PlanetLabs](http://www.planet-labs.com) vient de lancer sa constellation de satellites avec [Antares](http://www.parabolicarc.com/2014/01/09/antares-launches-cygnus-international-space-station/). Ce changement a déjà été entamé par MapBox avec le début du développement de Raster.io (porté par Sean Gillies, développeur de Shapely ou Fiona) et avec l'outillage raster qui ne cesse de s'étendre côté PostGIS.

## Pour aller plus loin, nous vous invitons à lire d'autres sources

Nous avons trouvé trois sources en anglais:

- <http://sensorsandsystems.com/dialog/perspectives/32439-ten-predictions-for-2014.html>
- <http://geohipster.com/2013/12/31/what-will-be-hot-in-geo-in-2014-predictions-from-the-geohipster-crowd/>
- <http://boundlessgeo.com/2014/01/paul-ramsey-predictions-2014/>

Publié depuis Twitter, on rajoutera les prédictions de [@cedricmoullet](https://twitter.com/cedricmoullet)

- 2014 Geoweb Prediction #1: Full convergence: mobile, desktop, 2D, 3D, 4D -> all in one geoportal !  
- 2014 Geoweb Prediction #2: Web mapping applications will mainly use HTTPS  
- 2014 Geoweb Prediction #3: OpenLayers 3 will be very largely used  
- 2014 Geoweb Prediction #4: Vector data in web mapping applications will be the rule  
- 2014 Geoweb Prediction #5: Foundation, Bootstrap, AngularJS, Ember etc... will be largely used in web mapping applications  
- 2014 Geoweb Prediction #6: SEO will be a very hot topic for geoportals  
- 2014 Geoweb Prediction #7: MapBox will be bought by one big player

Enfin, on terminera par une source en français:

- [http://fr.slideshare.net/Esri_France/2014-trends-v5](http://fr.slideshare.net/Esri_France/2014-trends-v5)

On verra bien en fin d'année qui a gagné à ce petit jeu ;) et si des prophéties auto-réalisatrices ont lieu (voir [cet article](http://www.persee.fr/web/revues/home/prescript/article/spgeo_0046-2497_2000_num_29_2_1981) pour les plus curieux).

Si vous avez d'autres sources ou bien voulez échanger sur le sujet, n'hésitez pas à commenter: nous sommes preneurs!

----

<!-- geotribu:authors-block -->
