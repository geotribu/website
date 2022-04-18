---
title: "Les easter eggs de QGIS : chasser et être chassé"
authors:
    - Delphine MONTAGNE
    - Julien MOURA
categories:
    - article
date: "2022-04-18 14:20"
description: "Les easter eggs de QGIS sont connus : contributors, dizzy, hackfests, bored, user groups... Mais comment les dénicher ? Et surtout comment en créer de nouveaux ?"
image: "https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/qgis_316_easteregg_user_groups.png"
license: cc4_by-sa
robots: index, follow
tags:
    - cartographie
    - easter egg
    - jeux vidéo
    - PyQGIS
    - GitHub
    - QGIS
---

# Quand QGIS nous régale d'_Easter eggs_

:calendar: Date de publication initiale : 18 avril 2022

## Introduction

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-rdp-news-thumb }

Tradition ~~séculaire~~ technique popularisée avec l'avènement du [Konami Code](https://fr.wikipedia.org/wiki/Code_Konami), les [_easter eggs_](https://fr.wikipedia.org/wiki/Easter_egg) (oeufs de Pâques en bon français) sont des fonctions cachées par des développeurs mutins dans les logiciels, y compris parmi les plus utilisés. Par exemple, sur la distribution Debian (et donc les distributions  de la famille Ubuntu) peuvent entrer `apt moo` :

```bash
❯ apt moo
                 (__)
                 (oo)
           /------\/
          / |    ||  
         *  /\---/\
            ~~   ~~  
..."Have you mooed today?"...
```

Il y a même un site dédié à leur inventaire : <https://eeggs.com/>.

### Et ailleurs... dans la cartographie par exemple

