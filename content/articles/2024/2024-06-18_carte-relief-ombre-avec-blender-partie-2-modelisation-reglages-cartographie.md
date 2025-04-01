---
title: Réaliser des cartes avec Blender - Partie 2
subtitle: Blindé jusqu’au relief 2
authors:
    - Thomas Szczurek-Gayant
categories:
    - article
comments: true
date: 2024-06-11
description: "Réaliser des cartes de relief avec le logiciel libre 3D Blender. Partie 2 : Modéliser le relief avec Blender."
icon: simple/blender
image:
license: default
robots: index, follow
tags:
    - 3D
    - Blender
    - cartographie
    - GDAL
    - relief
---

# Réaliser des cartes avec Blender - Partie 2

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

La suite de l'article précédent où nous nous étions attardés sur la préparation des données. Aujourd'hui le gros morceau : Blender !

[Lire la première partie :fontawesome-solid-backward:](./2024-05-28_carte-relief-ombre-avec-blender-partie-1-preparation-donnes-avec-qgis-et-gdal.md "Réaliser des cartes avec Blender - Partie 1 : préparation des données"){: .md-button }
{: align=middle }

## Petite présentation de Blender et configuration

![logo Blender](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/blender.png){: .img-thumbnail-left }

Pour télécharger Blender ça se passe [ici](https://www.blender.org/download/). Côté Windows, il est disponible dans le Windows Store et sur Linux il est aussi présent sur [Flatpak](https://flathub.org/apps/org.blender.Blender) si vous aimez ces formats de distribution. C'est un logiciel libre et gratuit, donc pas d'inquiétudes.

Faire le tour de Blender serait bien sûr beaucoup trop ambitieux ici, mais voici quelques indications de base pour celles et ceux qui n'ont jamais ouvert le logiciel.

Blender fonctionne sur un principe d'environnement en fonction de la tâche que vous êtes en train de réaliser (modéliser, travailler sur les textures ...). Pour passer de l'un à l'autre, on clique ici :

![Là](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img6_viewports.png){: .img-center loading=lazy }

3D Viewport est la vue 3D par défaut.

Les boutons situés ici permettent de changer le mode d'affichage des objets 3D (fil de fer, materiaux, rendu...).

![Là](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img7_render.png){: .img-center loading=lazy }

(Vous pouvez essayer avec le cube présent par défaut).

### Réglages préalables (moteur de rendu et carte graphique)

En cliquant là :

![Là](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img8_engine.png){: .img-center loading=lazy }

Vous pouvez changer le moteur de rendu utilisé entre Eevee et Cycles. Eevee est plus couramment utilisé pour du dynamique, et Cycles pour du rendu statique (notre cas). Attention, Cycles est plus gourmand en ressources.

!!! warning
    Choisissez aussi le "Feature Set" Expérimental (nous en aurons besoin).

Enfin, si vous faites des choix de vie douteux comme moi et que votre carte graphique est puissante, passez "Device" en `GPU Compute`.

En fonction de votre carte graphique, vous pouvez aussi faire un tour par le menu `edit -> preferences -> system` et choisir en fonction de votre crêmerie ce qui sera utilisé par Cycles. Choisir [OptiX](https://fr.wikipedia.org/wiki/OptiX) chez Nvidia / [HIP](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html) chez AMD si votre configuration matérielle le supporte (hey, vous venez sur un tuto 3D, il faut s'attendre à ce genre de phrases !).

Toujours là :

![Là](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img9_sampling.png){: .img-center loading=lazy }

En descendant vous verrez "Sampling". Ces options permettent de configurer le nombre de passages qu'effectuera le moteur de rendu en changeant la valeur `max samples`. Je vous conseille de configurer Viewport (quand vous serez en train de travailler mais en affichant quelque chose proche du rendu) avec une valeur basse pour gagner du temps, et Render avec une valeur haute pour avoir un beau rendu final. Activer l'option `Denoise` dans les deux cas qui permet d'enlever du "bruit" sur les rendus. Sur l'image vous verrez ma proposition de paramétrage.

Enfin la chose la plus importante, Blender fonctionne beaucoup avec les raccourcis clavier. Pour ajouter un objet : ++shift+a++.

Pour se déplacer, appuyez sur le bouton central de votre souris (++middle-button++) pour tourner, maintenez ++shift++ en plus pour translater ou ctrl pour zoomer.

## Modéliser le relief

Tout d'abord, on retire le cube par défaut en cliquant dessus pour le sélectionner puis en appuyant sur ++delete++ de votre clavier et on ajoute un plan à notre scène. ++shift+a++ -> `mesh` -> `plane`. Ne pas supprimer la caméra et la source de lumière (les autres trucs présents dans la scène par défaut).

Par défaut les objets apparaissent sous le "curseur 3D" mais on va déplacer notre plan pour le mettre aux coordonnées x 0 y 0 z 0 pour se simplifier la vie si ce n'est pas le cas.

On clique sur notre plan pour le sélectionner (il se détoure alors en orange) et on se rend là :

![La](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img10_loc.png){: .img-center loading=lazy }

On modifie ensuite les valeurs de `Location` x y et z à 0 si ce n'est pas le cas.

Je vous ai déjà parlé de mon amour de GDAL ? Et bien on ve le ressortir avec encore une fois la commande `gdalinfo`. En effet maintenant on va donner à notre plan les dimensions de notre raster d'elevation.

![taille raster](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img11_size.png){: .img-center loading=lazy }

La ligne Size vous donne la taille en pixels de votre mnt.

Toujours dans ce panneau de Blender, on modifie les valeurs de `scale` pour les faire correspondre. Indiquer x 8000 / y 7000 (mon cas) donnerait un plan beaucoup trop grand, l'important étant de garder le ratio. J'indique donc x 0.8 et y 0.7 comme valeur pour scale.

Je ne répèterai pas cette information mais pensez à sauvegarder ! `File > Save as`, puis enregistrez votre espace de travail au format `.blend.`

### Déformer le plan

C'est ici qu'on va commencer a faire des trucs un peu compliqués.

Dans le monde réel, les substances telles que le bois, la roche, le verre ... semblent différentes les unes des autres car elles ont des couleurs, des textures, une rugosité différentes. Blender est conçu pour simuler ces variations en permettant d'attribuer des propriétés reflétant ceci aux `matériaux` attribués aux objets. Les moteurs de rendus calculent ensuite l'apparence des objets ainsi que la dispersion et les rebonds de la lumière en fonction de ces `matériaux`.

Pour l'instant, notre plan ne possède aucun matériau, c'est pourquoi il apparaît gris mat. Si vous effectuez un rendu en cliquant sur `Render -> Render image`, ou en choisissant le mode de visualisation "Rendu" dans le 3D view port, vous vous en rendrez compte.

Pour affecter un matériau au plan, sélectionnez-le puis cliquez sur cette icône :

![setup materials](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img12_material.png){: .img-center loading=lazy }

Maintenant cliquez sur `New`. Blender créera alors un nouveau matériau nommé `Material.001`. Vous pouvez le renommer si vous le désirez.

Pour l'instant nous ne modifierons rien mais voici quelques explications :

- L'option `Surface` indique "Principled BSDF". Ce n'est pas référence à une pratique étrange du yoga mais à un `shader` utilisant une ["Bidirectional Scattering Distribution Function"](https://en.wikipedia.org/wiki/Bidirectional_scattering_distribution_function). Les `shaders` indiquent à Blender la manière dont la lumière rebondi sur les objets. Chaque `shader` présent dans cette liste représente un modèle mathématique d'interaction de la lumière avec l'objet. Utiliser autre chose que Principled BSDF permet de faire des objets qui ressemblerons à du verre, du coton... mais ce n'est pas ce que nous voulons ici donc on va laisser ce paramètre tranquille.

- Il y a beaucoup d'options pour ce `shader` : la rugosité, l'indice de refraction, la couleur ... mais pour le moment nous voulons un plan plat et réaliste, donc on ne touche à rien. On y reviendra plus tard.

Les `matériaux` ne servent pas qu'à assigner une couleur ou une interaction avec la lumière. Ils peuvent aussi posséder un `displacement` / `déplacement`, soit une déformation de leur surface. C'est comme ça que nous allons transformer notre plan en un modèle de relief réaliste.

Changez l'environnement de travail pour passer de "3D Viewport" à "Shader Editor" (voir la petite présentation de Blender plus haut pour voir comment faire).

Cette interface permet de régler les paramètres du `matériau` comme précédemment, mais bien plus encore. Faites bien attention à bien sélectionner votre plan en cliquant là :

![selectionner le plan](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img13_explorer.png){: .img-center loading=lazy }

La manière dont est rendu votre `matériau` est présentée sous forme d'un diagramme. Vous pouvez cliquer sur chacune des boîtes pour les déplacer, ainsi que vous déplacer dans la vue comme dans le 3D View Port.

Chaque boîte est un `node` et vous verrez une ligne reliant "Principle BSDF" à la "Surface" de notre `matériau` final, indiquant qu'il est utilisé pour déterminer son apparence. Vous verrez que vous pouvez aussi relier quelque chose qui donnera à la surface un `displacement`.

Depuis la barre de menu située au dessus de l'écran, choisissez `Add > Texture > Image Texture`.

![ajouter texture](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img14_addtexture.png){: .img-center loading=lazy }

Une nouvelle boite apparait. Positionnez-la où bon vous semble. Dans le language de Blender, une `texture` est une image ou une motif qui sera appliqué aux `matériaux` pour changer leur apparence. On pourrait ainsi charger une image de grain de bois pour faire ressembler notre plan à du bois. Mais ces textures peuvent aussi être utilisées pour générer un `displacement`.

- Cliquez sur `Open` dans cette boite et indiquez votre `mnt.TIF`.
- Cliquez sur le petit cercle à côté de `Color` en maintenant le bouton gauche de la souris appuyé.
- Et relier à `Displacement`
- Tant que nous y sommes, changez l'option `Linear` pour `Smart`. Ceci change l'interpolation de la texture pour être un peu plus jolie.

![ajouter texture](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img15_displacement.png){: .img-center loading=lazy }

Vous pouvez faire un essai de rendu en cliquant sur `Render -> Render Image` dans le menu tout en haut.

![ajouter texture](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img16_1strender.png){: .img-center loading=lazy }

Pour reprendre les mots de l'auteur originel : "Tout ceci est bâti sur un mensonge". Pour le moment Blender ne fait que **simuler** la déformation en utilisant une technique nommée _bump mapping_. C'est plus rapide à calculer mais pas aussi réaliste. Cette technique ne fait que donner une _apparence_ de profondeur, mais elle n'est pas réelle : aucune ombre n'est projetée et la lumière n'interagit pas avec l'objet.

On va faire beaucoup mieux.

### Subdiviser la surface

Pour l'instant notre plan est trop simpliste, car uniquement composé de 4 `vertices`/`vertex`/`noeud`/whatever -vous voyez de quoi je parle.

Ces `vertices` sont ce que Blender utilise pour déformer le terrain, et pour le moment, Blender ne pourrait utiliser que les quatre coins de l'image.

Pour l'instant ces derniers ne sont pas utilisés, Blender n'a fait que _peindre_ le relief sur le plan avec des nuances de gris. On pourrait ajouter des `vertices` à la main, mais on va utiliser une autre astuce. Les `modificateurs`.

- Retournez dans le `3D Viewport`
- Toujours bien penser à sélectionner le plan et cliquer sur l'icône en forme de clef à molette.
![modifiers](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img17_modifiers.png){: .img-center loading=lazy }
- Et maintenant, cliquez sur "Add Modifier"
- L'apparence de ce menu a été modifiée dans la toute dernière version de Blender mais l'idée est de choisir le groupe "Generate" puis ["Subdivision Surface"](https://docs.blender.org/manual/fr/4.1/modeling/modifiers/generate/subdivision_surface.html).

Apparemment, la communauté Blender surnomme ce modificateur `subsurf` ou `subdiv`. Ne me demandez pas. Il est très utilisé et permet de dire à Blender d'ajouter du détail à un objet (ainsi il permet de faire des objets très arrondis en travaillant avec des `mesh` simples).

Dans notre cas on va l'utiliser pour faire croire à Blender que notre objet est composé de très nombreux morceaux afin de simuler beaucoup de `vertices`.

- Deux algorithmes sont possibles et celui que nous voulons ici est `simple`.
- Si vous avez bien écouté au fond de la salle, vous verrez un bouton "adaptive subdivision" qu'il faut activer, sinon retournez sur la partie de présentation / configuration de Blender pour passez le feature set de `Cycles` à `Expérimental`. Vous savez, celle ou j'avais indiqué "important". En gras.
- Cette option indique à Blender de ne pas subdiviser la surface par un nombre défini mais là où _le plus de détail est necessaire_ en fontion de la taille de votre image et de la position de la caméra.
- Ce `modificateur` est non-destructif, il ne modifie par réellement l'objet. C'est une pile qui s'ajoute _par dessus_ alors qu'il est toujours constitué de quatre `vertices`. Blender ne subdivisera le plan que temporairement lors du rendu.

### Déplacement réel

- On retourne dans le "shader editor".
- `Add -> vector ->` [displacement](https://docs.blender.org/manual/fr/dev/render/shader_nodes/vector/vector_displacement.html)`

![true displacement](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img18_t_displacement.png){: .img-center loading=lazy }

Et on modifie notre diagramme pour qu'il ressemble à ceci :

![true displacement 2](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img19_t_displacement2.png){: .img-center loading=lazy }

Color vers height et displacement vers displacement. Ceci dit à Blender "regarde la couleur (clair ou sombre) et transforme ça en déplacement".

!!! tip "Changer l'espace colorimétrique"
    Tant que nous y sommes, changez le `color space` de votre texture MNT de `sRGB` à `non-color`.
    Dans la majorité des cas, les textures sont utilisées pour appliquer une image sur des objets, mais ce n'est pas notre cas. Si on laisse en `sRGB`, Blender va appliquer une courbe de correction sur notre couleur de MNT au lieu d'attribuer une hauteur de relief de façon linéaire en fonction du niveau de gris.

Si vous effectuez un rendu maintenant vous constaterez que pas grand-chose n'a changé. En effet il faut demander à Blender d'arrêter de bump mapper et de modifier réellement steuplé.

Dans les paramètres de notre matériau, sous la section `Settings -> Surface` réglez `displacement` à `displacement only`.

![true displacement 3](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img20_t_displacement3.png){: .img-center loading=lazy }

Vous pouvez tester un render et sous vos yeux émerveillés vous auto congratuler. Vous êtes beaux/belles et fort/es. (j'ai rien contre le point médian mais on devine que ce choix a été fait par des gens qui ne tapent pas sur un clavier d'ordinateur ! C'est ++alt+0+1+8+3++ mais sous [ghostwritter](https://ghostwriter.kde.org/fr/) ça marche pas).

![true displacement 4](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img21_t_displacement4.png){: .img-center loading=lazy }

Vous remarquez cependant trois choses :

- C'est très exagéré
- Les bords sont cracra
- le temps de rendu est beaucoup plus long

En changeant le paramètre `scale` du `node` `displacement` du shader editor, vous pouvez réduire l'exagération (on est ici dans l'artistique et plus dans le technique, donc pas de recommandation à part votre feeling). Comme notre éclairage et notre caméra ne sont pas encore configurés il est trop tôt pour s'en préoccuper.

Pour ce qui est des bords ce qui se passe c'est que pour le moment, Blender essaye de répéter votre image sur les bords. Dans le shader editor, sur le `node` de votre image, changez _Repeat_ pour _Extend_ pour corriger ça.

![extend](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img22_extend.png){: .img-center loading=lazy }

C'est déjà mieux !

![render2](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img23_render2.png){: .img-center loading=lazy }

Pour améliorer nos temps de rendu, nous avons déjà modifié le nombre de passages. Mais il est aussi possible de diminuer la taille des tiles (ce qui permet d'avoir un aperçu plus rapide du résultat et de stopper le rendu si celà ne nous convient pas)

Ça se passe ici :

![tiles_size](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img24_tiles.png){: .img-center loading=lazy }

Et vous pouvez par exemple diminuer à 512.

Comme dans l'article original, je vous incite à explorer les matériaux. Sauvegardez votre espace de travail puis changez des valeurs au hasard pour voir ce que ça donne (mais ne sauvegardez pas ensuite !)

## La caméra

![caméra de surveillance](https://cdn.geotribu.fr/img/logos-icones/divers/camera_surveillance.png){: .img-thumbnail-left }

On retourne dans le 3D view port. La caméra, c'est ce machin ci-contre :

![Blender - La caméra](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img25_camera.png){: .img-right loading=lazy }

Elle determine la position de la vue lors des rendus. En appuyant sur la touche 0 du pavé numérique de votre clavier vous pouvez "voir" ce que voit la caméra (réaappuyer sur 0 pour sortir). Si l'idée saugrenue d'utiliser Blender sur un pc portable sans pavé numérique vous est venue, il faudra à chaque fois passer par le menu `View -> Cameras -> active Camera` pour obtenir le même effet.

On veut que notre caméra soit située juste au-dessus de notre plan, et avec un angle de 0 degré.

- On la sélectionne (elle devient orange)
- On va dans le paneau des propriétés de l'objet.
- Et dans `Transform`, on passe les valeurs de location x et y = 0, et z = 3 (la valeur de z n'a pas trop d'importance à part d'être supérieure à 0, voir plus bas)
- Toujours dans `Transform`, on passe toutes les valeurs de rotation à 0

![réglages caméra](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img26_camera_settings.png){: .img-center loading=lazy }

Si vous passez en vue caméra vous verrez qu'on commence à avoir quelque chose qui ressemblera a une carte.

Il nous faut encore régler le ratio de la prise de vue pour le faire correspondre à celui de notre mnt/plan. Ça se fait dans les `output properties`. Dans Format (ou Dimensions dans d'anciennes versions de Blender), indiquez les dimensions en pixels de votre raster que vous aviez otenus avec `gdalinfo`. Ce paramètre modifie la résolution de sortie des rendus et vous verrez la caméra changer en fonction pour presque s'adapter aux dimensions de votre plan.

En dessous se trouve le symbole `%` qui adaptera la résolution indiquée par ce pourcentage lors des rendus. Cela peut être intéressant lors de rendus intermédiaires pour accélérer le processus, ou si comme moi votre raster est très grand et que vous avez des petits problèmes de mémoire lors des rendus.

![réglages caméra](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img27_camera_settings2.png){: .img-center loading=lazy }

Faisons maintenant un rendu pour voir.

![rendu3](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img28_render3.png){: .img-center loading=lazy }

Deux conclusions s'imposent.

1. Ça commence à avoir de la tronche
1. Houston nous avons un problème

Je considère que nous sommes entre géomaticien/nes ou personnes intéressées par le sujet. Le terme d'**ortho**photographie ne vous est pas inconnu et je n'ai pas à expliquer le concept de vue en perspective/orthographique.

Bon allez.

![diff ortho perspective](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img29_ortho.jpg){: .img-center loading=lazy }

Mais je ne ferai pas plus d'efforts.

Pour passer la caméra en vue orthographique, on la sélectionne, puis dans ses propriétés on change son type en "orthographic".

![ortho](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img30_ortho2.png){: .img-center loading=lazy }

Vous verrez par contre que maintenant votre caméra prend une zone beaucoup plus grande que votre plan. Pour remédier à ça, il faut paramétrer la valeur d'`orthographic scale` de ce même panneau. Pour trouver la bonne valeur, il faut multiplier par deux la plus grande dimension de votre plan. Ainsi, j'avais créé un plan de 0,8 x 0,7, donc dans mon cas 0,8 x 2 = 1,6. J'ai réussi ça de tête.

![rendu 3 ou 4 je sais plus](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img31_render3.png){: .img-center loading=lazy }

C'est beaucoup mieux !

Maintenant, on peut s'intéresser à l'exagération du relief. On retourne dans le shader editor, et sous le `node` `displacement`, on règle la valeur de `scale`. Vous pouvez faire des rendus pour voir ce qui vous convient le mieux. Personnellement je vais mettre cette valeur à 0,5.

## La lumière

![Cadran solaire](https://cdn.geotribu.fr/img/logos-icones/divers/sundial.png "Cadran solaire"){: .img-thumbnail-left }

On va maintenant régler la source de lumière qui éclaire notre sène. La source de lumière c'est ce truc :

![lumière](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img32_light.png){: .img-center loading=lazy }

Après l'avoir sélectionnée, cliquez sur l'icône en forme de bulbe d'ampoule :bulb: pour accéder à ses propriétés.

![réglages lumière](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img33_light2.png){: .img-center loading=lazy }

Plusieurs types de sources sont possibles (ampoule, spot...). Mais dans notre cas on veut une lumière naturelle.

Choisir donc "boule de feu géante abritant en son coeur des réactions de fusion nucléaire qui se transformera en [naine blanche](https://fr.wikipedia.org/wiki/Naine_blanche) à sa mort mais pas avant d'avoir enflé jusqu'aux limites de la terre la carbonisant au passage mais qui si elle était plus massive finirait en [étoile à neutrons](https://fr.wikipedia.org/wiki/%C3%89toile_%C3%A0_neutrons) voir en [trou noir stellaire](https://fr.wikipedia.org/wiki/Trou_noir_stellaire) dont notre physique n'arrive pas à expliquer les singularités centrales sans unifier la relativité générale et la quantique et ça fait 100 ans qu'on cherche, prend ça dans ta face la science."

Ou bien juste `sun` (ça veut dire [soleil](https://fr.wikipedia.org/wiki/Soleil)) :sun:.

Pour celles et ceux qui préfèrent la première version, je vous conseille [ceci](https://www.youtube.com/watch?v=zjIC6jIQRKQ) (avec un type qui a des patchs sur les coudes de ses vestes). Il a aussi écrit [ça](https://www.dunod.com/sciences-techniques/univers-multiples-nouveaux-horizons-cosmiques) si vous voulez vous retourner la tête. Si vraiment vous êtes hardcore il y a aussi [ceci](https://www.odilejacob.fr/catalogue/sciences/astronomie-astrophysique-cosmologie/ecume-de-l-espace-temps_9782738139719.php). Promis j'arrête.

Une ampoule près de vous enverra ses rayons dans toutes les directions. Dans le cas du soleil, il est suffisamment éloigné (et gros) pour que ses rayons arrivent à nous orientés tous selon le même angle (rappelez-vous vos cours de pourquoi qu'il fait chaud à l'équateur et froid aux pôles). C'est ce que simulera Blender en douchant notre scène de lumière provenant d'une unique direction.

Avec ce type de lumière, la position de l'objet la générant dans la scène n'est pas importante. Si vous effectuez un rendu maintenant vous vous rendrez compte que tout est très surexposé car nous n'avons pas réglé sa force (strength). Passons ce paramètre de 1000 à ... 5.

Pour définir l'angle d'incidence des rayons lumineux il faut se rendre dans les propriétés de l'objet (attention à bien le sélectionner) et changer sa rotation (pour les sources de lumière de type soleil).

Indiquer 0 pour x, 45 pour y et 135 pour z.

![réglages lumière](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img34_light3.png){: .img-center loading=lazy }

La valeur de `y` contrôle l'angle par rapport à l'horizon, et celle de `z` la direction de provenance. Une valeur de 135 vous donne une lumière qui arrive du Nord Ouest (en haut à gauche quoi), ce à quoi l'oeil humain est habitué pour une carte. Mettre 225 donnerait l'impression que notre relief est inversé.

Le tout dernier réglage à faire est de régler la taille de notre soleil. On reclique sur la petite ampoule verte et on regarde le paramètre Angle, mal nommé puisqu'il correspond au [diamètre angulaire](https://fr.wikipedia.org/wiki/Taille_apparente). Changer sa valeur régle la _douceur_ de la lumière. Avec une valeur basse par défaut, notre lumière nous donne un relief lunaire, essayez plutôt une valeur de 90 pour quelque chose de plus doux.

![réglages lumière](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender//img35_light4.png){: .img-center loading=lazy }

Un petit rendu pour la route ?

![rendu 5](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img36_render6.png){: .img-center loading=lazy }

Waoohh !!!

## Coloriser

![Color](https://cdn.geotribu.fr/img/logos-icones/divers/color_wheel.png "Color"){: .img-thumbnail-left }

Pour ça, je vais vous laissez vous reposer et ne pas ressortir GDAL, mais réouvrir un logiciel obscur nommé ArqGIS dans lequel on va charger notre raster d'élévation. L'idée va être de générer une image colorée qu'on appliquera ensuite dans Blender comme texture.

Si vous avez de l'eau :

On ouvre la calculatrice raster (`raster -> calculatrice`) et on tape juste cette formule `mnt@1 <= 0`. On enregistre sur le disque le résultat plutôt que de faire un raster virtuel car l'algorithme suivant veut un fichier (par exemple eau.tif). (le chiffre derriere le @ désigne le numéro de bande de l'image à utiliser).

Celà nous permet de générer un raster comprenant des 0 et des 1 en fonction de la hauteur par rapport au niveau de la mer. Comme notre raster d'origine est très précis, on va le tamiser pour retirer les pixels isolés et rendre le résultat plus propre ( [GDAL_sieve.py](https://GDAL.org/programs/GDAL_sieve.html) ). Ça se passe avec `raster -> Analyse -> Tamiser`.

- On sélectionne notre raster eau.
- l'option `seuil` détermine la taille limite des polygones qui devront êtres fusionnés avec leur voisin le plus proche
- `use 8-connectedness` permet de spécifier si on veut que les pixels en diagonale soient considérés ou non pour déterminer l'isolation d'un pixel.

Personnellement je choisis un seuil de 75 et je n'utilise pas 8-connectedness ici pour vraiment nettoyer.

Enfin, on va polygoniser le résultat pour transformer ça en couche vecteur : `raster -> conversion -> Polygoniser`.
Cet algorithme ne permet pas de créer une couche vectorielle en mémoire, donc veillez à bien indiquer un fichier de sortie :

- soit au format [Geopackage](https://www.geopackage.org/), une base SQLite normée par l'[OGC](https://www.ogc.org/)
- soit [FlatGeoBuf](http://flatgeobuf.org/), un format moderne optimisé cloud avec un fichier = une couche conçue pour la simplicité d'usage
- pas en [geojson](https://blog.ianturton.com/gis/2023/11/11/geojson.html) s'il vous plait.

On fait un clic droit sur notre vecteur d'eau, et on choisi filtrer avec la formule suivante "DN"=1. DN est le champ où la valeur du raster a été conservée. Vous pouvez maintenant donner une couleur bleue à votre eau (voilà, vous pouvez être prof de sémiologie).

Pour le reste :

1. On selectionne notre raster de mnt, et dans son style on change bande grise unique pour Pseudo-couleur à bande unique.
1. Dans palette de couleur, on choisit "créer une nouvelle palette" puis "catalogue cpt-city"

    ![catalogue cpt city](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img37_cptcity.png){: .img-center loading=lazy }

1. Descendre dans la section "Topography" et par exemple choisir "DEM_screen"
1. Une fois validé cliquez sur "classer"
1. Pour bien faire il faudrait rectifier la palette en fonction de vos hauteurs maximums mais comme je commence à vraiment aimer pouvoir finir (autre manière de dire : j'ai la grosse flemme), j'aurai des hauteurs de 198 mètres qui paraitront couvertes de neiges éternelles.

![menteur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img38_menteur.png){: .img-center loading=lazy }

Maintenant, essayez de zoomer sur la carte pour l'avoir la plus grande possible, mais complète sur votre écran. Puis choisir dans le menu `Projet -> Importer/Exporter -> Exporter la carte au format image` (ça permet d'exporter le contenu de votre canevas de carte sans passer par le composeur). Changez la résolution en 300 dpi et exporter au format PNG.

Maintenant ouvrez cette image dans [The Gimp](https://www.gimp.org/), un éditeur d'image libre, gratuit et open source. La seule et unique manipulation est de passer par le menu `image -> rogner` selon le contenu. Celà supprimera tout le blanc qui restait visible et d'obtenir une image avec le même ratio que notre mnt. Puis `fichier -> écraser` `couleur.png` (le nom de mon image).

On revient maintenant dans le `shader editor` de Blender. Comme pour ajouter notre mnt, on passe par le menu `Add -> Texture -> Image texture`. On sélectionne notre image de couleur, on n’oublie pas de passer l'interpolation en smart et l'extension en extend, mais on laisse le color space en sRGB. Puis on relie `color` à `Base color` de principled BSDF.

![coloriser](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img39_coloriser.png){: .img-center loading=lazy }

Et on effectue le rendu final !!!

![render final](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img40_renderfinal.png){: .img-center loading=lazy }

## Conclusion

On pourrait bien sûr jouer un peu plus avec les réglages (je trouve par exemple mes ombres encore un peu trop profondes et pourrai passer du temps sur le paramètre angle de ma lumière soleil), ou les couleurs (je trouve ce vert bouteille assez moche), ou encore sur le tamisage de notre couche d'eau, mais vous avez maintenant la base de la technique !

Voici par exemple ce que ça donne lors d'un essai précédent où j'ai passé un peu plus de temps à tout régler

![render final](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/gdal_qgis_blender/img41_pyrennees_render.png){: .img-center loading=lazy }

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-nc-sa.md" %}
