---
title: "Thèmes QGIS4, à vous les studios"
subtitle: Pimp my Georide
authors:
    - Guilhem ALLAMAN
categories:
    - article
comments: true
date: 2026-10-20
description: "Découverte du plugin QGIS Studio Themes, sur QGIS4, pour qustomizer votre logiciel Desktop SIG tout-terrain."
icon: fontawesome/solid/map
image:
license: default
robots: index, follow
tags:
    - Interface graphique
    - QGIS
    - qss
    - Qt
    - UIUX
---

# QGIS Themes plugin: à vous les studios !

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

_La suite est un dialogue à lire avec une voix façon vieux doublage de la TNT du début des années 2000_ :

> - Yo la géotroupe, j'me présente c'est Jean-Marc, mes amis m'appellent Double-Jay car mon nom de famille c'est Jisse. J'roule dans une vieille ArqMap(c) de 1999, et j'dois dire que mes jeunes collègues veulent pas monter dedans, j'sais pas trop quoi faire. J'ai aussi un MapInfo(c) de secours que ma tante m'a légué, celui-là date de 1995, et je modifie mes GeoJSON à la main dans _Edit_ de Windows. J'dois avouer que c'est pas facile tous les jours, et quand ma tire me lâche c'est-à-dire assez souvent, j'dois faire mes cartes sur Paint. _Geotribu Customs(tm)_, est-ce que vous pouvez faire quelque chose pour moi ?
> - Yo Double-Jay, ça roule mon pote ? T'as toqué à la bonne porte mec, mais laisse-moi t'dire un truc d'abord, vieux, c'est à propose de ton _setup_ et de ta géo-caisse: ta tire est un vrai danger mec, même un `.shp` ne veut pas s'asseoir dedans. Alors t'imagines même pas ouvrir un _COG_ ou un _zarr_ avec tes jeunes collègues. Ils veulent du tout-terrain, des étoiles dans les yeux et la tête dans le _cloud_, mec. Alors c'est pas dans ta poubelle antique que tu risques de les conduire en after-work. Mais tout ceci va changer vieux, et aujourd'hui Jean-Marc, on va tuner ta Qaisse.

![Pimp my Georide: Tune ta Qaisse avec le garage Geotribu Customs](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/pimp_my_georide/pimp_my_georide.webp){: .img-center loading=lazy }

> C'est bientôt l'hiver, et pour te réchauffer on va installer de la géo-fourrure rose dans ta barre de menu horizontale. Et comme tu nous as dit que tes jeunes collègues étaient fan de geoparquet, on va installer une piste de bowling dans ta Boîte à Outils de traitement pour que vous puissiez vous amuser en after-work. Allez c'est parti, on ouvre le qapot.

Voilà, fin de l'introduction.... Voici [:point_right: la ref douteuse :point_left:](https://www.youtube.com/watch?v=KTZznOF8zMs), issue de l'émission [_Pimp My Ride_](https://fr.wikipedia.org/wiki/Pimp_My_Ride). Si vous souhaitez creuser davantage ce phénomène culturel essentiel, il y a aussi [une parodie de Mister V.](https://www.youtube.com/watch?v=KTZznOF8zMs)

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Introduction

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-thumbnail-left }

