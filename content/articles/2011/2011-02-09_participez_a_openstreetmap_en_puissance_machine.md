---
title: "Participez à OpenStreetMap en offrant un peu de puissance machine"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2011-02-09
description: "Participez à OpenStreetMap en offrant un peu de puissance machine"
tags:
    - open source
    - OpenStreetMap
    - Tiles@Home
---

# Participez à OpenStreetMap en offrant un peu de puissance machine

:calendar: Date de publication initiale : 09 février 2011

![logo OpenStreetMap](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/Openstreetmap.png "logo OpenStreetMap"){: .img-thumbnail-left }

Participer au projet OpenStreetMap peut revêtir différentes formes. Si pour la plus grande majorité des contributeurs, cela consiste à uploader des fichiers GPX ou à digitaliser les données, sachez qu'il existe d'autres moyens de s'investir.  
L'un d'entre eux consiste à offrir un peu des ressources de votre ordinateur. En effet, la production des cartes requiert d'importants besoins en terme de calcul. Il s'agit alors de distribuer ces opérations sur des ordinateurs hôtes. L'idée n'est pas nouvelle, le projet [SETI@home](http://setiathome.ssl.berkeley.edu/) se proposait déjà de faire de même afin de rechercher l'existence d'une vie extraterrestre. Mais revenons à nos moutons et voyons comment adopter cela à notre problématique cartographique.

## Fonctionnement de Tiles@home

Le fonctionnement du programme Tiles@home se compose d'une partie serveur et d'une partie client. La partie serveur est en charge de récupérer les demandes de mise à jour de carte. La partie client, qui s'exécute sur les ordinateurs des contributeurs interroge le serveur et génère les nouvelles cartes pour ensuite les renvoyer.

## Installation de Tiles@home

Il existe deux manières de faire fonctionner le client Tiles@home. La plus simple consiste à télécharger [l'image disque](https://wiki.openstreetmap.org/wiki/Virtual_Tiles@Home_-_Ubuntu#Download) spécialement créée. Basée sur une distribution Ubuntu 10.04 LTS, il vous suffit simplement de lancer l'image avec par exemple [virtualBox](http://www.virtualbox.org/). Vous aurez alors un environnement complet prêt à fonctionner.

La seconde manière, un poil plus complexe, consiste à installer les librairies nécessaires. Heureusement, le [wiki d'OSM](https://wiki.openstreetmap.org/wiki/Tiles@home/Install_Guide) est bien fait. Les démarches pour chacune des distributions sont expliquées. J'ai donc suivi à la lettre les instructions pour [Ubuntu](https://wiki.openstreetmap.org/wiki/Tiles@home/Install_Guide#Ubuntu).

Il nous reste maintenant à [télécharger](https://wiki.openstreetmap.org/wiki/Tiles@home/Install_Guide#Download_the_program) le programme client. Cela se fait en utilisant le protocole svn :

`svn co <http://svn.openstreetmap.org/applications/rendering/tilesAtHome-dev/tags/Vizag> tilesAtHome`

Dernière ligne droite avant de lancer le programme, la [configuration](https://wiki.openstreetmap.org/wiki/Tiles@home/Install_Guide#Linux_.2F_Mac_OS_X_.2F_.2ABSD). Une fois les différents fichiers correctement paramétrés, nous pouvons maintenant générer nos tuiles.

## Utilisation de Tiles@home

L'utilisation de Tiles@home peut se faire en utilisant différentes options. Par exemple si vous souhaitez générer une seule tuile la commande est la suivante :

`perl tilesGen.pl once`

Ensuite pour uploader les images sur le serveur :

`perl tilesGen.pl upload`

Bien évidemment, vous n'allez pas répéter cette opération à chaque fois. C'est pourquoi, l'option que vous utiliserez le plus souvent est :

`perl tilesGen.pl loop`

Cela a pour effet d'effectuer les opérations que nous avons vues précédemment jusqu'à la suspension du programme par l'utilisateur.

![Tiles at home](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2011/tiles_at_home.png "Tiles at home"){: .img-center loading=lazy }

D'ailleurs, si vous souhaitez arrêter le processus Tiles@home alors qu'il est en train de générer les tuiles, vous devez créer un fichier `stopfile.txt` dans le dossier de Tiles@home. Sinon, vous pouvez également lancer la commande :

`./tilesGen.pl stop`

Cela aura pour effet d'arrêter la création des images et d'envoyer celles qui ont déjà été créées.

## Conclusion

Comme nous l'avons souligné en introduction, participer à OpenStreetMap peut prendre différentes formes. Celle que nous vous avons présentée ici offre l'avantage de tourner en tache de fond. Vous n'avez rien à faire à part offrir un peu de la puissance de votre ordinateur. Sachez que vous pouvez suivre l'évolution et les statistiques de votre participation sur le site de [Tiles@Home](http://tah.openstreetmap.org/User/show/) ou sur [tahstats](http://tahstats.appspot.com/).

La génération des images utilise le moteur de style [Osmarender](https://wiki.openstreetmap.org/wiki/FR:Osmarender). L'avantage de ce dernier, par rapport à Mapnik, est la mise à jour régulière du fond de carte (à peine quelques heures) rendu possible par la large distribution de Tiles@home. D'ailleurs sachez que, si vous le souhaitez, vous pouvez forcer cette mise à jour. Pour cela rien de plus, il vous suffit de vous rendre sur [l'interface cartographique](http://tah.openstreetmap.org/Browse/slippy/) dédiée.

----

<!-- geotribu:authors-block -->
