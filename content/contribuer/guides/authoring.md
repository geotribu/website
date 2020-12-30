---
title: Signer ses contributions
category: contribution
date: 2020-08-04 14:20
description: "Contribuer à Geotribu : comment signer ses contributions au site."
tags: contribuer,tutoriel,signature,authoring,auteur,paternité
---

# Signer les contributions

## Signature automatique

Le site se repose sur l'extension [mkdocs-git-authors-plugin](https://github.com/timvink/mkdocs-git-authors-plugin) qui utilise l'historique Git pour déterminer qui a contribué à quelle page :

![Git authors plugin](https://cdn.geotribu.fr/img/internal/contribution/authoring/auto_from_git_log.png "Exemple de la liste des personnes ayant contribué à une page")

!!! warning

    Ce système a été mis en place à partir de la refonte du site en mars 2020. Tous les contenus antérieurs ayant été récupérés et poussés sur GitHub par moi-même (Julien), c'est mon compte qui est indiqué, mais ça n'est évidemment pas moi qui aie rédigé tous les contenus !

    Ainsi, pour tout contenu créé avant avril 2020, cette information ne reflète donc pas la contribution réelle à l'ensemble des contenus. Se référer au bloc auteur/e indiqué en bas du contenu.

### Pourcentage de contribution

Le pourcentage de contribution est proportionnel au nombre de lignes créées ou modifiées.

### Informations remontées et personnalisation

Les informations (nom, adresse email) correspondent à la configuration locale de Git utilisées lors du commit. C'est l'adresse email qui fait office d'identifiant unique.

Si vous en utilisez plusieurs ou si vous souhaitez personnaliser le nom d'affichage, il est possible d'établir une table de correspondance en modifiant le fichier [.mailmap](https://github.com/geotribu/website/blob/master/.mailmap).

----

## Bloc auteur

Les contributeurs/rices réguliers peuvent se créer une page contenant une brève présentation dans [`content/team/`](https://github.com/geotribu/website/new/master/content/team) en respectant le nommage des fichiers déjà créés.

### Syntaxe d'intégration

On utilise ensuite les capacités d'insertion héritée d'un fichier Markdown dans un autre : [Snippets](https://facelessuser.github.io/pymdown-extensions/extensions/snippets/).

Une fois la page créée, la syntaxe est la suivante : `--8<-- "content/team/filename.extension"`.

Exemple :

=== "Markdown"

    <pre><code>--8&lt;-- "content/team/jmou.md"</code></pre>

=== "Rendu"

    --8<-- "content/team/jmou.md"
