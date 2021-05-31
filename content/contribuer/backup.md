---
title: "Sauvegarde des contenus et des images"
authors: ["Julien Moura"]
categories: ["article", "meta"]
date: 2021-06-01 10:20
description: "Comment fonctionne la sauvegarde automatique du site Geotribu."
image: "https://cdn.geotribu.fr/img/internal/workflow/geotribu_backup_result_github_release.png"
tags: geotribu,coulisses,sauvegarde,GitHub CLI,backup
---

# Sauvegarde du site Geotribu

![icône résilience](https://cdn.geotribu.fr/img/logos-icones/divers/resilience.png "icône résilience"){: .img-rdp-news-thumb }

Afin de ne pas reproduire le drame du crash de la base de données (voir [l'article sur la petite histoire de Geotribu](/articles/2020/2020-08-31_geotribu_histoire/)), le site recréé en 2020 est pensé pour maximiser la résilience :

- il s'agit d'un site statique : aucune base de données n'est à optimiser/maintenir/sécuriser, exceptée [celle des commentaires](/articles/2021/2021-05-14_commentaires_migration_disqus_isso/) mais qui n'est pas critique pour le fonctionnement global
- les contenus sont rédigés en [Markdown](/contribuer/guides/markdown_basics/), une syntaxe ouverte, lisible même dans sa forme "brute" et compatible avec énormément d'outils capables de la rendre en version "nette"
- les contenus sont donc des fichiers à plat stockés sur GitHub dont l'infrastructure est à l'évidence infiniment plus robuste que ce que l'on serait en mesure de proposer par nous-mêmes
- le principe de contribution étant fortement lié au système de versionnement décentralisé [Git], des copies des contenus existent sur différentes machines

Les seuls éléments non couverts directement par ces différents points sont donc les fichiers d'illustration : images, documents, etc.

## GitHub CLI et GitHub Release

![logo GitHub](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/github.png "logo GitHub"){: .img-rdp-news-thumb }

Pour couvrir cet aspect, nous avons mis en place un mécanisme de sauvegarde qui tire également parti de la plateforme GitHub : [Github Release](https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github) et [GitHub CLI](https://cli.github.com/).

Ainsi, tous les mois, le [script](https://github.com/geotribu/minimalist-cdn/blob/master/backup.sh) :

1. compresse l'ensemble des fichiers du pseudo-CDN
2. étiquette le dernier commit (*git tag*) avec un numéro de version calendaire de la forme `YYYY.MM`
3. crée une "release" sur GitHub en joignant l'archive compressée
4. notifie l'équipe sur [Slack](https://geotribu.slack.com/archives/CU9Q1B1FT)

![Sauvegarde - Notification Slack](https://cdn.geotribu.fr/img/internal/workflow/slack_geotribot_backup_notification.png "Sauvegarde - Notification Slack"){: .img-center loading=lazy }

[Télécharger la dernière sauvegarde :fontawesome-solid-download:](https://github.com/geotribu/website/releases/latest/){: .md-button }
{: align=middle }

Comme toujours, le code et fichiers de configuration sont librement accessibles :

[Fichiers de configuration et documentation :fontawesome-brands-github:](https://github.com/geotribu/minimalist-cdn/){: .md-button }
{: align=middle }

<!-- Hyperlinks reference -->
[Git]: https://git-scm.com/
