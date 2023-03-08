---
title: "Qualité des données : un voyage sur la plateforme humanitaire d'OpenStreetMap"
authors:
    - Delphine Montagne
categories:
    - article
date: "2023-03-24 18:20"
description: "Article revenant sur la validation des données de mapathon"
image: "Image d'illustration de l'article qui sert ensuite dans la mise en avant : réseaux sociaux, flux RSS..."
license: default
robots: index, follow
tags:
    - OpenStreetMap
    - JOSM
    - HOT OSM
---

# Qualité des données : un voyage sur la plateforme humanitaire d'OpenStreetMap 

:calendar: Date de publication initiale : 24 février 2023

## Introduction

Le 6 février 2023, la Turquie et la Syrie ont été touchées par [l’un des plus importants tremblements de terre de la région](https://fr.wikipedia.org/wiki/S%C3%A9ismes_de_2023_en_Turquie_et_Syrie). À la radio, à la télévision, sur les réseaux sociaux s’égrène le nombre de victimes et le coût des dégâts, des chiffres froids pour tenter d’exprimer l’ampleur de la catastrophe. 

Pour moi, c’est le signal que [HOT](https://tasks.hotosm.org/explore), la plateforme humanitaire d’OpenStreetMap, va bientôt déclencher une mission urgente et que mon aide sera nécessaire.


## La force du crowdsourcing cartographique

Car très vite en effet, la plateforme propose différents projets afin de cartographier, grâce aux images aériennes, une zone découpée en petits carrés.

![Début de validation d'une zone avec des carrés plus ou moins carrés](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/hot_qualite_contributions/00_hot_grille_travail.webp)

> Plus ou moins carrés : en bleu cartographié, cadenas pour le travail en cours, en vert validé, en gris mauvaise imagerie

Des bénévoles de tous niveaux choisissent une tâche qu’ils et elles complètent en ajoutant les informations sur OpenStreetMap. Quand tous les carrés sont terminés, la zone est cartographiée, et les données open source produites serviront immédiatement aux différentes équipes sur place. Une partition parfaitement maîtrisée depuis le [séisme d’Haïti de 2010](https://fr.wikipedia.org/wiki/S%C3%A9isme_de_2010_en_Ha%C3%AFti), jouée de jour comme de nuit grâce à un relais entre les différents fuseaux horaires : [OpenStreetMap ne dort jamais](https://live.openstreetmap.fr/).

Mais comment s’assurer que ces multiples contributions de personnes de niveaux et d’expériences différentes permettront d’obtenir des données homogènes à utiliser sur place, sans oubli ou erreur ? C’est là qu’intervient l’équipe de validation, dont je fais partie.

![Ma validation : feu vert pour le terrain](https://pad.oslandia.net/uploads/28ab878d-a2da-413d-94dc-9c7104fdc27a.png)



## Valider les données : une relecture par des pairs

Selon la logique que plusieurs regards sont complémentaires, mon travail de validatrice commence par la vérification des consignes du projet. Le plus souvent, il est demandé de cartographier des bâtiments, complété généralement par le réseau routier, parfois les cours d’eau, plus rarement l’occupation du sol. 

### Faire habiter la carte : la validation des bâtiments
En premier, je regarde les oublis. Toutes les maisons ont-elles été cartographiées ? Si en zone rurale l’opération ressemble à une chasse aux trésors, au contraire en zone urbaine un bâtiment peut en cacher un autre. Sont-elles bien dessinées une par une ? Avec la bonne forme ? La norme étant le carré, le rectangle et le rond, tout ce qui en dévie doit être vérifié. 

![Carte avec un fouillis de bâtiments mal dessinés](https://pad.oslandia.net/uploads/6731fdcb-517c-4122-a94f-f54b6feaf7c9.png)
> Exemple de cartographie à reprendre : chaque maison doit être tracée une par une et non en groupe, notez les problèmes de formes et à ~~droite~~ l'est un bâtiment dans un bâtiment.

Je traque les superpositions de bâtiments et je devine où se termine un toit dissimulé par un arbre. Je tourne, je redimensionne et je déplace les bâtiments pour les ajuster à l'image. Mais il y a des pièges ! Attention à ne pas confondre un carré de terre, une voiture, un arbre ou des murs avec une maison. Même l’intelligence artificielle, mobilisée sur certains projets, s’y trompe. 

![Image aérienne d'une double entreprise de construction : la zone industrielle qui fait de la construction et la carte en cours](https://pad.oslandia.net/uploads/8474d35e-369c-4643-8366-c3c427a3e87b.png)
> Cartographie de voitures et de matériaux entreposés, corrigée par la validation.

Pour m’aider, je regarde les ombres, je mesure la taille des objets, je compare au reste de la zone et pour statuer je suis attentive aux détails que laisse voir l’imagerie. Surtout, je passe mon temps à zoomer et dézoomer sur la zone.
![Avant/après la validation](https://pad.oslandia.net/uploads/2a72becf-946e-4b86-bac6-2964691c4650.png)
> Validation : bâtiments tracés un par un, correction des formes, ajustement de la zone résidentielle, correction d'une hélisurface.

### Faire se déplacer les personnes : valider les routes

Zoomer et dézoomer, c’est une opération continuelle en validant les routes. Plus que leur existence, la validation cherche à savoir si elles sont nécessaires. Les informations doivent permettre aux personnes de se déplacer sur place et de se représenter les lieux. Je réunis des petits bouts de routes pour en faire une seule, je coupe et je recolle les routes pour gagner en cohérence. J’enlève des nœuds qui ne sont pas nécessaire, surtout quand le reste de la zone cartographiée n'est pas aussi précis, et j’adoucie la courbe de virages par des ajouts là où il y a des manques. Nul besoin d’avoir des données inutilement volumineuses !

![« Qu’est-ce que c’est que ce bazar ? », leitmotiv de la validation](https://pad.oslandia.net/uploads/12986d87-61bf-433f-aff0-1755919092de.png)
> Route en rouge non reliée, morceaux de routes non harmonisés au sud, triangle de route d'une précision inutile au croisement et route à poursuivre à l'est

Cartographier des routes, c’est penser réseau : une route mène forcément quelque part. Sinon, il faut se poser la question de son utilité. Son tracé peut se trouver caché par des forêts, du sable, une zone d’ombre, un nuage, être effacé et reprendre plus loin… Quand cela ne conduit pas à s’apercevoir quelques mètres après que c’est une rivière intermittente. 

![Imaga aérienne et une route étrange...](https://pad.oslandia.net/uploads/9732955c-86fc-472a-8789-edf4c7b4376f.png)
> A l'ouest, la couleur verte montre une zone humide. La zone étudiée pouvait faire penser à une route, à une autre échelle les méandres sont typiques d'un cours d'eau.

J’ajoute des points d’intersection entre deux lignes (la topologie, une passion) et je connecte des routes qui paraissent si proches que l’on a oublié de les relier. En fonction des consignes, je vérifie qu’elles sont de la bonne catégorie, c’est rarement le cas des routes résidentielles. J’harmonise, je complète, je répare, j’ajuste : tout pour rendre une appli de routing heureuse !

![Voîture blanche sur une route vue d'une image aérienne. Le tracé de la cartographie semble courir derrière le véhicule](https://pad.oslandia.net/uploads/a4dda94b-e94d-4a69-b350-976c2c365382.png)
> Parfois, trouver une route, ainsi que sa classification en route pratiquable pour un véhicule, est simple.

La gestion d’un réseau est une opération tellement minutieuse que dans les zones avec beaucoup de travail, je m’occupe d’abord uniquement des bâtiments, ensuite des routes et enfin des deux. Mon objectif est de me mettre mentalement dans la tête des personnes qui auront besoin des données. Car paradoxalement, la qualité est invisible, ce sont les erreurs qui font en prendre conscience.

## Valider : une opération de décentrement
Généralement, la cartographie agit « égoïstement » sur son carré bien délimité. Lorsque l’on valide, il faut réfléchir à l’échelle des carrés voisins, voire à l’échelle de tout le projet. On apprend très vite les classiques effets de bords : une maison pile entre deux carrés, tout le monde pense que c’est à l’autre de s’en occuper, et le bâtiment n’est pas cartographié du tout (pensez à sa solitude et son sentiment d’abandon).

![Suite de lacs noirs au milieu d'une zone de cailloux formant un visage de souffrance, hurlant en silence](https://pad.oslandia.net/uploads/06253002-977d-439a-9cdb-6fefac22f57f.png)
> Comment survivre à une zone mal cartographiée ? En trouvant une imagerie qui pleure encore plus que soi.

J’ai toujours en tête les différentes pratiques sur place et l’utilisation des données. Il faut rester humble : je fais de la cartographie dite « de fauteuil » : si l’historique d’une donnée me dit qu’elle vient du terrain, c’est toujours le terrain qui a raison. Je n’hésite pas laisser à d’autres une tâche qui est hors de mes compétences : savoir céder sa place à quelqu’un qui fera mieux que vous est aussi une compétence en validation.

Il m’arrive pourtant de faire des écarts aux consignes : si je suis capable de reconnaître des bâtis, je peux aussi reconnaître piscine, château d’eau, lieu de culte, héliport, antenne, éolienne, moulin, cimétière, poteau à haute tension.... Saurez-vous trouver quelques-uns de ces trésors sur les imageries ci-dessous ?

![Héliport, antenne radio, cimetière, mosquée, antenne télévision, église. Il faut toujours regarder les descriptions d'images](https://pad.oslandia.net/uploads/64a519a1-2606-4a23-b162-dba30c186515.png)


En faisant le choix de les faire apparaître sur la carte, ma traduction de l’image fait passer de subtils messages : une forte concentration de piscines avec des bâtiments aux formes originales, c’est un complexe touristique. Un « [art de remarquer](https://fr.wikipedia.org/wiki/Anna_Tsing) » qui ne m’empêche pas, en cas de doute, d’ajouter un « [fixme](https://wiki.openstreetmap.org/wiki/FR:Key:fixme) », code qui signale au terrain qu’il doit faire attention avec cette donnée. Sur un projet multi-acteurs, acteurs sous pseudos que l’on ne rencontrera souvent jamais, la communication et l’échange restent une des clés du travail de la validation. Des astuces techniques que n'ont pas encore les personnes qui débutent.

## Parlons outil : JOSM, le secret d’une bonne validation

Très vite, un logiciel est indispensable pour valider : [JOSM](https://josm.openstreetmap.de/). La marche est haute pour le configurer, mais une fois adopté, on ne peut plus se passer de la qualité de son travail. Tout ce qui a été décrit plus haut tient beaucoup de la logique ; JOSM joue un rôle de fidèle assistant. Il détecte un nombre incalculable d'erreurs illogiques qu’il pointe automatiquement. Par exemple la classique intersection de cours d’eau et de route, un peu technique : c’est donc moi qui construis les ponts et creuse les tunnels. 

![Image aérienne d'un petit village](https://pad.oslandia.net/uploads/45e027c3-1ca3-4822-b1f7-9e39f58d9950.png)
> JOSM permet de créer automatiquement une zone résidentielle ajustée autour des bâtiments.

JOSM me permet de déplacer toutes les contributions d’une personne qui s’est trompée d’imagerie sans toucher à celles d’une autre. Il m’offre la possibilité remonter l’historique d’un objet pour lequel je soupçonne une erreur et de la corriger (parfois très loin du carré que je valide).

Il faut s’imaginer mes doigts volant entre [raccourcis claviers](https://josm.openstreetmap.de/wiki/Fr:Shortcuts) et naviguant dans les subtilités des tags que l’on finit par connaître par cœur. Une bonne validation c’est donc maîtriser ces outils qui, en plus de la qualité gagnée, économisent un temps précieux dans une mission urgente de HOT.

## Les impensés de la qualité d'une image aérienne

Le travail de validation repose en grande partie sur ma capacité à analyser une imagerie pour la traduire sous forme de carte. Or, les missions proposées sont à tous les coins de la planète ! Au début d’un projet, je prends donc le temps d’entraîner mon œil. Je commence par les bords du projet, plus petits et souvent avec moins de cartographie à réaliser (parfois j'ai des surprises !). 

Une imagerie précise me permet moins d'hésitations et d’avoir des détails capables de lever les doutes. Les défauts, comme les reflets des toits métalliques, y sont moins étendus. Le fait de ne pas avoir de nuages ou de fumées, c’est éviter les « blancs des cartes ». Et avoir d’autres images à ma disposition, c'est l’opportunité de pouvoir les consulter pour lever un doute ou pour compléter le puzzle… En espérant que le décalage d’imagerie, un calvaire, n’impacte pas la zone.

![A l'est, village cartographié. A l'ouest, rien de nouveau en raison de nuages : la carte est vide](https://pad.oslandia.net/uploads/2da14f2b-56e4-4cce-b25f-7fbef8af70cf.png)
> Les nuages sur la partie ouest de l'image ont rendu impossible la fin de la cartographie.

La beauté des images est rarement abordée. Pourtant, le premier contact est à chaque fois une surprise : va-t-on avoir l’émeraude de la végétation sub-tropicale ? Le blanc de la neige du Népal qui drape le paysage ? Des champs qui crééent un tableau de Mondrian ? Le désert désolé aux petites habitations blotties les unes aux autres ? Tout un dégradé de bleus, signature de lacs glaciaires ? Une belle imagerie favorise l’exploration et trompe la monotonie.

![Dégradé de bleus sur lacs qui devraient être sévérement punis pour être aussi grandioses](https://pad.oslandia.net/uploads/8b46e62f-3174-4836-92a6-2a55e1dd5495.png)
> La somptueuse beauté de trois lacs glaciaires qui laissent deviner par la palette de leurs couleurs des compositions physico-chimiques différentes.

![Image aériennes dans des nuances marrons](https://pad.oslandia.net/uploads/4a42d88a-dfdc-455c-9a7e-892b4e2f2bcb.png)
> D'étranges coups de pinceaux régulièrement confondus avec des maisons #TeamChocolat.

![100m de nuances de bleus : un lac glaciaire](https://pad.oslandia.net/uploads/d8490e4a-2b3d-4472-8bf7-3c0c31421005.png)
> Moment de poésie et de mise en abyme : un lac où semble se refléter le ciel.

![Trainées rouges sur une montagne ferrugineuse](https://pad.oslandia.net/uploads/61ac5d55-6bca-4b5e-950e-57ee932c4c4f.png)
> Qui a laissé tomber une boule de bain Lush sur cette montagne au Pérou ?

![Glacier au nord, lac au sud entouré du gris des pierres](https://pad.oslandia.net/uploads/1560508d-eabf-4d36-9ccf-b7275bb97b02.png)
> Une merveille de géomophologie : un lac glaciaire en cours de séparation de son glacier, avec les traces du poids de ce dernier dans le paysage, son abrasion de la roche et les lésions qu'il laisse sur la pierre.



## Valider : une question de personnes

Si je suis validatrice aujourd’hui, c’est que j’ai été formée il y a cinq ans par l’association de cartographie humanitaire [CartONG](https://www.cartong.org/fr) (merci Violaine, Jean-Yves, Jean-Paul et Michel !). Faire partie d’un groupe de validation permet de poser des questions de manière conviviale, de [découvrir des ouvrages](https://presses-universitaires.univ-amu.fr/signatures-sahariennes) pour nous aider dans notre lecture des images, de demander des avis sur une donnée et de partager ses devinettes, sa chasse aux trésors et son enquête généalogique de [POI](https://wiki.openstreetmap.org/wiki/FR:Points_d%27int%C3%A9r%C3%AAt). 

![Défaut d'imagerie sur un lac en saison humide et sèche](https://pad.oslandia.net/uploads/94a85b78-f67c-4539-a7b1-39e0792749bc.png)
> Le lac Ihotry, vous l'aimez comment ? Vide ou plein ? Les deux ? OK ! *(ce qui amène à préciser l'intermittence)*

CartONG propose aussi des retours du terrain, avec des personnes qui viennent parler de leur utilisation des données. Ce partage enrichit ma pratique.

![Vue d'un camp de réfugié avec une zone de forêt bien délimitée. Un peu de verdure ne fait pas de mal](https://pad.oslandia.net/uploads/93bfe44c-4c93-40e3-965c-00971a9d8ede.png)
> Depuis que l'on m'a indiqué que certains éléments sont un point de repère sur les cartes, comme les forêts solitaires, elles sont ajoutées.

Toutes les personnes qui valident ajoutent-elles ce que j'appelle des « éléments bonus » ? Rien ne les y oblige, même si cela améliore grandement la qualité des données.

## Pour conclure

Si cet article parle beaucoup des erreurs et du fouillis que je dois démêler, il arrive aussi que l’ouverture d’un carré provoque un ravissement devant la qualité du minutieux travail réalisé. On notera dans les exemples combien, derrière des règles simpes, plusieurs analyses, et donc plusieurs cartographies, plusieurs validations sont possibles. 

![Erreur de jonction entre hiver et été sur une image aérienne](https://pad.oslandia.net/uploads/5884072d-f60f-4201-9a28-5d1a3b30326a.png)
> Si vous ne savez pas ce qu'est une fractale, en voici un bel exemple. Avec la fée des saisons à l'œuvre. Ou [Perséphone](https://www.webtoons.com/fr/romance/lore-olympus/episode-1/viewer?title_no=1825&episode_no=1), au choix.

Quant aux statistiques elles sont formelles : on passe beaucoup moins de temps à valider qu’à cartographier. Nous sommes donc parfaitement complémentaires pour obtenir notre résultat : [une carte de qualité](https://hal.science/hal-02157229) destinée aux personnes sur le terrain.




----

## Auteur {: data-search-exclude }

--8<-- "content/team/dmon.md"

{% include "licenses/default.md" %}
