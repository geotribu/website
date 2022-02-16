---
title: "Choisir une licence"
categories:
    - article
    - contribution
    - tutoriel
date: "2021-07-12 11:20"
description: "Comment choisir et appliquer une licence à son article Geotribu."
image: "https://cdn.geotribu.fr/img/internal/contribution/licensing/license_block.png"
license: default
tags:
    - contribuer
    - licence
    - Markdown
    - tutoriel
# theme customizations
search:
  exclude: true
---

# Choisir une licence pour son article

![icône poignée de main](https://cdn.geotribu.fr/img/internal/icons-rdp-news/lobby.png "icône poignée de main"){: .img-rdp-news-thumb }

En publiant un contenu sur un site public tel que Geotribu, il faut être conscient qu'il va potentiellement être copié, collé, modifié, entièrement ou partiellement, etc. La plupart du temps sans que l'auteur/e n'en soit notifié/e.  
Même si cela n'empêchera pas les usages abusifs, il est recommandé de spécifier la licence du contenu, notamment pour dissiper le flou qui peut entourer la réutilisation du contenu.

Geotribu applique une [licence par défaut](#licence-par-defaut) mais permet également à l'auteur/e de spécifier une licence spécifique sur ses articles.

## Licence par défaut

Une licence par défaut a été choisie par [l'équipe](/team/). Sauf mention contraire, elle est automatiquement ajoutée dans le bas de page :

![bandeau licence](https://cdn.geotribu.fr/img/internal/contribution/licensing/license_default.png "Bandeau licence bas de page")
{: align=middle }

----

## Choisir une autre licence

Chaque auteur/e peut également choisir d'indiquer une licence différente ou bien de mettre davantage en avant la licence par défaut en insérant un bloc plus complet directement dans le corps du contenu, généralement après le [le bloc auteur](/contribuer/guides/authoring/#bloc-auteur).

### Syntaxe

#### Désactiver la licence par défaut

Cette étape n'est utile que si vous souhaitez utiliser une licence différente de celle par défaut.  
Il suffit de modifier [l'en-tête de la page](/contribuer/guides/metadata_yaml_frontmatter/) ainsi :

```yaml
license: beerware
# ou
license: none
```

#### Insérer le bloc

La syntaxe est celle de la [fonction d'intégration de Jinja](https://jinja.palletsprojects.com/en/latest/templates/#include). Pour appliquer la licence par défaut, il suffit d'insérer cette ligne :

```markdown
{% raw %}
{% include "licenses/default.md" %}
{% endraw %}
```

### Rendu

{% include "licenses/default.md" %}

### Licences disponibles

| Nom et lien rendu | Commentaire | En-tête | Syntaxe |
| :---------------- | :---------- | :-----: | :-----: |
| [Creative Commons 4.0 BY-SA](/toc_nav_ignored/snippets/licenses/cc4_by-sa/) | Licence autorisant toutes les réutilisations, y compris pour une finalité commerciale. | `license: cc4_by-sa` | {% raw %}`{% include "licenses/cc4_by-sa.md" %}`{% endraw %} |
| [Creative Commons 4.0 BY-NC-SA](/toc_nav_ignored/snippets/licenses/cc4_by-nc-sa/) | **Licence par défaut**. Empêche la réutilisation pour une finalité commerciale. | `license: default` ou `license: cc4_by-nc-sa` | {% raw %}`{% include "licenses/cc4_by-nc-sa.md" %}`{% endraw %} |
| [Beerware](/toc_nav_ignored/snippets/licenses/beerware/) | Licence humoristique autorisant toute réutilisation sans conditions mais qui invite à payer un coup à l'auteur/e original/e. | `license: beerware` | {% raw %}`{% include "licenses/beerware.md" %}`{% endraw %} |

!!! question "Suggérer une licence"
    La licence souhaitée n'est pas disponible ? Proposez-la via GitHub en créant un fichier dans [ce dossier](https://github.com/geotribu/website/tree/master/content/toc_nav_ignored/snippets/licenses), ou [en ouvrant une issue](https://github.com/geotribu/website/issues/new?title=Ajout%20d%27une%20licence) et/ou contactez-nous !

----

### Exemples

Laisser la licence par défaut :

```markdown
{% raw %}
{% include "licenses/default.md" %}
{% endraw %}
```

Appliquer la licence CC 4.0 BY-SA :

```markdown
{% raw %}
{% include "licenses/cc4_by-sa.md" %}
{% endraw %}
```

----

## Remarques

### Prévalence du cadre légal

Selon la casquelle avec laquelle vous rédigez un contenu, indiquer une licence contraire au cadre légal en vigueur ne suffira pas. Par exemple, si vous rédigez un contenu en tant qu'agent de la fonction publique (sur votre temps de travail ou pour une mission en particulier), spécifier une licence empêchant une réutilisation commerciale n'aura aucun effet, la [Licence Ouverte 2.0] s'appliquant de fait.

### Sous le capot

D'un point de vue technique, la gestion des licences est liée aux capacités de personnalisation du thème [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/customization/), du [plugin Macros](https://mkdocs-macros-plugin.readthedocs.io/en/latest/) qui tire parti de la [fonction d'intégration de Jinja](https://jinja.palletsprojects.com/en/latest/templates/#include).

<!-- Hyperlinks reference -->
[Licence Ouverte 2.0]: https://www.etalab.gouv.fr/wp-content/uploads/2017/04/ETALAB-Licence-Ouverte-v2.0.pdf
