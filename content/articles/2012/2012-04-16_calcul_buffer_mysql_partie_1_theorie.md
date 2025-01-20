---
title: "Calcul de buffer sous MySQL - 1ère partie : la théorie"
subtitle: MyTamponQL 1
authors:
    - Fabien Goblet
categories:
    - article
comments: true
date: 2012-04-16
description: "Calculer un buffer avec un SGBD sans extension spatiale (MySQL 5). 1ère partie : la théorie"
icon: simple/mysql
legacy:
    - node: 504
tags:
    - buffer
    - latitude
    - longitude
    - MySQL
    - rayon
    - Terre
---

# Calcul de buffer sous MySQL - 1ère partie : la théorie

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![logo MySQL](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/mysql.png){: .img-thumbnail-left }

J'ai été confronté à un problème simple il y a quelques temps : "extraire de ma base de données les enregistrements qui sont à une distance inférieure à un rayon donné". Là normalement pour toute base de données géographique bien constituée - genre PostGIS :wink: - pas de problème, hop un petit coup de `ST_Buffer` et on a le résultat.

Seulement si on avait tout le temps une extension spatiale sur le SGBD utilisé, ce serait facile. Si on prend les solutions proposées par OVH et Online sur les serveurs mutualisés, pas de trace de PostGIS - mon dernier contact avec les techniciens d'OVH pour savoir quand serait implémentée cette extension a retourné une réponse assez évasive du style "euh on teste, pas pour le moment ...". Hum je ne peux pas attendre.  
C'est sûr il existe des solutions vraiment pas mal chez Alwaysdata... même pas besoin de leur demander pour installer une extension géographique sur une base, mais parfois on n'a pas trop le choix. Donc ce sera du MySQL 5.x et faudra faire avec.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## MySQL Geospatial

Il existe des fonctions spatiales sous MySQL, mais pas toutes ... et malheureusement il n'y a pas de calcul de buffer ni même de calcul d'inclusion, ce n'est pas encore implémenté.
Avec un langage de script

Mes scripts qui pilotent les requêtes vers la base de données sont en PHP - on pourrait se dire, tiens je vais faire mes calculs avec ce langage, on fait une petite recherche sur notre blog préféré et on tombe sur une bibliothèque qui semble faire l'affaire. On extrait tous les points de la base et on calcule les distances avec le centre de notre recherche sur ces derniers. Mouais, pas optimal tout ça ... "la recherche sur tous les points" si il y en a beaucoup ça risque de mettre à genoux le SGBD, il va falloir affiner la requête SQL. De plus c'est toujours mieux de faire l'extraction directement depuis la base de données et non à un plus haut niveau avec le langage de script.

## Reposons le problème

### Qu'est-ce qu'on a

- des points : de type geometry ;
- un buffer qui correspond au rayon de recherche ;
- des coordonnées (latitude et longitude) du centre de recherche.

### Si la Terre était plate

En 2D, ce serait assez simple - hop une distance euclidienne :

```sql
SELECT * FROM poi WHERE SQRT(POW(latsearch - x(geom),2) + POW(lngsearch - y(geom)),2)
```

Et le tour (de la Terre) est joué !

Mais maintenant que l'on sait que la Terre n'est pas plate, la formule ne fonctionne pas. On va donc poser comme prédicat que la Terre est ronde. Ok, ce n'est pas vraiment une boule parfaite, elle est un peu aplatie aux pôles, mais on va faire comme si. D'ailleurs vue de loin ça ressemble pas mal à un ballon - un joli ballon même :

![la Terre](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2012/Terre_planete_bleue.webp){: .img-center loading=lazy }

## Faisons maintenant un peu de math

Si l'on fait une recherche sur Internet pour calculer la distance entre deux points sur une sphère on tombe sur pas mal d'informations.
La ressource la plus complète que j'ai lue est celle de Movable Type Ltd. Nous y apprenons que l'on peut utiliser la formule Haversine. Et en cherchant encore un peu, on tombe sur la traduction dans MySQL. Ca y est on a tout. On va pouvoir extraire les points de la base de données depuis un rayon de recherche et un centre.

## En SQL

Si l'on considère que l'on a une table poi qui contient nos points dont la géométrie est stockée dans le champ 'geom', nous pouvons en extraire les points qui sont à une distance inférieure au rayon de recherche depuis le centre donné.

```sql
SET @centersearch_lat = 48.85469 ;
SET @centersearch_lng = 2.3473 ;
SET @buffer = 250;
SELECT *,
6371 * 2 * asin(sqrt(power(sin((@centersearch_lat - abs(x(geom))) * pi() / 180 / 2), 2)
+ cos(@centersearch_lng * pi() / 180) * cos(abs(x(geom)) * pi() / 180)
* power(sin((@centersearch_lng - y(geom)) * pi() / 180 / 2), 2) )) AS distance
FROM poi
HAVING distance @buffer
ORDER BY distance
```

6371 ? C'est le rayon moyen volumétrique de la Terre en kilomètres.

### Résultat

C'est bien, on arrive à extraire les enregistrements qui sont à une distance à vol d'oiseau inférieure au rayon de recherche, mais pour cela on parcourt toute la base de données ... c'est pas franchement efficace et ça se rapproche de la solution avec la bibliothèque PHP. Ce serait peut-être un peu mieux d'extraire les résultats depuis une bounding box ... mais il faut calculer les coordonnées de cette bounding box (qui est le rectangle qui englobe notre cercle de recherche). Évidemment comme la Terre est ronde, il va falloir jouer un peu avec les cosinus.

Tout d'abord : combien fait un degré de latitude sur Terre ?

## On reprend nos cours de géométrie du collège

Le périmètre :

```math
2*pi()*rayon
```

1 degré de latitude :

```math
lat = 2 * pi() * 6371 / 360 ~= 111.195 km
```

Puis la longitude correspondante à la latitude avec 1 degré de longitude :

```math
lng = cos(lat) * 111.195
```

## Requête SQL finale

On calcule donc les coordonnées de la bounding box que l'on intègre dans la requête SQL :

```sql
SET @centersearch_lat = 48.85469 ;
SET @centersearch_lng = 2.3473 ;
SET @buffer = 250;

SELECT *,
6371 * 2 * asin(sqrt(power(sin((@orig_lat - abs(x(geom))) * pi() / 180 / 2), 2)
+ cos(@centersearch_lat * pi() / 180) * cos(abs(x(geom)) * pi() / 180)
* power(sin((@centersearch_lng - y(geom)) * pi() / 180 / 2), 2) )) AS distance
FROM poi
WHERE y(poi.geom) BETWEEN @centersearch_lng - @buffer / ABS(COS(RADIANS(@centersearch_lat)) * 111.195)
AND @centersearch_lng + @buffer / ABS(COS(RADIANS(@centersearch_lat)) * 111.195)
AND x(poi.geom) BETWEEN @centersearch_lat - (@buffer / 111.195) AND @centersearch_lat + (@buffer / 111.195)
HAVING distance @buffer
ORDER BY distance
```

Dans la seconde partie de ce petit billet nous allons développer une démo pour illustrer tout cela.

----

<!-- geotribu:authors-block -->
