---
title: "Le crowdsourcing avec cocarto"
subtitle: Faire participer des non-sigistes depuis leur téléphone avec un simple lien
authors:
    - Tristram Gräbener
categories:
    - article
comments: true
date: 2024-03-18
description: Comment utiliser cocarto pour permettre à des non-sigistes de collecter des données sur le terrain avec uniquement un smartphone
icon: material/table-plus
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/banner.png
license: default
robots: index, follow
tags:
    - cocarto
    - collecte
    - collecte terrain
    - contribution
    - smartphone
---

# Le crowdsourcing avec cocarto

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

[cocarto](https://cocarto.com/) est un outil pour faciliter la saisie collaborative et en temps réel de données géoréférencées. C’est un [logiciel libre](https://gitlab.com/CodeursEnLiberte/cocarto/), mais il existe un support payant.

Ce guide s’adresse aux personnes qui souhaitent mettre en place un système permettant à des utilisateurs qui ne sont pas des experts de la géomatique de faire des signalements.

Par exemple :

- Signaler un danger pour les cyclistes
- Faire remonter un dépôt sauvage d’encombrants
- Partager des photographies d’observation d’un animal sauvage

Pour des besoins plus poussés, [QField](https://www.qfield.org/) est plus complet. Le [guide d’installation du serveur](2024-02-06_mise_en_place_serveur_qfieldcloud.md) vous mettra le pied à l’étrier.

Voici le scénario proposé :

- Un ou une admin crée le formulaire pour guider la saisie des informations souhaitées
- Les contributeurs et contributrices :
    - reçoivent un lien à ouvrir sur le téléphone,
    - n’ont pas à se créer de compte,
    - utilisent la géolocalisation de leur téléphone,
    - peuvent prendre des photos.
- L’admin exporte ces données vers un service professionnel de cartographie

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
 {: align=middle }

## Côté adminstrateur de données

![icône admin](https://cdn.geotribu.fr/img/logos-icones/divers/admin.png "icône admin"){: .img-thumbnail-left }

cocarto est un [logiciel libre](https://gitlab.com/CodeursEnLiberte/cocarto/) et vous pouvez l’installer sur votre infrastructure.

Cependant, pour ne pas complexifier l'article, dans ce guide, on vous propose d'utiliser l’instance publique [cocarto.com](https://cocarto.com) après y avoir créé un compte.

### Création de la carte et de la couche

Une fois connecté, créez une nouvelle carte, avec une couche de type _points_. Il est également possible de créer des couches de type lignes ou polygones ; mais il n’y aura pas de formulaire simplifié pour la saisie sur téléphone portable.

![Écran de création d’une nouvelle couche](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/nouvelle_couche.webp){: .img-center loading=lazy }

### Création des colonnes/données attributaires

Les colonnes, aussi appelées données attributaires — selon que vous veniez du monde des bases de données ou de la géomatique — sont les données qui vont être associées à chaque point qui va être saisi par le grand public.

Si vous définissez bien leurs types en amont, les personnes effectuant la saisie seront rassurées et vous simplifiera grandement la tâche pour traiter les données après.

Nous allons créer trois colonnes. Il n’y a pas besoin de définir de colonne pour les coordonnées du point : elles sont implicites et gérées par cocarto.

#### Nature du problème

Un choix parmi une liste finie d’options :

![Écran d’ajout d’une colonne menu local](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/menu_local.webp){: .img-center loading=lazy }

#### Photo du lieu

Donnée de type fichiers. Il sera possible de déposer plusieurs pièces jointes et de prendre des photos directement depuis le téléphone :

![Écran d’ajout d’une colonne fichier](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/fichier.webp){: .img-center loading=lazy }

#### Commentaire

Du texte libre, au format long :

![Écran d’ajout d’une colonne texte long](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/texte_long.webp){: .img-center loading=lazy }

### Création d’un lien de partage anonyme

En allant sur le menu de partage, en haut à droite de l’écran, nous allons créer un lien de partage de type contributeur.

![Écran de création de liens de partage](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/lien_partage.webp){: .img-center loading=lazy }

Le premier lien permet d’accèder à la carte et au tableau de données sur un ordinateur. Le deuxième lien est tout particulièrement adapté pour la saisie sur téléphone portable.
C’est ce lien que nous allons partager à toutes les personnes qui seront sur le terrain. Elles n’ont pas besoin de se créer de compte sur cocarto.

Le droit _contributeur_ veut dire qu’une personne peut uniquement ajouter des points, mais ne pourra pas modifier les données des autres utilisateurs.

Si vous souhaitez contrôler au plus près les droits d’accès, il est également possible d’inviter des personnes par email ; dans ce cas elles devront créer un compte.

## Saisie de données

Toute personne ayant le lien pourra l’ouvrir sur son téléphone mobile. L’utilisateur peut accepter de partager sa position GPS : la carte sera alors centrée sur sa position courante pour faciliter la saisie. La position GPS ne sera jamais remontée sur cocarto ; seulement le point du signalement validé par l’utilisateur.

En déplaçant la carte, il est possible d’indiquer avec précision où placer le point.

Il ne reste plus qu’à compléter les champs, prendre une ou plusieurs photos et ajouter le point.

![Écran de saisie depuis le téléphone](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/vue_mobile.webp){: .img-center loading=lazy }

## Export

![icône geojson](https://cdn.geotribu.fr/img/logos-icones/divers/geojson.png "icône GeoJSON - GeoJSON File by andrewcaliber from the Noun Project"){: .img-thumbnail-left }

L’admin verra apparaitre tous les points dès leur signalement et pourra les corriger, les compléter ou encore supprimer les doublons.

![Écran du tableau de données et du boutton exporter](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/tableau_exporter.webp){: .img-center loading=lazy }

Afin de collaborer avec des cartographes, il suffira de cliquer sur le bouton télécharger pour obtenir un GeoJSON qui sera très simple à exploiter, avec [QGIS](https://qgis.org/fr/) par exemple.

Il est également possible d’obtenir un lien permanent vers le dernier GeoJSON à jour, mais cela depasse le cadre de ce guide.

## Conclusion

Nous espérons avoir démontré comment cocarto permet de faire le lien très rapidement entre des personnes sur le terrain, sans aucune connaissance en géomatique et des équipes professionnelles, afin que cela soit le plus simple pour les deux :

- aucune application à installer pour faire des remontées : un lien suffit ;
- les données remontées sont correctement formatées et il n’y a pas besoin de les retravailler pour les utiliser dans un SIG.

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
