---
title: "OpenStreetMap, la Réunion tout en couleur avec Corine Land Cover"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2012-03-15
description: "OpenStreetMap, la Réunion tout en couleur avec Corine Land Cover"
tags:
    - Corine Land Cover
    - La Réunion
    - OpenStreetMap
---

# OpenStreetMap, la Réunion tout en couleur avec Corine Land Cover

:calendar: Date de publication initiale : 15 mars 2012

![Logo Openstreetmap](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/Openstreetmap.png "Openstreetmap"){: .img-thumbnail-left }

Cela fait maintenant un peu plus de trois ans que mon activité de contributeur d'OpenStreetMap se concentre sur une zone particulière de l'Océan Indien : l'Ile de la Réunion. Originaire de ce petit coin de paradis, j'avais à coeur de faire avancer ce projet de cartographie libre. Étant sur place au départ, je pouvais compter sur mon fidèle GPS. Mais en raison de mon expatriation professionnelle, il m'a fallu composer avec d'autres ressources. Heureusement, la possibilité d'accéder au cadastre me permet de continuer à enregistrer de nouvelles routes. Si le réseau commence à prendre forme, cela n'était pas le cas pour ce qui concerne l'occupation du territoire. La carte apparaissait donc un peu vide et cela ne représentait pas, à mon sens, la luxuriante végétation et les paysages changeants de l'île. De ce fait, comme cela avait [déjà été fait pour la métropole](https://wiki.openstreetmap.org/wiki/FR:Corine_Land_Cover), je me suis attelé à importer les données [Corine Land Cover](https://fr.wikipedia.org/wiki/Corine_Land_Cover) (CLC). Je vous livre ici la méthode ainsi que les outils utilisés.

## Source des données

Première étape, trouver les données ! Un petit tour sur le site du [club géomatique de la réunion](http://clubgeomatique.agorah.com) m'a permit de [trouver mon bonheur](http://clubgeomatique.agorah.com/clubgeomatique/index.php/les-projets-reunionnais-lies-aux-sig-et-a-la-geomatique/401-corine-land-cover-reunion-2000-a-2006.html). Néanmoins, celles-ci étant au format MapInfo, je ne pouvais les exploiter immédiatement. De plus, il me fallait également séparer dans des couches distinctes les thématiques que je désirais intégrer dans la base OpenStreetMap. Avec l'aide [QGIS](https://www.qgis.org/), cette étape ne fut au final qu'une formalité. Je disposais alors d'autant de couches (au format shapefile) que de thématiques comme cela est spécifié dans le [Wiki CLC d'OSM](https://wiki.openstreetmap.org/wiki/WikiProject_France/Corine_Land_Cover/Nomenclature).

## Du shapefile à OSM

Maintenant que tout est en place, il me fallait un moyen de transformer mes fichiers , au format shapefile, en un format exploitable par [JOSM](http://josm.openstreetmap.de/), l'éditeur OpenStreetMap que j'utilise. Après avoir testé quelques une [des solutions listées](https://wiki.openstreetmap.org/wiki/Import/Shapefile#Conversion_to_osm_format) sur le wiki, je me suis tourné vers [OGR2OSM](https://wiki.openstreetmap.org/wiki/Ogr2osm) qui m’apparaissait comme étant la plus souple et la plus simple à utiliser. Cet utilitaire en ligne de commande vous permet de transformer votre fichier shapefile en un fichier OSM au moyen de l'instruction suivante :

`python ogr2osm/ogr2osm.py my-shapefile.shp`

Jusque-là rien d'exceptionnel me direz-vous. Mais ce qui m'a complètement convaincu c'est la possibilité de spécifier un fichier python au sein duquel sera spécifié les modifications ou ajouts à apporter en fonction d'un attribut donné. Ce fichier prend en entrée la valeur du champ et retourne en sortie un dictionnaire dans lequel vous avez spécifié vos nouveaux attributs. Cette étape vous permet ainsi de convertir automatiquement les valeurs de votre shapefile en tag OpenStreetMap valides. Prenons par exemple. Le fichier de translation sera alors le suivant :

```python
def translateAttributes(attrs):  
  if not attrs: return

  tags = {}

  # On ajoute automatiquement la source  
  tags.update({'source':'Union européenne - SOeS, CORINE Land Cover, 2006.'})  
  tags.update({'CLC:code': attrs['CODE_06'] })  
  tags.update({'CLC:id': attrs['ID'] })  
  tags.update({'CLC:year': '2006' })

  # On ajoute des tags en fonction de la valeur du champ  
  if attrs['libelle_fr'] == 'Prairies' :  
    tags.update({'landuse': 'meadow' })

    return tags  
```

Et voilà, je me retrouve donc avec autant de fichier OSM que j'ai de thématiques Corine Land Cover. La dernière étape est l'import des données dans la base. Rien de plus avec JOSM. Visualisons maintenant le résultat obtenu.

### L'avant-après CLC

Quand je vous disais qu'elle était un peu triste notre carte OSM de la réunion. Ne préférez-vous pas ce joli camaïeu de vert ?

![Avant-après CLC](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2012/avant_apres.png "Avant-après CLC"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->
