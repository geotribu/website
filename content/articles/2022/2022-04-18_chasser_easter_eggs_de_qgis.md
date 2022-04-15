---
title: "Les easter eggs de QGIS : chasser et être chassé"
authors: ["Julien MOURA"]
categories: ["article"]
date: "2022-04-18 10:20"
description: "Les easter eggs de QGIS sont connus : contributors, dizzy, hackfests, bored, user groups... Mais comment les dénicher ? Et surtout comment en créer de nouveaux ?"
image: "https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/qgis_316_easteregg_user_groups.png"
license: default
robots: index, follow
tags:
    - easter egg
    - PyQGIS
    - GitHub
    - QGIS
---

# Les _easter eggs_ dans QGIS : chasser et être chassé

:calendar: Date de publication initiale : 18 avril 2022

<https://eeggs.com/tree/154.html>

<https://halshs.archives-ouvertes.fr/halshs-02508252/document>

## NOTES

- préciser la "généalogie" si elle existe avec le jeu vidéo
- créer du lien social ? appartenance à une commaunauté (réf à une culture commune) ? encourager la relecture du code (cache-cache) ?
- oeuvre collective :
    - ajouter sa marque perso ?
    - être taquin anonyme ?
- easter egg inédit

## Introduction

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-rdp-news-thumb }

Tradition ~~séculaire~~ technique, devenue populaire depuis l'avènement du [Konami Code](https://fr.wikipedia.org/wiki/Code_Konami), les [_easter eggs_](https://fr.wikipedia.org/wiki/Easter_egg) sont des fonctions cachées par des développeurs mutins dans les logiciels (sur les Debian, entrer `apt moo`). Il y a même un site dédié à leur inventaire : <https://eeggs.com/>.

### Et ailleurs... dans la cartographie par exemple

