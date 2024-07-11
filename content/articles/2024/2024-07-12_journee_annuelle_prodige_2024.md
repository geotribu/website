---
title: "Journée annuelle Prodige 2024"
authors:
    - Benjamin Chartier
categories:
    - article
comments: true
date: 2024-07-12
description: "Synthèse de la journée annuelle Prodige qui s'est tenue en ligne le 3 juin 2024"
icon: octicons/people-16
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/journee_annuelle_prodige_2024/prodige_au_service_des_territoires.webp
license: beerware
robots: index, follow
tags:
    - Prodige
    - Afigéo
    - CNIG
    - Plateformes de données
---

# Journée annuelle Prodige 2024

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![logo IGN France](https://cdn.geotribu.fr/images/logos-icones/logiciels_librairies/prodige-logo-small.png){: .img-thumbnail-left }

La communauté [Prodige](https://www.prodige-opensource.org/accueil) s'est réunie lors d'un évènement en ligne organisé le 3 juin 2024 : [Journée annuelle PRODIGE 2024](https://www.prodige-opensource.org/accueil/journee-nationale-prodige). Comme l'année précédente, elle a accueilli des représentants d'autres communautés logicielles : notamment la plateforme Géo2France et le projet Ecosphères.

Cet article met en avant quelques points remarquables de cette journée. Je l'ai rédigé à l'occasion de mon intervention à propos du collectif CICCLO dans le cadre des missions d'animation que l'[Afigéo](https://www.afigeo.asso.fr/) m'a confiées pour dynamiser l'écosystème technique des plateformes de données géographiques.

## Expérience utilisateur

Un constat fait par les plateformes de données : leurs portails actuels ne sont pas adaptés à des non spécialistes de l'information géographique. Ce constat est partagé par bon nombre de plateformes y compris par celles qui n'utilisent pas Prodige. Ce n'est pas tant la partie strictement gérée par Prodige (outils de publication, recherche et exploitation des données) que la partie éditoriale des portails qui est visée ici.

Plusieurs plateformes ont entamé des travaux sur l'expérience utilisateur pour refondre leurs portails afin de mieux répondre aux attentes de leurs usagers : en particulier [DatARA](https://www.datara.gouv.fr/accueil) et [AtlaSanté](https://www.atlasante.fr/accueil) qui ont chacune présenté leur démarche. Ces travaux mobilisent des spécialistes de l'expérience utilisateur d'une part et d'autre part des utilisateurs avec différents profils (utilisateurs aguerris, utilisateurs découvrant le portail, et utilisateurs non spécialistes).

Cette tendance rejoint des efforts constatés ces derniers temps pour mettre l'expérience utilisateur au centre du développement des plateformes de données dont l'un des enjeux majeurs actuels est d'impliquer leurs usagers dans les démarches contributives qu'elles portent. Quelques exemples de conceptions orientées UX récentes : le [DataHub](https://www.geo2france.fr/datahub) par [Camptocamp](https://camptocamp.com/fr) pour Géo2France, le module contribution de Prodige par [Alkante](https://www.alkante.com), les outils collaboratifs de cartes.gouv.fr et l'interface de recherche du [portail open data de la Métropole Européenne de Lille](https://data.lillemetropole.fr) sur la base du DataHub.

![Image dont l'auteur de l'article ne reconnaît la paternité ; il ne dénoncera pas la personne qui a honteusement fait appel à une intelligence artifielle générative pour la produire...](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/journee_annuelle_prodige_2024/prodige_au_service_des_territoires.webp){: .img-center loading=lazy }

## Interopérabilité

On a pu également constaté le retour au premier plan des questions d'interopérabilité entre plateformes de données. Plusieurs présentations ont abordé cette question par de multiples axes :

- [Géo2France](https://www.geo2france.fr) : cette plateforme a présenté ses actions en faveur d'un meilleur accès aux métadonnées provenant de diverses sources afin de faciliter la découvrabilité des jeux de données. Dans cette présentation l'accent était porté sur les capacités de [Geoclip](https://www.geoclip.fr/) à produire des métadonnées ISO 19139 ainsi que celles du DataHub à les valoriser. Il est intéressant de noter que ces capacités de Geoclip ne sont presque pas connues des exploitants des instances de Geoclip présentes lors de cette journée (AtlaSanté, [Sigena](https://www.sigena.fr/accueil) et [Picto-Occitanie](https://www.picto-occitanie.fr/accueil/)) faute de communication de la part de l'éditeur. L'intérêt est d'autant plus important que Geoclip propose une interface graphique facile d'accès pour des agents ayant peu de compétences en information géographique. Faciliter l'accès des cartographies dynamiques depuis une interface de recherche simple telle que le DataHub rejoint les problématiques d'expérience utilisateur abordées plus tôt par DatARA et AtlaSanté.
- [CICCLO](https://cnig.gouv.fr/collectif-interoperabilite-et-mise-en-commun-de-a26159.html) : ce collectif formé en fin d'année dernière au sein du [CNIG](https://cnig.gouv.fr/) et animé par l'[Afigéo](https://www.afigeo.asso.fr/) a pour but de favoriser l'interopérabilité des solutions techniques sur lesquelles reposent les principales plateformes de données régionales et nationales. Parmi ses actions : partages d'expérience, mutualisation, développements coordonnés de nouvelles fonctionnalités entre communauté logicielles. Les présentations de Géo2france (qui met en œuvre [geOrchestra](https://www.georchestra.org/fr/)) et d'Ecosphères (qui s'appuie sur [data.gouv.fr](https://www.data.gouv.fr/fr/)) illustrent parfaitement la dynamique portée par CICCLO visant à instaurer des échanges constructifs entre les communautés logicielles.
- L'intervention du collectif CICCLO a été l'occasion de présenter le lancement d'un projet co-financé par l'État pour le développement du support d'[AgentConnect](https://agentconnect.gouv.fr/) et de l'[API Features](https://ogcapi.ogc.org/features/) de l'OGC au sein de geOrchestra, Prodige, [OneGeo Suite](https://www.onegeosuite.fr/) et la [Géoplateforme](https://www.ign.fr/geoplateforme).
- Projet [Ecosphères](https://www.eig.numerique.gouv.fr/defis/ecospheres/) : ce projet mené par [ECOLAB](https://greentechinnovation.fr/ecolab/) vise à proposé des bouquets de données adaptés à l'élaboration et au suivi des politiques publiques sur des thématiques environnementales. Le cœur de cet outil reposera sur les capacités techniques de data.gouv.fr. L'un des enjeux des travaux menés conjointement par ECOLAB et data.gouv.fr réside dans le renforcement des aptitudes à moissonner les métadonnées issues des plateformes de données telles que Prodige et à interpréter correctement les informations qu'elles contiennent. Pour cela, une documentation technique a été publiée : [Recommandations ISO/DCAT](https://ecospheres.gitbook.io/recommandations-iso-dcat).

## Nouveautés Prodige en approche

- Mise en place d'un nouveau mode de mise à jour des données par dépôt du jeu de données via une connexion sFTP ;
- Catalogage : intégration du DataHub et de [GeoNetwork](https://www.geonetwork-opensource.org/) 4.4 ;
- Module traitement permettant d'enrichir les traitements possibles avec des scripts Python ou R. Ce module implémente l'[API Processes](https://ogcapi.ogc.org/processes/) de l'OGC ;
- Nouvelle version du générateur d'applications métier no-code. Deux exemples d'applications métier créées avec Prodige : [Base de données des ZAE en Centre-Val de Loire](https://zae.doterr.fr), ou [Signalement Ambroisie](https://signalement-ambroisie.atlasante.fr) ;
- Datavisualisations : nouveau module de gestion des dataviz, avec la capacité de les exploiter dans le générateur d'application métier, de les cataloguer et les rendre accessibles via le DataHub ;
- Diffusion des données : mise en place de services WMS et WFS protégés, et implémentation de l'API Features de l'OGC dans le cadre d'un projet coordonné par le collectif CICCLO.

Pour en savoir plus sur les évolutions de Prodige : consultez la [feuille de route](https://www.prodige-opensource.org/accueil/decouvrir/developpements).

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
