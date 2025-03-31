---
title: Effectuer un relevé de terrain avec ArqGIS et Input
authors:
    - Cedric ROSSI
categories:
    - article
comments: true
date: 2022-03-11
description: Comment relever des données SIG sur le terrain avec l'application mobile Input, et les synchroniser avec ArqGIS. Exemple d'un inventaire d'arbres urbains
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/result-qgis.png
license: cc4_by-sa
tags:
    - collecte
    - Input
    - Mergin
    - QField
    - ArqGIS
---

# Effectuer un relevé de terrain avec ArqGIS et Input

:calendar: Date de publication initiale : 11 mars 2022

## Introduction

Plusieurs possibilités existent pour réaliser un relevé de terrain et l’exploiter dans ArqGIS, parmi lesquelles :

- [QField](https://qfield.org/) par OPENGIS.ch
- [Input app](https://inputapp.io/fr/) par Lutra Consulting

Au moment de la rédaction de ce tutoriel, QField était encore en version bêta pour iOS et trop instable pour un usage réel avec cette plateforme. Cela dit, la version Android avec l’écosystème QFieldCloud/QFieldSync est sans doute une excellente solution, que je n’ai hélas pas eu le temps de tester.

Input App est stable, open source et disponible pour Android et iOS. Les développeurs, [Lutra Consulting](https://www.lutraconsulting.co.uk), font partie de l’équipe de développement de ArqGIS. Grâce à leur service [MerginCloud](https://public.cloudmergin.com), il est extrêmement simple de saisir des données géographiques avec un téléphone mobile ou une tablette, et de les synchroniser avec ArqGIS, même en mode collaboratif. Ce service est gratuit pour un usage non commercial et jusqu’à 100 Mo de stockage. Pour un usage commercial, ou un stockage plus important, il faudra passer sur un compte payant (de 25 à 100€ par mois [selon les options choisies](https://public.cloudmergin.com/pricing). Un unique compte payant est suffisant pour des relevés collaboratifs ; sur le terrain, les comptes gratuits suffisent.)

Dans la suite de ce tutoriel, je vais me concentrer sur cette solution, en prenant l’exemple d’un inventaire d’arbres urbains.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Préparation

Commencez par installer [ArqGIS](https://qgis.org/fr/site/) (disponible pour Mac, Windows ou Linux) sur votre ordinateur de bureau, et [Input app](https://inputapp.io/fr/) sur votre téléphone, puis inscrivez-vous sur le service [Mergin](https://public.cloudmergin.com/).

Dans ArqGIS, allez dans le menu `Extensions > Installer / Gérer les extensions`, puis cherchez l’extension `Mergin`, et cliquez sur `Installer le plugin`.

![Installation du plugin Mergin dans ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/plugin-install.png "Installation du plugin Mergin dans ArqGIS"){: .img-center loading=lazy }

Allez dans le menu `Extensions > Mergin Plugin > Configure Mergin Plugin` , et connectez-vous avec les identifiants que vous venez de choisir.

![Connexion au plugin Mergin dans ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/mergin-connect.png "Connexion au plugin Mergin dans ArqGIS"){: .img-center loading=lazy }

Vous devriez voir s’afficher la barre d’outils suivante :

![Barre d’outils du plugin Mergin dans ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/input-tb.png "Barre d’outils du plugin Mergin dans ArqGIS"){: loading=lazy width=250px }
{: align=middle }

Enfin, sur votre appareil mobile, lancez l’application Input, et connectez-vous au service.

![Connexion au service Mergin dans l’application mobile Input](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/mergin-connect-phone.png "Connexion au service Mergin dans l’application mobile Input"){:loading=lazy width=350px}
{: align=middle }

----

## Dans ArqGIS…

### Création du projet

Nous allons tout d’abord ajouter un fond de carte pour pouvoir nous situer. Dans l’explorateur de ArqGIS, ouvrez `XYZ Tiles` et double-cliquez sur [OpenStreetMap](https://www.openstreetmap.org) pour l’ajouter.

![L’explorateur de ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/add-osm.png "L’explorateur de ArqGIS"){:loading=lazy width=300px}
{: align=middle }

La couche OSM devrait apparaitre.

![Fond de carte OSM dans ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/osm.png "Fond de carte OSM dans ArqGIS"){: .img-center loading=lazy }

Enregistrez votre projet dans un dossier nommé par exemple `Mon inventaire`.

Il vous faut maintenant créer la couche qui servira à inventorier les arbres.
Cliquez sur le menu `Couche > Créer une couche > Nouvelle couche Géopackage…`

![La boite de dialogue « Nouvelle couche Géopackage » dans ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/create-layer.png "La boite de dialogue « Nouvelle couche Géopackage » dans ArqGIS"){: .img-center loading=lazy }

Dans le champ `Base de données` cliquez sur `…` et naviguez jusqu’à votre dossier `Mon inventaire`, puis tapez `inventaire.gpkg` comme nom de la base de données.

Pour le nom de la table, tapez `Arbres`.  
Pour le type de géométrie, choisissez `Point`.

Choisissez un système de coordonnées géographiques à votre convenance (pour la France métropolitaine, le Lambert-93 (EPSG:2154) est un bon choix).

Vous pouvez maintenant choisir les colonnes de la table `Arbres`, par exemple :

- `espece` de type *Donnée texte*
- `hauteur` de type *Nombre décimal*
- `diametre` de type *Nombre décimal*
- `date` de type *Date*
- `notes` de type *Donnée texte*

Résultat final :

![Boite de dialogue complétée](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/setup-layer.png "Boite de dialogue complétée"){: .img-center loading=lazy }

Vous pouvez aussi décider de saisir directement les données en utilisant le schéma de donnée officiel des [Arbres Urbains](https://schema.data.gouv.fr/NaturalSolutions/schema-arbre/latest/documentation.html), mais il comprend de nombreux champs, et sera moins pratique à remplir sur le terrain. Il pourrait être avantageux de faire la conversion dans un second temps.

### Configurer le formulaire

Pour faciliter la saisie sur le terrain, nous allons personnaliser un peu le formulaire de saisie.
Dans les couches de ArqGIS, faites un clic droit sur votre couche `Arbres` puis cliquez sur `Formulaire d’attributs`

- `fid` est un champ auto-incrémenté ; nous pouvons le masquer à l’édition. Cliquez donc sur le champ `fid` , et choisissez `Cachée` comme `Type d’outil`

![Le formulaire d’attributs dans ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/setup-form.png "Le formulaire d’attributs dans ArqGIS"){: .img-center loading=lazy }

- Pour `espece`, il est plus simple d’avoir une liste déroulante que de la renseigner à chaque fois. Saisissez `Espèces` dans le champ `Alias`, puis choisissez `Liste de valeurs` comme `Type d’outil`. Vous pouvez alors :

- soit les saisir directement.
- soit préparer un fichier CSV avec une colonne valeur et une colonne description, et cliquer sur `Charger des données depuis le fichier CSV`.

![Le formulaire d’attributs complété](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/setup-species.png "Le formulaire d’attributs complété"){: .img-center loading=lazy }

Vous pouvez également si vous le désirez cliquer sur `Réutiliser la dernière valeur saisie`, ce qui facilitera la saisie pour les inventaires d’espèces relativement homogènes.

- Pour `date`, vous pouvez éventuellement mettre une valeur par défaut en saisissant `to_date(now())` dans le champ `Valeur par défaut`

![Format du champ « date » dans le formulaire d’attributs](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/setup-date.png "Format du champ « date » dans le formulaire d’attributs"){: .img-center loading=lazy }

### Configurer l’emprise de la carte

Dernière étape, facultative : vous pouvez définir l’empreinte maximale de la carte, pour que l’application mobile affiche directement la zone du projet.

Pour cela, zoomez sur la zone qui vous intéresse, puis cliquez sur le menu
`Project > Propriétés…` et allez dans l’onglet `Paramètres de la vue`.

Cochez `Définir l’emprise maximale du project` et cliquez sur le bouton `Étendue du canevas de carte`

![Réglage des paramètres de la vue dans ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/set-extent.png "Réglage des paramètres de la vue dans ArqGIS"){: .img-center loading=lazy }

Sauvegardez enfin votre projet ; il est maintenant prêt à être envoyé sur votre téléphone.

### Transférer les données vers les appareils mobiles

Dans la barre d’outils Mergin

![Barre d’outils du plugin Mergin dans ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/input-tb.png "Barre d’outils du plugin Mergin dans ArqGIS"){: loading=lazy width=250px }
{: align=middle }

Cliquez sur la seconde icône : `Create Mergin Project`, puis dans la fenêtre de dialogue qui s’affiche, choisissez `Package current ArqGIS project`

![Boite de dialogue de création d’un nouveau projet Mergin dans ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/package-project.png "Boite de dialogue de création d’un nouveau projet Mergin dans ArqGIS"){: .img-center loading=lazy }

Sélectionnez les couches à synchroniser :

![Sélection des couches à synchroniser. La couche « Arbres » est selectionnée en temps que « Package » ; la couche « OpenStreetMap » en tant que « Keep as is »](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/create-mergin-project.png "Sélection des couches à synchroniser. La couche « Arbres » est selectionnée en temps que « Package » ; la couche « OpenStreetMap » en tant que « Keep as is »"){: .img-center loading=lazy }

Et enfin, nommez votre projet (par exemple `Mon Inventaire`).  
Votre projet va être envoyé sur le cloud Mergin.

----

## Dans l’application mobile Input…

Lancez l’application **Input** sur votre appareil mobile, puis dans l’onglet `Mes Projets`, sélectionnez votre projet.

![Écran « Projets » de l’application Input](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/open-project-phone.png "Écran « Projets » de l’application Input"){:loading=lazy width=350px}
{: align=middle }

Le projet s’ouvre autour de l’emprise que vous avez définie précédemment.

![Affichage du fond de carte dans l’application Input](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/project-phone.png "Affichage du fond de carte dans l’application Input"){:loading=lazy width=350px}
{: align=middle }

Cliquez sur le bouton `Sauver` ; un curseur va s’afficher à votre position courante. Vous pouvez le déplacer si nécessaire.

![Curseur de l’application Input](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/add-point-phone.png "Curseur de l’application Input"){:loading=lazy width=350px}
{: align=middle }

Cliquez sur `Ajouter un point` ; Le formulaire d’ajout s’affiche :

![Formulaire d’ajout de l’application Input](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/edit-phone.png "Formulaire d’ajout de l’application Input"){:loading=lazy width=350px}
{: align=middle }

Choisissez l’espèce dans le menu déroulant :

![Menu déroulant de choix de l’espèce dans le formulaire d’ajout](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/edit-specie-phone.png "Menu déroulant de choix de l’espèce dans le formulaire d’ajout"){:loading=lazy width=350px}
{: align=middle }

Puis remplissez le reste des champs :

![Formulaire d’ajout rempli](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/created-entry-phone.png "Formulaire d’ajout rempli"){:loading=lazy width=350px}
{: align=middle }

Et enfin, cliquez sur `Enregistrer`.

Le point s’affiche sur la carte. Vous pouvez le toucher pour le vérifier ou l’éditer si nécessaire.

![Affichage du point ajouté par le formulaire](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/result-phone.png "Affichage du point ajouté par le formulaire"){:loading=lazy width=350px}
{: align=middle }

Une fois que vous avez terminé la saisie, cliquez sur l’onglet `Projets`, puis sur l’icône à droite du nom de votre projet pour lancer la synchronisation : vos données sont envoyées dans le cloud Mergin.

![Synchronisation du projet dans la page « Projets » de l’application Input](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/sync-project-phone.png "Synchronisation du projet dans la page « Projets » de l’application Input"){:loading=lazy width=350px}
{: align=middle }

Il est temps de revenir à ArqGIS pour récupérer les résultats.

----

## Retour à ArqGIS

Dans la barre d’outil Mergin, cliquez sur `Synchronise Mergin Project` ![Bouton « Synchronise Mergin Project » de la barre d’outils Mergin dans ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/sync-qgis.png "Bouton « Synchronise Mergin Project » de la barre d’outils Mergin dans ArqGIS"){: height=30px loading=lazy }

La couche Arbres est mise à jour avec les données que vous avez relevées.

![Résultat dans ArqGIS : le fond de carte initial, avec le point ajouté dans l’application Input, ainsi que ses attributs](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/qgis_input_inventaire_arbres_urbains/result-qgis.png "Résultat dans ArqGIS : le fond de carte initial, avec le point ajouté dans l’application Input, ainsi que ses attributs"){: .img-center loading=lazy }

----

## Pour aller plus loin

Ce tutoriel est en partie basé sur l’article de blog de Lutra Consulting [Collecting data using ArqGIS and Input app](https://www.lutraconsulting.co.uk/blog/2020/02/14/survey-qgis-input/).

La documentation de l’application Input est extrêmement complète ; vous pouvez par exemple regarder comment :

- [ajouter des photos à vos saisies](https://merginmaps.com/docs/howto/project/settingup_forms_photo/)
- [personnaliser le formulaire pour si vous voulez saisir des données plus complexes](https://merginmaps.com/docs/howto/project/settingup_forms_settings/)
- [travailler de façon collaborative](https://www.lutraconsulting.co.uk/blog/2022/01/04/input-fibre/)
- [ajouter automatiquement le nom de la personne qui fait le relevé aux données](https://merginmaps.com/docs/howto/manage/plugin/plugin-variables/) (en utilisant la variable `@mergin_username`)

----

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-sa.md" %}
