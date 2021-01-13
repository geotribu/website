---
title: "Plugin QGIS : utiliser les icônes intégrées"
authors: ["Julien MOURA"]
categories: ["article", "tutoriel"]
date: "2020-01-14 10:20"
description: "Pour le développement d'un plugin pour QGIS, soigner l'interface graphique peut être fastidieux, notamment de concevoir ou trouver les éléments graphiques. Pourquoi ne pas utiliser les icônes déjà embarquées dans QGIS ?."
image: "https://cdn.geotribu.fr/img/tuto/qgis_plugin_embedded_images/qgis_icons_file-explorer.png"
tags: "geotribu,QGIS,plugin,PyQt5,icônes,interface graphique"
---

# Utiliser les icônes intégrées de QGIS pour égayer ses plugins

:calendar: Date de publication initiale : 13 janvier 2021

**Mots-clés :** QGIS | PyQGIS | développement | plugin | interface graphique

Pré-requis :

- une connexion internet.
- des notions en PyQGIS (Python + Qt + API QGIS)

## Intro

![icône PyQT](https://cdn.geotribu.fr/img/logos-icones/programmation/python_and_qt.svg "Python + Qt = PyQt"){: .img-rdp-news-thumb }

Avec mon arrivée chez [Oslandia], je me remets au développement de plugins pour QGIS alors autant partager de temps en temps quelques cas d’usage :slightly_smiling_face:.

Lorsque qu'il s'agit de soigner l'interface graphique, c'est souvent fastidieux, notamment de concevoir ou de trouver des éléments graphiques. Bien souvent les menus sont dénués d'icônes, au détriment de la convivialité, de l'accessibilité et de la lisibilité.

![menu plugin cadastre](https://cdn.geotribu.fr/img/tuto/qgis_plugin_embedded_images/pyqgis_menu_icons_cadastre.png "Le menu du plugin Cadastre"){: .img-center }
*Pourtant c'est quand même plus joli avec des icônes*
{: align=middle }

Une solution est d'utiliser les images déjà embarquées dans QGIS. Elles sont déjà chargées, intégrées dans le thème de QGIS et sont suffisamment génériques pour bien des cas de figure. La plupart des images sont répertoriées dans le *Resource Collection File* enfin le [fichier de ressources](https://github.com/qgis/QGIS/blob/master/images/images.qrc) quoi.

Par exemple, lorsque l'on ajoute un bouton d'aide à son menu, on peut pointer sur l'icône du manuel d'aide :

```python
self.action_menu_help = QAction(
    QIcon(":/images/themes/default/mActionHelpContents.svg"),
    self.tr("Help") + "...",
    self.iface.mainWindow(),
)
self.iface.addPluginToMenu("Le nom du plugin", self.action_menu_help)
```

On obtient alors :

![menu plugin help](https://cdn.geotribu.fr/img/tuto/qgis_plugin_embedded_images/pyqgis_menu_icons_help.png "icône aide du menu"){: .img-center }

C'est déjà plus sympa et intégré non ?

!!! note
    De la même façon, il est aussi possible d'utiliser les ressources d'un autre plugin en adaptant le chemin avec le préfixe correspondant. Mais il faut pouvoir s'assurer que cet autre plugin soit toujours installé avec le nôtre.

Maintenant, vous n'avez plus aucune excuse pour ne pas mettre de belles icônes dans vos fenêtres et menus ! Avec modération bien sûr :wink:.

----

## Auteur

--8<--
content/team/jmou.md
--8<--

<!-- Hyperlinks reference -->
[Oslandia]: https://oslandia.com/
