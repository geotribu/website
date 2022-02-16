---
# theme customizations
search:
  exclude: true
---

# Guide de contribution pour les tutoriaux

!!! warning
    Ce contenu est une archive. Son contenu n'est sûrement plus très frais...

Suite à la migration de serveurs, les tutoriaux ont pris un sacré coup. Cela a eu un impact certain sur la fréquention du site. L'objectif est de remettre ces tutoriaux sur pieds. La démarche ci-dessous explique procédure à suivre pour créer un tutoriel.

Note : Quand cela est possible, il est bien de créer ses tutoriaux sous la forme d'un livre. Cela permet d'avoir une certaine logique et de guider le lecteur. Drupal permet cela nous pourrons en discuter si vous le souhaitez. C'est par exemple la démarche adoptée pour les tutoriaux d'OpenLayers.

## Création du tutoriel

Donc pour ajouter un nouveau tutoriel, il faut se rendre à cette adresse : <http://geotribu.net/node/add> et choisir `tutoriel`.

Une nouvelle page s'ouvre alors. Celle-ci comprends différents champs qu'il sera nécessaire de remplir. Ces champs (introduction, body, etc.) parlent d'eux même je pense. Inutile donc de s'attarder dessus.

![capture formulaire tutoriel](https://cdn.geotribu.fr/img/internal/old_guide/createtuto1.png){: loading=lazy }

## Ecrire du code dans le tutoriel

Inclure du code est un peu galêre. Drupal (ou peut être ma configuration) se prête mal à cela. Mais avec un peu d'habitude on y arrive. Pour cela deux étapes sont nécessaires. La première est de cliquer sur l'icone en forme de scripts dans la barre d'outils.

![capture formulaire tutoriel](https://cdn.geotribu.fr/img/internal/old_guide/createtuto2.png){: loading=lazy }

Une nouvelle fenêtre s'ouvre alors. Choisissez votre langage de programmation, puis cliquez sur le bouton `Insert syntaxhighlighter tag`.

![capture formulaire tutoriel](https://cdn.geotribu.fr/img/internal/old_guide/createtuto3.png){: loading=lazy }

A partir de l'interface d'édition il y aura un encadré noir.

![capture formulaire tutoriel](https://cdn.geotribu.fr/img/internal/old_guide/createtuto4.png){: loading=lazy }

**N'ajoutez pas votre code de suite** !

Pour je ne sais qu'elle raison cela ne fonctionne pas correctement. Il faut maintenant passer en mode `Disable rich-text`. Pour cela cliquer sur le lien en bas de la fenêtre d'édition.

Vous pouvez maintenant remplacer le texte `Type your code in the box. To create a new line within the box use SHIFT + ENTER` par votre code :

```html
\&lt;pre class=`brush: css; auto-links: true; collapse: false; first-line: 1; html-script: false; smart-tabs: true; tab-size: 4; toolbar: true; codetag`\&gt; **Type your code in the box. To create a new line within the box use SHIFT + ENTER.** \&lt;/pre\&gt;
```

On repasse en mode `Enable rich-text` et le tour est joué.

Pour ceux qui utilisent GitHub, il est également possible d'inserer son code directement. Mais, là il n'est pas possible de découper son code.

## Paramétrage du tutoriel

Tout en bas de la page, il y a un ensemble de menus permettant de paramétrer le tutoriel (date de publication, auteur, etc.). Si ce tutoriel fait partie d'un livre, il sera nécessaire de le spécifier. Pour cela dans le menu `structure du livre`, il faudra choisir le livre ainsi que l'élément auquel il doit se rattacher.

![capture formulaire tutoriel](https://cdn.geotribu.fr/img/internal/old_guide/createtuto5.png){: loading=lazy }

Et voilà, rien de plus :smile:.

Le tutoriel est créé.

Fabien
