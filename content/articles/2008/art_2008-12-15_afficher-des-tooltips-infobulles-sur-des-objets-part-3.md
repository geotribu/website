---
authors:
    - Arnaud Vandecasteele
categories:
    - article
date: 2008-12-15 10:20
description: ""
image: ''
license: default
robots: index, follow
tags:
- OpenLayers
- infobulle
- tooltips
title: Afficher des tooltips (infobulles) sur des objets [part 3]
---

# Afficher des tooltips (infobulles) sur des objets [part 3]

:calendar: Date de publication initiale : 15 décembre 2008

----

### Introduction

---

La librairie OpenLayers fournit un mécanisme intéressant permettant de facilement créer de nouvelles classes en fonction de ses besoins. Une fonctionnalité qui à mon sens faisait défaut, à cette merveilleuse librairie, était la possibilité d'afficher des tooltips au passage de la souris sur des objets. Google maps propose déjà ce genre de fonctionnalité directement dans son API : [Exemple](http://econym.googlepages.com/example_maptips.htm). Je me suis donc lancé, il y a quelques mois, dans la création de ma propre classe. Celle-ci à depuis considérablement évoluée. Les changements majeurs de cette nouvelle version sont une refont complète du code qui hérite dorénavant de la classe [OpenLayers.Control](http://dev.openlayers.org/releases/OpenLayers-2.7/doc/apidocs/files/OpenLayers/Control-js.html), une meilleure intégration des fonctions natives d'OpenLayers, ainsi qu'un placement automatique du tooltips en fonction de la position du curseur.

### Mise en application

---

Pour ajouter le script il vous suffit simplement, après l'avoir [téléchargé](http://ks356007.kimsufi.com/arno/lib/js/OpenLayers/lib/OpenLayers/Control/ToolTips.js) (ou la [version compressée*](http://ks356007.kimsufi.com/arno/lib/js/OpenLayers/lib/OpenLayers/Control/ToolTips_optimize.js)), de le déclarer dans le Header de votre page. Cela se fait de la manière suivante : `OpenLayers exemples` Pour utiliser les tooltips, il faut ensuite ajouter un objet de type controle (Etape 1), puis définir une action de type mouseover (Etape 2) pour les objets sur lesquels vous souhaitez voir les tooltips s'afficher . Enfin pour chacune des actions définir les méthodes show() et hide() de la classe (Etape 3) :  `ttips = new OpenLayers.Control.ToolTips({shadow:true}); map.addControl(ttips); // Etape 1 markers.events.register("mouseover", markers, toolTipsOver); markers.events.register("mouseout", markers, toolTipsOut); // Etape 2 function toolTipsOver(e) { ttips.show({html:"My first ToolTips  

"}); } function toolTipsOut(e){ ttips.hide(); } // Etape 3`

### Propriétés et méthodes

---

Vous pouvez à loisir customiser l'apparence du tooltips, ses propriétés sont :

* textColor (string) Ex : "black"
* bold (boolean) : false
* opacity (float between 0 to 1) Ex : 1
* bgColor (string) Ex : "#FFFFFF"
* html (string) : "some content"
* shadow (boolean) : true

### Exemple

---

Ci-dessous un exemple de ce qu'il est possible de réaliser :

------------------------------ * La version compressée a été obtenue grâce au formidable outil [Packer](http://dean.edwards.name/packer/)

----

## Auteur

--8<-- "content/team/avdc.md"
