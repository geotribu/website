---
title: "Walking papers, ou comment disposer d'OpenStreetMap sur papier"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-08-19
description: "Walking papers, ou comment disposer d'OpenStreetMap sur papier"
tags:
    - open source
    - OpenStreetMap
---

# Walking papers, ou comment disposer d'OpenStreetMap sur papier

:calendar: Date de publication initiale : 19 août 2009

![logo OpenStreetMap](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/Openstreetmap.png "logo OpenStreetMap"){: .img-thumbnail-left }

Dans le cadre d'un projet tel que [OpenStreetMap](https://www.openstreetmap.org/) (OSM) le GPS est l'outil idéal pour enregistrer précisément un parcours. Mais qu'en est-il des informations qu'il est possible de lui rattacher, comment saisir par exemple les numéros des maisons ou encore la position des feux tricolores? Dans ce cas rien ne remplace une bonne feuille de papier et un fond de carte. Néanmoins reste le problème de la (re)-saisie de ces informations afin de les intégrer ensuite dans la base d'OSM.

C'est sur cette problématique qu'est basée la plateforme [Walking Papers](http://walking-papers.org/) dont le but est de vous permettre d'imprimer un fond de carte et de le re-importer par la suite. Vous pouvez ainsi, une fois la zone désirée sélectionnée, enregistrer la carte sur votre ordinateur pour ensuite l'imprimer et l'utiliser sur le terrain. Une fois les informations recueillies il suffira de scanner la carte et de l'uploader sur la plateforme afin de faire les mises à jour directement sur l'outil d'OSM (potlach). Vous pouvez également choisir de rendre ce fond de carte public afin de le partager avec la communauté.

![Walking Papers Workflow](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/walking_papers_workflow.png "Walking Papers Workflow"){: .img-center loading=lazy }

Néanmoins, derrière cette apparente simplicité, se cache un trésor d'ingéniosité. En effet posons-nous simplement cette question : "comment l'application arrive à géoréférencer l'image et cela même si elle a été tournée ou changée d'échelle ?"

En fait, lors des exemples ci-dessus vous vous êtes peut-être demandé à quoi servaient les symboles placés aux 4 coins de l'image? C'est là tout le secret. En effet, une fois les trois éléments des coins haut-droite, haut-gauche et bas-gauche de la carte identifiés grâce à l'algorithme de [SIFT](https://en.wikipedia.org/wiki/Scale-invariant_feature_transform) (Scale Invariant Feature Transform), l'application est alors capable de décoder le [QR Code](https://en.wikipedia.org/wiki/QR_Code) qui identifie la carte (un peu comme un code-barre).

![Paper Map](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/walking_papers_paper_map.png "Paper Map"){: .img-center loading=lazy }

![qr_code geotribu](https://cdn.geotribu.fr/img/internal/qrcode/qrcode_geotribu_fr.png "QR Code du site Geotribu"){: .img-thumbnail-left }

La technologie du QR Code peine à percer en Europe, mais il faut savoir qu'au Japon celle-ci est quotidiennement utilisée ([video dailymotion](https://www.dailymotion.com/video/xemuk_japon-qr-code_tech)). Néanmoins, certains projets tentent de démocratiser son utilisation comme c'est le cas de [Mobulles](2009-03-26_toulouse_ville_numerique.md) que nous avions déjà présenté.

<iframe frameborder="0" type="text/html" src="https://www.dailymotion.com/embed/video/xemuk" width="100%" height="400" allowfullscreen title="Dailymotion Video Player" > </iframe>

Ce que j'aime avec Walking-papers et plus globalement avec OpenStreetMap, c'est la volonté qu'ils mettent à être le plus accessible possible. La technologie est là, bien présente, mais l'utilisateur lambda n'en a pas conscience, tout se passe pour lui naturellement.

----

> Source : [mike.teczno.com](http://mike.teczno.com/notes/slides/open-paper-maps.html)

----

<!-- geotribu:authors-block -->
