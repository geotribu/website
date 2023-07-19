---
title: Obtenir la version de PROJ installée en Python
authors:
    - Julien MOURA
categories:
    - article
date: 2023-07-25 10:20
description: "Mémo technique : comment récupérer la version de PROJ installée depuis un script Python, avec GDAL, PyProj ou le binaire proj."
image:
license: beerware
robots: index, follow
tags:
    - PROJ
    - Python
---

# Python : obtenir la version de PROJ installée

:calendar: Date de publication initiale : 25 juillet 2023

En butant sur un souci de reconnaissance de SRS lié aux choix éclairés de l'IGN en matière de registre spécifique, j'ai eu besoin de vérifier la version de PROJ installée de façon à pouvoir adapter le comportement du script.  
Formulé comme ça, mon candide moi s'est dit :

> allez zou, un coup de `proj --version` ou `-V` dans un subprocess et on n'en parle plus !

C'est alors que mon surmoi de galérien a pris le dessus !

Je me note donc ça ici, histoire de pas oublier et que ça puisse resservir.

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Avec pyproj

![logo PyProj](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/pyproj.png){: .img-rdp-news-thumb }

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

![logo GDAL](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/gdal.png){: .img-rdp-news-thumb }

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

![logo PROJ](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/proj.png){: .img-rdp-news-thumb }

Mais si on ne peut compter sur aucune des couches d'asbtraction précédentes, alors ça se corse. Il faut appeler l'exécutable de proj et se débrouiller avec la sortie par défaut puisqu'il n'y a pas d'option `--version` :

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

## Avec CBAL (Ceinture Bretelles Abstraction Library)

!!! note
    L'opérateur walrus `:=` requiert Python 3.8 et le typage `str | None` Python 3.10. Pour une version Python inférieure (quoique la 3.7 est en EOL depuis ce mois-ci...), penser à adapter la syntaxe :wink:.

```python
# -- IMPORTS --

# standard library
import logging
import re
from subprocess import STDOUT, CalledProcessError, check_output

# condition imports
try:
    from osgeo import gdal, osr

    PYTHON_GDAL_IS_AVAILABLE: bool = True
except ImportError:
    logging.info("GDAL (ou ses bindings Python) n'est pas installé.")
    gdal = osr = None
    PYTHON_GDAL_IS_AVAILABLE: bool = False

try:
    import pyproj

    PYPROJ_IS_AVAILABLE: bool = True
except ImportError:
    logging.info("PyProj n'est pas installé.")
    pyproj = None
    PYPROJ_IS_AVAILABLE: bool = False

# -- GLOBALS --

# logs
logger = logging.getLogger(__name__)

# -- FUNCTIONS --

def get_proj_version() -> str | None:
    """Récupère la version installée de la bibliothèque PROJ.

    Credits:
        Julien Moura (Geotribu)

    Returns:
        str | None: La version de PROJ installée ou None si PROJ n'est pas trouvé.
    """
    proj_version = None

    # from GDAL bindings
    if osr is not None and PYTHON_GDAL_IS_AVAILABLE:
        try:
            proj_version = (
                f"{osr.GetPROJVersionMajor()}."
                f"{osr.GetPROJVersionMinor()}."
                f"{osr.GetPROJVersionMicro()}"
            )
            logger.debug(
                f"Version de PROJ obtenue depuis les bindings Python de GDAL : {proj_version}"
            )
            return proj_version
        except Exception:
            pass

    # from PyProj
    if pyproj is not None and PYPROJ_IS_AVAILABLE:
        try:
            proj_version = pyproj.__proj_version__
            logger.debug(f"Version de PROJ obtenue depuis PyProj : {proj_version}")
            return proj_version
        except Exception:
            pass

    # from PROJ command-line
    try:
        # Exécute la commande "proj" en utilisant subprocess
        result = check_output(["proj"], stderr=STDOUT, text=True)

        # Recherche de la version dans la sortie à l'aide d'une expression régulière
        if version_match := re.search(r"Rel\. ([0-9.]+)", result):
            proj_version = version_match.group(1)
            logger.debug(
                f"Version de PROJ obtenue depuis le binaire proj : {proj_version}"
            )
            return proj_version
        else:
            logger.error(
                "PROJ est bien installé mais impossible de trouver la version en regex."
            )
    except FileNotFoundError as err:
        logger.info(f"Proj n'est pas installé. Trace : {err}")
    except CalledProcessError as err:
        logger.info(f"Erreur lors de l'exécution de la commande : {err}")

    logging.warning(
        "Impossible de déterminer la version de PROJ depuis les bindings GDAL, PyProj, "
        "ou les binaires proj. "
    )
    return proj_version

if __name__ == "__main__":
    """Standalone execution."""
    print(get_proj_version())
```

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

{% include "licenses/beerware.md" %}
