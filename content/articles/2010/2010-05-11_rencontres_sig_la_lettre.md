---
title: "Les rencontres SIG la lettre, un événement réussi"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-05-11
description: "Les rencontres SIG la lettre, un événement réussi"
tags:
    - colloque
    - rencontre
    - SIG la lettre
---

# Les rencontres SIG la lettre, un événement réussi

:calendar: Date de publication initiale : 11 mai 2010

![30575541:avatar_medium.jpg](https://cdn.geotribu.fr/img/Blog/divers/30575541%3Aavatar_medium.jpg){: .img-thumbnail-left }

C'est dans les locaux de l'[Ecole Nationale des Sciences Géographiques](http://www.ensg.eu/) (ENSG) que s'est tenue la seconde édition des [rencontres SIG la Lettre](http://www.rencontres-sig-la-lettre.fr/). Cet événement, unique sur le territoire français, a permis de regrouper pendant 3 jours (4-5-6 Mai) les principaux acteurs de la géomatique.

Le [programme](http://www.calameo.com/books/00000081549d6afa76cf9), très riche, était découpé entre les traditionnelles sessions de présentation, des Master Class et les visites des stands. Quelques grands noms de l'industrie du SIG ont fait le déplacement. Étaient présent notamment : [ESRI France](http://www.esrifrance.fr/), [Garmin](http://www.garmin.com/garmin/cms/site/fr), Google, [Pitney Bowes](http://www.pitneybowes.fr/)... Côté OpenSource ont a pu retrouver [CampToCamp](http://www.camptocamp.com/), [Makina Corpus](http://www.makina-corpus.com/), [Geomatys](http://www.geomatys.fr/geomatys/main.jsp?adress=Accueil.jsp), l'[OSGEO-fr](http://wiki.osgeo.org/wiki/Francophone_OSGeo_Chapter) et [OpenStreetMap](https://www.openstreetmap.org/). Les présentations ayant lieu simultanément, je n'ai malheureusement pas pu assister à l'ensemble d'entre elles. Je vous livre ci-dessous, mon impression sur ce colloque et sur les sujets qui y ont été abordés.

## Le programme des sessions

Les sessions, au nombre trois par jour, portaient à chaque fois sur une problématique d'actualité. Celle auxquelles j'ai assisté, intégralement ou presque, sont signalées par une icône. Voici le résumé du programme :

### Mardi 4 Mai

- Mettre en place un serveur spatial, coûts et conséquences ![02.png](https://cdn.geotribu.fr/img/Blog/divers/02.png "02.png")
- Inspire, la mise en œuvre au quotidien
- La géomatique au service des nouveaux enjeux territoriaux
- Master Class API

### Mercredi 5 Mai

- De la bonne utilisation des API grand public
- Standards OGC France, où en est-on
- La qualité des données, pourquoi fait-elle encore débat ![02.png](https://cdn.geotribu.fr/img/Blog/divers/02.png "02.png")
- Master Class 3D

### Jeudi 6 Mai

- La gestion des réseaux enterrés : un sujet chaud
- Quels référentiels sur l'eau aujourd'hui et demain
- Réalité augmentée, serious gaming : Les nouvelles expériences de la géographie ![02.png](https://cdn.geotribu.fr/img/Blog/divers/02.png "02.png")
- Master Class Mind Mapping

D'une manière générale, il est facile de noter que ce colloque à principalement porté les deux thèmes majeurs que sont le SIG-Web et la qualité des données. D'une manière plus transversale et à tous les niveaux la question de la démocratisation de la géomatique, également appelée Volunteered Geographic Information[^1], a tenu une place importante. Preuve s'il en est des intérêts, des craintes et des interrogations qu'elle suscite.

Enfin, ces trois jours ont également été ponctués par l'intervention de deux [grands témoins](http://www.rencontres-sig-la-lettre.fr/grands-temoins/), Loïc Hay et Dominique Boullier. Leur présentation a été, c'est en tous cas mon sentiment, REMARQUABLE. Le premier a abordé le sujet de "Attention la géomatique 2.0 débarque". Le second nous a quant à lui donné une leçon magistrale sur "Des SIG à la cartographie contributive : politiques de l’exploration spatiale". J'ai particulièrement aimé la folie et le décalage qu'ont su imposer ces deux orateurs hors pair. Messieurs, si vous lisez ces lignes, je vous tire mon chapeau !

Plutôt que de vous faire un résumé chronologique qui ferait un peu trop carnet de voyage, je vais garder le fil conducteur des deux thèmes principaux que nous avons identifiés précédemment (SIG-Web et la qualité des données). Nous y gagnerons, je pense, en cohérence. Ces trois jours de colloques seront ainsi résumés dans les deux paragraphes ci-dessous.

### SIG-Web

L'incursion de Google Maps en 2004 (pour les Etats-Unis, 2006 en France) dans notre univers web traditionnel a profondément modifié notre façon d'appréhender et de consommer l'information. Cette dernière a acquis une dimension géographique incontestable, au point que nous assistons aujourd'hui à une indexation spatiale systématique du contenu du Web[^2](#footnote2_xabuyh4 "Boris Mericskay, “Analyse du processus de  démocratisation de la géomatique. Le développement du GéoWeb 2.0 et ses impacts sur la gestion territoriale participative,” 2009. (projet de recherche)").

Cette démocratisation du Géo-Web a également eu de profondes répercussions pour nous géomaticiens. Pas une administration ou une institution qui ne souhaite disposer de son environnement de WebMapping. Mais le passage de notre univers bureautique habituel à univers virtuel n'est pas sans contrainte.

Sur ce point, la [présentation](http://www.rencontres-sig-la-lettre.fr/wp-content/uploads/2010/05/Serveur-Philipona.pdf) de Claude Philipona (CampToCamp) portant sur "Le cloud computing au service des applications cartographiques à haute disponibilité" a été particulièrement intéressante. En effet, en raison de ses caractéristiques particulières (nécessité d'une forte bande passante, gros volume de données...), le WebMapping nécessite une infrastructure de serveurs adaptée. Celle-ci ne va pas sans un investissement conséquent. Or en ces temps de rigueur budgétaire, il peut être intéressant de ne payer que ce qui est consommé. C'est ce que permet le Cloud Computing. Votre application est hébergée sur une ferme de serveur qui s'adapte en fonction du nombre d'utilisateurs connectés, de la bande passante nécessaire ou encore du volume de données. Mais au final vous ne payerez que ce que vous avez réellement utilisé. En somme, de l'informatique sur mesure. Divers services de Cloud Computing existent actuellement, les plus connus étant [Amazon](http://aws.amazon.com/), [GoGrid](http://www.gogrid.com/), [Rackspace Cloud](http://www.rackspacecloud.com/), [Google](http://code.google.com/intl/fr/appengine/)... Si le sujet vous intéresse, je vous conseille également la lecture du [billet](http://nauges.typepad.com/my_weblog/2010/04/la-r%C3%A9volution-industrielle-informatique.html) très formateur de Louis Naugès.  
Claude Philipona, lors de son intervention, a largement mis en avant les aspects positifs de cette solution sans toutefois aborder les points négatifs. N'ayant pas posé de question à la fin, j'ai également une part de responsabilité. Mais souvent quand je discute avec des administrateurs informatiques ils me font part de leurs inquiétudes quant à la localisation et à la sécurité de leurs données. A force d'être partout elles sont aussi nulle part.

La seconde [présentation](http://www.rencontres-sig-la-lettre.fr/wp-content/uploads/2010/05/Serveur-Ribot.pdf) qui a retenu mon attention est celle de Nicolas Ribot (Magellium) sur le thème de "Comparatif des bases de données spatiales : Oracle, PostgreSQL, MySQL, SpatialLite". Ces travaux font suite à une [première étude](http://cct.cnes.fr/cct05/public/2007/documents/Etude_comp_bases_donnees_spatialisees/rapport_etude_spatiale_final.pdf) réalisée pour le CNES qui portait uniquement sur les trois premières bases citées. Il en ressort que, globalement Oracle reste dominant au regard du nombre de fonctions métiers dont elle dispose. Mis à part cela, nos équivalents libres n'ont pas à rougir. Les fonctionnalités et les performances étant équivalentes avec le prix en moins. L'ajout de SpatiaLite comme nouvel objet d'étude est également un point à noter. Celle-ci, au contraire des 3 autres, n'utilise pas le paradigme habituel client-serveur. Au contraire, elle s'intègre directement dans l'application qui utilise sa bibliothèque logicielle. Ses caractéristiques et sa légèreté font qu'elle est particulièrement utilisée dans le monde des mobiles embarqués.

La partie Web étant terminé passons maintenant à la qualité des données.

### Qualité des données

En voilà un sujet qui aura su déchainer les convictions. De cette session, il faudra retenir cette expression qui nous vient tout droit de nos amis canadiens : "Pelleter des nuages". Celle-ci traduit l'état actuel des recherches autour de la qualité des données. C'est-à-dire un domaine que s'est accaparé le milieu universitaire mais dont les retombées dans le milieu industriel sont moins perfectibles. Si tout le monde s'accorde à dire que disposer de données de qualité est essentiel il reste toujours à répondre à la question du Comment. En effet, aujourd'hui, celle-ci est vue davantage comme une contrainte à mettre en place.

Actuellement la réponse la plus adéquate que nous ayons su apporter à la gestion de la qualité est la mise en place des métadonnées. Véritable carte d'identité, celles-ci introduisent de nombreux critères permettant de juger de la qualité de celle-ci :

- Généalogie
- Actualité
- Cohérence logique
- Précision sémantique
- Précision géographique
- Exhaustivité
- Complétude

Pour une description plus complète de ces critères, je vous renvoie à l'article "Qualité des données géographiques" paru dans le numéro 41 du magazine Sign@ture[^3].

Mais, si cette notion de métadonnée semble répondre à notre problématique initiale de gestion de la qualité, il faut admettre que, malheureusement, celle-ci ne couvre pas toutes les attentes des producteurs et des utilisateurs. A ce sujet, il convient de différencier les métadonnées producteur des métadonnées utilisateur. Les premières permettent de caractériser dans quelles conditions ont été acquises les données. Les secondes visent à mettre en adéquation les attentes de l'utilisateur et les possibilités de la donnée. Toutes deux renvoient à des objectifs différents.

Enfin, nous ne pourrions clore ce paragraphe sans parler de la table ronde qui s'est tenue jeudi soir. Celle-ci avait pour thème "La question de la qualité à l'heure de la géomatique collaborative". Pour ma part, et au regard des invités présents, le titre me gêne beaucoup. En effet, la géomatique collaborative définie notamment par Henri Pornon[^4] ne doit pas être confondu avec les mouvements communautaires participatifs actuellement en vogue dans notre domaine. Ils n'ont ni les mêmes origines, ni les mêmes objectifs. Ce point de détail passé, je vous livre ci-dessous mes impressions sur cette table ronde qui a vu se réunir (pour la 1ere fois ?) deux mondes qui d'habitude au mieux s'ignorent au pire se méprisent.

Une fois les présentations effectuées, nous sommes rapidement arrivés dans le vif du sujet avec une première question qui a donné, de suite, le ton de la discussion. Sans reprendre tout le discours, je traduirai celle-ci par : "La liberté de ces mouvements communautaires ne devraient-elle pas, dans certains cas, être plus encadrée voir même limitée ?".  
Pour appuyer cette réflexion revenons à la participation d'OpenStreetMap aux différentes catastrophes qui ont secoué la planète récemment. Le cas que nous étudierons sera celui du tremblement de terre d'Haïti.

L'implication d'OpenStreetMap dans les différentes catastrophes naturelles qui ont récemment marqué l'actualité (séisme Haïti) a apporté un nouvel éclairage quant à l'utilité immédiate de ce genre d'initiative (cf [wiki Haïti](https://wiki.openstreetmap.org/wiki/WikiProject_Haiti)).  
En effet, suite à cet événement, la [communauté de contributeurs](https://wiki.openstreetmap.org/wiki/Humanitarian_OSM_Team) s'est rapidement mobilisée afin de fournir aux autorités compétentes un état des lieux le plus exhaustif possible de la situation. Cette initiative a été rendue possible par la complémentarité des actions entre d'une part des instances gouvernementales ou privées (Geoeye, Google, Digitalglobe, NOAA, JAXA, SPOT) qui ont fourni les images satellites de la zone et d'autre part les contributeurs qui se sont appuyés sur ces dernières pour cartographier la zone sinistrée.  
Suite à la demande du Bureau de la coordination des affaires humanitaires en plus du réseau routier, l'emplacement des campements et leur taille ou encore la présence de barrières ou éboulement bloquant la rue ont été cartographiés. Ainsi en à peine quelques heures (moins de 48 heures) près de 16 000 bâtiments dont 7000 référencés comme endommagés ont pu être identifiés.

![hikebikemap-haiti](https://cdn.geotribu.fr/img/Blog/OSM/hikebikemap-haiti.png "hikebikemap-haiti")

> Source : [3liz](http://3liz.com/blog/rldhont/index.php/2010/01/18/327-openstreetmap-et-haiti-la-force-d-une-communaute)

D'un point de vue candide, cette mobilisation générale pour une cause noble ne peut être vue que positivement. Mais il est également nécessaire de prendre un minimum de recul et de se poser certaines questions. En effet, lors de cet évènement, il avait été demandé aux contributeurs de cartographier les routes praticables. Quelles auraient été les conséquences si une équipe de secours avait emprunté un pont fragilisé par le séisme mais dont les dégâts n'auraient pas été visibles à partir des images fournies ? Bien évidemment ces équipes avaient reçu l'ordre de vérifier les infrastructures. Mais en temps de crise, le manque de temps est souvent cruel et surtout il ne faut pas sous estimer le pouvoir cognitif d'une carte. Plus que tout autre média, celle-ci, est peu soumise au regard critique de l'utilisateur. Preuve en est, combien de personnes ont fini avec leur voiture dans un lac pour avoir préféré écouter leur GPS plutôt que les indications routières ?

Vous connaissez tous mon engagement pour OSM, il ne s'agit donc pas là de faire un procès contre ce mouvement mais plutôt d'améliorer celui-ci. En effet, si je reprends l'objectif initial d'OpenStreetMap, il s'agit de créer une carte du monde libre. Il n'avait donc jamais été question, à l'origine, d'aider des équipes de secours ou de porter assistance à des personnes. Si la réactivité et l'engagement des personnes participant au projet OSM nous permettent d'imaginer d'autres utilisations que celles initialement prévues, il convient aussi de revoir le modèle de publication ou d'encadrement de production. En effet, comme tous les mouvements communautaires, OpenStreetMap se base sur un processus itératif d'enrichissement afin d'améliorer la qualité de sa donnée. Or en période de crise, ce processus est court circuité par manque de temps. Il est à noter que des équipes d'OpenStreetMap travaillent activement à l'amélioration de ce processus à l'exemple des membres de [Crisis Mapper](http://www.crisismappers.net/). Un nouveau canal d'information permettant une gestion de crise plus locale est en train de se mettre en place. Je suis persuadé de son utilité et des bénéfices que cela apportera. Mais il est de notre responsabilité de nous poser (ou d'imposer) nos propres limitations sous peine d'arriver à des situations juridiques embarrassantes[^5](#footnote5_r6c7g9s "Marc Gervais et al., “Qualité des données géographiques. Obligations juridiques potentielles et modèle du producteur raisonnable,” Revue internationale de géomatique 17, n°. 1 (4, 2007): 33-62.").

La deuxième question, moins visible, soulevée par ce débat est : "à partir de quel moment passe-t-on de la cartographie de localisation à la connaissance ?". Pointer un arbre sur une carte a-t-il la même valeur si je renseigne en plus son essence et son nom ? Cette question n'est pas simple et ce billet déjà suffisamment long. Je ne développerai pas plus cette réflexion mais nous y reviendrons prochainement.

Comme nous avons pu le voir , et j'espère avoir réussi à vous le faire ressentir, nous sommes actuellement en face de deux communautés qui cherchent leurs marques. L'insertion de ces mouvements communautaires à certes bousculée nos habitudes, mais c'est à nous maintenant de savoir nous placer et d'utiliser au mieux les potentialités offertes par ce nouveau canal d'information.

### Conclusion et remarques

Pour mon premier colloque des rencontres SIG la lettre, je dois avouer que je garde un souvenir très positif. Les interventions ont été, pour la plupart, d'une remarquable qualité. De plus cela m'a également permis de mettre un visage sur des gens que nous fréquentons habituellement au travers des forums et des communautés virtuelles. Quelques grands nom du SIG ont également fait le déplacement. Ce fut l'occasion pour moi de nouer des contacts et surtout d'échanger des points de vues avec des personnes que j'ai plus souvent l'habitude de lire que de voir :)

Quelques points négatifs, il en faut bien, mais rien de bien méchant. Voici ce que j'ai pu relever et qui mériterait d'être amélioré :

- Mettre en place un canal Twitter
- Donner un accès Wifi aux visiteurs (renseignements pris, il suffisait de demander les codes wifi à l'accueil)
- Avoir un buffet cafés et viennoiseries à volonté :p

Je vous laisse avec quelques photos que prises durant ce colloque. J'espère que les personnes ne m'attaqueront pas pour utilisation abusive de leur image :wink:

![Gaël MUSQUET et Jean-Roc Morreale sur le stand OSGEO/OSM](https://cdn.geotribu.fr/img/Blog/divers/2010-05-04%2014.13.05.jpg "Gaël MUSQUET et Jean-Roc Morreale sur le stand OSGEO/OSM")

Au premier plan, Gaël MUSQUET et Jean-Roc Morreale sur le stand OSGEO/OSM

![Démonstration CampToCamp](https://cdn.geotribu.fr/img/Blog/divers/2010-05-04%2016.42.25.jpg "Démonstration CampToCamp")

Yves Jacolin et Cédric Moullet de CampToCamp en pleine démonstration

![Les experts de Google](https://cdn.geotribu.fr/img/Blog/divers/2010-05-06%2012.43.03.jpg "Les experts de Google")

La rencontre avec les experts de Google a fait le plein

[^1]: Michael Goodchild, “Citizens as sensors: the world of volunteered geography,” GeoJournal 69, n°. 4 (2007): 211-221.
[^3]: <http://www.certu.fr/download.php?file_url=IMG/pdf/signature41.pdf>
[^4]: Henri Pornon, “Vers des SIG plus collaboratifs : la géo-collaboration,” Géomatique Expert, n°. 20 (Septembre 2007)

----

<!-- geotribu:authors-block -->
