---
title: "Les ETL spatiaux OpenSource, à pieds joints dans l'informatique GéoDécisionnelle "
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-03-02
description: "Les ETL spatiaux OpenSource, à pieds joints dans l'informatique GéoDécisionnelle "
tags:
    - BI
    - ETL
    - géodécisionnel
    - logiciel
    - open source
---

# Les ETL spatiaux OpenSource, à pieds joints dans l'informatique GéoDécisionnelle

:calendar: Date de publication initiale : 02 mars 2010

![logo SOLAP](https://cdn.geotribu.fr/img/logos-icones/divers/solap.png "logo SOLAP"){: .img-thumbnail-left }

Les outils d'extraction, de transformations et de chargement de données (Extract, transform and load - ETL) constituent le premier maillon (fig 1) de la chaine décisionnelle également nommée Business intelligence (BI). Longtemps réservés au monde de l'entreprise, ces outils s'ouvrent aujourd'hui à tous les secteurs nécessitant une prise de décision rapide se basant sur l'analyse d'un grand nombre de données. Leur objectif est de capter les flux de données formelles (interne à l'entité) ou informelles (crowdsourcing) afin de les intégrer ensuite au sein du système informatique de l'entité (entreprise, association, administration...).

Au cours de ce billet, nous nous attacherons à présenter succinctement les concepts et l'histoire de la géomatique décisionnelle pour approfondir ensuite notre analyse sur les outils ETL OpenSource existants.

![ETL/SpatialOLAP](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/spatialOlap_etl2.png "ETL/SpatialOLAP"){: .img-center loading=lazy }

> Fig 1 : Les ETL dans la chaine décisionnelle

----

## Une société de l'information

Dans nos sociétés où l'information est devenue omniprésente (Gantz 2008), la capacité à pouvoir maitriser celle-ci est un enjeu majeur pour toute entité amenée à prendre une décision. Cette problématique s'explique du fait que nous assistons à :

- une explosion de l'information disponible
- une complexification croissante des entités
- une concurrence toujours plus forte se basant en majeure partie sur l'accès à l'information

Néanmoins, jusqu'à récemment, une grande partie de ces informations restait sous exploitée du fait de la non-prise en charge de la composante spatiale par les outils décisionnels existants. En effet, il a été démontré que l'utilisation de l'OLAP sans composante cartographique présentait d'importantes limitations pour l'analyse de phénomènes géographiques et spatio-temporels (Caron 1998).

Ces limitations se retrouvent tant au niveau des données que des moyens d'analyse utilisables le décideur. En effet, Franklin (Franklin 1992) estime à près de 80% les données stockées possédant une référence géographique. Enfin, il a été démontré que la carte plus que tout autre média, permet de par ses caractéristiques de stimuler nos capacités cognitives (Bertin & Bonin 1992; Standing 1973; Tufte 1992; T. Buzan & B. Buzan 2003).

## Le SOLAP comme nouvelle alternative

Conscient de ce nouvel enjeu, le docteur Yvan Bédard commence dés les années 2000 à réfléchir au concept de Spatial On Line Analytical Processing (SOLAP) (Bedard et al. 1997). Cinq après, fruit de ses travaux et en collaboration avec l'entreprise [k2 GeoSpatial](http://www.k2geospatial.com/geomatique-geospatial/information-geographique) (anciennement KHEOPS technologies), une première suite géodécisionnelle, nommée JMAP Solap, est disponible. De nombreux projets intégrant ce concept novateur ont été réalisés afin d'une part de valider les notions mises en jeu et avant tout comme preuve de concept. Ainsi, SOLAP a notamment été mis en application dans le domaine routier (Rivest et al 2001), dans le domaine sportif (Veilleux 2006) ou encore dans le domaine des fouilles archéologiques (Fortin et Bédard 2004).

## Du décisionnel au traitement de la donnée

Mais, jusqu'à récemment, il n'existait aucun équivalent à JMAP Solap dans le monde de l'OpenSource. Il était alors difficile pour des petites structures ou tout simplement par simple curiosité de mettre en place un projet SOLAP. Néanmoins, au regard du potentiel de cette technologie, de la [croissance de l'OpenSource](http://www.progilibre.com/7-previsions-pour-l-Open-Source-en-2010_a1025.html) dans ce domaine et de l'émergence de l'Open Source Business Intelligence (OSBI) quelques projets commencent à être disponibles.

Dans ce billet et par souci de synthèse nous nous attarderons sur les outils ETL. Bien que ces derniers ne soient qu'un des éléments d'une suite décisionnelle, il nous a semblé important de privilégier cette approche. En effet, ils sont à la base de la structure et servent à construire tout l'édifice qui abritera ensuite les entrepôts de données. De leur paramétrage dépend la réussite du projet.

Enfin, même si comme nous l'avons souligné tout au long de ce billet, les ETL appartiennent au monde de la BI, ils peuvent également être déconnectés d'une logique décisionnelle et assurer simplement le suivi complet des flux de données d'une structure.

Pas convaincu ? Alors mettons-nous en situation et prenons le rôle d'un administrateur SIG qui doit traiter quotidiennement d'importants volumes de données géographiques. Ces données doivent être dans un premier temps transformées (reprojection, simplification...) pour ensuite être envoyées en base. Classiquement pour cela vous auriez utilisé toute une armée de scripts qui seraient lancés, à intervalle régulier, par un cron. Imaginez maintenant qu'au lieu de cela, vous ayez une interface graphique simple et intuitive à votre disposition. C'est ce que permet un ETL et les avantages sont nombreux :

- gain de temps
- évolution du système plus facile
- opérations réalisables même par un non-informaticien
- ...

**C'est pourquoi bien que cet article s'intéresse particulièrement au monde du géodécisionnel il trouvera également tout son intérêt dans des schémas SIG plus classiques.**

## Les ETL OpenSource

A ma connaissance, il n'existe aujourd'hui que deux ETL spatiaux OpenSource :

- [Spatial Data Integrator (SDI)](http://www.spatialdataintegrator.com/)
- [GeoKettle](http://www.spatialytics.org/projects/geokettle/)

Ces ETL s'appuient sur des produits existants à savoir [Talend Open Studio](http://fr.talend.com/index.php) pour SDI et [Pentaho Data Integration](http://www.pentaho.com/) pour GeoKettle. Tout comme PostGis pour postgreSQL, ils agissent comme une surcouche spatiale permettant ainsi la manipulation de données géographiques.

Je ne vais pas vous faire un cours sur le décisionnel OpenSource mais il faut savoir que la plupart des suites proposées aujourd'hui sont composées de différents modules spécialisés qui ont été intégrés au fur et à mesure afin de fournir une offre globale. Pour une vision plus large du concept du décisionnel OpenSource, je vous conseille la lecture du livre blanc publié par Smile (Smile 2010). Concernant les ETL, l'ouvrage "Les ETL open Source, une réelle alternative aux solutions propriétaires" de chez Atol (Atol 2008) est également un très bon point de départ.

## Spatial Data Integrator

![Filter](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/filter_world_light.png "Filter"){: .img-center loading=lazy }

Basé sur l'ETL Talend Open Studio (TOS), Spatial Data Integrator (SDI) est développé par la société [CampToCamp](http://www.camptocamp.com/). Cet ETL est de type générateur de code. C'est-à-dire que pour chaque action que vous réalisez sur l'interface graphique, un code spécifique est généré. En plus de la centaine de connecteurs natifs disponibles dans TOS, SDI ajoute la possibilité de lire et/ou écrire des données au format WFS (r) et GPX (r/w) ainsi que de réaliser des traitements cartographiques (simplification, changement du sens des lignes...). De plus, il peut également être couplé à la bibliothèque [Sextante](http://forge.osor.eu/plugins/wiki/index.php?id=13&type=g) afin de travailler sur du raster. Enfin, la visualisation des données peut se faire directement depuis [Udig](http://udig.refractions.net/).

Le choix pour CampToCamp de proposer un ETL spatial n'est pas surprenant. En effet, au regard des autres produits (MapFish, OpenERP) il apparait clairement que la stratégie de l'entreprise s'oriente vers une gestion complète du flux de données allant de l'extraction au rendu cartographique. Le marché visé est, je pense, principalement celui des grosses entreprises. Même si, d'un point de vue économique, l'OpenSource reste facile d'accès, la mise en place d'une solution complète incluant un ETL + un ERP nécessite tout de même de très bonnes connaissances et compétences.

## GeoKettle

![Schema](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/schema_complet_hook_light.png "Schema"){: .img-center loading=lazy }

Développé par l'équipe du [Dr Badard](http://geosoa.scg.ulaval.ca/fr/index.php) de l'université de Laval (CRG - Canada), GeoKettle est basé sur l'ETL [Pentaho Data Integration](http://www.pentaho.com/products/data_integration/) (PDI). Contrairement à Talend Open Studio qui est un générateur de code, PDI est un moteur de transformation ETL. Dans cette logique, les données et les traitements sont séparés (meta-data driven) (Atol 2008). Avec SDI, il est possible d'accéder en lecture et/ou écriture à plus d'une trentaine de bases de données et de fichiers plats (CSV, XML...). GeoKettle, permet en plus de lire et écrire des données géographiques de bases PostGis, MySQL et de fichiers ShapeFiles.

Les possibilités sont certes un peu moindre que TOS, mais la road map laisse présager des améliorations proches à savoir :

- Prévisualisation cartographique
- Accès vers plus de sources de données
- ...

## Conclusion

J'ai volontairement essayé de résumer au maximum les caractéristiques des deux outils présentés ci-dessus. En effet, ils feront prochainement l'objet d'une présentation plus complète. Néanmoins, il est d'ores et déjà possible de tirer quelques rapides conclusion.

Tout d'abord, il est difficile aujourd'hui d'imaginer l'utilisation de ces outils dans un environnement en production. Les versions sont stables mais l'accès aux données spatiales reste tout de même limité. En effet, seuls quelques formats sont disponibles. Néanmoins, dans ces domaines où les évolutions sont très rapides, je ne serais pas surpris de voir cette limitation prochainement levée. En tout cas, dans un projet à composante GeoWEB utilisant en majorité des bases de données spatiales ces outils pourront avoir tout leur intérêt.

En conclusion, je dirais que ces applications sont à considérer comme les futures boites à outils du géomaticien moderne. Elles sont encore loin de pouvoir rivaliser avec un programme comme [FME](http://www.safe.com/) mais pourraient à terme fournir une alternative intéressante.

## Références

- Atol 2008, Livre blanc ([+](http://www.atolcd.com/actualites/detail-actualite/actualite/2/comparatif-etl-open-source-1.html%20) )
- Bedard, Y. et al., 1997. Geospatial Data Warehousing : positionnement technologique et stratégique.
- Bertin, J., 1999. Sémiologie graphique: Les diagrammes - Les réseaux - Les cartes, Editions de l'Ecole des Hautes Etudes en Sciences.
- Buzan, T. & Buzan, B., 2003. Mind Map : Dessine-moi l'intelligence 2 éd., Editions d'Organisation.
- Caron, P., 1998. Étude du potentiel de OLAP pour supporter l'analyse spatio-temporelle, Dép. Sciences géomatiques, Centre de recherche en géomatique, Université Laval.
- Fortin, M. et al., 2004. Développement d'un système de découverte des connaissances spatio-temporelles pour les chantiers de fouille archéologiques. Dans Colloque Géomatique 2004 - Un choix stratégique. Montréal.
- Franklin, C., 1992. An introduction to geographic information systems: linking maps to databases. Database, 15(2), 12-21. Gantz, J.F., 2008. The Diverse and Exploding Digital Universe. An Updated Forecast of Worldwide Information Growth Through 2011, IDC ([+](http://www.emc.com/collateral/analyst-reports/diverse-exploding-digital-universe.pdf))
- Rivest, S. et al., 2005. SOLAP technology: Merging business intelligence with geospatial technology for interactive spatio-temporal exploration and analysis of data. ISPRS Journal of Photogrammetry and Remote Sensing, 60(1), 17-33.
- Smile 2010, Livre blanc ([+](http://www.smile.fr/site-smile/livres-blancs/erp-et-decisionnel/decisionnel))
- Standing, L., 1973. Learning 10000 pictures. Quarterly Journal of Experimental Psychology, 25(2), 207.
- Tufte, E.R., 1992. The Visual Display of Quantitative Information, Graphics Press.
- Veilleux, J., Lambert, M. & Bédard, Y., 2004. Utilisation du système de positionnement par satellites (GPS) et des outils d’exploration et d’analyse SOLAP pour l’évaluation et le suivi de sportifs de haut niveau. Dans Colloque Géomatique 2004 - Un choix stratégique. Montréal.

## Ressources

- [Pentaho](http://www.pentaho.com/)
- [Talend](http://fr.talend.com/index.php)
- [Developpez](http://business-intelligence.developpez.com/tutoriels/etl-open-source/?page=sommaire)
- comparatif TOS vs PDI : [manapps](http://www.manapps.tm.fr/pdfETL/ETLBenchmarks_Manapps%20090203.pdf),

----

<!-- geotribu:authors-block -->
