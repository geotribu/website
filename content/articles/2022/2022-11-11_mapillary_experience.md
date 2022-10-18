---
title: "Contribution Mapillary et retour d'expérience"
authors:
    - Florian Boret
categories:
    - article
    - tutoriel
date: 2022-11-11 14:20
description: "Contribution Mapillary et retour d'expérience"
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/mapillary_logo.jpeg"
license: default
tags:
    - Bash
    - data
    - OGR
    - Mapillary
    - PostGIS
    - PostgreSQL
    - tuiles vectorielles
---

# Contribution Mapillary et retour d'expérience

:calendar: Date de publication initiale : 11 Novembre 2022

## Prérequis

## Intro

![Mapillary](https://cdn.geotribu.fr/img/logos-icones/divers/mapillary.png "Mapillary"){: .img-rdp-news-thumb }

Cet article s'inscrit dans la continuité de mon article que j'avais intitulé [accéder aux données Mapillary et les intégrer dans son SIG](/articles/2022/2022-05-31_donnees_mapillary/). En effet, au moment où celui-ci avait été rédigé, je n'étais pas encore équipé pour réaliser des vues immersives mais c'est maintenant chose faite et je vous propose un retour d'expérience qui je l'espère permettra d'alimenter les discussions sur le sujet.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Le matériel

### Le point de départ

![logo GoPro](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/GoPro.jpg "logo GoPro"){: .img-rdp-news-thumb }

J'interviens dans une petite Communauté de Communes et comme chacun le sait nos finances sont particulièrement contraintes en ces temps d'abstinence! L'idée n'était donc pas de réinventer la poudre mais de s'appuyer sur des solutions éprouvées et mises en places ailleurs. Je suis donc parti sur : 

- une GoPro Max 360° : environ 430 €
- un support triple ventouse Ram Mount (ref. RAP-B-365-224-202AU) : environ 90€
- un adpatateur GoPro à visser : environ 3€

> NOTE : Exemple de Montauban ou de Cartocité et parler aussi de la présentation au SOTM.

[![Configuration initiale](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/config_initiale.jpeg "Configuration initiale"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/config_initiale.jpeg){: data-mediabox="gallery-lightbox" data-title="Configuration initiale" }

### Une erreur qui aurait pu me coûter une GoPro

J'avais acheté un adapteur GoPro en plastique a 3€ pour limiter les coûts mais cette "chinoiserie" a bien failli me coûter la caméra!

En effet, le lendemain de ma première matinée de test, la caméra était posée sur le bureau quand sans action extérieure, la caméra s'est retrouvée sans prévenir sur le sol, gloups! L'adapteur en plastique avait complètement explosé.

[![Configuration cassée](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/config_break.jpeg "Configuration cassée"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/config_break.jpeg){: data-mediabox="gallery-lightbox" data-title="Configuration cassée" }

Un défaut de fabrication, la pièce trop serrée,... je ne sais pas mais ça m'a bien refroidi!

Après avoir partagé ma mésaventure sur Twitter, [Stéphane Péneau](https://twitter.com/stfmani) de Carto'Cité me conseille d'acheter un adaptateur Ram Mount (ref. RAP-B-202U-GOP1), certes plus cher mais aussi d'une tout autre qualité et 100% compatible avec le support triple ventouse.

[![Configuration finale](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/config_finale.jpeg "Configuration finale"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/config_finale.jpeg){: data-mediabox="gallery-lightbox" data-title="Configuration finale" }

### Sécuriser le système

Et pour sécuriser encore un peu plus un éventuel décrochement, j'ai ajouté deux éléments basiques pour assurer la caméra et me rassurer :

1. une ficelle et un mousqueton que j'ai fixé au support triple ventouse et que je viens attacher à l'intérieur de l'habitacle.
2. un bas de ligne acier (normalement utilisé pour la pêche au carnassier) pour relier cette ficelle à la GoPro pour ne pas la perdre en cas de détachement éventuel ou de rupture de l'adaptateur.

----

## Traitement des photos

Passées ces péripéties matérielles, je me suis penché sur le traitement des photos.

### Nettoyage des photos

Après mes premiers tests, lorsque je chargeais mes photos dans l'application [Mapillary Desktop Uploader](https://www.mapillary.com/desktop-uploader), je me rendais compte que j'avais une redondance de photos identiques lorsque je marquais un point d'arrêt aux Stop. J'ai donc commencé à me pencher sur une solution permettant de supprimer ces photos "inutiles" qui se retrouveront "inutilement" stockées sur un serveur Mapillary.


### Intégration du logo

[![Intégration du logo](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/mapillary_logo.jpeg "Intégration du logo"){: .img-center loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/mapillary_logo.jpeg){: data-mediabox="gallery-lightbox" data-title="Intégration du logo" }

----

## Publication des photos

----

## Conclusion

----

## Auteur {: data-search-exclude }

--8<-- "content/team/fbor.md"

{% include "licenses/default.md" %}
