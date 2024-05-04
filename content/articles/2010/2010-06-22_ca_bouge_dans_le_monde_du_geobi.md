---
title: "Ça bouge dans le monde du GeoBI"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-06-22
description: "Ça bouge dans le monde du GeoBI"
tags:
    - BI
    - ETL
    - GeoBI
    - géodécisionnel
    - open source
---

# Ça bouge dans le monde du GeoBI

:calendar: Date de publication initiale : 22 juin 2010

![logo SOLAP](https://cdn.geotribu.fr/img/logos-icones/divers/solap.png "logo SOLAP"){: .img-thumbnail-left }

Le monde du GeoBI OpenSource a été, ces derniers jours, particulièrement actif. En effet, entre la sortie de nouvelles versions de logiciels et la création de nouveaux partenariats ce sont au total quatres nouvelles qui seront présentées dans ce billet. Tout d'abord, nous commencerons par le projet GeoBi initiative. Ensuite, nous aborderons les évolutions des deux ETLs spatiaux Geokettle et Spatial Data Integrator.

## GeoBI Initiative

![logo GeoBI](https://cdn.geotribu.fr/img/logos-icones/divers/GeoBI.png "logo GeoBI"){: .img-thumbnail-left }

Initié par cinq compagnies[^1] et une université[^2], l'initiative GeoBI vise à regrouper l'ensemble des personnes évoluant dans le monde du géodécisionnel OpenSource. Ce projet est d'autant plus important qu'il allie recherche appliquée et partenariat industriel. Cette information a été largement commentée aussi bien sur les [blogs francophones](http://www.osbi.fr/) qu'[internationaux](http://fabiodovidio.blogspot.com/2010/06/geobi-initiative-has-been-launched.html).

Mais, le géodécisionnel qu'est-ce donc ? Ce domaine réuni deux mondes qui jusqu'alors se côtoyaient peu, celui de l'informatique décisionnelle (aussi appelée Business Intelligence) et celui des Systèmes d'information Géographiques (SIG). Nous avions déjà eu l'occasion d'aborder ce sujet au cours de deux précédents billets : Les ETL spatiaux OpenSource, à pieds joints dans l'informatique Géodécisionnelle[^3] et la géomatique décisionnelle, l'avenir du SIG?[^4]. Si vous souhaitez plus d'informations, je vous renvoie donc à ces derniers ou au site [SpatialOLAP](http://spatialolap.scg.ulaval.ca/default.asp) qui représente une des meilleures ressources disponibles sur le WEB.

Néanmoins, si le domaine du SOLAP porté par le docteur Yvan Bédard, commence à être relativement mature, son incursion dans le domaine de l'Open Source est récente. Mais, les potentialités sont nombreuses. En effet, selon une étude menée par Gartner, le marché de la Business Intelligence Open Source, et par extension celui du GeoBI, devrait être multiplié par 5 d’ici 2012[^5]. C'est pourquoi, l'initiative GeoBI est un premier pas important vers une consolidation des acteurs et des projets orientés géomatique décisionnelle.

En effet, pour le moment arriver à comprendre l'univers du GeoBI relève du parcours du combattant. Ce constat s'explique tout d'abord en raison de l'évolution rapide que celui-ci a connu en l'espace de quelques mois. Mais aussi par la difficulté à identifier clairement qui fait quoi du fait que chacun développe sa propre solution en empruntant des briques logiciels à l'un ou l'autre des acteurs.

C'est pourquoi, pour le marché comme les utilisateurs cette initiative est à saluer. Celle-ci permettra je l'espère une harmonisation des développements et un regroupement des acteurs autour d'objectifs communs qui sont :

- une meilleure coordination des travaux
- faire connaitre la BI au monde des SIG et inversement
- promouvoir une meilleure intégration entre la BI et les SIG
- créer d'une base de connaissance libre
- travailler en collaboration avec Open Geospatial Consortium (OGC) afin de définir de nouveaux standards (geoMDX)
- ...

Si vous souhaitez plus de détails sur ce projet, je vous invite à consulter le [manifeste](http://www.spagoworld.org/xwiki/bin/view/GeoBI/Manifesto) qui est disponible également en [français](http://www.osbi.fr/?p=1366) si l'anglais vous fait peur :)

## Spatialytics

Passons maintenant aux nouveautés concernant les outils D'extraction, de Transformation et de Chargement (en anglais ETL).

[Spatialytics](http://www.spatialytics.org/) est le nom de l'entreprise fondée par Luc Vaillancourt, le fondateur de l'agrégateur de nouvelles [media baliz geospatial](http://media.baliz-geospatial.com/), et Thierry Badard, le créateur de l'une des premières suite décisionnelles OpenSource (GeoKettle, GeoMondrian et SolapLayers). Spatialytics est également le tout premier revendeur de la suite [OpenGeo](http://blog.opengeo.org/2010/06/15/our-first-reseller/) (en [fr](http://www.spatialytics.com/fr/blogue/spatialytics-annonce-un-partenariat-avec-opengeo-pour-la-revente-de-la-opengeo-suite/?utm_source=twitterfeed&utm_medium=twitter)).

L'un de leurs produits phares est GeoKettle, un ETL spatial OpenSource basé sur [Pentaho Data Integration](http://www.neogeo-online.net/blog/archives/304/) (anciennement Kettle). ETL est l'acronyme d'Extract, Transform and Load, c'est-à-dire un outil permettant de charger, en entrée, des flux de données provenant de différentes sources, de leur faire subir des traitements (filtrage, agrégation...) et de les réinjecter ensuite en base de données (ou dans un des nombreux formats disponibles). Habituellement, cet outil sert à alimenter un cube de données (data warehouse) mais vous pouvez également l'utiliser au sein de votre activité habituelle. Comme le souligne [vector1media](http://vector1media.com/spatialsustain/how-will-the-geospatial-data-market-evolve-over-the-next-ten-years.html?utm_source=feedburner&utm_medium=feed&utm_campaign=Feed%3A+SpatialSustain+%28Spatial+Sustain%29), l'un des challenges des 10 prochaines années, dans le domaine de la géomatique, sera l'extraction et la gestion automatique des données. C'est dire l'importance que vont prendre ce genre d'outils dans notre paysage actuel.

A titre de comparaison, nous pourrions rapprocher GeoKettle de [FME](http://www.safe.com/). Mais, jusqu'à récemment, GeoKettle ne disposait qu'une d'une faible gamme de formats (en entrée et en sortie) disponibles. Ce qui est plutôt embêtant pour un logiciel souhaitant être affilié à un ETL...

C'est pourquoi, c'est avec plaisir que j'ai appris (via [tweeter](http://twitter.com/tbadard/status/16089334135)) l'intégration d'[Ogr2Ogr](http://www.gdal.org/ogr/). D'abord disponible uniquement en lecture, le Docteur Badard a semble-t-il réussi à utiliser cette librairie en lecture et en écriture au sein de GeoKettle. Je dis semble-t-il car cette nouvelle version ne devrait être disponible que dans les jours prochains. Je n'ai donc pas pu encore tester cette nouvelle fonctionnalité et il ne me reste qu'à prendre mon mal en patience.

## Spatial Data Integrator

La présentation des ETLs n'est pas finie car c'est maintenant avec celui initié par CampToCamp que je reviens. Celui-ci, nommé [Spatial Data Integrator](http://www.spatialdataintegrator.com/) (SDI), ajoute à [Talend Open Studio](http://fr.talend.com/index.php) la possibilité d'utiliser des données spatiales. Petite anecdote, Talend est une société française, en ces temps où notre "équipe nationale" fait grise mine est au fond du trou c'est le moment de lancer un petit cocorico. Petit clin d'œil à [nodeatweet](http://twitter.com/nodatweet/status/16459248822) qui a su trouver les mots justes : "Et si on misait sur l'innovation, plutôt que sur le football pour la fierté nationale ?".

J'ai eu l'opportunité de suivre pendant deux jours une formation sur SDI dans les locaux de CampToCamp à Chambéry. Moi qui avais, jusqu'alors, manipulé essentiellement GeoKettle, je dois avouer que j'ai été très agréablement surpris. Bien évidemment, chacun de ces outils possède sa propre logique mais ils sont tout à fait comparables dans leurs fonctionnalités (il faudra voir si l'intégration d'Ogr2Ogr ne donne pas un léger avantage à GeoKettle, même si certaines "[astuces](http://datagistips.blogspot.com/2009/12/one-simple-example-of-using-ogr.html)" existent).

Néanmoins, jusqu'à récemment, le développement de Spatial Data Integrator se faisait parallèlement à celui de Talend Open Studio. Cela posait notamment des problèmes lors de changements de version. Conscient de cette contrainte l'équipe de CampToCamp a revu l'architecture de SDI afin de l'intégrer directement dans TOS sous la forme de plugins. Cette information, de François-Xavier Prunayre publiée sur [neogeo-online](http://www.neogeo-online.net/blog/archives/304/), permettra, j'en suis certain, à une plus grande majorité d'utilisateurs de se pencher sur cet ETL spatial.

En conclusion, je pense que les mouvements auxquels nous assistons en ce moment dans le domaine du GeoBI ne sont que les prémices d'une incursion à plus large échelle de la géomatique décisionnelle au coeur de nos activités traditionnelles. Bien évidemment, toutes les facettes de ce domaine ne seront pas forcément utilisées, mais certaines d'entre elles feront partie de la boite à outils du géomaticien moderne.

[^1]: [Altic](http://www.altic.org/), [CampToCamp](http://www.camptocamp.com/), [Engineering Group](http://www.eng.it/), [Inova](http://www.inovaos.it/), [Spatialytics](http://www.spatialytics.com/)
[^2]: [Université de Milan](http://sesar.dti.unimi.it/)
[^3]: [Les ETL spatiaux OpenSource, à pieds joints dans l'informatique GéoDécisionnelle](http://www.geotribu.net/node/222)
[^4]: [La géomatique décisionnelle, l'avenir du SIG?](http://www.geotribu.net/node/131)
[^5]: [Le grand BI](http://www.legrandbi.com/2010/02/gartner-marche-bi-open-source/) et [OSBI](http://www.osbi.fr/?p=777)

----

<!-- geotribu:authors-block -->
