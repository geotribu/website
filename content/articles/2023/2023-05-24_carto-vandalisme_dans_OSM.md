---
title: "Carto-vandalisme dans OpenStreetMap : mythe ou réalité ?"
authors:
    - Quy Thy TRUONG
categories:
    - article
comments: true
date: 2023-05-24
description: Détection du vandalisme cartographique dans OSM grâce à de l'apprentissage automatique
icon: material/spray
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/osm_carto_vandalisme/osm_vandalisme_en-tete.png
license: default
robots: index, follow
tags:
    - carto-vandalisme
    - OpenStreetMap
---

# Carto-vandalisme dans OpenStreetMap : mythe ou réalité ?

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

![logo OpenStreetMap notes et validation](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/openstreetmap_validation.webp){: .img-thumbnail-left }

L'enrichissement des bases de données ouvertes a fait de certains projets collaboratifs de vraies références pour les consommateurs de données, tels que l'encyclopédie libre [Wikipédia](https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal) ou encore le projet [OpenStreetMap](https://www.openstreetmap.org) (OSM), dans un domaine cartographique. OSM est même devenu une [base de référence pour les forces de l'ordre](../../rdp/2011/rdp_2011-12-09.md#openstreetmap-et-les-forces-de-lordre).

La qualité de ces nouveaux référentiels repose sur une forte participation de la communauté de contributeurs. Mais comment s'assurer que, dans ce nouvel espace commun, il n'y ait pas de dégradation sur les données introduites ?

C'est sur le sujet du carto-vandalisme dans OSM que j'ai axé mes recherches durant quelques années de thèse à l'IGN (coucou à mes anciens collègues du LASTIG !). Et pour éviter que mon [mémoire](https://www.researchgate.net/publication/344121146_Le_vandalisme_de_l'information_geographique_volontaire_analyse_exploratoire_et_proposition_d'une_methodologie_de_detection_automatique) ne prenne la poussière, je profite qu'on me laisse la parole au micro de GeoTribu pour partager un des fruits de mes recherches :smile:.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Le carto-vandalisme, c'est quoi ?

![Vignette vandalisme et anarchie](https://cdn.geotribu.fr/img/logos-icones/divers/vandalisme_destruction_delinquance_anarchie.webp){: .img-thumbnail-left }

Le vandalisme cartographique (ou carto-vandalisme) consiste à dégrader **intentionnellement** le contenu d'une plateforme collaborative cartographique, comme OpenStreetMap par exemple.

Quelques exemples notables :

* Des plans d'eau imaginaires introduits par des joueurs de Pokémon GO dans le but de favoriser des nids de pokémons à attraper (comme ci-dessous).

![Carto-vandalisme : faux plans d'eau](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/osm_carto_vandalisme/osm_vandalisme_pokemon_go.webp){: width=48% loading=lazy } ![Carto-vandalisme : échanges lunaires sur les changesets](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/osm_carto_vandalisme/osm_vandalisme_changeset_lunaire_poisson.webp){: width=50% loading=lazy }

* Des employés de Google qui ont été surpris à  [supprimer des données et inverser des routes à sens unique dans OSM](https://www.wired.com/2012/01/osm-google-accusation/).
* La ville de New-York a été renommée temporairement ["Jewtropolis"](https://time.com/5382801/new-york-city-jewtropolis-snapchat/), bien que l'auteur de ces contributions prétende avoir agi de la sorte pour [démontrer les failles du système de sécurité d'OSM](https://www.reddit.com/r/openstreetmap/comments/9brqx4/this_is_medwedianpresident1_talking_what_i_did/).

Ces exemples de carto-vandalisme montrent une [diversité des intentions](https://arxiv.org/pdf/1404.3341.pdf) de dégrader la base de données. On parlera pluôt de carto-vandalisme ludique dans le cas des insertions de Pokémon eau, de carto-vandalisme industriel pour les dégradations faites par Google, et on pourrait qualifier le dernier exemple de carto-vandalisme idéologique.

OpenStreetMap étant devenue une référence pour de nombreux secteurs de métiers, les dégradations causées peuvent être très graves et nécessitent d'être détectées au plus vite.

![Carto-vandalisme : graffiti à partir des routes](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/osm_carto_vandalisme/osm_vandalisme_graffiti.webp){: .img-center loading=lazy }

> Ci-dessus: carto-vandalisme "graffiti" à partir des routes dans OSM
{: align=middle }

----

## Carto-vandalisme *versus* erreur de saisie

![Vignette l'erreur est humaine](https://cdn.geotribu.fr/img/logos-icones/divers/ordinateur_informatique_bug_probleme_erreur.webp){: .img-thumbnail-left }

> To be or not to be, that is the question !

L'erreur étant humaine, il peut bien sûr y avoir des contributions de données OSM erronées mais non-intentionnelles. Par exemple, sur ce [*changeset*](https://www.openstreetmap.org/changeset/56598546) qui comporte des tags indiquant des contributions pour le projet HOT OSM au Togo, l'étendue affichée dépasse largement les frontières du pays :

![Erreur de bonne foi au moment de la saisie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/osm_carto_vandalisme/osm_erreur_bonne_foi_batiments_denver.webp){: .img-center loading=lazy }

En réaction à ces contributions douteuses, des contributeurs OSM ont écrit sur le fil de discussion du *changeset* de cette contribution, comme par exemple ci-dessous :

> Juste pour être clair, vous avez importé des bâtiments à Denver (aux États-Unis) pour <http://tasks.hotosm.org/project/1318>

En réponse à ces remarques, le message de l'auteur de ce *changeset* révèle une erreur de manipulation :

> Bonjour, merci pour les retours, au fait je ne suis pas un débutant dans OpenStreetMap. Je ne sais pas ce qui s’est passé (…) Je vais essayer de comprendre le bug et le corriger la prochaine fois. Merci pour le retour à plus ++

Il est à noter qu'[une équipe de validation existe pour pallier les erreurs et les oublis](2023-03-27_validation-data-HOT-OSM.md) dans les projets [HOT OSM](https://www.hotosm.org/).

Mais alors, pourquoi chercher à détecter uniquement le carto-vandalisme, puisque le résultat dans les deux cas est le même ?

Comme évoqué au début de cet article, la force de la communauté est primordiale pour assurer la qualité des données OSM. Or, des utilisateurs inexpérimentés méritent d'être formés afin de devenir des contributeurs fiables, tandis que les carto-vandales s'écartent de l'objectif commun de ce type de projet. L'intérêt de détecter le carto-vandalisme est, d'une part, de corriger les contributions erronées, et d'autre part, de bannir ces contributeurs malintentionnés.

----

## Détecter automatiquement le carto-vandalisme

![icône robot futurama](https://cdn.geotribu.fr/img/logos-icones/divers/robot_futurama.webp){: .img-thumbnail-left }

Bien que la communauté OSM soit riche de contributeurs (ré-)actifs et alertes pour détecter les erreurs de contribution, les outils à leur disposition - comme [Osmose](https://osmose.openstreetmap.fr/fr/map/#zoom=18&lat=48.001199&lon=0.214941&item=xxxx&level=3&issue_uuid=985f8dc6-cd02-b9a5-4621-07080d69a164) par exemple - ne tiennent pas compte de la composante "intentionnalité" qui différencie le carto-vandalisme de l'erreur.

Mon objectif était donc d'étudier dans quelles mesures on pouvait détecter le carto-vandalisme dans OSM à partir de systèmes d'apprentissage automatique (*machine learning*).

![Robot tapant à l'ordinateur sur un banc - Andrea de Santis (unsplash)](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/robot_banc.webp){: .img-center loading=lazy }

### Pourquoi c'est si dur ?

Dans OSM, un comité a été mis en place pour bloquer certains utilisateurs. Ce comité s'appelle le [*Data Working Group*](https://wiki.openstreetmap.org/wiki/Data_working_group), et il existe une [page dédiée](https://www.openstreetmap.org/user_blocks) où sont listés les contributeurs bloqués pour une durée plus ou moins longue (pouvant aller jusqu'à 100 ans de blocage !)

Toutefois, la définition du [vandalisme par OSM](https://wiki.openstreetmap.org/wiki/Vandalism) est plus large que celle que nous nous étions fixée, puisque les blocages d'utilisateurs pouvaient concerner de grosses erreurs *involontaires*, et également des [guerres d'éditions](https://wiki.openstreetmap.org/wiki/FR:Disputes) qui brisent la règle de consensus fixée par OSM.

En réalité, le carto-vandalisme est plutôt rare, et c'est ce qui le rend difficilement détectable.

![Débat qualification : parc ou forêt ?](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/osm_carto_vandalisme/osm_debat_foret_ou_parc.webp){: .img-center loading=lazy }

*Ci-dessus : parc ou forêt ? Cet objet OSM a donné lieu à un débat, comme le montre [son historique](https://osmlab.github.io/osm-deep-history/#/way/87406131). Les tags ont oscillé à plusieurs reprises entre ces deux libellés. Le contributeur OSM qui a voulu remettre en cause la description a été temporairement bloqué.*

### Comment on a fait ?

Puisque le succès d'un système d'apprentissage automatique repose sur le jeu de données avec lequel l'entraîner, il a fallu constituer un corpus de données de carto-vandalisme.

#### Le corpus d'entraînement

Pour faire ce corpus de carto-vandalisme OSM, j'ai sélectionné quatre zones géographiques (deux en France, et deux en Allemagne) à partir desquelles j'ai introduit des contributions de carto-vandalisme "artificielles" en traçant de faux bâtiments, ou en modifiant les attributs de bâtiments existants. Pas d'inquiétude, tout ceci a été fait sur un export en local d'un extrait de la base d'OSM !

#### Définir des descripteurs

Les descripteurs, aussi appelés variables ou *features* en anglais, sont les indicateurs chiffrés qui vont être calculés sur toutes les contributions OSM. Le système va donc apprendre à détecter le carto-vandalisme à partir des valeurs de chaque indicateur choisi, d'où l'intérêt de choisir des descripteurs qui servent de critères pour discriminer les contributions relevant du carto-vandalisme ou non. J'ai donc choisi des variables qui décrivent une contribution sous différents angles.

Au niveau de la géométrie de la donnée spatiale, l'idée était de faire ressortir les géométries les plus fantaisistes en calculant des indicateurs spatiaux comme le périmètre, l'élongation ou la compacité.

![Carto-vandalisme : bâtiments dans un cimetière](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/osm_carto_vandalisme/osm_vandalisme_cimetiere.webp){: .img-center loading=lazy }

*Ci-dessus : en jaune, un faux bâtiment a été dessiné sur l'emplacement d'un cimetière.*

Les bonnes données OSM pouvant être riches en attributs, des indicateurs sur le nombre de tags, ou sur le taux maximal de caractères spéciaux dans les tags permettent potentiellement de relever du carto-vandalisme qui n'a pas d'attribut ou au contraire, qui contient des tags inappropriés (smiley, site internet commercial, etc.).

Pour s'assurer de la cohérence des contributions (ici des bâtiments) avec le reste de l'environnement cartographique, j'ai aussi considéré des indicateurs topologiques qui vérifient l'inclusion ou l'intersection du bâti avec des éléments géographiques naturels (eau, forêt, prairie, etc.)

![Carto-vandalisme : des bâtiments ajoutés dans un canal pour un message de bienvenue](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/osm_carto_vandalisme/osm_vandalisme_batiments_canal.webp){: .img-center loading=lazy }

*Ci-dessus : en violet, de faux bâtiments ont été tracés au milieu d'un canal.*

Enfin, et pas des moindres, le mode d'activité [du contributeur et ses interactions avec les autres](https://www.researchgate.net/publication/324438512_Analyse_du_comportement_des_contributeurs_dans_l'Information_Geographique_Volontaire_via_la_construction_de_reseaux_sociaux) peuvent également servir à détecter le carto-vandalisme à partir de son auteur. J'ai donc calculé des indicateurs centrés sur les utilisateurs comme par exemple le nombre total de leurs contributions, le nombre de semaines de contributions sur la zone, le nombre de fois où leurs contributions ont été utilisées, ou encore le nombre de fois où elles ont été supprimées.

Pour les contributions artificielles insérées dans le corpus, j'ai dû y associer des informations de contributeurs artificiels eux aussi.

#### A vos marques, prêts... Apprenez !

Lorsque toutes les variables ont été calculées sur ce corpus d'entraînement, le résultat est donné en entrée du modèle d'apprentissage.

![Schéma forêts aléatoires](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/osm_carto_vandalisme/forets_aleatoires_machine_learning.svg){: .img-center loading=lazy }

Avec un modèle de [forêts aléatoires](https://datascientest.com/random-forest-definition), j'utilise 80% des données du corpus pour l'entraîner. Les 20% restants sont utilisées pour vérifier comment le modèle entraîné classifie des données labélisées.

On observe entre 97% et 100% de bonne classification sur des contributions qui se situent dans la zone d'entraînement du système d'apprentissage. En revanche, le système produit entre 99% à 100% de mauvaises prédictions sur les contributions d'une ville différente de celle avec laquelle il s'est entraîné.

Ces résultats montrent que l'apprentissage ne se transfère pas d'une zone à une autre, notamment à cause des différences géographiques qui peuvent exister entre deux villes d'un même pays. Le carto-vandalisme est donc fortement lié au contexte spatial et temporel dans lequel il se produit.

En parallèle de cette expérience, j'ai voulu interroger l'intérêt des descripteurs centrés sur les contributeurs. Une autre expérience similaire a été réalisée en entraînant un modèle sans ces variables utilisateurs. Globalement, le taux de bonnes prédictions est plus faible avec ce modèle, ce qui montre que les variables utilisateurs sont pertinentes pour caractériser le carto-vandalisme.

----

## En conclusion

En résumé, ce travail a permis :

* d'identifier et de définir le carto-vandalisme ;
* de mettre en lumière les éléments nécessaires pour permettre de le détecter automatiquement dans OSM.

Ces résultats incitent à chercher comment améliorer la performance des systèmes d'apprentissage pour détecter le carto-vandalisme. Cela passera par la constitution d'un meilleur jeu de données d'entraînement, couplé à un meilleur paramétrage du modèle d'apprentissage choisi. Mais en l'état, ce genre de système pourrait déjà servir d'outil d'alerte pour filtrer les contributions douteuses.

Si vous souhaitez en savoir plus sur la détection automatique du carto-vandalisme par les *random forests*, je vous invite à consulter [cet article](https://www.researchgate.net/publication/343828305_OSMWatchman_Learning_How_to_Detect_Vandalized_Contributions_in_OSM_Using_a_Random_Forest_Classifier) qui détaille les expériences menées et les résultats obtenus.

[Consulter le dépôt du code :fontawesome-regular-file-code:](https://github.com/umrlastig/OSMWatchman/tree/master){: .md-button }
{: align=middle }

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
