---
title: "Créez une carte papier avec des données OpenStreetMap"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-06-07
description: "Créez une carte papier avec des données OpenStreetMap"
tags:
    - OpenStreetMap
---

# Créez une carte papier avec des données OpenStreetMap

:calendar: Date de publication initiale : 07 juin 2010

Encore un petit billet sur [OpenStreetMap](https://www.openstreetmap.org/). Nous verrons aujourd'hui comment produire une carte papier grâce aux données OSM. En effet, on voit souvent OSM comme un projet exclusivement Web. Et bien non ! On peut aussi fabriquer de jolies cartes vectorielles pour une impression papier.

## Avant-propos

Le but du présent billet est de fabriquer sa carte vectorielle avec des données OSM. La méthode utilisée ne nécessite aucun import en base de données, c'est d'ailleurs pour ça que c'est un peu long (cf. le rendu). Il existe d'autres méthodes pour avoir des cartes vectorielles - notamment le formidable [Maposmatic](http://www.maposmatic.org) qui permet aussi un export en SVG donc manipulable également avec Inkscape ou Illustrator et qui génère également automatiquement un index de rues :-)

## Les outils

Pour produire une carte papier d'une zone géographique avec des données OpenStreeMap, nous avons besoin de quelques outils que nous allons de ce pas installer. La procédure est décrite pour [Ubuntu Lucid Lynx](http://www.ubuntu.com/desktop).

- [Inkscape](http://www.inkscape.org/?lang=fr)
- [Java - OpenJDK](http://openjdk.java.net/)
- [JOSM](http://josm.openstreetmap.de/wiki/Fr%3AWikiStart)

### Inkscape

C'est un logiciel libre de dessin vectoriel. Un peu le Illustrator du libre. Pour l'installer, rien de bien méchant - une ligne de commande et 111 Mo d'espace disque :  

`$ sudo apt-get install inkscape`

Et c'est tout !

### Java

Java est nécessaire pour faire fonctionner JOSM (cf. juste en-dessous) - là encore une ligne et quelques Mo d'espace disque (91 Mo) :  

`$ sudo apt-get install openjdk-6-jre`

### JOSM

JOSM est un éditeur pour OpenStreetMap écrit en Java. Il mériterait un long billet à lui tout seul ! C'est un formidable outil avec de nombreux greffons. Ici pas besoin d'installation, il suffit juste de télécharger l'archive Java du logiciel :

`$ wget <http://josm.openstreetmap.de/josm-tested.jar>`

## Importer les données de la zone dont nous voulons faire une carte

Le premier travail consiste à télécharger les données de la zone désirée, pour cela JOSM est l'outil idéal - 4 clics de bouton de souris et une sélection de zone et c'est fini ! Lançons tout d'abord JOSM - ici en ligne de commande (il est tout à fait possible de faire un lanceur, mais bon faut bien s'entraîner un peu de temps en temps :-) ).  

`$ java -jar /path_to_josm/josm-tested.jar`

![JOSM](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/josm1.png "JOSM"){: .img-center loading=lazy }

### 1er clic

Télécharger des données depuis le serveur OSM :

![JOSM](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/josm2.png "JOSM"){: .img-center loading=lazy }

### 2ème clic

Sélectionner l'emprise dans l'onglet carte glissante et cliquer sur Télécharger. J'ai choisi ici la ville de [Roye](https://www.openstreetmap.org/?lat=49.6991&lon=2.79143&zoom=15&layers=B000FTF) dans la Somme parce que j'ai mappé cette (ma) ville il y a environ 8 mois avec mon vélo, mon GPS - un [Garmin 60CSx](https://buy.garmin.com/shop/shop.do?cID=145&pID=310) - , un papier, un crayon, et le [plugin Cadastre](https://wiki.openstreetmap.org/wiki/FR:JOSM/Fr:Plugin/Cadastre-fr) (il reste certainement pas mal de coquilles de numérisation ... peut-être les verra-t-on à la fin de la transformation en SVG). Le but étant de tester JOSM et d'avoir une carte libre vectorielle de la ville alternative à la [carte](http://www.roye80.fr/pageLibre000106d4.html) officielle.

![JOSM](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/josm3.png "JOSM"){: .img-center loading=lazy }

### 3ème clic

Sauvegarder les données :

![JOSM](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/josm4.png "JOSM"){: .img-center loading=lazy }

### 4ème clic

Enregistrer le fichier sélectionné - il faut absolument définir **data.osm** comme nom de fichier :

![JOSM](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/josm5.png "JOSM"){: .img-center loading=lazy }

## Transformation en SVG avec Osmarender

Et voilà, nous avons un fichier contenant les données. Par contre, il faut faire attention à ne pas demander une zone trop grande - le serveur rejettera la requête. Pour ma petite ville, le fichier data.osm fait 6.4 Mo - dû principalement je pense à la numérisation (longue ...) des bâtiments. L'étape suivante est donc l'édition de ce fichier en [SVG](https://fr.wikipedia.org/wiki/Scalable_Vector_Graphics). Le fichier data.osm et le SVG étant du XML, une transformation [XSLT](https://fr.wikipedia.org/wiki/Extensible_Stylesheet_Language_Transformations) devrait faire l'affaire. Ici nous utiliserons la [grammaire XSL](https://fr.wikipedia.org/wiki/Extensible_stylesheet_language) [Osmarender](https://wiki.openstreetmap.org/wiki/FR:Osmarender) ainsi que les règles pour un zoom 17. Dans un terminal, se placer dans le répertoire contenant le fichier data.osm et télécharger la grammaire et les règles :  

```bash
wget <http://svn.openstreetmap.org/applications/rendering/osmarender/stylesheets/osm-map-features-z17.xml>
wget <http://svn.openstreetmap.org/applications/rendering/osmarender/xslt/osmarender.xsl>  
```

Et lancer la commande de conversion :  

`$ xsltproc osm-map-features-z17.xml > roye.svg`

Et partir se coucher ... enfin c'est ce que j'ai fait, ce processus est un peu gourmand :-) surtout avec un fichier `data.osm` assez volumineux. Du coup, je n'ai pas vu le temps que ça a pris, je suppose une grosse heure, il faudrait que je recommence l'opération en journée. Nous voici donc en présence d'un magnifique fichier SVG de 5.4 Mo :

![JOSM](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/josm6.png "JOSM"){: .img-center loading=lazy }

Que nous allons nous empresser d'ouvrir avec Inkscape : `$ inkscape roye.svg`

![Inskape](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/inkscape1.png "Inskape"){: .img-center loading=lazy }

**Sympa !**

## Conclusion

Extraire des données depuis OpenStreetMap pour produire une carte vectorielle n'est pas vraiment compliqué. L'étape la plus longue sera la manipulation dans Inkscape ou Illustrator afin de produire un résultat bien sympathique. Mais la base est là. N'oubliez pas de rajouter le copyright [CC-by-SA](http://creativecommons.org/licenses/by-sa/2.0/) et un [logo](https://wiki.openstreetmap.org/wiki/Logo) :-) Il existe des méthodes alternatives à cette dernière pour produire des cartes papiers : cf. [ici](https://wiki.openstreetmap.org/wiki/OSM_on_Paper). Voici le résultat réalisé en quelques secondes par Maposmatic sur à peu près la même zone géographique : <http://www.maposmatic.org/jobs/14503>. Il est certain que c'est beaucoup plus rapide et qu'il n'y aucune manipulation à faire :

[![Maposmatic](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/maposmatic1.png "Maposmatic"){: .img-center loading=lazy }](http://www.maposmatic.org/jobs/14503)

Merci à Patrick Hochstenbach pour avoir publié ce [billet](http://www.use-it.be/europe/docs/OSMmanual/) pour MacOS sur lequel je me suis inspiré.

----

<!-- geotribu:authors-block -->