Après [un article de Julien en 2025](../2025/2025-01-28_tester-qgis-4-futur-sig-open-source.md), qui donne à voir ce qu'implique une montée de version majeure de QGIS, j'ai eu envie de (enfin) tester QGIS IV, après avoir fait quelques mèmes au travers du [Qalendrier de l'Avent de Décembre dernier](../2025/2025-12-25_qalendrier_decembre_2025.md).

À l'heure où sont rédigées ces lignes, la _Latest Release_ de QGIS est la 4.2, et le passage du cycle 4 en _Long Term Release_ est prévu pour début Mars 2026, avec la 4.4 qui aura bénéficié au préalable d'un _Feature Freeze_, permettant ainsi aux développeurs/euses de se concentrer sur du bugfix et de la stabilité pour ce nouveau cycle qui s'annonce prometteur.

![Mr Qreeze: 140 goûts assortis parmis lesquels PostGIS, geoparquet, COG... Arômes et colorants naturels, sans conservateurs. 140 x 45mL](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/pimp_my_georide/mr_qreeze.webp){: .img-center loading=lazy }

!!! tip "T'as pas une feuille (de route) ?"
    Un petit coup d'oeil à [la _Roadmap_ du projet QGIS](https://qgis.org/resources/roadmap/#schedule) vous permettra de connaître plus précisément les dates.

Lors de la géo-veille partagée qu'on aime bien faire et voir sur Geotribu - d'ailleurs c'est plutôt actif en ce moment sur le salon matrix :technologist:, venez participer à cette géo-veille [en lisant cet article !](../2026/2026-01-03_entrez-dans-la-matrix-geotribu.md) - j'ai vu passer quelques truqs sympa qui ont l'air possible avec QGIS 4, notamment en terme de customisation de l'interface, de nouveaux thèmes qui rendent bien, etc.

Voilà voilà, c'est le sujet de cet article: _Pimp my QGIS_ !

!!! info "Disclaimer"
    Avec des refs MTV du début des années 2000, c'est disons plutôt _oldskool_ alors autant vous dire que personnellement je suis team _LTR_ : à date j'utilise au quotidien QGIS 3.44, et dans l'optique d'expérimenter et rédiger cet article, je me suis créé une _Virtual Machine_ sur [Kubuntu 26.04](https://kubuntu.org/news/kubuntu-26-04-release-notes/). QGIS 4 y tourne plutôt bien.

!!! warning "J'aime bien [les encarts](https://contribuer.geotribu.fr/guides/admonition/) donc j'en rajoute outrageusement ;)"
    Cet article n'a pas vocation a dérouler comment installer QGIS 4 sur votre machine : si vous êtes sur W1ndows, [la page `download` de QGIS.org](https://qgis.org/download/) vous permet de télécharger un _installer_. Si vous êtes sur [linux](https://qgis.org/resources/installation-guide/#linux), vous pouvez ajouter une nouvelle _source_ apt. Et si vous êtes sur macOS, demandez à [Jeve Stobs](https://github.com/jeve-stobs) !

!!! info "_Yet another_ encart..."
    Je n'ai rien à voir avec ce Jeve Stobs, j'ai simplement _duckduckgoé_ (ohé ohé :duck:) ce terme et balancé en vrac le lien du profil GitHub de cette personne, qui au demeurant a l'air de faire des trucs audio sympa... Ah la la la veille, c'est pas demain la vieille, et les découvertes tiennent à peu de choses...

## QGIS, épisode IV

Une fois QGIS 4 installé, ouvrons-le donc, et notons déjà la nouvelle page d'accueil plutôt jolie :

![Écran de bienvenue de QGIS 4](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/pimp_my_georide/qgis4_welcome_page.webp){: .img-center loading=lazy }

La mécanique des plugins QGIS fait que les développeurs déclarent [une version minimum de QGIS](https://docs.qgis.org/3.44/fr/docs/pyqgis_developer_cookbook/plugins/plugins.html#metadata-txt) avec laquelle chaque plugin est compatible. Passage en version majeure v4 oblige, certains plugins - qui font usage des nouveautés de QGIS4 et Qt6 - sont donc disponibles uniquement à partir de QGIS 4. Partons à la découverte, _Babette_ !

## QGIS Studio Themes

### Présentation

Un plugin a particulièrement retenu mon attention: [`QGIS Studio Themes`](https://plugins.qgis.org/plugins/qgis_studio_themes/).

![Présentation du plugin QGIS Studio Themes, sur le dépôt des plugins QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/pimp_my_georide/plugin_qgis_studio_themes.webp){: .img-center loading=lazy }

Au-delà du logo plutôt sympa, ce plugin est disponible [à partir de la version `4.0` de QGIS](https://github.com/GallPeters/qgis-studio-themes/blob/a5ccec4a04f1f39275cd77191c155298714a7a61/metadata.txt#L4), installons-le et voyons ce qu'il nous propose.

"_Des thèmes modernes qui mettent en valeur l'interface utilisateur de QGIS et reflètent toute sa puissance grâce à un design épuré et professionnel._" ouah, une fois installé le plugin ajoute des nouvelles entrées dans la liste déroulante `UI theme`, dans les paramètres généraux de QGIS - tous les thèmes qui commencent par _Studio_ en fait :

![Sélection d'un thème dans les paramètres généraux de QGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/pimp_my_georide/qgis_settings_theme_selection.webp){: .img-center loading=lazy }

### Thèmes "sur l'étagère"

En voici donc quelques uns, parmi les thèmes fournis directement par le plugin :

!!! warning "Disclaimer"
    J'ai ouvert en parallèle l'interface [du plugin QChat](https://plugins.qgis.org/plugins/qchat/), au-delà du placement de produit(tm) c'est aussi l'occasion d'illustrer comment s'affichent les différents éléments graphiques dans QGIS, en fonction du thème sélectionné.

=== "Studio Pro"
    ![Thème QGIS "Studio Pro"](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/pimp_my_georide/qgis_studio_themes_pro.webp){: .img-center loading=lazy }

=== "Studio Light Orange"
    ![Thème QGIS "Studio Light Orange"](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/pimp_my_georide/qgis_studio_themes_light_orange.webp){: .img-center loading=lazy }

=== "Studio Web"
    ![Thème QGIS "Studio Web"](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/pimp_my_georide/qgis_studio_themes_web.webp){: .img-center loading=lazy }

=== "Studio QGIS Light"
    ![Thème QGIS "Studio QGIS Light"](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/pimp_my_georide/qgis_studio_themes_qgis_light.webp){: .img-center loading=lazy }

Valivala, je trouve personnellement que ça rend plutôt bien, épuré et agréable, avec des différents thèmes clairs et sombres, selon les goûts et appétences de tout-un-chacun.

_Retour de la voix dégueulasse de la TNT / MTV des années 2000..._

> Et maintenant, j'vais filer ta géo-tire au garage de _Geotribu Customs_ : c'est le moment d'ouvrir le capot et d'ajouter de la puissance à ton véhicule. J'vais tuner ton QGIS.

### Les mains dans le qambouis

Au sein du profil QGIS dans lequel on a installé le plugin, le code source est déposé dans `python/plugins/qgis_studio_themes/`.

!!! warning "Disqlaimer"
    C'est (très) crado de modifier le code source d'un plugin comme ça dans le dossier du profil. On peut se noter d'envisager la proposition d'une contribution au plugin `QGIS Studio Themes`, si jamais nos expérimentations sont concluantes et nous amènenent à un "joli" thème...

Notons que dans le fichier `qgis_studio_themes.py`, des variables "globales" python déclarent les thèmes ajoutés par le plugin aux paramètres de QGIS:

```python
THEMES = {
    "Premium": "premium",
    "Web": "web",
    "Pro": "pro",
    "Dark": "dark",
    "Light Orange": "light_orange",
    "QGIS Light": "qgis_light",
}

# Themes that must force the Qt palette colour scheme so unstyled /
# native widgets follow the stylesheet even when the desktop is in
# the opposite mode (e.g. a light theme on a dark desktop).
LIGHT_THEMES = frozenset({"Studio Light Orange", "Studio QGIS Light"})
DARK_THEMES = frozenset(
    {"Studio Premium", "Studio Web", "Studio Pro", "Studio Dark"}
)
```

Déclarons-y un nouveau thème, qu'on appellera `Dolphins`...

> Eh yo tu nous a dit que l'été dernier t'avais bien aimé regarder la mer pendant tes vacances, alors on va te peindre plein de dauphins bleus sur ta qarrosserie, comme ça t'as pas b'soin de faire le déplacement et tu peux mater la mer à travers ta nouvelle tire.

!!! warning "Disclaimer"
    C'est la dernière fois que vous entendez le doublage TNT des années 2000, promis...

En regardant l'arborescence des fichiers fournis par le plugin, on remarque un dossier `themes`, avec un sous-dossier par thème sélectionnable:

![Arborescence des sous-dossiers des thèmes, tel que fourni par le plugin "QGIS Studio Themes"](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/pimp_my_georide/qgis_studio_themes_folders_structure.webp){: .img-center loading=lazy }

Dans chaque sous-dossier donc pour chaque thème, c'est plutôt simple :

- un sous-dossier `icons` dans lequel on peut remplacer les `svg` des icônes de QGIS par d'autres.
- deux fichiers `.qss` pour [`Qt Style Sheet`](https://doc.qt.io/qt-6/stylesheet-syntax.html), un genre de fichier de style façon `css` pour les différents éléments disponibles dans Qt:
    - `style.qss`: ce fichier permet de changer les attributs graphiques des différents widgets, avec des directives qui s'appliquent par exemple à `QMainWindow`, `QDialog` `QDockWidget`, sans oublier les attributs "d'état", par exemple au travers de directives telles `QDockWidget::close-button:disabled`, qui pour le coup va s'appliquer au bouton pour fermer les DockWidgets lorseque ceux-ci sont désactivés... Ces `qss` permettent d'aller assez loin, et si vous avez déjà touché à du `css` vous trouverez assez rapidement votre chemin, car il y a des similitudes dans la manière de déclarer à quel(s) élément(s) les règles s'appliquent.
    - `variables.qss`: ce fichier contient commme son nom l'indique des variables pour factoriser les déclarations de style dans le `style.qss` décrit dessus. Dans notre cas il s'agit principalement des déclarations des couleurs, en [hex](https://www.color-hex.com/).

Changeons donc quelques variables, et voici le thème _Dolphins_ :dolphin: :tada: !

![Thème custom _Dauphins_ dans QGIS, avec texte en couleur cyan et fond en couleur fuchsia](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/pimp_my_georide/qgis_dolphins_theme.webp){: .img-center loading=lazy }

!!! info
    SVP ne me jugez pas: disons que la courbe d'apprentissage est _devant_ moi en termes de Goût et compétences en design...

Voici pour la petite expérimentation avec un nouveau thème dans l'esprit du plugin, et je crois que (_caramaba_) au final on va peut-être pas proposer une contribution au plugin avec ce thème _Dolphins_...

En tout cas si (vous) vous avez du goût, et des capacités en design, n'hésitez pas : plus y'a de thèmes plus on rit !

## Ribbon dans QGIS

Autre truc sympa vu passer récemment dans la veille Geotribu: un post d'[Anita Graser](https://anitagraser.com/) qui montre des expérimentations avec un bandeau (_ribbon_) en-haut de l'interface de QGIS !

<!-- markdownlint-disable MD033 -->
<blockquote class="mastodon-embed" data-embed-url="https://fosstodon.org/@underdarkGIS/117321893260993137/embed" style="background: #FCF8FF; border-radius: 8px; border: 1px solid #C9C4DA; margin: 0; max-width: 540px; min-width: 270px; overflow: hidden; padding: 0;"> <a href="https://fosstodon.org/@underdarkGIS/117321893260993137" target="_blank" style="align-items: center; color: #1C1A25; display: flex; flex-direction: column; font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen, Ubuntu, Cantarell, 'Fira Sans', 'Droid Sans', 'Helvetica Neue', Roboto, sans-serif; font-size: 14px; justify-content: center; letter-spacing: 0.25px; line-height: 20px; padding: 24px; text-decoration: none;"> <svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="32" height="32" viewBox="0 0 79 75"><path d="M63 45.3v-20c0-4.1-1-7.3-3.2-9.7-2.1-2.4-5-3.7-8.5-3.7-4.1 0-7.2 1.6-9.3 4.7l-2 3.3-2-3.3c-2-3.1-5.1-4.7-9.2-4.7-3.5 0-6.4 1.3-8.6 3.7-2.1 2.4-3.1 5.6-3.1 9.7v20h8V25.9c0-4.1 1.7-6.2 5.2-6.2 3.8 0 5.8 2.5 5.8 7.4V37.7H44V27.1c0-4.9 1.9-7.4 5.8-7.4 3.5 0 5.2 2.1 5.2 6.2V45.3h8ZM74.7 16.6c.6 6 .1 15.7.1 17.3 0 .5-.1 4.8-.1 5.3-.7 11.5-8 16-15.6 17.5-.1 0-.2 0-.3 0-4.9 1-10 1.2-14.9 1.4-1.2 0-2.4 0-3.6 0-4.8 0-9.7-.6-14.4-1.7-.1 0-.1 0-.1 0s-.1 0-.1 0 0 .1 0 .1 0 0 0 0c.1 1.6.4 3.1 1 4.5.6 1.7 2.9 5.7 11.4 5.7 5 0 9.9-.6 14.8-1.7 0 0 0 0 0 0 .1 0 .1 0 .1 0 0 .1 0 .1 0 .1.1 0 .1 0 .1.1v5.6s0 .1-.1.1c0 0 0 0 0 .1-1.6 1.1-3.7 1.7-5.6 2.3-.8.3-1.6.5-2.4.7-7.5 1.7-15.4 1.3-22.7-1.2-6.8-2.4-13.8-8.2-15.5-15.2-.9-3.8-1.6-7.6-1.9-11.5-.6-5.8-.6-11.7-.8-17.5C3.9 24.5 4 20 4.9 16 6.7 7.9 14.1 2.2 22.3 1c1.4-.2 4.1-1 16.5-1h.1C51.4 0 56.7.8 58.1 1c8.4 1.2 15.5 7.5 16.6 15.6Z" fill="currentColor"/></svg> <div style="color: #787588; margin-top: 16px;">Post by @underdarkGIS@fosstodon.org</div> <div style="font-weight: 500;">View on Mastodon</div> </a> </blockquote> <script data-allowed-prefixes="https://fosstodon.org/" async src="https://fosstodon.org/embed.js"></script>
<!-- markdownlint-enable MD033 -->

Je trouve personnellement ces travaux intéressants, et l'avenir nous dira si [ce plugin `qgis_tabbed_ui`](https://github.com/anitagraser/qgis-tabbed-ui) a vocation à arriver et vivre dans le dépôt officiel des plugins.

En tout cas, je me dis ça pourrait amener des néophytes à mieux appréhender et retrouver les fonctionnalités de QGIS dans l'interface, qui serait du coup similaire et semblable à pas mal d'autres logiciels, comme par exemple _Libre Office_. À suivre !

## Références

Pour finir dans le _thème_ de l'article, voici quelques références _Pimp my Georide_, trouvées dans [la rubrique _Vehicles_ de _mappery_](https://mappery.org/category/vehicles/)...

![Camionnette blanche avec une carte sur la carrosserie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/pimp_my_georide/mappery_vehicles_trollhatte-channel.webp){: .img-center loading=lazy }

![Petite voiture avec des lignes de niveau peintes sur la carrosserie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2026/pimp_my_georide/mappery_vehicles_spotted-in-lucca.webp){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
