---
authors:
- Fabien Goblet
categories:
- article
date: 2008-09-07 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- Google Maps
- itinéraire
title: 12. Calculer un itinéraire
---

# 12. Calculer un itinéraire


:calendar: Date de publication initiale : 07 septembre 2008


----





### Introduction




---


De la même manière que le géocodage à l'adresse, l'API Google Maps permet de calculer un itinéraire en utilisant la classe [GDirections](http://code.google.com/intl/fr/apis/maps/documentation/reference.html#GDirections).  



### Initialisation




---


Reprendre la carte du [tutoriel n°2](http://www.geotribu.net/node/13).  



### Calcul de l'itinéraire




---


Définir la fonction setDirections(fromAddress, toAddress) qui calcule l'itinéraire entre deux adresses :  

`function setDirections(fromAddress, toAddress) {  

gdir.load("from: " + fromAddress + " to: " + toAddress,{ "locale": "fr" });  

}`  

Définir un objet GDirections :  

`gdir = new GDirections(map);`  

Calculer un itinéraire lors de l'appel de la carte :  

`setDirections("Allée Machado, Toulouse, fr", "Avenue de l'agrobiopole, Auzeville-Tolosane, fr", "fr");  

`Et éditer le formulaire en HTML :  

`|  |  |
| --- | --- |
|  |  |
|  |  |
|  |








### Code complet




---


`-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">  







[Google Maps] 12. Calculer un itinéraire  



html { overflow:hidden; height:100%; } 
body { height:100%; margin:0; }
#map { width:100%; height:100%; }



var map = null;
var gdir;

function setDirections(fromAddress, toAddress) {
gdir.load("from: " + fromAddress + " to: " + toAddress,{ "locale": "fr" });
}

function initialize() {
if (GBrowserIsCompatible()) {
map = new GMap2(document.getElementById('map'));
map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),15);
map.addControl(new GMapTypeControl());
map.removeMapType(G\_HYBRID\_MAP);
map.addMapType(G\_PHYSICAL\_MAP);
map.setMapType(G\_PHYSICAL\_MAP);
map.addControl(new GOverviewMapControl());
map.addControl(new GScaleControl());
map.addControl(new GLargeMapControl());
map.enableScrollWheelZoom();

geocoder = new GClientGeocoder();

gdir = new GDirections(map);
setDirections("Allée Machado, Toulouse, fr", "Avenue de l'agrobiopole, Auzeville-Tolosane, fr", "fr");

var iti = new GControlPosition(G\_ANCHOR\_TOP\_LEFT, new GSize(60, 10));
iti.apply(document.getElementById("iti"));
map.getContainer().appendChild(document.getElementById("iti"));

}
else{
alert('Désolé, mais votre navigateur n\'est pas compatible avec Google Maps');
}
}








|  |  |
| --- | --- |
|  |  |
|  |  |
|  |













### Démonstration




---






[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto12.html)
Evidemment le résultat est plus joli en pleine page :-)


### Remarques




---


Toujours se référer à l'API Google Maps - [Google Maps API Reference](http://code.google.com/apis/maps/documentation/reference.html) pour les différentes classes, méthodes et options utilisées.
Le nombre de requêtes est limité à 15000 par jour et par adresse IP (idem que le géocodage).
Il est possible d'afficher l'itinéraire sous forme de texte en définissant un panel dans le constructeur GDirections.


### Conclusion




---


De la même manière que le géocodage, le calcul d'un itinéraire se fait de façon très simple grâce à l'API Google Maps.
L'affichage de l'itinéraire ainsi que le niveau de zoom approprié est fait de façon automatique par la méthode load() de la classe GDirections.


**Auteur : Fabien - fabien.goblet [ at ] gmail.com**


[Intermédiaire](/geotribu_reborn/taxonomy/term/8)[Google Maps](/geotribu_reborn/taxonomy/term/3)A propos de l'auteur: 


