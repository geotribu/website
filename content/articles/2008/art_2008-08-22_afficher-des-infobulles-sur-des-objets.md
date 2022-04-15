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
- OpenLayers
- tooltips
title: Afficher des infobulles sur des objets
---

# Afficher des infobulles sur des objets


:calendar: Date de publication initiale : 22 août 2008


----

### - Introduction -




---


Pour la réalisation de la page des DCP de La Réunion j'avais besoin de pouvoir au survol de la souris d'afficher une infobulle contenant le nom de l'objet. Pour cela j'ai mis au point un petit script que je vous présenterai ci-dessous.


### - Intégration du script -




---


Après avoir [téléchargé](../../../js/toolTips.js) le script des infobulles il vous suffit de l'inclure dans votre page de la manière suivante :








### - Définir un style pour la barre d'outils -




---


Dans l'exemple qui va suivre, nous allons utiliser le script toolTips.js pour afficher le nom du pays au survol, de la souris


`marker1.events.register("mouseover",{'feature': feature1,'bgColor':'blue','fontColor':'white','opacity':'0.5'}, toolTips);  

marker1.events.register("mouseout", feature1, eraseToolTips);`


marker1 est obtenu à partir de la méthode createMarker() de l'objet Feature. Le nom de chaque pays est en fait l'ID de l'objet feature, enfin, vous avez la possibilité de personnaliser les toolTips en modifiant les valeurs de 'bgColor','fontColor','opacity'.


L'exemple ci-dessous très simpliste présente l'utilisation de ce script:








----

## Auteur

--8<-- "content/team/avdc.md"
