---
title: "OpenGeo Suite en version 1.0, tests et impressions"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-02-04
description: "OpenGeo Suite en version 1.0, tests et impressions"
tags:
    - logiciel
    - open source
    - OpenGeo Suite
    - webmapping
---

# OpenGeo Suite en version 1.0, tests et impressions

:calendar: Date de publication initiale : 04 février 2010

![logo OpenGeo](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/opengeosuite.png "logo OpenGeo"){: .img-thumbnail-left }

Que de chemin parcouru depuis 2001, date du lancement du projet [GeoServer](http://geoserver.org/display/GEOS/Welcome), par l'équipe d'[OpenGeo](http://opengeo.org). En effet, il y a à peine quelques jours cette dernière annonce la sortie officielle d'[OpenGeo Suite](http://opengeo.org/products/suite/), un environnement complet (serveur et client cartographique) permettant de mettre en ligne des projets cartographiques et cela de manière complètement assistée. [CampToCamp](http://www.camptocamp.com/fr), avec le framework [MapFish](http://www.mapfish.org/), avait déjà à l'époque (Octobre 2008 - V1.0) fait sensation en offrant des fonctionnalités similaires sans toutefois atteindre la facilité d'administration que j'ai pu voir dans OpenGeo Suite. Profitant d'une [version d'essai](http://opengeo.org/products/suite/register/) de 30 jours j'ai donc installé cette version 1.0 afin de faire quelques tests.

## Installation

Premier gros point positif, l'installation est vraiment simple. En effet, le package fourni par OpenGeo est un all in one (tout en un). Il suffit donc simplement de lancer, en ligne de commande, le .bin et de répondre aux différentes questions. Sur Ubuntu cela a fonctionné immédiatement, quelqu'un a-t-il fait le test sur Windows ?

![install](https://cdn.geotribu.fr/img/Blog/geoserver/opengeo/install.png "install")

Une fois cette étape réalisée, selon l'endroit que vous avez spécifié lors de l'installation, vous devriez disposer d'un nouveau dossier contenant l'exécutable opengeo-dashboard. C'est ce programme qui va permettre de lancer l'interface d'administration que nous détaillerons dans les paragraphes suivants.

## Interface générale

Comme vous pouvez le constater, l'interface est sobre et vraiment agréable. Plusieurs menus contextuels et d'aides sont disponibles. Pour démarrer OpenGeo Suite, il est nécessaire de cliquer sur le bouton **start** en bas à droite de l'interface.

![dashboard](https://cdn.geotribu.fr/img/Blog/geoserver/opengeo/dashboard.png "dashboard")

## Ajout de données

Commençons un peu à jouer et ajoutons des données. Un lien sur l'interface précédente, "Import Layers", ouvre une nouvelle fenêtre dans le navigateur. Pour les habitués de GeoServer, vous n'aurez pas de mal à reconnaître l'interface de l'applicatif.

![add_layer](https://cdn.geotribu.fr/img/Blog/geoserver/opengeo/add_layer.png "add_layer")

Mes données n'ayant pas de référence spatiale, je suis invité à sélectionner une projection.

![add_srs_layer](https://cdn.geotribu.fr/img/Blog/geoserver/opengeo/add_srs_layer.png "add_srs_layer")

Enfin, il ne me reste plus qu'à importer mes données à mon projet cartographique.

![select_layer](https://cdn.geotribu.fr/img/Blog/geoserver/opengeo/select_layer.png "select_layer")

## Modification du style des données

Mes données n'ayant, pour le moment, aucune symbologie je vais les personnaliser à l'aide du "Styler". Ce menu de modification du style des couches a beaucoup fait parler de lui en particulier sur la liste GeoExt. Il faut dire que sa réalisation est vraiment aboutie. L'interface est simple et intuitive. Vous pouvez ainsi, en quelques clics, personnaliser le rendu de vos couches.

![style1](https://cdn.geotribu.fr/img/Blog/geoserver/opengeo/style1.png "style1")

Dans l'exemple ci-dessous, je suis passé de carré orange à des triangles rouges.

![style2](https://cdn.geotribu.fr/img/Blog/geoserver/opengeo/style2.png "style2")

## Export et publication

Une fois toutes ces étapes réalisées, il ne reste plus qu'à publier notre projet sur le web. Deux modes de publication sont possibles. Soit, sous forme d'Iframe ou alors un permalink permettant d'accéder directement au projet.

![publish](https://cdn.geotribu.fr/img/Blog/geoserver/opengeo/publish.png "publish")

![save_map](https://cdn.geotribu.fr/img/Blog/geoserver/opengeo/save_map.png "save_map")

## Conclusion

OpenGeo est un produit abouti qui saura convaincre les administrateurs SIG n'ayant pas ou peu de temps à consacrer à la mise en place d'une application de type WebMapping. Tout le paramétrage se fait directement depuis les différentes interfaces d'administration et cela apporte une réelle souplesse d'utilisation. La seule limite que j'ai trouvé porte sur la gestion des projets qui est inexistante; aucune interface me permettant de charger, modifier ou supprimer un projet précédemment créé n'est disponible, c'est un peu dommage.

Enfin, reste la question du [prix](http://opengeo.org/products/suite/buy/#price) qui va de 5730€ en entrée de gamme pour la "basic edition" jusqu'à 70 204€ pour la "strategic edition". Par curiosité, j'ai cherché à savoir combien valait la licence ArcGis Server. Impossible de trouver cette information sur le site d'Esri, je m'appuierai donc sur les prix donnés dans ce [post](http://georezo.net/forum/viewtopic.php?pid=100845#p100845) de GeoRezo où les tarifs vont de 7000 à 68 000€ (avec ArcSDE inclut). Je précise que ce ne sont pas des chiffres officiels et qu'ils doivent donc être utilisés avec précaution. Première remarque, Esri est moins cher que OpenGeo - ce n'est plus vrai en faisant la conversion dollar/euro (oups, désolé) - , grosse déception pour moi fervent défenseur de l'OpenSource. Mais en réalité comparer le prix n'a pas vraiment de signification. En effet, Esri fournit un logiciel alors qu'OpenGeo fournit un service. En effet, le prix d'OpenGeo, au contraire d'Esri, comprend la location et l'hébergement d'un serveur allant de 2 à 32 cpus (voir post ci-dessous), jusqu'à 4 jours de formation sur site, l'assurance d'une réponse du service technique en moins de 2 heures... Me voilà rassuré, ma vision de l'OpenSource reprend sa juste place.

----

<!-- geotribu:authors-block -->