![](https://cdn.geotribu.fr/images/internal/charte/geotribu_logo_64x64.png?itok=Q4cCqZQC) 
Fabien Goblet 
Fabien est l'un des fondateurs de Geotribu.




* [Ajouter un commentaire](/geotribu_reborn/comment/reply/40#comment-form "Partager vos idées et opinions au sujet de cette contribution.")
* [Send by email](/geotribu_reborn/printmail/40 "Send this page by email.")
* [PDF version](/geotribu_reborn/printpdf/40 "Display a PDF version of this page.")


/*
* touch theme implementation to wrap comments.
*
* Available variables:
* - $content: The array of content-related elements for the node. Use
* render($content) to print them all, or
* print a subset such as render($content['comment\_form']).
* - $classes: String of classes that can be used to style contextually through
* CSS. It can be manipulated through the variable $classes\_array from
* preprocess functions. The default value has the following:
* - comment-wrapper: The current template type, i.e., "theming hook".
*
* The following variables are provided for contextual information.
* - $node: Node object the comments are attached to.
* The constants below the variables show the possible values and should be
* used for comparison.
* - $display\_mode
* - COMMENT\_MODE\_FLAT
* - COMMENT\_MODE\_THREADED
*
* Other variables:
* - $classes\_array: Array of html class attribute values. It is flattened
* into a string within the variable $classes.
*
* @see template\_preprocess\_comment\_wrapper()
* @see theme\_comment\_wrapper()
*/
?>

## Commentaires





### 


Berti - lun, 26/07/2010 - 11:59am


Bonjour,


Est il possible de récupérer l'adresse automatiquement( gps ou antenne gsm) ou si l'utilisateur loggé a renseigné son adresse dans ses préférences.


Peut-on inscrire une adresse de destination fixe?




* [répondre](/geotribu_reborn/comment/reply/40/618)












## Formulaire de recherche



Rechercher 









* [ACCUEIL](/geotribu_reborn/)
* [ACTUALITES](/geotribu_reborn/actualites)
+ [Articles de blog](/geotribu_reborn/articles-blogs "Tous les articles et billets publiés sur les blogs des contributeurs")
+ [GeoGames](/geotribu_reborn/node/671)
+ [GeoInterview](/geotribu_reborn/geointerview "Retrouvez toutes les interviews d'acteurs de la géomatique")
+ [Revues de presse](/geotribu_reborn/revues-de-presse "Toutes les GeoRDP")
* [DOSSIERS](/geotribu_reborn/node/19)
+ [Base de données](/geotribu_reborn/node/525)
+ [Client](/geotribu_reborn/node/110)
+ [Logiciels](/geotribu_reborn/node/731)
+ [Serveur](/geotribu_reborn/node/111)
+ [Webmapping](/geotribu_reborn/dossiers)
* [LABO](/geotribu_reborn/lab)
* [CONTRIBUER](/geotribu_reborn/contribuer)
* [L'EQUIPE](/geotribu_reborn/node/649)








## Nous suivre


[![](http://geotribu.net/sites/default/public/public_res/img/logos-icones/social/twitter-50.png)](https://twitter.com/geotribu) [![](http://geotribu.net/sites/default/public/public_res/img/logos-icones/social/google-50.png)](https://plus.google.com/101577483589644696143) [![](http://geotribu.net/sites/default/public/public_res/img/logos-icones/social/mail-50.png)](mailto:geotribu@gmail.com) [![](http://geotribu.net/sites/default/public/public_res/img/logos-icones/social/rss-50.png)](http://geotribu.net/rss.xml) [![Logo Android](http://geotribu.net/sites/default/public/public_res/img/logos-icones/social/android.png "Télécharger l'application GeoTribu pour Android")](https://play.google.com/store/apps/details?id=com.geotribu&hl=fr "Télécharger l'application GeoTribu pour Android")




## Mots-clés populaires


[PostGIS](/geotribu_reborn/taxonomy/term/121 "http://postgis.net/")
[JavaScript](/geotribu_reborn/taxonomy/term/46)
[OpenStreetMap](/geotribu_reborn/taxonomy/term/99)
[GeoServer](/geotribu_reborn/taxonomy/term/29)
[QGIS](/geotribu_reborn/taxonomy/term/129)
[MapBox](/geotribu_reborn/taxonomy/term/356 "https://www.mapbox.com/")
[cartographie](/geotribu_reborn/taxonomy/term/438)
[Python](/geotribu_reborn/taxonomy/term/132)
[Google Maps](/geotribu_reborn/taxonomy/term/34)
[gvSIG](/geotribu_reborn/taxonomy/term/137)
[MapServer](/geotribu_reborn/taxonomy/term/40)
[Leaflet](/geotribu_reborn/taxonomy/term/308)
[IGN](/geotribu_reborn/taxonomy/term/124)
[OpenLayers](/geotribu_reborn/taxonomy/term/15)
[Google](/geotribu_reborn/taxonomy/term/72)
[GeoExt](/geotribu_reborn/taxonomy/term/14 "http://geoext.org/")
[Open Data](/geotribu_reborn/taxonomy/term/288)
[GeoRDP](/geotribu_reborn/mot-cle/GeoRDP "Les revues de presse hebdomadaires sur le petit monde de la géomatique par GeoTribu.")
[OSM](/geotribu_reborn/taxonomy/term/182)
[Open Source](/geotribu_reborn/taxonomy/term/107)
[Presse](/geotribu_reborn/taxonomy/term/261)
[Plus](/geotribu_reborn/tagclouds/chunk/4 "more tags")


## Articles Récents





[Revue de presse du 20 Février](/geotribu_reborn/GeoRDP/20150220)  

["Ce que l'orientation des rues de Paris (...)" : les dessous d'une carte](/geotribu_reborn/node/788)  

[Revue de presse du 13 février](/geotribu_reborn/GeoRDP/20150213)  

[8ème Géoséminaire du mastère SILAT : Géomatique et territioires intelligents, vers une nouvelle ère démocraTIC ?](/geotribu_reborn/evenement/geoseminaire_2015)  

[Revue de presse du 6 février](/geotribu_reborn/GeoRDP/20150206)  




## Articles Similaires





[5. Polylignes (suite) - La Terre n'est pas plate ...](/geotribu_reborn/node/17)  

[11. Géocoder une adresse](/geotribu_reborn/node/39)  

[20. [Google Maps API v3] Marqueur, événement et devices](/geotribu_reborn/node/204)  

[17. Ajouter un marqueur déplaçable et jouer avec la gravité](/geotribu_reborn/node/83)  

[8. Superposer un fichier KML et enrichir les infobulles](/geotribu_reborn/node/36)````


----

## Auteur

--8<-- "content/team/fgob.md"
