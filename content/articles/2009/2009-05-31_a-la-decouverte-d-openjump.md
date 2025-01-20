---
title: "A la découverte d'OpenJump"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-05-31
description: "A la découverte d'OpenJump"
tags:
    - Java
    - open source
    - OpenJump
    - SIG
---

# A la découverte d'OpenJump

:calendar: Date de publication initiale : 31 mai 2009

![logo OpenJump](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/openjump.png "logo OpenJump"){: .img-thumbnail-left }

Ce billet fait suite à la réflexion commencée lors de la présentation du logiciel [Puzzle-Gis](http://geotribu.net/node/117) dont le but est de découvrir et comparer l'offre de logiciel SIG Open Source disponible. Nous allons cette fois aborder Open Jump. A l'instar de [Skyjump](http://skyjumpgis.org/), [DeeJump](http://www.lat-lon.de/latlon/portal/media-type/html/user/anon/page/default.psml/js_pane/produkte%2Csub_produkte_deeJUMP) ou encore [OpenJUMP-The merge](http://www.projet-sigle.org/), OpenJump est né d'un fork de [Jump](http://www.jump-project.org/) qui était à l'origine développé par [vividsolutions](http://www.vividsolutions.com/). De [nombreuses autres distributions](http://openjump.org/wiki/show/OpenJUMPs+Family) sont également disponibles, attention néanmoins à vérifier qu'elles soient toujours en développement. Avant même de commencer la présentation, une question me vient à l'esprit : cet éparpillement des distributions, des ressources et contributions ne sont-elles pas préjudiciables à OpenJump? En effet, même si celui-ci est basé sur un maximum de modularité les versions et plugins ne sont pas toujours compatibles entre eux. De plus on se sent parfois un peu perdu ne sachant pas trop quelle distribution sera la plus adaptée. Néanmoins, laissons de côté ce détail et passons aux choses sérieuses.

## Téléchargement et installation

Première étape, le [téléchargement](http://sourceforge.net/project/showfiles.php?group_id=118054), sur la page en plus du logiciel lui-même de nombreux plugins sont disponibles ainsi qu'une [documentation](http://sourceforge.net/project/showfiles.php?group_id=118054&package_id=209987&release_id=598577) en français. Déjà un gros point positif. L'installation n'est pas compliquée, il suffit simplement de lancer l'"exécutable" d'OpenJump.

![OpenJUMP - Version](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/version.png "OpenJUMP - Version"){: .img-center loading=lazy }

## Découverte de l'interface

A première vue l'interface, bien qu'un peu moins soignée que Puzzle Gis, semble beaucoup plus riche en fonctionnalités. De plus, **tout est en français** ! Sélectionnons maintenant notre couche, malheureusement pour les vecteurs seuls les formats Shape et Gml sont disponibles. Néanmoins une fois le plugin [mifmid-driver](http://geo.michaelm.free.fr/spip.php?article10) téléchargé et installé vous pourrez comme son nom l'indique accéder aux données au format mif-mid (mais pas pour les .tab). Petit aparté pour souligner la simplicité d'installation des plugins. Il suffit en effet de les placer dans le répertoire "ext" de votre installation.  
Parenthèse faite revenons à notre interface qui est présentée ci-dessous dans laquelle j'ai affiché un fichier Shape (1.5 Mo - 209 objets) :

![OpenJUMP - Carte](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/carte.png "OpenJUMP - Carte"){: .img-center loading=lazy }

## Modification du style des couches

Passons ensuite à la modification du style de ma couche. L'interface proposée est riche, il est possible de modifier la couleur du contour, du fond, de jouer sur l'opacité , la taille des sommets ou encore la largeur des lignes :

![OpenJUMP - Style](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/style.png "OpenJUMP - Style"){: .img-center loading=lazy }

De plus il est également possible d'enrichir le style de notre couche en y ajoutant des éléments décoratifs tels que l'ajout d'un cercle ou d'une flèche sur le début, le milieu ou la fin du contour de notre objet. Travaillant quotidiennement sur une cartographie routière, cette fonctionnalité m'a été utile plus d'une fois :

![OpenJUMP - Symbologie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/style2.png "OpenJUMP - Symbologie"){: .img-center loading=lazy }

OpenJump permet également l'ajout d'étiquettes sur les objets. Là encore la personnalisation est vraiment aboutie. Car bien évidemment en plus de choisir le champ qui contiendra le texte à afficher, il est possible de définir l'alignement, la couleur la police ou encore l'échelle à laquelle le label sera visible.

![OpenJUMP - Label](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/label.png "OpenJUMP - Label"){: .img-center loading=lazy }

Finissons notre "tour d'horizon des styles" par (encore) une fonctionnalité intéressante. Dans les options du layer, il est possible d'importer un fichier de style au format SLD ou ArcMap.

![OpenJUMP - Layer](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/layer.png "OpenJUMP - Layer"){: .img-center loading=lazy }

## Interrogation des données

Autant j'ai longtemps été déçu par l'absence de cette fonctionnalité dans QGis autant là je suis agréablement surpris. En effet, il est possible d'effectuer des requêtes attributaires ou spatiales.

Commençons par les requêtes attributaires. trois modes sont disponibles : "requête attributaire", "simple requête", "rechercher dans tous les attributs". L'interface de requêtage est simple et soignée son utilisation en est donc facilitée. A noter que vos requêtes peuvent également être faites sous la forme d'expressions régulières.

![OpenJUMP - Query attributaire](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/openjump/query_attributaire.png "OpenJUMP - Query attributaire"){: .img-center loading=lazy }

pour les requêtes spatiales, différentes relations sont disponibles : intersecte, contient, recouvre, situé à mois de ... Décidément OpenJump me surprend de plus en plus.

![OpenJUMP - Spatial query](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/openjump/spatial_query.png "OpenJUMP - Spatial query"){: .img-center loading=lazy }

En plus de ces deux outils d'interrogations des données de nombreux autres comme la génération de zone tampon, de centroïde ou encore de simplification des objets sont disponibles. Je vous laisse les découvrir.

## Édition et modification des objets

Nous arrivons bientôt à la fin de ce billet, et devant toutes les éloges que j'ai déjà pu faire sur OpenJump, vous ne serez pas surpris si je vous dis que l'outil d'édition topologique est également des plus agréables et plein de fonctionnalités. Il est possible d'ajouter/supprimer un ou un groupe de sommets, de couper les lignes, de modifier la taille des éléments... Pour finir, je soulignerai une dernière fonctionnalité que je n'avais encore jamais rencontré sur aucun logiciel SIG, la possibilité d'ajouter des notes sur la carte. Avouez-que c'est plutôt bien pensé non?

![OpenJUMP - Topologie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/topologie.png "OpenJUMP - Topologie"){: .img-center loading=lazy }

## Conclusion

C'est sur une note très positive que je finirai ce billet. OpenJump a les moyens de jouer dans la cour des grands, la richesse de ces fonctionnalités est tout simplement impressionnante.

Le seul point négatif est la pauvreté des formats qu'il est possible d'ouvrir mais de nombreuses extensions pallient à cela. Seul abonné absent ? Le format tab j'espère que ce manque sera rapidement comblé. Peut-être également que l'interface mériterait un petit coup de jeune?  Mais après les goûts et les couleurs...

----

<!-- geotribu:authors-block -->
