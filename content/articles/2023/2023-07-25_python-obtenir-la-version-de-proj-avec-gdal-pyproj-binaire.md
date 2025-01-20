---
title: Obtenir la version de PROJ installée en Python
subtitle: EPSG:9.2.1
icon: material/spotlight
authors:
    - Julien MOURA
categories:
    - article
comments: true
date: 2023-07-25
description: 'Mémo technique : comment récupérer la version de PROJ installée depuis un script Python, avec GDAL, PyProj ou le binaire proj.'
image:
license: beerware
robots: index, follow
tags:
    - expression régulière
    - PROJ
    - Python
---

# Python : obtenir la version de PROJ installée

:calendar: Date de publication initiale : 25 juillet 2023

![icône projection](https://cdn.geotribu.fr/img/logos-icones/divers/projection.png){: .img-thumbnail-left }

En butant sur un souci de reconnaissance de SRS lié aux [choix éclairés de l'IGN en matière de registre spécifique](https://twitter.com/EvenRouault/status/1437818895604269059), j'ai eu besoin de vérifier la version de PROJ installée de façon à pouvoir adapter le comportement du script.  
Formulé comme ça, mon candide moi s'est dit :

> allez zou, un coup de `proj --version` ou `-V` dans un subprocess et on n'en parle plus !

C'est alors que mon surmoi de galérien a pris le dessus !

Je me note donc ça ici, histoire de pas oublier et que ça puisse resservir.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Avec pyproj

![logo PyProj](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/pyproj.png){: .img-thumbnail-left }

Si pyproj est installé :

```sh
pip install pyproj
```

Alors tout est presque trop facile :

```python
import pyproj

print(pyproj.__proj_version__)
```

## Avec les bindings GDAL

![logo GDAL](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/gdal.png){: .img-thumbnail-left }

Si GDAL est installée, ainsi que ses bindings Python :

```sh
pip install gdal
```

Alors on peut utiliser le package `osr` (dédié à l'abstraction sur les systèmes de coordonnées) :

```python
from osgeo import osr

print(
    f"{osr.GetPROJVersionMajor()}."
    f"{osr.GetPROJVersionMinor()}."
    f"{osr.GetPROJVersionMicro()}"
)
```

## Avec le binaire proj et une regex

![logo PROJ](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/proj.png){: .img-thumbnail-left }

Mais si on ne peut compter sur aucune des couches d'abstraction précédentes, alors ça se corse. Il faut appeler l'exécutable de proj et se débrouiller avec la sortie par défaut puisqu'il n'y a pas d'option `--version` :

```sh
> proj
Rel. 8.2.1, January 1st, 2022
usage: proj [-bdeEfiIlmorsStTvVwW [args]] [+opt[=arg] ...] [file ...]
```

Et qu'est ce qu'on fait quand on a doit chercher une structure de texte dans un texte non formaté ? eh bien on ~~se débat~~ s'exprime à la régulière. Joie.

```python
import re
import subprocess

proj_output = check_output(["proj"], stderr=STDOUT, text=True)
version_match = re.search(r"Rel\. ([0-9.]+)", proj_output):
if version_match:
    print(version_match.group(1))
```

## Mais ça, c'était aujourd'hui

![logo open source](https://cdn.geotribu.fr/img/logos-icones/opensource.png){: .img-thumbnail-left }

En tout cas, ça valait le coup de demander autour de moi et auprès de mes collègues puisque Loïc Bartoletti a proposé d'intégrer l'option `--version` à proj ! C'est dans cette [Pull Request](https://github.com/OSGeo/PROJ/pull/3836) que ça se passe et on y apprend plein de choses :

- que certains des [utilitaires packagés avec proj](https://proj.org/en/9.2/apps/index.html) disposent eux d'une option `--version` : `cct --version` et `gie --version`. Il y a donc une incohérence entre les différents CLI qu'il fait bon de mettre en lumière et résoudre.
- que la [demande ne date pas d'hier](https://github.com/OSGeo/PROJ/issues/2640) (mais qu'un malheureux bot avait occulté)
- que j'aurais pu creuser davantage quand j'ai regardé [comment pyproj se débrouille pour déterminer la version de PROJ](https://github.com/pyproj4/pyproj/blob/1452ba404be58c14a6b64d4551c320022f5aafcf/setup.py#L33-L53)

Et surtout que l'open source communautaire, c'est fichtrement vertueux !

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
