---
title: "Configuration de mon environnement de développement de plugins QGIS"
authors:
    - Julien MOURA
categories:
    - article
date: "2022-06-09 10:20"
description: "Description pour le SEO."
image: "Image d'illustration de l'article qui sert ensuite dans la mise en avant : réseaux sociaux, flux RSS..."
license: default
robots: index, follow
tags:
    - développement
    - plugin QGIS
    - PyQGIS
    - QGIS
    - tutoriel
---


# Quand je développe un plugin pour QGIS

:calendar: Date de publication initiale : 9 juin 2022

Lorsque je travaille sur un plugin pour QGIS, j'ai mes petites habitudes

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Quelques prérequis

J'aime disposer à la fois de la version déjà publiée (le cas échéant) et celle sur laquelle je travaille actuellement.

### Linux

```bash
sudo apt update
sudo apt install software-properties-common
```

1. Créer un profil QGIS dédié au dév du plugin : `qgis --profile dev_transdata`
2. Personnaliser rapidement le profil :
    - désactiver le check de version
    - désactiver le fil d'actu
    - désactiver les éléments d'interface inutiles
    - désactiver les extensions inutiles
3. Ajouter la variable d'environnement personnalisée qui va permettre à QGIS de trouver mon plugin :
    - Appliquer = `Ecraser`
    - Variable = `QGIS_PLUGIN_PATH`
    - Valeur = le chemin absolu vers mon plugin. Exemple : `/home/jmo/Git/External/transdata`
4. Installer les extensions de développement :
    - Plugin Reloader
    - VS Debug
5. Relancer QGIS
6. Configurer le Plugin Reloader pour qu'il pointe sur notre plugin
7. Installer Zeal avec les docsets PyQGIS, Qt 5 et autres si besoin (PosgreSQL, etc.)

## Cloner dans un dossier dédié

```bash
git clone git@github.com:geotribu/qtribu.git plg_qtribu_dev
```

## Créer un profil QGIS dédié

Pour bien compartimenter, avoir un environnement neutre, on crée un profil QGIS dédié au plugin :

```bash
qgis --profile plg_qtribu
```

le définir par défaut en modifiant `profiles.ini`

```bash
sed -i "s|^defaultProfile=.*|defaultProfile=plg_qtribu|" ~/.local/share/QGIS/QGIS3/profiles/profiles.ini
```

Ajouter le chemin du dossier via une variable d'environnement :

```bash
sed -i '/\[qgis\]/a customEnvVars="overwrite|QGIS_PLUGINPATH=/home/jmo/Git/Oslandia/QGIS/gml_application_schema_toolbox/"\ncustomEnvVarsUse=true' ~/.local/share/QGIS/QGIS3/profiles/plg_fresh/QGIS/QGIS3.ini
```

## Les plugins qui vont bien

- Plugin Reloader
- Network Logger (pour QGIS < 3.14)
- VS Debugger

## Renommer metadata.txt

Pour distinguer facilement de la version déployée sur le dépôt de plugins

----

## Référencer le plugin dans QGIS

### Ajouter le chemin du dossier en variable d'environnement QGIS

`QGIS_PLUGINPATH` : `vs dev`

![image alt](https://cdn.geotribu.fr/img/tuto/qgis_plugin_dev_setup/qgis_settings_env_var.png "title"){: .img-center loading=lazy }

### Autres options

#### Lien symbolique

Il est également possible d'utiliser les [liens symboliques](https://fr.wikipedia.org/wiki/Lien_symbolique) mais personnellement je n'aime pas trop cette option car :

- c'est trop "transparent" : je suis du genre à oublier que le plugin est référencé via ce mécanisme et si je clique sur "Désinstaller le plugin" depuis QGIS, je perds mon taf, mon setup, ma bonne humeur et ma foi dans l'humanité.
- c'est certes *cross-platform* depuis que Windows 10 permet d'en créer facilement (`mklink /D "D:\Git\Link To Folder" "C:\Users\Name\Original Folder"`) mais c'est plutôt à des fins de compatibilité et ça reste quand même très imprégné de la logique Unix, loin des autres systèmes d'exploitation
- le lien symbolique est référencé dans le système et j'aime pas l'encombrer pour rien (ouais, je suis du genre à n'avoir aucune icône sur mon bureau)

#### Via un script d'installation

C'est le cas qu'on trouve le plus couramment, surtout parmi les vieux ~~développeurs~~ plugins notamment ceux créés par le Plugin Builder : un bon [Makefile](https://github.com/g-sherman/plugin_build_tool/blob/master/test_plugin/Makefile) des familles avec plein de commandes pour faire des heureux

Sauf que :

- `make` c'est génial mais c'est que sur certaines distributions Linux (les principales)
- un plugin QGIS, c'est un package Python ; un langage qui permet notamment de scripter alors pourquoi s'embêter à en maîtriser un autre avec sa syntaxe et ses principes plus bas niveau quand on ne rêve pas de devenir développeur ?
- en vérité, même si c'est un script Python (`package.py`, `install.py`, etc.), j'ai la flemme de le lancer à chaque fois que j'ai besoin de voir le résultat dans QGIS et surtout de le maintenir

![Sweat Partisan du Moindre Effort](https://heroinesministries.files.wordpress.com/2017/12/img_0487.jpg "Sweat Partisan du Moindre Effort")

----

## Un seul script

![logo Partisans du Moindre Effort](https://cdn.geotribu.fr/img/logos-icones/divers/partisan_moindre_effort.webp "logo Partisans du Moindre Effort"){: .img-rdp-news-thumb }

Sur Ubuntu, avec Git et QGIS d'installés, ça donne :

```bash
# télécharger le script dans le dossier que vous voulez
git clone https://gist.github.com/bc7d883922676ab14f857ed951b3a583.git dev_plugin_qgis
cd dev_plugin_qgis

# autoriser l'exécution du script
chmod +x dev_qgis_plugin_setup.sh

# lancer le script en lui passant le dépôt de code distant et le dossier local - adapter à votre goût
./dev_qgis_plugin_setup.sh https://github.com/geotribu/qtribu.git ~/Git/QGIS/qtribu
```

[Voir le script :fontawesome-regular-file-code:](https://gist.github.com/Guts/bc7d883922676ab14f857ed951b3a583){: .md-button }
{: align=middle }

Merci à mon collègue [Loïc Bartoletti](/team/lbar/) pour l'interopérabilité BSD.

----

----

## Ailleurs sur le web

- le [guide de développement de plugin de GIS OPS](https://gis-ops.com/qgis-3-plugin-tutorial-plugin-development-reference-guide/)

----

## Auteur {: data-search-exclude }

--8<-- "content/team/jmou.md"

{% include "licenses/default.md" %}
