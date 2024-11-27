---
title: Retour sur le SotM 2024
subtitle: Attention à votre environnement
authors:
    - Romain LACROIX
categories:
    - article
comments: true
date: 2024-12-03
description: Romain Lacroix était au State of the Map France 2024 à Lyon et nous livre ce qui l'a marqué et ce qu'il a retenu.
icon: simple/openstreetmap
image:
license: default
robots: index, follow
tags:
    - conférence
    - OpenStreetMap
    - SotM
---

# « *Je portais déjà une grande attention à mon environnement, maintenant c’est pire.* » Retour sur le SotM 2024

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![Logo du SotM 2024 à Lyon](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/sotm_fr_2024.png){: .img-center loading=lazy }

Qu’on se le dise, [OSM France](https://www.openstreetmap.fr/association/), c'est du costaud. Tellement même qu'en assemblée générale ce samedi 29 juin au soir, les contributeurs s'interrogent sur une évolution qualitative du projet associatif.

Point d'orgue de ce **State of the Map**, l'événement annuel des contributeurs, cette AG montre la maturité des actions et des développements produits au sein ou en lien avec OSM en France. Du vendredi au dimanche 30 juin, plus de 300 participants se sont donné rendez-vous à la Manufacture des Tabacs de Lyon pour faire un point d'étape festif sur les avancées des uns et des autres. L'occasion également de se transmettre collectivement des compétences sur leurs pratiques de contribution et d'usage des données.

Il est alors difficile d'en résumer le contenu sans en perdre la richesse des sujets, des techniques et des moyens pédagogiques mis en œuvre pour que tout un chacun y trouve son compte.

De Panoramax à Osmose, des grands référentiels publics (BNB, OCSGE...) à ceux améliorés par OSM (BANO...), des traitements sur la France entière à ceux sur une commune et même à la micro cartographie, **le SotM, bien loin d'être une conférence uniquement centrée sur elle-même, est d'un intérêt tout particulier pour quiconque s'intéresse de près ou de loin au territoire, à l'environnement ou à la géomatique.**

Dès lors, qu'en retenir de façon globale ? Exercice difficile s'il en est, car la concomitance des présentations, dilemme habituel du congressiste, ne permet pas de rendre pleinement compte d'autre chose que ce à quoi il a assisté.

Quelques mots-clés peuvent servir à en décrire le contenu : Panoramax, qualité des données, vélo, trains, IGN, eau, portails d'accès, tourisme, applications, climat, IA, adresses, archivage...

Dans cet article, je vous parlerai donc essentiellement de quelques conférences auxquelles j'ai eu le bonheur d'assister. Pour le reste, les [vidéos](https://peertube.openstreetmap.fr/c/sotm_fr_2024/videos) et les [présentations](http://sotm2024.openstreetmap.fr/programme.html) sont disponibles (ou vont arriver très bientôt) et je rajoute en fin d'article quelques liens plus directs pour fouiller.

![Carte des participants au SotM FR 2024](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/sotm2024/carte_participantsOSM2024.webp){: .img-center loading=lazy }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Intervention inaugurale

- par la métropole de Lyon : H. Greolas retrace l'évolution de la gestion des données (spatiales) de la métropole de Lyon, notamment du MCPP (« Moi C'est Pas Pareil ») à la stratégie open data actuelle basée sur le triptyque « Comprendre (passé), Piloter (présent), Prévoir (futur) »

- puis par l'Université Lyon 3 : sont présentées la richesse actuelle des événements pour les amoureux des cartes avec de nombreuses [conférences](https://ichc2024.univ-lyon3.fr/accueil-fr) et de nombreuses [expositions](https://ichc2024.univ-lyon3.fr/expositions-1) de cartographie en cours dans la capitale des Gaules. Bernard Gauthiez, professeur de géographie, pointe le nécessaire archivage des données numériques en particulier dans les services publics. Petit clin d'œil malicieux du public qui le renvoie sur le travail de Christian Quest, présent dans la salle : [opendatarchives](https://www.opendatarchives.fr/).

- Petits topo éclairs sur quelques sujets :
    - C. Frayssinet nous présente une petite application permettant de proposer de la **formation sur smartphone** (*mobile learning*) avec **[ePoc](https://epoc.inria.fr/)** et comment il a développé une formation à OSM à destination de ses élèves de seconde
    - F. Rodrigo sur la difficulté à avoir de la **lisibilité spatiale et réglementaire sur les zones à faibles émissions** ([BN ZFE](https://transport.data.gouv.fr/datasets/base-nationale-consolidee-des-zones-a-faibles-emissions) « inutilisable », on utilise le tag [boundary = low_emission_zone](https://wiki.openstreetmap.org/wiki/Tag:boundary%3Dlow_emission_zone#France) dans OSM) et leurs liens avec les zones Crit'Air encore bien flous
    - A. Vuillard nous raconte ses **galères à développer des applications SIG** quand on n'a pas l'habitude
    - I. Amri nous présente un **[générateur d'atlas pour faire des cyclorando](http://atlas.iliasamri.com/)** à partir d'une trace GPX
    - Thibault nous renvoie vers son usage d'[OSM Tracker Android](https://wiki.openstreetmap.org/wiki/FR:OSMTracker_(Android)) pour **contribuer en mouvement**
    - J-C. Becquet nous parle des **belles rencontres** que l'on fait **grâce à OSM**

*Un petit ravitaillement juste après ces introductions aurait dû nous mettre la puce à l'oreille que l'activité principale du SotM serait bien physique : la montée des marches jusqu'au 3e étage pour rejoindre les salles de conférence.*

*Pas grand chose en soi. Simplement un soleil voilé. Par plus de 30°C. Et avec 70-80% d'humidité. Ce fut une occasion pour tout le monde d'en apprendre un peu plus sur sa propre résistance aux climats tropicaux humides (absolument médiocre pour ma part), mais également sur l['indice de chaleur](https://fr.wikipedia.org/wiki/Indice_de_chaleur).*

----

## Conférences

### DataSud

:fontawesome-solid-person-chalkboard: T. Emery et V. Canut (Région SUD-PACA)

![logo DataSud](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/DataSud.webp){: .img-thumbnail-left }

Présentation de l'outil [DataSud](https://www.datasud.fr/portal/), plateforme d'open data, mais pas que !

L'infrastructure est pensée pour mettre à disposition des données de différentes natures (dont [la matrice cadastrale MAJIC](https://guides.data.gouv.fr/reutiliser-des-donnees/autour-du-cadastre/manipuler-les-donnees-du-cadastre#faire-lintegration-metier-parcelles-et-majic)) à des publics différents : collectivités, associations, etc. Se voulant un hub de données régionales, DataSud moissonne les données OSM sur les [fichiers diffs](https://wiki.openstreetmap.org/wiki/Planet.osm/diffs) et crée des couches prétraitées grâce à [Osmium](https://github.com/osmcode/), [Osmosis](https://wiki.openstreetmap.org/wiki/Osmosis) et [osm2pgsql](https://osm2pgsql.org/). La base initiale est ainsi digérée en 35 tables définies par un fichier LUA. Puis d'autres tables sont gérées avec des vues thématisées selon [la nomenclature OSM FR](https://wiki.openstreetmap.org/wiki/FR:%C3%89l%C3%A9ments_cartographiques) (plus d'infos [ici](https://gitlab.datasud.fr/projets_publics/openstreetmap4datasud)).

Un [catalogue](https://www.datasud.fr/explorer/fr/recherche) permet des téléchargements dans des formats très divers et des [cartes](https://www.datasud.fr/maps/) sont directement proposées.

!!! quote "Entendu au SotM"
    - Vous savez où sont les toilettes ?
    - Attendez je regarde sur OSM...
    - Ah oui, c'est bon ! Elles sont là, juste à gauche !

### L'OCSGE et le CoSIA de l'IGN : une nouvelle opportunité pour OSM ?

:fontawesome-solid-person-chalkboard: X. Halbecq (IGN) et J.-L. Zimmermann (CD84)

![logo IGN](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/ign.png){: .img-thumbnail-left }

L'occupation du sol à grande échelle (OCSGE) est une nouvelle base géographique vectorielle de référence développée par l'IGN. En deux dimensions, elle vise à **(1) décrire la couverture et (2) l'usage des sols** de la [France entière d'ici fin 2025](https://macarte.ign.fr/carte/VVpbhc/Production-de-l-OCS-GE-NG). La résolution est d'environ 20cm mais l'échelle d'utilisation est a priori entre 1:2500 et 1:5000.  Son développement vient notamment combler les besoins de suivi de la [loi Zéro Artificialisation Nette](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000047866733).

Comment ça marche ?

- des photographies aériennes (RVB & infrarouges) sont récupérées et associées à des MNS et MNT[^mne_mns_mnt]
- un [modèle de *deep learning*](https://ignf.github.io/FLAIR/index_fr.html) entraîné sur un important jeu d'annotations classifie chaque pixel [14 formes de couverture](https://artificialisation.developpement-durable.gouv.fr/sites/artificialisation/files/inline-files/Marque%20page_OCS_GE_sept2017_RV_V3-1_0.png) et [17 formes d'usages du sol](https://artificialisation.developpement-durable.gouv.fr/sites/artificialisation/files/inline-files/Marque%20page_OCS_GE_sept2017_RV_V3-2.png)
- un processus de correction double est ensuite mobilisé pour détecter des anomalies dans la classification automatique :
    - correction par photointerprétation d'un sous-traitant
    - remontées utilisateurs
- un service de [téléchargement de la donnée](https://geoservices.ign.fr/ocsge#telechargement) est proposé, accompagné d'une [feuille de style pour SIG](https://geoservices.ign.fr/sites/default/files/2023-07/Styles_OCSGE.zip) ou même d'un [projet SIG](https://geoservices.ign.fr/sites/default/files/2022-11/Projets_carto_OCSGE.zip)

Autre produit présenté, [CosIA](https://cosia.ign.fr/), traitement purement automatique proposant [une couverture du sol en 16 classes](https://cosia.ign.fr/pdf/Cosia_Nomenclature_IGN_2023.pdf) sur une base vectorisée et simplifiée à une résolution de 20cm. [La précision et l'usage sont assez différents de l'OCSGE](https://cosia.ign.fr/pdf/Comparatif_OCSGE_CoSIA_IGN_2023.pdf) : c'est un pur traitement d'images aériennes, sans corrections, et sans information sur ce qui n'est pas visible. [Le produit est déjà téléchargeable pour quelques départements](https://cosia.ign.fr/info#export).

![Comparatif COSIA OCS GE](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/sotm2024/comparatif_cosia_ocsge.webp){: .img-center loading=lazy }

Ces produits de grande résolution offrent une formidable opportunité pour les cartes OSM françaises : [les données d'utilisation du sol](https://wiki.openstreetmap.org/wiki/FR:Key:landuse) ont historiquement été importées de Corine Land Cover, source relativement grossière et imprécise. La mise à jour régulière annoncée (tous les 3 ans) porte également en elle des espoirs de maintien durable de la qualité des données sur OSM... Mais aussi des problématiques sur les données Corine depuis enrichies et modifiées par la communauté sur OSM et qu'il faudra finement comparer.

!!! note "Une nomenclature sévère avec l'agriculture"
    Avec quelques regrets néanmoins de l'assemblée qui considère la nomenclature choisie relativement sévère sur l'agriculture, rassemblée dans un seul poste avec une absence de distinction des cultures (pérennes / annuelles / vergers / vignes, etc).

### uMap incubé par l'État, ça donne quoi ?

:fontawesome-solid-person-chalkboard: Y. Boniface

![logo uMap](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/umap_logo.png){: .img-thumbnail-left }

L'application [uMap](https://umap-project.org/fr/) qui aide à la création de cartographies interactives personnalisées à partir de couches OSM a passé le million de cartes créées.

De ce succès, notamment dans le cadre de fonction publique, a découlé des financements de la part de l'AIC - [Accélérateur d'Initiatives Citoyennes](https://communs.beta.gouv.fr/) - et de l'[Agence Nationale de la Cohésion des Territoires](https://agence-cohesion-territoires.gouv.fr/). Outre la création d'une [instance spécifique pour les agents de la fonction publique](https://umap.incubateur.anct.gouv.fr/)) afin de ne pas surcharger les serveurs OSM-France, cela a permis le financement de nombreux développements (V2) et nouvelles fonctionnalités présentées :

- Nombreuses améliorations UX (tableau de bord, explorateur, avertissements, alertes, signalisations, panneau de partage, gabarits de pop-up)
- Drag & Drop des données
- Assistant d'import Overpass, recherche GPS
- Formatage conditionnel
- Le clic-droit > "Modifier dans OpenStreetMap"

[:material-cloud-download: Télécharger le support de présentation :fontawesome-solid-file-pdf:](https://nuage.yohanboniface.me/umap_lyon_2024.pdf){: .md-button }
{: align=middle }

### Présentation de Cartes.app

:fontawesome-solid-person-chalkboard: M. Thomas-Quillévéré

![logo cartes.app](https://cdn.geotribu.fr/img/logos-icones/divers/cartes_app.webp){: .img-thumbnail-left }

Cette [présentation](https://peertube.openstreetmap.fr/w/oJwaAP1PbeLsK2zywTzLga) de Maël Thomas-Quillévéré m'a fait forte impression et je ne pense pas être le seul étant donné sa limpidité et son engagement. Vous pouvez d'ailleurs la revisionner [ici](https://peertube.openstreetmap.fr/w/oJwaAP1PbeLsK2zywTzLga). Il est rare que des développeurs tombent le masque et affichent des positions qui ne soient pas consensuelles pour les congressistes. Cette radicalité a pour elle de nous rappeler à l'acceptabilité éthique et morale de nos développements. En l'occurrence, Maël plante immédiatement le décor du problème à résoudre avec [ce graphique](https://ourworldindata.org/grapher/co2-mitigation-15c) montrant les réductions d'émissions à effectuer pour atteindre des objectifs climatiques qui ne soient pas irrémédiables pour notre planète et ses habitants des différentes espèces.

En France, 1/4 de l'empreinte environnementale est liée à la voiture et 90% des dépenses totales de mobilité (privées + publiques) vont pour le système "voiture".

Par ailleurs, l'application de mobilité dominante en France est Google Maps : une application qui est pensée pour la voiture et qui met en avant des fonctionnalités et des résultats pour la voiture au détriment des autres modes de transport.

La France est très/trop attachée à la voiture et de nombreuses lacunes informationnelles sont pointées quant au [coût réel du système "voiture" dans son ensemble et pour le particulier](https://futur.eco/cout-voiture#introduction), mais aussi sur des solutions comme la voiture électrique qui nage dans un "[océan d'infox](https://bonpote.com/ocean-de-fake-news-sur-la-voiture-electrique/)"

Le parti pris de Maël est que nous avons une *fausse dépendance à la voiture* et que **si les modes de transport alternatifs étaient mieux exposés et promus, bien plus de trajets pourraient s'effectuer avec des modes de transport peu émetteurs de CO2**.

![Étude citée par Maël Thomas-Quillévéré sur le vélo](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/sotm2024/cartesapp-veloetude.webp){: .img-center loading=lazy }

L'application navigateur [**cartes.app**](https://cartes.app/#5.52/46.857/2.025) développée entend prendre le contrepied en proposant  :

- des trajets calculés de façon préférentielle sur des modes doux (via [BRouter](https://brouter.de/brouter-web/#map=6/46.823/-0.791/cyclosm) pour le vélo) ou en transports publics (via [Motis](https://routing.spline.de/?motis=https%3A%2F%2Frouting.spline.de%2Fapi) et l'intégration des GTFS) avec une signalétique (discrète :smile:) sur l'itinéraire voiture. Une navigation possible au sein des différents réseaux de transports publics.
- une mise en avant des lieux de façon non commerciale (un salon de massage ne sera jamais au-dessus d'une gare dans les priorités d'affichage !)
- des données OSM, avec des requêtes Overpass
- une interface de rendu qui soit plus jolie que celle de la carte OSM ! (qui doit être considérée comme une vue de la BDD) avec l'intégration de Panoramax pour la vue immersive
- une application sur navigateur pour des facilités de développement

Les problèmes rencontrés :

- la décentralisation et les silos de données concernant les réseaux de transports publics en France : chaque petite région de mobilité a ses données, a développé son application de transport, mais est très frileuse (modes de gestion public-privé) à l'idée de partager et de rendre tout ça interopérable à l'échelle de la France entière

- La simplification pour le rendu d'autant de données complexes sur le Web : elle peut rendre l'utilisation parfois un peu moins fluide que prévue

- L'installation sur smartphone qui n'est pas toujours évidente pour tout le monde selon l'OS, le navigateur, etc.
- Un modèle économique ? 😉

### Cartographier les cours d'eau

:fontawesome-solid-person-chalkboard: F. Lacombe et J.L. Zimmermann

![icône cours d'eau](https://cdn.geotribu.fr/img/logos-icones/divers/cours_eau.webp){: .img-thumbnail-left }

La restitution de l'expérience acquise par deux grands contributeurs de cette thématique sur OSM a tenu toutes ses promesses. La résolution d'un certain nombre de problèmes de sémantique ou de capillarité a ici été démontrée pour cette thématique d'avenir.

Quand on parle de cours d'eau, on pense évidemment aux lacs ou à la belle rivière coulant sans obstacle, mais la réalité est bien plus complexe que ça à intégrer pour OSM : cours d'eau artificiels, intermittents, de tracé variable ou enterré.

L'attention sémantique pour OSM est d'abord portée sur l'identification du type d'écoulement lié finalement au cycle général de l'eau :

- l'écoulement libre : rivières, canaux...
- l'écoulement sous pression : canalisations, galeries, siphons...
- l'écoulement par infiltration : nappes

Alors pour l'instant OSM ne peut pas représenter l'intégralité de ces éléments, mais 3 objectifs réalistes sont présentés pour la communauté OSM :

- parvenir à décrire l'**hydrographie globale** : le maillage des cours d'eau naturels et artificiels. Ce n'est clairement pas finalisé dans de nombreux territoires et c'est relativement facile à compléter (quoique pas toujours !), sur différentes échelles, différentes activités liées aux cours d'eau (loisirs, tourisme, agriculture, fontaines) et différents éléments affleurants (piézomètres, captages, ripisylves)
- disposer d'une **sémantique détaillée** : définie par l'ensemble des tags utilisés, la sémantique émerge de la communauté par propositions et par uniformisation au niveau mondial. Certains tags ont été supprimés pour les faire évoluer vers des choses plus précises et utilisables. On a maintenant la capacité de décrire un grand nombre d'objets très précisément : à découvrir sans tarder sur le wiki ([FR:Key:inlet](https://wiki.openstreetmap.org/wiki/FR:Key:inlet)). Il reste cependant beaucoup de travaux à mener au niveau des tags ! Une attention doit enfin être portée aux liens avec les **référentiels nationaux** (Sandre notamment) et les standards (Star-EAU)

    ![Schéma d'évolution des tags sur OSM](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/sotm2024/negociation_travailsemantique_osm.webp){: .img-center loading=lazy }

- **compléter l'inventaire : en allant sur le terrain !!**
    - très peu d'objets hors écoulement libre
    - beaucoup d'objets non/mal connectés au réseau, en assurant la connectivité : la base OSM fournit finalement un graphe connexe des cours d'eau et en utilisant <https://waterwaymap.org/> on peut vérifier la connectivité !

    ![Connectivité globale des cours d'eau sur waterwaymap - Crédit : waterwaymap.org](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/sotm2024/waterwaymap.webp){: .img-center loading=lazy }

    - ce qui permet de pallier les manques de la BD Topage, très incomplète et/ou incorrecte qui gagnerait sans doute à intégrer OSM dans ses données.

----

## Conférences parallèles et quelques liens

- [State of Panoramax](https://peertube.openstreetmap.fr/w/iKjt6BjhP9Da54cUxmfohT) par C. Quest & F. Lainez : [Panoramax](https://panoramax.fr/), « *une seule photo pour les servir tous*» (libre, [ouvert](https://gitlab.com/panoramax), commun), [une appli de contribution en alphatest](https://s.42l.fr/panoramax-beta), [une carto des zones à photographier !](https://panoramax.openstreetmap.fr)

- Cartographier les zones climatiques locales avec OSM par E. Bocher : [un package R pour analyse tout ça](https://github.com/orbisgis/lczexplore) et les besoins d'avoir la hauteur des bâtiments remplie dans OSM avec une [méthode d'estimation](https://hal.science/hal-03811271)

- Adiu ! Quand l'union des communs fait la force du patrimoine immatériel par D. Montagne et H. Lopez : cas de l'occitan sifflé, mise en commun de communs [Wikipédia](https://fr.wikipedia.org/wiki/Wikip%C3%A9dia:Accueil_principal), [Wikidata](https://www.wikidata.org/wiki/Wikidata:Main_Page?uselang=fr), [Commons](https://commons.wikimedia.org/wiki/Accueil), [Lingua Libre](https://lingualibre.org/wiki/LinguaLibre:Main_Page) et OpenStreetMap. [Lien vers la présentation](https://hal.science/hal-04628915v1).

- [Atelier de découverte d'OSM](https://peertube.openstreetmap.fr/w/7Pa25evG1WV8Zo5u2AGaRc) par C. Frayssinet : présentation [ici](https://pretalx.com/media/sotm-fr-2024/submissions/YA93ZV/resources/2024_Decouverte_OSM_r%C3%A9duite_iBaHjW7.pdf)

- [Clearance : contrôler collaborativement des données OSM pour des usages thématiques](https://peertube.openstreetmap.fr/w/m9irHASKWBdCLqff9nbLnQ) par V. Bergeot et F. Rodrigo.

- Cartes IGN par N. Berthelot : présentation [ici](https://pretalx.com/media/sotm-fr-2024/submissions/PKLYHN/resources/Appli_Cartes_IGN_SOTM_2024_lZHF0sl.pdf). En attendant <https://cartes.gouv.fr/>

- [Comment SNCF Voyageurs utilise OSM pour calculer l'écart horaire](https://peertube.openstreetmap.fr/w/1Bi7aeGiRFWAXhU61a8gKC) par D. Cheynet

- Cartographie des gares françaises pour l'application "Ma Gare SNCF" avec Wemap par T. Michel : présentation [ici](https://pretalx.com/media/sotm-fr-2024/submissions/7ALMTV/resources/SOTM2024_-_Carto_SNCF_MaGare___Wemap_ZiQkMAN.pdf)

- Production d'une cartographie des zones climatiques locales avec l'outil GeoClimate par E. Bocher et J. Bernard : [Home · orbisgis/geoclimate Wiki · GitHub](https://github.com/orbisgis/geoclimate/wiki)

- Panoramax, les mains dans le cambouis ! par A. Pavie : présentation [ici](https://pretalx.com/media/sotm-fr-2024/submissions/LCQYMZ/resources/2024-06_Pr%C3%A9sentation_r%C3%A9utilisation_techniques__WSEGI6Q.pdf). [Panoramax / Clients / Web viewer · GitLab](https://gitlab.com/panoramax/clients/web-viewer)

- Panoramax, retour d'expérience du SDIS 34 sur ses prises de vue RTK/360° par N. Moyroud : présentation [ici](https://pretalx.com/media/sotm-fr-2024/submissions/BV9LPD/resources/SDIS34_Panoramax_wKYO6Qs.pdf). Le [kit de prise de vues](https://cartocite.fr/le-kit-de-collecte-cartocite/). [Centipède](https://centipede.fr/index.php/view/map/?repository=cent&project=centipede&layers=0B0TTTTTTFT&bbox=-2178936.878916%2C4865478.399287%2C2443974.591128%2C6998377.23626&crs=EPSG%3A3857&layerStyles=buffer50%3Ad%C3%A9faut%3Bbasesrtk%3Ad%C3%A9faut). [Appli Android de connexion au réseau](https://play.google.com/store/apps/details?id=com.lefebure.ntripclient&hl=fr&gl=US&pli=1). Liens à faire le [LIDAR HD](https://geoservices.ign.fr/lidarhd)

- Carto Graou : sous les trains, la carte par N. Wurtz : [Carto Graou Prez](https://prez.carto.tchoo.net/#/pre-coucou)

- Cartographie pour le VTT par L. Morinon : présentation [ici](https://pretalx.com/media/sotm-fr-2024/submissions/HJ7ZLW/resources/SOTM2024-UtagawaVTT_2_e7Jho5z.pdf). [UTAGAWA VTT](https://www.utagawavtt.com/search?city=&w=[-12.48047,39.59722,15.64454,52.88901]&q=[1,2,3,4]&k=0&l=all&u=1&aa=25)

- Mapper les trottoirs pour l'accessibilité par F. Lainez et M. Nicolas : présentation [ici](https://pretalx.com/media/sotm-fr-2024/submissions/RR8LHN/resources/Mapper_des_trottoirs_pour_laccessibilit%C3%A9_XvYiUhZ.pdf)

- Architecture SIG au SDIS34 pour l'exploitation des données OSM par N. Moyroud : présentation [ici](https://pretalx.com/media/sotm-fr-2024/submissions/83N9QQ/resources/architecture_SIG_OSM_SDIS34_RVKi3xx.pdf). [LeBonTag](https://www.lebontag.fr/)

- Underpass-API : requêtes Overpass sur une base SQL par F. Rodrigo : présentation [ici](https://pretalx.com/media/sotm-fr-2024/submissions/A3TRQ8/resources/Underpass_API_sTKVXij.pdf)

- Géocoder efficacement avec BANO et Addok F. Rodrigo : présentation [ici](https://pretalx.com/media/sotm-fr-2024/submissions/9XBWWA/resources/G%C3%A9ocoder_effectivement_avec_BANO_et_Addok_BYTKxkM.pdf)

- Le [stationnement cyclable dans les grandes villes européennes](https://peertube.openstreetmap.fr/w/pxjVCP4BYEEowJXvL7y4Fy) par [GeoVélo](https://geovelo.app/fr/). Selon leur classement, dépendant des données remontées, Lyon est la meilleure ville française en nombre de stationnement vélo /hab.

- [OSMTracker-Android : personnaliser, contribuer et maintenir](https://peertube.openstreetmap.fr/w/51rvQ2UVMbC8fwUs9NZB8y) par Thibtib51

----

## Conclusion

Voilà pour ce petit article sur cette édition 2024 du SotM. Beaucoup de liens dans tous les sens, il faut dire que c'était riche ! J'espère que ça vous en a donné un aperçu, l'idée était de revenir sur quelques conf qu'il me semblait intéressant à partager au plus grand nombre. En espérant vous avoir donné envie de participer une prochaine fois et bien sûr de contribuer à openStreetMap :wink:. Merci de m'avoir lu, je vous laisse avec la vidéo rétrospective et un [autre compte-rendu de l'événement](https://mschauli.fr/2024/06/29/cartographier-le-temps-dun-week-end-%F0%9F%97%BA%EF%B8%8F/) suggéré par Delphine en relecture :

<iframe title="Retour sur le SOTM∙France₂₀₂₄ | Édition 2024" width="100%" height="400" src="https://peertube.openstreetmap.fr/videos/embed/e827c08c-f4d1-4ca2-9a65-555aa28f5b5c" frameborder="0" allowfullscreen="" sandbox="allow-same-origin allow-scripts allow-popups allow-forms"></iframe>

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}

<!-- Notes de bas de page -->
[^mne_mns_mnt]:
    Modèles Numérique d'Élévation, Surface ou Terrain : description altimétrique du sol, des structures (bâtiments, végétaux...) à partir de photogrammétrie. On parle parfois aussi de MNC pour la Canopée. Pour plus d'informations, consulter la [page de l'IGN](https://geoservices.ign.fr/actualites/2020-12-10-MNT-MNS) ou [Wikipedia](https://fr.wikipedia.org/wiki/Mod%C3%A8le_num%C3%A9rique_de_terrain).
