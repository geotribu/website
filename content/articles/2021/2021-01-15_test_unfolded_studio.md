---
title: "Unfolded Studio, une nouvelle plateforme de visualisation de géodonnées"
authors: ["Aurélien Chaumet"]
categories: ["article"]
date: 2021-01-15 11:11
description: "Représentation de données Airbnb de Bordeaux via Unfolded Studio"
#image: ""
tags: unfolded, application, geodonnees, datavisualisation, analyse
---

Unfolded Studio est un tout nouvel outil créé par l'équipe derrière [kepler.gl](https://kepler.gl/), [deck.gl](https://deck.gl/) ou [H3](https://h3geo.org/).  
Ils se sont rencontrés lorsqu'ils travaillaient pour Uber et ont monté en 2019 la société [Unfolded.ai](https://www.unfolded.ai/).

Ils parlent de cette plateforme comme de la nouvelle génération d'outils d'analyse et de visualisation web de données géographiques.

J'ai donc voulu tester un peu tout ça !

# Carte des logements Airbnb de Bordeaux

## Un primo-affichage un poil lent

<iframe width="100%" height="500px" src="https://studio.unfolded.ai/public/705a57c1-b45d-4c68-9cd2-45064d5b2440/embed" frameborder="0" allowfullscreen></iframe>

Vous allez rapidement vous rendre compte que le premier défaut que je trouve à l'outil est le temps de chargement.  
Il y a une 60aine de Mo à charger, certes, mais ça gâche un peu l'expérience utilisateur, qu'ils vantent comme simple et rapide...  
En revanche, une fois l'affichage terminé, l'interface réagit très bien, ce qui est un très bon point.

Cette carte représente (à gauche) la densité de logements Airbnb sur l'agglomération bordelaise, comparée (à droite) à une discrétisation par niveaux de prix (plus c'est foncé, plus le logement est cher).

>Si vous souhaitez explorer plus librement cette carte, n'hésitez pas à [vous rendre ici pour l'afficher en plein écran.](https://studio.unfolded.ai/public/705a57c1-b45d-4c68-9cd2-45064d5b2440)

## Une documentation bien fournie

La documentation [se trouve ici](https://docs.unfolded.ai/) et est déjà bien achalandée pour un nouveau produit.

Pour ceux ayant utilisé kepler.gl, vous remarquerez que pas mal de features se croisent dans Unfolded Studio, ce qui explique sans doute, le niveau de maturité de l'application.

## Manipulation de l'application

Tout est très simple dans l'application pour construire une carte.

Ce qu'il faut savoir c'est que tout se base via le navigateur web.  
Vous accédez au studio ici <https://studio.unfolded.ai/>, et une fois connecté, il n'y a plus qu'à lancer une nouvelle carte.

On vous propose d'importer des fichiers ou d'en utiliser à partir d'une url.

Et l'application affiche dans un premier temps ce qu'il lui semble le plus "logique" comme manière de représenter chaque donnée chargée.

Libre à vous ensuite de changer de type de représentation, dont les possibilités sont assez fournies :

- Point
- Arc
- Ligne
- Grille
- Polygone
- Cluster
- Icône
- Hexbin
- Heatmap
- H3
- Trip layer

Et de choisir quel champs servira à la symbologie.  

Sur cet exemple, j'ai chosi de représenter une heatmap pour observer la densité de logements Airbnb.  
On peut modifier la palette de couleurs, ainsi que le radius et ajouter un poids à sa création.

Pour la deuxième carte, j'ai voulu afficher les différences de prix, en jouant sur la couleur du ponctuel.

Tout ces paramètres sont très rapides à modifier et relativement instinctifs.

On remarquera qu'il n'est pour l'instant pas possible de jouer sur les transparences des différentes couches affichées...

## Coooluuuuumns

Passons rapidement sur ce titre imitant très mal le bad side de Smeagol.

L'onglet Columns permet de faire un peu de manipulation de données.

Il est possible de :

- Voir les différents champs des jeux de données chargés
- Ajouter un nouveau champ en utilisant des expressions
- Renommer un champ
- Réaliser des jointures, ainsi que des group by

Déjà pas mal !

## Fonctionnalités réjouissantes mais peu poussées

D'autres fonctionnalités existent comme des filtres, des options sur les infobulles ou encore un geocoder.  
Elles ont le mérite d'exister, mais ne sont pour l'instant que peu poussées.

Il est également possible de choisir quelle fond de plan servira à votre carte.  
Il faudra pour cela accepter de passer par MapBox, hé oui...

Enfin, plusieurs options d'export s'offrent à vous :
- 

# Données

Les données proviennent du site <http://insideairbnb.com/get-the-data.html> qui n'est pas affilié à Airbnb, mais qui a récupéré des tonnes de données directement sur le site.

# Conclusions
