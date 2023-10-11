---
title: "Panoramax, quel bilan tirer de la phase de construction? "
subtitle: Photo-cartographions librement le monde
authors:
    - Mathilde FERREY
    - Christian QUEST
categories:
    - article
comments: true
date: "2023-10-03 10:20"
description: "C'était il y a un an... l'IGN répondait à la proposition d'OpenStreetMap France et se lançait dans une phase d'investigation pour la création d'un street-view libre. Aujourd'hui, où en est-on ?"
image: "Image d'illustration de l'article qui sert ensuite dans la mise en avant : réseaux sociaux, flux RSS... 400x800 en PNG"
license: default
robots: index, follow
tags:
    - Geovisio
    - Panoramax
    - vues immersives
---


# Panoramax, quel bilan tirer de la phase de construction?

:calendar: Date de publication initiale : 3 octobre 2023

C'était il y a un an... l'[IGN](https://www.ign.fr/) répondait à la proposition d'[OpenStreetMap France](https://www.openstreetmap.fr/) et se lançait dans une phase d'investigation pour la création d'un Street-View libre nommé Panoramax. Aujourd'hui, où en est-on ?

Le projet tient-il ses promesses et les contributeurs sont-ils bien au rendez-vous ?

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Quelques chiffres

Fin septembre 2023, Panoramax c'est :

* 2 instances publiques ([IGN](https://panoramax.ign.fr/) et [OSM-FR](https://panoramax.openstreetmap.fr/#focus=map&map=2.01/12.45/31.69&speed=250))
* Plus de 8 millions de photos
* Plus de 20.000 séquences
* Une cinquantaine de contributeurs
* Un début d’intégration QGIS (avec Oslandia)

----

## Que propose Panoramax aujourd'hui?

Panoramax, c'est avant tout un géo-commun construit sur des principes fondateurs :

* Partager ses photos pour qu'un même cliché géolocalisé soit utilisable par tous
* Une multiplicité d’acteurs tant pour les prises de vue que pour les réutilisations
* Un projet décentralisé soutenu par une communauté élargie

![Panoramax - Projet décentralisé](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/panoramax/panoramax_01_projet_decentralise.webp){: .img-center loading=lazy }

Depuis le mois de mai dernier, un prototype développé au sein de la Fabrique des Géocommuns de l'IGN évolue au gré des tests et des retours des premiers utilisateurs.
La version bêta actuelle propose les premières briques essentielles que sont l'API et la visionneuse ainsi que deux outils de versement de photos sans oublier le moteur de floutage.

Tous ces développements sont libres et open-source, publiés sur <https://gitlab.com/geovisio> pour permettre aussi un retour direct avec des issues ou de la documentation.

----

## Une instance Panoramax : stockage et API

Partager des photos c'est avant tout une question de stockage et de catalogage de celles-ci.

![Panoramax - Carte des contributions](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/panoramax/panoramax_02_carte.webp){: .img-center loading=lazy }

Une API permet de verser des images, de les cataloguer, puis de les rechercher pour une diffusion à destination de différents outils (visionneuse mais pas uniquement). Elle s'appuie sur un espace de stockage et une base de données (PostgreSQL). Cette API se conforme au standard [STAC](https://stacspec.org/) (_Spatio Temporal Assets Catalog_) pour assurer l'intéropérabilité avec des outils existants.

Toute personne ou entité peut déployer sa propre "instance" Panoramax. Ceci permet par exemple à une collectivité de diffuser ses prises de vue en toute autonomie.

Actuellement deux instances publiques ont été mises en place, l'une par l'[IGN](https://panoramax.ign.fr/) et l'autre par [OpenStreetMap France](https://panoramax.openstreetmap.fr/#focus=map&map=2.01/12.45/31.69&speed=250). Le versement d'images y est ouvert à tous.

Les instances de stockage telles que celles de l'IGN ou d'OSM permettent à ceux qui n'ont pas la capacité de créer leur propre instance d'y stocker et partager leurs photos.

En quelques mois, ce sont plus de 8 millions de photos qui ont ainsi été versées sur ces deux instances.

----

## Un viewer de référence

Stocker et cataloguer c'est bien, mais permettre la visualisation des photos est bien sûr une nécessité !

La visionneuse de référence actuelle est issue de Geovisio, un développement initié entre autre par Géovélo et largement amélioré ces derniers mois pour Panoramax.

Elle permet de naviguer sur un fond de carte, de visualiser les séquences de photos et les photos qu'elles soient classiques ou sphériques (vues sphériques immersives à 360°).

![Panoramax - Visualiseur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/panoramax/panoramax_03_viewer.webp){: .img-center loading=lazy }

----

## Les outils de versement

Le premier outil de version proposé par la startup Panoramax a visé les versements en masse de prises de vue existantes. C'est un outil en ligne de commande (écrit en python) qui permet de verser des dossiers entiers d'images.

Depuis début septembre, un second outil de versement est disponible sous la forme d'une interface web utilisable avec un simple navigateur. On peut y glisser-déposer les photos à verser, qui sont ensuite envoyées par le navigateur vers l'instance Panoramax.

![Panoramax - Téléversement via l'application web](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/panoramax/panoramax_04_upload.webp){: .img-center loading=lazy }

Les versements ne sont pas anonymes, un compte utilisateur est nécessaire, pour l'instance OpenStreetMap France, c'est tout simplement le compte OSM qui est utilisé pour s'identifier.

----

## Une API de floutage

Le floutage des plaques d'immatriculation et des visages est un pré-requis à la diffusion publique des photos de terrain.

Celui-ci se fait à l'aide d'un modèle de machine-learning qui a été entraîné collaborativement. Pour cela, quelques milliers de photos ont été annotées par une vingtaine de contributeurs à l'aide du logiciel libre label-studio. Par la suite, les images classifiées ont été utilisées pour entraîner un modèle avec YOLOv8.

![Panoramax - API de floutage](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/panoramax/panoramax_05_floutage.webp){: .img-center loading=lazy }

Le floutage a donné de suite de bons résultats sur les photos "planes" mais était un peu décevant sur les photosphères (360°) en partie à cause de leurs dimensions. Un changement de paramètre permet désormais de bien meilleurs résultats et le modèle a été à nouveau entrainé pour encore améliorer les résultats.

Les annotations et le modèle couvrent un troisième type d'objet: les panneaux de signalisation. Ceci a permis de démarrer une expérimentation pour les détecter et les classer automatiquement.

----

## La gestion des séquences

Une fois les séquences de photos versées sur une instance, quelques outils sont disponibles pour masquer ou supprimer si besoin des photos ou des séquences entières.

![Panoramax - Gestion des séquences](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/panoramax/panoramax_06_sequences.webp){: .img-center loading=lazy }

De premiers outils de filtrage ont été mis en place dans la visionneuse pour sélectionner des images par date ou type. Ceci sera complété au fur et à mesure des besoins identifiés.

----

## Quelles sont les perspectives de réutilisation?

La contribution est la clé du succès du géocommun. Mais la réussite du projet tient aussi à ses réutilisations, et les possibilités sont infinies. Voici quelques exemples :

* Base de données Panneaux : référencement et identification automatisée des panneaux routiers
* Usages non routiers : référentiel des rivières (ex. dans le Lot Dordou), chemins de randonnée.

![Panoramax - Usage non routier](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/panoramax/panoramax_07_canal.webp){: .img-center loading=lazy }

* Enseignes publicitaires : détection par les collectivités locales
* Boitiers Fibre : repérages avant intervention
* Etat des fossés : repérages pour intervention
* végétation : identifier les tailles nécessaires - état (taille nécessaire)
* cimetières : vérifier l'état des sépultures
* accessibilité : préparer un déplacement, vérifier les cheminements
* arboretum - tourisme : se répérer avant la visite
* arrêts de bus : repérages, état

Et beaucoup d'autres encore à inventer. À suivre !

----

## Autrice

--8<-- "content/team/mfer.md"
