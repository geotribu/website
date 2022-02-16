---
title: "Créer une revue de presse"
authors:
    - Geotribu
    - Julien MOURA
categories:
    - contribution
date: "2021-12-29 10:20"
description: "Guide de création d'une revue de presse (GeoRDP) sur Geotribu : méthodologie, script bash, GitHub Workflow, etc."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/collaboration_world.png"
license: default
tags:
    - contribuer
    - GeoRDP
    - GitHub
    - GitHub Actions
    - GitHub Workflow
    - guide
    - workflow
---

# Création d'une revue de presse

![icône news générique](https://cdn.geotribu.fr/img/internal/icons-rdp-news/news.png "icône news générique"){: .img-rdp-news-thumb }

Concrètement, une revue de presse est un fichier markdown, nommé d'une certaine façon, stocké dans le dossier `content/rdp/` et organisé en sections dans lesquelles les contributeur/ices viennent ensuite insérer leurs "news". L processus de contribution est bâti autour de la logique de Git.

Avant d'ouvrir la revue de presse aux contributions, il est donc nécessaire de créer :

1. une branche dédiée dans le dépôt du site
2. le fichier Markdown avec la structure type
3. la Pull Request permettant de visualiser les différentes contributions puis de publier (fusionner) la revue de presse une fois finalisée

Il est possible de créer en utilisant Git en ligne de commande ou via l'interface web de GitHub.

!!! info "Zone réservée"
    La création d'une nouvelle revue de presse nécessite de disposer des droits d'écriture sur le dépôt GitHub : [{{ config.repo_name }}]({{ config.repo_url }}).

## Automatiquement via GitHub Workflow

![icône GitHub Actions](https://cdn.geotribu.fr/img/logos-icones/divers/github_actions.png "GitHub Actions"){: .img-rdp-news-thumb }

L'outillage et la logique de publication de Geotribu sont largement basés sur Git et la plateforme GitHub. Nous utilisons notamment les principes de l'intégration et du déploiement continus ([CI/CD pour les intimes](https://fr.wikipedia.org/wiki/CI/CD)).

La méthode la plus simple pour créer une nouvelle revue de presse est donc d'utiliser le *workflow* ":newspaper2: New GeoRDP" disponible sur GitHub :

1. Se rendre sur l'onglet `Actions` et sélectionner le *workflow* ":newspaper2: New GeoRDP" ou [cliquer ici]({{ config.repo_url }}actions/workflows/manual_new_rdp.yml)
2. Cliquer sur `Run workflow`
3. Entrer les infos demandées :
    - branche : `master`
    - date de la revue de presse : doit être au format `YYYY-MM-DD` et pointer sur un vendredi
    - choisir d'envoyer automatiquement une notification sur Slack
4. Cliquer sur le bouton vert `Run workflow`.

Après une trentaine de secondes, on obtient :

- une branche dédiée pour la revue de presse
- un fichier Markdown avec la structure type et la date de publication
- une Pull Request basée sur le modèle
- une notification Slack pour informer l'équipe

Voici une vidéo illustrant le déroulé :

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/7-G_gRJrUPA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

<!-- markdownlint-disable MD046 -->
!!! abstract "Prérequis"
    La bonne exécution du workflow dépend de ces éléments :

    - la revue de presse ou sa branche n'ont pas déjà été créées par ailleurs
    - le modèle de revue de presse est à jour et bien présent : `content/rdp/templates/template_rdp.md`
    - le modèle de Pull Request est bien présent : `.github/PULL_REQUEST_TEMPLATE.md`
    - l'URL du webhook de Slack (`SLACK_WEBHOOK_URL`) est bien configurée dans [les secrets du dépôt]({{ config.repo_url }}settings/secrets/actions) (cliquer [ici pour administrer le webhook Slack](https://api.slack.com/apps/A020C9Q93BK/incoming-webhooks/))
<!-- markdownlint-enable MD046 -->

### Utiliser localement le script intégré localement

Si vous disposez d'un terminal Bash et disposez du dépôt cloné, il est possible d'utiliser le script intégré :

```bash
# stocker la date de la RDP au format YYYY-MM-DD
DATE_RDP=2022-01-07

# exécuter le script
scripts/new_rdp.sh $DATE_RDP

# pousser vers le dépôt distant
git pull
git checkout -b rdp/$DATE_RDP
git add content/rdp/
git commit -am "Crée la GeoRDP $DATE_RDP"
git push origin rdp/$DATE_RDP
```

Ne pas oublier ensuite de :

1. se rendre sur [GitHub pour créer la Pull Request]({{ config.repo_url }}pulls)
2. sur [le canal dédié aux revues de presse sur Slack](https://geotribu.slack.com/archives/C010DD7FMEX) pour notifier l'équipe

## Manuellement via l'interface web de GitHub

Il est également possible d'utiliser l'ancienne procédure manuelle.  
Voici une vidéo retraçant les étapes de création d'une revue de presse via l'interface web de GitHub :

<iframe width="100%" height="400" src="https://www.youtube.com/embed/dVpOdGYAtIk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

----

## Processus détaillé

Cette partie explique chaque étape du processus de création d'une revue de presse pour comprendre ce que font les automatisations présentées au-dessus (script, GitHub Actions...).

### 1. Créer la branche de la revue de presse

![logo Git](https://cdn.geotribu.fr/img/logos-icones/divers/git.png "logo Git"){: .img-rdp-news-thumb }

La première étape consiste à créer une branche [Git] pour la revue de presse. Elle n'est réalisable que par une personne disposant d'un compte GitHub ayant les droits en écriture sur le dépôt du site : [{{ config.repo_name }}]({{ config.repo_url }}).

Il est important de respecter la convention de nommage `rdp/YYYY-MM-DD` où :

- `YYYY` est l'année de publication
- `MM` le mois de publication prévisionelle
- `DD` le jour de publication prévisionnelle

Exemple si la GeoRDP devait être publiée le 17 septembre 2021 : `rdp/2021-09-17`.

#### :fontawesome-brands-github:  GitHub

Sur l'interface web du dépôt :

1. Se positionner sur la branche `master`
2. Dans le menu déroulant de sélection des branches, entrer le nom de la nouvelle branche
3. Cliquant sur `Create branch: rdp/2021-09-17 from 'master'`.

![Github - New branch](https://cdn.geotribu.fr/img/internal/contribution/github_branch_rdp_new.png "GitHub - Création d'une branche"){: .img-center loading=lazy }

#### :fontawesome-solid-terminal: Ligne de commande

Si vous disposez du dépôt localement et que vous préférez utiliser la ligne de commande de [Git], voici les étapes à suivre :

1. Mettre à jour le dépôt local :

    ```bash
    git pull
    ```

2. Vérifier qu'une branche n'existe pas déjà en listant les branches du dépôt sur GitHub en filtrant sur la structure de nommage :

    ```bash
    git branch -r -l 'origin/rdp/*'
    ```

3. Créer la nouvelle branche :

    ```bash
    $ git checkout -b rdp/2021-09-17
    Switched to a new branch 'rdp/2021-09-17'
    ```

4. Pousser la branche sur GitHub :

    ```bash
    $ git push origin rdp/2021-09-17
    Total 0 (delta 0), réutilisés 0 (delta 0), réutilisés du pack 0
    remote:
    remote: Create a pull request for 'rdp/2021-09-17' on GitHub by visiting:
    remote:      https://github.com/geotribu/website/pull/new/rdp/2021-09-17
    remote:
    To github.com:geotribu/website.git
    * [new branch]        rdp/2021-09-17 -> rdp/2021-09-17
    ```

----

### 2. Créer le fichier de la revue de presse

![icône globe tricot](https://cdn.geotribu.fr/img/internal/icons-rdp-news/matiere.png "icône globe tricot"){: .img-rdp-news-thumb }

Afin d'accueillir les news, il s'agit de créer un fichier en respectant l'organisation et le nommage des fichiers : `content/rdp/YYYY/rdp_YYYY-MM-DD.md` où :

- `YYYY` est l'année de publication
- `MM` le mois de publication prévisionelle
- `DD` le jour de publication prévisionnelle

Exemple si la GeoRDP devait être publiée le 17 septembre 2021 : `content/rdp/2021/rdp_2021-09-17.md`.

#### Structure type et modèle

Les revues de presse sont structurées de la même façon d'une édition à l'autre, facilitant leur consultation et les traitements automatiques. Le plus simple est donc de copier/coller la structure type à partir du modèle maintenu à jour :

[soit depuis le PAD :fontawesome-solid-feather-pointed:](https://geotripad.herokuapp.com/DCBQirjYSp6sqxPd5JYqLg?both){: .md-button }
[soit depuis GitHub :fontawesome-brands-github-alt:](https://raw.githubusercontent.com/geotribu/website/master/content/rdp/templates/template_rdp.md){: .md-button }
{: align=middle }

Ensuite, il faut mettre à jour certains éléments :

- dans [l'en-tête du fichier](/contribuer/guides/metadata_yaml_frontmatter/), mettre à jour les valeurs de `title:`, `date:` et `description:` (notamment la date)
- changer la date dans le titre de niveau 1

Les lignes concernées sont surlignées ci-dessous (attention, cela peut varier selon le modèle utilisé) :

```markdown hl_lines="2 7 17"
---
title: "[TEMPLATE] Revue de presse du 21 août 2021"
authors:
    - Geotribu
categories:
    - revue de presse
date: 2021-08-21 14:20
description: ""
image: "URL de l'image d'illustration de la RDP"
license: default
tags:
    - tag 1
    - tag 2
    - ...
---

# Revue de presse du 21 août 2021

## Intro

![icône news générique](https://cdn.geotribu.fr/img/internal/icons-rdp-news/news.png "icône news générique"){: .img-rdp-news-thumb }

[Commenter cette revue de presse :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }
```

### 3. Pousser le fichier sur GitHub

Enfin, il faut pousser le fichier sur la branche créée sur GitHub.

#### :fontawesome-brands-github: GitHub Desktop

> TO DOC

#### :fontawesome-solid-terminal: Ligne de commande

```bash
git add content/rdp/2021/rdp_2021-09-17.md
```

<!-- Footnotes -->
[^pr]: étape où un contributeur propose d'intégrer ses modifications dans le socle principal du projet. Voir [la documentation de GitHub](https://docs.github.com/fr/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

<!-- Hyperlinks reference -->
[Git]: https://fr.wikipedia.org/wiki/Git
