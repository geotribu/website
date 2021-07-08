---
title: "Choisir une licence pour son article"
categories: ["article", "contribution", "tutoriel"]
date: "2021-07-12 11:20"
description: "Comment choisir et appliquer une licence à son article Geotribu."
image: "https://cdn.geotribu.fr/img/internal/contribution/markdown/markdown_yaml_frontmatter.png"
tags: "contribuer,tutoriel,markdown,licence"
---

# Choisir une licence pour son article

> TO DOC

## Licence par défaut

Par défaut, la licence est celle-ci :

{% include "licenses/default.md" %}

## Licences disponibles

| Nom et lien rendu | Commentaire | Syntaxe |
| :------ | :---------- | :-----: |
| [Creative Commons 4.0 BY-SA](/toc_nav_ignored/snippets/licenses/cc4_by-sa/) | Licence par défaut. | `{% include "licenses/cc4_by-sa.md" %}` |
| [Creative Commons 4.0 BY-NC-SA](/toc_nav_ignored/snippets/licenses/cc4_by-nc-sa/) | Attention la clause de non utilisation commerciale est contestée, car considérée comme une entorse au principe de *Free Culture*. | `{% include "licenses/cc4_by-nc-sa.md" %}` |

La licence souhaitée n'est pas disponible ? Contactez-nous !

## Exemples

Laisser la licence par défaut :

```markdown
`{% include "licenses/default.md" %}`
```

Appliquer la licence CC 4.0 BY-NC-SA :

```markdown
`{% include "licenses/cc4_by-nc-sa.md" %}`
```
