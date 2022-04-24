---
authors:
    - Fabien Goblet
categories:
    - article
date: 2008-11-02 10:20
description: ""
image: ''
license: default
robots: index, follow
tags:
- Google Earth
- 3D
- tour eiffel
title: 3. La Tour Eiffel en 3D
---

# 3. La Tour Eiffel en 3D

:calendar: Date de publication initiale : 02 novembre 2008

----

### Introduction

---

Il est possible d'afficher les couches 'bâtiments' présentes dans Google Earth dans l'API et donc dans sa propre page Internet.  

Nous verrons ici comment afficher la tour Eiffel et comment définir par défaut les paramètres de vue.  

### Initialisation

---

Reprendre le globe du [tutoriel n°2](http://www.geotribu.net/node/53).  

### Processus

---

Ajouter le contrôle de la navigation - en mode automatique :  

`ge.getNavigationControl().setVisibility(ge.VISIBILITY_AUTO);`  

Créer une vue :  

`var eiffel = ge.createLookAt('');`  

Puis paramétrer cette vue - latitude, longitude, altitude de la caméra, comment l'altitude est gérée (ici 50 mètres au-dessus du niveau du sol), l'angle de la caméra par rapport au nord, l'inclinaison de la caméra et la distance de la caméra :  

`eiffel.set(48.858521049096, 2.29425080771864, 50, ge.ALTITUDE_RELATIVE_TO_GROUND, 250, 75, 1100);`  

Positionnons la caméra dans la carte en 3D :  

`ge.getView().setAbstractView(eiffel);`  

Et activons le mode 'Bâtiments en 3D' - les mêmes que dans e logiciel Google Earth :  

`ge.getLayerRoot().enableLayerById(ge.LAYER_BUILDINGS, true);`  

### Code complet

---

`[Google Earth] 2. Ajoutons quelques contrôles

html { overflow:hidden; height:100%; }
body { height:100%; margin:0; }

google.load("earth", "1");
var ge = null;

function init() {
google.earth.createInstance("map3d", initCallback);
}

function initCallback(object) {
ge = object;
ge.getWindow().setVisibility(true);
ge.getOptions().setMouseNavigationEnabled(true);
ge.getNavigationControl().setVisibility(ge.VISIBILITY\_AUTO);
var eiffel = ge.createLookAt('');
eiffel.set(48.858521049096, 2.29425080771864, 50, ge.ALTITUDE\_RELATIVE\_TO\_GROUND, 250, 75, 1100);
ge.getView().setAbstractView(eiffel);

ge.getLayerRoot().enableLayerById(ge.LAYER\_BUILDINGS, true);
}`  

### Démonstration

---

[Résultat pleine page](http://88.191.39.115/fabien/geotribu/%5bgeotribu%5d_Google-Earth_tuto3.html)

### Remarques

---

Les bâtiments en France sont encore peu nombreux, mais il y a en aura de plus en plus.
L'API - <http://code.google.com/apis/earth/documentation/reference/index.html> - est à mettre en relation avec les informations de référence des objets KML - <http://code.google.com/apis/kml/documentation/kmlreference.html> .

### Conclusion

---

Il est possible d'afficher les couches présentes dans Google Earth.
On peut déclarer une caméra, et agir dessus.

**Auteur : Fabien - fabien.goblet [ at ] gmail.com**

----

## Auteur

--8<-- "content/team/fgob.md"
