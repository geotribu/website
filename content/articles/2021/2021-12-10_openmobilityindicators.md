---
title: OpenMobilityIndicators, l'appli 'Mon quartier à pied' est en ligne
authors:
    - Patrick GENDRE
categories:
    - article
comments: true
date: 2021-12-10
description: Open Mobility Indicators est un ensemble d’outils logiciels libres et collaboratifs qui traite les données ouvertes pour créer des indicateurs de mobilité durable.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/open_mobility_indicators/OpenMobilityIndicators_apercu.png
license: default
tags:
    - marche
    - mobilité
    - OpenStreetMap
---

# Projet OpenMobilityIndicators, appli "mon quartier à pied" : c'est en ligne

:calendar: Date de publication initiale : 10 décembre 2021

## Introduction

![icône globe flux](https://cdn.geotribu.fr/img/internal/icons-rdp-news/flux.png "icône globe flux"){: .img-thumbnail-left }

Après un démonstrateur couvrant la région Sud PACA l'an dernier avec le soutien du Conseil Régional et de l'Ademe,
la nouvelle version de l'application web "Mon quartier à pied" dans le cadre du [projet OpenMobilityIndicators](https://openmobilityindicators.org/) couvre désormais la France métropolitaine. Elle a été développée grâce au travail de l'équipe de [Jailbreak](https://jailbreak.paris/fr-fr/) et au soutien du [programme "Résilience des territoires" de l'Ademe](https://wiki.resilience-territoire.ademe.fr/wiki/Mon_quartier_%C3%A0_pied).

![OpenMobilityIndicators - Clapiers](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/open_mobility_indicators/OpenMobilityIndicators_clapiers.png "OpenMobilityIndicators - Clapiers"){: .img-center loading=lazy }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Présentation

L'application est centrée sur une dimension de la marchabilité : le maillage du réseau de voirie empruntable par les piétons et indirectement sur la mise en évidence des cheminements à créer.  
Elle s'appuie donc essentiellement sur la donnée de voirie d'OpenStreetMap.

La grosse valeur ajoutée, qui ne se voit pas dans l'application, est qu'elle est conçue pour qu'on puisse ajouter de nouveaux indicateurs (via des [notebooks python](https://gitlab.com/open-mobility-indicators/indicators/)), sur le thème de la marche, ou sur tout autre mode de transport (d'où le nom du projet Open Mobility Indicators).  
Nous cherchons bien sûr des territoires et des partenaires intéressés pour tester cet outil.

L'ensemble du projet (code, données, livrables) est un commun librement utilisable décrit dans le wiki du projet, encore en cours de mise à jour. [Les données GeoJSON ou CSV produites sont republiées](https://gitlab.com/open-mobility-indicators/website/-/wikis/1_visiteur/T%C3%A9l%C3%A9charger-les-donn%C3%A9es).

### Sous le capot

On retrouve des [notebooks](https://gitlab.com/open-mobility-indicators/indicators) essentiellement basés sur [pyrosm](https://pyrosm.readthedocs.io/en/latest/) et [geopandas](https://geopandas.org/) comme librairies géomatiques.  
L'application web cartographique utilise [SvelteKit](https://kit.svelte.dev/) et [Maplibre](https://maplibre.org/).  
Les tuiles vecteur sont générées avec [tipecannoe](https://github.com/mapbox/tippecanoe).

----

## Un premier cas d’usage possible

![panneau C13d](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/open_mobility_indicators/panneau_C13d.png "panneau C13d"){: .img-thumbnail-left }

"[Libérez vos impasses](https://www.tousapied.be/nos-projets/liberez-vos-impasses/)" est une initiative lancée en 2015 par l’association belge « Tous à pied », qui consiste à transformer les panneaux "impasse" en y ajoutant des autocollants représentant un piéton et un cycliste ([pour en faire un panneau « C13d »](https://fr.wikipedia.org/wiki/Panneau_d%27indication_d%27une_impasse_en_France) - F45b en Belgique), lorsque la voie est en impasse.

L’indicateur « [pedestrian-way-types](https://gitlab.com/open-mobility-indicators/indicators/pedestrian-way-types/-/blob/main/README.md) » identifie (en bleu sur la carte) ce qu’on a appelé les traverses, donc précisément les voies qui pourraient bénéficier d’un panneau C13d. Il pourrait donc être utilisé pour recenser ces voies et faciliter une démarche participative similaire à « Libérez vos impasses » en France.

Bien d'autres cas d'usage sont possibles, notamment en travaillant sur le terrain à améliorer la cartographie OSM.

Toutes vos suggestions, questions, remarques et critiques sont bienvenues, et même plus, **indispensables** pour nous aider à améliorer l'outil. Le [forum est grand ouvert](https://forum.fabmob.io/t/open-mobility-indicators/220) ! Merci !

[Application :fontawesome-solid-earth-europe:](https://app.openmobilityindicators.org/){: .md-button }
[Site du projet :fontawesome-solid-up-right-from-square:](https://openmobilityindicators.org/projet/){: .md-button }
[Forum :fontawesome-regular-comments:](https://forum.fabmob.io/t/open-mobility-indicators/220/){: .md-button }
{: align=middle }

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
