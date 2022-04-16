---
authors:
- '?'
categories:
- article
date: 2009-11-27 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- Android
- Google Maps API
title: Quelques fonctions basiques pour votre carte Google Maps sur Android
---

# Quelques fonctions basiques pour votre carte Google Maps sur Android


:calendar: Date de publication initiale : 27 novembre 2009


----

### Introduction




---


Nous avons appris à mettre une carte dans une application Android, mais une carte mal positionnée, sans fonction de zoom, sans autre vue que la carte basique, est une carte sans intérêt. Comment mettre en oeuvre tout cela. C'est assez simple.


### Le contrôleur de zoom




---


Pour pouvoir afficher le contrôleur de zoom dès que l'utilisateur touche sa carte, il suffit de quelques lignes de codes, que vous pouvez insérer dans la méthode onCreate()  `public void onCreate(Bundle savedInstanceState) { super.onCreate(savedInstanceState); setContentView(R.layout.main); MapView mapView = (MapView) findViewById(R.id.mapview); mapView.setBuiltInZoomControls(true); }`  R.id.mapview fait référence à l'identifiant de votre carte dans son layout , ici dans /res/layout/main.xml. Il suffit alors d'appliquer la méthode setBuiltInZoomControls avec le paramètre true; si vous le passez à false, cela permet d'enlever ce contrôleur. Voici le résultat :


![](http://88.191.39.115/fabien/geotribu/logos/android_tuto_2_zoom.png)


### Une vue satellite




---


Pour changer le mode d'affichage pour une vue satellite, il suffit d'appliquer à votre mapView la méthode setSatelitte avec le paramètre true.  `public void onCreate(Bundle savedInstanceState) { super.onCreate(savedInstanceState); setContentView(R.layout.main); MapView mapView = (MapView) findViewById(R.id.mapview); mapView.setBuiltInZoomControls(true); mapView.setSatellite(true); }`  Et voici le résultat:


![](http://88.191.39.115/fabien/geotribu/logos/android_tuto_2_sat.png)


### Centrer la carte sur un point précis




---


Pour positionner sa carte au bon endroit, il suffit d'utiliser quelques méthodes sur la classe MapControler.  `public void onCreate(Bundle savedInstanceState) { super.onCreate(savedInstanceState); setContentView(R.layout.main); MapView mapView = (MapView) findViewById(R.id.mapview); mapView.setBuiltInZoomControls(true); // centrer la carte sur la station de métro Grands Boulevards à Paris double lat = 48.87153740744375; double lon = 2.342920216006007; GeoPoint gp = new GeoPoint((int) (lat * 1E6), (int) (lon * 1E6)); MapController mc = mapView.getController(); mc.setCenter(gp); mc.setZoom(17); }`  Il suffit de créer un GeoPoint qui est caractérisé par une latitude et une longitude. Les nombres en format double sont multipliés par 1000000 et castés en int. Ensuite on donne ce point à la méthode setCenter qui s'applique sur le MapController de la mapView. On peut ensuite appliquer un niveau de zoom, suivant ce que l'on souhaite voir. Et voici le résultat:


![](http://88.191.39.115/fabien/geotribu/logos/android_tuto_2_center.png)


### Dois-je prendre la route ?




---


Pour finir ce tutoriel, on peut ajouter une couche de trafic routier par exemple.  `public void onCreate(Bundle savedInstanceState) { super.onCreate(savedInstanceState); setContentView(R.layout.main); MapView mapView = (MapView) findViewById(R.id.mapview); mapView.setBuiltInZoomControls(true); // centrer la carte sur la station de métro Grands Boulevards à Paris double lat = 48.87153740744375; double lon = 2.342920216006007; GeoPoint gp = new GeoPoint((int) (lat * 1E6), (int) (lon * 1E6)); MapController mc = mapView.getController(); mc.setCenter(gp); mc.setZoom(15); mapView.setTraffic(true); }`  Il suffit d'utiliser la méthode setTraffic avec le paramètre true. Donc, je ne vais pas prendre la voiture :


![](http://88.191.39.115/fabien/geotribu/logos/android_tuto_2_traffic.png)


### Remarques




---


Liens utiles : Google APIs Add-On API Level 4 : [http://code.google.com/intl/fr/android/add-ons/google-apis/reference/ind...](http://code.google.com/intl/fr/android/add-ons/google-apis/reference/index.html)


### Conclusion




---


Ce second tutoriel à propos d'Android est bien plus simple que le premier. Il s'agit ici de jouer un peu avec l'API Google.  
**Auteur : Loïc - loic.goblet [ at ] gmail.com**




----

## Auteur

![Portait de ?](https://cdn.geotribu.fr/images/internal/charte/geotribu\_logo\_64x64.png){: .img-rdp-news-thumb }
**?**
