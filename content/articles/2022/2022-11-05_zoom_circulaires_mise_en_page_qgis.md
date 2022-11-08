---
title: "Zooms circulaires dans une mise en page QGIS"
authors:
    - Jérémie PRUD'HOMME
categories:
    - article
    - tutoriel
date: "2022-11-05 13:30"
description: "Paramétrer la mise en page de QGIS pour afficher des zooms circulaires."
image: "https://pbs.twimg.com/media/FgsgdNraEAAukhn?format=png&name=small"
license: default
robots: index, follow
tags:
    - QGIS
---

# Zooms circulaires dans une mise en page QGIS

:calendar: Date de publication initiale : 8 novembre 2022

## Introduction

!!! info "Traduction"
    Suite à l'appel de Julien [dans la GeoRDP du 4 novembre](/rdp/2022/rdp_2022-11-04/#trucs-et-astuces-sur-le-composeur-dimpression-de-qgis), j'ai tenté de traduire au plus juste le [billet de blog](https://north-road.com/2022/11/04/creating-circular-insets-and-other-fun-qgis-layout-tricks/) publié le 4 novembre 2022 par North Road à l'occasion du [30 Day Map Challenge](https://twitter.com/hashtag/30DayMapChallenge) concernant la création de zooms circulaires dans les mises en page de QGIS.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Création de zooms circulaires et autres astuces amusantes de mise en page dans QGIS

Grâce à la récente popularité du «30 Day Map Challenge», le mois de novembre est devenu synonyme de belles cartes et cartographies.  Au cours de ce mois de novembre, nous allons partager un certain nombre de conseils et d'astuces qui utilisent certaines fonctionnalités avancées de QGIS pour aider à créer de belles cartes.

Une technique qui peut améliorer considérablement l'apparence des cartes consiste à remplacer les zooms rectangulaires par des formes plus organiques, telles que des cercles ou des ovales.

En 2020, nous avons eu l'occasion d'ajouter la possibilité dans les mise en page de QGIS de créer directement des zooms circulaires (grâce au parrainage de la ville de Canning, en Australie !). Bien que cette fonctionnalité facilite la création de zooms non rectangulaires, de nombreux utilisateurs de QGIS ne savent peut-être pas que c'est possible. Nous avons donc voulu mettre en avant cette fonctionnalité pour notre premier post du 30 Day Map Challenge.

Commençons par un exemple de carte. Nous vous présentons ci-dessous un extrait de la [candidature de Brisbane aux Jeux olympiques de 2032](https://stillmed.olympics.com/media/Documents/Olympic-Games/Brisbane-2032/General/IOC-Feasibility-Assessment-Brisbane.pdf?_ga=2.48780838.1295957495.1666960789-1227590087.1665520398) que certains membres de l'équipe de North Road ont contribué à créer (au nom de [SMEC](https://www.smec.com/au/) pour [EKS](https://www.eks.com/)). Cette carte est conçue pour mettre en évidence les sites potentiels dans le sud-est du Queensland et les possibilités de déplacement entre ces régions :

![Plan d'ensemble des sites pour les Jeux olympiques de 2032](https://user-images.githubusercontent.com/9571164/200112536-e938f1aa-e4fc-4959-8952-e6e4e56f4ebf.png "Plan d'ensemble des sites pour les Jeux olympiques de 2032, évaluation de faisabilité du CIO - Jeux olympiques, Brisbane février 2021"){: .img-center loading=lazy }

Les cercles figuraient en bonne place sur les cartes des précédentes candidatures olympiques (comme celle de Budapest), dont nous nous sommes inspirés. En utilisant le même langage que les destinaires de la carte – pensez aux anneaux olympiques ! – cela peut, ou non, jouer un rôle.

![Plan d'ensemble des Jeux olympiques de Budapest 2024](https://user-images.githubusercontent.com/9571164/200112912-29ad96b1-adc0-476b-91cd-c324b1c39293.jpg "Plan d'ensemble des Jeux olympiques de Budapest 2024"){: .img-center loading=lazy }

### Guide étape par étape de la création d'un zoom circulaire

Tout d'abord, préparez une mise en page avec une carte principale et un zoom. Veillez à ce que celui-ci soit suffisamment grand pour couvrir le cercle souhaité :

![Carte de base et zoom rectangulaire](https://user-images.githubusercontent.com/9571164/200113058-5c6d24a9-8297-4181-b771-9bdbe3314056.png "Carte de base et zoom rectangulaire"){: .img-center loading=lazy }

Dans la barre d'outils de mise en page, cliquez sur le bouton Ajouter Forme, puis sélectionnez Ajouter Ellipse :

![Capture d'écran du menu QGIS Ajouter Ellipse](https://user-images.githubusercontent.com/9571164/200113152-5de641be-2847-4e7f-bce0-b141daa264e8.PNG "Menu Ajouter Ellipse"){: .img-center loading=lazy }

Dessinez l'ellipse au milieu de votre zoom (astuce : si vous maintenez la touche Maj enfoncée pendant que vous dessinez l'ellipse, vous la forcerez à prendre une forme circulaire !) Si vous n'avez pas réussi à créer un cercle exact, vous pouvez préciser manuellement la largeur et la hauteur dans les propriétés de l'élément de forme. Pour cet exemple, nous avons choisi un cercle de 50 mm x 50 mm :

![Capture d'écran des propriétés de l'élément Ellipse](https://user-images.githubusercontent.com/9571164/200113336-52576afd-14b0-4303-827c-4e8927760546.png "Propriétés de l'élément Ellipse"){: .img-center loading=lazy }

Ensuite, sélectionnez l'élément zoom et, dans ses propriétés, cliquez sur le bouton Paramètres de découpage :

![Capture d'écran du bouton Paramètres de découpage](https://user-images.githubusercontent.com/9571164/200113390-5949b4ae-abad-4832-9a3c-b50f712889ed.PNG "Bouton paramètres de découpage dans les propriétés de la carte principale"){: .img-center loading=lazy }

Dans les paramètres de découpage, faites défiler jusqu'à la deuxième section et cochez la case _Découper aux limites de l'élément_, puis sélectionnez votre élément Ellipse dans la liste. (Si vous avez des étiquettes affichées dans votre zoom, vous pouvez également cocher l'option « Forcer les étiquettes à l'intérieur de la forme de découpage » pour forcer ces étiquettes à l'intérieur du cercle. Si vous ne cochez pas cette option, les étiquettes seront autorisées à déborder en dehors du cercle).

![Capture d'écran de la section Découper aux limites de l'élément](https://user-images.githubusercontent.com/9571164/200113587-39953f47-239b-4fd4-ae8d-623bc8e1eecb.PNG "Paramètres du découpage"){: .img-center loading=lazy }

Votre zoom est maintenant lié à l'ellipse !

![Capture d'écran du zoom découpé selon l'ellipse](https://user-images.githubusercontent.com/9571164/200113591-1f5723b6-da57-4b96-9950-90534a2c3c87.png "Le zoom découpé selon l'ellipse"){: .img-center loading=lazy }

Encore un peu plus de magie à ajouter à cette carte – dans les propriétés de la carte principale, cliquez sur Aperçus et créez-en un pour le zoom, il affichera alors la zone circulaire visible et non le rectangle !

![Capture d'écran de la mise en page avec la carte principale et le zoom circulaire](https://user-images.githubusercontent.com/9571164/200113850-b9d8127f-f26c-4714-920b-9feec0ceced8.png "Zoom circulaire et l'aperçu qui se cale sur cette forme"){: .img-center loading=lazy }

### Point bonus : un texte de titre circulaire !

Pour les utilisateurs avancés, nous avons une autre astuce amusante... et par amusante nous voulons dire « jouons avec les radians » ! Ici, nous allons créer un titre avec un arrière-plan calé sur le contour de notre zoom circulaire. Cela demande un peu de doigté, mais le résultat final peut être visuellement remarquable ! Nous allons utiliser l'élément HTML de la mise en page de QGIS pour créer un dessin avancé. Une certaine expérience du codage HTML et CSS est donc souhaitable. (Une autre approche serait d'utiliser une application d'illustration vectorielle comme Inkscape, et d'ajouter votre titre et votre fond circulaire en tant qu'élément SVG dans la mise en page d'impression).

Nous allons commencer par créer un texte circulaire incurvé :

![Capture d'écran du zoom circulaire et d'un texte qui suit la courbure](https://user-images.githubusercontent.com/9571164/200114170-ba31b305-b0cd-4890-a5c4-97be30cfce2e.png "Exemple de texte qui suit la courbure du zoom circulaire"){: .img-center loading=lazy }

Tout d'abord, ajoutez un « cadre HTML » à votre mise en page d'impression :

![Capture d'écran du menu QGIS Ajouter HTML](https://user-images.githubusercontent.com/9571164/200114203-804421df-d396-4893-9f10-6ae79660f7ee.PNG "Menu Ajouter HTML"){: .img-center loading=lazy }

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

Maintenant, ajoutons un arrière-plan pour mettre davantage l'accent sur le titre !

![Capture d'écran du zoom circulaire avec le texte et son fond qui suivent la courbure](https://user-images.githubusercontent.com/9571164/200114566-72898388-1ba2-4eea-b693-e8fcd6040e2f.png "Et voilà le résultat final, un texte avec fond qui suit la courbure du zoom circulaire !"){: .img-center loading=lazy }

Pour ajouter l'arrière-plan, créez un autre cadre HTML. Nous allons à nouveau créer la forme de l'arc en utilisant un élément SVG, donc ajoutez le code suivant dans le champ « source » de l'élément :

```svg
<svg width="750" height="750" xmlns="http://www.w3.org/2000/svg">
  <path d="M 90 70
           A 56 56, 0, 0, 0, 133 140
           L 150 90 Z" fill="#414042" transform=" scale(2.1) rotate(68 150 150) " />/>
</svg>
```

!!! tip
    Vous pouvez en savoir plus sur [les courbes et les arcs SVG](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths) sur le site de ressources MDN.

Et voilà ! Ces deux techniques peuvent vous aider à pousser plus loin vos créations de cartes QGIS et à faciliter la création de belles cartographies directement dans QGIS lui-même. Si vous avez trouvé ces conseils utiles, gardez un œil sur ce blog car nous publierons d'autres conseils et astuces au cours du mois de novembre. Et n'oubliez pas de suivre le [30 Day Map Challenge](https://30daymapchallenge.com/) pour découvrir tout un assortiment de cartes absolument époustouflantes.

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jpru.md"

{% include "licenses/default.md" %}
