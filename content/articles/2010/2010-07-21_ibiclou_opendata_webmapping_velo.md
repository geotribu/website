---
title: "iBiclou : OpenData, webmapping et vélo"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-07-21
description: "iBiclou : OpenData, webmapping et vélo"
tags:
    - API
    - Google Maps
    - iBiclou
    - open data
    - vélo
---

# iBiclou : OpenData, webmapping et vélo

:calendar: Date de publication initiale : 21 juillet 2010

![logo iBiclou](https://cdn.geotribu.fr/img/logos-icones/divers/ibiclou_geotribu_logo.png "logo iBiclou"){: .img-thumbnail-left }

L'[OpenData](https://en.wikipedia.org/wiki/Open_science_data) est à l'honneur en ce moment. Il s'agit d'un mouvement de libération des données de toutes formes pour les rendre accessibles à tout le monde, sans contrainte ni restriction. On peut assimiler ce mouvement à celui de l'[OpenSource](https://fr.wikipedia.org/wiki/Open_source) mais ici pour les données. Comment utiliser ces données dans des environnements WebMapping, où les trouver ?

Plutôt que d'essayer maladroitement de vous expliquer l'OpenData, je vous renvoie vers les excellents articles de [Owni](http://owni.fr/categorie/opendata-cultures-numeriques/) ou ceux - tout aussi excellents - de [Regards Citoyens](http://www.regardscitoyens.org/open-data-en-france/), de [LiberTIC](http://libertic.wordpress.com/) ou de [ePSI platform](http://www.epsiplatform.eu/) sur cette thématique : vous y verrez que licence libre, innovation (sociale et technologique), économie et politique sont étroitement liées. Cette [vidéo](http://www.ted.com/talks/tim_berners_lee_the_year_open_data_went_worldwide.html) de TED.com présente également comment et pourquoi utiliser des données libérées. Lire aussi l'[interview](http://www.lemonde.fr/technologies/article/2010/07/01/michael-cross-les-donnees-publique-s-doivent-pouvoir-etre-reutilisees-librement_1381453_651865.html) de Michael Cross - journaliste au Guardian - sur l'OpenData et notamment les problématiques que sous-entendent une libération des données.

D'ores et déjà, quelques municipalités de par le monde ont décidé de libérer en partie leurs données, c'est notamment le cas de :

- [Londres](http://data.london.gov.uk/)
- [San Francisco](http://www.datasf.org/)
- [Vancouver](http://data.vancouver.ca/)
- [New York](http://www.nyc.gov/html/datamine/html/home/home.shtml)
- [Toronto](http://www.toronto.ca/open/)
- [Rennes](http://data.keolis-rennes.com/)

Et même des pays :

- [Etats-Unis](http://www.data.gov/)
- [Royaume-Uni](http://data.gov.uk/)

Ou au niveau régional :

- [Regione Piemonte](http://www.dati.piemonte.it/)

## Le succès des données Londoniennes

L'ouverture de l'API des données temps réel transport à Londres a créé un tel engouement de la part des développeurs que les serveurs se sont vus un peu [surchargés](http://www.guardian.co.uk/technology/blog/2010/jul/02/tfl-tube-map-api-overwhelmed-demand). Cette explosion de requêtes est cependant prometteuse, en effet ce phénomène d'OpenData prend de l'ampleur là où il est mis en place. C'est que quelque part ça répond à un besoin. Cela va dans le bon sens selon moi. Il faudra que les services ouvrant leurs données prennent en compte la charge sur leurs serveurs : duplication de serveurs, clé API de test ...

## L'Agence du Patrimoine Immatériel de l'Etat

*Les richesses de l'immatériel sont les clés de la croissance future.* C'est pas moi qui le dit, c'est écrit sous le nom du [site](https://www.apiefrance.com/). Cet organisme a un [rôle](https://www.apiefrance.com/sections/presentation_apie/missions/missions_de_l_apie) dans la définition et la valorisation de l'immatériel en France. Quel est donc sa position envers l'OpenData ? La gratuité d'une majeure des données publiques pour tout le monde ? Un forfait à payer dès que l'utilisation des données apportent un revenu ? Pour essayer d'y voir un peu plus clair sur la politique de l'APIE, voici quelques liens intéressants :

- [L'effet pervers de l'OpenData payant](http://berjon.com/blog/2010/07/apie-opendata-payant-effet-pervers.html)
- [Open Data : que fait le gouvernement ?](http://www.temps-reels.net/dossier/view/open-data-que-fait-le-gouvernement)

## Rennes et ses données transport

En mars dernier, Rennes a ouvert le bal de la libéralisation de ses données en France - Brest et [Plouarzel](http://www.a-brest.net/article6002.html) avaient déjà commencé notamment dans la diffusion de leurs données cartographiques. Ainsi Rennes met à disposition les données en temps réel de ses bornes de vélo - nombre de vélos disponibles et nombre d'emplacements libres - via une [API](http://data.keolis-rennes.com/fr/accueil.html).

Celle-ci permet de récupérer via une simple requête URL les données au format XML ou JSON. Le site d'explication est très bien documenté, le forum actif et les administrateurs [réactifs](http://data.keolis-rennes.com/fr/forum/developpement.html?tx_mmforum_pi1%5Baction%5D=list_post&tx_mmforum_pi1%5Btid%5D=50).

Vivement l'ouverture de nouvelles données. Bravo pour cette initiative et en espérant qu'elle ouvre la voie à d'autres communes ou agglomérations !

## Utilisation de l'API Data Keolis

Rien de bien méchant : il suffit de demander une [clé](http://data.keolis-rennes.com/fr/obtenir-un-compte.html) et de commencer les développements. Je vous laisse regarder [ici](http://data.keolis-rennes.com/fr/les-donnees/fonctionnement-de-lapi.html) pour comprendre le fonctionnement de l'API. Attention il est nécessaire d'avoir un compte pour pouvoir accéder à cette page !

## Développement d'une application sur ces données

Nous avons maintenant toutes les cartes en main pour produire une petite web application sympathique : avoir une carto des disponibilités des vélos à Rennes. Comme nous avons besoin de cette information souvent dans la rue, celle-ci devra être disponible sur smartphone et quelque soit l'OS de celui-ci (iPhone, Android, BlackBerry, etc). Pour éviter de faire des applications dans tous ces langages, une WebApps est la solution. Il suffira à l'utilisateur d'entrer une URL dans son navigateur mobile et d'accéder à la carto (cf. [Quel développement cartographique pour des plateformes différentes ?](http://geotribu.net/node/195)). Pour le moment seule l'[API Google Maps v3](http://code.google.com/intl/fr/apis/maps/documentation/javascript/) est fluide sur navigateur mobile, je ne sais pas si OpenLayers sera utilisable sur smartphone dans le futur - si vous avez des infos dessus, n'hésitez pas. Edit : [quelques discussions](http://www.spatiallyadjusted.com/2010/06/28/openlayers-3-0-takes-shape/) sur OpenLayers dans sa version 3.0 - il y aura peut-être un support mobile ... cf. le 11ème point Edit2 : on m'annonce qu'une version mobile d'OpenLayers existe déjà mais à l'état embryonnaire : [IOL](http://projects.opengeo.org/mobile). Et quelques [tests](http://trac.openlayers.org/browser/sandbox/camptocamp/mobile/trunk/lib/IOL/externals/openlayers/examples/select-feature.html) dans la sandbox d'OpenLayers suivent ce chemin.

## iBiclou

Sous la forme d'un petit (plus complet que prévu :-) ) site web - disponible sur ordinateur classique et surtout sur smartphone - l'application web propose une cartographie des bornes de vélos et la disponibilité de ces derniers. Un petit code couleur permet d'identifier rapidement les bornes les plus proches et leur état. En petite forme au niveau inspiration, nous lui avons donné le nom d'**iBiclou** :-) - cliquez sur l'image pour accéder au site

[![iBiclou](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/ibiclou1.png "iBiclou"){: .img-center loading=lazy }](http://www.ibiclou.com)

Bonne navigation et [allez taffer en vélo](http://forum.velotaf.com/) :-)

Au fait, le site dans sa version PC, ça fonctionne bien mieux sur des navigateurs qui supportent le HTML5 ...

----

<!-- geotribu:authors-block -->
