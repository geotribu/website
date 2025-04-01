---
title: "Développement QGIS : utiliser les documentations hors-ligne avec Zeal"
authors:
    - Julien MOURA
categories:
    - article
comments: true
date: 2021-03-02
description: "Blog-note de développement sur QGIS : présentation de Zeal qui permet de naviguer hors-ligne dans les documentations techniques de QGIS, PyQGIS, PostGIS etc."
icon: material/bookshelf
image: https://cdn.geotribu.fr/img/tuto/qgis_doc_dash_zeal/zeal_search_filtered_pyqgis_qgsprovider.png
tags:
    - développement
    - documentation
    - PyQGIS
    - QGIS
    - Zeal
---

# Utiliser Zeal pour développer sur QGIS

:calendar: Date de publication initiale :  {{ page.meta.date | date_localized }}

![logo Zeal Docs](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/zeal.png "logo Zeal Docs"){: .img-thumbnail-left }

Quand on développe sur QGIS (un plugin, un traitement ou carrément dans le coeur), la documentation technique est souvent ouverte quelque part dans le navigateur web.  
Mais il est justement fastidieux de naviguer dans une documentation et on a tôt fait de se retrouver avec beaucoup (trop) d'onglets, occasionnant de la confusion voire ~~du troll~~ des soucis de RAM  :innocent:.

