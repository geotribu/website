---
title: Comment bien préparer un date avec QGIS et l’analyse spatiale ?
subtitle: L'amour est dans le précarté
authors:
    - Valentin Buira
categories:
    - article
comments: true
date: 2026-02-14
description: "Comment bien préparer un date avec QGIS et l’analyse spatiale ?"
icon: material/heart-cog-outline
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/preparer-un-date-avec-qgis/bravo_les_lesbiennes.webp
license: beerware
robots: index, follow
tags:
    - modèles
    - modélisation
    - OpenStreetMap
    - parodie
    - QGIS
    - QuickOSM
    - urbanisme
---

# Comment bien préparer un date avec QGIS et l’analyse spatiale ?

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Introduction

Je vous pose le décor.

Après une rude journée à *géomatiquer* vous ouvrez votre application de rencontres [préférée](https://play.google.com/store/search?q=Rencontre&c=apps&hl=fr).

Et là, par on ne sait quel miracle vous avez un *match*. Encore plus incroyable, vous ne vous ghostez pas mutuellement, et finalement la discussion se passe bien.

Arrive alors le moment fatidique où vous convenez d’un date. Avec la grande question :

> "T’as envie d’aller où ?”.

Votre âme de géomaticien·ne en vous s’éveille, et se dit, ça doit pas être si compliqué de trouver tous les cafés entre vous et votre *crush*. Après tout, tout ce dont vous avez besoin pour ça c’est de deux coordonnées, le reste vous pouvez le déduire.

Voilà c’est parti, peut-être êtes-vous inconscient·e ? Ou peut-être êtes-vous juste *étrange* ? Mais, vous vous partagez mutuellement vos localisations.

Cet article est une adaptation méthodologique tirée de faits réels (ou non).

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Méthodologie

Pour cet article, nous allons prendre un exemple fictif, dans lequel vous habitez rue Ada Lovelace à Paris, et où votre *match* habite allée Marie Laurent. Une chance inouie si j’ose dire, si on prends l'exemple sur Nantes [seul 14% des rues ont un nom de femme en France](https://asmn.univ-nantes.fr/index.php?id=795), mais cette proportion se retrouve ailleurs en France, même si Paris figure parmi les bons élèves.

Notre objectif final sera donc de trouver tous les cafés et bars entre ces deux adresses.

### Connect the dots

Pour commencer, dans QGIS, nous allons créer une couche ligne, pour y tracer une ligne servant à relier vos deux positions. Dans notre exemple parisien nous obtenons quelque chose comme ça :

![étape 1 créer une ligne entre vos positions](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/preparer-un-date-avec-qgis/step_1.webp){: .img-center loading=lazy  width=85% }

### Changer de dimension pour mieux chercher

Ça n'a pas de sens de chercher des cafés (c’est-à-dire des points) sur une ligne, cela pourrait cependant être plus intéressant concernant un polygone. Nous allons donc utiliser un **tampon** (buffer) autour de notre ligne créée à l’étape précédente pour générer un polygone.

J’ai choisi par défaut de faire un tampon de 250 mètres autour de notre ligne, mais vous pouvez augmenter ou baisser cette valeur en fonction de la distance que vous êtes prêts à parcourir autour de la ligne initiale.

Nous avons donc maintenant quelque chose qui ressemble désormais à ça :

![Etape 2 tampon(buffer) autour de la ligne](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/preparer-un-date-avec-qgis/step_2.webp){: .img-center loading=lazy width=85%}

Ce tampon sera notre "zone de recherche" pour les cafés et bars.

### QuickOSM à la rescousse

Pour ce faire, nous allons partir des données d’OpenStreetMap, qui ont l’avantage d’être disponibles mondialement, et qui sont souvent plus complètes que les données institutionnelles grâce au modèle collaboratif d’OpenStreetMap, similaire à celui de Wikipedia. Et enfin la communauté QGIS à créé des outils pour exploiter et extraire les données d’OpenStreetMap, notamment le plugin QuickOSM.

QuickOSM est un plugin de QGIS qui permet de télécharger facilement des données depuis OpenStreetMap directement dans QGIS.

OSM utilise un modèle de données "clé"="valeur" appelé *tags*. À chaque objet dans OpenStreetMap sont associés plusieurs *tags* que l’on peut ensuite venir interroger comme base de données.  

Dans notre exemple, nous allons rechercher les cafés et les bars. Mais vous pouvez tout à fait customiser votre requête à cette étape, la liste des tags et clés est assez [ex](https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dcinema)[haus](https://wiki.openstreetmap.org/wiki/Tag:amenity%3Dswingerclub)[ti](https://wiki.openstreetmap.org/wiki/Tag:shop%3Derotic)[ve](https://wiki.openstreetmap.org/wiki/Key:lgbtq).

![Interface de QuickOSM pour query les cafés et les bars](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/preparer-un-date-avec-qgis/quickosm_annotation.webp){: .img-center loading=lazy width=85%}
*Interface de QuickOSM pour requêter OpenStreetMap*
{: align=middle }

QuickOSM fonctionne sur l’étendue de la couche, c'est-à-dire le rectangle qui englobe notre tampon, et non sur la couche en elle-même. Nous nous retrouvons alors avec plus de points que ce nécessaire.

![Etape 3 requeste osm avec QuickOSM](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/preparer-un-date-avec-qgis/step_3.webp){: .img-center loading=lazy width=85%}

Mais pas de panique ! Il ne nous reste qu’à couper (clipper) le résultat de QuickOSM avec notre tampon.

![Etape 4 couper les résultats sur la zone de recherche](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/preparer-un-date-avec-qgis/step_4.webp){: .img-center loading=lazy width=85%}

Et voilà ! Félicitations, vous avez trouvé tous les lieux idéaux pour vos dates. (ou alors une couche vide, s’il n’y a aucun bar ou café entre vous, navré)

## Partager vos fiertés

Bon c’est bien gentil tout ça, mais s' il y a un second date ? Vous allez quand même pas refaire tous ces clics à chaque date ? C’est là qu’intervient le [modeleur graphique de QGIS](https://docs.qgis.org/3.40/fr/docs/user_manual/processing/modeler.html)

### Automatiser votre méthodologie

Le modeleur graphique vous permet de créer des chaînes de traitements, en liant ensemble plusieurs traitements.

Et le mieux dans tout ça ? C’est que vous avez déjà fait la moitié du boulot dans l’étape précédente. Et oui, les géotraitements du modeleur sont ceux de QGIS. Vous n’avez qu’à reprendre votre méthodologie et remettre vos traitements dans l’ordre.

**Et l’autre moitié restante ?**

Il vous faut identifier les éléments qui serviront d'entrées à votre modèle. Ici ce sont votre position et la position de votre *crush* qui serviront pour créer la ligne entre vos positions  dans notre méthodologie.

Ensuite, j’ai dit dans mon paragraphe précédent que les géotraitements sont les mêmes que dans QGIS, et c’est vrai pour la majorité des cas, car les développeur·euses les ont codés pour. Mais on a parfois des mauvaises surprises, et c’est le cas ici pour les traitements de QuickOSM qui ne sont pas exactement les mêmes. Quelques modifications ont donc été nécessaires pour les faire marcher dans le modeleur.

De plus, si les traitements sont  disponibles, d'autres actions manuelles de QGIS sont plus compliquées. Par exemple, créer une couche avec une seule entité s’avère étonnamment compliqué dans le modeleur, et a requis une ligne de SQL.

![le modele finale](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/preparer-un-date-avec-qgis/plan_a_date_final.webp){: .img-center loading=lazy width=85%}

Mais une fois que vous avez fait votre modèle, il est directement intégré aux autres géotraitements de la boîte à outils, et vous pouvez l’utiliser comme n’importe quel géotraitement.

### Mettre votre modèle en ligne sur le hub de QGIS

Maintenant que vous avez fini votre modèle (ou votre [spaghetti](https://pbs.twimg.com/media/EYbqaEaUMAARbja?format=jpg&name=small)). Vous pouvez le partager au reste du monde. C’est d’ailleurs le cas du modèle de cet article ! Vous pouvez dès à présent l’utiliser dans QGIS, grâce à l'extension [QGIS Hub Plugin](https://plugins.qgis.org/plugins/qgis_hub_plugin/) qui permet d'accéder directement dans QGIS aux ressources en ligne sur <hub.qgis.org>.

Je ne reviens pas sur le fonctionnement du ressources hub de QGIS, ni sur les autres méthodes existantes pour partager un modèle. Marc Ducobu en parle déjà mieux que moi sur géotribu [ici](https://geotribu.fr/articles/2025/2025-12-06_partage_modeles_qgis/).

![modele "plan a date" de l'article dans le model hub de QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/preparer-un-date-avec-qgis/model_plan_a_date_in_qgis_hub_plugin.webp){: .img-center loading=lazy width=75%}

## Piste d’améliorations

J’aurais pu arrêter cet article ici, mais à quoi bon faire un mémoire sur la marchabilité en ville si on ne le ressort pas du placard de temps en temps. Donc c’est parti pour soulever l’une des limitations de cet article/méthode.

Depuis le début, notre méthodologie utilise le chemin à vol d’oiseau représenté par une ligne droite comme pour construire le tampon qui sert de “zone de recherche”. Mais si la distance à vol d’oiseau est une bonne approximation, elle ne correspond à la réalité que dans le cas où vous rentrez de votre date sur un petit nuage. Y aller à pied est  en revanche une autre paire de manches.

![Sangoku et Chichi sur le nuage magique](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/preparer-un-date-avec-qgis/goku_chichi_nuage.webp){: .img-center loading=lazy }

*Sangoku et Chichi revenant d’un date circa 1985*  

Si nous reprenons notre exemple de tout à l’heure et que l’on remplace le chemin à vol d’oiseau par le chemin le plus court à pied, nous obtenons alors un résultat très différent.  

![comparaison entre la distance à voil d'oiseau et à pieds](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/preparer-un-date-avec-qgis/piste_amelioration.webp){: .img-center loading=lazy width=85%}

## Conclusion

Voilà, maintenant vous pouvez à la fois préparer vos dates, mais aussi et surtout quand on vous posera la question : “A quoi ça sert QGIS et la géomatique?” vous pouvez répondre à ça : :arrow_up:

PS : L'auteur·ice se dédouane de toute responsabilité en cas d’échec de vos dates.

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
