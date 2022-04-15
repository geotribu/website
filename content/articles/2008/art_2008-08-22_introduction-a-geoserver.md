---
authors:
- Arnaud Vandecasteele
categories:
- article
date: 2008-08-22 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- GeoServer
title: Introduction à GeoServer
---

# Introduction à GeoServer


:calendar: Date de publication initiale : 22 août 2008


----

**that through cooperation we can build something greater than any of us could alone**  

([tiré de la Philosophy de GeoServer](http://docs.codehaus.org/display/GEOSDOC/Introduction "Philosophie d'OpenLayers"))


### - Introduction -




---


Cette introduction sur GeoServer se décompose en 3 parties. Après avoir retracé l'historique de celui-ci, nous nous attacherons à savoir pour qui ce genre d'outil est utile, et quel sont ces possibilités 


### - Qu'est ce que GeoServer -




---


[GeoServer](http://docs.codehaus.org/display/GEOS/Home "Site GeoServer") est, comme son nom l'indique, un serveur cartographique (ou moteur cartographique) OpenSource (licence GPL 2.0) spécialisé dans la gestion d'information géographique (comme [MapServer](http://mapserver.gis.umn.edu/ "Site MapServer")).


Son développement initié par l'association "[The Open Planning Project (TOPP)](http://www.openplans.org/)" avait pour objectif de départ d'offrir une suite d'outils permettant de rendre la gestion de projet urbain plus transparente pour les citoyens. La philosophie principale de ce projet est de l'aveu même des créateurs tournée vers l' "Open Democraty". Terme que je traduirai par démocratie participative, plutôt que démocratie ouverte, car cela implique non seulement une ouverture et une transparence de cette démocratie, mais également une implication des citoyens qui sont les premiers acteurs de ce projet.


GeoServer a ensuite continué à évoluer, notamment en terme de respect des normes en suivant les préconisations de "l'Open Geospatial Consortium (OGC)" (en intégrant par exemple la norme WFS), mais également en ajoutant des modules supplémentaires en se basant sur la librairie [GéoTools](http://geotools.codehaus.org/ "Site GeoTools") permettant ainsi l'intégration de données multi-source (ShapeFiles, Oracle, PostGis ...).


Nous en sommes aujourd'hui à la version 1.6.1, ce qui indique une certaine maturité du projet. Il faut souligner également que la librairie (GeoTools) sur laquelle se base GeoServer est utilisé par de nombreux autres logiciels (uDig, gvSIG...), ce qui permet une complète intégration des diverses facettes du SIG tout en permettant de disposer d'une base technique commune.


### - A qui s'adresse cet outil ? -




---


GeoServer s'adresse en particulier aux administrations, services et personnes souhaitant disposer d'un moteur cartographique en vue d'une externalisation de leurs donnés vers une interface de type WebMapping. A la question, pourquoi utiliser GeoServer plutôt que MapServer, je répondrais que c'est beaucoup plus une question d'habitude. Néanmoins, GeoServer dispose de quelques atouts supplémentaires comme une interface de gestion des données (ce qui par rapport au format text du .map de MapServer est plus qu'agréable), un export vers différents type de rendu cartographique (GoogleEarth, OpenLayers...), ou encore l'intégration des normes d'échange de données actuelles (WMS, WFS ...).


Mais comme je le soulignais, le choix de partir vers telle type plutôt qu'un autre est avant tout personelle, les deux solutions se valent et disposent d'une communauté importante et réactive. Et comme deux avis valent mieux qu'un je vous renvoie vers [l'article de Y.Jacolin sur Géorézo](http://georezo.net/geoblog/?q=node/152 "Comparatif MapServer OpenLayers") portant sur la comparaison de ces deux solutions.


### - Que peut on faire avec ? -




---


Si vous avez bien lu les paragraphes précédents la réponse coule de source. Mais comme répéter ne fait pas de mal, nous alllons revenir sur les principales caractéristiques de Geoserver. Ainsi, GeoServer vous permettra de disposer d'un environnement complet pour la publication et l'édition de données géographique tout en utilisant les standarts de l'OSGEO. Les protocoles WMS, WFS-T, WCS sont dors et déjà implémentés, et la publication peut se faire dans les différents formats suivants, JPEG, PNG, SVG, KML/KMZ, GML, PDF, GeoJSON, ShapeFiles...


Pour un aperçu complet des possibilités je vous invite à consulter cette page de démo : [[Facile](/geotribu_reborn/taxonomy/term/7)](http://geo-s12.leeds.ac.uk:9080/geoserver/mapPreview.do "demo GeoServer>Démo</a> GeoServer.</p>


</div></div></div><div class=")

[GeoServer](/geotribu_reborn/taxonomy/term/1)A propos de l'auteur: 


![](https://cdn.geotribu.fr/images/internal/contributeurs/avdc.jpg?itok=f8cGqWT6) 
Arnaud Vandecasteele 
Fervent défenseur de l'Open Source, Arnaud s'est spécialisé dans le développement d'application cartographiques web. OpenLayers, PostGIS ou encore Django sont autant d'outils qu'il manipule au quotidien.   
S'il n'est pas en face de son ordinateur, vous le retrouverez un GPS à la main en train de cartographier pour OpenStreetMap, de faire voler son drone ou sur un tatami !




* [Ajouter un commentaire](/geotribu_reborn/comment/reply/6#comment-form "Partager vos idées et opinions au sujet de cette contribution.")
* [Send by email](/geotribu_reborn/printmail/6 "Send this page by email.")
* [PDF version](/geotribu_reborn/printpdf/6 "Display a PDF version of this page.")


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


Anaïs D - mar, 29/11/2011 - 5:51pm


Bonjour,


Le lien vers l'article comparatif de Y.jacolin entre geoserver et mapserver n'est plus actif! Merci pour tout sinon!cdlt




* [répondre](/geotribu_reborn/comment/reply/6/1265)












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





[Ajouter des SHP dans GeoServer](/geotribu_reborn/node/7)  

[Appeler un service WMS externe avec GeoServer (WMS Cascading)](/geotribu_reborn/node/321)  

[Interfacer OpenLayers avec un serveur WMS (MapServer/Geoserver)](/geotribu_reborn/node/9)  

[Installation de GeoServer sous Ubuntu 10.04 Lucid Lynx et diffusion d'un service WMS](/geotribu_reborn/node/298)  

[Revue de presse du 22 mars](/geotribu_reborn/node/595)  







----

## Auteur

--8<-- "content/team/avdc.md"
