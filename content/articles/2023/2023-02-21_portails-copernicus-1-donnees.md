---
title: Données Copernicus et Sentinel
subtitle: Accès aux données Copernicus et Sentinel
authors:
    - Nicolas DAVID
categories:
    - article
comments: true
date: 2023-02-21
description: Introduction et description des données d'observation de la terre produite dans le cadre du progamme européen Copernicus
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/copernicus_logo.png
license: beerware
robots: index, follow
tags:
    - Corine Land Cover
    - open data
    - satellite
    - Sentinel-2
    - télédétection
---

# Accès aux données Copernicus, partie 1 : données OCS et Sentinel

:calendar: Date de publication initiale : 21 février 2023

## Introduction

![icône satellite](https://cdn.geotribu.fr/img/logos-icones/divers/satellite.png "icône satellite"){: .img-thumbnail-left }

L'Europe fait évoluer, en 2023, les possibilités d'accès aux différentes données des satellites de la constellation Sentinel via la création du "Copernicus Data Space Ecosytem" : [dataspace.copernicus.eu](https://dataspace.copernicus.eu/).
Le lancement de ce nouveau portail est donc une bonne occasion de revenir un peu sur l'historique du programme Sentinel ainsi que les différentes possibilités d'accéder aux données open-data Sentinel puis de détailler les fonctionnalités prévues pour ce nouveau service au cours de trois articles, chacun dédié à une partie pour faciliter la lecture et le "picorage" d'information à ceux qui connaissent déjà le sujet.

Dans cette première partie nous revenons sur le programme Copernicus et surtout sur les différentes données produites par celui-ci. Les personnes connaissant déjà les données et l'ecosystème Sentinel / Copernicus peuvent directement aller au troisième et dernier article de la série.

Série **Accès aux données Copernicus/Sentinel** :

* [Partie 2 : portails d'accès, 'the road so far'](2023-02-28_portails-copernicus-2-passe.md).
* [Partie 3 : évolution de l'accès aux données Copernicus](2023-03-07_portails-copernicus-3-futur.md).

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Programme Copernicus et données d'occupation du sol

[Copernicus (Europe Eyes on Earth)](https://www.copernicus.eu/en/about-copernicus) est le programme européen de suivi et d'observation de la Terre.
Il est responsable d'une part de la production de différentes couches de données géographiques et d'autre part de la mise en service et du suivi opérationnel d'une constellation de satellites d'observation de la terre appelée Sentinel.

Concernant la production de données géographiques issues de Copernicus on peut notamment citer [les produits d'occupation du sol](https://land.copernicus.eu) comme [Corinne Land Cover](https://land.copernicus.eu/pan-european/corine-land-cover), existant depuis 1990 et [Urban Atlas](https://land.copernicus.eu/local/urban-atlas) qui sont produits par photointerprétation manuelle.
Ci-dessous un exemple de ces deux données sur une zone de Clermont-Ferrand, la surface minimale des polygones pour Corinne Land Cover est de 25 hectares et entre 0.25 et 1 hectare pour Urban Atlas :

![Orthophotographie RVB sur Clermont-Ferrand](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/clermont_ferrand_ortho_a.jpg "Orthophotographie RVB sur Clermont-Ferrand - Crédits IGN"){: .img-center loading=lazy }

![Corinne land Cover sur Clermont-Ferrand](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/clermont_ferrand_CLC18_a.jpg "Données Corinne Land Cover 2018 sur Clermont-Ferrand - Crédits IGN  et Copernicus"){: .img-center loading=lazy }

![Urban Atlas sur Clermont-Ferrand](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/clermont_ferrand_UA18_a.jpg "Données Urban Atlas 2018 sur Clermont-Ferrand - Crédits IGN  et Copernicus"){: .img-center loading=lazy }

A cela s'ajoute les couches HRL, [High Resolution Layers](https://land.copernicus.eu/pan-european/high-resolution-layers), produites de façon semi-automatique, de résolution 10m, et se focalisant chacune sur une des thématiques suivantes : zones imperméables, forêts, prairies et les surfaces d'eaux/zones humides, cultures.
Ci-dessous les exemples pour les couches *imperviousness* et *tree cover density* sur la même zone que précédemment :

![Couche HRL imperviousness sur Clermont-Ferrand](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/clermont_ferrand_HRL18_impervious_a.jpg "Données Copernicus HRL imperviousness 2018 sur Clermont-Ferrand - Crédits IGN et Copernicus"){: .img-center loading=lazy }

![Couche HRL Forest sur Clermont-Ferrand](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/clermont_ferrand_HRL18_tree_density_a.jpg "Données Copernicus HRL Tree Cover Density 2018 sur Clermont-Ferrand - Crédits IGN et Copernicus"){: .img-center loading=lazy }

## Données satellites Sentinel d'observation de la terre

Pour les données brutes d'observation de la terre (imagerie spatiale) leur production et mise à disposition sont faites par le déploiement des satellites de la constellation Sentinel, qui s'est inspirée du [succès des satellites US Landsat](https://www.usgs.gov/news/featured-story/fifty-years-landsat-sharing-earth-information-benefit-all).

### Satellites de la constellation Sentinel

![Constellation sentinel 1 slide](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/copernicus_sentinel_esa_mission.jpg "Satellites constellation Sentinel une diapo ESA - Crédits ESA"){: .img-center loading=lazy }

Pour l'aspect observation de la partie surface continentale on peut citer les satellites et capteurs suivants :

* [Sentinel-1](https://esamultimedia.esa.int/docs/S1-Data_Sheet.pdf) : satellites équipés de capteur SAR ([Synthetic Aperture Radar](https://en.wikipedia.org/wiki/Synthetic-aperture_radar)) en bande C avec une revisite de 3 jours. Capteurs : Sentinel-1A (2014- ), Sentinel-1B (04-2016 /06-2022), Sentinel 1C (prévu 04/2023)
* [Sentinel-2](https://esamultimedia.esa.int/docs/S2-Data_Sheet.pdf) : satellites avec capteur optique multispectral à 10/20/60m de résolutions sur 12 bandes spectrales avec une revisite de 5 jours. Les données utilisées sont principalement les données de niveau 2A orthorectifiées et calibrées radiométriquement. Capteurs : Sentinel-2A (06/2015- ), Sentinel-2B (03/2017 - ), Sentinel-2C (prévu 2024)
* [Sentinel-3](https://esamultimedia.esa.int/docs/S3-Data_Sheet.pdf) : satellites altimétriques et observation océan/atmosphère (notamment température) Capteurs : Sentinel-3A (02/2016- ), Sentinel-3B (04/2018 - )
* [Sentinel-5](https://esamultimedia.esa.int/docs/S5-prec_Data_Sheet.pdf) : satellites pour le suivi de l'atmosphère

[D'autres satellites Sentinel](https://www.esa.int/ESA_Multimedia/Images/2022/01/Copernicus_Sentinel_Expansion_missions) sont prévus dans le futur pour augmenter encore les capacités d'observation de la constellation avec en particulier en télédétection pour les surfaces continentales :

* Sentinel-12 / ROSE-L : satellites radar en bande L pour le suivi de la forêt et complémentaire de Sentinel-1 (lancement vers 2027). Bande radar utilisée en particulier pour des applications "forestières"
* Sentinel-10 / CHIME : satellites avec capteur optique hyperspectral en complément des capteurs mutlispectraux de Sentinel-2  (lancement vers 2029)

### Données optiques Sentinel 2

Les données Sentinel-2 sont des données optiques à [13 bandes spectrales](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi/resolutions/spatial) avec trois bandes dédiées à la partie atmosphérique pour les masques de nuages/aérosol et dix bandes spectrales “utiles” pour la télédétection. Parmi ces dernières, 4 ont une résolution de 10m et la plupart des autres sont à 20m de résolution. Les deux satellites Sentinel-2 permettent que chaque portion du territoire français soit volée tous les 5 jours.

![Images Sentinel 2 RVB](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/Sentinel_2_L2A_with_or_without_cloud.jpg "Images Sentinel 2 RVB - Crédits IGN"){: .img-center loading=lazy }

Ci-dessus exemples de données Sentinel 2, visualisation des trois canaux RVB sur une même zone à deux dates : avec et sans nuages

Les données sont disponibles dans plusieurs [niveaux de traitements](https://sentinels.copernicus.eu/web/sentinel/user-guides/sentinel-2-msi/processing-levels), du plus brut au plus proche du besoin utilisateur final, et distribuées soit sous forme de granules soit sous forme de tuiles en projection cartographique UTM :

* **Niveau L1B** : granules mises en forme radiométriquement dans la géométrie d’acquisition capteur (non orthorectifiées). Les informations radiométriques sont de type radiance TOA ([Top Of Atmosphère](https://www.un-spider.org/node/10958)) donc non corrigées des effets comme le voile atmosphérique (aspect bleuté des images)
* **Niveau L1C** : données mises en forme radiométriquement sous forme de tuiles orthorectifées. Même radiométrie TOA que le niveau L1B seule la géométrie des données change. La résolution spatiale des différentes bandes est 10m, 20m, 60m.
* **Niveau L2A** : données en radiométrie BOA (Bottom Of Atmosphère) sous forme de tuiles orthorectifiées et obtenues à partir des données L1C. En plus des données radiométriques cette étape ajoute le plus souvent des images supplémentaires contenant des masques pour définir les pixels valides : masques de nuages et ombres (avec différents types possibles), masque d’occupation du sol (détection de neige, eau), pixels saturés et pixels non compris dans l’emprise d’acquisition.
* **Niveau L3A** : Synthèse temporelle d’acquisition L2A sans présence de nuages. Il s’agit d’interpolations temporelles entre plusieurs images L2A avec présence éventuelle de nuages. Le plus généralement il y a une image par mois. Par exemple produites avec [WASP](https://labo.obs-mip.fr/multitemp/theias-sentinel-2-l3a-monthly-cloud-free-syntheses/)
* **Niveau L4A** : Indices dérivés des données L2A ou L3A comme une occupation du sol au pixel, comme [OSO](https://www.theia-land.fr/ceslist/ces-occupation-des-sols/) ou bien une image d’indice [NDVI](https://custom-scripts.sentinel-hub.com/custom-scripts/sentinel-2/ndvi/) (rapport entre les bandes rouges/infrarouges) ou indices LAI (Leaf Area Index) dérivés des différentes bandes spectrales.

!!! note
    Les tuiles Sentinel suivent le carroyage MGRS, [Military Grid Reference System](https://en.wikipedia.org/wiki/Military_Grid_Reference_System), ce qui explique que vous pouvez entendre des petits noms comme "T30UXV" pour une tuile sur le Calvados par les personnes faisant de la télédétection sur des données Sentinel.

La fréquence élevée de revisite des données Sentinel-2 permet de suivre l'évolution temporelle d'un paysage. Ci dessous une image en composition colorée basée sur ces informations temporelles.

![Composition colorée temporelle NDVI Sentinel 2](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/composition_ndvi_3dates_nov_jan_avr.png "Composition colorée temporelle NDVI Sentinel 2 - Crédits IGN"){: .img-center loading=lazy }

Cette image est obtenue en calculant un indice de présence de végétation (NDVI) à trois dates différentes de l'année et en les composant en une image RVB de telle sorte que les canaux bleu, vert et rouge correspondant respectivement aux dates de novembre 2018, janvier 2019 et avril 2019.
On peut alors représenter le cycle phénologique de la végétation et distinguer différentes espèces de plantes dans les parcelles agricoles. On observe en violet léger les forêts de feuillus, dont l’indice varie selon les saisons, en blancs les conifères dont la valeur reste la même, en noir les zones sans végétalisation…

### Données radar Sentinel 1

Les données Sentinel-1 sont des données Radar/[SAR](https://fr.wikipedia.org/wiki/Radar_%C3%A0_synth%C3%A8se_d%27ouverture) en bande C (longueur d’onde d’approximativement 5cm) et ont une revisite de 3 jours.
Le radar présente un grand intérêt pour le suivi de culture et n’est pas soumis aux masques de nuages comme les images optiques et donc toutes les données acquises sont utiles.

!!! note
    Pour en savoir plus sur les données SAR vous pouvez vous référer notamment au livre [The SAR handbook](https://ntrs.nasa.gov/api/citations/20190002563/downloads/20190002563.pdf) en open access

La résolution des détails observables sur une image Sentinel-1 est annoncée à 20 mètres. A noter que les images SAR sont affectées par un bruit multiplicatif appelé chatoiement. Le plus courant pour traiter ce bruit est d'appliquer un filtre de convolution moyen sur l'image.
On peut appliquer au données SAR Sentinel-1 des niveaux de traitements similaires aux données optiques Sentinel-2 même si de façon générale elles sont
disponibles seulement à des niveaux assez bruts et donc possèdent moins de niveaux de traitement disponibles

* **Niveau L0** : données brutes
* **Niveau L1/L1C** : produits géo-référencés en géométrie capteur par slice (intervalle d’une orbite)
    * GRD : Ground Range Detected, amplitude du signal retour SAR (selon les deux polarités VV et VH)
    * SLC : Single Look Complex , amplitude et phase du signal retour SAR
* **Niveau L2A** : produit ortho-rectifié et tuilée selon grille MGRS
* **Niveau L3A** : produit moyenne temporelle.

Parmi les formats d'image fournis par l'ESA à partir de données de Sentinel 1 on retrouve les formats SLC et GRD.

![Image Sentinel 1 SLC](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/Sentinel_1_SLC.jpg "Image Sentinel 1 SLC - Crédits ESA"){: .img-center loading=lazy }

!!! note
    La fréquence de revisite plus élevée par rapport aux données optiques Sentinel-2 s’explique par le fait que les données SAR sont acquises par un capteur actif et peuvent acquérir des données de nuit donc 2 fois plus que pour des données optiques qui n’acquièrent des données que sur la partie éclairée de leurs orbites.

Les données SLC sont en particulier utilisées en mode "différentiel" entre deux observations successives pour observer les changements géométriques du terrain. Cela peut être pour l'observation de mouvement de terrain (interférométrie radar) mais aussi pour observer des évolutions dans les cultures, pousse des plantes ou inversement récolte d'une culture. Dans ce dernier cas un type d'image dérivée des données SLC sont les [images de cohérence](https://proceedings.esa.int/files/89.pdf) à 6 ou 12 jours (voir illustration ci-dessous), celles-ci permettent de voir si des changements, de l'ordre de la longueur d'onde radar (5 cm), ont eu lieu sur l'intervalle de temps observé. Une forte cohérence indique un non-changement et une faible cohérence du changement.  

![Cohérence radar Sentinel-1](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/copernicus_data/sentinel_1_esa.png "Images de cohérence sentinel-1 6 jours - Crédits ESA"){: .img-center loading=lazy }

----

## Je veux plus d'images !

Si tout cela n'a pas encore suffi à satisfaire vos mirettes, ou que vous souhaitez changer votre fond d'écran, je ne peux que vous conseiller d'aller par exemple sur le site [Image of the day Copernicus]( https://www.copernicus.eu/en/media/image-day) pour y trouver d'autres images Sentinel sélectionnées en fonction de l'actualité ou de leur esthétisme.

<!-- geotribu:authors-block -->
