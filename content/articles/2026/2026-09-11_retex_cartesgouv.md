---
title: "Cartes.gouv.fr : on ne remplace pas un portail, on sort d'un modèle"
authors:
    - Xavier THAUVIN
categories:
    - article
comments: true
date: 2026-09-11
description: "Cartes.gouv.fr : retour d’expérience sur la transformation du Géoportail en plateforme ouverte de données, services et cartes du territoire."
icon: fontawesome/solid/map
image:
license: default
robots: index, follow
tags:
    - cartes.gouv.fr
    - GeoNetwork-UI
    - Géoplateforme
    - Géoportail
    - IGN
    - métadonnées
    - OpenSource
    - QGIS

---

# Cartes.gouv.fr : on ne remplace pas un portail, on sort d'un modèle

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

> Vu de loin, [cartes.gouv.fr](https://cartes.gouv.fr) ressemble à un successeur du Géoportail avec une interface neuve.
La lecture est naturelle, elle est aussi assez trompeuse.
Ce qui s'est joué derrière ce site, c'est le passage d'une collection d'outils spécialisés à une logique de plateforme, avec des briques faites pour vivre ensemble et un cycle de vie de la donnée traité comme un tout.
Retour sur plusieurs années de chantier, jusqu'à l'ouverture aux professionnels.

J'ai écrit cet article à l'été 2026, huit mois après l'ouverture aux professionnels et quelques semaines après celle au grand public. Assez de recul pour que les choses aient décanté, pas assez pour avoir oublié l'historique.

## « Au fond, que remplace-t-on ? »

C'est la question qui revenait le plus souvent au début du projet. Le Géoportail ? Géoservices ? MaCarte ? L'Espace collaboratif ?

La réponse s'est imposée très tôt, confirmée par un atelier d'une quinzaine d'utilisateurs en phase de conception. Et impossible de les assigner à un profil particulier car leurs missions les faisaient côtoyer le rôle de producteur de données, de géomaticiens, de développeurs ou encore d'usagers.

**Réponse : aucun de ces outils et un peu tous à la fois.**

<!-- markdownlint-disable MD046 -->
!!! note  "L'écosystème de l'époque fonctionnait bien et le projet n'est pas né d'un constat d'échec."
    On avait simplement accumulé, au fil des besoins métier, des outils solides certes mais "silotés" :

    - le Géoportail pour la consultation,
    - les Géoservices pour les flux et les API,
    - MaCarte pour la composition et la diffusion,
    - l'Espace collaboratif pour la contribution.

    Quatre (bons) outils, quatre univers.

    Les passages de l'un à l'autre restaient limités et le cycle de vie de la donnée n'était jamais couvert de bout en bout : produite ici, décrite là, diffusée ailleurs, réutilisée dans un quatrième endroit. Quand le métier consiste précisément à produire, documenter, diffuser et faire réutiliser de la donnée géographique, cette fragmentation finit par avoir un coût.
    Pas en performance, en cohérence.
<!-- markdownlint-enable MD046 -->

**On ne remplaçait donc pas un produit, on essayait de sortir d'un modèle.**

## Guidé par un historique

La tentation de la page blanche existe toujours, sauf que la page n'était pas blanche. 67 millions de visites annuelles sur `geoportail.gouv.fr`. À ce niveau d'usage, on ne réinvente pas, on compose.

Le [géotuileur](https://github.com/IGNF/geotuileur-site) est éclairant. Démonstrateur déployé et testé entre l'été 2022 et l'été 2023, il couvrait déjà une chaîne complète (téléverser, tuiler, appliquer une symbologie, publier le service) avec un objectif qui tenait en une phrase : rendre le producteur autonome pour diffuser et faire connaître ses données. L'expérimentation a été concluante et l'intention comme les fonctionnalités ont été reprises dans [`cartes.gouv.fr`](https://cartes.gouv.fr) et dans [le plugin Géoplateforme pour QGIS](https://plugins.qgis.org/plugins/geoplateforme/), reparti des bases du plugin Géotuileur.

Le point structurel est ailleurs. Chaque outil historique couvrait proprement un segment du cycle de vie, et un seul, sans mécanisme pour passer le relai au suivant. Les usages, eux, avaient bougé.  On ne vient plus seulement consulter une carte, on veut comprendre une donnée, la croiser, l'intégrer dans son SIG, la republier.
**La question n'était plus de savoir si nos briques étaient performantes mais comment elles s'articulaient entre elles.**

## Une doctrine qui paraît simple

**Proposer un point d'accès cohérent aux cartes, aux données et aux services du territoire.**  
Énoncé comme ça, ça paraît évident. C'est justement ce qui rend l'exercice redoutable, parce qu'il faut faire cohabiter des profils qui n'entrent pas par la même porte.

Le développeur cherche une API et sa documentation. Le producteur veut publier et suivre ce que devient sa donnée. Le créateur de cartes veut composer et diffuser. L'animateur de communautés veut fédérer des contributions. Le géomaticien veut surtout que la ressource arrive proprement dans QGIS. Du coup, une question apparemment anodine devient un arbitrage structurant. Par quoi commence-t-on ? Par la carte, par la recherche de données, par les services, par un cas d'usage ? Chaque réponse est défendable, pour un profil différent et chaque personne peut adopter tout ou partie des attentes des profils.

## L'engagement en 2022

En avril 2022, le COPIL Géoplateforme décide d'engager le projet Interfaces, celui qui donnera naissance à [`cartes.gouv.fr`](https://cartes.gouv.fr) . La réponse retenue a été de **ne pas raisonner en fonctionnalités à reprendre, mais en proposition de valeur par profil**. Ce découpage date de l'été suivant (2022), bien avant les premières maquettes.

![Proposition de valeur par profil](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/cartes_gouv_fr_coulisses/cartesgouv_retex_projet.svg){: width="1170px" .img-center }

Ce schéma montre que l'ambition ne portait déjà pas sur un site : usine logicielle, catalogue d'API, bac à sable partenaires, plugin QGIS, studio de création de cartes, fabrique à espaces collaboratifs, outil de création de portails en marque blanche. Il fournit aussi un instrument de mesure rudimentaire, puisqu'il suffit de le relire aujourd'hui pour voir ce qui est en service, ce qui a été transformé en chemin et ce qui attend toujours.
Le bloc « outil de création de portails » mérite qu'on s'y arrête. Une plateforme qui permet à d'autres de fabriquer leurs propres portails accepte, par construction, de ne plus être le point d'entrée unique.

## Donner une forme aux idées

Avant les développements, il a fallu rendre le projet tangible. Les premiers mois ont été consacrés à la réalisation de filaires et de maquettes permettant de matérialiser les parcours imaginés lors du cadrage. À ce stade, l'objectif n'était pas de dessiner l'interface définitive mais de vérifier que les différentes briques pouvaient s'articuler de manière cohérente pour les utilisateurs.

![Filaire de cartes.gouv.fr](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/cartes_gouv_fr_coulisses/cartesgouv_retex_filaire.png ){: width="1700px" .img-center .caption  }

Le travail ne s'est ensuite jamais vraiment arrêté. Les développements ont fait émerger de nouvelles questions, les retours utilisateurs ont conduit à revoir certains parcours et l'arrivée progressive des différents composants a nécessité des ajustements réguliers.
**L'UX/UI n'a donc pas été une étape préalable au projet mais un compagnon de route présent jusqu'aux dernières livraisons, et encore aujourd'hui.**

## La tentation de l'isofonctionnel

**Construire une plateforme ne consiste pas à reproduire l'existant dans une interface plus moderne.** La tentation de l'isofonctionnel reste pourtant forte, et elle est rationnelle. On reprend, on transpose, on coche, on passe à la suite. C'est rassurant et c'est mesurable.

**La valeur est ailleurs, dans la capacité à raisonner sur le cycle de vie complet de la donnée.**

![Cycle de vie de la donnée](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/cartes_gouv_fr_coulisses/cartesgouv_retex_cycle.svg){: width="400px" .img-center }

Comment une donnée est-elle produite, validée, documentée, diffusée ? Comment la retrouve-t-on ? Et comment finit-elle réellement réutilisée, dans un SIG ou une application métier ? Ce parti pris impose des choix structurants à court terme : maintenir une cohérence forte entre données et métadonnées, préférer l'automatisation aux interventions manuelles, chercher la convergence entre produits au lieu de laisser chacun régler son problème dans son coin…

## Les métadonnées, ce sujet fréquemment relégué au second plan

Les métadonnées ont longtemps été traitées comme une obligation. On les renseigne pour la conformité, sans supposer que quiconque les lise. Les usages disent l'inverse. On ne cherche pas seulement à visualiser, on veut savoir d'où vient la donnée, ce qu'elle contient, comment elle est diffusée, à quelles conditions elle est réutilisable. Comprendre avant de télécharger. Et elles ne servent pas qu'à être lues, on s'appuie dessus pour automatiser, à commencer par l'index Géoplateforme.
**Entretenir un produit pour sa diffusion, c'est le décrire une fois proprement** plutôt que de traîner les scories d'un contenu maintenu à la main dans un gestionnaire de contenu (CMS).

C'est le rôle qu'a pris le Datahub, appuyé sur [GeoNetwork-UI](https://github.com/geonetwork/geonetwork-ui), une brique éprouvée et portée par une communauté européenne. Construire avec l'existant plutôt que réinventer localement ce que d'autres améliorent déjà.

L'effet de bord est largement sous-estimé. Il a fallu reprendre les métadonnées elles-mêmes, celles diffusées par l'infrastructure du Géoportail, produits IGN comme produits partenaires. Fiche par fiche.

## Faire du mode produit sans pouvoir montrer

C'est la difficulté la plus réelle du projet, et elle n'a rien de technique.

**Le mode produit repose sur le triptyque : livrer tôt, observer, ajuster.**
Dans la sphère publique, l'exigence d'irréprochabilité immédiate prend le pas : si une fonctionnalité n'est pas totalement aboutie, elle est écartée « à plus tard », ce qui, dans un programme de cette envergure, signifie souvent aux calendes grecques.
Faute de pouvoir ouvrir pleinement le dialogue avec les communautés pour nourrir le produit de retours qualitatifs, les arbitrages se sont faits en circuit fermé, à partir d'un échantillon d'avis trop étroit pour être représentatif.
S'ajoute une réalité qu'on oublie en regardant l'interface. **Cartes.gouv.fr est un client de la Géoplateforme**, pas son propriétaire. Il consomme des API, un index, des services qui ont leur propre trajectoire et servent d'autres clients. Beaucoup de sujets produit ne se règlent donc pas dans l'IHM (Interface Homme Machine) mais en amont, à un rythme qui n'est pas celui du portail. C'est le prix normal de la mutualisation, et ça déplace une partie du travail produit vers la gestion de dépendances.

Des exemples de reports, il y en a eu. J'en retiens cinq :

- [**Le catalogue d'attributs**](https://github.com/geonetwork/geonetwork-ui/pull/1206) (*feature catalog*) de "*Rechercher une donnée*", qui décrit le contenu réel d'une donnée champ par champ. C'est ce qui permet de connaitre le modèle de données de ce qu'on télécharge avant de le télécharger, bien plus ergonomique que le format PDF.
- [**Les réutilisations affichées dans les fiches**](https://github.com/geonetwork/geonetwork-ui/issues/1140) de "*Rechercher une donnée*", pour montrer ce que d'autres ont fait d'une donnée. Souvent le signal le plus parlant sur son intérêt.
- [**L'explorateur de capacités**](https://github.com/geonetwork/geonetwork-ui/issues/1139) de "*Rechercher une donnée*" qui décrit les données mises à disposition dans les fiches API/Services.
- **Un catalogue de styles**, qui permettrait de récupérer les styles proposés par le producteur de la donnée, voire par la communauté, au lieu de les refaire chacun de son côté. L'intérêt saute aux yeux avec le plugin [BD TOPO® Extractor](https://plugins.qgis.org/plugins/bd_topo_extractor/) : on extrait une couche, puis il faut reconstruire à la main une symbologie que le producteur a déjà définie quelque part, ou exploiter celle proposée par le propriétaire du plugin.
- **Le nettoyage de l'index Géoplateforme**, moins visible et plus structurant. Il conditionne la recherche de couches dans *Explorer* de cartes.gouv.fr et la capacité des IHM tierces — SIG, plugins, applications métier — à exploiter proprement l'offre. Le symptôme se constate en trois clics : dans les filtres d'Explorer de cartes.gouv.fr, la catégorie « Autres » rassemble 384 entrées côté thématique et 410 côté producteur.

![Capture cartes.gouv.fr](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/cartes_gouv_fr_coulisses/cartesgouv_retex_cartalogue.png){: width="300px" .img-center }

Les trois premiers ont été financés par le programme Géoplateforme et sont [disponibles](https://github.com/geonetwork/geonetwork-ui/releases?page=2#release-v2.6.0) depuis la fin de l'été 2025. Restent à les activer et à pousser du contenu dans le GeoNetwork de la Géoplateforme. Le catalogue de styles, lui, en est resté à l'état de souhait.

Aucun de ces sujets ne fait une annonce, et c'est probablement ce qui les condamne à glisser. Une fois déployés, en revanche, ils se voient immédiatement, puisque ce sont eux qu'on rencontre en cherchant une couche, en lisant une fiche ou en branchant un SIG.
**Le coût du report ne se manifeste jamais comme un incident, il se manifeste comme un contournement.**
L'utilisateur qui abandonne la recherche de couches. Celui qui va chercher la description des champs ailleurs. Celui qui recompose son index dans son [coin](https://github.com/Geoplateforme/plugin_idg_gpf). Les retours terrain tranchent assez nettement : **mieux vaut un service imparfait mais utile qu'un service théoriquement parfait qui tarde à répondre à un besoin réel.**

## Des petites équipes et la cohérence à tenir

Un aspect dont on parle peu, parce qu'il ne se voit ni dans l'interface ni dans les dépôts : l'organisation du travail.

Un duo produit et technique en pilotage, un product manager et un lead dev, et autour plusieurs petites équipes organisées sur le même modèle, chacune avec son couple product owner et tech lead sur un composant : Explorer, Rechercher, Publier de cartes.gouv.fr, les extensions cartographiques, le plugin Géoplateforme QGIS, la documentation.

C'est efficace, chaque équipe est autonome et développe une vraie expertise sur son périmètre.
En contrepartie, **la cohérence cesse d'être un effet secondaire du développement pour devenir un travail à part entière.** Ce n'est la faute de personne, c'est mécanique. Chaque équipe optimise légitimement son composant, et l'articulation entre composants n'a pas de propriétaire naturel.
Concrètement, ça veut dire arbitrer entre vitesse locale et convergence globale, écarter une solution locale élégante parce qu'elle diverge, répéter la même intention à plusieurs endroits, vérifier qu'une décision prise ailleurs a été comprise de la même manière. Le duo de tête tient le pourquoi et l'ordre des priorités d'un côté, le comment et la chaîne de dépendances de l'autre.

C'est aussi la partie la plus difficile à valoriser, puisqu'elle ne produit aucune fonctionnalité identifiable.

## Le design system de l'Etat (DSFR) ne fait pas de cartes

Comme tout service numérique de l'État, cartes.gouv.fr doit respecter le [système de design de l'État](https://www.systeme-de-design.gouv.fr/version-courante/fr). C'est plutôt une bonne chose, entre la cohérence d'ensemble des sites publics et l'accessibilité. Mais le DSFR ne couvre pas la cartographie. Ni sélecteur de couches, ni légende, ni widget de zoom, ni recherche géographique, ni gestion des styles. Il fallait donc s'écarter du référentiel ou produire ce qui manquait.

On a choisi de produire une bibliothèque publique : la bibliothèque d'extensions [geopf-extensions-openlayers](https://github.com/IGNF/geopf-extensions-openlayers), sous licence AGPL-3.0. Des widgets alignés sur l'identité de l'État, utilisables dans n'importe quelle application cartographique. Rien de ce qu'affiche cartes.gouv.fr ne lui appartient en propre.

![bibliothèque d'extensions geopf-extensions-openlayers pour page internet avec composante cartographique au design-system de l'Etat ou non](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/cartes_gouv_fr_coulisses/cartesgouv_retex_geopf-extensions-openlayers.png){: width="2680px" .img-center }

**Une obligation réglementaire devenue un actif partagé, et enrichissable avec de nouveaux widgets** (contributeurs, n'hésitez pas).

Même logique avec le [plugin Géoplateforme pour QGIS](https://github.com/Geoplateforme/plugin-qgis-geoplateforme), porte d'entrée plus naturelle qu'une interface web pour une grande partie des géomaticiens. En repartant des bases du Géotuileur, entre avril et décembre 2025, il est distribué en GPLv2+ depuis le [dépôt officiel des plugins QGIS](https://plugins.qgis.org/plugins/geoplateforme/) et [documenté ici](https://geoplateforme.github.io/plugin-qgis-geoplateforme/).
Il se synchronise avec cartes.gouv.fr pour la publication et la découvrabilité des services ainsi que pour l'interface de style. Il fonctionne comme un fédérateur de plugins : [GPF Isochrone / Isodistance / Itinéraire](https://plugins.qgis.org/plugins/gpf_isochrone_isodistance_itineraire/), [French Locator Filter](https://plugins.qgis.org/plugins/french_locator_filter/), [QGiréférentiels](https://plugins.qgis.org/plugins/qgireferentiels/), [BD TOPO® Extractor](https://plugins.qgis.org/plugins/bd_topo_extractor/) ; plutôt que comme un monolithe.
La liste a vocation à s'allonger, avec des plugins qui ne viendront pas forcément de l'IGN. C'est le travail de mon successeur.

![Plugin GPF pour QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/cartes_gouv_fr_coulisses/cartesgouv_retex_pluginQGIS.png ){: width="1400px" .img-center }

## Structurant, mais pas bloquant

Une plateforme impose des choix. Bibliothèque cartographique, référentiel de design, socle de catalogage, standards d'échange. Sans eux, pas de cohérence possible.

La ligne à suivre tient dans une distinction. **Un choix structurant fixe une direction, un choix bloquant interdit les usages qu'on n'avait pas prévus.**
Le test est simple, il suffit de se demander si quelqu'un peut faire autrement que nous avec les mêmes briques. En pratique, ça veut dire exposer les composants indépendamment de l'application, garder API, flux et métadonnées accessibles hors interface, et ne jamais faire du portail le chemin obligatoire vers la donnée. C'est aussi ce qui rend les reports évoqués plus haut coûteux, parce qu'un index propre ou un catalogue d'attributs ne sert pas qu'au portail. Il sert à tout ce qui se branche dessus.

## Ouvrir le code, et le reste

L'ouverture est souvent comprise dans un seul sens : diffuser des données. C'est le socle, et la Géoplateforme l'assume, elle héberge et diffuse les données d'autres producteurs que l'IGN. Le plus intéressant concerne l'ouverture des briques logicielles :

- la bibliothèque d'extensions **[geopf-extensions-openlayers](https://github.com/IGNF/geopf-extensions-openlayers),** développées pour [Explorer de cartes.gouv.fr](https://cartes.gouv.fr/explorer-les-cartes/) et utilisables telles quelles dans n'importe quel site, gouvernemental ou non ;
- le **Datahub**, qui porte [Rechercher de cartes.gouv.fr](https://cartes.gouv.fr/catalogue/search), construit au sein de la communauté [GeoNetwork-UI](https://github.com/geonetwork/geonetwork-ui) aux côtés de [Camptocamp](https://camptocamp.com/) ;
- le **[plugin Géoplateforme pour QGIS](https://github.com/Geoplateforme/plugin-qgis-geoplateforme),** conçu et financé par l'IGN, développé par [Oslandia](https://oslandia.com/), un financement dont ont également bénéficié [French Locator Filter](https://plugins.qgis.org/plugins/french_locator_filter/) et, à travers lui, la [Base Adresse Nationale](https://adresse.data.gouv.fr/) ;
- **Geostyler**, qui sert à donner une symbologie à une donnée publiée depuis [Publier de cartes.gouv.fr](https://cartes.gouv.fr/publier-une-donnee), entretenu par une [communauté active](https://geostyler.org/codesprint-2025/).

La documentation suit la même règle, et l'ouverture ne porte pas que sur le code. Le [site d'aide](https://cartes.gouv.fr/aide/fr/) est un site statique généré avec [Eleventy](https://www.11ty.dev/), à partir du [template eleventy-dsfr de codegouvfr](https://github.com/codegouvfr/eleventy-dsfr), avec Pagefind pour la recherche. Surtout, les contributeurs de l'écosystème [cartes.gouv.fr](https://cartes.gouv.fr) et Géoplateforme peuvent y publier leur propre documentation.

Le 4 décembre 2024, à [Open Source Experience](https://www.opensource-experience.com/), le concours [Les Acteurs du Libre](https://cnll.fr/news/laur%C3%A9ats-des-acteurs-du-libre-2024/) organisé par le CNLL a décerné son Prix de la collaboration public-privé à l'IGN et Camptocamp pour le travail mené sur GeoNetwork-UI et le Datahub. Le plugin Géoplateforme, lui, a été bien accueilli aux Rencontres des Utilisateurs Francophones de QGIS, à Avignon, le 11 juin 2025. **Ces distinctions ne portent pas sur le portail, elles portent sur les briques.**

## Durer

C'est le sujet dont on parle le moins. **Contribuer n'est pas un acte ponctuel**, et c'est là que les démarches publiques peinent à se maintenir sur le long terme (mais je suis confiant).
On finance un développement, on livre, l'attention passe au chantier suivant. Six mois plus tard la version amont a avancé sans nous et la dette qu'on voulait éviter réapparaît ailleurs. Durer coûte du temps de développeur sur du code qui n'est pas le nôtre, mais pas seulement. Il faut animer, participer à la conception en amont, relire les contributions des autres, être présent là où se décident les orientations, cofinancer des évolutions dont on ne sera pas l'unique bénéficiaire. Aucune de ces lignes n'apparaît dans un bilan de projet.

Le périmètre est déjà large — GeoNetwork-UI, QGIS et ses plugins, OpenLayers, GeoStyler, le DSFR  — et à chaque fois l'IGN est passé d'utilisateur à contributeur. Mais cela reste à formaliser au travers de financements récurrents, d'engagement de maintenance, de siège dans une gouvernance.

## Où on en est

L'ouverture aux professionnels, le 15 décembre 2025, est la première étape réelle de la bascule. Cartes.gouv.fr cesse d'être un site pour devenir une offre, un ensemble de produits cohérents entre eux, désignés par ce qu'ils permettent de faire : **Explorer**, **Rechercher**, **Publier**.

![Identité visuelle de Cartes.gouv.fr](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/cartes_gouv_fr_coulisses/cartesgouv_retex_logo.png ){: width="500px" .img-center }

C'est là que s'arrête mon rôle sur le projet. **Le socle est posé, les choix structurants assumés, les briques publiées**, et ce qui reste relève de l'ajout plutôt que de la fondation.
Mes derniers faits d'armes de ce début d'année 2026 auront permis de boucler la VSR (Validation de Service Régulier) du plugin Géoplateforme pour QGIS, d'embarquer des plugins tiers, tout en élargissant la communication vers les réseaux sociaux professionnels, au-delà du cercle initial de bêta-testeurs mobilisés sur [Tchap](https://tchap.gouv.fr/#/room/#PluginQgisGoplateformeKDBGAqBBfs:agent.dev-durable.tchap.gouv.fr).

L'[ouverture au grand public](https://www.ign.fr/institut/espace-presse/cartesgouvfr-le-nouveau-site-souverain-de-cartographie) a suivi à l'été 2026. Vue de l'extérieur, c'est le lancement, le moment dont on parle. Côté fonctionnalités, la principale nouveauté tenait à l'arrivée de [Panoramax](https://panoramax.fr/), le reste était déjà en service. Le gros du travail était ailleurs, dans les dispositions programmées pour accompagner les utilisateurs et dans le contenu de documentation à verser.

La suite est [engagée](https://cartes.gouv.fr/evolutions/). **Collaborer** reprendra le rôle de l'Espace collaboratif, et **Éditer des cartes** celui de MaCarte. Les briques historiques ne reviennent donc pas une à une sous forme d'équivalents modernisés, mais comme des entrées d'une même offre, sur un socle commun.

## Relier plutôt qu'ajouter

**Il ne s'agissait pas de construire un portail supplémentaire, mais de relier des mondes qui se côtoyaient sans dialoguer.**

Relier la donnée à sa documentation. Faciliter le passage de la publication à la réutilisation. Rapprocher les producteurs de données de ceux qui les utilisent au quotidien. Fédérer progressivement des producteurs aux pratiques, aux outils et aux contraintes différentes afin de rendre leurs données plus faciles à découvrir, comprendre et exploiter. Relier les outils historiques aux usages émergents. Et, plus largement, faire dialoguer un service public avec les communautés qui peuvent contribuer à son enrichissement.

Le résultat reste perfectible, comme toute plateforme vivante. L'apport le plus intéressant n'est sans doute pas le site, mais la tentative de traiter la donnée géographique comme un continuum. C'est aussi ce qui permet de passer la main sans trop d'inquiétude.
Un socle posé, des briques publiées, des communautés qui s'en emparent. À condition d'y contribuer encore!

**Les portails finissent par vieillir. Les écosystèmes peuvent grandir.**

----
P.S. : Le 30 septembre 2026, le **Géoportail** fermera définitivement ses portes pour rejoindre [cartes.gouv.fr](https://cartes.gouv.fr), pour en savoir [plus](https://cartes.gouv.fr/actualites/le-geoportail-rejoint-cartesgouvfr).

Pour rejoindre la communauté [Géoplateforme et Cartes.gouv.fr](https://www.expertises-territoires.fr/jcms/pl1_557493/fr/communaute-geoplateforme-et-cartes-gouv)

## Ressources

- [cartes.gouv.fr](https://cartes.gouv.fr)
- [geopf-extensions-openlayers](https://github.com/IGNF/geopf-extensions-openlayers) : extensions Géoplateforme pour OpenLayers (AGPL-3.0)
- [plugin Géoplateforme pour QGIS](https://github.com/Geoplateforme/plugin-qgis-geoplateforme) : [documentation](https://geoplateforme.github.io/plugin-qgis-geoplateforme/), [dépôt officiel des plugins QGIS](https://plugins.qgis.org/plugins/geoplateforme/)
- [GeoNetwork-UI](https://github.com/geonetwork/geonetwork-ui) : socle du Datahub
- [géotuileur](https://github.com/IGNF/geotuileur-site) : dépôt archivé de l'expérimentation 2022-2023
- [Les Acteurs du Libre 2024](https://cnll.fr/news/laur%C3%A9ats-des-acteurs-du-libre-2024/) : palmarès du CNLL, et l'[annonce de Camptocamp](https://camptocamp.com/fr/actualites-evenements/acteurs-du-libre-2024)
- [rencontres QGIS d'Avignon du 11 juin 2025](https://conf.qgis.osgeo.fr/2025/07/08/publication-videos-conferences.html)

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-nc-sa.md" %}
