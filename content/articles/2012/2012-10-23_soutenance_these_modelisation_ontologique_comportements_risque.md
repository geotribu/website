---
title: "Soutenance de thèse : Modélisation ontologique des connaissances expertes pour l'analyse de comportements à risque"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2012-10-23
description: "Soutenance de thèse : Modélisation ontologique des connaissances expertes pour l'analyse de comportements à risque"
tags:
    - ontologie
    - spatial ontologie
    - SWRL
---

# Soutenance de thèse : Modélisation ontologique des connaissances expertes pour l'analyse de comportements à risque

:calendar: Date de publication initiale : 23 octobre 2012

![icône globe](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "icône globe"){: .img-thumbnail-left }

Vous êtes dans la région (Sophia Antipolis) le 30 Novembre (14h) et le domaine des ontologies vous intéresse ? Alors, n'hésitez pas à passer pour assister à ma soutenance de thèse. Celle-ci porte sur la modélisation ontologique des connaissances expertes pour l'analyse de comportements à risque. Cette modélisation a été plus spécifiquement appliquée à la surveillance maritime. Je vous laisse découvrir ci-dessous le résumé :

Dans nos sociétés où l'information est devenue omniprésente, la capacité à pouvoir capter et exploiter celle-ci est un enjeu majeur pour toute entité amenée à prendre une décision. En effet, de cette capacité dépendent ensuite les actions et les moyens d'interventions qui seront engagés. Mais, face à l'augmentation des données disponibles, au nombre croissant d'acteurs et à la complexification des menaces, l'environnement dans lequel évolue le décideur est marqué par une grande incertitude.

Ce constat général se retrouve également au sein du domaine de la surveillance maritime qui se caractérise par des menaces hétérogènes, par une zone d'action très vaste et par un réseau d'acteurs important. La recrudescence de la piraterie ou encore l’impact des récentes catastrophes écologiques sont des exemples concrets de la nécessité de disposer de nouveaux moyens de surveillance. Des initiatives gouvernementales ou privées ont donc été menées afin de développer des systèmes aux capacités d’acquisition et d’analyse améliorées (Jangal et al. 2009; Morel et al. 2007; Jangal et al. 2008). Ces derniers s’appuient notamment sur une composante majeure, la détection de comportements anormaux de navires. Pour y parvenir, une formalisation fine de la connaissance experte est nécessaire. Mais, le nombre important de données, la complexité des situations, l’absence de prise en compte de la dimension spatiale ou encore les différentes interprétations potentielles, font que cette modélisation est actuellement insuffisamment exploitée. De ce fait, cette thèse se propose d'étudier les potentialités des ontologies spatiales pour la description des comportements anormaux de navires. Pour cela, les connaissances expertes ont été dans un premier temps formalisées sous la forme d'une ontologie. Ces connaissances étant géographiques par nature, il a été nécessaire d'étendre le langage Semantic Web Rule Language (SWRL) afin de prendre en compte cette dimension. Les ontologies créées ont par la suite été intégrées au sein d'un système entièrement dirigé par une ontologie spatiale à laquelle est associé un moteur d’inférence géographique (Vandecasteele and Napoli 2012). L'objectif de ce prototype est de permettre à la fois l'identification des navires potentiellement suspects mais aussi les scénarios probables définis par les opérationnels. Les détails de ces deux principales étapes sont décrits dans les paragraphes suivants.

Formaliser la connaissance experte nécessite de disposer d'un formalisme de représentation suffisamment riche pour traduire les différentes notions et les liens du monde réel. À l'heure actuelle, c'est le domaine des ontologies et plus particulièrement celui du Web Sémantique qui concentre l'essentiel des travaux, langages et outils. Néanmoins, malgré les potentialités descriptives offertes, aucun standard, ni aucun consensus n'existent pour l'intégration des connaissances spatiales (Dia Miron 2009). Or, pour la description du comportement des navires cette dimension géographique est nécessaire. Dans le cadre de cette thèse, une modélisation du domaine ainsi qu'une extension du langage de règle SWRL ont donc été proposées. Celles-ci offrent aux experts de la surveillance maritime les éléments nécessaires à la description de connaissances spatiales.  
La modélisation du domaine repose à la fois sur le travail réalisé par Yan (Yan 2011) et sur la notion de trajectoire sémantique (Spaccapietra et al. 2008). Trois ontologies ont alors été créées. La première est relative aux concepts géométriques pour la modélisation des trajectoires, la seconde porte sur la description géographique des concepts et la dernière est directement liée au domaine étudié. Les positions initiales des navires sont alors enrichies pour ensuite former des trajectoires sémantiques. À partir de ces trajectoires, les experts du domaine peuvent créer des règles décrivant une situation anormale. Le choix du langage de règles utilisé s'est porté sur le Semantic Web Rule Language (SWRL). Celui-ci dispose déjà d'opérateurs de comparaison (mathématique, chaîne de caractères, etc.) qu'il est également possible d'étendre grâce aux points d'extensions nommés Built-ins (Horrocks et al. 2004). C'est cette approche qui a été choisie pour l'intégration de la dimension spatiale. Ainsi, de simples mots-clés comme intersects ou touches suffisent à définir un atome spatial qui permettra de vérifier la satisfiabilité ou non d'une règle.  
Une fois la connaissance modélisée, il est alors possible de l'intégrer au sein d'un système de surveillance maritime. Dans le cadre de cette thèse, un prototype nommé OntoMap a été développé. Celui-ci est composé de différents modules dont les deux principaux sont le module d'inférence et le module de Raisonnement À Partir de Cas. Le premier compare les positions et les trajectoires des navires aux règles SWRL définies préalablement. Le second met en correspondance les alertes potentielles d'un navire et les scénarios définis par les experts du domaine. Enfin, les résultats sont affichés sur une interface cartographique. De par ses caractéristiques, cette carte offre un accès facilité à l'information ainsi qu'une utilisation intuitive.

