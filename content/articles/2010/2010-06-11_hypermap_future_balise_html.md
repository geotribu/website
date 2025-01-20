---
title: "hypermap, future balise HTML ?"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-06-11
description: "hypermap, future balise HTML ?"
tags:
    - HTML
    - JavaScript
    - OpenLayers
    - open source
---

# hypermap, future balise HTML ?

:calendar: Date de publication initiale : 11 juin 2010

La cartographie et la localisation font partie intégrante de notre environnement web actuel. Le succès d'application comme GoogleMaps avec plus de 10 millions de cartes créées[^1] ou encore Google Earth qui recense plus de 500 millions de téléchargements[^2] en est la preuve concrète. Cette ouverture vers le spatial a apporté, à mon avis, autant de bouleversements que l'ouverture sociale du Web 2.0.

----

La plupart des cartes que j'ai pu voir se résument à quelques marqueurs auxquels ont été ajoutées des informations complémentaires. Rien de très méchant "cartographiquement" parlant. Néanmoins et même si les API sont relativement faciles à comprendre, il faut être un minimum intéressé par la programmation pour créer sa propre application.

D'où l'idée que je développe dans ce billet, celle d'une futur balise HTML `<hypermap></hypermap>`, qui serait interprétée directement par votre navigateur. Celle-ci permettrait de créer automatiquement une carte en fonction des caractéristiques associées. Un exemple de squelette HTML est présenté ci-dessous afin d'illustrer mon propos :

```html
<body>
    <hypermap>
        <mapOptions>
            <zoom>4</zoom>
            <lonlat>273950;5841011</lonlat>
            <static>False</static>
        </mapOptions>
        <layers>
            <layer>OSM</layer>
        </layers>
        <control>
        </control>
        <data>
            <point>
                <lonlat>313385;6242152</lonlat>
                <content>Paris</content>  
            </point>
            <point>
                <localisation>Nice,France</localisation>
                <content>Nice</content>  
            </point>
        </data>
    </hypermap>
  </body>
```

Détaillons un peu plus en détails chacune des sous balises :

- mapOptions : spécifie les caractéristiques générales de la carte
- layers : défini les couches à afficher
- control : ajoute des contrôles spécifiques à la carte
- data : définie les données qui seront affichées. Les positions peuvent être données au format longitude/latitude ou simplement nommées par leur localisation (celle-ci sera converti grâce à la librairie [YQL](http://developer.yahoo.com/yql/))

De la théorie à la pratique, il y a tout de même un monde. C'est pourquoi, j'ai décidé d'implémenter cette idée afin de valider cette preuve de concept ([exemple](http://geotribu.net/applications/tutoriaux/openlayers/hypercarte/hypermap_prototype.html)). Pour cela j'ai utilisé comme librairie [OpenLayers](https://openlayers.org/) et [Prototype](http://www.prototypejs.org/) et comme source de données [OpenStreetMap](https://www.openstreetmap.org/). L'architecture du DOM est la même que l'exemple présenté ci-dessus. Si vous affichez le code source de la page, vous ne verrez rien d'autre qu'une balise hypermap !

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://geotribu.net/applications/tutoriaux/openlayers/hypercarte/hypermap_prototype.html" width="600" height="500" scrolling="no" bordure="0px"></iframe>`

[^1]: [http://maps-forum-announcements.blogspot.com/2009/01/juicy-facts-in-goog...](http://maps-forum-announcements.blogspot.com/2009/01/juicy-facts-in-google-maps-world.html)
[^2]: [http://www.gpsbusinessnews.com/Google-Earth-over-500-million-downloads_a...](http://www.gpsbusinessnews.com/Google-Earth-over-500-million-downloads_a1307.html)

----

<!-- geotribu:authors-block -->
