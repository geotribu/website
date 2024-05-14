---
title: 'Qualité des données : un voyage sur la plateforme humanitaire d''OpenStreetMap'
authors:
    - Delphine Montagne
categories:
    - article
comments: true
date: 2023-03-27
description: Offrir des données de qualité quand elles sont produites par des centaines de personnes de niveaux différents est un défi. Focus sur les méthodes en cartographie humanitaire avec HOT OSM.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/hot_validation_qualite_donnees.png
license: default
robots: index, follow
tags:
    - CartONG
    - HOT OSM
    - JOSM
    - OpenStreetMap
    - qualité
---

# Qualité des données : un voyage sur la plateforme humanitaire d'OpenStreetMap

:calendar: Date de publication initiale : 27 mars 2023

## Introduction

![logo HOT OSM](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/hot_osm.png){: .img-thumbnail-left }

Le 6 février 2023, la Turquie et la Syrie ont été touchées par [l’un des plus importants tremblements de terre de la région](https://fr.wikipedia.org/wiki/S%C3%A9ismes_de_2023_en_Turquie_et_Syrie). À la radio, à la télévision, sur les réseaux sociaux s’égrène le nombre de victimes et le coût des dégâts, des chiffres froids pour tenter d’exprimer l’ampleur de la catastrophe.

Pour moi, c’est le signal que [HOT](https://tasks.hotosm.org/explore), la plateforme humanitaire d’OpenStreetMap, va bientôt déclencher une mission urgente et que mon aide sera nécessaire.

## La force du crowdsourcing cartographique

Très vite en effet, la plateforme propose différents projets sur l'évenement. La cartographie se réalise grâce aux images aériennes sur une zone découpée en petits carrés.

![Début de validation d'une zone avec des carrés plus ou moins carrés](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/00_hot_grille_travail.webp){: .img-center loading=lazy }

> Un découpage plus ou moins carré

Le découpage renseigne sur l'état d'avancement avec en bleu la zone cartographiée, un cadenas quand le travail est en cours, du vert pour la zone validée quand le gris signale une mauvaise imagerie.

Des bénévoles de tous niveaux (dont vous peut-être ?) choisissent une tâche qu’ils et elles complètent en ajoutant les informations sur OpenStreetMap. Quand tous les carrés sont terminés, la zone est cartographiée et les données ouvertes produites serviront immédiatement aux différentes équipes sur place. Une partition parfaitement maîtrisée depuis le [séisme d’Haïti de 2010](https://fr.wikipedia.org/wiki/S%C3%A9isme_de_2010_en_Ha%C3%AFti), jouée de jour comme de nuit grâce à un relais entre les différents fuseaux horaires : [OpenStreetMap ne dort jamais](https://live.openstreetmap.fr/).

Mais comment s’assurer que ces multiples contributions de personnes de niveaux et d’expériences différentes permettront d’obtenir des données homogènes à utiliser sur place, sans oubli ou erreur ? C’est là qu’intervient l’équipe de validation, dont je fais partie.

![Ma validation : feu vert pour le terrain](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/01_hot_carto_refugies.webp){: .img-center loading=lazy }

----

## Valider les données : une relecture par des pairs

Selon la logique que plusieurs regards sont complémentaires, mon travail de validatrice commence par la vérification des consignes du projet. Le plus souvent, il est demandé de cartographier des bâtiments, complétés généralement par le réseau routier, parfois les cours d’eau, plus rarement l’occupation du sol.

### Bâtir une carte valide : la validation des bâtiments

En premier, je regarde les oublis. Toutes les maisons ont-elles été cartographiées ? Si en zone rurale l’opération ressemble à une chasse aux trésors, au contraire en zone urbaine un bâtiment peut en cacher un autre. Sont-ils bien dessinées un par un ? Avec la bonne forme ? La norme étant le carré, le rectangle et le rond, tout ce qui en dévie doit être vérifié.

![Carte avec un fouillis de bâtiments mal dessinés](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/02_hot_validation_batiments.webp){: .img-center loading=lazy }

> Exemple de cartographie à reprendre : chaque maison doit être tracée une par une et non en groupe, notez les problèmes de formes et à ~~droite~~ l'est un bâtiment dans un bâtiment.

Je traque les superpositions de bâtiments et je devine où se termine un toit dissimulé par un arbre. Je tourne, je redimensionne et je déplace les bâtiments pour les ajuster à l'image. Mais il y a des pièges ! Attention à ne pas confondre un carré de terre, une voiture, un arbre ou des murs avec une maison. Même l’intelligence artificielle, mobilisée sur certains projets, s’y trompe.

![Image aérienne d'une double entreprise de construction : la zone industrielle qui fait de la construction et la carte en cours](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/03_hot_validation_batiments_imagerie.webp){: .img-center loading=lazy }  

> Cartographie de voitures et de matériaux entreposés, corrigée par la validation.

Pour m’aider, je regarde les ombres, je mesure la taille des objets, je compare au reste de la zone et pour statuer je suis attentive aux détails que laisse voir l’imagerie. Surtout, je passe mon temps à zoomer et dézoomer sur la zone.

![Avant/après la validation](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/04_hot_validation_batiments_finale.webp){: .img-center loading=lazy }

> Validation : bâtiments tracés un par un, correction des formes, ajustement de la zone résidentielle, correction d'une hélisurface.

### Faire se déplacer les personnes : valider les routes

Zoomer et dézoomer, c’est une opération continuelle en validant les routes. Plus que leur existence, la validation cherche à savoir si elles sont nécessaires. Les informations doivent permettre aux personnes de se déplacer sur place et de se représenter les lieux. Je réunis des petits bouts de routes pour en faire une seule, je coupe et je recolle les routes pour gagner en cohérence. J’enlève des nœuds qui ne sont pas nécessaire, surtout quand le reste de la zone cartographiée n'est pas aussi précis, et j’adoucis la courbe de virages par des ajouts là où il y a des manques. Nul besoin d’avoir des données inutilement volumineuses !

![« Qu’est-ce que c’est que ce bazar ? », leitmotiv de la validation](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/05_hot_validation_routes_cas.webp){: .img-center loading=lazy }

> Route en rouge non reliée, morceaux de routes non harmonisés au sud, triangle de route d'une précision inutile au croisement et route à poursuivre à l'est

Cartographier des routes, c’est penser réseau : une route mène forcément quelque part. Sinon, il faut se poser la question de son utilité. Son tracé peut se trouver caché par des forêts, du sable, une zone d’ombre, un nuage, être effacé et reprendre plus loin… Quand cela ne conduit pas à s’apercevoir quelques mètres après que c’est une rivière intermittente.

![Image aérienne et une route étrange...](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/06_hot_validation_routes_riviere.webp){: .img-center loading=lazy }

> A l'ouest, la couleur verte montre une zone humide. La zone étudiée pouvait faire penser à une route, à une autre échelle les méandres sont typiques d'un cours d'eau.

J’ajoute des points d’intersection entre deux lignes (la topologie, une passion) et je connecte des routes qui paraissent si proches que l’on a oublié de les relier. En fonction des consignes, je vérifie qu’elles sont de la bonne catégorie, c’est rarement le cas des routes résidentielles. J’harmonise, je complète, je répare, j’ajuste : tout pour rendre une appli de routing heureuse !

![Voiture blanche sur une route vue d'une image aérienne. Le tracé de la cartographie semble courir derrière le véhicule](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/07_hot_validation_routes_vehicule.webp){: .img-center loading=lazy }  
> Parfois, trouver une route, ainsi que sa classification en route pratiquable pour un véhicule, est intuitive.

La gestion d’un réseau est une opération tellement minutieuse que dans les zones avec beaucoup de travail, je m’occupe d’abord uniquement des bâtiments, ensuite des routes et enfin des deux. Mon objectif est de me mettre mentalement dans la tête des personnes qui auront besoin des données. Car paradoxalement, la qualité est invisible, ce sont les erreurs qui font en prendre conscience.

----

## Valider : une opération de décentrement

Généralement, la cartographie se fait « égoïstement » sur un carré bien délimité. Lorsque l’on valide, il faut réfléchir à l’échelle des carrés voisins, voire à l’échelle de tout le projet. On apprend très vite les classiques effets de bords : une maison pile entre deux carrés, tout le monde pense que c’est à l’autre de s’en occuper, et le bâtiment n’est pas cartographié du tout (pensez à sa solitude et son sentiment d’abandon).

![Suite de lacs noirs au milieu d'une zone de cailloux formant un visage de souffrance, hurlant en silence](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/08_imagerie_pleureuse.webp){: .img-center loading=lazy }

> Comment survivre à une zone mal cartographiée ? En trouvant une imagerie qui pleure encore plus que soi.

J’ai toujours en tête les différentes pratiques sur place et l’utilisation des données. Il faut rester humble : je fais de la cartographie dite « de fauteuil » : si l’historique d’une donnée me dit qu’elle vient du terrain, c’est toujours le terrain qui a raison. Je n’hésite pas laisser à d’autres une tâche qui est hors de mes compétences : savoir céder sa place à quelqu’un qui fera mieux que vous est aussi une compétence en validation.

Il m’arrive pourtant de faire des écarts aux consignes : si je suis capable de reconnaître des bâtis, je peux aussi reconnaître piscine, château d’eau, lieu de culte, héliport, antenne, éolienne, moulin, cimétière, poteau à haute tension.... Saurez-vous trouver quelques-uns de ces trésors sur les imageries ci-dessous ?

![Héliport, antenne radio, cimetière, mosquée, antenne télévision, église. Il faut toujours regarder les descriptions d'images](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/09_galerie_objets_remarquables.webp){: .img-center loading=lazy }

En faisant le choix de les faire apparaître sur la carte, ma traduction de l’image fait passer de subtils messages : une forte concentration de piscines avec des bâtiments aux formes originales, c’est un complexe touristique. Un « [art de remarquer](https://fr.wikipedia.org/wiki/Anna_Tsing) » qui ne m’empêche pas, en cas de doute, d’ajouter un « [fixme](https://wiki.openstreetmap.org/wiki/FR:Key:fixme) », code qui signale au terrain qu’il doit faire attention avec cette donnée. Sur un projet multi-acteurs, acteurs sous pseudos que l’on ne rencontrera souvent jamais, la communication et l’échange restent une des clés du travail de la validation. Des astuces techniques que n'ont pas encore les personnes qui débutent.

----

## Parlons outil : JOSM, le secret d’une bonne validation

![logo JOSM](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/josm.png){: .img-thumbnail-left }

Très vite, un logiciel est indispensable pour valider : [JOSM](https://josm.openstreetmap.de/). La marche est haute pour le configurer, mais une fois adopté, on ne peut plus se passer de la qualité de son travail. Tout ce qui a été décrit plus haut tient beaucoup de la logique ; JOSM joue un rôle de fidèle assistant. Il détecte un nombre incalculable d'incohérences qu’il pointe automatiquement. Par exemple la classique intersection de cours d’eau et de route, un peu technique : c’est donc moi qui construis les ponts et creuse les tunnels.

![Image aérienne d'un petit village](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/10_JOSM_zone_residentielle.webp){: .img-center loading=lazy }

> JOSM permet de créer automatiquement une zone résidentielle ajustée autour des bâtiments.

JOSM me permet de déplacer toutes les contributions d’une personne qui s’est trompée d’imagerie sans toucher à celles d’une autre. Il m’offre la possibilité de remonter l’historique d’un objet pour lequel je soupçonne une erreur et de la corriger (parfois très loin du carré que je valide).

Il faut s’imaginer mes doigts volant entre [raccourcis claviers](https://josm.openstreetmap.de/wiki/Fr:Shortcuts) et naviguant dans les subtilités des tags que l’on finit par connaître par cœur. Une bonne validation c’est donc maîtriser ces outils qui, en plus de la qualité gagnée, économisent un temps précieux dans une mission urgente de HOT.

----

## Les impensés de la qualité d'une image aérienne

Le travail de validation repose en grande partie sur ma capacité à analyser une imagerie pour la traduire sous forme de carte. Or, les missions proposées sont à tous les coins de la planète ! Au début d’un projet, je prends donc le temps d’entraîner mon œil. Je commence par les bords du projet, plus petits et souvent avec moins de cartographie à réaliser (parfois j'ai des surprises !).

Une imagerie précise me permet moins d'hésitations et d’avoir des détails qui permettent de lever les doutes. Les défauts, comme les reflets des toits métalliques, y sont moins étendus. Le fait de ne pas avoir de nuages ou de fumées, c’est éviter les « blancs des cartes ». Et avoir d’autres images à ma disposition, c'est l’opportunité de pouvoir les consulter pour lever un doute ou pour compléter le puzzle… En espérant que le décalage d’imagerie, un calvaire, n’impacte pas la zone.

![A l'est, village cartographié. A l'ouest, rien de nouveau en raison de nuages : la carte est vide](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/11_carto_impossible_nuages.webp){: .img-center loading=lazy }

> Les nuages sur la partie ouest de l'image ont rendu impossible la fin de la cartographie.

La beauté des images est rarement abordée. Pourtant, le premier contact est à chaque fois une surprise : va-t-on avoir l’émeraude de la végétation sub-tropicale ? Le blanc de la neige du Népal qui drape le paysage ? Des champs qui crééent un tableau de Mondrian ? Le désert désolé aux petites habitations blotties les unes aux autres ? Tout un dégradé de bleus, signature de lacs glaciaires ? Une belle imagerie favorise l’exploration et trompe la monotonie.

![Dégradé de bleus sur lacs qui devraient être sévérement punis pour être aussi grandioses](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/12_lacs_glaciaires.webp){: .img-center loading=lazy }

> La somptueuse beauté de trois lacs glaciaires qui laissent deviner par la palette de leurs couleurs des compositions physico-chimiques différentes.

![Image aériennes dans des nuances marrons](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/13_coups_de_pinceaux.webp){: .img-center loading=lazy }

> D'étranges coups de pinceaux régulièrement confondus avec des maisons #TeamChocolat.

![100m de nuances de bleus : un lac glaciaire](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/14_lac_miroir.webp){: .img-center loading=lazy }

> Moment de poésie et de mise en abyme : un lac où semble se refléter le ciel.

![Trainées rouges sur une montagne ferrugineuse](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/15_Perou_couleurs_montagne_boule_bain_Lush.webp){: .img-center loading=lazy }

> Qui a laissé tomber une boule de bain Lush sur cette montagne au Pérou ?

![Glacier au nord, lac au sud entouré du gris des pierres](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/16_lac_glaciaire_wip.webp){: .img-center loading=lazy }

> Une merveille de géomophologie : un lac glaciaire en cours de séparation de son glacier, avec les traces du poids de ce dernier dans le paysage, son abrasion de la roche et les lésions qu'il laisse sur la pierre.

----

## Valider : une question de personnes

![logo cartONG](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/cartONG.webp){: .img-thumbnail-left }

Si je suis validatrice aujourd’hui, c’est que j’ai été formée il y a cinq ans par l’association de cartographie humanitaire [CartONG](https://www.cartong.org/fr) (merci Violaine, Jean-Yves, Jean-Paul et Michel !). Faire partie d’un groupe de validation permet de poser des questions de manière conviviale, de [découvrir des ouvrages](https://presses-universitaires.univ-amu.fr/signatures-sahariennes) pour nous aider dans notre lecture des images, de demander des avis sur une donnée et de partager ses devinettes, sa chasse aux trésors et son enquête généalogique de [POI](https://wiki.openstreetmap.org/wiki/FR:Points_d%27int%C3%A9r%C3%AAt).

![Défaut d'imagerie sur un lac en saison humide et sèche](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/17_lac_Ihotry_double_face.webp){: .img-center loading=lazy }

> Le lac Ihotry, vous l'aimez comment ? Vide ou plein ? Les deux ? OK ! *(ce qui amène à préciser l'intermittence)*

CartONG propose aussi des retours du terrain, avec des personnes qui viennent parler de leur utilisation des données. Ce partage enrichit ma pratique.

![Vue d'un camp de réfugié avec une zone de forêt bien délimitée. Un peu de verdure ne fait pas de mal](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/18_foret_solitaire.webp){: .img-center loading=lazy }

> Depuis que l'on m'a indiqué que certains éléments sont un point de repère sur les cartes, comme les forêts solitaires, elles sont ajoutées.

Toutes les personnes qui valident ajoutent-elles ce que j'appelle des « éléments bonus » ? Rien ne les y oblige, même si cela améliore grandement la richesse des données.

## Pour conclure

La validation sur HOT OSM est exhaustive : grâce au nombre de personnes mobilisé, chaque carré cartographié est validé un à un. Toutefois il m'est arrivé de regarder les contributions d'un maximum de personnes différentes. L'objectif : invalider les carrés des personnes faisant trop d'erreurs et ainsi redonner rapidement à ces carrés maltraités le statut de « à cartographier ».

Si cet article parle beaucoup des erreurs et du fouillis que je dois démêler, il arrive aussi que l’ouverture d’un carré provoque un ravissement devant la qualité du minutieux travail réalisé. On notera dans les exemples combien, derrière des règles simples, plusieurs analyses, et donc plusieurs cartographies, plusieurs validations sont possibles.

![Erreur de jonction entre hiver et été sur une image aérienne](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/19_fractale_saisonniere.webp){: .img-center loading=lazy }

> Si vous ne savez pas ce qu'est une fractale, en voici un bel exemple. Avec la fée des saisons à l'œuvre. Ou [Perséphone](https://www.webtoons.com/fr/romance/lore-olympus/episode-1/viewer?title_no=1825&episode_no=1), au choix.

Quant aux statistiques elles sont formelles : on passe beaucoup moins de temps à valider qu’à cartographier. Nous sommes parfaitement complémentaires pour obtenir notre résultat : [une carte de qualité](https://hal.science/hal-02157229) destinée aux personnes sur le terrain et [aux multiples utilisations](https://www.openstreetmap.org/user/pedrito1414/diary/401009). Vous vous joignez au mouvement ?

[Rejoindre l'aventure pour cartographier :map:](https://tasks.hotosm.org/explore){: .md-button }
{: align=middle }

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
