---
authors:
- Fabien Goblet
categories:
- article
date: 2009-06-06 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- Google Maps
- API
- v3
title: 18. Introduction à l'API v3
---

# 18. Introduction à l'API v3


:calendar: Date de publication initiale : 06 juin 2009


----





### Introduction




---


La nouvelle API de Google Maps est sensiblement identique à la version 2. Pour les développeurs connaissant l'API v2, ce ne devrait pas être trop déroutant, juste un peu plus simple et logique - selon moi.  



### Initialisation




---


Afin de garantir l'utilisation de la carte sur tous les supports Internet, il est nécessaire de définir dans les méta que la carte sera affichée pleine page et que l'utilisateur ne pourra pas modifier la taille de cette dernière.  



L'appel à l'API se fait maintenant sans avoir besoin de clé - quel est le devenir de l'[API Google Maps Premier](http://www.google.fr/enterprise/maps/) ?  



Ici nous ne travaillerons pas à le 'sensor' de l'utilisateur.  



### Construction de l'objet 'map'




---


Une des nouveautés de cette API est le fait qu'il faille initialiser les paramètres de position et de zoom du centre, et les paramètres de type de couche avant de construire l'objet carte, dans un souci de performance, ces options seront des objets 'non construits' et donc littéraux :  

`var latlng = new google.maps.LatLng(48.856667, 2.350987);  

var myOptions = {  

zoom: 13,  

center: latlng,  

mapTypeId: google.maps.MapTypeId.ROADMAP  

};`  

Et enfin nous initialisons la carte avec le nouveau appel typique à cette nouvelle version : google.maps à la place de GMaps2 :  

`var map = new google.maps.Map(document.getElementById("map_canvas"), myOptions);`  



### Corps de la page HTML




---


Toujours dans le souci d'affichage sur les mobiles nouvelle génération, nous définissons la taille de la carte sur tout l'espace disponible du navigateur.  





### Code complet




---


`function initialize() {
var latlng = new google.maps.LatLng(48.856667, 2.350987);
var myOptions = {
zoom: 13,
center: latlng,
mapTypeId: google.maps.MapTypeId.ROADMAP
};
var map = new google.maps.Map(document.getElementById("map\_canvas"), myOptions);
}`  



### Démonstration




---






[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Maps_tuto18.html)


### Remarques




---


La documentation de l'API v3 se trouve cette à cette adresse : <http://code.google.com/intl/fr/apis/maps/documentation/v3/>


### Conclusion




---


Bien qu'encore à l'état bêta, il est tout à fait possible de créer une simple carte - sans se soucier des contrôles - accessible rapidement par les ordinateurs de bureau et les smartphones 3G.
Le reste des fonctions et services disponibles sur la version 2 de l'API seront progressivement adaptés sur la version 3.
Nous les essayerons au fur et à mesure de leur sortie.


**Auteur : Fabien - fabien.goblet [ at ] gmail.com**




----

## Auteur

--8<-- "content/team/fgob.md"