![troll Chrome](https://cdn.geotribu.fr/img/tuto/qgis_doc_dash_zeal/troll_chrome_tabs.jpeg "Troll nombre d'onglets sur Chrome"){: .img-center }

J'avais vu passer le [tweet d'un de mes collègues](https://twitter.com/CabiecesJ/status/1339870135897747456) sur sa contribution à [Zeal] et m'étais alors mis le lien de côté.  
C'est un autre collègue qui m'en a reparlé récemment (coucou [Loïc](https://twitter.com/lo_bartoletti)) : il était donc temps d'essayer !

![Capture d'écran de Zeal](https://cdn.geotribu.fr/img/tuto/qgis_doc_dash_zeal/zeal_search_filtered_pyqgis_qgsprovider.png "Zeal - Recherche filtrée sur PyQGIS"){: loading=lazy }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Présentation

### Historique

![logo Dash](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/dash_docs.png "logo Dash"){: .img-thumbnail-left }

A la base, [Zeal] est une imitation open-source assumée de [Dash], un logiciel pour MacOS uniquement développé par (Maître) Kapeli (en fait un développeur indépendant, Bogdan Popescu) et vendu 30$. Notons que l'éditeur de Dash connaît et tolère bien Zeal et que ce dernier a un accès aux documentations (*docsets*) du premier.

![Bannière Dash](https://cdn.geotribu.fr/img/tuto/qgis_doc_dash_zeal/dash_banner.png "Bannière Dash")

Zeal est donc un équivalent open-source (GPL 3, [dépôt GitHub](https://github.com/zealdocs/zeal)) en Qt (le même cadriciel[^1] graphique que QGIS) packagé pour les plateformes ignorées par Dash : Windows et Linux donc, sans oublier [les vrais unix ou Haiku](https://github.com/haikuports/haikuports/tree/master/app-doc/zeal).

### Principes

![logo lessive Dash](https://cdn.geotribu.fr/img/tuto/qgis_doc_dash_zeal/dash_lessive.jpg "logo lessive Dash"){: .img-thumbnail-left }

C'est simple, l'application se compose de deux ingrédients :

- l'interface graphique qui est *grosso modo* **un mini navigateur web** avec des onglets et un volet de favoris
- les **docsets** : les documentations en elle-mêmes structurées et distribuées sous forme de flux que l'on télécharge pour en disposer hors-ligne

----

## Installer

Sur Ubuntu, c'est simple :

```bash
sudo apt install zeal
```

Sur Windows, il y a [un installateur](https://zealdocs.org/download.html#windows) ou bien avec Chocolatey (entre autres) :

```powershell
choco install zeal
```

----

## Télécharger les docsets

Une fois Zeal installé, il s'agit de télécharger les documentations qui nous intéressent. Il y a deux cas de figure.

### Docsets intégrés

![logo Python](https://cdn.geotribu.fr/img/logos-icones/programmation/python.png "logo Python"){: .img-thumbnail-left }

Soit la documentation est maintenue par [Dash] et elle est donc directement intégrée. C'est le cas de nombreux langages de programmation.  
Il suffit alors de la charger via le menu `Tools > Docsets...`, dans l'onglet `Available`. Par exemple pour Python 3 :

![Zeal Python](https://cdn.geotribu.fr/img/tuto/qgis_doc_dash_zeal/zeal_feeds_dash_python.png "Zeal - Docsets Python"){: loading=lazy .img-center }

### Docsets de la communauté

![logo Open Source](https://cdn.geotribu.fr/img/logos-icones/opensource.png "logo Open Source"){: .img-thumbnail-left }

Soit il s'agit d'une documentation propre à un projet ou à un cadriciel[^1] (*framework*) moins généraliste. Il faut alors de nouveau s'émerveiller devant la force des dynamiques de contribution communautaire et utiliser les documentations publiées sur <https://zealusercontributions.now.sh/>.

![Zeal - Docsets de la commaunauté](https://cdn.geotribu.fr/img/tuto/qgis_doc_dash_zeal/zeal_feeds_qgis.png "Zeal - Docsets de la commaunauté filtrés sur le mot-clé qgis"){: loading=lazy }

C'est justement le cas des **docsets** pour QGIS et PyQGIS, pour lesquelles on peut remercier Julien Cabieces :wine_glass: (<-- cet emoji désigne un verre de Gaillac) qui a fait les [mises à jour en décembre dernier](https://github.com/Kapeli/Dash-User-Contributions/pulls?q=is%3Apr+is%3Aclosed+qgis).

Elles se présentent alors sous forme de flux, qu'il s'agit d'ajouter via le bouton `Add feed` en bas de l'onglet `Installed` et d'entrer le flux récupéré depuis le site web.

Comme je suis sympa, je vous reporte ici les flux correspondant aux documentations de [QGIS](https://qgis.org/api/3.16/) et [PyQGIS](https://qgis.org/pyqgis/3.16/) :

Pour développer sur QGIS :

```http
https://zealusercontributions.now.sh/api/docsets/QGIS.xml
```

![Zeal - Flux QGIS](https://cdn.geotribu.fr/img/tuto/qgis_doc_dash_zeal/zeal_feeds_contrib_qgis.png "Zeal - Flux QGIS"){: loading=lazy .img-center }

Pour développer sur PyQGIS :

```http
https://zealusercontributions.now.sh/api/docsets/PyQGIS.xml
```

![Zeal - Flux PyQGIS](https://cdn.geotribu.fr/img/tuto/qgis_doc_dash_zeal/zeal_feeds_contrib_pyqgis.png "Zeal - Flux PyQGIS"){: loading=lazy .img-center }

!!! tip
    Avec un peu de curiosité, on trouve plein d'autres pépites : PostGIS (2.1), Pandas, etc.

----

## Utiliser

L'utilisation est simple mais voici quelques astuces histoire de fluidifier l'expérience.

### Recherche filtrée

![Filtre QGIS](https://raw.githubusercontent.com/qgis/QGIS/master/images/themes/default/mActionFilter2.svg "Filtre QGIS"){: .img-thumbnail-left }

Il est possible de filtrer sa recherche sur l'une des documentations en utilisant son préfixe (un peu à la manière du [localisateur de QGIS](https://docs.qgis.org/3.16/fr/docs/user_manual/introduction/qgis_configuration.html#locator-settings)). Par exemple pour chercher dans PyQGIS, on préfixe avec `pyqgis_3:` :

<video width="700" controls>
    <!-- markdownlint-disable MD033 -->
    <source src="https://cdn.geotribu.fr/img/tuto/qgis_doc_dash_zeal/zeal_demo_pyqgis.mp4" type="video/mp4">
    Votre navigateur ne supporte pas la balise video HTML 5.
    <!-- markdownlint-enable MD033 -->
</video>

### Intégrer à son IDE

L'outil s'intègre dans de nombreux environnements de développement. Par exemple pour Visual Studio Code, il y a cette extension : <https://github.com/deerawan/vscode-dash>.

----

## Conclusion

Zeal me semble utile particulièrement pour les personnes faisant du développement mais sans forcément le socle de compétences initiales qui va avec ; catégorie dans laquelle je nous range, géomaticien/nes que nous sommes. Le fait de pouvoir naviguer entre les documentations est très pratique : QGIS retourne un QStringList ? hop, tu recherches dans la doc et voilà ! Même pas le temps pour le doute !

C'est aussi avec ce genre d'outil que l'on se rend compte des bénéfices du travail de documentation et de la dynamique de capitalisation/partage qu'est l'open source.

En plus, avec ces documentations hors-ligne, on gagne quelques points de *green-it friendly* en épargnant un paquet de requêtes réseau :leafy_green:. Car, certes les documentations peuvent être tirées avec les paquets mais le gros avantage c'est d'avoir cela dans un seul endroit et accessible à tous (y compris sur des systèmes ou `man` n'existe pas :scream:).

----

<!-- geotribu:authors-block -->

<!-- Footnotes reference -->
[^1]: traduction de *framework* recommandée par l'Office québécois de la langue française. Source : [Wikipedia](https://fr.wikipedia.org/wiki/Framework#Traduction_fran%C3%A7aise)

<!-- hyperlinks reference -->
[Dash]: https://kapeli.com/dash
[Zeal]: https://zealdocs.org/
