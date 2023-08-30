---
title: Monter un kit de géolocalisation à haute précision
authors:
    - Jérémie Hanke
categories:
    - article
    - tutoriel
date: "2023-09-05 10:20"
description: Tutoriel de montage d'un kit de géolocalisation à haute précision (rover RTK) à coût limité, sans avoir à faire de soudure ni production de pièces sur mesure, juste à brancher. Variante du tutoriel de l'INRAE (projet Centipede).
icon: material/satellite-uplink
image:
license: default
robots: index, follow
tags:
    - centipede
    - GPS
    - rover
    - RTK
---

# Tutoriel : monter un kit de géolocalisation à haute précision (rover RTK)

:calendar: Date de publication initiale : 5 septembre 2023

## Introduction

![icône GPS](https://cdn.geotribu.fr/img/logos-icones/gps.png "icône GPS"){: .img-rdp-news-thumb }

Ce tutoriel rassemble les informations pour obtenir un kit de géolocalisation (Rover) à haute précision mais à coût limité et le configurer avec son smartphone Android.

Il s'agit d'une alternative au [projet de création de rover initié par l'INRAE et ses contributeurs](https://docs.centipede.fr/docs/make_rover/), sans avoir à faire de soudure, et sans production de pièces sur mesure, juste à brancher.

A noter que je n'ai pas de préférence pour tel ou tel produit / marque / revendeur et que j'ignore la fiabilité des solutions matérielles ou logicielles choisies.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## Matériel

### Prérequis

- smartphone fonctionnant sous Android avec un forfait data

### Pour la partie géolocalisation à haute précision

- [Kit préconfiguré comprenant le Récepteur RTK ZED F9P avec Bluetooth d'Ardusimple et l'antenne u-blox ANN-MB-00](https://www.ardusimple.com/product/simplertk2blite-bt-case-kit/)
- [Batterie](https://fr.shopping.rakuten.com/offer/buy/8745966944/batterie-de-secours-5000-mah-1-usb-a-max-series-noire-bleue.html?fbbaid=10776957204&t=180177&gclid=EAIaIQobChMIwPSJ37Tv_wIV1pJoCR2QkAP6EAQYAyABEgKZ5fD_BwE) externe, type recharge pour smartphone, pas trop encombrante pour une alimentation dédiée du récepteur.
- [Interrupteur](https://m.fr.aliexpress.com/item/1005004055554570.html?pdp_npi=2%40dis%21EUR%215%2C28%E2%82%AC%213%2C59%E2%82%AC%21%21%21%21%21%40211b612816882797560523189ea16c%2112000027880087678%21btf&_t=pvid%3A00fec2bb-2b37-44a1-9765-1ec9059854d9&afTraceInfo=1005004055554570__msite__c_ppc_item_bridge__xxxxxx__1688279756&spm=a2g0n.ppclist.product.0&gatewayAdapt=gloPc2fraMsite) USB avec diode, pour le confort d'utilisation.

### Pour un montage sur une canne

- [Canne](https://m.fr.aliexpress.com/item/1005004495311018.html?spm=a2g0n.productlist.0.0.60dd6d69RZXJqt&browser_id=16a1a524c6bc47239b3a0e6ec13b3b69&aff_platform=msite&m_page_id=ktanhewysycavbsl18914796bd4b1eeb581d8baa08&gclid=&pdp_npi=3%40dis%21EUR%2135.35%2126.87%21%21%21%21%21%402100bbf516882656491165512d0745%2112000029359608806%21sea%21FR%210&isseo=y&algo_pvid=fccc553b-4c66-483a-80d1-02e03b135c41) télescopique ou à assembler.
- [Platine](https://www.sparkfun.com/products/17519) servant de masse et de support pour l'antenne aimantée.
- [Réducteur](https://www.amazon.fr/dp/B07QGZHY9Q/ref=sspa_mw_detail_0?ie=UTF8&psc=1&sp_csd=d2lkZ2V0TmFtZT1zcF9waG9uZV9kZXRhaWwp13NParams&th=1) 5/8-20 à 1/4-11 pour pouvoir visser la platine sur la canne.

### Coût global

Pour l'ensemble de géolocalisation, en juin 2023, la dépense est inférieure à 400€ TTC frais de port inclus.  
Si on ajoute le matériel pour créer une "canne d'arpentage", toujours 400€ en allant chercher les pièces à pied... ou 450€ frais de port compris.

![GPS Ardusimple - Matériel](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/ardusimple/GPS_ardusimple_materiel.jpg){: .img-center loading=lazy }

### Assemblage et configuration

Rien de plus simple :

- Assembler
- Brancher le matériel
- puis le mettre sous tension !
- Activer le bluetooth sur le smartphone et associer le récepteur à votre smartphone.

----

## Utilisation

Deux principes pour l'utilisation du gps RTK avec correction en temps réel :

- A : utilisation d'applications de saisie de données contenant une interface pour gérer les corrections en temps réel NTRIP. Par exemple : [SW Maps](https://play.google.com/store/apps/details?id=np.com.softwel.swmaps) (non payant) ou Map-it  ( add-on NTRIP payant).
- B : utilisation d'applications de saisie ou de consultation ne prenant pas en charge les corrections en temps réel ([Qfield](https://qfield.org/), [Locus](https://www.locusgis.com/), Map-it sans l'add-on, navigateur web...). Dans ce cas, on utilise une application qui va gérer uniquement les corrections NTRIP sans interface cartographique + configuration d'Android pour utiliser le GPS externe avec la correction en temps réel.

### Cas d'utilisation A : Utilisation de l'application SW Maps

![icône SW Maps](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/sw_maps.webp){: .img-rdp-news-thumb }

SW Maps présente l'avantage d'être gratuite et de gérer les corrections en temps réel NTRIP.

1. Ajout du fichier [Raf20](https://www-iuem.univ-brest.fr/pops/attachments/2512) dans le smartphone, dans le répertoire :

    ```txt
    Stockage du téléphone/Android/media/np.com.softwel.swmaps/geoids
    ```

1. Installer et démarrer SW Maps
1. Sélection du fichier `raf20.gtx` dans `Settings/Geoids`.
1. Renseigner la hauteur d'antenne.
1. Mesurer au prélable la hauteur de l'ensemble matériel : hauteur de canne + réducteur + platine + [décalage](https://portal.u-blox.com/s/question/0D52p00009AYzYjCAL/difference-between-cfgtmodeecefz-and-cfgtmodeecefzhp) ARP de [l'antenne](https://www.u-blox.com/sites/default/files/documents/ANN-MB_DataSheet_UBX-18049862.pdf)
1. Connexion du récepteur à l'application:
1. Sélection de votre équipement de géolocalisation dans la liste des appareils bluetooth disponibles. Ex: GNSS-RTK.
1. Connexion à un réseau de correction NTRIP : voir plus bas.

### Cas d'utilisation B : Utilisation de la localisation simulée

Le mieux est de disposer d'un smartphone sous Android 11+.

1. Installer une application de géolocalisation prenant en charge les corrections NTRIP. Par exemple : [Lefebure Ntrip client](https://play.google.com/store/apps/details?id=com.lefebure.ntripclient). A noter que SW Maps est également capable de gérer la localisation simulée.
1. Activer la consommation de données en [arrière plan](https://www.ardusimple.com/question/rtk-fix-location-obtained-in-lefebure-ntrip-client-mock-app-disconnects-when-switching-over-to-mapit-gis-app/) de l'application qui va produire l'information de localisation (NTRIP client, SW Maps). Ceci afin de ne pas avoir le flux de géolocalisation coupé lorsque vous allez switcher sur votre application de saisie ou de consultation.
1. Activer le mode developpeur de votre smartphone. Pour cela, il faut rechercher sur internet comment activer le mode dévéloppeur pour le modèle de votre appareil. En effet, il peut y avoir quelques différences entre modèles. Généralement, cela consiste simplement en un appui repeté (~ 7 fois) sur un item numéro de build ou de version situé dans les paramètres du téléphone que l'on trouve :
    - Avec Android 10 sans surcouche fabricant : `Paramètres` > `A propos du téléphone` > `Numéro de build`
    - Avec Android 11 avec surcouche Color OS 11 : `Paramètres` > `A propos du téléphone` > `Version` > `Numéro de version`
1. Activer la position simulée : l'intitulé est variable selon la version d'Android ( Sélectionner l'application de postion fictive ou encore Enable Mock location) dans le menu " Options développeurs" ( *Paramètres/ Paramètres avancés/ Systeme sous Android 10* ) et choisir l'application que vous aller utiliser pour gérer le geo-positionnement corrigé ( Ntrip client, Swmaps...).
1. Mettre en route le GPS de votre smartphone.
1. Désactiver, dans les options de contrôle de positionnement d'Android, la recherche wifi et la recherche bluetooth.
1. Désactiver "améliorer la précision de la localisation" dans l'item précision de la localisation de Google.
1. Connexion du récepteur à l'application :
    sélection de votre équipement de géolocalisation dans la liste des appareils bluetooth disponibles. Ex: GNSS-RTK.
1. Mettre en route votre application de gestion des corrections NTRIP.
1. Connecter votre recepteur GPS Bluetooth à l'application de gestion des corrections NTRIP.
1. Configurer avec les informations disponibles sur l'item NTRIP précédent et cocher la case "Mock location"  pour les applications NTRIP client le proposant (pas nécessaire dans SW Maps).
1. Mettre en route votre application de consultation ou de saisie de données ( [Qfield](https://qfield.org/), [Locus](https://www.locusgis.com/), navigateur web ...).

!!! Info "A noter pour la méthode B uniquement"
    Si l'application vous propose d'utiliser le GPS interne ou le GPS externe, choisir interne puisqu'il s'agit en réalité de votre GPS Bluetooth + la correction NTRIP. D'où la notion de localisation simulée. Si vous choisissez le GPS bluetooth, vous utiliserez le GPS externe sans la correction NTRIP.

----

## NTRIP : connexion à un réseau de correction

Exemple de réseau ouvert [centipede](https://docs.centipede.fr/docs/centipede/3_connect_caster.html) :

- Nom du réseau : `caster.centipede.fr`
- Identifiant et mot de passe : laisser vide ou centipede pour les 2 champs
- Choisir un [point de montage](https://centipede.fr/index.php/view/map/?repository=cent&project=centipede) proche de votre lieu de collecte en consultant la carte des antennes disponibles sur: <https://centipede.fr/index.php/view/map/?repository=cent&project=centipede>.

----

## Conclusion

Votre équipement, assemblé et configuré, est prêt pour la collecte de données. Cet ensemble offre une très bonne précision dans les meilleures conditions de récéption.

Des contraintes sont toutefois à prendre en compte pour avoir une qualité de géopositionnement la plus précise possible :

- il est nécessaire d'être dans une zone de récéption de data via le téléphone mobile, et d'être le plus proche possible d'une base de correction NTRIP.
- Les limitations habituelles de récéption des signaux satellites provoqué par le bati et le couvert végétal s'appliquent également.

En dehors des conditions optimales d'utilisation, l'ensemble offre tout de même une précison supérieure à la puce GPS d'un téléphone portable.

Ce type de dispositif est vendu comme capable d'obtenir une précision centimétrique. Je n'utilise volontairement pas les termes de précison centimétrique/ décimétrique/submétrique pour qualifier la précision des données collectées.

Suite à quelques tests effectués sur plusieurs jours de collecte, en étant situé à une dizaine de kilomètres d'une base, je constate une distribution des points relevés sur une emprise d'une dizaine de centimètre en latitude et longitude, et une vingtaine de centimètre en altimètrie. Une campagne de tests plus rigoureux et de comparatifs avec des points relevés par un géomètre permettrait d'affiner les qualificatifs à employer!

![GPS Ardusimple](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2023/ardusimple/GPS_ardusimple.jpg){: .img-center loading=lazy }

Je vous invite également à consulter [le site du réseau Centipede](https://docs.centipede.fr) pour comprendre l'excellente démarche initiée par l'[INRAE](https://www.inrae.fr/) et les contributeurs. Vous y trouverez des informations pour comprendre le principe de fonctionnement de la géolocalisation RTK, des informations pour créer votre propre station de diffusion de correction NTRIP pour permettre d'augmenter la couverture sur votre territoire et comment créer votre rover de façon plus économique si vous souhaitez davantage "mettre les mains dans le cambouis".

Contributions qui pourraient être intéressantes :

- À récepteur et conditions identiques, quelles sont les incidences sur la précision du relevé et les capacités de réception des signaux avec d'autres antennes ?
- À antenne et conditions identiques, quels résultats sur la précision du relevé avec un autre fabricant de récepteur à bas coût ZED F9P ( Drotek, Sparkfun) ?

L'idée serait de pouvoir évaluer le gain sur un rapport coût/précision.

## Sources

- [Centipede](https://docs.centipede.fr/)
- [Ardusimple](https://www.ardusimple.com/documentation/)
- [Université de Brest](https://www-iuem.univ-brest.fr/pops/attachments/2512)
- [Institut Geographique National](https://geodesie.ign.fr/index.php?page=grilles)
- [Parc naturel régional du golfe du Morbihan](https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.parc-golfe-morbihan.bzh/medias/2023/02/UBO_notice_Centipede-RTKsurveyor-2.pdf&ved=2ahUKEwjTo8nL2u__AhXsVaQEHSYeB3wQFnoECA0QAQ&usg=AOvVaw1WYPlWQZnnqtvwUNTzsix_)
- [U-Blox](https://www.u-blox.com/en/product/ann-mb-series)

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jhan.md"

{% include "licenses/default.md" %}
