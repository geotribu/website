---
title: "MapChat, ou la Géocollaboration OpenSource"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-02-15
description: "MapChat, ou la Géocollaboration OpenSource"
tags:
    - géocollaboration
    - open source
---

# MapChat, ou la Géocollaboration OpenSource

:calendar: Date de publication initiale : 15 février 2010

![logo MapChat](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/logo_mapchat.jpg "logo MapChat"){: .img-thumbnail-left }

Lors du précédent [billet](http://geotribu.net/node/212), nous avions rapidement abordé la notion de GéoCollaboration. Il est temps de mettre en application cette notion que nous illustrons avec l'application [MapChat](http://mapchat.ca/) dont l'objectif est de fournir, au sein d'une même interface cartographique, les outils nécessaires à une géocollaboration.

Ce projet a débuté en 2003 à l'université de Waterloo grâce à l'initiative du Dr. G. Brent Hall. Mais ce n'est qu'en 2005 que la 1ere version est disponible. Celle-ci est alors utilisée dans divers projets de type PPGIS (public participation GIS). La seconde version, dont le développement a débuté en 2008, est assurée conjointement par Michael G. Leahy en collaboration avec le Dr. Hall.

Au niveau de l'infrastructure, nous sommes sur des standards OpenSource. Côté background, nous retrouvons MapServer comme serveur cartographique, PostgreSQL/PostGIS comme base de données et enfin Zend comme framework Php. Côté interface, c'est un mélange de Ka-Map's et de jQuery.

![Architecture](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/oswebmapping2009chapter.architecture.jpg "Architecture"){: .img-center loading=lazy }

*source : [MapChat](http://mapchat.ca/files/images/publications/oswebmapping2009chapter.architecture.jpg)*

La carte générale qui s'affiche au départ est volontairement dépouillée. Il suffit ensuite à partir d'un click droit, d'ajouter les éléments que vous désirez. Chacun de ces éléments peut être déplacé sur la carte. Au niveau de la boite à outils il est possible notamment, de dessiner des formes, d'identifier des objets sur la carte, de zoomer et de dezoomer...

Jusque à maintenant, au niveau des fonctionnalités, rien d'exceptionnel me direz vous. Mais une fois la partie chat affichée sur la carte toute l'application prend alors son intérêt. En effet, il est possible à partir de cette interface de lier des objets ou la carte courante à un message du chat. Imagions que dans un projet d'aménagement du territoire il soit question de l'emplacement d'un nouveau centre commercial. Nous créons donc un nouveau sujet de discussion que nous lions à la forme que nous venons de dessiner sur la carte et qui représente le futur emplacement de la zone commerciale. Sur le chat, chacun est libre d'ajouter son commentaire et participe ainsi à la prise de décision.

![MapChat](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/mapchat_commerce.png "MapChat"){: .img-center loading=lazy }

Comme nous le disions précédemment, ce genre d'application trouve tout son intérêt dans des initiatives de type PPGIS. Néanmoins, il faut avouer que l'utilisation demande tout de même une certaine compétence en informatique. Ce qui peut être un frein à l'adoption de ce genre d'outil, "some people are intimidated by the technology" [Daniel Weine 2002]. Enfin, il faut avouer qu'il manque encore à cet outil quelques fonctionnalités. Il n'est par exemple pas possible de modifier une forme précédemment créée. Difficile dans ce cas de réaliser des scenarios et d'arriver ainsi par itérations cartographiques successives à un consensus comme nous pourrions le faire avec un système de type [WikiSIG](http://wikisig.scg.ulaval.ca/) [Mericskay, Roche 2009].

## Référence

Boris Mericskay, Stéphane Roche 2009. Cartographie numérique en ligne nouvelle génération : impacts de la néogéographie et de l’information géographique volontaire sur la gestion urbaine participative [[+](http://ulaval.academia.edu/documents/0037/0017/Article_Hyperurbain2_2009.pdf)]

Daniel Weiner, Trevor M. Harris , William J. Craig 2002. Community Participation and Geographic Information Systems [[+](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.15.4296)]

----

<!-- geotribu:authors-block -->
