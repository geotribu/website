---
title: "7. Découverte de l'API Google Maps Static - Interlude ..."
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2008-08-24
description: "7. Découverte de l'API Google Maps Static - Interlude ..."
tags:
    - Google Maps
---

# 7. Découverte de l'API Google Maps Static - Interlude

:calendar: Date de publication initiale : 24 août 2008

:warning: L'API Google Maps v2 est dépréciée depuis le 19 mai 2010.

## Introduction

![logo Google](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/google/google.webp "logo Google"){: .img-thumbnail-left }

Google propose une version simplifiée de l'API Google Maps : l'[API Google Maps Static](http://code.google.com/intl/fr/apis/maps/documentation/staticmaps/). Cette API est destinée aux développeurs qui ne veulent pas utiliser l'API standard ou pour les développements qui ne nécessitent pas de déplacement dans la carte, de changement de zoom ou de changement de vue.  

## Carte simple

Une carte avec l'API Google Maps Static est définie par une URL :  

`http://maps.google.com/staticmap?center=43.57691664771851,1.402451992034912&zoom=15&size=400x400&key=votre_clé_ici`  

Pour le résultat suivant :

- L'attribut `center` prend les coordonnées du centre de la carte.
- L'attribut `zoom` définit le niveau de zoom.
- L'attribut `size` définit la taille en pixel de la carte - la taille maximale possible est de 640 x 640.

## Carte avec un marqueur

L'ajout d'un marqueur sur la carte se fait de la façon suivante :  

`http://maps.google.com/staticmap?center=43.57691664771851,1.402451992034912&zoom=15&size=400x400&markers=43.57691664771851,1.402451992034912,bluem&key=votre_clé_ici`  

Qui produit cette carte :

![Carte Google](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2008/staticmap2-2.gif "Carte Google"){: .img-center loading=lazy }

L'attribut `marker` permet d'ajouter un marqueurs sur la carte, il prend comme valeur les coordonnées du marqueur ainsi que le cas échéant la couleur du marqueur suivi de la letter 'm' pour lettre un M dans le marqueur.  

## Laissez faire Google

L'attribut spécial `span` permet de ne pas spécifier un niveau de zoom mais en précisant une longitude et une latitude en degrés de laisser faire l'API.  

Exemple d'une carte centrée sur Toulouse, de taille 640 x 640, de 1° de hauteur et de 1° de largeur :  

`http://maps.google.com/staticmap?center=43.57691664771851,1.402451992034912&span=1,1&size=640x640&key=votre_clé_ici`  

Qui donne la carte ci-dessous :

![Carte Google](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2008/staticmap3-2.gif "Carte Google"){: .img-center loading=lazy }

## Conclusion

La création d'une carte simple sous forme d'image se fait facilement grâce à une URL.  

Elle permet de créer une carte très rapidement et de l'enregistrer pour enrichir un document (attention toutefois aux droits d'utilisation).  

La génération d'une carte nécessite quand même d'un clé Google Maps - [http://code.google.com/apis/maps/signup.html](http://code.google.com/apis/maps/signup.html) - si vous ne possédez pas d'espace sur un serveur Internet, vous pouvez demander une clé avec l'adresse [http://localhost](http://localhost) auquel cas il vous faudra quand même un serveur Web installé en local sur votre ordinateur.  

Si vous avez la flemme, vous pouvez générer l'URL directement en ligne - [http://gmaps-samples.googlecode.com/svn/trunk/simplewizard/makestaticmap.html](http://gmaps-samples.googlecode.com/svn/trunk/simplewizard/makestaticmap.html).  

----

<!-- geotribu:authors-block -->
