---
title: "iOS 4.2 - carte et accéléromètre"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-12-20
description: "iOS 4.2 - carte et accéléromètre"
tags:
    - Google Maps
    - iOS
    - Sencha
---

# iOS 4.2 - carte et accéléromètre

:calendar: Date de publication initiale : 20 décembre 2010

![icône iPhone](https://cdn.geotribu.fr/img/logos-icones/divers/iphone_logo.png "icône iPhone"){: .img-thumbnail-left }

Le développement sur smartphone devient incontournable. [CampToCamp](http://www.camptocamp.com/fr/blog/2010/12/mobile-web-gis/) accélère le développement d'une version compatible smartphone ou tablette d'OpenLayers, en gérant les interactions avec l'écran tactile. Le W3C a publié récemment les [bonnes pratiques](http://www.w3.org/TR/mwabp/) de développement de web applications pour les smartphones : en effet, devant l'extrême hétérogénéité des OS smartphones, il devient quasiment impossible pour les développeurs de déployer une application pour tout le monde. C'est là qu'intervient les web applications au travers du HTML5 : le navigateur devenant l'entrée applicative, celui-ci pouvant interagir avec des composants de plus en nombreux du smartphone - GPS, gyroscope, HTML storage, ...

Nous publiions au début de l'année un petit [article](http://www.geotribu.net/node/195) sur les différents développements possibles pour des applications mobiles : selon moi les web applications semblent en passe de gagner la partie. Les navigateurs embarqués sur les smartphones commencent à supporter l'interaction avec les capacités physiques de l'appareil. C'est ainsi que nous avons codé une petite webapp disponible sur iOS 4.2 qui permet d'utiliser les données des accéléromètres pour se mouvoir sur la carte :-)

On pivote à droite, ça bouge la carte vers l'ouest ; on pivote vers le haut, on déplace la carte vers le nord, etc.  
Les axes pour les accéléromètres sont ceux-ci : l'axe Y pour un déplacement est-ouest, l'axe X pour un déplacement nord-sud.

![iPhone Axis](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/iphone_axis.png "iPhone Axis"){: .img-center loading=lazy }

Pour cela, nous avons utilisé l'[API Google Maps v3](http://code.google.com/intl/fr-FR/apis/maps/documentation/javascript/) et le framework [Sencha Touch](http://www.sencha.com/products/touch/). Le framework n'est pas nécessaire pour utiliser l'accéléromètre de Safari iOS 4.2.  
Pardon pour ceux d'entre-vous qui ne possèdent pas d'iPhone et encore moins l'iOS 4.2, je n'ai pas réussi à faire une vidéo avec la gestion de l'accéléromètre dans le Simulateur de XCode.

Au fait, n'ayant pas d'Android sous la main, il [paraîtrait](http://www.frandroid.com/17842/android-2-2-froyo-quavons-nous/) que ça marche aussi avec le browser de Froyo ... tous les retours sont les bienvenus.

Flashouillez le QR code pour aller sur la page :-) ou sinon l'adresse c'est <http://goo.gl/hWenP>  

![iPhone](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/iphone_gmaps_accelerometer.png "iPhone"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->