Les travaux présentés dans cette thèse se situent au croisement de la gestion des connaissances et du raisonnement spatial. Il s'agit en effet d'étudier les défis et les avantages qui découlent d'une exploitation maîtrisée des informations spatiales à des fins décisionnelles. Pour cela une modélisation des connaissances expertes ainsi qu'un prototype de système de surveillance maritime ont été proposés. Bien que les tests de performance effectués montrent qu'une utilisation en temps réel est pour le moment prématurée, il est néanmoins possible de s'appuyer sur l'approche présentée lors notamment des phases de retour d'expérience. Au-delà du domaine maritime, ce travail de recherche propose également une formalisation des règles spatiales sous la forme d'une extension du langage SWRL. Des mots clés tels que intersects ou touches sont traités par le moteur d'inférence comme significatif d'une fonction spatiale et utilisés comme paramètre afin d'exprimer des règles de comportements.

## Bibliographie

- Horrocks, Ian, Peter Patel-Schneider, Harold Boley, Said Tabet, Benjamin Grosof, and Mike Dean. 2004. “SWRL: A Semantic Web Rule Language Combining OWL and RuleML.” <http://www.w3.org/Submission/SWRL/>.
- Jangal, Florent, Jean-Pierre Georgé, Alain Bonnot, Marie-Annick Giraud, Michel Morel, Aldo Napoli, and Anne Littaye. 2009. “Toward a Complete System for Surveillance of the Whole EEZ: ScanMaris and Associated Projects.” In OCEANS 2009, MTS/IEEE Biloxi - Marine Technology for Our Future: Global and Local Challenges, 1 –4.
- Jangal, Florent, Marie-Annick Giraud, Anne Littaye, Michel Morel, Jean-Pierre Mano, and Aldo Napoli. 2008. “Extraction of Suspicious Behavior of Vessels in the Exclusive Economic Zone.” In International Symposium on Antennas Et Propagation.
- Dia Miron, Alina. 2009. “Découverte D’associations Sémantiques Pour Le Web Sémantique Géospatial - Le Framework ONTOAST”. THESE, Université Joseph-Fourier - Grenoble I. <http://tel.archives-ouvertes.fr/tel-00635118>.
- Morel, Michel, Marie-Pierre Gleizes, Aldo Napoli, Anne Littaye, Valérie Bazin, Bernard Alhadef, Christian Scapel, Bruno Leroy, Jacques Lebrevelec, and Daniel Dejardin. 2007. “Scanmaris: An Adaptative and Integrated Approach for Wide Maritime Zone Surveillance.” In Cognitive Systems with Interactive Sensors (COGIS 2007), 10–14. Stanford University California USA.
- Spaccapietra, Stefano, Christine Parent, Maria Luisa Damiani, Jose Antonio de Macedo, Fabio Porto, and Christelle Vangenot. 2008. “A Conceptual View on Trajectories.” Data & Knowledge Engineering 65 (1) (April): 126–146.
- Vandecasteele, Arnaud, and Aldo Napoli. 2012. “Enhancement of Ontology with Spatial Reasoning Capabilities to Support Maritime Anomaly Detection.” In SOSE 2012. Genova, italie.
- Yan, Zhixian. 2011. “Semantic Trajectories: Computing and Understanding Mobility Data”. Phd, Ecole Polytechnique Fédérale de Lausanne.

## Localisation de la soutenance

MINES ParisTech salle R017, bâtiment I

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe width="500" height="500" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://cartosm.eu/map?lon=7.0531001430518&amp;lat=43.615313044755&amp;zoom=17&amp;width=400&amp;height=350&amp;mark=true&amp;nav=true&amp;pan=true&amp;zb=inout&amp;style=default&amp;icon=down"></iframe>`

----

<!-- geotribu:authors-block -->
