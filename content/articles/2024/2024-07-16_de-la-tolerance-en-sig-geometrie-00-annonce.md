---
title: De la tolérance en SIG
subtitle: La vraie tolérance consiste à voir large sans perdre la mesure (c) Barratin
authors:
    - Loïc Bartoletti
categories:
    - article
comments: true
date: 2024-07-16
description: "Un tour d'horizon des SIG sur la précision des calculs géométriques."
icon: material/vector-intersection
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_annonce.png
license: beerware
robots: index, follow
tags:
    - analyse
    - ArcGIS
    - FME
    - géométrie
    - GEOS
    - GRASS
    - PostGIS
    - QGIS
    - SAGA
    - SFCGAL
    - topologie
---

# De la tolérance en SIG

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

Régulièrement, j'ai des questions sur certaines « irrégularités » rencontrées lors d'opérations courantes :

- Pourquoi l'accrochage dans QGIS ne se positionne-t-il pas toujours exactement sur la géométrie ?
- Pourquoi les calculs lors des opérations de superposition semblent manquer de précision ?
- Et pourquoi un calcul et son inverse ne produisent-ils pas toujours des résultats cohérents ?

Ces questions reflètent des préoccupations courantes parmi les utilisateurs de SIG, qui s'attendent à une exactitude et à une précision rigoureuses. La maxime "rigueur, rigueur, rigueur", si chère à l'un de mes anciens chefs, n'est pas toujours… de rigueur sur nos ordinateurs.

Alors que je préparais un article sur la topologie que je dois à [Julien](https://geotribu.fr/team/julien-moura/) depuis plusieurs mois, j'ai été frappé par ce que l'on appelle le [phénomène Baader-Meinhof, ou l'illusion de fréquence](https://fr.wikipedia.org/wiki/Illusion_de_fr%C3%A9quence) : soudainement, ce sujet paraît surgir partout, des cours aux discussions en ligne. Entre les _issues_ signalées et les conversations avec mes collègues, j'ai décidé de changer mon fusil d'épaule. Plutôt que de continuer sur le chemin prévu, j'ai opté pour réaliser plusieurs séries d'articles, explorant certains traitements, « problèmes », différences dans les SIG. Cet article, subdivisé en chapitres, fera partie d'une série qui vise donc à montrer le dessous des SIG.

Dans les chapitres suivants, nous explorerons ensemble :

- [Le constat : les calculs ne sont pas bons](./2024-07-18_de-la-tolerance-en-sig-geometrie-01-calculs-intersects-qgis-pas-bons.md).
- [Fonctionnement interne de QGIS et GEOS : comment ces outils gèrent-ils les données et les opérations géométriques](./2024-07-25_de-la-tolerance-en-sig-geometrie-02-qgis-et-geos.md).
- [Et les autres SIG Open Source ? Comparaisons avec GRASS et SAGA](./2024-08-01_de-la-tolerance-en-sig-geometrie-03-grass-saga.md).
- [Et dans les bases de données ? Comparaisons de SQL Server, Oracle et PostGIS](./2024-08-08_de-la-tolerance-en-sig-geometrie-04-postgis-oracle-ms-sql-server.md).
- [Utilisation de la topologie : est-ce que la topologie peut nous sauver ?](./2024-08-15_de-la-tolerance-en-sig-geometrie-05-topologie-forces-et-limites.md)
- [Approche alternative : utilisation de SFCGAL pour des calculs plus robustes.](./2024-08-22_de-la-tolerance-en-sig-geometrie-06-sfcgal.md)
- [Et chez les proprios, ça se passe comment ?](./2024-08-29_de-la-tolerance-en-sig-geometrie-07-esri-fme.md)
- [Algorithmes et code : comment cela fonctionne-t-il ? Cette partie sera optionnelle, pour ceux ne voulant pas voir de code.](./2024-09-05_de-la-tolerance-en-sig-geometrie-08-algorithmes-code.md)
- [La conclusion : comment arrêter de trop penser et vivre une vie meilleure !](./2024-09-26_de-la-tolerance-en-sig-geometrie-09-conclusions.md "Conclusions")

Êtes-vous prêts pour l'aventure ? Sortons nos SIG !

![Série d'été 2024 de Loïc Bartoletti - Les Géométries et les SIG : annonce - Crédits : Sylvain Beorchia](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_annonce.png){: .img-center loading=lazy }

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
