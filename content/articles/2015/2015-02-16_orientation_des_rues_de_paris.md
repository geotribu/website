---
title: "'Ce que l'orientation des rues de Paris (...)' : les dessous d'une carte"
authors:
    - Mathieu RAJERISON
categories:
    - article
comments: true
date: 2015-02-16
description: "Making-of la carte publiée dans Slate : 'Ce que l'orientation des rues de Paris nous dit de son histoire'"
tags:
    - cartographie
    - histoire
    - Paris
    - QGIS
    - R
---

# 'Ce que l&apos;orientation des rues de Paris (...)' : les dessous d'une carte

:calendar: Date de publication initiale : 16 février 2015

[![Article Slate](https://cdn.geotribu.fr/img/articles-blog-rdp/story/slipslate.png "Article Slate"){: .img-center loading=lazy }](http://www.slate.fr/story/96387/orientation-rues-paris-histoire)

Ce billet est un peu un making-of. J'y raconte la genèse d'une [carte](https://www.flickr.com/photos/10519370@N04/15654896891/) sur l'orientation des rues de Paris et de [l'article](http://www.slate.fr/story/96387/orientation-rues-paris-histoire) qui y est associé.

----

## Datapointed

[![Datapointed](https://cdn.geotribu.fr/img/articles-blog-rdp/story/crayon%20the%20grids.PNG "Datapointed"){: .img-center loading=lazy }](http://www.datapointed.net/2014/10/maps-of-street-grids-by-orientation/)

C'était le 14 Octobre de l'année dernière. Un informaticien américain du nom de Stephen Von Worley diffuse sur le web une série de cartes où les rues sont classées par couleur selon leur orientation. Ce que j'ai apprécié dans sa démarche, c'est la façon dont il arrive à révéler une certaine beauté d'un magma a priori informe de spaghettis.

Sur son [billet](http://www.datapointed.net/2014/10/maps-of-street-grids-by-orientation/), l'auteur explique :

![Explication](https://cdn.geotribu.fr/img/articles-blog-rdp/story/explanation.PNG "Explication"){: .img-center loading=lazy }

S'il est vrai que j'apprécie que me soit livré le code, je trouve aussi stimulant de déterminer comment une carte a pu être fabriquée.

![Magie](https://cdn.geotribu.fr/img/articles-blog-rdp/story/magie.jpg "Magie"){: .img-center loading=lazy }

## Traduction

![Voronoï](https://cdn.geotribu.fr/img/articles-blog-rdp/story/voronoi.PNG "Voronoï"){: .img-center loading=lazy }

De ce que j'ai pu comprendre, Stephen Von Worley a disposé une grille de points sur l'étendue de ses mégalopoles. Pour chaque point, il a déterminé l'orientation des N segments les plus proches, l'ensemble devant comptabiliser 500 m. Enfin, il a pondéré, pour chaque point, la valeur d'angle assignée à chaque segment par la longueur de ces derniers.

Le résultat donne un aspect mosaïque/vitraux semblable à ce qu'on obtient après [voronoïsation](https://fr.wikipedia.org/wiki/Diagramme_de_Vorono%C3%AF), à l'exception que dans le cas présent, les couleurs semblaient avoir été lissées.

Quelque chose d'intrigant avait trait à la couleur des lignes qui était graduelle alors qu'en général, nos outils colorient les segments avec une teinte unique. Je découvris après quelques essais qu'un tel résultat pouvait être obtenu en couplant un raster et une couche de lignes tout en utilisant le mode de fusion "revêtement" sachant que [QGIS](http://www2.qgis.org/fr/site/) en est doté depuis la version 2.

## Fabrication

![Utilisation de R et QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/story/ninja.jpg "Utilisation de R et QGIS"){: .img-center loading=lazy }

La façon dont j'ai conçu ma carte est beaucoup plus simple. J'ai retenu les milieux de tronçons, auxquels j'ai passé directement une fonction d'[interpolation](https://fr.wikipedia.org/wiki/Interpolation_spatiale). Le raster obtenu a été lissé. Niveau outils, je choisis [R](http://cran.r-project.org/web/views/Spatial.html), ma boîte à outils spatiale préférée, bien que python eusse été aussi un choix pertinent. J'ai effectué le rendu sous QGIS.

## Choix

![Premier rendu](https://cdn.geotribu.fr/img/articles-blog-rdp/story/cartepremiere.PNG "Premier rendu"){: .img-center loading=lazy }

Afin de mimer la carte de datapointed, j'appliquai des rampes de couleur avec beaucoup de teintes. Le résultat avait un côté Comics US comme on le voit au-dessus.

Un choix limité à deux teintes me parut plus pertinent car il facilitait la lecture. Là aussi, je testai plusieurs couples de couleurs.

Rouge et bleu ? Cela fait trop élections..Vert et Jaune ? Trop alien et geek.

![Cercle chromatique](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2015/10686817_10152617685222815_6967472526011265745_n.jpg "Cercle chromatique"){: .img-center loading=lazy }

Je sélectionnai les couleurs jaune orangé ainsi que magenta. Jaune car celle-ci donne un aspect lumineux à la carte qui rappelle la ville vue de l'espace. Magenta car c'est une couleur vive qu'on associe rarement à un élément de terrain ou une thématique. Le violet est en outre presque à l'opposé du jaune sur le cercle chromatique.

[![Rendu lumineux](https://cdn.geotribu.fr/img/articles-blog-rdp/story/streets%20of%20paris.jpg "Rendu lumineux"){: .img-center loading=lazy }](https://www.flickr.com/photos/10519370@N04/15654896891/)

L'image obtenue était finalement beaucoup plus simple que celle de datapointed.

Pour la légende, j'aurais pu choisir une forme conventionnelle mais il me semblait qu'un quart de cercle trigonométrique parvenait à résumer le mode de lecture de la carte.

![Légende](https://cdn.geotribu.fr/img/articles-blog-rdp/story/l%C3%A9gendes.PNG "Légende"){: .img-center loading=lazy }

La carte est volontairement épurée, presque énigmatique. Ainsi, les lecteurs pourraient s'interroger et trouver par eux-mêmes certaines réponses.

Je publiai [la méthode ainsi que le code](http://datagistips.blogspot.fr/2014/11/streets-of-paris-colored-by-orientation.html) sur mon blog le 15 Novembre.

## Diffusion

![Coquillage](https://cdn.geotribu.fr/img/articles-blog-rdp/story/coquillage.jpg "Coquillage"){: .img-center loading=lazy }

Je percevais l'intérêt qu'une telle carte pouvait présenter pour un urbaniste ou un historien féru de l'histoire de Paris mais l'absence de narration en faisait en quelque sorte une jolie coquille vide.

![Narration](https://cdn.geotribu.fr/img/articles-blog-rdp/story/diffusion.jpg "Narration"){: .img-center loading=lazy }

J'espérais qu'en la diffusant sur twitter, elle rebondisse au fil des retweets jusqu'à atterrir dans les mains d'un specialiste.

Finalement, le 18 Novembre, c'est la revue Slate qui m'a contacté en me demandant de réaliser un article.

![Contact Slate](https://cdn.geotribu.fr/img/articles-blog-rdp/story/datapointed.PNG "Contact Slate"){: .img-center loading=lazy }

Pour appuyer sa requête, elle citait datapointed : "Lots of stories in there: of cities waxed, towns waned, territory absorbed, and terrain negotiated", ce qui veut dire *"Pas mal d'histoires là-dedans : de villes rénovées, de terrains absorbés, de parcelles négociées [...]"*.

## Recherche

La demande de Slate m'a motivé à réaliser un travail d'investigation que je ne m'étais pas accordé le temps de faire. Faire émerger les épisodes du développement de la Cité grâce à au graphisme de ses rues me paraissait une idée séduisante.

![Paris - Skate](https://cdn.geotribu.fr/img/articles-blog-rdp/story/skate.jpg "Paris - Skate"){: .img-center loading=lazy }

Etudiant, j'en avais seulement apprécié les courbes lors de virées nocturnes en skate. J'ignorais alors ce que ces rues pouvaient dessiner vues de haut et aujourd'hui, je n'habite plus Paris. C'était un drôle de petit défi.

## Rédaction

Un coup de fil passé à une amie urbaniste me mit sur la piste. Elle m'évoqua les travaux initiés par [Georges Eugène Hausmann](https://fr.wikipedia.org/wiki/Georges_Eug%C3%A8ne_Haussmann). La Toile fut par la suite une alliée précieuse.

![Pérégrination](https://cdn.geotribu.fr/img/articles-blog-rdp/story/p%C3%A9r%C3%A9grination.jpg "Pérégrination"){: .img-center loading=lazy }

Dans un premier temps, j'ai repéré des zones où différentes couleurs se conjuguaient de façon atypique. Au fil de mes pérégrinations sur la Toile, pendant lesquelles je parcourais simultanément l'espace de ma carte, j'ai pu rassembler assez d'éléments pour donner du sens, finalement, à cette carte.

J'ai pu compter sur [des sites de passionnés](http://paris-atlas-historique.fr/), sur Wikipedia, sur Géoportail, Google Street View. Afficher de la donnée Openstreetmap dans Géoportail peut paraître paradoxal, mais cela m'a permis d'accéder à des cartes historiques datant de 1820 ainsi que de 1906 auxquelles je pus superposer le réseau de voies actuel.

L'articulation de mon article s'appuie, non pas sur un ordre chronologique, mais sur des graphismes distincts sur la carte. J'ai réduit mon nombre d'observation à 10.

![Observation](https://cdn.geotribu.fr/img/articles-blog-rdp/story/zoom_0.jpg "Observation"){: .img-center loading=lazy }

Dans un premier temps, mon article invite à contempler la carte de loin, pour ensuite affiner l'observation sur des amas de voies (groupes de rues de même couleurs) et des discontinuités (percées hausmaniennes, îlots de couleur différente).

J'assemblais toutes mes observations au fur et à mesure dans un document Google Docs. C'est ce dernier que je soumis à Slate le 17 Décembre.

## Echanges avec Slate

Slate trouvera certains termes étaient trop cryptiques. "Concentricité" fera place à "convergence", "disruption" à "singularités".

Ses critiques m'ont aussi permis d'améliorer le paragraphe où l'on explique comment lire la carte.

Enfin, c'est Slate qui me suggérera le nom de l'article : "Ce que l'orientation des rues de Paris nous dit de son histoire".

## Retours

Le 19 Janvier, Slate m'annonce que l'article est publié et qu'il a beaucoup de retours positifs sur les réseaux sociaux, ce qui me laisse plutôt surpris et déconcerté.

L'article est relayé au sein de différents médias : généralistes comme les [Inrocks](http://www.lesinrocks.com/2015/01/buzzodrome/ce-que-lorientation-des-rues-de-paris-nous-dit-de-son-histoire/), [Télérama](http://www.telerama.fr/medias/a-voir-ce-que-l-orientation-des-rues-de-paris-nous-dit-de-son-histoire,121970.php) et [Mediapart](http://www.mediapart.fr/journal/france/200115/ce-que-lorientation-des-rues-de-paris-nous-dit-de-son-histoire), plus spécialisés comme le blog de [revolutionanalytics](http://blog.revolutionanalytics.com/2015/02/pariss-history-captured-in-its-streets.html).

<iframe src="http://www.dailymotion.com/embed/video/x2fg3wf" frameborder="0" height="270" width="100%"></iframe>

Il m'a même valu d'être interviewé sur LCI pour la revue de presse hebdomadaire [la semaine de Slate](http://www.slate.fr/story/97209/semaine-slate-reader-lci-barack-obama-hololens-liliane-bettencourt) (vers 8 min). Lors de l'émission, j'ai trouvé amusant que les présentateurs s'étonnent du terme de géomaticien et découvrent de quoi il s'agit. J'ai trouvé sympa, aussi, qu'OSM prenne une part belle dans la chronique.

Sur Twitter, une personne avouera ne presque avoir rien compris à ma carte mais que ça fait un joli fonds d'écran. Mon amie dit qu'on pourrait y découvrir un mandala caché, comme un code secret inscrit dans l'écriture de ses rues.

<blockquote class="twitter-tweet" tw-align-center" data-dnt="true"><p lang="fr" dir="ltr"><a href="https://twitter.com/Slatefr?ref_src=twsrc%5Etfw">@Slatefr</a> <a href="https://twitter.com/datagistips?ref_src=twsrc%5Etfw">@datagistips</a> j&#39;ai presque rien compris. Mais en fond d&#39;écran c&#39;est trop joli. :) <a href="http://t.co/4hH3cdlPjr">pic.twitter.com/4hH3cdlPjr</a></p>&mdash; Jérôme (@MrZenein) <a href="https://twitter.com/MrZenein/status/557249720654249985?ref_src=twsrc%5Etfw">January 19, 2015</a></blockquote>

## Audience d'une carte

![Diagramme de Venn](https://cdn.geotribu.fr/img/articles-blog-rdp/story/sujet%20verbe%20complement.jpg "Diagramme de Venn"){: .img-center loading=lazy }

L'image ci-dessus est un [diagramme de Venn](https://fr.wikipedia.org/wiki/Diagrammes_d'Euler,_de_Venn_et_de_Carroll). Elle comporte les trois ingrédients qui déterminent, selon moi, l'audience d'une carte.

En dehors du média qui contribue à la diffuser, on la devrait à la conjugaison d'un esthétisme, d'un thème et de ce que j'appelle proximité, cette dernière pouvant être de trois ordres : temporelle (actualité), spatiale et affective.

Une carte des élections présidentielles ou de mobilisation sociale en France n'aura d'impact que durant la période où ces dernières se produisent (proximité temporelle). Même si les élections, disons au hasard au Montenegro, se passaient en ce moment, il se pourrait qu'elles ne vous intéressent pas (proximité spatiale) à moins que vous n'ayez des racines monténégrines plus ou moins lointaines (proximité affective).

Aussi, la représentation cartographique n'a pas forcément besoin d'être sophistiquée. Il existe des cartes d'un graphisme très sommaire qui touchent par le thème qu'elles abordent. Citons un exemple : [la carte des bises](http://combiendebises.free.fr/).

A l'opposé, des cartes fascinent par leur esthétique malgré le fort niveau d'abstraction des sujets qu'elles représentent. C'est le cas des cartes d'[Eric Fischer](http://www.fastcodesign.com/1664462/infographic-of-the-day-using-twitter-and-flickr-geotags-to-map-the-world) qui puisent dans les réseaux sociaux.

Enfin, la carte étant une matière à penser qui se suffit peu à elle-même, la narration qui en découle est importante. Sa faculté à nourrir l'imaginaire du lecteur déterminera l'intérêt qu'elle pourra susciter.

## I ♥ Openstreetmap

[Quelqu'un, sur twitter, a écrit : "OpenStreetMap, mon amour"](https://twitter.com/BenoitVicart/status/557640221886795779). C'est effectivement ça. L'article m'a permis d'illustrer les bienfaits du libre : des outils et des informations extrêmement riches, fruits de ses contributeurs et générateurs de belles histoires. Je souhaitais leur rendre hommage d'une certaine façon.

## Genèse d'un article

Voici comment, finalement, tout cela s'est déroulé :

![Genèse](https://cdn.geotribu.fr/img/articles-blog-rdp/story/diagramme.jpg "Genèse"){: .img-center loading=lazy }

La création du code permettant de générer la carte ne m'a pas pris en soi beaucoup de temps. C'est surtout la rédaction de l'article, étalée sur un mois, qui a été chronophage. Je me rappelle parcourir les pages de Wikipedia dans le bus, sur le chemin de mon travail, pour ensuite les relire à la maison. Je me rappelle certaines soirées d'hiver, occupé à compiler mes différentes observations dans un fichier texte. Le jeu en a valu la chandelle et ce fut une belle aventure.

## Plus loin

A noter que d'autres sources de données auraient très bien pu être exploitées : l'excellent projet [Alpage](http://alpage.huma-num.fr/fr/) d'analyse diachronique de l'espace urbain parisien qui ne m'est malheureusement pas revenu en mémoire lorsque j'ai commencé l'écriture de l'article.

[![Alpage](https://cdn.geotribu.fr/img/articles-blog-rdp/story/alpage_0.PNG "Alpage"){: .img-center loading=lazy }](http://alpage.huma-num.fr/fr/)

Après publication, un ancien professeur me demandait si j'avais utilisé des indicateurs d'isotropie afin de savoir si les rues suivaient une direction particulière dans l'espace.

![Nature](https://cdn.geotribu.fr/img/articles-blog-rdp/story/nature.PNG "Nature"){: .img-center loading=lazy }

Dans la revue [Nature](http://www.nature.com/srep/2013/130708/srep02153/full/srep02153.html), un article datant de 2013 révèle l'histoire de Paris au travers de ses rues en mobilisant, notamment, la théorie des réseaux/graphes. A lire.

Bien entendu, on aurait pu aller plus loin dans l'analyse spatiale du réseau mais dans ce cas, l'article aurait perdu ce côté un peu grand public.

## The end (ou plutôt le début ?)

Pour conclure, je dirais qu'il est rassurant que l'imaginaire de personnes puisse encore être nourri par des visions du territoire, à une époque où ses frontières se sont estompées dans les canaux du numérique.

Enfin, le retentissement inusuel de cet article montre que les cartes ont encore de beaux jours devant elles, tout comme ceux qui s'appliquent à les créer et s'échinent à en renouveler les formes : cartographes et géomaticiens.

## Sources

[NounProject](http://thenounproject.com/) est un projet fascinant qui vise à créer un langage visuel utilisable par tous. J'en ai tiré de multiples icônes pour le billet ici présent :

- La baguette par Dmitry Baranovskyi,
- l'oiseau qui ressemble à Twitter par Thomas Le Bas,
- le cerveau par Greg Pabst,
- l'éléphant par N.K.Narasimhan,
- l'éléphant normal par spotted paint,
- l'œil par Gareth Servant,
- la main avec des graines par Luis Prado,
- la Joconde par Cornelius Danger (mais initialement par Da Vinci),
- le lapin par Adam Mullin,
- le bonhomme avec un zizi par Patrick Trouvé,
- le ninja par John O'Shea,
- le carnet par Sarah Abraham,
- le peintre par Luis Prado,
- les cotillons par Tommy Lau,
- la perle par Aaron Dodson,
- le pigeon par Olivier Guin,
- le globe avec la loupe par hunotika,
- le coquillage par Matt Bortz,
- le skate par Paul J Miller,
- le slip par iconsmind.com,
- le sage à lunette par Luis Martins,
- la toile d'araignée par Ryan Mochal,
- la plume d'écrivain par Cédric Villain

Sinon, le cercle chromatique a été réalisé par [sylveno](https://fr.wikipedia.org/wiki/Cercle_chromatique#mediaviewer/File:CYM_color_wheel.png) et le portrait de cubisme est tiré d'i[ci](http://www.ec-renards-fontenay.ac-versailles.fr/spip.php?article408)  

----

<!-- geotribu:authors-block -->
