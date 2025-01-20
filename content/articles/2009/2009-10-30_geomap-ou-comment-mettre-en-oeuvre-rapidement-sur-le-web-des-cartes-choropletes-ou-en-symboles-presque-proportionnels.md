---
title: "Geomap ou comment mettre en œuvre rapidement sur le web des cartes choroplètes ou en symboles (presque) proportionnels"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-10-30
description: "Geomap ou comment mettre en œuvre rapidement sur le web des cartes choroplètes ou en symboles (presque) proportionnels"
tags:
    - carte thématique
    - choroplèthe
    - Geomap
    - Google
    - symbole proportionnel
---

# Geomap ou comment mettre en œuvre rapidement sur le web des cartes choroplètes ou en symboles (presque) proportionnels

:calendar: Date de publication initiale : 30 octobre 2009

![icône globe world](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "icône globe générique"){: .img-thumbnail-left }

Si comme nous vous utilisez régulièrement Google Analytics, la carte qui est présentée ci-dessous, ne vous est pas inconnue. Mais saviez-vous qu'il est possible également d'utiliser cette technologie de Google afin de produire une carte personnalisée et analytique. La représentation des données pouvant se faire sous la forme d'aplats de couleurs (carte choroplète) ou de symboles pseudo-proportionnels. Nous allons tout au long de ce tutoriel découvrir les possibilités de [GeoMap](http://code.google.com/intl/fr/apis/visualization/documentation/gallery/geomap.html) et de son API.

Avant de mettre les mains dans le cambouis, revenons sur le terme **pseudo-proportionnel** que nous avons évoqué en introduction. En effet, je n'ai pas pris ma règle, mais la surface des pastilles n'a pas l'air proportionnelle au nombre représenté. Mais face à la facilité de mise en place de cet outil, nous sacrifierons les principes de la sémiologie graphique ! De toute façon cela ne sera pas le premier raccourci que prendra Google en terme de représentation géographiquement correcte de données comme le souligne cet article de L. Jégou paru dans la revue [Mappemonde](http://mappemonde.mgm.fr/num20/internet/int08401.html).

Bon revenons à nos moutons et commençons à voir les possibilités de cet outil. Donc Geomap, c'est encore du Google, mais cette fois-ci ce n'est ni Google Maps ni Google Earth, mais une partie de l'[API Visualization](http://code.google.com/intl/fr/apis/visualization/documentation/gallery/geomap.html). Celle-ci permet de générer une carte (en Flash) d'un pays ou d'une région et d'associer à des points ou des pays des données afin de réaliser une analyse thématique. Dans le cas de données sur les pays, ce sera des aplats de couleurs, dans le cas de points, il s'agira de symboles presque proportionnels. En fait pas tout à fait, il faut spécifier dans les options le style de carte que nous désirons.  
Voici, ci-dessous, un rapide exemple de ce qu'il est possible de faire. Nous avons réalisé, avec GeoMap une analyse thématique portant sur les villes de plus de 100000 habitants :

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.39.115/fabien/geotribu/geomap/geomap2.html" height="375px" width="600px"></iframe>`

Les outils de navigation cartographique usuels ne sont pas disponibles. De ce fait, il n'est pas possible de se déplacer. La seule liberté qui nous est laissée est la possibilité de zoomer et dézoomer. Les données sont stockées dans des 'Datatable' qui peuvent contenir jusqu'à 400 enregistrements pour une région ou un pays donné. Si vos données ne sont pas géoréférencées, il est possible, conjointement, d'utiliser l'API de Géolocalisation de GoogleMaps. Cela peut se révéler fort utile dans le cas de données possédant une dimension spatiale non géometrique. Mais le pendant est que cela ralentit le temps de chargement (cf. la première carte) puisque pour chaque adresse il faut aller chercher des coordonnées via une requête de géolocalisation et pour cela disposer d'une [clé Google Maps](http://code.google.com/intl/fr/apis/maps/signup.html). Cela sans compter les [limites d'utilisation](http://code.google.com/intl/fr/apis/maps/terms.html) liées à la licence qui stipule que le nombre de requêtes par jour ne peut excéder 15000.

Passons maintenant aux différentes possibilités. Nous avons vu que nous pouvions réaliser des cartes chloroplètes : ici l'indice de développement humain en Amérique du Sud (sources : [Wikipédia](https://fr.wikipedia.org/wiki/Classement_IDH_des_pays). L'IDH pour la Guyane Française a été calculé par l'Université Antilles-Guyane et l'INSEE.)

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.39.115/fabien/geotribu/geomap/geomap1.html" height="375px" width="600px"></iframe>" height="375px" width="600px"></iframe>`

Il est également possible de lier des données d'un document partagé et la carte. cf. [cet exemple](http://spreadsheets.google.com/pub?key=pCQbetd-CptHo44c-Bt43eg&gid=0).

En conclusion, c'est pratique, esthétique et facile à mettre en place. Je vous invite donc à consulter [les spécifications](http://code.google.com/intl/fr/apis/visualization/documentation/gallery/geomap.html) pour toutes les subtilités.  
Je pense que je vais réutiliser souvent cet outil surtout dans le cadre de présentation rapide. Même si Geomap n'est en rien comparable aux réalisations (presque artistiques) de [Geoclip](http://www.geoclip.net/fr/) (enfin pas pour le moment ... on ne sait jamais avec Google), elle apporte tout de même une certaine souplesse d'utilisation. Néanmoins, il faut garder à l'esprit qu'il n'est pas possible d'utiliser des données spatiales stockées en base, de faire une mise en page, d'exporter, de faire des analyses thématiques.

----

<!-- geotribu:authors-block -->