C'est l'objet de la publication ["A la recherche des œufs de Pâques cartographiques" de Delphine Montagne](https://halshs.archives-ouvertes.fr/halshs-02508252/document) (magazine Carto, le monde en cartes, Areion, 2020, pp.54-55. halshs-02508252) :

[![Easter egg cartographique - Annecy](https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/easter_egg_carto_ign_annecy_delphine-montagne.png "Easter Egg - Lac d'Annecy (IGN) - Delphine Montagne HAL/Carto"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/easter_egg_carto_ign_annecy_delphine-montagne.png){: data-mediabox="lightbox-gallery" data-title="Easter Egg - Lac d'Annecy (IGN) - Delphine Montagne HAL/Carto"}

### Dans QGIS

Après avoir pris le temps d'essayer les [easter eggs listés sur Pasq.fr](https://pasq.fr/easter-egg-dans-qgis) et d'en faire [un tweet](https://twitter.com/geojulien/status/1378954806367297538) pour le lundi de Pâques, on m'indique qu'il en manque un : `user groups` ! Damned !

Mais comment les trouver à coup sûr ? Comment s'assurer de ne pas revenir bredouille de la chasse aux géœufs de Pâques ?

Je vous livre ma stratégie de battue :rabbit: !

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/suOhOAVOQ6g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

### Les Easter eggs et la cartographie papier

Les oeufs de Pâques se trouvent souvent dans un travail créatif et collectif. C'est le cas bien entendu des cartes papiers, comme présenté dans un article publié en 2020 dans le magazine [_Carto_](https://halshs.archives-ouvertes.fr/halshs-02508252/document).

[![Easter egg - Elépahant carte](https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/easter_egg_carto_elephant.webp "Easter egg - Elépahant carte"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/easter_egg_carto_elephant.webp){: data-mediabox="lightbox-gallery" data-title="Easter Egg - Eléphant dans une carte"}

Nouvelle expression : [avoir un éléplant dans la ~~pièce~~](https://fr.wikipedia.org/wiki/Elephant_in_the_room) carte. Cherchez bien, il est ~~en haut à gauche~~ au nord-nord-ouest, formé par un jeu avec les courbes de niveaux entre les chiffres 24 et 25. Cet oeuf de Pâques a été relevé par [Big Think](https://bigthink.com/strange-maps/670-nil-how-to-hide-an-elephant-the-1923-gold-coast-survey/) (mais l'histoire ne dit pas si l'on peut trouver en ce point du Ghana des éléplants).

### Croquer les oeufs de Pâques de QGIS

Incroyable projet collaboratif et créatif, QGIS a bien entendu lui aussi ses propres oeufs de Pâques, soigneusement dissimulés comme il se doit :

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/suOhOAVOQ6g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Ecrire le bon code au bon endroit : un moyen classique d'activer les Easter eggs ! Mais derrière ces amusantes cartes bonus et les jeux taquins proposés, on note, aussi, un message plus fort. En localisant ses développeurs, QGIS rend discrètement hommage aux personnes, peu visibles, qui l'ont codé. De même, inventorier les hackfests, c'est garder trace de l'histoire des grands événements de code qui rythment le développement du logiciel.

Ces Easter Eggs permettent de [mettre en avant un groupe discret](https://planet293.rssing.com/chan-13166735/all_p42.html) ainsi que des événements communautaires de manière élégante. Ils offrent une reconnaissance au précieux travail réalisé. La manière est elle aussi discrète, connue uniquement des personnes qui connaissent bien le SIG, donc au moins sensibilisées. Preuve du consensus de cette action, alors qu'il est possible d'effacer ces fonctionnalités grâce au code libre, cela n'a pas été remis en cause. Un beau cadeau pour les personnes qui développent... Et qui savent chercher ces oeufs sur ce drôle d'oiseau qu'est QGIS.

----

## La battue

!!! info
    Pour des raisons d'éthique évidentes, nous nous interdisons ici d'avoir recours à des armes de recherche massive qui pourraient mettre en péril le délicat équilibre des fonctions cachées. _Exit_ donc Google et consorts (quoique Qwant pourrait être toléré...)

### En planque

![GRASS loupe](https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/grass_mapset_search.svg "Planqué dans l'herbe"){: .img-rdp-news-thumb }

La première tactique est le dogme de la passivité : il suffit d'attendre bien sagement qu'une information sorte sur un easter egg. Au temps des infox, mieux vaut s'appuyer sur les sources officielles : les notes de version visuelles.

Véritable bijou de transparence et de vulgarisation des évolutions techniques d'un logiciel, ces _visual changelogs_ permettent également de faire des recherches à travers les âges de QGIS.

Cherchons donc [_easter egg_](https://www.qgis.org/en/search.html?q=easter+egg&check_keywords=yes&area=default) :

![Changelog QGIS - Recherche easter egg](https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/qgis_changelogs_search_easter_egg.png "Changelog QGIS - Recherche easter egg"){: .img-center loading=lazy }

Hum, cela nous mène uniquement à [celui apparu dans la 3.16](https://www.qgis.org/fr/site/forusers/visualchangelog316/index.html?highlight=fonction%20cach%C3%A9e#add-user-groups-easter-egg) et le moteur de recherche semble mal gérer les caractères spéciaux (espaces et accents), vu les résultats retournés par une [requête en français sur "fonction cachée"](https://www.qgis.org/fr/search.html?q=fonction+cach%C3%A9e).

Voilà qui ne suffit pas à satisfaire notre soif d'exhaustivité !

### Au coeur du terrier

![Octocat GitHub détective](https://octodex.github.com/images/inspectocat.jpg "Octocat GitHub détective"){: .img-rdp-news-thumb }

Prenons notre courage à `0:n` mains (oui, je reste vague pour n'exclure personne, pas même un/e éventuel/le lecteur/ice manchot/e) et allons à la source : le code sur GitHub :scream_cat:.  
L'occasion de démystifier ce qui se cache sous QGIS en se répétant ce que Napoléon disait toujours à ses troupes face aux cyber-attaques caratcéristiques de la campagne de Russie :

!!! quote "Napoléon - Cyber-campagne de Russie)
    N'ayez pas peur : les logiciels informatiques ne sont ni plus ni moins que des fichiers textes bien organisés !

Hauts les coeurs ! Si c'est du texte, il doit bien y avoir des traces des mots-clés qui déclenchent les _easter eggs_ !

Une fois infiltré dans le _repository_ (là où les gens qui parlent couramment machine entreposent le code source), on peut lancer [une recherche bien sentie](https://github.com/qgis/QGIS/search?q=%22user+groups%22&type=code) dans la barre en haut à gauche :

![Recherche dans le GitHub de QGIS](https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/qgis_github_search_easteregg.png "Rechercher dans le code de QGIS sur GitHub"){: .img-center loading=lazy }

C'est donc dans la [fonction de validation des coordonnées que se terrent les fonctions cachées](https://github.com/qgis/QGIS/blob/760a436f4f52a02533140b3f24c0828f8fdbd071/src/app/qgsstatusbarcoordinateswidget.cpp#L113-L161) :

En poussant plus loin notre avantage, on peut même retrouver [quand et par qui le dernier _easter egg_ a été proposé puis ajouté](https://github.com/qgis/QGIS/pull/38505) et au passage prendre connaissance du [tableau de suivi des groupes d'utilisateur/ices de QGIS dans le monde](https://docs.google.com/spreadsheets/d/1Wte5pfcpOeZ1bfBUn7KJuYzw31_rtKyGqciBPW3RXwg/edit#gid=678994363).

C'est fou la transparence, c'est beau l'open source :heart_eyes: !

----

## Auteur

--8<-- "content/team/jmou.md"

{% include "licenses/cc4_by-sa.md" %}
