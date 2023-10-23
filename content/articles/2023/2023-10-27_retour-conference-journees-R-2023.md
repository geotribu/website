---
title: "Retour sur les Rencontres R d'Avignon"
authors:
    - Delphine Montagne
categories:
    - article
date: "2023-10-27 10:30"
description:
icon: fontawesome/solid/bridge-water
license: default
robots: index, follow
tags:
    - conférence
    - R
---

# Spatial, R, code et communauté : retour sur les rencontres R

:calendar: Date de publication initiale : 27 octobre 2023

## Introduction

![Pastille hexagonale de R aux couleurs jaune coquille d'oeuf et bleu azur d'Avignon](https://pad.oslandia.net/uploads/5b19df77-7a2a-4b46-b7b2-6440a6baa3c2.png){: .img-rdp-news-thumb }

En juin dernier, Avignon a accueilli les [Rencontres R](https://rr2023.sciencesconf.org/), le plus grand événement français dédié au célèbre logiciel libre de statistiques. Il y avait un invité spécial : le spatial. Ce qui tombe bien, car si je ne suis plus débutante sur ce logiciel, j'ai encore des marches de progression à passer. C'est de ce point de vue que je propose ce retour sur trois jours de présentations et de discussions.

## Découvrir le spatial et R : l'atelier pratique

Le premier jour des rencontres commence officiellement l'après-midi, le temps que tout le monde arrive sur le site. L'organisation (je reviendrai sur ce point plus bas) a donc banalisé la matinée avec des tutoriels. Si le [machine learning](https://github.com/abichat/rr23-tuto-tidymodels)  était proposé, si [Quarto](https://cderv.quarto.pub/tuto-quarto-rr2023/) était également au menu...

![Adoreble image d'un hérisson frileux tricotant HTML, Word, PDF, LATEX, sites internet etc... Comme le fait Quarto](https://pad.oslandia.net/uploads/afc2c3bd-e0d4-45a1-9cd4-71595d7c9a88.png){: .img-center loading=lazy }

La [session Quarto](https://cderv.quarto.pub/tuto-quarto-rr2023/) avait l'air très ~~piquante~~ chouette.
*llustration par Alison Hill and Allison Horst, pour RStudio, tirée de la présentation de Christophe Dervieux.*

... j'étais bien évidemment inscrite à l'atelier d'[analyse spatiale avec R](https://github.com/antuki/RR2023_tuto_statspatiale) proposé par Kim Antunez (INSEE) et Etienne Côme (Université Gustave Eiffel). Au programme, carte statistiques, cartes interactives et analyse spatiale avec les deux.
D'abord on parle des cartes statiques, avec la révolution de "sf" et sa déclinaison spatiale "sfg", soit *[simple feature geometry](https://r-spatial.github.io/sf/articles/sf1.html)*, qui a l'avantage d'être composé d'autre chose que de "0" et "1", ce qui le rend compréhensible par un être humain.

![Tableau de données avec des exemples de simple feature](https://pad.oslandia.net/uploads/53636f5d-6c41-4635-97a5-4f8fddaaf69c.png){: .img-center loading=lazy }

Le package [mapsf](https://riatelab.github.io/mapsf/) a pris le pas sur d'autres, comme cartography. J'y ai notamment appris l'existence du [geoparquet](https://geoparquet.org/) pour traiter les gros volumes de données spatiales... Et que différentes versions de R peuvent bloquer dans des exercices sans que l'on n'est aucun message d'erreur (sinon ce n'est pas drôle).
Je n'ai pas eu le temps de tout explorer pour la partie carte interactive, les deux heures étant très denses pour tout le programme prévu. C'est donc un atelier parfait pour les géographes, mais les personnes extérieures à cette thématique sont restées bloquées sur les tenants et aboutissants de termes comme les zones tampons ou polygones de Voronoï.

## Aurélie Vache : combattre le sentiment d'imposture

Le choix d'une conférence d'ouverture est un exercice d'équilibriste. Il faut offrir un contenu riche, tout en étant accessible et percutant. Avec ce cahier des charges en tête, le choix d'Aurélie Vache était plus que brillant.
Après avoir rappelé que c'est un problème de comparaison, que l'on trouve donc beaucoup dans le milieu de la tech' et particulièrement dans l'informatique, que les femmes sont assez touchées (mais pas uniquement), elle a donné de bonnes astuces  :

1. Être dans une communauté ;
2. Rédiger des articles sur son blog perso, puis sur d'autres (Géotribu par exemple), dans des journaux, faire des conférences et aller dans des écoles ;
3. Ne pas copier les autres, avoir confiance en ses idées et son style ;
4. Tooter ce que l'on a appris aujourd'hui, pour les autres comme pour soi ;
5. Faire du pair programming ;
6. Face aux haters, s'appuyer sur ses personnes proches (cercle amical, famille, collègues de confiance) ;
7. Demander des retours et non pas de la validation.

Au passage, elle a égratigné avec un mordant libérateur l'obligation d'avoir le bon cursus, voire la passion des recrutements avec obligatoirement LE diplôme de LA bonne école.

Elle a rappelé le [validisme](https://fr.wikipedia.org/wiki/Capacitisme) ambiant, dont nos milieux ne sont pas épargnés, avec le talent de quelqu'un capable de présenter avec humour des horreurs. Bonne nouvelle, pour la voir changer de la boue en or, sa présentation a été filmée et je ne peux que vous la conseiller :

<iframe width="100%" height="315" src="https://www.youtube-nocookie.com/embed/sPiu8us444w?si=al1kSSL5il7qLB8Y" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

----

## Les paillettes de Lise Vaudor (épisode 1)

![logo glitteR](https://pad.oslandia.net/uploads/3641f389-3481-48ea-afd8-da1e2d0ef716.png){: .img-rdp-news-thumb }

Le package GlitteR explore le web sémantique, comprenez des données qui sont elles-même reliées à d'autres données, ce qui donne par exemple Wikidata. J'ai appris que l'on y accède grâce à des points d'accès, les *endpoint*. Lise Vaudor rappelle fort justement que l'inconvénient des graphes de connaissance, c'est que l'on ne peut pas avoir une vision d'ensemble comme avec un tableau... D'où l'importance de connaître son terrain ou de partir d'un terrain connu afin de pouvoir couper les branches inutiles du graphe. Et GLitteR dans tout cela ? Il permet d'accéder aux données de Wikidata avec R, sans avoir à passer par le SPARQL. Une grosse avancée pour les personnes pas du tout à l'aise avec ce langage. Il est vrai que tout le monde n'a pas encore eu de [wikimédien ou wikimédienne en résidence](https://fr.wikipedia.org/wiki/Projet:Wikifier_la_science) (patience).

----

## Shiny selon Enedis

Chez Enedis, l'application Shiny est traitée de manière très originale : comme un prototype de futures potentielles applications. Par exemple, peut-on ajouter une borne de recharge électrique sans faire de surcharge sur le réseau ? Avec Shiny, on peut modéliser l'ajout d'une borne et voir ce qui se passe.

![Copie d'écran d'une carte modélisant une nouvelle borne et ses conséquences sur l'approvisionnement](https://pad.oslandia.net/uploads/a0265cad-bf96-4ed1-859d-3ded0b161515.png){: .img-center loading=lazy }

(Les données sont factices)

Ce qui m'a le plus intéressée, [c'est leur méthode](https://www.youtube.com/watch?v=NzruKscUUdE) : Shiny est pensé pour avoir des retours et des améliorations continues durant 3 ans.

Ça marche ? Enedis développe une application dédiée hors Shiny.

Ça ne marche pas ? Abandon de ce test, sans avoir eu à avancer trop de moyens coûteux.

----

## L'INSEE passe à R

C'est *LA* grande annonce du colloque. L'institution publique de la statistique française passe sur *LE* logiciel libre des statistiques. Un changement pareil ne se fait pas naturellement dans une institution aussi ancienne. Alors comment a-t-elle fait ?

1️⃣ Un choix institutionnel, et donc impulsé en tant que tel ;

2️⃣ Montrer ce que l'on peut faire de plus avec R par rapport à SAS ;

3️⃣ Beaucoup de formations et de supports partagés en interne ;

4️⃣ Mobilisation de Quarto et de RMarkdown.

Comment impulser de bonnes pratiques de codage, comme la documentation ? L'INSEE en a [listé plusieurs ici](https://inseefrlab.github.io/formation-bonnes-pratiques-git-R/), dont :

- Le code est plus lu qu'écrit ;
- La maintenance du code est coûteuse ;
- Aller vers Git permet de l'améliorer rien que par l'idée d'avoir un potentiel regard extérieur ([Foucault](https://fr.wikipedia.org/wiki/Panoptique) ne pourrait être que d'accord) ;
(même si, attention, il faut une bonne journée de formation sur Git pour le prendre en main)
- Faire de l'amélioration graduelle du code, peu à peu.

## Les RLadies françaises

Depuis 2016, il existe un [groupe des Rladies en France](https://www.youtube.com/watch?v=MIcMzFtTAuw) qui regroupe plus de 500 personnes. Beaucoup de leurs événements parisiens sont aussi disponibles en ligne, [comme les rediffusions](https://www.youtube.com/@rladiesparis) de leurs réunions.

<iframe width="100%" height="315" src="https://www.youtube-nocookie.com/embed/MIcMzFtTAuw?si=8qdbVnhyAEcz5nzG" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Publier ses réalisations sur R

Faire du code R, ui. Faire de magnifique réalisations, ui à nouveau. Les documenter (un motif récurrent de ces conférences, vous l'aurez noté), c'est mieux. Face à la dispersion des ressources sur R en sciences humaines et sociales, nous avons eu la présentation de [Rzine](https://rzine.fr/). Ce site internet centralise la documentation existante, mais aussi et surtout, il permet de *publier* des fiches techniques inédites. Avec un DOI bien sûr ! Idéal pour valoriser son travail, notamment dans les environnements de recherche.

## L'informatique partage ses bonnes pratiques pour R

C'est [une présentation si dense et riche](https://www.youtube.com/watch?v=4uXaRx4USnI) qu'il vaut mieux renvoyer à la vidéo pour en prendre tous les (nombreux) éléments intéressants en fonction de son niveau. Mais pour une non-informaticienne comme moi, en voici quelques uns :

- Documenter sur quoi tourne le code (Windows, version de R...) ;
- Documenter à quoi sert le code, comment l'utiliser, les pistes abandonnées et les expérimentations ;
- La configuration (URL externes, coefficients etc.) doit être écrite **dans un fichier annexe** ;
- Utiliser des "*styles guides*" qui lisent toutes les erreurs et tous les bugs les plus courants (ex : nommer ses variables autrement que a1, a2) ;
- Utiliser Git (encore un motif réccurent) ;
- Les correctifs de données **font partie** des sources de données. On ne corrige pas les données après les avoir importées, on importe des correctifs comme des sources de données.

## Data visualisation et R

Yan Holtz est revenu durant cette planière sur présentation des données avec R et sur les outils utiliser en fonction du public.
Par exemple, si des collègues ont du mal sur R, leur proposer [datawrapper](https://www.datawrapper.de/).
Il est revenu sur ggplot2, qui en 2007 a été une révolution en faisant passer R d'un outil *exploratoire* à un outil **explicatif** qui permet de faire de la dataviz avec R. Une révolution qui a infusé jusqu'à Python et javascript. Il a également mentionné "R tutor" pour faire du Shiny aidé par chatGPT.

## L'IGN en mode happi

L'[IGN a présenté LE package](https://www.youtube.com/watch?v=Ha44VTGhOVo) qui permet d'accéder à toutes ses données, Lidar compris : ⭐ happign ⭐. C'est un des éléments qui me fait aimer R et me pousse à m'y former : la facilité d'accès aux données avec le logiciel.

## Un package spatial : Timothée Giraud et mapsf

On l'a indiqué, ces journées R portaient spécialement sur le spatial. Timothée Giraud est donc venu présenter le travail autour du package phare : mapsf.

Il a commencé par un historique rappelant la généaologie des différents packages qui intègrent la géographie et qui petit à petit permis l'émergence de : ⭐mapsf⭐ .

On l'a dit plus haut, mapsf s'appuie sur le standard *simple feature* (aussi mobilisé par postgis) pour importer, exporter et faire les géotraitements de données géographiques. Il est également revenu sur la mise à la retraite d'un package, exemplaire selon lui de ce qu'il faut bien faire dans la communauté (ne régligez donc pas les stages de préparation à la retraite).

Il est revenu sur les possibilités de package, avec des exemples avignonnais évidemment.

J'ai appris que la commuanuté R avait une passion pour les palettes de couleur. Avec par exemple paletteer et l'appli shiny cols4all qui permet de tester le rendu pour les personnes daltoniennes... Du moins si les fantastiques palettes [ColorBrewer](https://fr.wikipedia.org/wiki/Cynthia_Brewer), déjà incluses dans `mapsf`, ne suffisent pas.

## Les paillettes de Lise Vaudor (épisode 2)

C'est au tour de [la présentation de Lise Vaudor](https://www.youtube.com/watch?v=fIJ9gr1MK2Q) qui nous propose un retour sur son parcours et ses réalisations.

Ingénieure agronome, elle a été recrutée au CNRS après sa thèse en écologie/statistiques, notamment grâce à ses compétences en R. Son travail au qotidien s'articule autour du soutien à la recherche et elle propose beaucoup de formation continue... Notamment auprès d'un public doctorant tRaumatisé.

C'est de cette expérience de terrain qu'est né son [blog Ratique](https://perso.ens-lyon.fr/lise.vaudor/) et la création de contenu visant à démocratiser R. Un contenu qu'elle a voulu illustré, avec ses propres dessins (tant qu'à faire), avec des couleurs pastels, des ~~GlitteR~~ paillettes et des blagues. Elle propose des anti-sèche illustrées et soignées (devinez les couleurs ? pastels, bravo) et des métaphores visuelles accessibles qui piochent dans la dataviz. Du contenu créé *sur son temps de travail* (et valorisé comme tel par le CNRS).

Comment parler à tout le monde quelque soit la discipline ? Lise Vaudor transporte son public dans le monde de la magie grâce à ses "grimoires". Mais elle travaille moins sur ce contenu ces temps-ci.

Car elle est revenue sur son parcours personnel, notamment sa double maternité a quelque peu chamboulé sa vie. Elle a donc rejoint les RLadies, "seulement maintenant" car elle n'en ressentait pas le besoin. Elle indique ne pas avoir eu à souffrir de sexisme dans la communauté R.

Les raisons ?

Pour elle, c'est l'ouverture de la communauté. Une ouverture qui se retrouve aussi dans l'équipe du programme de ces journées, qui a voulu mettre à égalité les différents genres, mélanger secteur privé/public, universitaire et non-universitaire etc.

C'est une communauté capable de valoriser ses paillettes, ses dessins, ses couleurs pastels et tout le contenu de ses formations, par cette invitation à une intervention dans une plénière. Une intervention au même niveau que celle de gros packages, comme celui de Timothée Giraud. A titre personnel, ce point de l'intervention m'a beaucoup marquée.

## Quelles bonnes idées à piquer à l'organisation ?

Ce n'est bien entendu pas visible dans ce compte-rendu : les Rencontres R étaient mûrement réfléchies en termes d'inclusion et d'environnement. C'est la première fois que je viens à un événement professionnel avec une [code de conduite](https://rr2023.sciencesconf.org/resource/page/id/10). Cette charte est à signer lors de l'inscription, rappelée en plénière, à chaque moment collectif et nous avons eu une présentation des personnes à qui s'adresser en cas de problème. C'était bienvenu.

L'engagement était aussi écologique : les goodies venaient des environs. La bière, brassée spécialement pour l'occasion, était locale, tout comme le jus de fruit. Nous avions de la verrerie, produite elle aussi tout proche, aux couleurs des rencontres et que l'on utilisait donc pour les pauses cafés. Le tour de cou, avec un clin d'oeil malin à R, rappelait toutes les informatiques pratiques, dont le programme numérique, le programme papier étant limité aux rares personnes sans téléphone. Enfin, pour garder un ultime souvenir de ces journées, le tour de cou peut se planter afin d'obtenir de délicieuses plantes aromatiques.

----

## Autrice

--8<-- "content/team/dmon.md"

{% include "licenses/default.md" %}
