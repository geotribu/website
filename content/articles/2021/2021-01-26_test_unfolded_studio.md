---
title: Unfolded Studio, une nouvelle plateforme de visualisation de géodonnées
authors:
    - Aurélien CHAUMET
categories:
    - article
comments: true
date: 2021-01-26
description: Prise en main d'Unfolded Studio, une plateforme clé en mains de dataviz, via la représentation de données AirBNB de Bordeaux.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/unfolded_capture.png
tags:
    - analyse
    - application
    - datavisualisation
    - géodonnées
    - Unfolded
---

# Unfolded Studio, une nouvelle plateforme de visualisation de géodonnées

![logo unfolded studio](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/unfolded-logo-black.png "Logo Unfolded Studio"){: .img-thumbnail-left loading=lazy }

[Unfolded Studio](https://studio.unfolded.ai/) est un tout nouvel outil créé par l'équipe derrière [kepler.gl], [deck.gl] ou [H3].  
Ils se sont rencontrés lorsqu'ils travaillaient pour Uber et ont monté en 2019 la société [Unfolded.ai](https://www.unfolded.ai/).

Ils parlent de cette plateforme comme de la nouvelle génération d'outils d'analyse et de visualisation web de données géographiques.

Après l'avoir évoqué dans [la dernière GeoRDP](../../rdp/2021/rdp_2021-01-15.md#unfolded-studio), j'ai donc voulu tester un peu tout ça !

----

Si vous avez essayé Unfolded Studio, n'hésitez pas à laisser vos impressions dans les commentaires !

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Carte des logements Airbnb de Bordeaux

![capture unfolded studio](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/unfolded_capture.png "Capture Unfolded Studio"){: .img-center loading=lazy }

Cette carte représente (à gauche) la densité de logements Airbnb sur l'agglomération bordelaise, comparée (à droite) à une discrétisation par niveaux de prix (plus c'est foncé, plus le logement est cher).

### Un primo-affichage un poil lent

<iframe width="100%" height="500px" src="https://studio.unfolded.ai/public/705a57c1-b45d-4c68-9cd2-45064d5b2440/embed" frameborder="0" allowfullscreen></iframe>

