---
title: "Réaliser des cartes avec Blender"
authors:
    - Thomas Szczurek-Gayant
categories:
    - article
comments: true
date: 2024-04-07
description: "Technique permettant de réaliser des cartes de relief avec le logiciel libre 3d Blender, ainsi qu'un petit tutoriel gdal"
icon: simple/blender
image: https://github.com/thomas-szczurek/images/blob/main/title.png
license: default
robots: index, follow
tags:
    - cartographie
    - Blender
    - gdal
---

# Réaliser des cartes avec Blender

(et aussi un petit tuto gdal en lignes de commandes)

Cet article se base sur celui initialement paru en anglais sur [somethingaboutmaps](https://somethingaboutmaps.wordpress.com/2017/11/16/creating-shaded-relief-in-blender/), dont on remerciera l'auteur pour l'article initial et l'aimable autorisation d'écrire celui-ci.

Ou comment faire des cartes qui ont la classe. Grossièrement, la technique consiste à déformer un plan avec un raster d'élévation.

Je vais ici utiliser le  MNT à 1 mètre issus du [RGE ALTI](https://geoservices.ign.fr/rgealti) de l'IGN sur le département des Pyrennées Atlantiques, ce qui permettra d'avoir et du relief (ce qui rend bien avec cette technique) et de la mer (sacro-sainte règle des effets de manche pour avoir la classe : mettez de la flotte).

Il y a plusieurs étapes de préparation des données et l'une d'entre elle nécessite obligatoirement l'utilisation de gdal en lignes de commande. Restez ici ! Rien de bien compliqué et on vous explique tout (et on va profiter de cet article pour essayer de faire tout les pré-traitmements raster en lignes de commande pour s'y familiariser. Au cazou j'indiquerai aussi comment faire avec Qgis).

Ceci implique d'avoir accès à gdal. Sur windows ça passe en se rendant dans votre répertoire d'installation de Qgis et ensuite en démarrant OSGeo4W.bat. Je considère que les linuxiens sont assez aguéris pour se débrouiller (au pire faites vous un environnement [mamba](https://mamba.readthedocs.io/en/latest/) qui va bien (miniconda réécrit en c/c++)) et je refuse par principe de parler aux appeliens (sauf à ma cheffe de service car je suis bien obligé).

## Préparation des données

Après récupération du jeu de données, chargez une des dalles au format asc dans qgis. Le format asc ne gère pas les projections et Qgis essayera par défaut de les positionner en WGS 84 (ne vous inquietez pas, les coordonnées sont les bonnes). Vous pouvez repositionner l'image en cliquant sur la petite icône de l'image ci-dessous et en spécifiant ce bon vieux Lambert 93.

![Ca arrive même aux meilleurs](https://github.com/thomas-szczurek/images/blob/main/img1_lign.png)

Sur ces considérations on chargera plutôt la couche "dalles" [dans le format dont il ne faut pas prononcer le nom](http://switchfromshapefile.org/) située dans le dossier "3_SUPPLEMENTS_LIVRAISON" de l'archive et on active un fond de plan open street map sous "xyz tiles" de l'explorateur de Qgis histoire de se repérer.

### Mosaïquage

On va ici créer un fichier qui nous permettra de fusionner les dalles voulues pour notre carte.

- Dans Qgis, on sélectionne les dalles de la région (rectangulaire) que l'on souhaite cartographier et on exporte la sélection au format csv qu'on nommera select.csv.
- On ouvre ce fichier dans LibreOfficeCalc (ou logiciel propriétaire équivalent) et on supprime l'entête des colonnes ainsi que toutes les colonnes sauf celle contenant le nom des tuiles.
- Dans la colonne adjacente on écrit cette formule :

```
# Libre office
=CONCAT(A1;".asc")
# Excel
=CONCATENER(A1;".asc")
```

- On tire la formule et on remplace par les valeurs "en dur " avec un collage spécial
- Puis on supprime la colonne d'origine.
- Enfin on change à la brutasse l'extension du fichier en .txt ce qui nous donne une fois ouvert :

![exemple fichier tuile](https://github.com/thomas-szczurek/images/blob/main/img2_tuiles.png)

- On déplace ce fichier directement dans le répertoire contenant les tuilles asc téléchargées.

Et maintenant GDAL coeuravélesdoigts.

Pour les non initiés à la ligne de commande, on se déplace dans un répertoire avec la commande cd (pour change directory). On peut soit passer un repertoire situé dans le repertoire courant, soit une adresse complète.

Ex :
cd /home/nabuchodonosor/Documents (Linux)
cd C:\\\Users\nabuchodonosor\Documents (Windows)

Sur windows pour changer de lecteur juste indiquer la lettre et les deux points, sans cd (exemple `D:`).

(on peut copier l'adresse dans l'explorateur et la coller pour se simplifier la vie)

Pour remonter d'un cran dans l'arboresence :
`cd ..`

Vous vous souvenez de ces gens relous qui vous demandent des noms de dossiers/fichiers juste en alphanumériques et sans espaces mais avec des _ ? C'est pour ça.

Les commandes gdal sont accompagnées de `-` ou `--` et de lettres, ceci correspond aux options spécifiques du programme.

On se déplace dans le dossier contenant les images ex :

![exemple fichier tuile](https://github.com/thomas-szczurek/images/blob/main/img3_cd.png)

Et maitenant on va utiliser [gdal_merge.py](https://gdal.org/programs/gdal_merge.html), le programme de gdal permettant de fusionner des images.

```bash
gdal_merge.py -o mosaic.tif -co BIGTIFF=YES --optfile select.txt
```

L'option`-o` permet de spécifier le nom du fichier de sortie (c'est donc obligatoire). On ne caressera jamais assez dans le sens du poil les gens derrière gdal donc on dit que c'est très fort et ça reconnait le type de fichier désiré juste avec l'extension.

`-co` correspond aux options spécifiques non pas du programme mais du driver du type de fichier (ici geotiff). BIGTIFF permet de faire des tif de plus de 4gb. Ce n'est pas mon cas ici mais ça ne coute rien de passer la commande par sécurité.

Il faut ensuite normalement spécifier un par un les noms de fichiers à fusionner ce qui serait fastidieux, mais l'option `--optfile` nous permet de passer un fichier contenant une liste, d'où les étapes précedantes !

Dans le repertoire vous trouverez votre geotiff mosaic.tif que je vous encourage à déplacer ailleurs pour s'y retrouver.

Dans ~~l'interface graphique de gdal~~ Qgis cette étape est faisable via le menu raster -> Divers -> fusion (il faut au préalable charger l'ensemble des tuiles voulues dans qgis).

### Reprojection

On va maintenant reprojeter (vous vous souvenez des fichiers asc ?) notre image avec [gdalwarp](https://gdal.org/programs/gdalwarp.html) le programme servant à ... reprojeter.

Se déplacer dans le répertoire où vous avez placé l'image et :

```bash
gdalwarp -t_srs EPSG:2154 -r near -co BIGTIFF=YES mosaic.tif mosaicl93.tif
```

- L'option `-t_srs` sert à indiquer le srid de sortie.
- `-r` permet de spécifier la méthode de rééchantillonage. Le choix dépasse le cadre de cet article mais sachez que des methodes avancées comme cubicspline ou lanczos peuvent donner des résultats "floutés" car modifiant la valeur des pixels selon des courbes. On va donc rester sur la méthode par défaut : nearest neighbour (plus proche voisin) pour éviter ceci.

Pour celles et ceux à l'aise avec gdal, vous pouvez compresser les images pour réduire la taille des fichiers de sortie au moins en deflate (pour les autres, ça se fait en passant une seconde option pour le driver de type de fichier : `-co COMPRESS=methode`, la plus courrament utilisée étant `-co COMPRESS=DEFLATE` pour s'assurer de la compatibilité avec tous les systèmes / logiciels).

Sinon, ça se fait avec raster -> Projection -> Assigner une projection dans Qgis.

### Fausser les données

Oui. Nous allons commettre ceci. Ne sortez pas les bidons d'essence tout de suite s'il vous plait. Pour ce que nous allons en faire, Blender n'accepte que les images en entier 16 bits non signés (UInt16, on y reviendra), donc une plage de valeur pour les pixels comprise entre 0 et 65 535. Mais sans virgules, ce que contient notre raster initial donc on perdrait du détail. L'idée est donc de réattribuer aux pixels de notre image des valeurs sur l'ensemble de cette plage, ceci pour bénéficier de l'entièreté de cette finesse.

On fait ça avec [gdal_calc.py](https://gdal.org/programs/gdal_calc.html) mais on peut aussi rester simple et faire ça avec la calculatrice raster de Qgis.

Tout d'abord, on normalise notre raster car certaines valeurs peuvent êtres en dessous de 0 (notamment quand il y a de l'eau). On va donc les mettres à 0.

```bash
gdal_calc.py -A moasicl93.tif --outfile=mosaic_cut.tif --calc="A*(A>=0)"
```

Avec gdal_calc.py les maths doivent être "[numpy](https://numpy.org/) style".

- `-A` permet d'attribuer un raster à une lettre qui sera ensuite utilisée dans la formule.
- `--outfile` le nom du fichier de sortie (ça dépend des programmes gdal, souvent c'est la position du nom qui fait foi dans la commande).
- `--calc` la formule de calcul, entourée de "".

Ou dans qgis : raster -> calculatrice raster puis

![calc_raster](https://github.com/thomas-szczurek/images/blob/main/img4_calc.png)

if (condition, valeur si vrai, valeur si faux)

On regarde les valeurs minimum et maximum de notre raster. Soit dans les propriétés de la couche qgis, soit avec [gdalinfo](https://gdal.org/programs/gdalinfo.html).

```bash
gdalinfo -mm mosaic_cut.tif
```

- l'option `-mm` permet de forcer le calcul des valeurs min/max qui n'est pas donné par défaut par gdalinfo. Elles apparaitrons tout en bas (dans mon cas, 0 et 196,8).

![La](https://github.com/thomas-szczurek/images/blob/main/img5_minmax.png)

Le calcul à faire pour réaffecter nos pixels est le suivant :
(Valeur pixel – min) ÷ (max – min) * 65535

Dans mon cas celà donne :

```bash
gdal_calc.py -A mosaic_cut.tif --outfile=mosaic_rescale.tif --calc="(A - 0) / (196.8 - 0) * 65535"
```

Dans la calculatrice raster de Qgis celà donnerai :
("mosaic_cut@1" - 0) / (196.8 - 0) * 65535.

Enfin, on va convertir notre raster en UInt16 pour l'import dans Blender. C'est cette opération qui n'est pas réalisable dans Qgis sans circonvolutions. Donc on sort [gdal_translate](https://gdal.org/programs/gdal_translate.html), le programme qui sert à faire des conversions.

```bash
gdal_translate -ot UInt16 mosaic_rescale.tif mnt.tif
```

- `-ot` est l'option qui permet de forcer le type de données de sortie.
- les fichiers d'entrée et de sortie se précisent par leur position dans la commande comme précisé dans la [**documentation**](https://gdal.org/index.html) très complète de gdal que je m'efforce de vous inciter à consulter depuis le début en vous en spammant le lien le plus de fois possible.

## Petite présentation de Blender et configuration

Pour télécharger Blender ça se passe [ici](https://www.blender.org/download/). C'est un logiciel libre donc pas d'inquiétudes. (sur Linux il est aussi présent sur [Flatpak](https://flathub.org/apps/org.blender.Blender)).

Faire le tour de Blender serait bien sur beaucoup trop ambiteux ici, mais voici quelques indications de base pour celles et ceux qui n'ont jamais ouvert le logiciel.

Blender fonctionne sur un principe d'environnement en fonction de la tache que vous êtes en train de réaliser (modéliser, travailler sur les textures ...). Pour passer de l'un à l'autre, on clique ici :

![La](https://github.com/thomas-szczurek/images/blob/main/img6_viewports.png)

3D Viewport est la vue 3d par défaut.

Les boutons situés ici permettent de changer le mode d'affichage des objets 3d (fil de fer, materiaux, rendu ...).

![La](https://github.com/thomas-szczurek/images/blob/main/img7_render.png)

(vous pouvez essayer avec le cube présent par défaut).

**Important**

En cliquant là :

![La](https://github.com/thomas-szczurek/images/blob/main/img8_engine.png)

Vous pouvez changer le moteur de rendu utilisé entre Eevee et Cycles. Eevee est plus couramment utilisé pour du dynamique, et Cycles pour du rendu statique (notre cas). Attention, Cycles est plus gourmant en ressources. Choisissez aussi le "Feature Set" Expérimental (nous en aurons besoin). Enfin, si vous faites des choix de vie douteux comme moi et que votre carte graphique est puissante, passez "Device" en GPU compute.

En fonction de votre carte graphique, vous pouvez aussi faire un tour par le menu edit -> preferences -> system et choisir en fonction de votre crémerie ce qui sera utilisé par Cycles. Choisir [OptiX](https://fr.wikipedia.org/wiki/OptiX) chez Nvidia / [HIP](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html) chez AMD si votre configuration matérielle le supporte (hey, vous venez sur un tuto 3d, il faut s'attendre à ce genre de phrases !).

Toujours là :

![La](https://github.com/thomas-szczurek/images/blob/main/img9_sampling.png)

En descendant vous verez Sampling. Ces options permettent de configurer le nombre de passages qu'effectuera le moteur de rendu en changeant la valeur max samples. Je vous conseille de configurer Viewport (quand vous serez en train de travailler mais en affichant quelque chose proche du rendu) avec une valeur basse pour gagner du temps, et Render avec une valeur haute pour avoir un beau rendu final. Activer l'option Denoise dans les deux cas qui permet d'enlever du "bruit" sur les rendus. Sur l'image vous verez ma proposition de paramètrage.

Enfin la chose la plus importante, Blender fonctionne beaucoup avec les raccourcis clavier. Pour ajouter un objet : `shift + A`.

Pour se déplacer, appuyez sur le bouton central de votre souris (le clic de la molette) pour tourner, maintenez shift en plus pour translater ou ctrl pour zoomer.

## Modéliser le relief

Tout d'abord, on retire cube par défaut en cliquant dessus pour le sélectionner puis en appuyant sur `suppr` de votre clavier et on ajoute un plan à notre scène. `shift + A` -> mesh -> plane. Ne pas supprimer la caméra et la source de lumière (les autres trucs présents dans la scène par défaut).

Par défaut les objets apparaissent sous le "curseur 3D" mais on va déplacer notre plan pour le mettre aux coordonnées x 0 y 0 z 0 pour se simplifier la vie si ce n'est pas le cas.

On clique sur notre plan pour le sélectionner (il se détoure alors en orange) et on se rend là :

![La](https://github.com/thomas-szczurek/images/blob/main/img10_loc.png)

On modifie ensuite les valeurs de `Location` x y et z à 0 si ce n'est pas le cas.

Je vous ai déjà parlé de mon amour de gdal ? Et bien on ve le ressortir avec encore une fois la commande `gdalinfo`. En effet maintenant on va donner à notre plan les dimensions de notre raster d'elevation.

![taille raster](https://github.com/thomas-szczurek/images/blob/main/img11_size.png)

La ligne Size vous donne la taille en pixels de votre mnt.

Toujours dans ce panneau de Blender, on modifie `scale` pour faire correspondre. Indiquer x 8000 / y 7000 (mon cas) donnerai un plan beaucoup trop grand, l'important est de garder le ratio. J'indique donc x 0.8 et y 0.7 comme valeur pour scale.

Je ne répeterai pas cette information mais pensez à sauvegarder ! File -> save as et enregistrez votre espace de travail au format `.blend.`

### Déformer le plan

C'est ici qu'on va commencer a faire des trucs un peu compliqués.

Dans le monde réel, les substances telles que le bois, la roche, le verre ... semblent différentes les unes des autres car elles ont des couleurs, des textures, une rugosité différentes. Blender est conçu pour simuler ces variations en permettant d'attribuer des propriétés reflétant ceci aux `materiaux` attribués aux objets. Les moteurs de rendus calculent ensuite l'apparence des objets ainsi que la dispersion et les rebonds de la lumière en fonction de ces `matériaux`.

Pour l'instant, notre plan ne possèque aucun matériau, ce pourquoi il apparait gris mat. Si vous effectuez un rendu en cliquant sur render -> render image, ou en choissant le mode de visualisation "rendu" dans le 3d view port, vous vous en rendrez compte.

Pour affecter un matériau au plan, selectionnez le puis cliquez sur cette icone :

![setup materials](https://github.com/thomas-szczurek/images/blob/main/img12_material.png)

Puis cliquez sur `New`. Blendez créera alors un nouveau materiau nommé Material.001. Vous pouvez le renommer si vous le désirez.

Pour l'instant nous ne modifierons rien mais voici quelques explications :

- L'option `Surface` indique "Principled BSDF". Ce n'est pas référence à une pratique étrange du yoga mais à un `shader` utilisant une ["Bidirectional Scattering Distribution Function"](https://en.wikipedia.org/wiki/Bidirectional_scattering_distribution_function). Les `shaders` indiquent à Blender la manière dont la lumière rebondi sur les objets. Chaque `shader` présent dans cette liste représente un modèle mathématique d'interaction de la lumière avec l'objet. Utiliser autre chose que Principled BSDF permet de faire des objets qui ressemblerons à du verre, du coton... mais ce n'est pas ce que nous voulons ici donc on va laisser ce paramètre tranquille.

- Il y a beaucoup d'options pour ce `shader` : la rugosité, l'incide de refraction, la couleur ... mais pour le moment nous voulons un plan plat et réaliste, donc on touche à rien. On y reviendra plus tard.

Les `matériaux` ne servent pas qu'à assigner une couleur ou une interaction avec la lumière. Ils peuvent aussi posséder un `displacement` / `déplacement`. Soit une déformation de leur surface. Et c'est comme ça que nous allons transformer notre plan en un modèle de relief réaliste.

Changez l'environnement de travail pour passer de "3D View port" à "Shader editor" (voir la petite présentation de Blender plus haut pour voir comment faire).

Cette interface permet de régler les paramètres du `matériau` comme précédemment, mais bien plus encore. Faites bien attention à bien sélectionner votre plan en cliquant là :

![selectionner le plan](https://github.com/thomas-szczurek/images/blob/main/img13_explorer.png)

La manière dont est rendu votre matériau est présentée sous forme d'un diagramme. Vous pouvez cliquer sur chacune des boites pour les déplacer, ainsi que vous déplacer dans la vue comme dans le 3d View Port.

Chaque boite est un `node` et vous verrez une ligne reliant Principle BSDF à la "Surface" de notre `matériau` final, indiquant qu'il est utilisé pour déterminer son apparence. Vous verrez que vous pouvez aussi relier quelque chose qui donnera a la surface un `displacement`.

Depuis la barre de menu située au dessus de l'écran, choisissez Add -> Texture -> Image texture.

![ajouter texture](https://github.com/thomas-szczurek/images/blob/main/img14_addtexture.png)

Une nouvelle boite apparait, positionnez la où bon vous semble. Dans le language de Blender une `texture` est une image ou un motif qui sera appliqué aux `matériaux` pour changer leur apparence. On pourrait ainsi charger une image de grain de bois pour faire ressembler notre plan à du bois. Mais ces texture peuvent aussi être utilisées pour générer un `displacement`.

- Cliquez sur `Open` dans cette boite et indiquez votre mnt.tif.
- Cliquez sur le petit cercle à côté de `Color` en maintenant le bouton gauche de la souris appuyé.
- Et relier à `Displacement`
- Tant que nous y sommes, changez l'option `Linear` pour `Smart`. Ceci change l'interpolation de la texture pour être un peu plus jolie.

![ajouter texture](https://github.com/thomas-szczurek/images/blob/main/img15_displacement.png)

Vous pouvez faire un essai de rendu en cliquant sur Render -> render image dans le menu tout en haut.

![ajouter texture](https://github.com/thomas-szczurek/images/blob/main/img16_1strender.png)

Pour repprendre les mots de l'auteur originel "Tout ceci est bâti sur un mensonge". Pour le moment Blender ne fait que **simuler** la déformation en utilisant une technique nommée *bump mapping*. C'est plus rapide à calculer mais pas aussi réaliste. Cette technique ne fait que donner une *apparence* de profondeur, mais elle n'est pas réelle : aucune ombre n'est projetée et la lumière n'interagit pas avec.

On va faire beaucoup mieux.

### Subdiviser la surface

Pour l'instant notre plan est trop simpliste, car uniquement composé de 4 `vertices`/`vertex`/`noeud` whatever vous voyez de quoi je parle.

Ces `vertices` sont ce que Blender utilise pour déformer le terrain et pour le moment Blender ne pourrait utiliser que les quatre coins de l'image.

Pour l'instant ces derniers ne sont pas utilsés, Blender n'a fait que *peindre* le relief sur le plan avec des nuances de gris. On pourrait ajouter des `vertices` à la main mais on va utiliser une autre astuce. Les `modificateurs`.

- Retournez dans le 3d View Port
- Toujours bien penser à sélectionner le plan et cliquez sur l'icone en forme de clef à molette.
![modifiers](https://github.com/thomas-szczurek/images/blob/main/img17_modifiers.png)
- Et maintenant cliquez sur "Add modifier"
- L'apparence de ce menu a été modifiée dans la toute dernière version de Blender mais l'idée est de choisir le groupe "Generate" puis ["Subdivision Surface"](https://docs.blender.org/manual/fr/4.1/modeling/modifiers/generate/subdivision_surface.html).

Apparemant la communauté Blender surnomme ce modificateur "subsurf" ou "subdiv". Ne me demandez pas. Il est très utilisé et permet de dire à Blender d'ajouter du détail à un objet (ainsi il permet de faire des objets très arrondis en travaillant avec des `mesh` simples).

Dans notre cas on va l'utilier pour faire croire à Blender que notre objet est composé de très nombreux morceaux afin de simuler beaucoup de `vertices`.

- Deux algorithmes sont possibles et celui que nous voulons ici est `simple`.
- Si vous avez bien écouté au fond de la salle, vous verrez un bouton "adaptive subdivision" qu'il faut activer, sinon retournez sur la partie de présentation / configuration de Blender pour passez le feature set de Cycles à expérimental. Vous savez, celle ou j'avais indiqué "important". En gras.
- Cette option indique à Blender de ne pas subdiviser la surface par un nombre défini mais là où *le plus de détail est necessaire* en fontion de la taille de votre image et de la position de la caméra.
- Ce `modificateur` est non destructif, il ne modifie par réellement l'objet. C'est une pile qui s'ajoute *par dessus* alors qu'il est toujours constitué de quatre `vertices`. Blender ne subdivisera le plan que temporairement lors du rendu.

### Déplacement réel

- On retourne dans le "shader editor".
- Add -> vector -> [displacement](https://docs.blender.org/manual/fr/dev/render/shader_nodes/vector/vector_displacement.html)

![true displacement](https://github.com/thomas-szczurek/images/blob/main/img18_t_displacement.png)

Et on modifie notre diagramme pour qu'il ressemble à ceci :

![true displacement 2](https://github.com/thomas-szczurek/images/blob/main/img19_t_displacement2.png)

Color vers height and displacement vers displacement. Ceci dit à Blender "regarde la couleur (clair ou sombre) et transforme ça en déplacement".

**important**

Tant que nous y sommes, changez le `color space` de votre texture mnt de **sRGB** à  **non-color**. Dans la majorité des cas, les textures sont utilisées pour appliquer une image sur des objets, mais ce n'est pas notre cas. Si on laisse en sRGB, Blender va appliquer une courbe de correction sur notre couleur de mnt au lieu d'attribuer une hauteur de relief de façon linéaire en fonction du niveau de gris.

Si vous effectuez un rendu maintenant vous constaterez que pas grand chose n'a changé. En effet il faut demander à Blender d'arrêter de bump mapper et de modifier réellement steuplé.

Dans les paramètres de notre matériau, sous la section `Settings`-> `Surface` réglez displacement à "displacement only".

![true displacement 3](https://github.com/thomas-szczurek/images/blob/main/img20_t_displacement3.png)

Vous pouvez tester un render et sous vos yeux emerveillés vous auto congratuler. Vous êtes beaux/belles et fort/es. (j'ai rien contre le point médian mais on devine que ce choix a été fait par des gens qui ne tapent pas sur un clavier d'ordinateur (c'est alt + 0183 mais sous ghostwritter ça marche pas)).

![true displacement 3](https://github.com/thomas-szczurek/images/blob/main/img21_t_displacement4.png)

Vous remarquez cependant trois choses :

- C'est très exagéré
- Les bords sont cracra
- le temps de rendu est beaucoup plus long

En changeant le paramètre `scale` du `node` displacement du shader editor, vous pouvez réduire l'exagération (on est ici dans l'artistique et plus dans le technique, donc pas de recommandation à part votre feeling). Comme notre éclairage et notre caméra ne sont pas encore configurés il est trop tôt pour s'en préoccuper.

Pour ce qui est des bords ce qui se passe c'est que pour le moment, Blender essaye de répéter votre image sur les bords. Dans le shader editor, sur le `node` de votre image, changez *Repeat* pour *Extend* pour corriger ça.

![extend](https://github.com/thomas-szczurek/images/blob/main/img22_extend.png)

C'est déjà mieux !

![render2](https://github.com/thomas-szczurek/images/blob/main/img23_render2.png)

Pour améliorer nos temps de rendu, nous avons déjà modifié le nombre de passages. Mais il est aussi possible de diminuer la taille des tiles (ce qui permet d'avoir un aperçu plus rapide du résultat et de stopper le rendu si celà ne nous convient pas)

Ca se passe ici :

![tiles_size](https://github.com/thomas-szczurek/images/blob/main/img24_tiles.png)

Et vous pouvez par exemple diminuer à 512.

Comme dans l'article original, je vous incite à explorer les matériaux. Sauvegardez votre espace de travail puis changez des valeurs au hasard pour voir ce que ça donne (mais ne sauvegardez pas !)

## La caméra

On retourne dans le 3D view port. La caméra, c'est ce machin :

![la caméra](https://github.com/thomas-szczurek/images/blob/main/img25_camera.png)

Elle determine la position de la vue lors des rendus. En appuyant sur la touche 0 du pavé numérique de votre clavier vous pouvez "voir" ce que voit la caméra (réaappuyer sur 0 pour sortir). Si l'idée saugrenue d'utiliser Blender sur un pc portable sans pavé numérique vous est venue, il faudra à chaque fois passer par le menu View -> Cameras -> active Camera pour obtenir le même effet.

On veut que notre caméra soit située juste au dessus de notre plan, et avec un angle de 0 degrés.

- On la selection (elle devient orange)
- On va dans le paneau des propriétés de l'objet.
- Et dans Transform, on passe les valeurs de location x et y = 0, et z = 3 (la valeur de z n'a pas trop d'importance a part d'être supérieure à 0, voir plus bas)
- Toujours dans transform, on passe toutes les valeurs de rotation à 0

![réglages caméra](https://github.com/thomas-szczurek/images/blob/main/img26_camera_settings.png)

Si vous passez en vue caméra vous verrez qu'on commence à avoir quelque chose qui ressemblera a une carte.

Il nous faut encore régler le ratio de la prise de vue pour le faire correspondre à celui de notre mnt/plan. Ca se fait dans les `output properties`. Dans Format (ou Dimensions dans d'anciennes versions de Blender), indiquez les dimensions en pixels de votre raster que vous aviez otenus avec gdalinfo. Ce paramètre modifie la résolution de sortie des rendus et vous verrez la caméra changer en fonction pour presque s'adapter aux dimensions de votre plan.

En dessous se trouve le symbole `%` qui adaptera la résolution indiquée par ce pourcentage lors des rendus. Celà peut être interessant lors de rendus intermédiaires pour accélerer le processus, ou si comme moi votre raster est très grand et que vous avez des petits problèmes de mémoire lors des rendus.

![réglages caméra](https://github.com/thomas-szczurek/images/blob/main/img27_camera_settings2.png)

Faisons maintenant un rendu pour voir.

![rendu3](https://github.com/thomas-szczurek/images/blob/main/img28_render3.png)

Deux conclusions s'imposent.

- Ca commence a avoir de la tronche
- Houston nous avons un problème

Je considère que nous sommes entre géomaticien/nes ou personnes interessées par le sujet. Le terme d'**ortho**photographie ne vous est pas inconnu et je n'ai pas à expliquer le concept de vue en perspective/orthographique.

Bon allez.

![diff ortho perspective](https://github.com/thomas-szczurek/images/blob/main/img29_ortho.jpg)

Mais je ne ferrai pas plus d'efforts.

Pour passer la caméra en vue orthographique, on la sélectionne, puis dans ses propriétés on change son type en "orthographic".

![ortho](https://github.com/thomas-szczurek/images/blob/main/img30_ortho2.png)

Vous verrez par contre que maintenant votre caméra prends une zone beaucoup plus grande que votre plan. Pour remedier  à ça, il faut paramétrer la valeur d'`orthographic scale` de ce même panneau. Pour trouver la bonne valeur, il faut multiplier par deux la plus grande dimension de votre plan. Ainsi, j'avais créé un plan de 0,8 x 0,7, donc dans mon cas 0,8 x 2 = 1,6. J'ai réussi ça de tête.

![rendu 3 ou 4 je sais plus](https://github.com/thomas-szczurek/images/blob/main/img31_render3.png)

C'est beaucoup mieux !

Maintenant, on peut s'interesser à l'exagération du relief. On retourne dans le shader editor, et sous le `node` `displacement`, on règle la valeur de `scale`. Vous pouvez faire des rendus pour voir ce qui vous convient le mieux. Personnellement je vais mettre cette valeur à 0,5.

## La lumière

On va maintenant régler la source de lumière qui éclaire notre sène. La source de lumière c'est ce truc :

![lumière](https://github.com/thomas-szczurek/images/blob/main/img32_light.png)

Après l'avoir selectionnée, cliquez sur l'icone en forme de bulbe d'ampoule pour accéder à ses propriétés.

![réglages lumière](https://github.com/thomas-szczurek/images/blob/main/img33_light2.png)

Plusieurs types de source sont possible (ampoule, spot...). Mais dans notre cas on veut une lumière naturelle. Choisir donc "boule de feu géante abritant en son coeur des réactions de fusion nucléaire qui se transformera en [naine blanche](https://fr.wikipedia.org/wiki/Naine_blanche) à sa mort mais pas avant d'avoir enflé jusqu'aux limites de la terre la carbonisant au passage mais qui si elle était plus massive finirai en [étoile à neutrons](https://fr.wikipedia.org/wiki/%C3%89toile_%C3%A0_neutrons) voir en [trou noir stellaire](https://fr.wikipedia.org/wiki/Trou_noir_stellaire) dont notre physique n'arrive pas à expliquer les singularités centrales sans unifier la relativité générale et la quantique et ça fait 100 ans qu'on cherche, prend ça dans ta face la science."

Ou bien juste sun (ça veut dire [soleil](https://fr.wikipedia.org/wiki/Soleil)).

Pour celles et ceux qui préfèrent la première version je vous conseille [ceci](https://www.youtube.com/watch?v=zjIC6jIQRKQ) (avec un type qui a des patchs sur les coudes de ses vestes). Il a aussi écrit [ça](https://www.dunod.com/sciences-techniques/univers-multiples-nouveaux-horizons-cosmiques) si vous voulez vous retourner la tête. Si vraiment vous êtes hardcore il y a aussi [ceci](https://www.odilejacob.fr/catalogue/sciences/astronomie-astrophysique-cosmologie/ecume-de-l-espace-temps_9782738139719.php). Promis j'arrête.

Une ampoule près de vous envera ses rayons dans toutes les directions. Dans le cas du soleil, il est sufisamment éloigné (et gros) pour que ses rayons arrivent à nous orientés tous selon le même angle (rapellez vous vos cours de pourquoi qu'il fait chaud à l'équateur et froid aux pôles). C'est ce que simulera Blender en douchant notre scène de lumière provenant d'une unique direction.

Avec ce type de lumière, la position de l'objet la générant dans la scène n'est pas importante. Si vous effectuez un rendu maintenant vous vous rendrez compte que tout est très surexposé car nous n'avons pas réglé sa force (strength). Passons ce paramètre de 1000 à ... 5.

Pour définir l'angle d'incidence des rayons lumineux il faut se rendre dans les propriétés de l'objet (attention à bien le sélectionner) et changer sa rotation (pour les sources de lumière de type soleil).

Indiquer 0 pour x, 45 pour y et 135 pour z.

![réglages lumière](https://github.com/thomas-szczurek/images/blob/main/img34_light3.png)

La valeur de y contrôle l'angle par rapport à l'horizon, et celle de z la direction de provenance. Une valeur de 135 vous donne une lumière qui arrive du Nord Ouest (en haut à gauche quoi), ce à quoi l'oeil humain est habitué pour une carte. Mettre 225 donnerai l'impression que notre relief est inversé.

Le tout dernier réglage à faire est de régler la taille de notre soleil. On reclique sur la petite ampoule verte et on regarde le paramètre Angle, mal nommé puisqu'il correspond au [diamètre angulaire](https://fr.wikipedia.org/wiki/Taille_apparente). Changer sa valeur régle la *douceur* de la lumière. Avec une valeur basse par défault, notre lumière nous donne un relief lunaire, essayez plutôt une valeur de 90 pour quelque chose de plus doux.

![réglages lumière](https://github.com/thomas-szczurek/images/blob/main//img35_light4.png)

Un petit rendu pour la route ?

![rendu 5](https://github.com/thomas-szczurek/images/blob/main/img36_render6.png)

Waoohh !!!

## Coloriser

Pour ça, je vais vous laissez vous reposer et ne pas ressortir gdal, mais réouvrir un logiciel obscur nommé Qgis dans lequel on va charger notre raster d'élévation. L'idée va être de générer une image colorée qu'on appliquera ensuite dans Blender comme texture.

Si vous avez de l'eau :

On ouvre la calculatrice raster (raster -> calculatrice) et on tape juste cette formule `mnt@1 <= 0`. On enregistre sur le disque le résultat plutôt que de faire un raster virtuel car l'algorithme suivant veut un fichier (par exemple eau.tif). (le chiffre derriere le @ désigne le numéro de bande de l'image à utiliser).

Celà nous permet de générer un raster comprenant des 0 et des 1 en fonction de la hauteur par rapport au niveau de la mer. Comme notre raster d'origine est très précis, on va le tamiser pour retirer les pixels isolés et rendre le résultat plus propre ( [gdal_sieve.py](https://gdal.org/programs/gdal_sieve.html) ). Ce se passe avec raster -> Analyse -> Tamiser.

- On sélectionne notre raster eau.
- l'option `seuil` détermine la taille limite des polygones qui devront êtres fusionnés avec leur voisin le plus proche
- `use 8-connectedness` permet de spécifier si on veut que les pixels en diagonale soient considérés ou non pour déterminer l'isolation d'un pixel.

Personnellement je choisi un seuil de 75 et je n'utilise pas 8-connectedness ici pour vraiment nettoyer.

Enfin, on va polygoniser le résultat pour transformer ça en couche vecteur : raster -> conversion -> Polygoniser.
Cet algorithme ne permet pas de créer une couche vectorielle en mémoire, donc veillez à bien indiquer un fichier de sortie soit au format [Geopackage](https://www.geopackage.org/) (une base sqlite normée par l'[OGC](https://www.ogc.org/)), soit [FlatGeoBuf](http://flatgeobuf.org/) (format moderne optimisé cloud avec un fichier = une couche conçu pour la simplicité d'usage). Pas en [geojson](https://blog.ianturton.com/gis/2023/11/11/geojson.html) s'il vous plait.

On fait un clic droit sur notre vecteur d'eau, et on choisi filtrer avec la formule suivante "DN"=1. DN est le champ où la valeur du raster a été conservée. Vous pouvez maintenant donner une couleur bleu à votre eau (voilà, vous pouvez être prof de sémiologie).

Pour le reste :

- On selectionne notre raster de mnt, et dans son style on change bande grise unique pour Pseudo-couleur à bande unique.
- Dans palette de couleur, on choisi "créer une nouvelle palette" puis "catalogue cpt-city"

![catalogue cpt city](https://github.com/thomas-szczurek/images/blob/main/img37_cptcity.png)

- Descendre dans la section "Topography" et par exemple choisir "DEM_screen"
- Une fois validé cliquez sur "classer"
- Pour bien il faudrai rectifier la palette en fonction de vos hauteurs maximum mais comme je commence à vraiment aimer pouvoir finir (autre manière de dire : j'ai la grosse flemme), j'aurai des hauteurs de 198 mètres qui paraitrons couvertes de neiges eternelles.

![menteur](https://github.com/thomas-szczurek/images/blob/main/img38_menteur.png)

Maintenant, essayez de zoomer sur la carte  pour l'avoir la plus grande possible, mais complète sur votre écran. Puis choisir dans le menu Projet -> Importer/Exporter -> Exporter la carte au format image (ça permet d'exporter le contenu de votre canevas de carte sans passer par le composeur). Changez la résolution en 300 dpi et exporter au format png.

Maintenant ouvrez cette image dans [The Gimp](https://www.gimp.org/), un éditeur d'image libre et open source. La seule et unique manipulation est de passer par le menu image -> rogner selon le contenu. Celà supprimera tout le blanc qui restait visible et d'obtenir une image avec le même ratio que notre mnt. Puis fichier -> écraser couleur.png (le nom de mon image).

On revient maintenant dans le `shader editor` de Blender. Comme pour ajouter notre mnt, on passe par le menu Add -> Texture -> Image texture. On selectionne notre image de couleur, on oublie pas de passer l'interpolation en smart et l'extension en extend, mais on laisse le color space en sRGB. Puis on relie `color` à `Base color` de principled BSDF.

![coloriser](https://github.com/thomas-szczurek/images/blob/main/img39_coloriser.png)

Et on effectue le rendu final !!!

![render final](https://github.com/thomas-szczurek/images/blob/main/img40_renderfinal.png)

On pourrait bien sur jouer un peu plus avec les réglages (je trouve par exemple mes ombres encore un peu trop profondes et pourrai passer du temps sur le paramètre angle de ma lumière soleil), ou les couleurs (je trouve ce vert bouteille assez moche), ou encore sur le tamisage de notre couche d'eau,  mais vous avez maintenant la base de la technique !

Voici par exemple ce que ça donne lors d'un essai precédent où j'ai passé un peu plus de temps à tout régler

![render final](https://github.com/thomas-szczurek/images/blob/main/img41_pyrennees_render.png)

--8<-- "content/team/thomas-szczurek-gayant.md"
