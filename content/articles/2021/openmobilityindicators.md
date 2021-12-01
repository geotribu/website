---
title: "Projet OpenMobilityIndicators, appli 'mon quartier à pied' : c'est en ligne"
authors:
    - Patrick GENDRE
categories:
    - article
date: "2021-11-29 11:20"
description: "Open Mobility Indicators est un projet open source de calcul d'indicateurs à base de notebooks python utilisant l'infrastructure gitlab, l'application web sur le thème de la marchabilité en France"
image: "Image d'illustration de l'article qui sert ensuite dans la mise en avant : réseaux sociaux, flux RSS..."
license: default
tags:
    - OpenStreetMap
    - marche
---

# Projet OpenMobilityIndicators, appli "mon quartier à pied" : c'est en ligne

:calendar: Date de publication initiale : 29 novembre 2021

## Introduction

Après un démonstrateur couvrant la région Sud PACA l'an dernier avec le soutien du Conseil Régional et de l'Ademe, 
la nouvelle version de l'application "mon quartier à pied" dans le cadre du [projet OpenMobilityIndicators](https://openmobilityindicators.org/) couvre désormais la France métropolitaine : elle a été développée grâce au travail de l'équipe de [Jailbreak](https://jailbreak.paris/fr-fr/) et au soutien du [programme "Résilience des territoires" de l'Ademe](https://wiki.resilience-territoire.ademe.fr/wiki/Mon_quartier_%C3%A0_pied).

![](https://openmobilityindicators.org/img/clapiers.png)

[L'appli est ici](https://app.openmobilityindicators.org/).

[Pour en savoir plus sur le projet](https://openmobilityindicators.org/projet).

L'appli est centrée sur une dimension de la marchabilité : le maillage du réseau de voirie empruntable par les piétons, et indirectement sur la mise en évidence des cheminements à créer.
Elle s'appuie donc essentiellement sur la donnée de voirie d'OpenStreetMap.

La grosse valeur ajoutée, qui ne se voit pas dans l'application, est qu'elle est conçue pour qu'on puisse ajouter de nouveaux indicateurs (via des [notebooks python](https://gitlab.com/open-mobility-indicators/indicators/)), sur le thème de la marche, ou sur tout autre mode de transport (d'où le nom du projet Open Mobility Indicators).   
Nous cherchons bien sûr des territoires et des partenaires intéressés pour tester cet outil.

L'ensemble du projet (code, données, livrables) est un commun librement utilisable décrit dans le wiki du projet, encore en cours de mise à jour.

 Un 1er cas d’usage possible :    
"[Libérez vos impasses](https://www.tousapied.be/nos-projets/liberez-vos-impasses/)" est une initiative lancée en 2015 par l’association belge « tous à pied », qui consiste à transformer les panneaux Impasses en y ajoutant des autocollants représentant un piéton et un cycliste ([pour en faire un panneau « C13d »](https://fr.wikipedia.org/wiki/Panneau_d%27indication_d%27une_impasse_en_France) - F45b en Belgique), lorsque la voie est en impasse. L’indicateur « [pedestrian-way-types](https://gitlab.com/open-mobility-indicators/indicators/pedestrian-way-types/-/blob/main/README.md) » identifie (en bleu sur la carte) ce qu’on a appelé les traverses, donc précisément les voies qui pourraient bénéficier d’un panneau C13d. Il pourrait donc être utilisé pour recenser ces voies et faciliter une démarche participative similaire à « Libérez vos impasses » en France.    
Bien d'autres cas d'usage sont possibles, notamment en travaillant sur le terrain à améliorer la cartographie OSM.

[Toutes vos suggestions, questions, remarques et critiques sont bienvenues, et même plus, indispensables pour nous aider à améliorer l'outil. Merci !](https://forum.fabmob.io/t/open-mobility-indicators/220)

![icône news générique](https://cdn.geotribu.fr/img/internal/icons-rdp-news/news.png "icône news générique"){: .img-rdp-news-thumb }

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Auteur

<!-- --8<-- "content/team/jmou.md" -->

{% include "licenses/default.md" %}
