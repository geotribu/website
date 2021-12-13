---
title: "Créer une revue de presse"
authors:
    - Geotribu
categories:
    - contribution
date: "2021-09-30 10:20"
description: "Guide de création d'une revue de presse sur Geotribu."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/collaboration_world.png"
license: default
tags:
    - contribuer
    - guide
    - GeoRDP
    - workflow
---

# Création d'une revue de presse

![icône news générique](https://cdn.geotribu.fr/img/internal/icons-rdp-news/news.png "icône news générique"){: .img-rdp-news-thumb }

La création d'une revue de presse passe par la création d'une branche dédiée dans le dépôt du site et du fichier Markdown qui contiendra les news dans une structure type. Il est possible de créer en utilisant Git en ligne de commande ou via l'interface web de GitHub.

TL;DR : voici une vidéo retraçant les étapes de création d'une revue de presse via l'interface web de GitHub :

<iframe width="100%" height="400" src="https://www.youtube.com/embed/dVpOdGYAtIk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

----

## Créer la branche de la revue de presse

![logo Git](https://cdn.geotribu.fr/img/logos-icones/divers/git.png "logo Git"){: .img-rdp-news-thumb }

La première étape consiste à créer une branche [Git] pour la revue de presse. Elle n'est réalisable que par une personne disposant d'un compte GitHub ayant les droits en écriture sur le dépôt du site : [{{ config.repo_name }}]({{ config.repo_url }}).

Il est important de respecter la convention de nommage `rdp/YYYY-MM-DD` où :

- `YYYY` est l'année de publication
- `MM` le mois de publication prévisionelle
- `DD` le jour de publication prévisionnelle

Exemple si la GeoRDP devait être publiée le 17 septembre 2021 : `rdp/2021-09-17`.

### :fontawesome-brands-github:  GitHub

Sur l'interface web du dépôt :

1. Se positionner sur la branche `master`
2. Dans le menu déroulant de sélection des branches, entrer le nom de la nouvelle branche
3. Cliquant sur `Create branch: rdp/2021-09-17 from 'master'`.

![Github - New branch](https://cdn.geotribu.fr/img/internal/contribution/github_branch_rdp_new.png "GitHub - Création d'une branche"){: .img-center loading=lazy }

### :fontawesome-solid-terminal: Ligne de commande

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

## Créer le fichier de la revue de presse

![icône globe tricot](https://cdn.geotribu.fr/img/internal/icons-rdp-news/matiere.png "icône globe tricot"){: .img-rdp-news-thumb }

Afin d'accueillir les news, il s'agit de créer un fichier en respectant l'organisation et le nommage des fichiers : `content/rdp/YYYY/rdp_YYYY-MM-DD.md` où :

- `YYYY` est l'année de publication
- `MM` le mois de publication prévisionelle
- `DD` le jour de publication prévisionnelle

Exemple si la GeoRDP devait être publiée le 17 septembre 2021 : `content/rdp/2021/rdp_2021-09-17.md`.

### Structure type et modèle

Les revues de presse sont structurées de la même façon d'une édition à l'autre, facilitant leur consultation et les traitements automatiques. Le plus simple est donc de copier/coller la structure type à partir du modèle maintenu à jour :

[soit depuis le PAD :fontawesome-solid-feather-alt:](https://geotripad.herokuapp.com/DCBQirjYSp6sqxPd5JYqLg?both){: .md-button }
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

### Pousser le fichier sur GitHub

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
