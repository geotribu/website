---
title: "ign2map : Du site à la carte"
authors: ["Florian Boret, Julien Moura"]
categories: ["article"]
date: 2021-02-19 11:11
description: ""
image: ""
tags: bash,ign,leaflet,github
---

# ign2map : automatisation et déploiment

:calendar: Date de publication initiale : 19 Février 2021

**Mots-clés :** bash | IGN | déploiement | GitHub Actions | GitHub Pages

[Accéder à la carte :earth_africa:](https://geotribu.github.io/ign-fr-opendata-download-ui/index.html){: .md-button }
{: align=middle }

## Le déploiement

![icône GitHub Actions](https://cdn.geotribu.fr/img/logos-icones/divers/github_actions.png "GitHub Actions"){: .img-rdp-news-thumb }

L'IGN ayant annoncé que l'ouverture serait progressive, on anticipe que la page est donc appelée à s'agrandir (sic). Pour que le projet ne soit pas un symbôle d'obsolescence programmée, on choisit donc d'automatiser le processus via [Github Actions] et la publication sur [Github Pages]. Une chaîne de valeurs que l'on connaît bien puisque déjà utilisée pour générer et publier le site actuel de Geotribu à partir des fichiers Markdown.

A l'instar de la plupart des plateformes d'intégration et de déploiement continus (_CI_ et _CD_ pour les intimes des acronymes anglophones), cela consiste à décrire le processus (_workflow_ dans la terminologie GitHub) dans la syntaxe [YAML].

Le [fichier complet est dans le dépôt](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/.github/workflows/run_n_publish.yml) mais prenons ici le temps de détailler les étapes.  

Mais avant de pouvoir automatiser, il était nécessaire de rendre le script paramétrable.

### Travail préalable : rendre le script paramétrable

L'idée est donc de pouvoir passer plusieurs paramètres :

- l'URL source
- gérer les échelles : départements, régions et France entière
- la liste des produits de l'IGN ouverts pour en ajouter, enlever ou renommer selon l'évolution de la dynamique

### Conditions d'exécution

Tout d'abord, on indique les critères de déclenchement du processus. On a choisi de concilier deux cas de figure :

- une exécution récurrente sur une base mensuelle, le permier jour de chaque mois
- une exécution manuelle pour nos tests ou quand l'envie nous prend

On souhaite également déclencher l'exécution uniquement lorsque des modifications sont appliquées sur la branche principale du projet.

Voici ce que cela donne :

```yaml
on:
  schedule:
    - cron: "0 0 1 * *"  # exécution planifiée le premier jour de chaque mois
  workflow_dispatch:     # permet de déclencher manuellement (ici sans passer aucun paramètre particulier)
  push:
    branches: [ main ]
    paths:
      - '.github/workflows/run_n_publish.yml'  # on déclenche aussi quand le fichier du workflow est lui-même modifié
```

### L'environnement d'exécution

Une fois les règles de déclenchementen place, passons aux tâches (*jobs*) qui doivent être exécutées. On commence par indiquer dans quel environnement on travaille.  
Vu que notre outil est écrit en bash, une surcouche du monde Linux au Shell, on opte pour Ubuntu :

```yaml
jobs:
  run:
    runs-on: ubuntu-latest
```

### Les étapes

Puis, on décrit pas à pas (*steps*) les différentes tâches.

#### Récupération du code

```yaml
# on récupère le contenu du dépôt Git (= git fetch ou clone pour les intimes)
    steps:
      - name: Checkout
        uses: actions/checkout@master
```

#### Paramétrage des options

On utilise les variables d'environnement définies dans le fichier example et on le renomme. Notez que c'est la solution de facilité et qu'il aurait été préférable d'utiliser des variables d'environnement :

- soit définies en haut du fichier via (voir [doc sur `env:`](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions#env)),
- soit via [la définition d'un environnement](https://docs.github.com/en/actions/reference/environments) ou [les Actions Secrets](https://docs.github.com/en/actions/reference/encrypted-secrets)

```yaml
      - name: Rename env file
        run: mv example.env .env
```

----

## La publication

On doit avouer :

- que le couvre-feu, nous a un peu aidé car il ne nous aura fallu que 15 jours pour arriver au résultat publié et quelques jours de plus pour mettre tout ça au propre.
- qu'on ne s'attendait pas à un tel retentissement

![Tweet IGN](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/ign_opendata_map_tweet_ign.png "Tweet IGN"){: loading=lazy .img-center }

----

## Auteurs

--8<-- "content/team/fbor.md"

--8<-- "content/team/jmou.md"

<!-- Hyperlinks reference -->
[GitHub Actions]: https://github.com/features/actions
[GitHub Pages]: https://guides.github.com/features/pages/
[YAML]: https://fr.wikipedia.org/wiki/YAML
