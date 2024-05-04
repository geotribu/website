---
title: "Sortie de QGIS 1.2.0 'Daphnis'"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-09-04
description: "Sortie de QGIS 1.2.0 'Daphnis'"
tags:
    - GIS
    - logiciel
    - open source
    - QGIS
---

# Sortie de QGIS 1.2.0 'Daphnis'

:calendar: Date de publication initiale : 04 septembre 2009

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-thumbnail-left }

Il y a quelques jours sur la liste OSGEO-fr j'ai eu le bonheur d'apprendre la sortie de la version 1.2.0 de QGIS. Je me fais donc l'écho Jean Roc Morreale et reprends ci-dessous son annonce :

## Annonce

Nous sommes très heureux de pouvoir vous annoncer la sortie de la version de développement 1.2.0 de QGIS, portant le nom de "Daphnis".

Nos versions de développement sont fournies afin d'offrir une chance à nos utilisateurs d'essayer de nouvelles fonctionnalités au fur et à mesure de leur inclusion. Nous n'offrons pas un support de longue durée pour ces versions et de fait, elles sont plutôt destinées à ceux ne craignant pas les changements d'outils et d'interfaces d'une version à l'autre. Nous abandonnons le terme d'instable en faveur de celui de développement pour caractériser ces versions, car cela donnait la mauvaise impression que celles-ci étaient plus sujettes aux plantages. En réalité, les versions de développement contiennent de nombreuses résolutions de problèmes qui améliorent la stabilité par rapport aux versions précédentes.

Les fichiers d'installations et le code source sont disponibles à cette page :  
<http://qgis.org/en/download/current-software.html>

Une liste de changements avec des captures d'écrans est visible à cette adresse :  
<http://blog.qgis.org/node/137>

En parallèle à la version QGIS 1.2.0, l'équipe de la communauté QGIS travaille d'arrache-pied à la mise à jour du manuel utilisateur anglais tandis que la version française de la 1.0 devrait être disponible courant septembre.

QGIS est un projet mené de manière volontaire par une équipe dévouée de programmeurs, documentalistes, traducteurs, etc. Nous tenons à remercier tous ceux qui ont donné de leur temps pour faire aboutir cette version.

Si vous désirez faire une donation ou sponsorisez notre projet, veuillez visiter la page <https://www.qgis.org/en/sponsorship.html> . QGIS est un logiciel libre et donc rien ne vous y oblige.

Une rencontre des contributeurs est organisée à Vienne (Autriche) du 05 au 09 septembre 2009, si cela vous intéresse faite un tour à cette page pour plus de détails :[https://www.qgis.org/wiki/2._QGIS_Hackfest_in_Vienna_2009](https://www.qgis.org/wiki/2._QGIS_Hackfest_in_Vienna_2009)

================

Voici une courte liste des changements apportés dans la 1.2.0 :

### Édition

Les fonctionnalités d'édition de QGIS ont été améliorées dans cette  
version, elles incluent de nouveaux outils d'édition vectorielle :  
— supprimer une partie d'une entité multipartite  
— supprimer un trou d'un polygone  
— simplifier une entité  
— ajout d'un nouvel outil de noeud (dans la barre de numérisation avancée)  
— nouvelle fonctionnalité pour la fusion d'entités  
— ajout d'une option 'annuler/refaire' pour l'édition des couches  
vectorielles  
— ajout d'une option pour afficher uniquement les marqueurs des entités  
sélectionnées en mode édition  
— changement de l'icône de couche pour refléter la capacité d'édition

De plus, il y a des actions d'annulation/répétition dans le menu d'édition, dans la barre de numérisation avancée et un nouveau bouton affichant une pile d'annulations possibles pour la couche active.

À propos de l'outil de noeuds : il rassemble un outil pour éditer les chemins par noeuds qui sont présents dans tous les éditeurs vecteurs. Comment ça marche ? Cliquez sur une entité, ses noeuds seront marqués par de petits rectangles. Clqiuez sur un noeud pour le déplacer. Double-cliquer un segment rajoutera un nouveau noeud. La touche Supprimer effacera le noeud actif. Il est possible de sélectionner plus de noeuds actifs à la fois en cliquant et déplaçant un rectangle. On peut sélectionner les noeuds adjacents d'un segment en cliquant sur le segment. Il est possible d'ajouter et de supprimer des noeuds actifs en utilisant la touche Ctrl lorsque vous cliquez sur noeud ou étirez un rectangle.

Nous vous recommandons de désactiver les marqueurs de sommets dans les options de QGIS lorsque vous travaillez avec cet outil pour des raisons de performances graphiques.

### Raccourcis clavier

On peut maintenant configurer les raccourcis des actions directement depuis la fenêtre principale de QGIS, en allant dans Préférences->Configurer les raccourcis.

### Composition de cartes

Il est possible de verrouiller la position des éléments avec un clic droit. La hauteur et la largeur de la carte seront fixées si l'utilisateur spécifie une emprise pour le canevas de la carte. La date peut être affichée dans les étiquettes en saisissant (d 'Juin' yyyy) ou similaires. Les couches actuelles peuvent être conservées dans le compositeur de carte même si d'autres couches sont ajoutées. L'export PDF est disponible.

### Tables attributaires

Une recherche peut être faite uniquement sur les enregistrements sélectionnés. Les performances générales ont été améliorées. Définir la longueur et la précision d'un champ lors de l'ajout d'attributs est faisable. La prise en compte des attributs d'un service WFS est perfectionnée.

Les alias d'attributs des couches vecteurs sont disponibles, ils sont affichés à la place des noms de champs originaux dans l'outil d'identification et la table attributaire. Il y a une nouvelle interface pour paramétrer les fenêtres d'édition des attributs de couche. Un nouveau dialogue permet de charger une palette de valeur depuis une couche (depuis une table non spatialisée également !).

### Extensions

— l'ordre des couches dans la liste du dialogue WMS peut être modifié  
— l'extension eVis, version 1.1.0, a été intégrée au projet QGIS et inclus de manière standard. Plus d'information à [http://biodiversityinformatics.amnh.org/open_source/evis/documentation.php](http://biodiversityinformatics.amnh.org/open_source/evis/documentation.php)  
— l'extension d'interpolation peut utiliser les couches de lignes comme contraintes pour la triangulation. Vous pouvez aussi enregistrer la triangulation dans un fichier shapefile  
— un service et une extension OpenStreetMap ont été ajoutés

### Gestion de projet

QGIS inclut le support optionnel des chemins relatifs pour les sources de fichiers.

Service PostGIS & PostgreSQL :

Vous pouvez sélectionner le mode de connexion SLL quand vous ajoutez une nouvelle base de données. Désactiver le SSL améliore les performances de chargement de données QGIS quand des conditions de sécurité ne sont pas requises. Le support de types natifs et de paramètres a été étendu.

### Amélioration de la symbologie

— actualisation des symboles  
— ajout du support pour les noms symboles définis par les données  
— ajout du support pour les marqueurs de symbole de police (définit par  
les données — il n'y a pas encore d'interface)  
— la taille des symboles peut s'exprimer en unité de la carte (ie. les  
symboles ont une taille indépendante de l'échelle de la carte)

### Options de la ligne de commande

— support des options de ligne de commande sous Windows  
— permet de fixer une taille de capture d'écran  
— suppression possible de l'écran d'accueil  
— permet de capturer les décorations de fenêtre des extensions

### Grass

Il y a un nouveau terminal GRASS ainsi que beaucoup de nettoyage et d'amélioration de la consistance.

----

<!-- geotribu:authors-block -->
