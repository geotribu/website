---
title: "Processus des revues de presse"
authors: ["Geotribu"]
categories: ["contribution"]
date: "2021-05-24 10:20"
description: "Cycle de vie d'une revue de presse sur Geotribu (GeoRDP) : création, contribution, validation, publication, diffusion."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/collaboration_world.png"
license: default
tags: guide,contribuer,geotribu,GeoRDP,workflow
---

# Processus de publication d'une revue de presse

![icône news générique](https://cdn.geotribu.fr/img/internal/icons-rdp-news/news.png "icône news générique"){: .img-rdp-news-thumb }

La rédaction des revues de presse (GeoRDP) est collaborative et ouverte à toute personne souhaitant partager une actualité ou contribuer à la veille commune. L'équipe est là pour coordonner les différentes contributions et s'assurer de la cohérence et de la qualité de la publication.

Gardez en tête que le travail de l'équipe est **bénévole**. A ce titre, plus votre contenu est conforme à nos prérequis et aux guides de contribution, moins il ne demande de travail de notre part. Ce que vous ne faites pas, nous devrons le faire.

Bref, appliquons le principe du *fair-use*[^fairuse] au bénévolat :hugging: !

[Proposer une news par email :fontawesome-solid-paper-plane:](mailto:geotribu+rdp@gmail.com?subject=Contribution à la GeoRDP){: .md-button }
[Proposer une news via GitHub :fontawesome-solid-ticket-alt:](https://github.com/geotribu/website/issues/new?assignees=aurelienchaumet%2C+Guts%2C+igeofr&labels=contribution+externe%2C+rdp&template=suggestion-de-news-pour-une-revue-de-presse.md&title=%5BNews+GeoRDP%5D){: .md-button }
{: align=middle }

## Processus global

1. Une branche est créée et une revue de presse vide est poussée par un membre de l'équipe (= ayant les droits d'écriture sur le dépôt du site : [{{ config.repo_name }}]({{ config.repo_url }}))
2. Une Pull Request est créée proposant de fusionner la branche de la RDP dans la branche principale
3. Les contributions sont ouvertes :
    - soit via des commits directement sur la branche de la revue de presse
    - soit via des Pull Requests pointant sur la branche de la RDP
4. La validation de la RDP se fait par une équipe de validation
5. Une fois validée et relue, la branche est fusionnée et la RDP publiée puis diffusée.

## Git workflow

> TO DOC

----

## Créer la branche de la revue de presse

![logo Git](https://cdn.geotribu.fr/img/logos-icones/divers/git.png "logo Git"){: .img-rdp-news-thumb }

La première étape consiste à créer une branche git pour la revue de presse. Elle n'est réalisable que par une personne disposant d'un compte GitHub ayant les droits en écriture sur le dépôt du site : [{{ config.repo_name }}]({{ config.repo_url }}).

Il est important de respecter la convention de nommage `rdp/YYYY-MM-DD` où :

- `YYYY` est l'année de publication
- `MM` le mois de publication prévisionelle
- `DD` le jour de publication prévisionnelle

Exemple si la GeoRDP devait être publiée aujourd'hui : `rdp/{{ now().strftime("%Y-%m-%d") }}`.

### :fontawesome-brands-github:  GitHub

Sur l'interface web du dépôt :

1. Se positionner sur la branche `master`
2. Dans le menu déroulant de sélection des branches, entrer le nom de la nouvelle branche
3. Cliquant sur `Create branch: rdp/2021-09-17 from 'master'`.

![Github - New branch](https://cdn.geotribu.fr/img/internal/contribution/github_branch_rdp_new.png "GitHub - Création d'une branche"){: .img-center loading=lazy }

### :fontawesome-solid-terminal: Ligne de commande

Si vous disposez du dépôt localement et que vous préférez utiliser la ligne de commande de git, voici les étapes à suivre :

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
    $ git checkout -b rdp/{{ now().strftime("%Y-%m-%d") }}
    Switched to a new branch 'rdp/{{ now().strftime("%Y-%m-%d") }}'
    ```

4. Pousser la branche sur GitHub :

    ```bash
    $ git push origin rdp/{{ now().strftime("%Y-%m-%d") }}
    Total 0 (delta 0), réutilisés 0 (delta 0), réutilisés du pack 0
    remote:
    remote: Create a pull request for 'rdp/{{ now().strftime("%Y-%m-%d") }}' on GitHub by visiting:
    remote:      https://github.com/geotribu/website/pull/new/rdp/{{ now().strftime("%Y-%m-%d") }}
    remote:
    To github.com:geotribu/website.git
    * [new branch]        rdp/{{ now().strftime("%Y-%m-%d") }} -> rdp/{{ now().strftime("%Y-%m-%d") }}
    ```

----

## Créer le fichier de la revue de presse

![icône globe tricot](https://cdn.geotribu.fr/img/internal/icons-rdp-news/matiere.png "icône globe tricot"){: .img-rdp-news-thumb }

Créer un fichier dans `content\rdp\AAAA` en respectant le nommage suivant : `rdp_AAAA-MM-JJ.md`. Exemple : `content\rdp\2020\rdp_2020-06-12.md` pour la revue de presse du 12 juin 2020.

> TO DOC

----

## Publication et diffusion

![icône porte-voix](https://cdn.geotribu.fr/img/internal/icons-rdp-news/journalisme.png "icône porte-voix"){: .img-rdp-news-thumb }

Une fois la Pull Request[^pr] validée par un membre de l'équipe, une date de publication est décidée en tenant compte du planning de publication.

Une fois la branche de l'article fusionnée (*merged*) dans la branche principale, votre contenu est publié et référencé automatiquement.  
En ce qui concerne la diffusion, cela reste à la discrétion de chacun/e, sachant que nous utiliserons le compte Twitter de Geotribu pour relayer la publication.

<!-- Footnotes -->
[^fairuse]: analogie avec un cadre légal qui repose sur un usage raisonnable des oeuvres et ressources. Voir [la fiche Wikipedia](https://fr.wikipedia.org/wiki/Fair_use).
[^pr]: étape où un contributeur propose d'intégrer ses modifications dans le socle principal du projet. Voir [la documentation de GitHub](https://docs.github.com/fr/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

<!-- Hyperlinks reference -->
[dépôt GitHub]: https://github.com/geotribu/website
[Git]: https://fr.wikipedia.org/wiki/Git
