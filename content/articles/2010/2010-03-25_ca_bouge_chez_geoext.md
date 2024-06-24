---
title: "Ca bouge chez GeoExt"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-03-25
description: "Ca bouge chez GeoExt"
tags:
    - GeoExt
    - JavaScript
    - librairie
---

# Ca bouge chez GeoExt

:calendar: Date de publication initiale : 25 mars 2010

![logo GeoExt](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/geoext.png "logo GeoExt"){: .img-thumbnail-left }

Cela faisait longtemps que nous n'avions pas discuté de [GeoExt](http://www.geoext.org/lib/index.html). C'est pourquoi je reviens avec non pas une, mais deux grandes nouvelles. Tout d'abord, la sortie de la [version 0.7](http://trac.geoext.org/wiki/Release/0.7/Notes) ([dl](http://www.geoext.org/downloads.html)) et ensuite la mise en place de l'outil [custom build tool](http://geoext.org/builder/v0.6.html)

## GeoExt en version 0.7

La nouveauté majeure apportée par cette nouvelle version est une suite complète d'outil permettant d'imprimer la carte. Ainsi trois nouveaux plugins, [PrintProviderField](http://dev.geoext.org/trunk/geoext/examples/print-form.html), [PrintPageField](http://dev.geoext.org/trunk/geoext/examples/print-form.html), [PrintExtent](http://dev.geoext.org/trunk/geoext/examples/print-extent.html) et un nouveau widget, [PrintMapPanel](http://dev.geoext.org/trunk/geoext/examples/print-preview.html) ont été ajoutés.

De nombreuses autres améliorations ont également été apportées. Je vous invite à consulter la [liste complète](http://trac.geoext.org/query?group=type&resolution=fixed&milestone=0.7&order=component) pour plus d'informations.

## Custom Build Tool

Même si les débits internet sont de plus en plus importants, il est toujours intéressant d'optimiser le temps de chargement des librairies. Pour cela différentes techniques existent (mise en cache, minify...). L'une d'entre elle consiste à ne charger que les classes utilisées par l'application. Ext propose déjà un service de ce genre et c'est au tour de GeoExt via [custom build tool](http://geoext.org/builder/v0.6.html) de faire de même.

Pour OpenLayers, s'il n'existe aucun outil similaire en ligne, vous pouvez toujours le faire via build.py inclus dans la librairie. Un [tutoriel](http://geotribu.net/node/52) expliquant la marche à suivre est disponible sur GeoTribu.

La [version 1.0](http://trac.geoext.org/milestone/1.0) de GeoExt se profile à l'horizon. Celle-ci semble aller bien au-delà d'une simple fusion d'OpenLayers et d'Ext en proposant notamment des connexions à certaines fonctionnalités des serveurs cartographiques comme c'est le cas, par exemple, pour la possibilité d'imprimer la carte. Il ne reste plus qu'à prendre son mal en patience et attendre cette future release.

----

<!-- geotribu:authors-block -->
