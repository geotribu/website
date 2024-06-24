---
title: "La géomatique décisionnelle, l'avenir du SIG?"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-07-17
description: "La géomatique décisionnelle, l'avenir du SIG?"
tags:
    - BI
    - ETL
    - GeoBI
    - géodécisionnel
    - open source
---

# La géomatique décisionnelle, l'avenir du SIG?

:calendar: Date de publication initiale : 17 juillet 2009

![SOLAP](https://cdn.geotribu.fr/img/logos-icones/divers/solap.png "SOLAP"){: .img-thumbnail-left }

Empruntés au monde de la **B**usiness **I**ntelligence (BI), les **S**ystèmes d'**A**ide à la **D**écision (SAD) apportent aux décideurs un haut degré d'abstraction facilitant ainsi le processus décisionnel. Néanmoins alors que l'on assiste à une véritable explosion de la spatialisation de l'information (environ 80% des données ont une composante spatiale ) peu de ces systèmes intègrent ce nouvel élément. A contrario les Systèmes d'Informations Géographiques (SIG) basés sur l'utilisation de cette dimension spatiale sont difficilement exploitables en tant qu'outil d'aide à la décision.  

C'est pourquoi la géomatique décisionnelle qui apporte à l'informatique décisionnelle la notion du spatial représente une nouvelle approche particulièrement novatrice. Elle prend en effet, les qualités de chacun des deux éléments (BI+SIG) pour fournir au final une architecture spatiale orientée décision.  

Les premiers travaux initiés par le professeur [Yvan Bédard](http://yvanbedard.scg.ulaval.ca/) de l'Université de Laval ont permis de fixer les caractéristiques techniques, logiques et conceptuelles s'appliquant à la géomatique décisionnelle. Celles-ci ont été résumées sous le terme SOLAP signifiant **S**patial **O**n **L**ine **A**nalytical **P**rocessing. Tout comme les SIG, la géomatique décisionnelle est formée de plusieurs composants allant du formatage des données à la visualisation finale de celles-ci :

![SOLAP](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/spatialOlap.png "SOLAP"){: .img-center loading=lazy }

Si de par sa logique la géomatique décisionnelle se situe à l'opposée des structures SIG actuelles ces deux notions n'en restent pas moins complémentaires. Néanmoins dans un système SOLAP le rôle du géomaticien en tant qu'analyste n'a plus sa place. En effet dans un processus classique le processus décisionnel se trouve divisé, au minimum, en deux niveaux. D'un côté l'analyste SIG, de l'autre les décideurs. Cette dispersion des informations et des décisions est fortement préjudiciable à la chaîne décisionnelle. C'est pourquoi dans une architecture SOLAP l'accent est mis sur une démocratisation verticale (vers les décideurs) de l'information géographique.  

Globalement les différences entre nos systèmes SIG actuels et les systèmes SOLAP se situent au niveau de leur conception et des objectifs finaux. Le tableau ci-dessous compare succinctement les caractéristiques de chacune :

| SIG  | SOLAP |
| :---------------: |:---------------:|
|Base de données de type transactionnelle : orientée MAJ/transaction |Base de données de type OLTP : orienté analyse |
|Optimisation de l'espace de stockage |Optimisation des temps de réponse (précalcul et agrégation des données)|
|Interface de requête et d'analyse complexe |Interaction complète de l'utilisateur avec les données.|

 De cette nouvelle approche est née [Jmap](http://www.kheops-tech.com/en/home/index.jsp) 1er logiciel commercial intégrant le concept SOLAP. Néanmoins au niveau openSource aucune solution n'était jusqu'alors disponible. Ce vide est dorénavant comblé avec l'arrivée de la nouvelle version de [GeoKettle](http://geosoa.scg.ulaval.ca/en/index.php?module=pagemaster&PAGE_user_op=view_page&PAGE_id=17), de [GeoMondrian](http://www.geo-mondrian.org/) et [Spatialytics](http://www.spatialytics.org/), tous développés par l'équipe du professeur Thierry Badard également de l'université de Laval. Sa présentation est résumée dans les deux paragraphes ci-dessous :  

GeoKettle ajoute une dimension spatiale à l'ETL (Extract Transform Load) de Pentaho Data Integration (Kettle). Les nouveautés apportées par la version 3.1.0-20081103 sont notamment :

* le portage des extensions de GeoKettle vers le nouveau Pentaho Data Integration (PDI)
* le support des projections avec également la capacité d'effectuer des reprojections à la volée
* l'utilisation des nouvelles versions de [GeoTools](http://geotools.codehaus.org/) (v 2.5.5) et [JTS](http://www.vividsolutions.com/jts/jtshome.htm) (v 1.10).

GeoMondrian est une version spatialisée du serveur OLAP Mondrian (également nommé Pentaho Analysis Services). GeoMondrian ajoute à Mondrian un type de données Geometry, permettant le stockage des propriétés de membres et des mesures contenant des géométries vectorielles (points, lignes, polygones) nativement dans le cube de données. Des extensions au langage d'interrogation MDX supportant ce type de données sont aussi fournies. Elles permettent d'ajouter des capacités d'analyse spatiale au coeur même des requêtes analytiques.  
Pour faire simple, GeoMondrian apporte au serveur OLAP Mondrian, ce que PostGIS apporte au SGBD PostgreSQL un support cohérent et puissant de la composante spatiale.  

Spatialytics est un composant cartographique léger et open source qui permet la navigation dans les cubes de données Spatial OLAP (SOLAP). Il vise à être intégré dans différents frameworks de tableau de bord afin de produire de véritables tableaux de bord géo-analytiques interactifs. Ils permettront de supporter le processus de décision en incluant la dimension spatiale au cœur de l'analyse des données d'entreprise.  
Spatialytics est basé sur le client cartographique OpenLayers et utilise olap4j pour réaliser la connexion à des sources de données OLAP.  
Spatialytics permet ainsi :

* la connexion à un serveur SOLAP tel que GeoMondrian
* la navigation dans les cubes de données géospatiales
* la représentation cartographique de mesures et de membres d'une dimension spatiale sous la forme, pour l'heure, de cartes choroplèthes (intervalles fixes ou intervalles égaux dynamiques)

Ces nouvelles applications OpenSource sont une véritable opportunité pour le monde de la géomatique spatiale car elle représente aujourd'hui les seules alternatives libres à la mise en place d'une solution SOLAP.

----

Retrouvez également cet [article](http://www.portailsig.org/index.php?id=1176) (et bien plus) sur le [portail SIG](http://www.portailsig.org/).

## Source

* Bédard, Y., Proulx, M.J., Rivest S., (2005) Enrichissement du OLAP pour l'analyse géographique: exemples de réalisations et différentes possibilités technologiques
* Bédard, Y., Merrett, T., Han, J. (2001) Fundamentals of spatial data warehousing for geographic knowledge discovery. In H. Miller & J. Han (Eds.), Geographic Data Mining and Knowledge Discovery. London: Taylor & Francis
* Lambert, M. (2006) Développement d’une approche pour l'analyse SOLAP en temps réel: adaptation aux besoins des activités sportives en plein air
* Laurent, A. et all (2002) Entrepôt de données et OLAP : un aperçu orienté recherche – Groupe de travail GaFOLAP – Action spécifique GaFoDonnées
* McHugh, R., Roche, S., Bédard , Y. (2007) Vers une solution SOLAP comme outil participatif
* Pornon, H., (2007) Revue Geomatique expert – Bilan et perspectives de 20 années de Géomatique. Vers des SIG plus collaboratifs, La Géo-collaboration.
* Rageul, N,. (2007) Vers une optimisation du processus d'analyse en ligne de données 3D : Cas des fouilles archéologiques

----

<!-- geotribu:authors-block -->
