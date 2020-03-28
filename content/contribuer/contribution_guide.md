---
Title: Guide de contribution à Geotribu
Category: contribution
Date: 2020-03-20 10:20
Tags: guide
---

# Guide de contribution

!!! info

    Page en cours de rédaction. Veuillez patienter...

## Processus (_workflow_)

1. [Cloner le dépôt central](requirements#git) localement
```
>git clone https://github.com/geotribu/website.git
```
2. Créer ou utiliser une branche git locale

    a. Soit, créer une branche locale "rdp/2020-01-01"
    ```
    >git checkout -b rdp/2020-01-01
    Switched to a new branch 'rdp/2020-01-01'
    ```

    b. Ou, utiliser la branche "rdp/2020-01-01" déjà existante
    ```
    >git checkout rdp/2020-01-01
    Switched to a new branch 'rdp/2020-01-01'
    ```

3. Créer/modifier localement du contenu en markdown
4. Pousser son contenu avec Git vers le dépôt central ou vers un dépôt de son compte si on n'a pas les droits

    a. Si c'est une nouvelle branche
    ```
    >git push -u origin "rdp/2020-01-01"
    ```

    b. Ou, si c'est une branche déjà existante
    ```
    >git push
    ```

5. Une fois le contenu prêt pour être publié, créer une [_Pull Request_](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) de sa branche vers la branche `master` du dépôt central


!!! info

    Avant d'ajouter du contenu sur une branche déjà existante, bien penser à récupérer les changements faits par les autres contributeurs avant, en faisant :
    ```
    >git pull
    ```  

## Créer une revue de presse


Créer un fichier dans `content\rdp` en respectant le nommage suivant : `rdp_AAAA-MM-JJ.md`. Exemple : `rdp_2020-03-27.md` pour la revue de presse du 20 mars 2020.

## Modifier une revue de presse

### Texte

Coucher sa prose en markdown en s'appuyant sur :

- [voir un spécimen de ce qu'il est possible d'obtenir](https://squidfunk.github.io/mkdocs-material/specimen/)
- [utiliser des blocs stylés](https://squidfunk.github.io/mkdocs-material/extensions/admonition/)
- [insérer du code](https://squidfunk.github.io/mkdocs-material/extensions/codehilite/)
- [astuces de rédaction (en)](https://yakworks.github.io/mkdocs-material-components/cheat-sheet/)

### Ajouter une image

Dans la mesure du possible, les images doivent être récupérées depuis les autres sites / hébergées en externe :

```markdown
![Texte de remplacement](https://www.site-externe.com/medias/adresse_de_l_image.png "Titre/légende de mon image")
```

Si ça n'est vraiment pas possible :

1. Déposer l'image dans le sous-dossier adéquat sous `content/assets/images/`
2. La référencer dans un article suivant cette syntaxe :

<!-- Hyperlinks reference -->
[Git]: https://git-scm.com/download/win
[GitHub Desktop]: https://desktop.github.com/
[GitHub]: https://help.github.com/en/github/writing-on-github
[markdown]: https://fr.wikipedia.org/wiki/Markdown
[Python]: http://help.geotribu.com/development-guidelines/languages/python/
[StackEdit]: https://stackedit.io/
