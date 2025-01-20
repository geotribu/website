---
title: Contribution Mapillary et retour d'expérience
authors:
    - Florian Boret
categories:
    - article
    - tutoriel
comments: true
date: 2022-12-09
description: Contribution Mapillary et retour d'expérience
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/mapillary_logo.jpeg
license: default
tags:
    - Bash
    - data
    - Mapillary
    - OGR
    - SQL
---

# Contribution Mapillary et retour d'expérience

:calendar: Date de publication initiale : 09 décembre 2022

## Prérequis

### Matériel

- GoPro Max
- Support ventouse

### Application

- l'interpréteur [Bourne-Again shell](https://fr.wikipedia.org/wiki/Bourne-Again_shell)
- l'outil de conversion [ogr2ogr](https://gdal.org/programs/ogr2ogr.html)
- Python >= 3.6
- [exiftool](https://exiftool.org)
- [Imagemagick](https://imagemagick.org/index.php)
- [ffmpeg / ffprobe](https://ffmpeg.org)

## Intro

![Mapillary](https://cdn.geotribu.fr/img/logos-icones/divers/mapillary.png "Mapillary"){: .img-thumbnail-left }

Cet article s'inscrit dans la continuité de l'article que j'avais intitulé [accéder aux données Mapillary et les intégrer dans son SIG](2022-05-31_donnees_mapillary.md). En effet, au moment où celui-ci avait été rédigé, je n'étais pas encore équipé pour réaliser des vues immersives. C'est maintenant chose faite et je vous propose un retour d'expérience qui je l'espère permettra d'alimenter discussions et réflexions sur le sujet.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Le matériel

### Le point de départ

![logo GoPro](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/GoPro.jpg "logo GoPro"){: .img-thumbnail-left }

J'interviens dans une petite Communauté de Communes et comme chacun le sait nos finances sont particulièrement contraintes. L'idée n'était donc pas de réinventer la poudre mais de s'appuyer sur des solutions éprouvées et mises en place dans différentes structures comme la [CA du Grand Montauban](https://prezi.com/p/ufcelyteyqzc/n-street-view-libre_retour_experience_grandmontauban_aitf/) ou l'Agglomération Val Parisis. Je suis donc parti sur :

- une GoPro Max 360° livrée avec une batterie et une carte mémoire carte SD de 64 Go : environ 430 €
- un support triple ventouse Ram Mount (ref. RAP-B-365-224-202AU) : environ 90€
- un adpatateur GoPro à visser : environ 3€

![Configuration initiale](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/config_initiale.jpeg "Configuration initiale"){: .img-center loading=lazy }

### Une erreur qui aurait pu me coûter une GoPro

J'avais acheté un adapteur GoPro en plastique à 3€ pour limiter les coûts mais cette "chinoiserie" a bien failli me coûter la caméra !

En effet, le lendemain de ma première matinée de test, la caméra était posée sur le bureau quand sans action extérieure, elle s'est retrouvée sans prévenir sur le sol, gloups ! L'adapteur en plastique avait complètement explosé.

![Configuration cassée](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/config_break.jpeg "Configuration cassée"){: .img-center loading=lazy }

Un défaut de fabrication, la pièce trop serrée,... je ne sais pas mais toujours est-il que ça m'a bien refroidi !

Après avoir partagé ma mésaventure sur Twitter, [Stéphane Péneau](https://twitter.com/stfmani) de [Carto'Cité](https://cartocite.fr) me conseille d'acheter un adaptateur Ram Mount (ref. RAP-B-202U-GOP1), certes plus cher mais aussi d'une tout autre qualité et 100% compatible avec le support triple ventouse du même fabriquant.

![Configuration finale](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/config_finale.jpeg "Configuration finale"){: .img-center loading=lazy }

### Sécuriser le système

Et pour sécuriser encore un peu plus un éventuel décrochement, j'ai ajouté deux éléments "basiques" pour assurer la caméra et me rassurer :

1. une ficelle et un mousqueton que j'ai fixés au support triple ventouse et que je viens attacher à l'intérieur de l'habitacle (poignée ou pare soleil suivant les véhicules).
2. un bas de ligne acier (normalement utilisé pour la pêche au carnassier) pour relier cette ficelle à la GoPro pour ne pas la perdre en cas de détachement éventuel ou de rupture de l'adaptateur.

### L'autonomie

Avec une batterie neuve, on arrive à faire une demi-journée de prises de vue. Si on veut aller plus loin, il faut faire l'acquisition de plusieurs batteries et d'un chargeur multiple.

----

## Prises de vue

### Configuration

La caméra installée et démarrée, j'utilise l'application [GoPro Quik](https://gopro.com/fr/fr/shop/quik-app-video-photo-editor) et la connexion bluetooth pour lancer ou stopper les prises de vue tout en étant dans la voiture.

![GoPro Quik](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/app_gopro.png "GoPro Quik"){: .img-center loading=lazy }

A noter que pour bénéficier de [l'aperçu en direct et la visualisation des médias, vous devrez basculer sur une connexion Wi-Fi entre la caméra et votre mobile](https://community.gopro.com/s/article/What-is-Bluetooth-Connectivity-How-Does-it-Differ-From-Wi-Fi?language=fr).

!!! Info
    La connexion bluetooth consomme moins d'énergie que la connexion Wi-Fi.

### L'intervalle

La GoPro est paramétrée pour prendre des prises de vue 360° avec un intervalle de deux secondes (intervalle minimum avec cette caméra) ce qui représente pour vous donner un ordre d'idée, une distance de :

- 17 mètres à 30km/h
- 28 mètres à 50km/h

Dans les secteurs urbains assez denses, il est nécessaire de limiter sa vitesse pour obtenir une bonne densité d'images.

### Une équipe de photographes

Les prises de vue sont réalisées par :

- notre équipe de gardes champêtres/ASVP qui sont en permanence sur le terrain et que j'oriente pour capter certaines "zones blanches",
- moi-même lors de mes déplacements sur le territoire (réunions, formations, collectes,...).

### Quelques chiffres

La caméra a été réceptionnée début août et après la phase de test, nous avons réalisé des prises de vue de manière aléatoire en terme de durée et ce jusqu'à fin septembre. A ce jour, nous avons publié un peu plus de 14000 images et parcouru près de 160km.

Ce qui représente autour de 40Go en terme de stockage des fichiers bruts.

[Voir nos prises de vue :fontawesome-solid-image:](https://www.mapillary.com/app/?lat=43.72760029668447&lng=4.096942011775923&z=11.016156934274354&username%5B%5D=data_wax){: .md-button }
{: align=middle }

### Conditions

A partir du mois d'octobre, le soleil étant plus bas et la luminosité plus faible, les images sont "moins nettes" et le soleil peut plus facilement éblouir le capteur. Nous avons donc décidé de stopper la campagne de prises de vue jusqu'au printemps privilégiant la qualité des prises de vue à la quantité.

----

## Traitement des photos

### Processus global

Le processus que je vous présente mélange du bash, de l'OGR, du SQL et du python.

```mermaid
flowchart TD;
    A[Photo 360]
    A --> |exiftool|R{Extraction de la<br>localisation des img}
    R --> |ogr/sql|B{Suppression des<br>images inutiles}
    B --> |nadir-patcher.py| C{Ajout du logo}
    C --> E(Mapillary Desktop)
    E --> |Publication| F(Mapillary)
```

### Un environnement de travail : config.env

Avant de se lancer, il est bon de paramétrer le fichier de configuration que vous devrez adapter à votre organisation et qui sera utilisé pour traiter les photos. On y définit le répertoire de travail et différentes variables nécessaires à la bonne éxécution du script.

Voici le fichier `config.env` à adapter :

```ini title="Environnement de travail" linenums="1"
# REPERTOIRE DE TRAVAIL
REPER='/mapillary_traitement_images'

# REPERTOIRE DE STOCKAGE DES LOGS
REPER_LOGS='logs'

# PARAMETRES OGR
ENCODAGE='UTF-8'
```

[Consulter le fichier de configuration :fontawesome-regular-file-code:](https://github.com/igeofr/gopromax2mapillary/blob/main/config.env){: .md-button }
{: align=middle }

### Nettoyer les photos "inutiles"

Après mes premiers tests, lorsque je chargeais mes photos dans l'application [Mapillary Desktop Uploader](https://www.mapillary.com/desktop-uploader), je me rendais compte que j'avais une redondance de photos "identiques" lorsque je marquais un point d'arrêt, notamment aux Stop. Cette redondance est peu pertinente pour l'utilisateur et d'un point de vue environnemental, elle vient inutilement charger les serveurs de Mapillary. Je vous explique ci-dessous quelle solution a été mise en place pour réaliser ce "nettoyage".

[Accéder au script complet  :fontawesome-regular-file-code:](https://github.com/igeofr/gopromax2mapillary/blob/main/gopromax2mapillary.sh){: .md-button }
{: align=middle }

!!! Info
    Si vous utilisez `mapillary_tools`, il existe la commande `--duplicate_distance DUPLICATE_DISTANCE`qui vous permet de faire sensiblement la même chose mais l'idée était bien d'être indépendant pour ne pas s'enfermer dans la solution Mapillary si le projet [Panoramax](https://forum.geocommuns.fr/c/panoramax/6) aboutit. A noter, cette option n'est pas présente dans Mapillary Desktop Uploader.
    `--duplicate_distance DUPLICATE_DISTANCE : The maximum distance that can be considered "too close" between two images. If both images also point in the same direction (see --duplicate_angle), the later image will be marked as duplicate and will not be upload. [default: 0.1]`

#### Extraire la localisation des images

Pour la première étape, j'ai utilisé `exiftool` pour lire chacune des images afin d'en extraire leur localisation ainsi que la date et l'heure de la prise de vue. En sortie, j'obtiens un fichier `csv` listant chacune des images ainsi que les paramètres demandés (latitude, longitude, date, nom du fichier, ...).

```bash title="Extraction de la localisation des images" linenums="1"
exiftool -filename -gpstimestamp -gpsdatestamp -gpslatitude -gpslongitude -n -csv -r $REPER'/tmp' > './list/'$DATE_YMD'_img.csv'
```

#### Créer un fichier SIG à partir de la localisation des images

La deuxième étape est une étape intermédiaire qui permet de créer un fichier SIG à partir des informations extraites précédemment des images. En entrée, on a donc le fichier `csv` que l'on va transformer en une couche ponctuelle localisant les images et intégrant les informations extraites.

```bash title="Création du fichier au format SIG" linenums="1"
ogr2ogr \
  -f "SQLite" \ # FORMAT DE SORTIE
  -dsco SPATIALITE=YES \
  -lco LAUNDER=NO \
  -oo X_POSSIBLE_NAMES=gpslongitude \ # ON DEFINIT LE CHAMP X
  -oo Y_POSSIBLE_NAMES=gpslatitude \ # ON DEFINIT LE CHAMP Y
  ${csvfile%.*}.sqlite \ # NOM DU FICHIER EN SORTIE
  ${csvfile%.*}.csv # NOM DU FICHIER EN ENTREE
```

#### Identification des images

Vous connaissez mon côté OGR centré ! Au départ, j'ai commencé par digérer la localisation des images dans OGR pour supprimer les points des photos dont la distance avec le suivant était inférieure à 2 mètres. C'était un bon début mais perfectible.

![Identification des images à supprimer - version 1](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/nettoyage_v1.png "Identification des images à supprimer - version 1"){: .img-center loading=lazy }

Finalement après de nombreux échanges avec [Michaël Galien](https://twitter.com/tetranos), plutôt SQL centré, on est arrivé à une requête récursive sur PostgreSQL permettant de supprimer les photos qui se succèdent si leur écartement est inférieur à X mètres (dans le cas présent 3 mètres). Si on compare visuellement ces deux versions, cette solution permet de conserver une meilleure répartition des photos. C'est notamment lié à la récursivité qui permet d'avancer sur le point qui suit de manière progressive.

![Identification des images à supprimer - version 2](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/nettoyage_v2.png "Identification des images à supprimer - version 2"){: .img-center loading=lazy }

Cette requête a ensuite été adaptée pour tourner avec ogr2ogr de manière autonome (OGR centré, je vous dis !).

```bash title="Identification des images" linenums="1"
ogr2ogr \
-f CSV \ # FORMAT DE SORTIE
-dialect sqlite \
-sql 'WITH RECURSIVE clean_sequence as (
  --PERMET DE RECUPERER LA PREMIERE PHOTO
  SELECT g.*,
  cast(null as geometry) as aproximite,
  cast(null as integer) as id_ref,
  cast(null as real) AS distance
  FROM (SELECT * FROM conf LIMIT 1) g
  UNION ALL
  --REGARDE SI LE POINT SUIVANT SE TROUVE A UNE DISTANCE XX
  SELECT T.*,
    CASE
    WHEN C.aproximite IS NULL AND PtDistWithin(T.geom, C.geom,3) THEN T.geom_prev
    WHEN not (C.aproximite IS NULL) AND PtDistWithin(T.geom, C.aproximite,3) THEN C.aproximite
    ELSE NULL
    END as aproximite,
    CASE
    WHEN C.aproximite IS NULL AND PtDistWithin(T.geom, C.geom,3) THEN t.prev_val
    WHEN not (C.aproximite IS NULL) AND PtDistWithin(T.geom, C.aproximite,3) THEN C.id_ref
    ELSE NULL
    END as id_ref,
    CASE
    WHEN C.aproximite IS NULL AND PtDistWithin(T.geom, C.geom,3) THEN ST_Distance(T.geom, C.geom)
    WHEN not (C.aproximite IS NULL) AND PtDistWithin(T.geom, C.aproximite,3) THEN ST_Distance(T.geom, C.aproximite)
    ELSE NULL
    END as distance
    FROM clean_sequence as C
    INNER JOIN (SELECT * FROM conf) as T
    ON T.id_photo = C.id_photo + 1),
  conf AS (SELECT
    sourcefile,
    filename,
    substr(filename,1,4) as sequence,
    cast(substr(filename,5,4) AS integer) as id_photo,
    CAST(gpslatitude AS REAL) AS gpslatitude,
    CAST(gpslongitude AS REAL) AS gpslongitude,
    ST_Transform(SetSRID(MakePoint(CAST(gpslongitude AS REAL), CAST(gpslatitude AS REAL)), 4326),2154)as geom,
    LEAD(ST_Transform(SetSRID(MakePoint(CAST(gpslongitude AS REAL), CAST(gpslatitude AS REAL)), 4326),2154)) over (order by filename) AS geom_next, --GEOMETRY DU POINT SUIVANT
    LAG(ST_Transform(SetSRID(MakePoint(CAST(gpslongitude AS REAL), CAST(gpslatitude AS REAL)), 4326),2154)) over (order by filename) AS geom_prev, --GEOMETRY DU POINT PRECEDENT
    LAG(cast(substr(filename,5,4) AS integer)) OVER (ORDER BY cast(substr(filename,5,4) AS integer)) AS prev_val, --NUMERO DU POINT PRECEDENT
    LEAD(cast(substr(filename,5,4) AS integer)) OVER (ORDER BY cast(substr(filename,5,4) AS integer)) AS next_val --NUMERO DU POINT SUIVANT
  FROM "'${csvfile%.*}'" ORDER BY filename)
  SELECT sourcefile
   FROM clean_sequence WHERE NOT (aproximite IS NULL)
  ' \
  ${csvfile%.*}"_a_sup.csv" \ # NOM DU FICHIER EN SORTIE
  ${csvfile%.*}".sqlite" # NOM DU FICHIER EN ENTREE
```

#### Suppression des images

Une fois la liste des images à supprimer identifiée, il ne nous reste plus qu'à les effacer.

```bash title="Suppression des images" linenums="1"
# SUPPRESSION DES IMAGES INUTILES
for csvfile_sup in *.csv; # BOUCLE SUR LES FICHIERS CSV
do
    sed 1d ${csvfile_sup} | xargs rm -f | bash # SUPPRESSION DES IMAGES
    rm ${csvfile_sup} # SUPPRESSION DU FICHIER CSV A LA FIN
done
```

#### Autre piste à explorer

En parallèle des échanges avec M. Galien, [Vincent de Château-Thierry](https://twitter.com/_vdct) nous proposait une solution alternative ne s'appuyant pas sur le recursif et qu'il serait intéressant de creuser :point_down:.

<blockquote class="twitter-tweet tw-align-center" data-conversation="none" data-lang="fr"><p lang="fr" dir="ltr">Une proposition qui oublie le récursif : - composer des lignes avec les points ordonnées via ST_MakeLine(geometrie ORDER BY timestamp) - les simplifier avec ST_RemoveRepeatedPoints en jouant sur la tolérance. En blanc les points supprimés, les rouges restent. A affiner bien sûr <a href="https://t.co/EN8xML4XEt">pic.twitter.com/EN8xML4XEt</a></p>&mdash; user:vincent_95 (@_vdct) <a href="https://twitter.com/_vdct/status/1555122774380879873?ref_src=twsrc%5Etfw">4 août 2022</a></blockquote>

### Intégration du logo

Pour la partie intégration du logo, je suis reparti d'une solution proposée par Cécile Mahé et Christophe Munoz du SIG de l'[Agglomération Val Parisis](https://portailsig.valparisis.fr) et partagée au sein du groupe de l'[AITF SIG et topographie](https://www.aitf.fr/groupe-travail/sig-topographie). Cette solution repose sur le projet et le script python `Nadir Patcher` de [David G](https://github.com/himynamesdave) de [Trek View](https://www.trekview.org).

[Accéder au projet Nadir Patcher :fontawesome-regular-file-code:](https://github.com/trek-view/nadir-patcher){: .md-button }
{: align=middle }

```bash title="Intégration du logo" linenums="1"
# Exemple : permet d'intéger un logo couvrant 17% de l'image panoramique
python3 nadir-patcher.py $REPER'/tmp' $REPER'/logo.png' 17 $REPER'/out'
```

![Intégration du logo](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/mapillary_logo.jpeg "Intégration du logo"){: .img-center loading=lazy }

----

## Publication des photos

Pour la publication des photos, je ne passe pas par `Mapillary Tools`. Je préfère utiliser l'[application bureautique](https://www.mapillary.com/desktop-uploader) car cela me permet de contrôler mon cheminement et éventuellement de supprimer certaines images manuellement avant publication.

----

## Usages

Le territoire n'étant pas intégralement couvert, il n'y a pas encore eu de campagne de promotion en interne. Toutefois, l'usage de la GoPro a éveillé la curiosité de certains collègues ayant l'habitude d'utiliser StreetView et à qui j'ai déjà présenté la démarche :

- le service qui instruit les demandes d'urbanisme pour localiser et visualiser les projets,
- le service déchet pour s'immerger sur site lors d'appels d'usagers,
- les services techniques pour travailler sur des projets d'aménagement.

A terme, l'objectif est de présenter ce projet à l'ensemble des services de l'intercommunalité ainsi qu'aux agents des communes.

Concrètement dans notre WebSIG, l'utilisateur peut visualiser les voies couvertes et à l'aide d'un outil métier, il peut interroger la localisation d'une photo pour ensuite la visualiser dans Mapillary.

!!! Rappel
    Comme expliqué dans l'[article précédent](2022-05-31_donnees_mapillary.md), les données relatives à la couvertures et aux images sont récupérées depuis Mapillary et régulièrement intégrées dans notre base de données.

![Intégration WebSIG](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/integration_websig.png "Intégration WebSIG"){: .img-center loading=lazy }

En dehors de Mapillary, j'ai aussi travaillé avec mon service culture pour photographier une exposition de Street Art dans le but de prolonger l'évènement sous la forme d'une visite immersive en m'appuyant sur l'outil [Pannellum](https://pannellum.org). On sort clairement du cadre initial mais cela ouvre d'autres perspectives.

![Exposition immersive](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2022/2022-11-11-mapillary_experience/exposition.png "Exposition immersive"){: .img-center loading=lazy }

----

## Conclusion

Cet article vous illustre mon retour d'expérience matériel concernant la prise de vues immersives et vous détaille l'enchainement des étapes que je réalise entre la prise de vue et la publication sur Mapillary avec pour objectif d'automatiser au maximum de traitements tout en gardant une forme d'indépendance si nous devions changer de solution à l'avenir (ex. [le Géocommun Panoramax](https://forum.geocommuns.fr/c/panoramax/6)). A noter, que j'ai récemment retravaillé sur une nouvelle version de mon script pour intègrer deux possibilités :

- supprimer les images lorsque je suis passé récemment sur une voie,
- créer des dossiers separés pour chacune des séquences d'images me permettant ainsi de choisir les séquences à publier pour améliorer le maillage sans introduire de redondance d'images.

----

<!-- geotribu:authors-block -->

{% include "licenses/default.md" %}
