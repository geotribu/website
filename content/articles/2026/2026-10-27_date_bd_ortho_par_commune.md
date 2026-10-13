---
title: "De quand date l'ortho de ma commune ?"
subtitle: La BD ORTHO datée commune par commune, et quatre pièges silencieux
authors:
    - Yvann BARBOT
categories:
    - article
comments: true
date: 2026-10-27
description: "L'IGN date la BD ORTHO par département. En croisant le graphe de mosaïquage avec AdminExpress, on obtient la date du vol pour chacune des 34 877 communes. La méthode, et quatre pièges qui faussent le résultat sans jamais lever d'erreur."
icon: fontawesome/solid/plane
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/date_bd_ortho_par_commune/carte-age-photographie-aerienne-france.webp
license: default
robots: index, follow
tags:
    - GDAL
    - GeoPackage
    - IGN
    - open data
    - QGIS
    - SQL
    - WFS
---

# De quand date l'ortho de ma commune ?

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

> « L'ortho de ma commune, elle date de quand ? »
On croit que la réponse tient dans un tableau. En fait, elle tient dans une couche que presque personne n'ouvre, et dans quatre pièges qui ne lèvent aucune erreur.

## Le tableau de l'IGN ne suffit pas

Quand on veut savoir de quand date la BD ORTHO, le premier réflexe est d'ouvrir le tableau des prises de vue de l'IGN. On cherche son département, on lit l'année, et on passe à autre chose.

Le souci, c'est que ce tableau donne une année par département. Dans la Marne, il annonce 2022, et c'est vrai pour 601 communes. Mais cinq autres ont été photographiées en 2024, et quatre en 2025. Si vous travaillez sur l'une de ces neuf communes, vous avez une image plus récente que ce que dit le tableau, et vous ne le savez pas.