C'est l'objet de la publication ["A la recherche des œufs de Pâques cartographiques" de Delphine Montagne](https://halshs.archives-ouvertes.fr/halshs-02508252/document) (magazine Carto, le monde en cartes, Areion, 2020, pp.54-55. halshs-02508252) :

![Easter egg cartographique - Annecy](https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/easter_egg_carto_ign_annecy_delphine-montagne.png "Easter Egg - Lac d'Annecy (IGN) - Delphine Montagne HAL/Carto")

### Dans QGIS

Après avoir pris le temps d'essayer les [easter eggs listés sur Pasq.fr](https://pasq.fr/easter-egg-dans-qgis) et d'en faire [un tweet](https://twitter.com/geojulien/status/1378954806367297538) pour le lundi de Pâques, on m'indique qu'il en manque un : `user groups` ! Damned !

Mais comment les trouver à coup sûr ? Comment s'assurer de ne pas revenir bredouille de la chasse aux géœufs de Pâques ?

Je vous livre ma stratégie de battue :rabbit: !

<iframe width="100%" height="400" src="https://www.youtube-nocookie.com/embed/suOhOAVOQ6g" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

----

## La battue

!!! info
    Pour des raisons d'éthique évidentes, nous nous interdisons ici d'avoir recours à des armes de recherche massive qui pourraient mettre en péril le délicat équilibre des fonctions cachées. _Exit_ donc Google et consorts (quoique Qwant pourrait être toléré...)

### En planque

![GRASS loupe](https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/grass_mapset_search.svg "Planqué dans l'herbe"){: .img-rdp-news-thumb }

La première tactique est le dogme de la passivité : il suffit d'attendre bien sagement qu'une information sorte sur un easter egg. Au temps des infox[^1], mieux vaut s'appuyer sur les sources officielles : les notes de version visuelles.

Véritable bijou de transparence et de vulgarisation des évolutions techniques d'un logiciel, ces _visual changelogs_ permettent également de faire des recherches à travers les âges de QGIS.

Cherchons donc [_easter egg_](https://www.qgis.org/en/search.html?q=easter+egg&check_keywords=yes&area=default) :

![Changelog QGIS - Recherche easter egg](https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/qgis_changelogs_search_easter_egg.png "Changelog QGIS - Recherche easter egg"){: .img-center loading=lazy }

Hum, cela nous mène uniquement à [celui apparu dans la 3.16](https://www.qgis.org/fr/site/forusers/visualchangelog316/index.html?highlight=fonction%20cach%C3%A9e#add-user-groups-easter-egg) et le moteur de recherche semble mal gérer les caractères spéciaux (espaces et accents), vu les résultats retournés par une [requête en français sur "fonction cachée"](https://www.qgis.org/fr/search.html?q=fonction+cach%C3%A9e).

Voilà qui ne suffit pas à satisfaire notre soif d'exhaustivité !

### Au coeur du terrier

![Octocat GitHub détective](https://octodex.github.com/images/inspectocat.jpg "Octocat GitHub détective"){: .img-rdp-news-thumb }

Prenons notre courage à `0:n` mains (oui, je reste vague pour n'exclure personne, pas même un/e éventuel/le lecteur/ice manchot/e) et allons à la source : le code sur GitHub :scream_cat:.  
L'occasion de démystifier ce qui se cache sous QGIS en se répétant ce que Napoléon disait toujours à ses troupes face aux cyber-attaques caratcéristiques de la campagne de Russie :

> N'ayez pas peur : les logiciels informatiques ne sont ni plus ni moins que des fichiers textes bien organisés !

Hauts les coeurs ! Si c'est du texte, il doit bien y avoir des traces des mots-clés qui déclenchent les _easter eggs_ !

Une fois infiltré dans le _repository_ (là où les gens qui parlent couramment machine entreposent le code source), on peut lancer [une recherche bien sentie](https://github.com/qgis/QGIS/search?q=%22user+groups%22&type=code) dans la barre en haut à gauche :

![Recherche dans le GitHub de QGIS](https://cdn.geotribu.fr/img/tuto/qgis_easter_eggs/qgis_github_search_easteregg.png "Rechercher dans le code de QGIS sur GitHub"){: .img-center loading=lazy }

C'est donc dans la [fonction de validation des coordonnées que se terrent les fonctions cachées](https://github.com/qgis/QGIS/blob/760a436f4f52a02533140b3f24c0828f8fdbd071/src/app/qgsstatusbarcoordinateswidget.cpp#L113-L161) :

En poussant plus loin notre avantage, on peut même retrouver [quand et par qui le dernier _easter egg_ a été proposé puis ajouté](https://github.com/qgis/QGIS/pull/38505) et au passage prendre connaissance du [tableau de suivi des groupes d'utilisateur/ices de QGIS dans le monde](https://docs.google.com/spreadsheets/d/1Wte5pfcpOeZ1bfBUn7KJuYzw31_rtKyGqciBPW3RXwg/edit#gid=678994363).

C'est fou la transparence, c'est beau l'open source :heart_eyes: !

----

## Ajouter un easter egg

![fff](https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/propertyicons/plugin-new.svg){: .img-rdp-news-thumb }

Maintenant que l'on sait où sont terrés les fonctions cachées _officielles_, comment résister à la tentation d'y ajouter le nôtre ? :innocent:

```python


# PyQGIS
import PyQt5
from qgis.core import QgsProjectMetadata, QgsProject
from qgis.gui import QgsStatusBar
from qgis.PyQt.QtWidgets import QLineEdit


# fonction appelée quand la barre de coordonnées est modifiée
def on_coords_changed(coords_line_edit: QLineEdit):
    if coords_line_edit.text() == "geotribu":
        print("Geotribu mode enabled")
        coords_line_edit.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        current_project = QgsProject.instance()
        current_project.setTitle("Geotribu Easter Egg")

        # metadata
        gt_md = QgsProjectMetadata()
        gt_md.setAuthor("Geotribu")
        gt_md.setLanguage("FRE")
        current_project.setMetadata(gt_md)

# on attrape la barre de statut de QGIS
qgis_st = iface.mainWindow().statusBar()

# on filtre la barre de statut pour ne garder le widget des coordonnées
for wdgt in qgis_st.children()[1].children():
    if wdgt.objectName() == "mCoordsEdit":
        break

# dans le widget, on ne garde que la ligne de saisie
le_coords = wdgt.findChild(PyQt5.QtWidgets.QLineEdit)
```

Si vous voulez voir un exemple d'implémentation, j'ai caché un easter egg dans [notre plugin QTribu](/articles/2021/2021-04-01_qtribu_plugin_qgis_geotribu/) :wink:.

----

## Auteur

--8<-- "content/team/jmou.md"

<!-- Hyperlinks reference -->
[^1]: équivalent officiel de _fake news_. Source : [LégiFrance](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000037460897).
