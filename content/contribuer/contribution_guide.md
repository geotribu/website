---
Title: Guide de contribution à Geotribu
Category: contribution
Date: 2020-03-20 10:20
Tags: guide,contribuer,geotribu
---

# Guide de contribution

!!! info

    Page en cours de rédaction. Veuillez patienter...

## Processus (_workflow_)

### 1. [Cloner le dépôt central](../local/requirements#git) localement

```bash
git clone https://github.com/geotribu/website.git
```

### 2. Créer ou utiliser une branche git locale

Pour afficher les différentes branches actives afin de sélectionner celle souhaitée, il suffit de lister les branches distantes pour savoir si une revue de presse a déjà été créée :

```bash
# liste les branches débutant par 'rdp'
git branch --list 'rdp*'

  rdp/2020-04-03

# liste toutes les branches centralisées
git branch -r

  origin/HEAD -> origin/master
  origin/ci-cd
  origin/gh-pages
  origin/master
  origin/material-5
  origin/pelican
  origin/rdp/2020-04-03
  origin/tutorials
  origin/tutos
  origin/vuepress
```

Basculer ensuite sur la branche qui va bien :

- soit en créant une branche locale `rdp/2020-04-03` :

    ```bash
    git checkout -b rdp/2020-04-03
    Switched to a new branch 'rdp/2020-04-03'
    ```

- soit en utilisant la branche `rdp/2020-04-03` déjà existante

    ```bash
    git checkout rdp/2020-04-03
    Switched to a new branch 'rdp/2020-04-03'
    ```

### 3. Créer/modifier localement du contenu en markdown

Le bon moment de se rappeler [comment écrire du bon markdown](../local/requirements#markdown) :wink: !

### 4. Enregistrer sa modification

Ajouter un message bref qui décrivant :

```bash
git commit -am "Ajout news sur la carte de la semaine"
```

### 5. Pousser son contenu avec Git vers le dépôt central

> ou vers un dépôt de son compte si on n'a pas les droits

- si c'est une nouvelle branche

    ```bash
    git push -u origin "rdp/2020-04-03"
    ```

- Ou, si c'est une branche déjà existante

    ```bash
    git push
    ```

### 6. Proposer la publication sur le site

Une fois le contenu prêt pour être publié, créer une [_Pull Request_](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) de sa branche vers la branche `master` du dépôt central

![Créer la pull request](https://cdn.geotribu.fr/images/internal/contribution/github_pull-request_form.png)

Et voilà ! Dès qu'elle sera validée, la correction sera automatiquement publiée :smile:


!!! warning

    Avant d'ajouter du contenu sur une branche déjà existante, bien penser à récupérer les changements faits par les autres contributeurs avant, en faisant :

    ```bash
    git pull
    ```  



----

## Modifier un contenu

### Texte

Coucher sa prose en markdown en s'appuyant sur :

- [voir un spécimen de ce qu'il est possible d'obtenir](https://squidfunk.github.io/mkdocs-material/specimen/)
- [utiliser des blocs stylés](https://squidfunk.github.io/mkdocs-material/extensions/admonition/)
- [insérer du code](https://squidfunk.github.io/mkdocs-material/extensions/codehilite/)
- [astuces de rédaction (en)](https://yakworks.github.io/mkdocs-material-components/cheat-sheet/)

### Ajouter une image

Voir [le guide dédié](../guides/image).

### Insérer un tweet

Voir [le guide dédié](../guides/twitter).

### Insérer une vidéo

Voir [le guide dédié](../guides/video).

### Utiliser un emoji

Voir [le guide dédié](../guides/emoji).

----

## Créer une revue de presse

Créer un fichier dans `content\rdp\AAAA` en respectant le nommage suivant : `rdp_AAAA-MM-JJ.md`. Exemple : `content\rdp\2020\rdp_2020-06-12.md` pour la revue de presse du 12 juin 2020.

## Ajouter une news

Un modèle de news est disponible ici :

- en brut : <https://raw.githubusercontent.com/geotribu/website/master/content/rdp/templates/template_rdp_news.md>
- rendu sur Github (non contractuel) : <https://github.com/geotribu/website/blob/master/content/rdp/templates/template_rdp_news.md>

<!-- Hyperlinks reference -->
[Git]: https://git-scm.com/download/win
[GitHub Desktop]: https://desktop.github.com/
[GitHub]: https://help.github.com/en/github/writing-on-github
[markdown]: https://fr.wikipedia.org/wiki/Markdown
[Python]: http://help.geotribu.com/development-guidelines/languages/python/
[StackEdit]: https://stackedit.io/