![La Marne d'après le tableau IGN, puis commune par commune](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/date_bd_ortho_par_commune/carte-sans-et-avec-le-jeu-de-donnees.webp){: .img-center loading=lazy }

J'ai donc voulu calculer la date commune par commune. Le calcul en lui-même est rapide. Ce qui m'a pris du temps, c'est de comprendre pourquoi mes premiers résultats étaient faux alors que tout tournait sans la moindre erreur.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Deux couches et un croisement

Tout part de deux couches de l'IGN, servies par le WFS de la Géoplateforme et sous Licence Ouverte 2.0. La première est le graphe de mosaïquage de la BD ORTHO (`graphe_bdortho`) : c'est elle qui dit quel morceau de la mosaïque nationale vient de quel vol, avec la date de passage de l'avion et la résolution. La seconde, c'est AdminExpress, pour les contours des communes.

Le graphe est servi à deux niveaux de généralisation. En filtrant sur `echelle=res`, on garde une seule couche nationale, sans recouvrement, où chaque zone est à sa résolution d'origine (20 ou 50 cm).

Il ne reste qu'à croiser les deux. Pour chaque commune, on mesure la surface couverte par chaque vol, et celui qui en couvre le plus donne la date retenue. Sur le papier, c'est tout. En pratique, il y a eu quatre surprises.

## Un WFS qui répond, mais à vide

Pour alléger le téléchargement, j'ai demandé seulement les champs utiles avec `PROPERTYNAME`. Le service a répondu sans broncher, code 200, avec des entités sans géométrie. Le croisement est sorti vide, sans erreur.

Il faut simplement penser à mettre le champ géométrique dans la liste : `geom` pour le graphe, `geometrie` pour AdminExpress. La requête ressemble alors à ça :

```sh
curl -fsSL --get "https://data.geopf.fr/wfs/ows" \
  --data "SERVICE=WFS" \
  --data "VERSION=2.0.0" \
  --data "REQUEST=GetFeature" \
  --data "TYPENAMES=ORTHOIMAGERY.ORTHOPHOTOS.GRAPHE-MOSAIQUAGE:graphe_bdortho" \
  --data "OUTPUTFORMAT=application/json" \
  --data "SRSNAME=EPSG:4326" \
  --data "PROPERTYNAME=dep,pva,res,echelle,date_vol,geom" \
  --data-urlencode "CQL_FILTER=echelle=res AND geom IS NOT NULL" \
  --data "COUNT=100" \
  --data "STARTINDEX=0" \
  -o graphe_page_0.json
```

## Des vols fantômes dans la table

Le `geom IS NOT NULL` à la fin du filtre vient de la deuxième surprise. Quand une zone est rephotographiée, l'IGN ne supprime pas l'ancienne prise de vue du graphe. Il la laisse dans la table et lui retire juste sa géométrie.

Ces lignes ne couvrent plus rien, mais elles sont nombreuses : 211 sur 838. Si on ne les écarte pas, on compte des vols qui ne sont plus sur la mosaïque. Une fois filtrées, il reste 627 emprises pour toute la France.

## Deux mètres qui en font 220 000

Celle-là, je ne l'ai pas vue venir. Le croisement était lent, alors j'ai simplifié les géométries avec `ogr2ogr -simplify 2`. Deux mètres de tolérance, ça ne pouvait rien changer.

Sauf que la tolérance s'applique dans l'unité de la donnée source, et les données arrivaient en EPSG:4326, donc en degrés. Mes deux mètres étaient en réalité deux degrés, soit environ 220 km. La surface couverte en France est passée de 720 000 à 548 535 km², et le script s'est terminé normalement.

Depuis, je ne simplifie plus rien. C'est plus lent, mais c'est juste. Si vous tenez à simplifier, reprojetez d'abord dans un système en mètres, et comparez la surface totale avant et après : c'est cette comparaison qui m'a alerté.

## Des surfaces à NULL

Pour le calcul, j'ai rangé les deux couches dans un GeoPackage reprojeté en EPSG:6933, une projection qui conserve les surfaces. C'est ce qu'il faut quand la question est « quelle part de la commune est couverte par ce vol ».

J'ai lancé le SQL avec `ogr2ogr -dialect SQLite`, et toutes les surfaces sont sorties à NULL. Avec ce dialecte, GDAL lit le GeoPackage avec son SQLite natif : la géométrie arrive sous forme de blob GeoPackage, que les fonctions SpatiaLite ne savent pas lire. Elles renvoient NULL sans rien dire. La solution est de passer chaque géométrie dans `GeomFromGPB()`.

Le croisement final s'appuie aussi sur les index R-tree du GeoPackage, pour ne pas tester chaque commune contre chaque emprise :

```sql
SELECT
  c.code_insee AS code_insee,
  m.pva AS millesime,
  m.res AS resolution_cm,
  m.date_vol AS date_vol,
  ST_Area(ST_Intersection(GeomFromGPB(c.geom), GeomFromGPB(m.geom))) AS aire_intersection_m2
FROM communes c
JOIN rtree_communes_geom rc ON rc.id = c.fid
JOIN rtree_mosaic_geom rm
  ON rm.minx <= rc.maxx AND rm.maxx >= rc.minx
 AND rm.miny <= rc.maxy AND rm.maxy >= rc.miny
JOIN mosaic m ON m.fid = rm.id
WHERE ST_Intersects(GeomFromGPB(c.geom), GeomFromGPB(m.geom))
```

## Vérifier plutôt que croire

Après ça, je ne fais plus confiance à un script juste parce qu'il se termine sans erreur. Le traitement s'arrête maintenant s'il trouve un code INSEE en double, une commune sans couverture, une résolution inattendue, ou un nombre de communes différent de celui annoncé par le WFS.

Et surtout, il compare son résultat au tableau de l'IGN : pour chaque département, l'année majoritaire calculée doit être celle du tableau. À l'extraction du 3 septembre 2026, les 102 départements comparables concordent. Agrégée, la méthode retombe donc sur les chiffres officiels, avec le détail en dessous.

## Ce que ça montre

![L'âge de la photographie aérienne IGN, commune par commune](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/date_bd_ortho_par_commune/carte-age-photographie-aerienne-france.webp){: .img-center loading=lazy }

Au lieu d'une année par département, on obtient 229 dates de vol différentes. Dans 50 départements sur 102, des communes voisines n'ont pas été photographiées la même année. Et une commune sur trois (10 923 exactement) est couverte par plusieurs vols.

Ce dernier chiffre appelle une précaution : quand une commune est à cheval sur deux vols, la date retenue est celle du vol qui couvre le plus de surface, pas forcément celle du centre-bourg. C'est pour ça que le jeu donne aussi le nombre de vols et la part de chacun.

## Les données

Le résultat est en ligne sur data.gouv.fr, sous Licence Ouverte 2.0 : [Date des prises de vue aériennes IGN (BD ORTHO) par commune](https://www.data.gouv.fr/datasets/date-des-prises-de-vue-aeriennes-ign-bd-ortho-par-commune). Il y a une ligne par commune, en CSV, en JSON et en GeoPackage. Le GeoPackage embarque son style, donc il s'affiche directement coloré par âge de l'image quand on le glisse dans QGIS.

La page décrit aussi les limites. C'est la date du vol, pas celle de la mise en ligne, qui arrive plusieurs mois après. Seule la campagne RVB actuelle est couverte. Et treize communes de Guyane sont couvertes à moins de 99 %.

Si une date ne colle pas avec ce que vous voyez sur le terrain, laissez le code INSEE en commentaire. Il reste peut-être un cinquième piège.

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
