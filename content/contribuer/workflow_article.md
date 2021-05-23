---
title: "Proposer un article"
categories: ["contribution"]
date: 2021-05-25 10:20
description: "Comment proposer un article sur Geotribu : recommandations, outils et workflow."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/collaboration_world.png"
tags: guide,contribuer,geotribu,article,workflow
---

# Proposer un article

La rédaction d'articles est possible pour toute personne souhaitant partager une expérience, l'histoire de la conception d'une carte, une méthodologie, un outil, un tutoriel, un billet d'humeur ou autre tant qu'il ne s'agit pas d'une publicité ou d'un communiqué ou contenu assimilable.

Gardez en tête que le travail de l'équipe est **bénévole**. A ce titre, plus votre contenu est conforme à nos prérequis et aux guides de contribution, moins il ne demande de travail de notre part. Ce que vous ne faites pas, nous devrons le faire.

Bref, appliquons le principe du *fair-use* au bénévolat :hugging: !

## Rédiger

1. Créer un fichier Markdown (extension `.md` ou `markdown`)
2. Copier/coller le modèle d'article :
    - soit [depuis Github](https://github.com/geotribu/website/blob/master/content/articles/templates/template_article.md)
    - soit [depuis le PAD](https://geotripad.herokuapp.com/g70BvjD0TAuGHHb6jTzgPQ?edit)

[Utiliser le PAD :fontawesome-solid-feather-alt:](https://geotripad.herokuapp.com/){: .md-button }
{: align=middle }

Lire et s'appuyer sur les guides de rédaction :

- [bases du Markdown](/contribuer/guides/markdown_basics/) et spécificités de l'implémentation utilisée sur le site
- insérer des medias :
    - [images](/contribuer/guides/image/)
    - des [vidéos](/contribuer/guides/video/)
    - des [émojis](/contribuer/guides/emoji/)
    - des [diagrammes (schémas)](/contribuer/guides/diagrams/)
    - des [tweets](/contribuer/guides/twitter/)
- gérer les [métadonnées](/contribuer/guides/metadata_yaml_frontmatter/)
- [signer son article](/contribuer/guides/authoring/)

[Contacter l'équipe pour échanger :fontawesome-regular-paper-plane:](mailto:geotribu+article@gmail.com){: .md-button }
{: align=middle }

----

## Soumettre

Une fois le contenu prêt, il ne reste plus qu'à pousser le contenu sur [le dépôt GitHub]. La procédure est différente selon si vous des droits en écriture ou non sur [le dépôt GitHub]. Ces droits sont généralement réservés aux contributeur/ices régulier/ères et aux membres de l'équipe.

### J'ai accès en écriture

1. Créer une branche en respectant la convention de nommage suivante `article/XXXXXX` où `XXXXXX` est nom de l'article en minuscules et sans caractère spécial

    ![Github - New branch](https://cdn.geotribu.fr/img/internal/contribution/github_branch_new.png "GitHub - Création d'une branche"){: .img-center loading=lazy }

2. Créer un fichier selon la convention de nommage `content/articles/YYYY/YYYY-MM-DD_XXXXXX` où :
    - `YYYY` est l'année de publication
    - `MM` le mois de publication prévisionelle
    - `DD` le jour de publication prévisionnelle
    - `XXXXXX` le nom de l'article sans les caractères spéciaux ou les mots superflus (prépositions...)

    !!!tip
        Penser à s'inspirer des [articles déjà publiés](https://github.com/geotribu/website/tree/master/content/articles/2021) :wink: !  
        La date de publication pourra être amenée à changer selon les autres contenus planifiés.

3. [Créer la Pull Request](https://github.com/geotribu/website/compare)[^pr] en choisissant la branche de l'article comme source (`head`) et la branche principale (`master` ou `main`) comme destination (`ref`).

    ![Github - Pull Request new](https://cdn.geotribu.fr/img/internal/contribution/github_pull-request_button.png "GitHub - Créer une Pull Request"){: .img-right loading=lazy }

4. Adapter la description de la Pull Request en indiquant rapidement le sujet et la motivation de l'article
5. Demander la relecture sur Slack, dans [le canal `Articles`](https://geotribu.slack.com/archives/C0165UARRBQ)

### Je n'ai pas accès en écriture

> TO DOC

----

## Publication

Une fois la Pull Request[^pr] validée par un membre de l'équipe, une date de publication est décidée en tenant compte du planning de publication.

<!-- Footnotes -->
[^pr]: étape où un contributeur propose d'intégrer ses modifications dans le socle principal du projet. Voir [la documentation de GitHub](https://docs.github.com/fr/github/collaborating-with-issues-and-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

<!-- Hyperlinks reference -->
[le dépôt GitHub]: https://github.com/geotribu/website
