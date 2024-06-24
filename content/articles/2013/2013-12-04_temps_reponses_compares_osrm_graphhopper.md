---
title: Temps de réponses comparés OSRM vs GraphHopper
authors:
    - Rodolphe Quiédeville
categories:
    - article
comments: true
date: 2013-12-04
description: La récente sortie de la version 0.2 de GraphHopper est l'occasion de comparer les performances avec OSRM, le projet de calcul d'itinéraires (routing) open source de référence.
icon: material/routes-clock
tags:
    - benchmark
    - GraphHopper
    - routing
    - OpenStreetMap
    - OSRM
---

# Temps de réponses comparés OSRM vs GraphHopper

:calendar: Date de publication initiale : 04 décembre 2013

La [récente sortie](https://karussell.wordpress.com/2013/11/25/releasing-graphhopper-0-2-further-faster-road-routing/) de la version 0.2 de [GraphHopper](http://graphhopper.com/) est une bonne occasion de tester plus en avant cet outil et de vérifier les assertions de l'équipe quant aux temps de réponses annoncés comme très bons. Si l'on regarde dans l'univers des outils libres de routing utilisant les données du projet OpenStreetMap on pense de suite à [OSRM](https://github.com/DennisOSRM/Project-OSRM/wiki) comme compétiteur natif, ce billet expose les résultats des outils stressés par différents tests de charge. Après avoir expliqué la méthode de test et la création du jeu de données de test nous passerons sur le ban de test ces deux outils et nous en tirerons les conclusions qui s'imposent.

----

Commençons par faire un point sur les versions :

- en ce qui concerne OSRM nous allons utiliser la version extraite du git `v0.3.5-501-g992458a` qui est proche de la dernière version stable à savoir la 0.3.7,
- pour GraphHopper nous utilisons la version 0.2 téléchargée depuis le site du projet.

## Méthodo

En ce qui concerne le jeu de données, celui-ci provient du projet OpenStreetMap en utilisant le fichier france-latest des exports [Geofabrik](https://download.geofabrik.de/europe/france.html). Afin de pouvoir faire des calculs de routage nous avons besoin d'un ensemble de couples de points qui représentent le point de départ et le point d'arrivée. Ces couples sont créés en extrayant du fichier protobuff de la France un lot de points référencés __amenity__. La liste non exhaustive des `amenity` utilisées contient `school`, `bank`, `parking`, `atm`, `library`, `pub`, `fuel`, `bus_station`... Nous avons pris garde de mixer des points se trouvant sur les _way_ et des points en dehors des _ways_, ce qui a une inluence sur les résultats comme on le verra plus loin. L'intérêt de ces points est qu'ils sont diffus sur toute la France et permettront d'extraire des populations de points plus ou moins proches entre eux.

Le test qui va servir à la mesure consiste à faire un appel de l'API en mode _json_ avec la présentation de l'itinéraire, comme cela est fait dans les cas d'utilisation réels. Tous les tests seront réalisés avec [Tsung](http://tsung.erlang-projects.org/) en utilisant une cible sur internet et des machines d'injections également sur internet mais dans un datacenter différent afin de se placer au plus près des conditions réelles d'utilisation.

Un premier test effectue deux appels, une fois vers GraphHopper et une fois vers OSRM dans la même session, la charge est légère (7,5 req/s au max) étant donné que les deux outils tournent en même temps sur la machine, ceci afin de ne pas perturber les mesures par une éventuelle saturation de ressource.

![Durée des transactions](https://cdn.geotribu.fr/img/articles-blog-rdp/transaction1_0.png "Durée des transactions"){: .img-center loading=lazy }

La courbe verte correspond aux temps de réponses d'OSRM, la bleue ceux de GraphHopper. Tout itinéraire confondu GrahHopper répond avec un temps moyen de 87 ms et OSRM 120 ms avec des percentile 95 respectifs de 120 et 210 ms. Ce premier test donne l'avantage à GraphHopper, lors de ce test le nombre de requête par seconde a varié entre 0,1 et 10 sans pour autant faire varier le temps de réponse (le [détail](http://tsung.quiedeville.org/tsung-reports/20131127-0947/report.html) du test est consultable en ligne). En analysant les résultats fournis nous avons noté que les distances annoncées varient dans 99,93% des cas, avec dans 83% des cas une distance supérieure pour GraphHopper ; ceci s'explique par le fait que GraphHopper ajoute la distance du point demandé au premier point de la way utilisée (il fait de même à l'arrivée) ce que ne fait pas OSRM qui ne compte que les distances sur les ways.

Ce premier test nous a également permis de créer cinq nouveaux jeux de données définis ainsi, distance inférieure à 3Km (trajet en ville), distance comprise entre 3 et 50 km (trajet départemental), entre 50 et 200 km (grand trajet départemental), entre 200 et 500 km (trajet régional), et distances de plus de 500 km (trajet national) ; pour rappel les points sont tous en France. Quelques informations sur les données ; le fichier initial contient 226482 routes, après tri on conserve respectivement suivant les jeux de données 4480, 53722, 149130 et 198824 routes ; sachant que celles-ci sont constituées de façon totalement aléatoire lors des tirages de points de départs et d'arrivée il est plus fréquent d'avoir des distances longues que des courtes. Cela nous donne tout de même des volumes suffisants pour avoir des résultats non biaisés.  

## Mesure comparative

Tous les temps sont exprimés en msec. ([détail](http://tsung.quiedeville.org/tsung-reports/20131202-1446/report.html) des résultats)

| Jeu de données | Ghp Mean | OSRM mean | delta % | Ghp 95th | OSRM 95th | delta % |
| :--------------- |:---------------:|:---------------:|:---------------:|:---------------:|:---------------:|:---------------:|
| inf à 3km | 49.5 | 48.01 | -3.10 | 55.12 | 52.13 | -5.74 |
| entre 3 km et 50km | 51.94 | 54.29 | 4.33 | 58.74 | 75.93 | 22.64 |  
| entre 50 km et 200 km | 60.10 | 72.33 | 16.91 | 79.51 | 96.42 | 17.54 |  
| entre 200 km et 500 km | 81.92 | 100 | 18.08 | 93.43 | 150 | 37.71  |
| sup à 500 km | 98.97 | 150 | 34.02 | 120 | 220 | 45.45 |

L'analyse des résultats du tableau ci-dessus montre que si l'on compare les temps de réponses de chacun des outils par jeu de données, on voit que globalement les temps de GraphHopper (Ghp) sont meilleurs que OSRM. Il faut tout de même noter que OSRM reste plus rapide sur les trajets courts (inférieur à 3 km). Enfin pour les deux outils le temps de réponses augmente en fonction de la distance du trajet, ce que montre très nettement le grahique ci dessous.

![Mesure comparative](https://cdn.geotribu.fr/img/articles-blog-rdp/time-distance.png "Mesure comparative"){: .img-center loading=lazy }

A ce stade du comparatif GraphHopper semble être plus performant que OSRM, il reste pour parfaire la comparaison à pousser les deux solutions dans leur dernier retranchement.

## Tests aux limites

Nous allons effectuer un test aux limites en injectant de plus en plus d'utilisateurs, avec un taux d'injection d'un à deux utilisateurs par seconde. Le but étant de mesurer l'évolution du temps de réponses en fonction du nombre requêtes simultanées et de définir un point de rupture du système. Pour ce test on rejouera exactement les même requêtes sur les deux outils dans un environnement isolé.

Premier sur le banc OSRM, le détail du test est publié en ligne ([ici)](http://tsung.quiedeville.org/tsung-reports/20131203-0840/graph.html) je me limiterai ici à comparer le taux de requête max par seconde atteint par chacun. Pour OSRM la limite telle que montrée sur le graphique ci-dessous se situe au alentour de 80 requ/sec, avec un temps maximum atteint sur le percentile 99 de 30 secondes.

![Test OSRM](https://cdn.geotribu.fr/img/articles-blog-rdp/osrm-rqrate.png "Test OSRM"){: .img-center loading=lazy }

Pour la même charge GraphHopper (voir le graphique ci dessous et le [détail](http://tsung.quiedeville.org/tsung-reports/20131203-1018/report.html)) s'en sort un mieux en dépassant les 250 requ/sec, et un percentile 99 de 140 msec pour un temps moyen de 50 msec.

![Test GraphHopper](https://cdn.geotribu.fr/img/articles-blog-rdp/graphhopper-rqrate.png "Test GraphHopper"){: .img-center loading=lazy }

## Conclusion

Dans un contexte d'installation "out of the box" on peut conclure après ces quelques chiffres que GraphHopper s'en sort mieux en terme de temps de réponse et de charge supportée. Seulement on l'a vu sur des distances courtes la différence est minime, sur un projet de routage intra commune le choix ne pourra pas se faire sur ce seul critère. Maintenant l'avenir nous dira si cette différence persistera quand GraphHopper aura atteint le niveau de fonctionnalités de OSRM qui reste bien en avance encore.

----

<!-- geotribu:authors-block -->
