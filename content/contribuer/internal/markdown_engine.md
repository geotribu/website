---
title: "Comprendre le rendu Markdown"
categories:
    - contribution
date: 2020-09-14 14:20
description: "Comprendre le fonctionnement de Python Markdown et ses spécificités pour contribuer en markdown à Geotribu."
image: "https://cdn.geotribu.fr/img/internal/contribution/markdown_exemple.png"
tags:
    - contribuer
    - HTML
    - Markdown
    - Python
    - rédaction
    - tutoriel
# theme customizations
search:
  exclude: true
---

# Le moteur de rendu Markdown utilisé et ses spécificités

## MkDocs et Python-Markdown

On utilise [MkDocs] pour générer le site web statique (HTML/JS/CSS), outil lui-même basé sur l'implémentation de [Markdown] en Python : [Python-Markdown].

## Utiliser

Pour comprendre le fonctionnement, rien de mieux que d'utiliser directement cette bibliothèque sous-jacente.

Après installation (`python -m pip install markdown`), le fonctionnement est très simple :

```python
# import du package
import markdown

# texte en markdown
texte_en_markdown = """# Super tutoriel sur la dernière techno fun en géomatique

Bienvenue dans mon **super** tutoriel, dans lequel on va apprendre :

1. à installer la techno fun du moment
2. à l'utiliser dans 2 cas d'usage :
    - analyser la répartition spatiale des poules en batterie
    - cartographier les flux de communications entre les membres de Geotribu

> Source : [*Geotribu*](https://static.geotribu.fr)

"""

# conversion en HTML
texte_en_html = markdown.markdown(texte_en_markdown, output_format="html5")

# écriture du fichier html
with open("super_tuto.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
    output_file.write(texte_en_html)
```

Le fichier HTML en sortie :

```html
<h1>Super tutoriel sur la dernière techno fun en géomatique</h1>
<p>Bienvenue dans mon <strong>super</strong> tutoriel, dans lequel on va apprendre :</p>
<ol>
<li>à installer la techno fun du moment</li>
<li>à l'utiliser dans 2 cas d'usage :<ul>
<li>analyser la répartition spatiale des poules en batterie</li>
<li>cartographier les flux de communications entre les membres de Geotribu</li>
</ul>
</li>
</ol>
<blockquote>
<p>Source : Geotribu</p>
</blockquote>
```

Si on ouvre le fichier `super_tuto.html` dans un navigateur :

![Markdown rapide exemple](https://cdn.geotribu.fr/img/internal/contribution/markdown_quick_exemple_rendu.png "Fichier HTML en sortie de la conversion du Markdown"){: .img-center loading=lazy }

!!! note
    La bibliothèque est évidemment utilisable en ligne de commande :  
    `python -m markdown input.md > output.html`

## Différences avec la syntaxe de référence

Si [Python-Markdown] est quasiment compatible avec l'implémentation [Markdown] de référence, mais il y a quand même quelques menues [différences] qu'il est intéressant de connaître pour les prendre en compte.

## Spécificités

- le retrait (tabulation) est de 4 espaces
- les sauts de lignes sont significatifs

## Extensions

Certaines extensions de la [syntaxe] sont intégrées au site ou peuvent l'être sur demande et après examen technique. Elles permettent d'ajouter des fonctionnalités et d'enrichir les possibilités rédactionnelles, dont certaines sont décrites dans des guides dédiés :

- ajouter des [attributs de style à des images](/contribuer/guides/image/#style-personnalise)
- ajouter [un effet "_lightbox_" (mise en avant et galerie) à des images](/contribuer/guides/image/#lightbox)
- intégrer [des diagrammes UML](/contribuer/guides/diagrams/)

Trouver des extensions :

- les [extensions](https://python-markdown.github.io/extensions/) de la bibliothèque [Python-Markdown]
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/).

!!! info
    Consulter la liste des extensions activées dans [le fichier de configuration](https://github.com/geotribu/website/blob/master/mkdocs.yml#L111).

<!-- Hyperlinks references -->
[MkDocs]: https://www.mkdocs.org/
[différences]: https://python-markdown.github.io/#differences
[extensions]: https://python-markdown.github.io/extensions/
[Markdown]: https://daringfireball.net/projects/markdown/
[Python-Markdown]: https://python-markdown.github.io/
[syntaxe]: https://daringfireball.net/projects/markdown/syntax
