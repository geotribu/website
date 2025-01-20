---
title: "YQL Geo Library, la localisation facilement"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-03-15
description: "YQL Geo Library, la localisation facilement"
tags:
    - géolocalisation
    - JavaScript
---

# YQL Geo Library, la localisation facilement

:calendar: Date de publication initiale : 15 mars 2010

![icône globe](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "icône globe"){: .img-thumbnail-left }

Les librairies javascript orientées cartographie et localisation fleurissent sur le web. Mais, si cette richesse est bénéfique, passer de l'une à l'autre nécessite toujours un temps d'adaptation. En effet, il faut se réhabituer à l'API, aux différents objets et méthodes, à l'architecture...  
Imaginez maintenant, une librairie de plus haut au niveau qui aurait à charge d'unifier ([wrapper](https://en.wikipedia.org/wiki/Wrapper_library)) tout cela au sein d'une même API? C'est ce que fait [YQL Geo Library](http://isithackday.com/hacks/geo/yql-geo-library/).

Vous pouvez ainsi grâce à elle accéder indépendamment aux six librairies suivantes :

- [Yahoo Placemaker](http://developer.yahoo.com/geo/placemaker)
- [Yahoo GeoPlanet](http://developer.yahoo.com/geo/geoplanet/)
- [jsonip.appspot.com](http://jsonip.appspot.com)
- [IP location tools](http://iplocationtools.com/ip_location_api.php)
- [W3C Geo location](http://dev.w3.org/geo/api/spec-source.html)
- [Flickr.places.findByLatLon](http://www.flickr.com/services/api/flickr.places.findByLatLon.html)

La construction d'une requête de géolocalisation se fait très simplement à partir de la méthode **yqlgeo.get(what,callback)**. "What" peut être aussi bien un nom de ville, une adresse IP ou encore une position géographique. Par exemple, pour connaitre les coordonnées de la ville de Paris, le code à écrire est le suivant :

```javascript
yqlgeo.get('paris,fr',function(o){
  alert(o.place.name+' ('+
    o.place.centroid.latitude+','+
    o.place.centroid.longitude+
  ')');
})
```

Ce qui affichera :

`Paris (48.856918,2.341210)`

Vous trouverez de nombreux autres exemples sur le site. En tout cas, je dois avouer que [YQL Geo Library](http://isithackday.com/hacks/geo/yql-geo-library/) est un véritable concentré de simplicité et d'efficacité.

----

## Sources

- [Ajaxian](http://ajaxian.com/archives/yql-geo-library-all-your-geo-needs-in-pure-javascript)  
- [Et encore chez Benjamin Chartier](http://benjamin.chartier.free.fr/pro/?p=1694)

----

<!-- geotribu:authors-block -->
