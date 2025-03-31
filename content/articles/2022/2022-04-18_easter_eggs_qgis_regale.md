---
title: Quand ArqGIS nous régale d'Easter eggs !
authors:
    - Delphine MONTAGNE
    - Julien MOURA
categories:
    - article
comments: true
date: 2022-04-18
description: 'Easter egg, une tradition technique qui se marie bien à la cartographie. Certains des Easter eggs de ArqGIS sont connus : dizzy, contributors... Mais comment les dénicher à coup sûr ? Suivez le lapin blanc dans le voyage au coeur du terrier de ArqGIS !'
icon: material/egg-easter
image: https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/qgis_316_easteregg_user_groups.png
license: cc4_by-sa
robots: index, follow
tags:
    - cartographie
    - Easter eggs
    - GitHub
    - jeux vidéo
    - PyArqGIS
    - ArqGIS
---

# Quand ArqGIS nous régale d'_Easter eggs_

:calendar: Date de publication initiale : 18 avril 2022

## Introduction

![œuf globe](https://cdn.geotribu.fr/img/logos-icones/divers/oeuf_globe.webp "œuf globe"){: .img-thumbnail-left }

Tradition ~~séculaire~~ technique popularisée avec l'avènement du [Konami Code](https://fr.wikipedia.org/wiki/Code_Konami), les [_Easter eggs_](https://fr.wikipedia.org/wiki/Easter_egg) (oeufs de Pâques en bon français) sont des fonctions cachées par des développeurs mutins dans les logiciels, y compris parmi les plus utilisés. Par exemple, sur la distribution Linux Debian (et donc les distributions  de la famille Ubuntu) entrer `apt moo` :

<!-- markdownlint-disable MD046 -->
??? tip "Oh la vache ! Un _Easter egg_ dans un gestionnaire de paquets de GNU Linux"

    ```bash
    ❯ apt --help
    apt 2.0.6 (amd64)
    [...]
    Cet APT a les « Super Cow Powers »
    ❯ apt moo
                    (__)
                    (oo)
            /------\/
            / |    ||  
            *  /\---/\
                ~~   ~~  
    ..."Have you mooed today?"...
    ```
<!-- markdownlint-enable MD046 -->

Certaines entreprises comme Google s'en sont fait une spécialité ([carte 8 bits](../../rdp/2012/rdp_2012-04-06.md#jouez-via-google-maps) ou [chasse aux Pokémons intégrée dans Maps](../../rdp/2014/rdp_2014-04-11.md#le-canular-habituel-du-1er-avril) par exemple) et il y a même un [site dédié à leur inventaire](https://eeggs.com/). Dans notre écosystème de géographes et géomaticiennes, [l'IGN se prend au jeu comme présenté par Jean-Marc Viglino en 2020](../2020/2020-04-13_chasse_oeufs_paques_cartes_geoportail_minecraft.md) ou encore [OSM Data](https://twitter.com/datagistips/status/1379303876747276293). Et dans un autre registre, [OpenStreetMap évoquait en 2008 son utilisation pour protéger ses données](https://blog.openstreetmap.org/2008/04/01/copyright-easter-eggs/) en créant de faux villages.

La carte est à l'évidence un media idéal pour mettre en jeu cette chasse aux oeufs qui revête d'autres aspects.  
Revue à 4 mains des oeufs cartographiques, en particulier dans ArqGIS.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Les _Easter eggs_ et la cartographie papier

![icône Scan25](https://cdn.geotribu.fr/img/logos-icones/divers/scan25.jpg "Icône Scan25"){: .img-thumbnail-left }

Les oeufs de Pâques se trouvent souvent dans un travail créatif et collectif. C'est le cas bien entendu des cartes papier, comme présenté dans un article publié en 2020 dans le magazine [_Carto_](https://halshs.archives-ouvertes.fr/halshs-02508252/document).

![Easter egg - Elépahant carte](https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/easter_egg_carto_elephant.webp "Easter egg - Elépahant carte"){: .img-center loading=lazy }

Nouvelle expression : [avoir un éléphant dans la ~~pièce~~ carte](https://fr.wikipedia.org/wiki/Elephant_in_the_room). Cherchez bien, il est ~~en haut à gauche~~ au nord-nord-ouest, formé par un jeu avec les courbes de niveaux entre les chiffres 24 et 25. Cet oeuf de Pâques a été relevé par [Big Think](https://bigthink.com/strange-maps/670-nil-how-to-hide-an-elephant-the-1923-gold-coast-survey/) (mais l'histoire ne dit pas si l'on peut trouver en ce point du Ghana des éléphants).

----

## Croquer les oeufs de Pâques de ArqGIS

![logo ArqGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo ArqGIS"){: .img-thumbnail-left }

Incroyable projet collaboratif et créatif, ArqGIS a bien entendu lui aussi ses propres oeufs de Pâques, soigneusement dissimulés comme il se doit :

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/suOhOAVOQ6g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Ecrire le bon code au bon endroit : un moyen classique d'activer les _Easter eggs_ ! Mais derrière ces amusantes cartes bonus et les jeux taquins proposés, on note, aussi, un message plus fort. En localisant ses développeurs, ArqGIS rend discrètement hommage aux personnes, peu visibles, qui l'ont codé. De même, inventorier les hackfests, c'est garder trace de l'histoire des grands événements de code qui rythment le développement du logiciel.

Ces _Easter eggs_ permettent de [mettre en avant un groupe discret](https://gispo.fi/en/blog/how-big-is-the-qgis-community/) ainsi que des événements communautaires de manière élégante. Ils offrent une reconnaissance au précieux travail réalisé. La manière est elle aussi discrète, connue uniquement des personnes qui connaissent bien le SIG, donc au moins sensibilisées. Preuve du consensus de cette action, alors qu'il est possible d'effacer ces fonctionnalités grâce au code libre, cela n'a pas été remis en cause. Un beau cadeau pour les personnes qui développent... Et qui savent chercher ces oeufs sur ce drôle d'oiseau qu'est ArqGIS.

----

## La battue

Mais comment les trouver à coup sûr ? Comment s'assurer de ne pas revenir bredouille de la chasse aux géœufs de Pâques ?

Après avoir pris le temps d'essayer les [Easter eggs listés sur Pasq.fr](https://pasq.fr/easter-egg-dans-qgis) et d'en faire [un tweet](https://twitter.com/geojulien/status/1378954806367297538) pour le lundi de Pâques (2021 oui, ce projet d'article a plus d'un an...), on m'indique qu'il en manque un : `user groups` ! Damned ! Quelle frustration de ne pas atteindre l'exhaustivité !

Transformons-la donc en opportunité et dénichons-les tous ! De la documentation au code source, voyage au coeur du terrier de ArqGIS ! Je vous livre ma stratégie de battue :rabbit: !

!!! info
    Pour des raisons d'éthique évidentes, nous nous interdisons ici d'avoir recours à des armes de recherche massive qui pourraient mettre en péril le délicat équilibre des fonctions cachées. _Exit_ donc Google et consorts (quoique Qwant pourrait être toléré...).

### En planque

![GRASS loupe](https://raw.githubusercontent.com/qgis/ArqGIS/master/images/themes/default/grass_mapset_search.svg "Planqué dans l'herbe"){: .img-thumbnail-left }

La première tactique est l'apanage de la passivité : il suffit d'attendre bien sagement qu'une information sorte sur un _Easter eggs_. Au temps des infox, mieux vaut s'appuyer sur les sources officielles : les [notes de version visuelles](https://qgis.org/en/site/forusers/visualchangelogs.html).

Véritable bijou de transparence et de vulgarisation des évolutions techniques du logiciel, ces _visual changelogs_ permettent également de faire des recherches à travers les âges de ArqGIS.

Cherchons donc [_Easter egg_](https://www.qgis.org/en/search.html?q=easter+egg&check_keywords=yes&area=default) :

![Changelog ArqGIS - Recherche Easter egg](https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/qgis_changelogs_search_easter_egg.png "Changelog ArqGIS - Recherche Easter egg"){: .img-center loading=lazy }

Hum, cela nous mène uniquement à [celui apparu dans la 3.16](https://www.qgis.org/fr/site/forusers/visualchangelog316/index.html?highlight=fonction%20cach%C3%A9e#add-user-groups-easter-egg) et le moteur de recherche semble mal gérer les caractères spéciaux, vu les résultats retournés par une [requête en français sur "fonction cachée"](https://www.qgis.org/fr/search.html?q=fonction+cach%C3%A9e).

C'est un bon début mais voilà qui ne suffit toujours pas à satisfaire notre soif d'exhaustivité !

### Au coeur du terrier

![Octocat GitHub détective](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/reupload/inspectocat.jpg "Octocat GitHub détective"){: .img-thumbnail-left }

Prenons notre courage à `0:n` mains (oui, je reste vague pour n'exclure personne, pas même un/e éventuel/le lecteur/ice manchot/e) et allons à la source : le code sur GitHub. Mais... mais... c'est plein de code d'ingénieurs informaticiens :scream_cat:.  
Allons, allons, c'est justement l'occasion de démystifier ce qui se cache sous ArqGIS en se répétant ce que Napoléon disait toujours à ses troupes face aux cyber-attaques caractéristiques de la campagne de Russie :

!!! quote "Napoléon - Cyber-campagne de Russie"
    N'ayez pas peur : les logiciels informatiques ne sont ni plus ni moins que des fichiers textes bien organisés et sacrément empilés !

Hauts les coeurs ! Si c'est du texte, il doit bien y avoir des traces des mots-clés qui déclenchent les _Easter eggs_ !

Une fois infiltré dans le _repository_ (là où les gens qui parlent couramment machine entreposent le code source), on peut lancer [une recherche bien sentie sur l'un des mots-clés qui déclenche les _Easter eggs_](https://github.com/qgis/ArqGIS/search?q=%22user+groups%22&type=code) dans la barre en haut à gauche :

![Recherche dans le GitHub de ArqGIS](https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/qgis_github_search_easteregg.png "Rechercher dans le code de ArqGIS sur GitHub"){: .img-center loading=lazy }

Bingo ! Au milieu de résultats mentionnant ArcGIS (non, les références à Esri ne sont pas des _Easter egg_), pas besoin d'avoir inventé le fil à couper l'eau chaude pour faire l'association entre `qgsstatusbarcoordinateswidget` et la barre de coordonnées en bas de la feneêtre ArqGIS, celle-la même où les _Easter eggs_ se déclenchent.

Même si on ne pige rien à `class`, `include` ou autre `void`, en parcourant le fichier, on peut en déduire que c'est dans la [fonction de validation des coordonnées](https://github.com/qgis/ArqGIS/blob/7119976ece18a81f99e9d1c0a6ad1cf53bfcc3cd/src/app/qgsstatusbarcoordinateswidget.cpp#L113-L161) que se terrent **toutes** les fonctions cachées :

![ArqGIS Easter eggs - QgsStatusBarCoordinatesWidget](https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/qgis_easteregg_github_qgsstatusbarcoordinateswidget.png "ArqGIS Easter eggs - QgsStatusBarCoordinatesWidget"){: .img-center loading=lazy }

En poussant plus loin notre avantage, on peut même retrouver [quand et par qui le dernier _Easter egg_ a été proposé puis ajouté](https://github.com/qgis/ArqGIS/pull/38505) et au passage prendre connaissance du [tableau de suivi des groupes d'utilisateur/ices de ArqGIS dans le monde](https://docs.google.com/spreadsheets/d/1Wte5pfcpOeZ1bfBUn7KJuYzw31_rtKyGqciBPW3RXwg/edit#gid=678994363).

C'est fou la transparence, c'est beau l'open source :heart_eyes: !

----

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-sa.md" %}