[Cliquez ici pour voir la carte en plein écran](https://studio.unfolded.ai/public/705a57c1-b45d-4c68-9cd2-45064d5b2440){: .md-button }
{: align=middle }

Vous allez rapidement vous rendre compte que le premier défaut que je trouve à l'outil est le temps de chargement.  
Il y a une 60aine de Mo à charger, certes, mais ça gâche un peu l'expérience utilisateur, que l'entreprise vante comme simple et rapide...  
En revanche, une fois l'affichage terminé, l'interface réagit très bien, ce qui est un très bon point.

### Une documentation bien fournie

La documentation [se trouve ici](https://docs.unfolded.ai/) et est déjà bien achalandée pour un nouveau produit.

Pour ceux ayant utilisé [kepler.gl], vous remarquerez que pas mal de features se retrouvent dans Unfolded Studio, ce qui explique, sans doute, le niveau de maturité de l'application.

### Manipulation de l'application

Tout est très simple dans l'application pour construire une carte.

Ce qu'il faut savoir c'est que tout se base via le navigateur web.  
Vous accédez au studio ici <https://studio.unfolded.ai/>, et une fois connecté, il n'y a plus qu'à lancer une nouvelle carte.

On vous propose d'importer des fichiers ou d'en utiliser à partir d'une url.

![import donnee](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/import_donnees.png "Import données"){: loading=lazy }

Et l'application affiche dans un premier temps ce qu'il lui semble le plus "logique" comme manière de représenter chaque donnée chargée.

![premiere representation](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/premiere_representation.png "Première représentation"){: loading=lazy }

Libre à vous ensuite de changer le type de représentation, dont les possibilités sont assez fournies. Vous trouverez ci-dessous la liste complète, avec un accès à la documentation (en cliquant sur le nom de la représentation) et un exemple :

#### [Point](https://docs.unfolded.ai/studio/layer-reference/point)

![point](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/point.png "Point"){: .img-center loading=lazy }

#### [Arc](https://docs.unfolded.ai/studio/layer-reference/arc)

![arc](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/arc.png "Arc"){: .img-center loading=lazy }

#### [Ligne](https://docs.unfolded.ai/studio/layer-reference/line)

![ligne](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/ligne.png "Ligne"){: .img-center loading=lazy }

#### [Grille](https://docs.unfolded.ai/studio/layer-reference/grid)

![grille](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/grille.png "Grille"){: .img-center loading=lazy }

#### [Polygone](https://docs.unfolded.ai/studio/layer-reference/polygon)

![polygone](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/polygone.png "Polygone"){: .img-center loading=lazy }

#### [Cluster](https://docs.unfolded.ai/studio/layer-reference/cluster)

![cluster](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/cluster.png "Cluster"){: .img-center loading=lazy }

#### [Icône](https://docs.unfolded.ai/studio/layer-reference/icon)

![icone](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/icone.png "Icône"){: .img-center loading=lazy }

#### [Hexbin](https://docs.unfolded.ai/studio/layer-reference/hexbin)

![hexbin](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/hexbin.png "Hexbin"){: .img-center loading=lazy }

#### [Heatmap](https://docs.unfolded.ai/studio/layer-reference/heatmap)

![heatmap](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/heatmap.png "Heatmap"){: .img-center loading=lazy }

#### [H3](https://docs.unfolded.ai/studio/layer-reference/h3)

![h3](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/h3.png "H3"){: .img-center loading=lazy }

#### [Trip layer](https://docs.unfolded.ai/studio/layer-reference/trip)

![trip layer](https://d1a3f4spazzrp4.cloudfront.net/kepler.gl/documentation/k-trip.gif "Trip layer"){: .img-center loading=lazy }

Vous avez la possibilité de choisir quel(s) champs servira(ont) à la symbologie.  

Sur l'exemple illustrant cet article, j'ai choisi de représenter une heatmap pour observer la densité de logements Airbnb.  
On peut modifier la palette de couleurs, ainsi que le radius et ajouter un poids à sa création.

Pour la deuxième carte, j'ai voulu afficher les différences de prix, en jouant sur la couleur du ponctuel.

Tout ces paramètres sont très rapides à modifier et relativement instinctifs.

On remarquera qu'il n'est, pour l'instant, pas possible de jouer sur les transparences des différentes couches affichées...

### Coooluuuuumns

!!! warning
    Passons rapidement sur ce titre imitant très mal le bad side de Smeagol.

![manipulation donnees](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/columns.png "Manipulation de données"){: loading=lazy align=right clear=left width=100px }

L'onglet Columns permet de faire un peu de manipulation de données.

Il est possible de :

- Voir les différents champs des jeux de données chargés
- Ajouter un nouveau champ en utilisant des expressions
- Renommer un champ
- Réaliser des jointures, ainsi que des group by

Déjà pas mal !

### Fonctionnalités réjouissantes mais peu poussées

![filtres](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/filtres.png "Filtres"){: loading=lazy align=left clear=left width=90px }

D'autres fonctionnalités existent comme des filtres, des options sur les infobulles ou encore un geocoder.

Elles ont le mérite d'exister, mais ne sont pour l'instant que peu poussées.

Il est également possible de choisir quel fond de plan servira à votre carte.

Il faudra pour cela accepter de passer par MapBox, hé oui...

### Publication et export

C'est dans la publication de votre carte que les choses changent réellement par rapport à [kepler.gl].  
Unfolded va stocker la carte que vous venez de créer dans un dossier de leur côté, vous permettant alors d'y revenir ou bien de la partager.

Une fois publiée (ce qui peut prendre du temps), vous pourrez la partager directement via une url ou l'embarquer dans un site internet via un iframe.

![partager](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/partager.png "Partager"){: loading=lazy }

Enfin, [plusieurs options d'export](https://docs.unfolded.ai/studio/user-guide/publish-and-export) s'offrent à vous :

- Image
- Data
- Carte

### Business model

Unfolded propose un free tier avec les caractéristiques suivantes :

![pricing](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/unfolded/pricing.png "Pricing"){: loading=lazy }

Clairement, rien n'est gratuit dans ce bas monde, donc si vous souhaitez faire un peu plus que jouer avec Unfolded Studio, il est fort à parier que vous serez obligé de passer par la version payante (dont le prix n'est pour l'instant pas communiqué) ou que vous vous retournerez vers [kepler.gl] ou [deck.gl].

## Données

Les données utilisées pour cet article proviennent du site <http://insideairbnb.com> qui n'est pas affilié à Airbnb, mais qui a récupéré des tonnes de données directement sur le site.

## Conclusions

Quelques réflexions issues de cette première prise en main.

D'abord, ses avantages :

- Prise en main de l'application très rapide
- Une fois les données chargées, l'application répond très rapidement aux changements de paramètres
- La publication de la carte permet de la réutiliser facilement ailleurs

Quelques inconvénients ou améliorations à attendre :

- Une certaine lenteur dans le chargement de la carte publiée
- Les fonctionnalités de modification des jeux de données sont assez peu poussées
- Le free tier limite assez rapidement l'utilisation, que ce soit au niveau de la taille de fichier stockable (1GB au total), du nombre de cartes publiables ou encore sur la non capacité à se connecter à des bases de données

Personnellement, au vu des avantages et inconvénients précédemment listés, cela me donne l'impression d'un [kepler.gl] embarqué dans un [PaaS](https://fr.wikipedia.org/wiki/Platform_as_a_service).  
Si vous n'avez le temps ou les compétences pour utiliser et embarquer [kepler.gl] ou d'autres bibliothèques de ce type, cela peut être une bonne solution.

Reste à voir la manière dont cela évoluera dans le futur !

----

<!-- geotribu:authors-block -->

<!-- hyperlinks reference -->
[deck.gl]: https://deck.gl/
[kepler.gl]: https://kepler.gl/
[H3]: https://h3geo.org/
