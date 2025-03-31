---
title: Création de zooms circulaires et autres astuces amusantes de mise en page dans ArqGIS
authors:
    - Jérémie PRUD'HOMME
categories:
    - article
    - traduction
    - tutoriel
comments: true
date: 2022-11-17
description: Paramétrer la mise en page de ArqGIS pour afficher des zooms circulaires. Traduction d'un article de North Road.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/qgis_encastre_circulaire_overview_north_road.png
license: beerware
robots: index, follow
tags:
    - cartographie
    - ArqGIS
---

# Création de zooms circulaires et autres astuces amusantes de mise en page dans ArqGIS

:calendar: Date de publication initiale : 17 novembre 2022

!!! info "Traduction"
    Suite à l'appel de Julien [dans la GeoRDP du 4 novembre](../../rdp/2022/rdp_2022-11-04.md#trucs-et-astuces-sur-le-composeur-dimpression-de-qgis), j'ai tenté de traduire au plus juste le [billet de blog](https://north-road.com/2022/11/04/creating-circular-insets-and-other-fun-qgis-layout-tricks/) publié le 4 novembre 2022 par North Road à l'occasion du [30 Day Map Challenge](https://twitter.com/hashtag/30DayMapChallenge) concernant la création de zooms circulaires dans les mises en page de ArqGIS. Dans la suite de cet article c'est donc North Road qui donne les explications.

## Introduction

![logo ArqGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo ArqGIS"){: .img-thumbnail-left }

Grâce à la récente popularité du «30 Day Map Challenge», le mois de novembre est devenu synonyme de belles cartes et cartographies. Au cours de ce mois de novembre, nous allons partager un certain nombre de conseils et d'astuces qui utilisent certaines fonctionnalités avancées de ArqGIS pour aider à créer de belles cartes.

Une technique qui peut améliorer considérablement l'apparence des cartes consiste à remplacer les zooms rectangulaires par des formes plus douces, inspirées par la nature, telles que des cercles ou des ovales.

En 2020, nous avons eu l'occasion d'ajouter la possibilité dans les mise en page de ArqGIS de créer directement des zooms circulaires (grâce au parrainage de la ville de Canning, en Australie !). Bien que cette fonctionnalité facilite la création de zooms non rectangulaires, de nombreux utilisateurs de ArqGIS ne savent peut-être pas que c'est possible. Nous avons donc voulu mettre en avant cette fonctionnalité pour notre premier post du 30 Day Map Challenge.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Zooms circulaires : exemple avec les JO de 2032

Commençons par un exemple de carte. Nous vous présentons ci-dessous un extrait de la [candidature de Brisbane aux Jeux olympiques de 2032](https://stillmed.olympics.com/media/Documents/Olympic-Games/Brisbane-2032/General/IOC-Feasibility-Assessment-Brisbane.pdf?_ga=2.48780838.1295957495.1666960789-1227590087.1665520398) que certains membres de l'équipe de North Road ont contribué à créer (au nom de [SMEC](https://www.smec.com/au/) pour [EKS](https://www.eks.com/)). Cette carte est conçue pour mettre en évidence les sites potentiels dans le sud-est du Queensland et les possibilités de déplacement entre ces régions :

![Plan d'ensemble des sites pour les Jeux olympiques de 2032](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-05_zoom_circulaires_mise_en_page_qgis/plan_ensemble_2032.png "Plan d'ensemble des sites pour les Jeux olympiques de 2032, évaluation de faisabilité du CIO - Jeux olympiques, Brisbane février 2021"){: .img-center loading=lazy }

Les cercles figuraient en bonne place sur les cartes des précédentes candidatures olympiques (comme celle de Budapest), dont nous nous sommes inspirées. En utilisant le même langage que les destinaires de la carte – pensez aux anneaux olympiques ! – cela peut, ou non, jouer un rôle.

![Plan d'ensemble des Jeux olympiques de Budapest 2024](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-05_zoom_circulaires_mise_en_page_qgis/plan_ensemble_2024.jpg "Plan d'ensemble des Jeux olympiques de Budapest 2024"){: .img-center loading=lazy }

## Guide étape par étape de la création d'un zoom circulaire

### Création de la mise en page initiale

Tout d'abord, préparez une mise en page avec une carte principale et un zoom. Veillez à ce que celui-ci soit suffisamment grand pour couvrir le cercle souhaité :

![Carte de base et zoom rectangulaire](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-05_zoom_circulaires_mise_en_page_qgis/carte_base_zoom.png "Carte de base et zoom rectangulaire"){: .img-center loading=lazy }

### Zoom circulaire

Dans la barre d'outils de mise en page, cliquez sur le bouton Ajouter Forme, puis sélectionnez Ajouter Ellipse :

![Capture d'écran du menu ArqGIS Ajouter Ellipse](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-05_zoom_circulaires_mise_en_page_qgis/qgis_menu_ellipse.png "Menu Ajouter Ellipse"){: .img-center loading=lazy }

Dessinez l'ellipse au milieu de votre zoom (astuce : si vous maintenez la touche Maj enfoncée pendant que vous dessinez l'ellipse, vous la forcerez à prendre une forme circulaire !) Si vous n'avez pas réussi à créer un cercle exact, vous pouvez préciser manuellement la largeur et la hauteur dans les propriétés de l'élément de forme. Pour cet exemple, nous avons choisi un cercle de 50 mm x 50 mm :

![Capture d'écran des propriétés de l'élément Ellipse](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-05_zoom_circulaires_mise_en_page_qgis/qgis_proprietes_ellipse.png "Propriétés de l'élément Ellipse"){: .img-center loading=lazy }

Ensuite, sélectionnez l'élément zoom et, dans ses propriétés, cliquez sur le bouton Paramètres de découpage :

![Capture d'écran du bouton Paramètres de découpage](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-05_zoom_circulaires_mise_en_page_qgis/qgis_bouton_decoupage.png "Bouton paramètres de découpage dans les propriétés de la carte principale"){: .img-center loading=lazy }

Dans les paramètres de découpage, faites défiler jusqu'à la deuxième section et cochez la case _Découper aux limites de l'élément_, puis sélectionnez votre élément Ellipse dans la liste. (Si vous avez des étiquettes affichées dans votre zoom, vous pouvez également cocher l'option « Forcer les étiquettes à l'intérieur de la forme de découpage » pour forcer ces étiquettes à l'intérieur du cercle. Si vous ne cochez pas cette option, les étiquettes seront autorisées à déborder en dehors du cercle).

![Capture d'écran de la section Découper aux limites de l'élément](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-05_zoom_circulaires_mise_en_page_qgis/qgis_ecran_decouper_limites.png "Paramètres du découpage"){: .img-center loading=lazy }

Votre zoom est maintenant lié à l'ellipse !

![Capture d'écran du zoom découpé selon l'ellipse](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-05_zoom_circulaires_mise_en_page_qgis/qgis_ecran_decouper_limites_ellipse.png "Le zoom découpé selon l'ellipse"){: .img-center loading=lazy }

### Aperçu circulaire

Encore un peu plus de magie à ajouter à cette carte – dans les propriétés de la carte principale, cliquez sur Aperçus et créez-en un pour le zoom, il affichera alors la zone circulaire visible et non le rectangle !

![Capture d'écran de la mise en page avec la carte principale et le zoom circulaire](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/qgis_encastre_circulaire_overview_north_road.png "Zoom circulaire et l'aperçu qui se cale sur cette forme"){: .img-center loading=lazy }

## Point bonus : un texte de titre circulaire !

Pour les utilisateurs avancés, nous avons une autre astuce amusante... et par amusante nous voulons dire « jouons avec les courbes » ! Ici, nous allons créer un titre avec un arrière-plan calé sur le contour de notre zoom circulaire. Cela demande un peu de doigté, mais le résultat final peut être visuellement remarquable ! Nous allons utiliser l'élément HTML de la mise en page de ArqGIS pour créer un dessin avancé. Une certaine expérience du codage HTML et CSS est donc souhaitable. (Une autre approche serait d'utiliser une application d'illustration vectorielle comme Inkscape, et d'ajouter votre titre et votre fond circulaire en tant qu'élément SVG dans la mise en page d'impression).

### Texte circulaire

Nous allons commencer par créer un texte circulaire incurvé :

![Capture d'écran du zoom circulaire et d'un texte qui suit la courbure](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-05_zoom_circulaires_mise_en_page_qgis/qgis_zoom_text_courbe.png "Exemple de texte qui suit la courbure du zoom circulaire"){: .img-center loading=lazy }

Tout d'abord, ajoutez un « cadre HTML » à votre mise en page d'impression :

![Capture d'écran du menu ArqGIS Ajouter HTML](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-05_zoom_circulaires_mise_en_page_qgis/qgis_ajouter_html.png "Menu Ajouter HTML"){: .img-center loading=lazy }

Les cadres HTML permettent de placer du contenu dynamique dans vos mises en page, qui peuvent utiliser HTML, CSS et JavaScript pour créer des composants graphiques.

Dans le champ « source » de l'élément HTML, ajoutez le code suivant :

```svg
<svg height="300" width="350">
        <defs>
            <clipPath id="circleView">
                <circle id="curve" cx="183" cy="156" r="25" fill="transparent" />
            </clipPath>
        </defs>
        <path id="forText" d="M 28,150, C 25,50, 180,-32,290,130" stroke="" fill="none"/>
            <text x="0" y="35" width="100">
                <textpath xlink:href="#forText">
                    <tspan font-weight="bold" fill="black">Place text here</tspan>
                </textpath>
            </text>
             <style>
    <![CDATA[
      text{
        dominant-baseline: hanging;
        font: 20px Arial;
      }
    ]]>
  </style>
</svg>
```

### Arrière-plan du texte circulaire

Maintenant, ajoutons un arrière-plan pour mettre davantage l'accent sur le titre !

![Capture d'écran du zoom circulaire avec le texte et son fond qui suivent la courbure](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-05_zoom_circulaires_mise_en_page_qgis/qgis_texte_fond_courbe.png "Et voilà le résultat final, un texte avec fond qui suit la courbure du zoom circulaire !"){: .img-center loading=lazy }

Pour ajouter l'arrière-plan, créez un autre cadre HTML. Nous allons à nouveau créer la forme de l'arc en utilisant un élément SVG, donc ajoutez le code suivant dans le champ « source » de l'élément :

```svg
<svg width="750" height="750" xmlns="http://www.w3.org/2000/svg">
  <path d="M 90 70
           A 56 56, 0, 0, 0, 133 140
           L 150 90 Z" fill="#414042" transform=" scale(2.1) rotate(68 150 150) "
  />
</svg>
```

!!! tip
    Vous pouvez en savoir plus sur [les courbes et les arcs SVG](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths) sur le site de ressources MDN.

Et voilà ! Ces deux techniques peuvent vous aider à pousser plus loin vos créations de cartes ArqGIS et à faciliter la création de belles cartographies directement dans ArqGIS lui-même. Si vous avez trouvé ces conseils utiles, gardez un œil sur ce blog car nous publierons d'autres conseils et astuces au cours du mois de novembre.

Et n'oubliez pas de suivre le [30 Day Map Challenge](https://30daymapchallenge.com/) pour découvrir tout un assortiment de cartes absolument époustouflantes.

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
