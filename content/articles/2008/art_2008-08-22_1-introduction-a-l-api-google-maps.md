---
authors:
- Fabien Goblet
categories:
- article
date: 2008-08-22 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- tutoriel
- Google Maps
title: 1. Introduction à l'API Google Maps
---

# 1. Introduction à l'API Google Maps


:calendar: Date de publication initiale : 22 août 2008


----


![attention_light.jpg](/sites/default/files/Tuto/img/attention_light.jpg)**L'API Google Maps v2 est dépréciée depuis le 19 mai 2010.**


### Introduction




---


****L'[API Google Maps](http://code.google.com/intl/fr/apis/maps/) permet d'intégrer une carte semblable à [celle de Google](http://maps.google.fr/maps?hl=fr&tab=wl) dans ses pages Web en utilisant un peu de Javascript.****


### Appel à l'API grâce à la clé




---


****Pour utiliser l'API Google Maps, il est nécessaire d'obtenir une clé gratuite à cette [adresse](http://code.google.com/intl/fr/apis/maps/signup.html). Et d'écrire cette ligne dans le de la page HTML qui contiendra la carte Google Maps :**** 


* v=2.x : ici on note la version de l'API utilisée dans notre projet : - 2.x correspond à la dernière version de l'API - 2.s correspond à la dernière version stable de l'API - 2 correspond à la version courante Détail des changements de l'API : <http://mapki.com/wiki/Changelog>


****NB : Nous utiliserons par la suite toujours la version courante de l'API afin d'éviter les [mauvaises surprises](http://www.geotribu.net/node/102).****


### Code Javascript de déclaration de la carte




---


****Nous déclarons la fonction initialize() qui sera chargée lors du chargement de la page Web. Cette fonction contient les instructions afin de déclarer la carte Google Maps. La structure conditionnelle 'if then else' permet d'alerter l'utilisateur si son navigateur n'accepte pas le JavaScript grâce à la fonction GBrowserIsCompatible(). Nous déclarons ensuite l'objet map qui sera affiché dans le bloc dont l'identifiant sera 'map\_canvas' de la page HTML : `var map = new GMap2(document.getElementById('map'));` et définissons un centre et un niveau de zoom pour cet objet. `map.setCenter(new GLatLng(43.57691664771851, 1.402451992034912),15);`****


### Code HTML




---


****Afin d'afficher la carte, il est nécessaire de déclarer un bloc div qui contiendra la carte :**** 



****Et il faut appeler la fonction initialize() lors du chargement de la page :  La fonction GUnload() permet de libérer la mémoire lorsque l'on quitte la page Web.****


### Code complet




---


******Code :** `[Google Maps] 1. Introduction à Google Maps`****




### Démonstration




---



&amp;lt;/p&amp;gt; &amp;lt;a href="<http://88.191.142.86/fabien/geotribu/tuto/gmaps-v2/tuto1.html>" target="\_blank"&amp;gt;Résultat pleine page&amp;lt;/a&amp;gt; &amp;lt;br/&amp;gt; &amp;lt;h3&amp;gt;Remarques&amp;lt;/h3&amp;gt; &amp;lt;hr/&amp;gt; &amp;lt;ul&amp;gt; &amp;lt;li&amp;gt;Le système de coordonnées dans Google Maps est le WGS84 (système géodésique du système GPS ) - <http://fr.wikipedia.org/wiki/WGS_84> . &amp;lt;li&amp;gt;Le niveau de zoom est généralement défini par un chiffre entre 0 et 18. Cependant, il est parfois possible d'aller un peu plus loin : [http://maps.google.com/maps?q=15.29854,19.429741&amp;amp;ie=UTF8&amp;amp...](http://maps.google.com/maps?q=15.29854,19.429741&amp;amp;ie=UTF8&amp;amp;ll=15.298539,19.42974&amp;amp;spn=0.000117,0.000154&amp;amp;t=h&amp;amp;z=23) &amp;lt;/ul&amp;gt; &amp;lt;br/&amp;gt; &amp;lt;h3&amp;gt;Conclusion&amp;lt;/h3&amp;gt; &amp;lt;hr/&amp;gt; La création d'une simple carte et l'intégration de celle-ci dans une page Internet est très facile. Cependant dans celle-ci, il n'est possible que de se déplacer - grâce à la souris, de zoomer d'un level - doucle-clic gauche et de dézommer - double-clic droit. Ces options sont intégrées par défaut lors de l'appel au constructeur et nous verrons par la suite comment enrichir l'interface pour pouvoir naviguer dans la carte et comment ajouter des informations sur cette dernière. Il est possible de développer ses propres applications en localhost : pour ceci, il faut demander une clé spécifique pour l'adresse <http://locahost/> . &amp;lt;br/&amp;gt; &amp;lt;h3&amp;gt;Liens&amp;lt;/h3&amp;gt; &amp;lt;hr/&amp;gt; &amp;lt;ul&amp;gt; &amp;lt;li&amp;gt;Récupérer une clé Google Maps : <http://code.google.com/apis/maps/signup.html> &amp;lt;li&amp;gt;La documentation complète de l'API Google Maps : <http://code.google.com/intl/es/apis/maps/documentation/reference.html> &amp;lt;/ul&amp;gt; &amp;lt;br/&amp;gt; &amp;lt;strong&amp;gt;Auteur : Fabien - fabien.goblet [ at ] gmail.com&amp;lt;/strong&amp;gt; &amp;lt;br/&amp;gt;&amp;lt;/div&amp;gt;




----

## Auteur

--8<-- "content/team/fgob.md"
