---
title: "ign2map : automatisation et déploiement"
authors: ["Florian Boret, Julien Moura"]
categories: ["article"]
date: 2021-02-19 11:11
description: "Suite du projet ign2map : automatisation de l'exécution des scripts et du déploiement de la carte interactive des liens de téléchargement des données ouvertes de l'IGN, en tirant profit de GitHub Actions et Pages."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/github_action_workflow_result.png"
tags: bash,IGN,GitHub Pages,GitHub Actions
---

# ign2map : automatisation et déploiment

:calendar: Date de publication initiale : 19 Février 2021

**Mots-clés :** bash | IGN | déploiement | GitHub Actions | GitHub Pages

## Intro

![icône IGN](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/ign.png "IGN"){: .img-rdp-news-thumb }

L'IGN ayant annoncé que l'ouverture des données serait progressive, on anticipe que la page est donc appelée à s'agrandir (*sic*). Pour que le projet ne soit pas un symbôle d'obsolescence programmée (même s'il est certainement éphémère), on choisit donc d'automatiser le processus via [Github Actions] et la publication sur [Github Pages]. Une chaîne de valeurs que l'on connaît bien puisque déjà utilisée pour générer et publier le site actuel de Geotribu à partir des fichiers Markdown.

Après avoir présenté la génèse et détaillé la démarche de notre petit projet de carte des liens IGN, voici venir le second volet consacré à l'exécution complètement automatisée et paramétrable des scripts puis du déploiement tout aussi automatique.

[Accéder à la carte :earth_africa:](https://geotribu.github.io/ign-fr-opendata-download-ui/index.html){: .md-button } [Consulter l'article détaillant la démarche :fontawesome-solid-step-backward:](/articles/2021/2021-02-19_ignfr2map_automatisation_deploiement/){: .md-button }
{: align=middle }

## Travaux préliminaires

![icône agnostique](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/agnostique.jpg "agnostique"){: .img-rdp-news-thumb }

Avant de pouvoir automatiser sur une plateforme d'intégration et de déploiement continus (CI/CD pour les intimes), il s'agit de rendre l'exécution de nos scripts complètement indépendante de nos machines individuelles et paramétrables.

L'idée est donc de pouvoir passer plusieurs paramètres :

- l'URL source
- gérer les échelles : départements, régions et France entière
- la liste des produits de l'IGN ouverts pour en ajouter, enlever ou renommer selon l'évolution de la dynamique

----

## Le déploiement

![icône GitHub Actions](https://cdn.geotribu.fr/img/logos-icones/divers/github_actions.png "GitHub Actions"){: .img-rdp-news-thumb }

A l'instar de la plupart des autres, [GitHub Actions] consiste à décrire le processus (_workflow_ dans la terminologie GitHub) dans la syntaxe [YAML].

Le [fichier complet est dans le dépôt](https://github.com/geotribu/ign-fr-opendata-download-ui/blob/main/.github/workflows/run_n_publish.yml) mais prenons ici le temps de détailler les étapes.  

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

On commence par récupérer le contenu du dépôt Git (= `git fetch` ou `clone` pour les intimes) :

```yaml
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

#### Exécution

Sommairement[^1], cela donne donc :

```yaml
- name: Run it
  run: bash ./ignfr2map.sh
```

Vu qu'on utilise les paramètres par défaut, le résultat final est donc stocké dans le dossier `final`. Histoire de se faciliter le debug, on peut lister les fichiers temporaires et finaux :

```yaml
- name: List temp
  run: ls -R _temp/

- name: List final output
  run: ls -R final/
```

#### Déploiement

Enfin, il s'agit de pousser le dossier final sur la branche `gh-pages` publiée sur [Github Pages]. Pour cela, j'ai pris l'habitude d'utiliser l'outil [ghp-import], notamment inclus dans [MkDocs], l'outil qu'on utilise pour notre site. C'est par flemme car dans l'idéal il aurait fallu rester avec la seule ligne de commande et ainsi ne pas avoir besoin d'installer Python. On donne ainsi une chance à une contribution externe de briller :sparkler:.

Voici ce que ça donne :

```yaml
- name: Set up Python
  uses: actions/setup-python@v2.2.1
  with:
    python-version: 3.8

- name: Deploy to GitHub Pages
  run: |
    python -m pip install ghp-import
    ghp-import --force --no-jekyll --push final
```

----

## Conclusion

![Github workflow result](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/ign_opendata_map/github_action_workflow_result.png "Résultat de l'exécution déclenchée manuellement : 40 secondes"){: loading=lazy }
{: align=middle }

----

## Auteurs

--8<-- "content/team/fbor.md"

--8<-- "content/team/jmou.md"

<!-- Footnotes -->
[^1]: oui, j'ai osé ce jeu de mots avec le titre du paragraphe :wink:

<!-- Hyperlinks reference -->
[ghp-import]: https://pypi.org/project/ghp-import/
[GitHub Actions]: https://github.com/features/actions
[GitHub Pages]: https://guides.github.com/features/pages/
[YAML]: https://fr.wikipedia.org/wiki/YAML
