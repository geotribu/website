---
title: Afficher des infobulles sur des objets [Part 2]
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-08-31
description: Afficher des infobulles sur des objets [Part 2]
tags:
    - OpenLayers
---

# Afficher des infobulles sur des objets [Part 2]

:calendar: Date de publication initiale : 31 août 2008

## Introduction

![Logo OpenLayers](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/openlayers.png){: .img-thumbnail-left }

Lors d'un précédent tutoriel nous avions appris comment afficher des infobulles sur un marker. Bon me direz-vous mais à quoi sert ce nouveau tuto ? Tout simplement l'ancien script était trop artisanal. En effet, la librairie OpenLayers offre des mécanismes simples d'enrichissement de classes qui n'ont pas été exploités.
Ce [nouveau script](http://ks356007.kimsufi.com/arno/geotribu/applications/js/toolTips_ol.js "script toolTips V2") pallie à ce manque en ajoutant une spécification supplémentaire à la classe marker. Cette façon de faire permet une plus grande souplesse de travail et une meilleur portabilité à long terme.

Je dois souligner que le [code original](http://trac.openlayers.org/ticket/751 "Script label OpenLayers") n'est pas de moi, je n'ai fais que rajouter certaines options supplémentaires.

## Ajouter le script

Pour ajouter le script il vous suffit simplement de le déclarer dans le Header de votre page. Cela se fait de la manière suivante :

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
 <head>
   <meta http-equiv="content-type" content="text/html; charset=utf-8"/>
   <title>OpenLayers exemples</title>
   <script src="./js/OpenLayers/OpenLayers.js" type="text/javascript"></script>
   <script src="./js/OpenLayers/toolTips.js" type="text/javascript"></script>
</head>
```

## Utiliser le script

La classe OpenLayers.Marker.Label hérite de OpenLayers.Marker en lui ajoutant des spécifiés supplémentaires. Le seul paramètre obligatoire est Label. C'est lui qui définit le texte à afficher :

```javascript
var ll = new OpenLayers.LonLat(0,10);  
var myLabel = "![](http://www.photo-libre.fr/mer/100b.jpg)Mer";  
fcolor="red";  
bckColor="yellow";  
var options = {mouseOver:true,marginLeft:"30px",marginTop:"0px",bckColor:"#9AD3FF",fontColor:"#043E6A",fontBold:true};  
marker1 = new OpenLayers.Marker.Label(ll,null,myLabel,options);  
mlayer.addMarker(marker1);
```

Voici les propriétés et méthodes de cette classe :

| Propriétés |  |
| :--------------- |:---------------|
| labelDiv | DOMElement |
| label | String |
| mouseOver | Boolean |
| labelClass | String |
| events | OpenLayers.Events |
| div | DOMElement |
| onlyOnMouseOver | Boolean |
| marginLeft | String |
| marginTop | String |
| fontColor | String |
| bckColor | String |
| opacity | String |
| fontBold | String |

| Méthodes | |
| :--------------- |:---------------|
| OpenLayers.Marker.Label | Constructeur |
| destroy | Supprime le marker et l'infobulle |
| draw | Dessine le marker et l'infobulle |
| onmouseover | events |
| onmouseout | events |
| setLabel | Définit un nouveau texte pour le label |
| setLabelVisibility | Définit la visibilité du label |
| getLabelVisibility | Permet de savoir si l'infobulle est affichée (boolean) |

Télécharger le script : Script [ToolTips V2](http://ks356007.kimsufi.com/arno/geotribu/applications/js/toolTips_ol.js "script toolTips V2")

**Et un exemple concret :**

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://geotribu.net/applications/tutoriaux/openlayers/tooltips_v2/toolTips_v2.html" width="100%" height="500px"></iframe>`

----

<!-- geotribu:authors-block -->
