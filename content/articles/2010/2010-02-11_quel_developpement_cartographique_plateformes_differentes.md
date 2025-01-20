---
title: "Quel développement cartographique pour des plateformes différentes ?"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-02-11
description: "Quel développement cartographique pour des plateformes différentes ?"
tags:
    - Android
    - carte
    - device
    - Google Maps
    - Internet
    - iPhone
---

# Quel développement cartographique pour des plateformes différentes ?

:calendar: Date de publication initiale : 11 février 2010

![icône globe](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "icône globe"){: .img-thumbnail-left }

En tant que développeur d'applications cartographiques, je suis souvent confronté au problème de portage sur différentes plateformes. Le succès actuel des smartphones - iPhone et Android en tête - oblige à revoir les développements. Doit-on privilégier une approche 'native', concevoir l'application pour qu'elle fonctionne sur tous les 'devices' ou faire un développement pour chacun ? Nous essaierons dans ce billet de faire un état des lieux des différentes API cartographiques grand public usuelles sur les principales plateformes : smartphones et ordinateurs de bureau.

L'approche dite native sera toujours la plus complète, c'est-à-dire qu'elle prend en compte les fonctionnalités que proposent les différentes plateformes : GPS, accéléromètre pour les nouveaux smartphones.

Les SDK Android et iPhone proposent en natif des classes permettant de gérer une vue cartographique basée sur l'API Google Maps. Il est possible d'utiliser pratiquement toutes les possibilités de l'API, presqu'autant qu'un développement sur ordinateur, et d'en entrevoir de nouvelles.  
Le principal avantage d'un tel développement est de pouvoir faire interagir les fonctionnalités du smartphone avec la carte : par exemple se déplacer dans la carte en bougeant l'appareil (en utilisant l'accéléromètre), appeler un n° de téléphone directement depuis une infobulle, se repérer grâce au GPS, ...  
Le problème est qu'il faut développer pour chacun des smartphones et ré-apprendre de nouveaux langages : [iPhone](http://developer.apple.com/iphone/index.action), [Android](http://developer.android.com/index.html) ou [Windows Mobile](http://msdn.microsoft.com/fr-fr/windowsmobile/default.aspx), [Blackberry](http://na.blackberry.com/eng/developers/), [Nokia](http://www.forum.nokia.com/), etc.

On entrevoit de suite les problèmes qui peuvent surgir :

- **Client** : Je veux une application qui fonctionne sur smartphone.  
- **Prestataire** : Euh, quel type de smartphone vous voulez privilégier ?  
- **Client** : Bah tous, moi j'ai un iPhone, ça marche bien, c'est sympa, ma femme un Blackberry et notre plus grand un mobile concurrent de l'iPhone, j'ai pas tout compris il m'a dit que c'était un Google Phone alors que c'est un Samsung.  
- **Prestataire** : ... [gloups]  
- **Prestataire** : Il va falloir budgeter l'application pour chaque plateforme.  
- **Client** : Ah ! Y'a pas une solution intermédiaire ?

L'approche 'on fait du Web et que du Web' semble être la plus rapide, c'est-à-dire un seul développement pour toutes les plateformes ; mais cette fois le développement se basera sur le plus petit dénominateur commun entre les devices.  
L'avantage est que chaque modification de l'application sera pris en compte immédiatement sur toutes les plateformes.  
Le problème est d'avoir une API qui soit compétitive aussi bien sur les smartphones, les tablettes et les ordinateurs. Pour le moment, seul Google avec la [version 3](http://code.google.com/apis/maps/documentation/v3/) de son API est performante sur tous les smartphones et sur les ordinateurs de bureau. Cependant celle-ci n'est pas encore à mettre en production, il reste de nombreuses fonctionnalités qui n'ont pas été importées de la version 2.  
Je n'ai aucune information concernant Bing Maps, Yahoo Maps, ou le GeoPortail.

L'approche mixte dite par 'Webview' permet d'inclure une page web dans une application. Il sera nécessaire de faire des développements sur toutes les plateformes, mais la cartographie sera commune puisqu'elle appellera une cartographie optimisée sur plusieurs plateformes. C'est un choix judicieux lorsque l'on ne veut pas s'occuper de la cartographie sur tous les devices et avoir à comprendre les classes sur chacun des SDK. Si peu ou pas d'interactions entre la carte et la plateforme sont demandées, ça peut être un bon compromis.  
Cependant, il faudra utiliser une API qui fonctionne bien partout ; et pour l'instant c'est Google.

Et quid d'OpenLayers : sera-t'il optimisé pour les smartphones ? Pour le moment je n'ai vu que ce [billet](http://www.spatiallyadjusted.com/2008/10/22/adding-touch-control-to-openlayers/) de blog qui en parle. [La question du portage](http://trac.openlayers.org/wiki/SummerOfCode#OpenLayersiPhoneDevelopment) n'est pas encore arrêtée.  
Qu'en sera-t'il de [GeoExt](http://www.geoext.org/) ? On peut espérer que la moitié du chemin sera faite dans la prochaine [minor](http://www.extjs.com/products/extjs/roadmap.php) d'ExtJS, mais il faudra qu'OpenLayers suive.

Enfin, pour illustrer ce billet, nous avons écrit 5 tutoriaux pour mieux apprécier les différentes possibilités sur iPhone, Android et ordinateurs de bureau :

1. [un tutoriel sur l'API Google Maps v3](http://geotribu.net/node/204)
2. [un tutoriel sur iPhone intégrant une WebView](http://geotribu.net/node/215)
3. [un tutoriel sur Android intégrant une WebView](http://geotribu.net/node/207)
4. [un tutoriel sur iPhone pour intégrer une MapView](http://geotribu.net/node/214)
5. [un tutoriel sur Android pour intégrer une MapView](http://geotribu.net/node/176)

----

<!-- geotribu:authors-block -->
