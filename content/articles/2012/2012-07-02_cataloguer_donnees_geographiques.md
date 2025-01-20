---
title: "Cataloguer vos données géographiques en .NET"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2012-07-02
description: "Catalogue vos données géographiques avec Isogeo (GeoSIK)"
tags:
    - .NET
    - catalogage
    - données géographiques
    - GeoSIK
    - Isogeo
    - SIG
---

# Cataloguer vos données géographiques en .NET

:calendar: Date de publication initiale : 02 juillet 2012

![logo globe](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "Icône de globe"){: .img-thumbnail-left }

Dans le domaine du GeoWeb peu de solutions existent pour Windows et encore moins proposent une API .Net compatible. Cela peut donc rapidement devenir un véritable casse-tête si l'essentiel de votre architecture est construit autour de la marque aux quatre losanges. Mais, tout n'est pas perdu pour autant ! En effet, si vous souhaitez implémenter un service de cataloguage de données géographique alors le serveur Open Source [GeoSIK](http://geosik.codeplex.com/) pourrait très certainement vous intéresser. Développé par [Isogeo](http://www.isogeo.fr/), celui-ci est l'une des pièces majeures d'une solution plus globale de recensement, de documentation et de valorisation de l'information géographique.

## Isogeo

[Fondée](http://www.isogeo.com/histoire-geographie) par Mathieu Becker et animée par une équipe pluridisciplinaire, Isogeo développe son savoir-faire dans le domaine de la valorisation de l'information géographique. L'objectif affiché est de changer notre vision du cataloguage qui est un peu la bête noire de beaucoup de géomaticiens. On a beau dire que c'est essentiel et faire la leçon à nos collègues, je dois avouer que quand il s'agit de m'y mettre et de remplir ma fiche...

C'est pourquoi l'orientation choisit par Isogeo est de proposer une solution Web permettant la création automatisée d'inventaire à partir de toutes les données disponibles (fichiers, base de données, services web). Cet inventaire peut être ensuite personnalisé en fonction du profil des utilisateurs afin d'offrir une vision orientée usage. A cela s'ajoute également un moteur de recherche et de filtres ainsi qu'un tableau de bord afin d'aider l'administrateur SIG d'obtenir une vision globale. Enfin, et cela devrait ravir les programmeurs en herbe, une API est également disponible vous permettant par exemple de réaliser en quelques heures un site internet en interaction avec votre catalogue.

[![Isogeo schéma solution](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/isogeo/isogeo_schema_platform_modAPI.png "Isogeo schéma solution"){: .img-center loading=lazy }](http://www.isogeo.fr/solution)

## GeoSIK

Bon maintenant que l'architecture générale a été présentée quand est-il côté programmation. C'est le moment de mettre un peu les mains dans le cambouis ! C'est là qu'intervient GeoSIK, le serveur CSW OpenSource développé en .Net. Pour la petite anecdote, GeoSIK est la contraction de "*Geospatial Services Implementation Kit*", et une référence à l'adjectif geodesic (géodésique en Français) avec lequel il partage sa prononciation. Son objectif est bien évidemment de permettre l'intégration du standard de cataloguage [CSW](http://www.opengeospatial.org/standards/cat) défini par l'OGC.

![GeoSIK logic](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/isogeo/isogeo_geosik_architecture_linq.png "GeoSIK logic"){: .img-center loading=lazy }

Côté architecture GeoSIK permet l'implémentation d'un serveur CSW indépendamment de la technologie (à part .NET, évidemment). Ainsi, le service peut être implémenté en WCF, en ASP .NET MVC . Le travail du développeur consiste alors à créer le "squelette" du service et de le connecter à GeoSIK. Ce qui en terme de code représenterait moins d'une centaine de lignes. Concernant maintenant le stockage des données, cela peut se faire nativement avec toute technologie qui possédant un fournisseur LINQ (SQL Server, Oracle, PostgreSQL, MySQL, SQLite...). Mais si vous disposez d'un format exotique rien ne vous empêche de développer votre propre connecteur. On me souffle dans l'oreillette que cela est faisable avec moins de 500 lignes de code. Fondé sur un modèle Open Source, vos développements pourront ensuite être potentiellement intégrés par l'équipe du projet.

Au niveau des fonctionnalités, GeoSik supporte les langages de requête définis par l'OGC comme : [Filter](http://www.opengeospatial.org/standards/filter) et CQL (défini dans le standard [CSW](http://www.opengeospatial.org/standards/cat)). A cela s'ajoute également la possibilité de "jouer" avec les projections grâce aux connecteurs natifs vers les bibliothèques [projnet](http://projnet.codeplex.com/) et [DotSpatial.Projections](http://dotspatial.codeplex.com/wikipage?title=DotSpatial.Projections&referringTitle=Documentation).

## Conclusion

Sur le papier, la solution proposée par [Isogeo](http://www.isogeo.fr) apparaît comme étant particulièrement pertinente. Les fonctionnalités proposées ainsi que les potentialités offertes sont intéressantes. Néanmoins, mes compétences en programmation windows ne sont pas suffisantes pour vous offrir de véritables tests. Mon avis est donc subjectif et se base principalement sur la plaquette présentée ainsi que sur [la démo en ligne](http://www.isogeo.fr/demo). Mais, peut-être que certains de nos lecteurs auront déjà eu l'occasion de le faire ? Vos commentaires sont évidemment les bienvenues !

----

<!-- geotribu:authors-block -->
