---
title: Comment j'ai quantifié les inégalités de traitement météorologiques entre Brest et Dijon
authors:
    - Victor ALEXANDRE
categories:
    - article
comments: true
date: 2022-01-11
description: 'Comment quantifier le temps passé par une présentatrice météo devant une zone de la carte de France : passer de la remarque d''un canapé à une réponse circonstanciée'
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/meteo_inegalites_traitement_avec_r/distance_moyenne_toutes_journees_toutes_sequences.jpg
license: default
robots: index, follow
tags:
    - météo
    - R
    - télévision
---

# Comment j'ai quantifié les inégalités de traitement météorologiques entre Brest et Dijon

!!! info "Republication"
    Article initialement paru sur ma [page Github personnelle](https://github.com/Valexandre/zones_meteo).

:calendar: Date de publication initiale : 11 janvier 2022

## Introduction (Epic version)

![logo Epic Games](https://cdn.geotribu.fr/img/logos-icones/divers/epic-games.png "logo Epic Games"){: .img-thumbnail-left }

Normand de naissance et de coeur, je n'ai jamais accordé une place très importante aux différents bulletins météo, ne sachant que trop bien ce dont allait être faite la journée. Ayant eu le privilège de connaître des personnes venant d'autres horizons, notamment de la lointaine et exotique Bretagne, j'ai réalisé que, dans d'autres lieux, les informations météorologiques pouvaient apporter autre chose que "Bah demain, y r'pleut". Avec plusieurs expériences de bulletins météo télévisés et une formation de datajournaliste derrière moi, je me suis retrouvé un soir sur un canapé devant un constat et un défi : pourquoi la dame de la météo (ça a toujours été une dame quand j'ai regardé) commente les températures des villes orientales en se plaçant au dessus de la Bretagne, laissant ainsi aux intéressés d'autant moins de temps pour voir et lire les informations par elle obstruées et ne pourrait-on pas mesurer cette inégalité d'accès à l'information ?

Ceci est mon histoire.

## Introduction (Honest version)

Ce projet, complètement con sur le fond, consiste à tenter de mesurer les variations autour de zones sur une vidéo. Je m'y suis penché en me disant que ce serait une occasion de faire de me faire la main sur du machine learning, pis en fait non.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Principes

### Matériau

- **Source vidéo** : Je me suis appuyé sur le bulletin [météo de France 2](https://www.france.tv/france-2/meteo-2/) précédant le journal de 20h, tel qu'il a été posté sur la chaîne Youtube de Anaïs Baydemir (la fameuse dame de la météo).
- **Logiciel** : [ffmpeg](https://www.ffmpeg.org) et [R](https://www.r-project.org), avec les packages `imagemagick`, `tidyverse` et `colorscale`.

### Principe du bulletin météo

![logo météo](https://cdn.geotribu.fr/img/logos-icones/divers/weather_app.png "logo météo"){: .img-thumbnail-left }

Une dame rentre dans le champ de la caméra sur un fond vert, des images ou des cartes défilant dans le fond. On ne va s'intéresser ici qu'aux séquences relatives l'allure du ciel : nuages, pluie, ciel bleu, etc (que j'appelle prévisions ici) pour le matin et pour l'après-midi et aux températures pour le matin et pour l'après-midi. Le niveau de zoom sur la métropole est le même tous les jours; la surface n'est donc pas modifiée d'un jour sur l'autre.

## Principe du projet

### 1. Flux vidéo → listes d'images

Impossible de récupérer les fichiers vidéos des bulletins récents via [france.tv](https://www.france.tv), je me suis donc appuyé sur [la chaîne Youtube de Anaïs Baydemir](https://www.youtube.com/channel/UCCjC5WdWYmqLnuwILaJ2Lew), dont j'ai récupéré les fichiers mp4 par un site en ligne ([yt1s.io](<https://yt1s.io>)), puis renommé avec la date en format DDMMYYYY.
Après avoir essayé différentes techniques, c'est avec `ffmpeg` que j'ai pu sortir un nombre suffisamment important d'images pour chacun des mp4 générés (5 par seconde).

```r
system("ffmpeg -i METEO_ZONE/01012019.mp4 -r 5 -f image2 METEO_ZONE/img_01012019_%05d.png")
```

### 2. Extraction des images avec une carte de France

Le package `imagemagick` permet une lecture de texte dans des images. J'ai donc, dans un premier temps, tenté de délimiter quelles étaient les images relatives aux prévisions ou températures du matin selon ce que le texte présent dans l'image indiquait. Toutefois, certaines images se trouvaient zoomées sur certaines parties de l'hexagone sans que cela ne puisse être détectable.
J'ai donc changé mon fusil d'épaule et suis passé sur une sélection à la main d'une image de référence, une image de début et de fin de la séquence, pour chacune des 4 séquences. Par exemple, dans l'image ci-dessous, la première colonne représente l'image de référence : celle qui est la plus dégagée de la séquence, la seconde représente la première image de la séquence et la dernière colonne représente la dernière image de la séquence.

- La première ligne représente les prévisions du lendemain matin.
- La seconde représente les prévisions du lendemain après-midi.
- La troisième représente les températures du lendemain matin.
- La quatrième et dernière représente les températures du lendemain après-midi.

![Explication des images de références, de début et de fin de séquences](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/meteo_inegalites_traitement_avec_r/montage_images_bases_11012019.jpg "Explication des images de références, de début et de fin de séquences"){: .img-center loading=lazy }

### 3. Découpage de la carte de métropole en zones

Une fois l'image découpée, je conserve uniquement la forme de la métropole. Je scinde ensuite cette forme en une série de zones hexagonales de 10 pix de côté, ce qui fait un peu plus de 660 zones sur notre carte.

### 4. Estimation de la couleur médiane par zone de la carte sans présentatrice (référence)

Pour pouvoir déterminer l'état de chaque zone, j'ai choisi de me fier à sa couleur et au fait qu'elle variait plus ou moins de son niveau de référence. Par exemple : une zone ensoleillée est présentée en jaune dans la carte de référence. Je considère qu'elle est couverte par la présentatrice si sa couleur est modifiée. En termes de codages, je récupère la couleur de chaque pixel de la carte, en rouge, vert et bleu; et considère que la couleur de la zone est la médiane du niveau de rouge, de vert et de bleu sur chacun des pixels de cette zone.
On récupère ainsi un tableur avec une couleur de référence pour chaque hexagone, pour chaque séquence (prévision matin et après-midi, températures matin et après-midi).

### 5. Estimation de la couleur médiane par zone de la carte pour chaque image relative à la séquence

Pour les autres images de chaque séquence, on fait le même travail.

### 6. Estimation de la distance moyenne par zone entre la référence et la séquence

On rapporte la couleur obtenue pour chaque zone de chaque image de la séquence à la couleur de référence de la séquence pour en estimer la distance, avec l'excellent package `colorscale`.
Avantage de cette façon de faire : on peut prendre en compte les différences dans les couleurs des zones, quelles que soient ces couleurs.
Inconvénient :

- la séquence de prévision météo utilisant parfois des signalétiques animées (des nuages allant de droite à gauche), l'image de référence ne prend la couleur médiane d'une des phases de cette animation.
- la présentatrice n'étant pas habillée de pied en cap de la même couleur, la présence de sa main, de ses cheveux ou de sa robe sur une même zone créera une distance différente sur la zone, bien que le résultat soit le même pour le spectateur : une zone cachée.

## Résultats

![logo OpenWeatherMap](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/openweathermap.png "logo OpenWeatherMap"){: .img-thumbnail-left }

Image par image, on peut voir le calcul : d'une vidéo vers une image (à gauche), et de cette image, on sort une couleur médiane par zone (au centre), et de cette couleur médiane on calcule la distance à la couleur médiane lorsque la carte est dégagée (à droite).

![Trois phases](https://user-images.githubusercontent.com/1596222/148133096-3c3349ea-f9ff-4d7e-9b73-1a163ad0fda1.gif "Trois phases"){: loading=lazy }

Au global, entre les bulletins du 2, 3, 11, 12, 13 et 14 janvier 2019 (c'est dire si l'étude est sérieuse !), on constate un rapport de 1 à 21 entre Vannes et Gap sur les écarts de couleurs affichées.

![Distance entre la couleur de référence et la couleur observée](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/meteo_inegalites_traitement_avec_r/distance_moyenne_toutes_journees_toutes_sequences.jpg "Distance entre la couleur de référence et la couleur observée"){: .img-center loading=lazy }

Pour la partie qui est le moins soumise à des variations de couleurs, car pas soumise à des animations, i.e. les séquences liées aux températures du lendemain, la zone où la variation est la plus faible connaît une distance de 0,16 à sa référence tandis que celle où la variation est la plus forte présente une distance de 43, soit un ratio de 1 à 268. Même ordre de grandeur pour les températures de l'après-midi avec un ratio de 1 pour 261.

Autrement dit, selon ce calcul si vous habitez Dijon, vous aurez un accès à l'affichage des températures du lendemain matin 260 fois moins obstrué que si vous habitez Brest.

Pour ce qui est de la partie relative aux prévisions de couverture (nuages, pluie, ciel bleu, etc.), le rapport est moins fort avec un ordre de grandeur de 1 pour 34 le matin et 1 pour 55 l'après-midi.

## Conclusion

Voilà donc la conclusion de notre enquête : **il est 20 fois plus difficile de lire ce qui concerne une zone bretonne qu'une zone de l'est ou du sud-est.**

[Consulter le code R :fontawesome-regular-file-code:](https://github.com/Valexandre/zones_meteo/blob/main/code.R){: .md-button }
{: align=middle }

!!! info "A noter"
    Comme vous pouvez vous en douter, ce projet a été réalisé sur mon temps personnel et n'a pas vocation à enfreindre les droits à l'image de la (excellente au demeurant) présentatrice en question, que je remercie d'avoir publié ces vidéos et ainsi m'avoir permis d'avoir enfin une réponse à une question de canapé.

----

<!-- geotribu:authors-block -->
