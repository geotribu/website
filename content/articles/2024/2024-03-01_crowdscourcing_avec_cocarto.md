---
title: "Le crowdsourcing avec cocarto"
authors:
    - Tristram Gräbener
categories:
    - article
comments: true
date: 2024-03-01
description: "Comment utiliser cocarto pour permettre à des non-sigistes de collecter des données sur le terrain avec uniquement un smartphone"
icon: "material/table-plus"
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/banner.webp"

license: default
robots: index, follow
tags:
    - cocarto
    - contribution
    - collecte terrain
    - smartphone
---

# Le crowdsourcing avec cocarto

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

[cocarto](https://cocarto.com/) est un outil pour faciliter la saisie collaborative et en temps réel de données géoréférencées.

Ce guide s’adresse aux personnes souhaitant mettre en place un système pour remonter des signalement par des utilisateurs qui ne sont pas des experts de la géomatique.

Par exemple :

- Signaler un danger pour les cyclistes
- Faire remonter un dépôt sauvage d’encombrants
- Photographie d’observation d’un animal sauvage

Voici le scénario proposé :

- Un ou une admin créé le formulaire pour guider la saisie des informations souhaitées
- Les contributeurs et contributrices
    - reçoivent un lien à ouvrir sur le téléphone
    - n’ont pas à se créer de compte
    - utilisent la géolocalisation de leur téléphone
    - peuvent prendre des photos
- L’admin exporte ses données vers un service professionnel de cartographie

## Côté adminstrateur de données

cocarto est un [logiciel libre](https://gitlab.com/CodeursEnLiberte/cocarto/) et vous pouvez l’installer sur votre infrastructure.

Cependant, pour ne pas complexifier ce guide, créez un compte sur l’instance publique [cocarto.com](https://cocarto.com).

### Création de la carte et de la couche

Une fois connecté, créez une nouvelle carte, avec une couche de type _points_

![Écran de création d’une nouvelle couche](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/nouvelle_couche.webp)

### Création des colonnes/données attributaires

Les colonnes (si vous êtes du monde des bases de données) aussi appelées données attributaires (si vous venez du monde de la géomatique) sont les données qui vont être associées à chaque point qui va être saisi par le grand public.

Bien définir les types de données que vous voulez rassurera les personnes qui saisissent la donnée et vous simplifiera grandement la tâche pour traiter les données après.

Nous allons créer trois colonnes (les coordonnées du point sont implicites).

#### Nature de problème

Un choix parmis une liste finie de choix

![Écran d’ajout d’une colonne menu local](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/menu_local.webp)

#### Photo du lieu

Donnée de type fichier

![Écran d’ajout d’une colonne fichier](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/fichier.webp)

#### Commentaire

Du texte libre, au format long
![Écran d’ajout d’une colonne texte long](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/texte_long.webp)

### Création d’un lien de partage anonyme

En allant sur le menu de partage (en haut à droite de l’écran), nous allons créer un lien de partage de type contributeur.

![Écran de création de liens de partage](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/lien_partage.webp)

Le premier lien permet d’accèder à la carte et au tableau de données sur un ordinateur. Le deuxième lien est tout particulièrement adapté pour de la saisie sur téléphone portable.
C’est ce lien que nous allons partager à toutes les personnes qui seront sur le terrain. Elles n’ont pas besoin de se créer de compte sur cocarto.

Le droit _contributeur_ veut dire qu’une personne peut uniquement ajouter des points, mais ne pourra modifier les données des autres utilisateurs.

Si vous souhaitez controller au plus près les droits d’accès, il est également possible d’inviter des personnes par email ; dans ce cas elles seront invitées à crééer un compte.

## Saisie de données

Toutes les personnes avec le lien pourront l’ouvrir sur leur téléphone mobile. Si elles acceptent de partager leur position GPS (elle ne sera jamais remontée sur cocarto et ne sert que pour centrer la carte), la carte sera centrée sur sa position courante.

En déplaçant la carte, il est possible d’indiquer avec précision où placer le point.

Il ne reste plus qu’à compléter le champs, prendre une ou plusieurs photos et ajouter le point.

![Écran de saisie depuis le téléphone](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/vue_mobile.webp)

## Export

L’admin vera les points apparaitre tous les points en temps réel et pourra éventuellement corriger, compléter ou encore supprimer les doublons.

![Écran du tableau de données et du boutton exporter](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/cocarto/tableau_exporter.webp)

Afin de collaborer avec des cartographes, il suffira de cliquer sur le bouton télécharger pour obtenir un GeoJSON qui sera très simple à exploiter.

Il est également possible d’obtenir un lien permanent vers le dernier GeoJSON à jour, mais celà depasse le cadre de ce guide.

## Conclusion

Nous espérons avoir démontré comment cocarto permet de très rapidement faire le lien entre des personnes sur le terrain, sans aucune connaissance en géomatique et des équipe professionnelles pour ce soit au plus simple pour les deux :

- aucune application à installer pour faire des remontées: un lien suffit ;
- les données remontées sont correctement qualifiées et il n’y a pas besoin de les retravailler pour les utiliser dans un SIG.

## Auteur

--8<-- "content/team/tgram.md"

{% include "licenses/default.md" %}
