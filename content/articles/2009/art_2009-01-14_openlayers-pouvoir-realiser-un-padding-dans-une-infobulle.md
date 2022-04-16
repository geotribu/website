---
authors:
- Arnaud Vandecasteele
categories:
- article
date: 2009-01-14 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- infobulle
- padding
title: OpenLayers, pouvoir réaliser un "padding" dans une infobulle
---

# OpenLayers, pouvoir réaliser un "padding" dans une infobulle


:calendar: Date de publication initiale : 14 janvier 2009


----

### Introduction




---


Par défaut OpenLayers permet de créer des infobulles ne pouvant afficher qu'une seule et unique zone de texte ([Popup](http://openlayers.org/dev/examples/)). La nouvelle classe présentée ci-dessous étant OpenLayers.Popup.FramedCloud afin de proposer des infobulles similaires à celle du site [EveryBlock](http://miami.everyblock.com/).


### Intégration de la nouvelle classe




---


Pour intégrer le script proposé, cela n'est pas très compliqué. Il suffit simplement de définir un lien vers la classe [OpenLayers.Popup.FramedCloudPagging](http://ks356007.kimsufi.com/arno/lib/js/OpenLayers/lib/OpenLayers/Popup/FramedCloudPagging.js). Enregistrez par exemple le fichier dans OpenLayers/lib/OpenLayers/Popup. Les deux flèches utilisées comme image sont téléchargeables ici : [flèche de gauche](http://ks356007.kimsufi.com/arno/lib/js/OpenLayers/img/pagging_left.png) et [flèche de droite](http://ks356007.kimsufi.com/arno/lib/js/OpenLayers/img/pagging_right.png). Elles doivent être placées dans le répertoire img d'OpenLayers (OpenLayers/img).




Ensuite, vous n'avez plus qu'a appeler cette nouvelle classe de la manière suivante :


`var jsonContent = [{  

newContent{  

title : "title" ,  

content : "content"  

}  

}]  

popup = new OpenLayers.Popup.FramedCloudPagging(  

"paggingPopup",  

ll,  

null,  

jsonContent,  

null, null, null  

);  

map.addPopup(popup);`  

Ce qu'il est possible de remarquer immédiatement c'est que par rapport a une utilisation habituelle la propriété **contentHTML** qui est de type string a été remplacée par un **array**. Ensuite l'essentielle des modifications sont directement des méthodes "privées" (autant que peut le faire du JS) que vous n'aurez pas besoin d'utiliser.


### Exemple d'utilisation




---








----

## Auteur

--8<-- "content/team/avdc.md"
