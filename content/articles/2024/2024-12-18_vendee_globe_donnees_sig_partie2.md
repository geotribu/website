---
title: Suivre le Vendée Globe 2024 depuis un SIG - Partie 2
subtitle: Hissez la grand voile carto - Partie 2
authors:
  - Florent FOUGÈRES
categories:
  - article
comments: true
date: 2024-12-18
description: Après avoir récupéré, nettoyé et visualisé les données SIG du Vendée Globe 2024 dans QGIS, voyons comment automatiser tout cela et développer une application application Web de suivi avec MapLibre.
icon: material/sail-boat
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/illustration_article_partie_2.png
license: beerware
robots: index, follow
tags:
  - CI/CD
  - GitHub Pages
  - GitHub Actions
  - MapLibre
  - QGIS
  - Vendée Globe
  - voile
  - webmapping
---
# Suivre le Vendée Globe 2024 depuis un SIG - Partie 2

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

## Résumé de la Partie 1

![logo Vendée Globe](https://cdn.geotribu.fr/img/logos-icones/divers/vendee_globe.png){: .img-thumbnail-left }

Dans le [premier article](https://geotribu.fr/articles/2024/2024-11-20_vendee_globe_donnees_sig/), que je vous invite à consulter si ce n'est pas déjà fait, avant de lire celui-ci, nous avions abordé les étapes techniques nécessaires à l'exploitation du tableur Excel officiel des pointages émis par l'organisation. Le but était de construire des données SIG à partir de ceux-ci qui sont publiés toutes les quatre heures. Pour cela je vous avais présenté une série de script Python qui permet le téléchargement automatisé des fichiers Excel, leur nettoyage, préparation des données, la conversion des coordonnées DMS en degrés décimaux, ainsi que la création des géométries pour tracer les points et les trajectoires des bateaux.

[:material-web: Accéder au premier article :simple-readdotcv:](https://geotribu.fr/articles/2024/2024-11-20_vendee_globe_donnees_sig/){: .md-button }
{: align=middle }

Dans cette seconde partie, nous allons voir les suites que j'ai apportées à ce projet.

Spoiler : CI/CD et cartographie web.

![Illustration cartographie et voile - Crédits : généré par IA, prompt et retouche par Florent Fougères](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/illustration_article_partie_2.png){: .img-center loading=lazy }

----

## Mise en musique de la construction des données SIG dans un pipeline de CI/CD

!!! question "C'est quoi la CI/CD ?"
    La [CI/CD](https://fr.wikipedia.org/wiki/CI/CD) (Intégration Continue et Déploiement Continu) est une méthodologie utilisée dans le développement logiciel pour automatiser le cycle de vie des applications. Elle permet de tester, intégrer et déployer du code de manière régulière grâce à des pipelines automatisés.

### Le pipeline

![icône GitHub Actions](https://cdn.geotribu.fr/img/logos-icones/divers/github_actions.png "GitHub Actions"){: .img-thumbnail-left }

Pour automatiser la génération des données SIG présentée dans le premier article, j'ai opté pour la mise en place d'un pipeline CI/CD.  
Les fichiers Excel officiels étant publiés sur une base régulière, le processus de téléchargement, nettoyage et conversion en formats SIG (GeoJSON et GeoPackage) est planifié.  
Grâce à ce système, j’ai pu garantir une actualisation continue et fiable des données géographiques sans intervention manuelle, tout en rendant les résultats immédiatement exploitables dans des outils cartographiques, ouvrant de nouvelles possibilités.

Dans mes activités professionnelles, j'utilise plus la CI/CD de GitLab que celle de GitHub, c'était donc pour moi un peu une découverte, mais j'ai réussi à m'en sortir en regardant des pipelines existants et en consultant la [documentation](https://docs.github.com/fr/actions).

Ce pipeline se trouve dans le fichier [.github/workflows/pointages.yml](https://github.com/florentfgrs/Vendee-Globe-2024/blob/main/.github/workflows/pointages.yml) du projet GitHub.

Sans rentrer dans une explication détaillée de ce code, globalement ce pipeline exécute trois "jobs", qu'on pourrait appeler trois étapes.

- `generate` : ce [job](https://github.com/florentfgrs/Vendee-Globe-2024/blob/main/.github/workflows/pointages.yml#L21) installe les dépendances Python puis exécute les scripts qui permettent de télécharger les tableurs Excel des pointages pour les convertir en données SIG. En somme, ce qui est décrit dans l'article précédent.
- `release`: ce [second job](https://github.com/florentfgrs/Vendee-Globe-2024/blob/main/.github/workflows/pointages.yml#L48) publie les données SIG dans une release GitHub, cette partie est détaillée plus tard dans l'article.
- `update-files`: ce [dernier job](https://github.com/florentfgrs/Vendee-Globe-2024/blob/main/.github/workflows/pointages.yml#L75) commit et push les données SIG dans le projet afin d'avoir une URL fixe pour les utiliser dans l'application web. Ce job est amené à disparaitre pour être intégré au [job de déploiement](https://github.com/florentfgrs/Vendee-Globe-2024/blob/main/.github/workflows/static.yml) de l'application web dans GitHub Pages.

En [haut du pipeline](https://github.com/florentfgrs/Vendee-Globe-2024/blob/main/.github/workflows/pointages.yml#L3-L5), on peut voir ce format de morceau de code.

```yaml
on:
  schedule:
    - cron: "30 3,7,11,15,19,23 * * *"
```

C'est dans cette partie qu'est planifiée l'automatisation, il s'agit d'un cron, pour plus d'informations sur cette syntaxe, je trouve cette [documentation](https://doc.ubuntu-fr.org/cron) bien faite. Ici le script s'exécute chaque jour à 3h30, 7h30, 11h30...

!!! warning "Attention sur l'heure"
    Les heures qu'on indique sont des heures GMT 0 ([heure de Greenwich](https://time.is/fr/GMT)) dans mon exemple il y a donc un décalage de +1h avec l'heure de Paris (GMT+1).

### Release automatique

!!! question "C'est quoi une release ?"
    Une _release_ est le terme pour désigner la publication d'une version d’un projet informatique. Sur les plateformes de forge logicielle comme GitLab et GitHub entre autres, elle sont liées généralement liées à une étiquette apposée sur un commit (`git tag`) et enrichies d'une description des changements (_release notes_) et de fichiers livrés : artefacts générés par la CI/CD, exécutables, binaires, données etc.

Chaque fois que le pipeline est exécuté, les dernières données écrasent les précédentes. Plus précisément, la dernière release est supprimée, et une nouvelle portant le même nom (`latest`) est créée. Il n'y a donc qu'une seule release des données disponible à cette [adresse](https://github.com/florentfgrs/Vendee-Globe-2024/releases/tag/latest). Tous les quatre heures, vous pouvez ainsi télécharger les dernières données d'avancement de la course.

![Release des données sur GitHub](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/release.png){: .img-center loading=lazy }

L'intérêt est donc de pouvoir récupérer les données sans avoir à cloner le projet, installer les dépendances et lancer les scripts pour construire les données, c'est la magie de la CI qui s'occupe de tout ça !

### Interroger directement la release depuis QGIS

Vous pouvez même charger ces données directement dans QGIS sans avoir à télécharger le fichier manuellement.

Pour cela dans votre QGIS rendez-vous dans le menu **Couche** puis **Ajouter une couche** et enfin **Ajouter une couche vecteur**

![QGIS - Ajouter une couche vecteur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/ajouter_une_couche.png){: .img-center loading=lazy }

Dans la fenêtre qui s'affiche, dans le champ `Jeux de données vectorielles` vous pouvez coller une URL de fichier qui provient de la release.

On va donc y mettre l'URL du fichier `latest_data.gpkg` qui contient la couche des pointages et celle des trajectoires.

```url
https://github.com/florentfgrs/Vendee-Globe-2024/releases/download/latest/latest_data.gpkg
```

![QGIS - URL de couche vecteur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/ajouter-couche-vecteur.png){: .img-center loading=lazy }

Après un temps de chargement (le temps que QGIS télécharge le fichier dans le cache) les données vont apparaître.

Ou plus simplement, télécharger et ouvrir le projet QGIS :

[:octicons-download-24: Projet QGIS Vendée Globe 2024 :simple-qgis:](https://github.com/florentfgrs/Vendee-Globe-2024/raw/refs/heads/main/Vend%C3%A9e%20Globe%202024.qgz){: download .md-button .md-button--primary }
{: align=middle }

----

## Visualiseur cartographique web

![icône MapLibre](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/maplibre.png){: .img-thumbnail-left }

Cette carte est basée sur les données générées par la CI, ce n'est donc pas du temps réel, mais un aperçu du dernier pointage. Les données sont donc automatiquement mises à jour toutes les 4h, là encore, c'est la magie de la CI qui permet ça.

!!! info inline end "Transparence sur le développement"
    Le développement web n'étant pas mon domaine de prédilection même si j'ai acquis les bases il y a quelques années lors de la formation au [master SIGAT](https://formations.univ-rennes2.fr/fr/formations/master-37/master-mention-geomatique-parcours-systeme-d-information-geographique-et-analyse-des-territoires-sigat-JEOC8L9A.html). Je me suis donc aidé de l'intelligence artificielle pour le développement de la partie JavaScript et CSS comme indiqué dans le [readme](https://github.com/florentfgrs/Vendee-Globe-2024?tab=readme-ov-file#%EF%B8%8F-visualisateur-web).

D'un point de vue technique, elle se base sur [Maplibre](https://maplibre.org/), il s'agit d'une bibliothèque JavaScript open-source de cartographie web permettant de créer des cartes interactives personnalisées à partir de données géospatiales.

Par défaut aucune trace n'est affichée, il faut alors cliquer sur les concurrents de votre choix dans la barre de gauche (ils sont classés dans l'ordre de leur position en course), ou bien cliquer sur le bouton `Tout afficher`.

Au survol d'une trace, un popup avec le temps apparait et des informations complémentaires en haut à gauche, tel que le cap et la vitesse.

![Application web de visualisation des données](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/vendee_globe_donnees_sig/webapp.png){: .img-center loading=lazy }

Cette application web est encore en phase de développement, j'aimerais encore l'améliorer. Par exemple, actuellement, dans la petite fenêtre qui s'affiche au survol, en haut à gauche, tous les attributs ne sont pas affichés. Comme énoncé plus haut, j'aimerais aussi ne plus lire les données en dur dans le dépôt GitHub, mais j'aimerais tout gérer dans le pipeline de déploiement de la GitHub Pages.

[:material-web: Accéder à la cartographie web du Vendée Globe 2024 :map:](https://florentfgrs.github.io/Vendee-Globe-2024/){: .md-button }
{: align=middle }

À suivre donc !

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
