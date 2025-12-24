---
title: Retrospective du Qalendrier Geotribu 2025
subtitle: Quelques moyens mèmotechnique
authors:
    - Guilhem ALLAMAN
categories:
    - article
comments: true
date: 2025-12-25
description: Une retrospective sur les posts du Qalendrier de l'Avent 2025 de Geotribu, histoire d'amorcer en douceur la transition vers QGIS 4.
icon: material/emoticon-happy-outline
image:
license: beerware
tags:
    - gischat
    - QGIS
    - QGIS4
    - meme
---

# Restrospective sur le Qalendrier 2025

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

Quand j'étais petit, j'aimais bien lire des atlas et des BD. Et, entre nous, mes vignettes préférées c'était celles où y'avait que des images...

Voici donc un article principalement composé d'images, de "mèmes" comme on dit et au-delà de [réduire la charge pour l'équipe de relecture :wink:](https://contribuer.geotribu.fr/articles/review/), c'est l'occasion de publier et de revenir sur le Qalendrier Geotribu 2025 !

Un Qalendrier publié dans le but de célébrer,

<!-- markdownlint-disable MD033 -->

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/3GwjfUFyY6M?si=4sjAKodS7wD8aj41" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

<!-- markdownlint-enable MD033 -->

Et préparer les qalins pour la période des fêtes !

![Livraison de qalins](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/qalins.webp){: .img-center loading=lazy }

D'autant plus que la création de mèmes a un peu été ma porte d'entrée vers la contribution à Geotribu, notamment via [mon premier article signé ici](../2023/2023-01-28_retour-vers-le-futur-du-30dmc.md), sur un ton disons _décontract'_ au risque de passer pour un Guignol... Et via, disons, la fibre de "_trolling_" que contient le groupe et la communauté, qui s'accompagne d'une affinité pour le partage, les technos et les évènements FOSS4G.

## Concept, principe, règles du jeu

En novembre dernier, suite [au billet de blog de QGIS.org](https://blog.qgis.org/2025/10/07/update-on-qgis-4-0-release-schedule-and-ltr-plans/) qui annonçait la _roadmap_ et les dates de QGIS 4, ça m'a donné envie de créer des images humoristiques, pour marquer le coup et amorcer la transition vers cette nouvelle version majeure.

Après discussion, on s'est dit que ce serait marrant de publier ces images sur les réseaux sociaux, et [Julien](../../team/julien-moura.md) m'a donné le petit coup de boost pour me lancer. Histoire de rigoler un coup, communiquer sur ces dates majeures dans la joie et la bonne humeur :face_with_peeking_eye:

D'autant plus qu'on avait quelques images en stock, ainsi que d'autres déjà publiées, sur des évènements et technologies SIG. Soit aussi l'occasion de les mettre à jour et de les ressortir !

_À noter que le site imgflip.com a été utilisé pour certains mèmes, ainsi que textstudio.com pour certains lettrages._

## Qalendrier 2025

### Jour 1

Première publication : on explique les règles du jeu et on plante le décor !

![Qalendrier - jour 1](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/1_drake_qalendar_alt.webp){: .img-center loading=lazy }

### Jour 2

:sailboat: Cap sur Brest, avec [les prochaines Rencontres QGIS-fr](https://conf.qgis.osgeo.fr/) qui s'y tiendront fin mars 2026, organisées par [l'OSGeo-fr](https://www.osgeo.fr/) en partenariat avec [l'UMR LETG](https://letg.cnrs.fr/).

L'occasion de jauger votre qumi-qata ?  
L'occasion d'arborer votre nouveau Qimono ?  
L'occasion de rencontrer d'autres ceintures du Q-Gitsu / PostGiTsu ?

![Affiche des Journées Portes Ouvertes de la Fédération Francophone de QGITSU](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/2_qgitsu_brest_qgisfr2026.webp){: .img-center loading=lazy }

### Jour 3

Focus sur [la roadmap de QGIS4](https://blog.qgis.org/2025/10/07/update-on-qgis-4-0-release-schedule-and-ltr-plans/), avec la v4.0 prévue en février prochain, et la v4.2 - première LTR - en octobre 2026.

Ça va venir vite, alors anticipez, dès maintenant !

Par exemple en vérifiant la compatibilité de vos plugins avec Qt6, la nouvelle version qu'embarquera QGIS4.

![Qalendrier - jour 3](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/3_shaq_qgis4_deadline_en.webp){: .img-center loading=lazy }

### Jour 4

Aujourd'hui, un tuyau #BlaqFriday : vente flash sur la nouvelle gamme de Barbe-Q multifonctions !

![Qalendrier - jour 4](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/4_qing_of_the_grid_queen_of_the_fid.webp){: .img-center loading=lazy }

### Jour 5

Quand on a fait tourner pour la première fois les outils de vérification de compatibilité QGIS4 sur notre plugin [QTribu](https://plugins.qgis.org/plugins/qtribu/)...

À noter que les outils permettent de détecter précisément les endroits du code à changer, ainsi que par quoi remplacer.

![Qalendrier - jour 5](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/5_harold_run_pyqt5_to_pyqt6_script.webp){: .img-center loading=lazy }

### Jour 6

QGIS4 c'est Qt6 et non plus Qt5, pour que vos outils soient compatibles exit donc les imports explicites !

Dîtes au revoir aux `from PyQt5.QtGui import QIcon`, dîtes bonjour aux `from qgis.PyQt.QtGui import QIcon` !

![Qalendrier - jour 6](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/6_cardriver_pyqt5import_qgis4.webp){: .img-center loading=lazy }

### Jour 7

QGIS 4 ? #QuickMath

![Qalendrier - jour 7](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/7_qgis4_qgis3_plus_1_alt.webp){: .img-center loading=lazy }

### Jour 8

Vous avez dit "[GDAL](https://gdal.org/en/stable/software_using_gdal.html)" ?

![Qalendrier - jour 8](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/8_gdal_softwares.webp){: .img-center loading=lazy }

### Jour 9

On traverse le Rhin, avec une blague qlassique chez nos amis allemands, au sujet de ce logiciel SIG qu'est vachement bien : KuhGIS :cow:.  
Une image qui on l'espère ne vous rendra pas chèvre...

![Qalendrier - jour 9](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/9_kuhqgis4.webp){: .img-center loading=lazy }

### Jour 10

Et cette fameuse tirade de _William Shakesfile_ :

> LTR or not LTR, that is the question.

![Qalendrier - jour 10](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/10_buttons_qgis4_0_qgis4_2_en.webp){: .img-center loading=lazy }

### Jour 11

Exorcisez vos démons, par exemple en lançant [l'outil](https://github.com/qgis/pyqgis4-checker)`pyqgis4-checker` sur vos plugins ?

![Qalendrier - jour 11](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/11_monkey_bike_pyqgis4-checker_plugins_fr.webp){: .img-center loading=lazy }

### Jour 12

On est en avance de phase avec cette playlist "Summer GIS Hits" du plus bon goût, pour les mélomanes de cet été...

![Qalendrier - jour 12](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/12_summer_gis_hits.webp){: .img-center loading=lazy }

Une playlist [enrichie par Jean-Daniel C.](https://www.linkedin.com/feed/update/urn:li:activity:7405131827734167552) avec les _hits_ suivants :

- Quand la statistique est bonne
- Les LAS du Connemara
- Les Shapefiles des tropiques

### Jour 13

:notes: Y'a de la data, y'a de la data, ohé ohé !

RIP Guy Bévert, feu batteur et chanteur de [la Compagnie Créole](https://fr.wikipedia.org/wiki/La_Compagnie_cr%C3%A9ole) <3

![Qalendrier - jour 13](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/13_gdal_masque.webp){: .img-center loading=lazy }

Stéphane R. [a aussi du GDALida dans son répertoire](https://www.linkedin.com/feed/update/urn:li:activity:7405509292247756800) :wink:

### Jour 14

Puisqu'un calendrier sans chat n'en est pas vraiment un :cat:

![Qalendrier - jour 14](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/14_cat_qt5_import_qgis4_en.webp){: .img-center loading=lazy }

### Jour 15

On parle _Extract - Transform - Load_, avec ce fameux single du R'n'B français des années 2000, de **Q-Maro** :

:notes: Donne-moi ton core bébé, j'veux FME like U !

![Qalendrier - jour 15](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/15_qmaro_fme_like_u.webp){: .img-center loading=lazy }

### Jour 16

Votre pare-data a subi un impaqt ?  
Votre qarosserie nécessite une remise en forme ?  
Vous aussi vous en avez marre de cette pub qui matraque les neurones ?  

RDV dans votre garage OSGeo le plus proche, QGIS et GRASS s'en chargent !  

![Qalendrier - jour 16](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/16_qargrass_repare_qargrass_remplace.webp){: .img-center loading=lazy }

Et Antoine G. [nous dit qu'une paire d'essuie-grass est offerte](https://mapstodon.space/@ant2trem/115728039463134015) jusqu'au 24.12 !

### Jour 17

On célèbre le modeleur graphique de QGIS, et notamment sa capacité à se plonger en profondeur dans le vaste océan des SIG !

Et :two_hearts: sur les cyclistes sigistes qui sont sous l'eau pour boucler l'année !

![Qalendrier - jour 17](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/17_bicycle_undersea_buzy_qgis_model_fr.webp){: .img-center loading=lazy }

### Jour 18

Ça part sur ce classique du rap français, et le _Suprême MNT_ :

:notes: Laisse pas traîner ton GIS, si tu veux pas qu'il glisse !

![Qalendrier - jour 18](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/18_supreme_mnt.webp){: .img-center loading=lazy }

### Jour 19

Aujourd'hui on met en avant [Panoramax](https://panoramax.fr/), les _Gissy Riders_ et toute la contribution vaillante en vadrouille : à pinces, à biqlou, à béqane, en qamion de pompier...

Ce qui s'accompagne également d'une playlist Roq'n'Roll, est-ce que vous reconnaîtrez les morceaux ?

![Qalendrier - jour 19](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/19_gissy_rider_ride.webp){: .img-center loading=lazy }

Une playlist [enrichie par Panoramax et Christian Q.](https://www.linkedin.com/feed/update/urn:li:activity:7407668515299540992) avec les morceaux suivants :

- Grass Jones : Slave to the algo-rythm
- Visages : Fade to grey and blur
- Police : Ghost in the server / Too much data / Every little thing sgblur does is magic / Don't stand so close to my camera
- Tomtom Jones : It's not undefined

### Jour 20

Suite arithmétique ? 🤔

![Qalendrier - jour 20](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/20_qgis8_qt10_en.webp){: .img-center loading=lazy }

$$
\forall n \ge 2 ; QGIS(n) = Qt(n+2) ?
$$

C'est vrai ce mensonge ?

### Jour 21

Hommage au [QGIS plugin templater](https://oslandia.gitlab.io/qgis/template-qgis-plugin/), et sachiez-vous qu'il y a maintenant [un plugin QGIS](https://plugins.qgis.org/plugins/qgis_plugin_templater_gui/) ?

Oui, il est possible de générer une structure de plugin moderne en quelques clics !

![Qalendrier - jour 21](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/21_danny_qgis_plugin_templater_en_v2.webp){: .img-center loading=lazy }

### Jour 22

Aujourd'hui, clin d'oeil aux connexions Marseille - Nord-Est Parisien, au travers de la projection Lambert 80 zetrei !

![Qalendrier - jour 22](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/22_reprojection_lambert80zetrei.webp){: .img-center loading=lazy }

### Jour 23

On fête la sortie de QField 4, au travers de cette référence géomusicale de 1979 :mirror_ball:

![Qalendrier - jour 23](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/23_sugar_qfield_gang_mappers_delight.webp){: .img-center loading=lazy }

### Jour 24

Il y a bien longtemps, dans une géogalaxie lointaine, très lointaine...

Les GeoJedis s'allient, rassemblent et mutualisent les forces en présence.

Jeune padawan, rejoins le côté QGIS de la Force !

![Qalendrier - jour 24](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/24_qgis_episode_4.webp){: .img-center loading=lazy }

Et merci de nous avoir suivi pendant ce qalendrier de décembre, joyeuses fêtes !

### Bonus

Et en voici quelques uns pour la route, qui n'ont pas été sélectionnés pour publication au cours du qalendrier...

> Mmmmh ces mots doux que vous pouvez dès à présent susurrer à l'oreille de vos qollègues...

![Qalendrier - bonus 1](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/32_goosebumps_qgis4_en.webp){: .img-center loading=lazy }

> Une image à destination de décideurs / décideuses SIG, fans de tuning et de qustomization de véhiQles ?

![Qalendrier - bonus 2](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/32_reprends_les_qles_du_qamion.webp){: .img-center loading=lazy }

> Contrairement à QGIS et aux logiciels libres et OpenSource, celui-ci est "gratuit"... Juste pour le template qui est plutôt cool :)

![Qalendrier - bonus 3](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/32_undertaker_qgis4_qgis3plugin_en.webp){: .img-center loading=lazy }

> _Rest In Peace_ Plugin Builder, merci pour toutes ces années de bons et loyaux services !

![Qalendrier - bonus 4](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/32_bath_gisers_qgis_plugin_templater_plugin_builder_fr.webp){: .img-center loading=lazy }

> C.F. Indiana Jones - Les Aventuriers de l'_Artefact Build pour Windows_...

![Qalendrier - bonus 5](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2025/retrospective_qalendrier_2025/32_indiana_jones_qgis4_qt6_vcpkg.webp){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
