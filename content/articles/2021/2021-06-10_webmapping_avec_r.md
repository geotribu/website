---
title: "De petites applications webmapping avec R"
authors: ["Romain LACROIX"]
categories: ["article", "tutoriel"]
date: "2021-04-XX 10:20"
description: "Description pour le SEO."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/exempletitre.png"
tags: "template,mot-clé-seo1,mot-clé-seo2"
---

# De petites applications webmapping avec R

:calendar: Date de publication initiale : XX juin 2021

**Mots-clés :** Carte interactive | webmapping | R | Leaflet | dashboard | Mapbox

## Prérequis

* une machine avec R 4.0 et RStudio
* quelques connaissances sur la programmation R
* éventuellement un compte Mapbox

## Introduction

Autant l'avouer d'emblée, je suis quand même un petit peu un traumatisé du point-virgule ; inversement je suis un grand amoureux d'R : mon jugement est donc biaisé, mais je l'assume totalement. :smirk:

Si le développement classique de cartes interactives en JavaScript est devenu prépondérant grâce à une très grande flexibilité d'usages et de paramétrages, il existe certains cas particuliers où d'autres approches peuvent être mobilisées.

Par exemple, mettons qu'on ait besoin de communiquer cartographiquement et de la même façon des données privées et personnalisées à 10, 100 ou 1000 destinataires, sans volonté ou possibilité d'infrastructure informatique susceptible d'accueillir une telle application cartographique ou n'ayant tout simplement pas les compétences pour en développer une (ou les finances pour s'en payer). Cela peut à première vue paraître des conditions initiales pour le moins incongrues lorsque l'on parle de géomatique (car trouvant majoritairement son débouché dans des organisations publiques), mais si l'on regarde tout le spectre possible des organisations susceptibles de pouvoir recourir à des applications carto, je pense que des situations telles que je présente ici existent beaucoup plus fréquemment que l'on imagine au premier abord.

Je propose donc ici un petit tutoriel afin de réaliser des cartes interactives personnalisées simplement à l'aide de R et quelques packages.
L'exemple est de simuler ici la création de cartes personnalisées pour des agriculteurs, chacun possédant quelques parcelles différentes, afin qu'ils puissent repérer différentes informations sur leur environnement.

Vous êtes prêts ? Allez, pour bien comprendre, suivez bien les pas :trumpet:

![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/GrizzledCircularArmedcrab-size_restricted.gif)


----

## Démarrage, packages et données


### Packages R




Les packages utilisés sont les suivants :

```r
library(tidyverse)
library(geojsonsf)
library(crosstalk)
library(rnaturalearth)
library(rgdal)
library(geosphere)
library(RColorBrewer)
library(DT)
library(sf)
library(flexdashboard)
```


**Une version particulière de leaflet pour une utilisation des polygones avec crosstalk doit être installée :**

```r
devtools::install_github("dmurdoch/leaflet@crosstalk4")

library(leaflet)
```

### Données

On va générer un jeu de données aléatoire basé sur les données du cadastre Etalab pour les parcelles. Seront également utilisées quelques autres pour de l'information géographique que l'on veut superposer.

La commune choisie est par exemple ici celle de Quincié-en-Beaujolais (INSEE : 69192), on inventera une dizaine d'agriculteurs fictifs possédant des parcelles tout aussi fictives sur lesquelles ils voudront avoir l'information des délimitations des AOC viticoles, ainsi que celle de la carte géologique ou des ZNIEFF.

#### Organisation

Notre projet consistera basiquement en 2 fichiers :
* un fichier "script" .R : pour la création des données et la génération automatisée des cartes pour chaque agriculteur
* un fichier "sortie" .Rmd : pour la sortie .html de la carte avec ses différents composants

#### Téléchargement du cadastre de la commune

```r
library(geojsonsf)
library(tidyverse)
library(sf)

# définition du n°dpt
dpt <- "69"

# définition du n°insee communal
insee <- "69162"
url <- "https://cadastre.data.gouv.fr/data/etalab-cadastre/latest/geojson/communes/"

parcelles <- st_as_sf(geojson_sf(gzcon(url(paste0(
  url, dpt, "/", insee,
  "/cadastre-", insee, "-parcelles.json.gz"
)))))

# pour avoir un rendu pas trop moche et des parcelles qui, quand on
# les sélectionne au hasard, ressemblent à des parcelles agricoles,
# on récupère aussi les bâtiments

batiments <- st_as_sf(geojson_sf(gzcon(url(paste0(
  url,  dpt, "/", insee,
  "/cadastre-", insee, "-batiments.json.gz"
)))))
```
Il faut maintenant passer des données brutes cadastrales à des données d'exemple intéressantes à travailler :yum:

#### Création des parcelles

```r
# pour filtrer les parcelles "avec bâtiments"

parcelles_bati <- parcelles %>%
  st_intersection(., batiments)

parcelles_viti <- parcelles %>%
  filter(!(id %in% parcelles_bati$id)) %>%  # filtre des parcelles sans bâtiments
  slice_sample(n = 100) %>% # échantillonnage de 100 parcelles
  mutate(Exploitation = rep(c(
    "Exploitation A", "Exploitation B",
    "Exploitation C", "Exploitation D",
    "Exploitation E", "Exploitation F",
    "Exploitation G", "Exploitation H",
    "Exploitation I", "Exploitation J"
  ), times = 10))%>%
  mutate(FaireValoir = sample(c("Propriétaire", "Fermier","Métayer","Commodat"),
                              100, prob = c(0.6,0.3,0.08,0.02), replace = T))%>%
  mutate(Cépage = sample(c("Gamay N","Aligoté B","Chardonnay B"),100,
                         prob = c(0.8,0.1,0.1), replace = T))

ggplot() +
  geom_sf(data = parcelles, fill = NA) +
  geom_sf(data = batiments, fill = "red", color = "red") +
  geom_sf(data = parcelles_viti, aes(fill = Exploitation, color = Exploitation)) +
  theme_minimal()

```
![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/parcelles_viti_test.png)

Sur notre jeu de données, on a ajouté des attributs spécifiques à titre d'exemple (Faire-Valoir, Cépage) histoire d'avoir des possibilités de filtres "intelligents" sur la carte finale.



## La carte

Bon, les données sont disponibles, mais concrètement, maintenant, comment on passe de cette carte statique à la carte interactive, personnalisée et partageable promise ?

Avec les documents Rmarkdown, on peut faire interagir notre jeu de données dans un document exportable, qui peut être du Word, PowerPoint, PDF ou html. C'est ici la sortie .html qui nous intéresse, car c'est elle qui va nous permettre la génération d'une carte interactive.

Un certain nombre de packages R permettent des rendus déjà préconfigurés : pour cet exemple, on utilise le package 'flexdashboard' qui permet d'avoir une sortie déjà pré-agencée avec différents modules.

L'intérêt est aussi d'avoir ces différents modules qui communiquent entre eux : un filtre doit par exemple interagir sur ce qui est affiché sur la carte, mais également sur le tableau de données.


### Organisation de la page

Pour créer un nouveau document .Rmd basé sur flexdashboard, il faut aller dans File > New File > R Markdown et sélectionner flexdashboard dans l'onglet 'From Template'

![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/tmprmd.png)

*(parce qu'il serait trop long de décrire ici toutes les fonctionnalités d'agencement graphique, je vous renvoie à l'adresse suivante pour en savoir plus : https://pkgs.rstudio.com/flexdashboard/articles/using.html)*

On va utiliser pour cet exemple un agencement par ligne, avec le thème 'lumen', que je trouve intéressant et qui se combine bien avec les tuiles Positron de CartoDB.


Ainsi :

```
---
title: "Cartographie | `r nom_exploitation`"
output:
  flexdashboard::flex_dashboard:
    orientation: rows
    theme: lumen
---
```

On va ensuite organiser la page comme cela :
* un onglet principal avec
    * un bloc header sur la première ligne pour changer d'onglet(généré automatiquement)
    * un bloc "carte" à droite
    * un bloc filtre à gauche
    * un bloc avec le tableau des données sous la carte
* un deuxième onglet qui peut accueillir les informations annexes, manuel d'utilisation, sources des données, contact, etc.

Cela correspond à la syntaxe suivante :
```markdown
---
title: "Cartographie | `r nom_operateur`"
output:
  flexdashboard::flex_dashboard:
    orientation: rows
    theme: lumen
---



Carte {data-icon="fa-map"}
=====================================  

Inputs {.sidebar}
-----------------------------------------------------------------------


Row {data-height=700}
-------------------------------------


Row {data-height=300}
-------------------------------------




Information {data-orientation=rows data-icon="fa-info-circle"}
=====================================

### Comment utiliser cet outil ?


### À propos


#### Contact
```

Ce qui donne la sortie suivante (après compilation en appuyant sur le bouton Knit qui vous demande également de sauvegarder votre fichier, ici on l'a appelé "exemple.Rmd")

![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/carte_blank.png)
![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/carte_blank2.png)

Maintenant il s'agit de remplir les différentes parties avec nos données !
### La carte

Il faut tout d'abord injecter nos données dans le Rmd. Le problème à résoudre, c'est d'avoir nos données spécifiques à chaque exploitation dans la carte : les données doivent donc être filtrées en amont de la création de la carte.

#### Filtre des données et génération automatisée

On retourne donc dans notre fichier script et on procède à l'écriture de la boucle permettant d'obtenir
* les données filtrées pour chaque exploitation
* tant qu'à faire, le nom de l'exploitation pour l'afficher en titre de la carte
* la sortie .html de la carte pour cette exploitation

```r
liste_exploitation <- unique(parcelles_viti$Exploitation) # liste des exploitations

for (x in 1:10){
  parcelles_exploitation <- parcelles_viti %>%
    filter(Exploitation %in% liste_exploitation[[x]]) # filtre perso

  nom_exploitation <- liste_exploitation[[x]] # nom de l'exploitation
  rmarkdown::render("exemple.Rmd",
  output_file = paste0(nom_exploitation,".html"), quiet = T) # rendu par exploitation

  cat("carte ",x,"/10\n")
}
```
Et sur notre répertoire de travail apparaissent : :smiley:
![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/files_auto.png)

Bon, c'est bien, par contre les cartes sont toutes vides. Il faut maintenant s'atteler à remplir le document Rmd en utilisant les données personnalisées : "parcelles_exploitation" et "nom_exploitation"

#### Configuration des données personnalisées

Il faut commencer par remplir le premier 'chunk' R avec les packages que l'on souhaite utiliser et les données personnalisées pour l'utilisation dans le reste des modules.

(pour les délimitations de chunk, il faut enlever les # avant les "```")

```markdown
```{r setup, include=FALSE}
library(flexdashboard)
library(tidyverse)
library(crosstalk)
library(leaflet) # attention il faut bien avoir la bonne version !
library(DT)
library(sf)

# on enleve les données qui nous servent à rien dans le tableau

data <- parcelles_exploitation %>%
  select(-c("prefixe","created","updated","arpente"))%>%
  as_Spatial()

# on met nos données dans un environnement crosstalk permettant
# la connexion entre les différents modules

sd <- SharedData$new(data)
sd_df <- SharedData$new(data@data, group = sd$groupName())

```

 Maintenant, chaque carte intégrera des données spécifiques.

 On peut également en profiter et modifier le titre de la carte afin qu'il affiche le nom de l'exploitation :

```markdown
---
title: "Cartographie | `r nom_exploitation`"
output:
  flexdashboard::flex_dashboard:
    orientation: rows
    theme: lumen
---
```
 ![](https://geotripad.herokuapp.com/uploads/upload_fa13dadb00c71723051059d7f805c2ef.png)

#### À la carte !

Afficher la carte correspond dans notre layout à remplir un chunk R en-dessous de :

```markdown
Row {data-height=700}
-------------------------------------
###
```
*(Il faut bien rajouter les 3 # avant de mettre le chunk sinon des bugs peuvent se produire)*

On va créer une carte leaflet avec :
* nos parcelles
* 3 fonds de carte : couche Positron (CartoDB), couche Satellite (Google) et couche Cadastre (IGN)
* un module de mesures de surfaces et de distance
* une échelle
* un sélecteur de couches

Afin d'ajouter de l'interactivité, on crée un objet contenant le texte à afficher quand on clique sur une parcelle.

```markdown
Row {data-height=700}
-------------------------------------
###
```{r}
# définition du texte quand on clique sur la parcelle
click <- paste0(
  sd_df$data()$id, "<br/>",
  sd_df$data()$Cépage, "<br/>",
  sd_df$data()$FaireValoir
)

leaflet(sd) %>%
  addProviderTiles("CartoDB.Positron", group = "Positron") %>%
  addTiles(urlTemplate = "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", "© Google", group = "Satellite") %>%
  addTiles(urlTemplate = "https://wxs.ign.fr/choisirgeoportail/geoportail/wmts?REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0&STYLE=PCI vecteur&TILEMATRIXSET=PM&FORMAT=image/png&LAYER=CADASTRALPARCELS.PARCELLAIRE_EXPRESS&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}", "© IGN", group = "Cadastre") %>%
    addPolygons(
    fillOpacity = 0.7, weight = 0.5,
    popup = click, group = "Parcelles"
  ) %>%

  addScaleBar(position = "bottomleft",
      options = scaleBarOptions(metric = TRUE, imperial = FALSE)) %>%
  addLayersControl(baseGroups = c("Positron", "Satellite", "Cadastre"),
      overlayGroups = c("Parcelles"), options = layersControlOptions(collapsed = FALSE)) %>%
  addMeasure(
    position = "topright",
    primaryLengthUnit = "meters",
    primaryAreaUnit = "hectares",
    localization = "fr",
    activeColor = "red",
    completedColor = "#7D4479"
  )

```


![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/cartev0.png)


#### Création des filtres



```{r}
Inputs {.sidebar}
-----------------------------------------------------------------------

#```{r}
filter_select("Section", "Section", sd_df, ~section, allLevels = TRUE)
filter_select("Cépage", "Cépage", sd_df, ~Cépage, allLevels = TRUE)
filter_select("FaireValoir", "Faire-Valoir", sd_df, ~FaireValoir, allLevels = TRUE)

#```
```

![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/cartev1.png)


#### Création du tableau de données

On utilise ici le package DT qui permet la communication avec le reste des modules via crosstalk.
On ajoute des boutons pour copier, exporter en csv et exporter en excel.

```
Row {data-height=300}
-------------------------------------

###

#```{r}
datatable(sd_df, editable = T,
  rownames = FALSE, extensions = c("Scroller", "Buttons"),
  options = list(dom = "Blrtip", scrollY = 300, scroller = TRUE,
                 buttons = list('copy', 'csv', 'excel')))

#```
```

![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/cartev2.png)


### L'ajout d'autres couches non-personnalisées

La dernière question : comment *facilement* ajouter des couches non-personnalisées telles que les aires AOC ou la géologie ?






#### Cas où la donnée a une version tuilée : carte géologique & ZNIEFF

On récupère les couches WMS : comme c'est assez retors pour obtenir les liens directs, on passe par QGIS.

Par exemple, pour un WMS du BRGM on ajoute une nouvelle connexion WMS à QGIS - http://geoservices.brgm.fr/geologie

![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/qgis_wms_brgm.png)

Puis on clique sur connexion pour obtenir les noms des différentes couches disponibles :

![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/qgis_brgm_couches.png)


Ici, la couche qui nous intéresse est par exemple le scan des cartes géologiques 1/50000e, on note donc de prendre "SCAN_D_GEOL50". Dans notre carte, on rajoute une fonction addWMSTiles comme ci-dessous. J'ai également mis les ZNIEFF 1 que l'on peut récupérer de la même façon depuis https://inpn.mnhn.fr/telechargement/cartes-et-information-geographique/inv/znieff1



```r
leaflet(sd) %>%
  addProviderTiles("CartoDB.Positron", group = "Positron") %>%
  addTiles(urlTemplate = "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", "© Google", group = "Satellite") %>%
  addTiles(urlTemplate = "https://wxs.ign.fr/choisirgeoportail/geoportail/wmts?REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0&STYLE=PCI vecteur&TILEMATRIXSET=PM&FORMAT=image/png&LAYER=CADASTRALPARCELS.PARCELLAIRE_EXPRESS&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}", "© IGN", group = "Cadastre") %>%
  addWMSTiles(baseUrl = "http://geoservices.brgm.fr/geologie/",
              layers = "SCAN_D_GEOL50",
              options = WMSTileOptions(token = "public", format = "image/png",
                         transparent = F, srs = "EPSG:4326"),
              attribution = "© BRGM", group = "Géologie") %>%
  addWMSTiles(baseUrl = "http://ws.carmencarto.fr/WMS/119/fxx_inpn",
              layers = "Znieff1",
              options = WMSTileOptions(token = "public", format = "image/png",
                         transparent = F, srs = "EPSG:4326"),
              attribution = "© INPN", group = "ZNIEFF") %>%

  addPolygons(
    fillOpacity = 0.7, weight = 0.5,
    popup = click, group = "Parcelles"
  ) %>%

  addScaleBar(position = "bottomleft",
              options = scaleBarOptions(metric = TRUE, imperial = FALSE)) %>%

# bien modifier les groupes ici pour qu'ils soient cliquables
  addLayersControl(baseGroups = c("Positron", "Satellite", "Cadastre"),
                   overlayGroups = c("Parcelles", "Géologie", "ZNIEFF"),
                   options = layersControlOptions(collapsed = FALSE)) %>%
  addMeasure(
    position = "topright",
    primaryLengthUnit = "meters",
    primaryAreaUnit = "hectares",
    localization = "fr",
    activeColor = "red",
    completedColor = "#7D4479"
  )%>%
    addLegend("bottomright", # ici c'est la légende que l'on veut afficher
    group = "ZNIEFF",
    colors = "#008A37",
    title = "ZNIEFF Type 1",
    labels = "",
    opacity = 0.8
  ) %>%
    hideGroup(c("Géologie","ZNIEFF"))
```
![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/cartev3.png)

#### Cas où la donnée n'a pas de version tuilée : aires AOC et autres couches perso avec Mapbox



Un WMS est disponible, mais ne permet pas de correctement différencier les AOC au sein d'une même zone :yum:
À partir de la couche INAO des aires AOC viticoles, on réalise donc une extraction autour de notre zone d'étude sur QGIS. On la nettoie (Alg. : *Réparer les géométries*), on passe la couche en géométries uniques (Alg. : *De morceaux multiples à morceaux uniques*), et on l'exporte en geojson / WGS84.


On charge ensuite la couche sur https://studio.mapbox.com/tilesets/, dans *New Tilesets*.

![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/uploadmapbox.png)


Ce service va nous permettre de nous créer facilement de petits WMS intégrables dans notre carte. On peut les customiser et créer des couches de belle facture pour notre carte en quelques clics.

Une fois la couche chargée, vous pouvez créer un style comprenant la donnée que vous venez d'uploader en allant dans Styles > New Style > Blank Style.
Vous cliquez ensuite sur Layers et ajoutez vos données depuis le bouton "Source"

![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/mapbox1.png)

On peut ensuite paramétrer notre style en conditionnant la symbologie aux valeurs des attributs :

![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/mapbox2.png)
![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/mapbox3.png)

Quand votre style est prêt, pour pouvoir l'utiliser dans la carte interactive, il faut le publier et récupérer le lien. On clique sur "Publish"
![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/mapbox4.png)

Puis sur Share, en sélectionnant "Third party" & Fulcrum pour avoir un lien de tuile XYZ facile à intégrer dans notre code.

![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/mapbox5.png)


On met à jour notre code de carte, en utilisant cette fois la fonction addTiles() :

```r
leaflet(sd) %>%
  addProviderTiles("CartoDB.Positron", group = "Positron") %>%
  addTiles(urlTemplate = "https://mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}", "© Google", group = "Satellite") %>%
  addTiles(urlTemplate = "https://wxs.ign.fr/choisirgeoportail/geoportail/wmts?REQUEST=GetTile&SERVICE=WMTS&VERSION=1.0.0&STYLE=PCI vecteur&TILEMATRIXSET=PM&FORMAT=image/png&LAYER=CADASTRALPARCELS.PARCELLAIRE_EXPRESS&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}", "© IGN", group = "Cadastre") %>%
addWMSTiles(baseUrl = "http://geoservices.brgm.fr/geologie/", layers = "SCAN_D_GEOL50",
options = WMSTileOptions(token = "public", format = "image/png", transparent = F, srs = "EPSG:4326"), attribution = "© BRGM", group = "Géologie") %>%
  addWMSTiles(baseUrl = "http://ws.carmencarto.fr/WMS/119/fxx_inpn", layers = "Znieff1",
options = WMSTileOptions(token = "public", format = "image/png", transparent = F, srs = "EPSG:4326"), attribution = "© INPN", group = "ZNIEFF") %>%

  #remplacer l'adresse ci-dessous par la votre ;-)
  addTiles(urlTemplate = "https://api.mapbox.com/styles/v1/yournamehere/codebizarre/tiles/256/{z}/{x}/{y}@2x?access_token=codeencoreplusbizarre",
           "INAO, Mapbox", group = "Aires AOC") %>%


  addPolygons(
    fillOpacity = 0.7, weight = 0.5,
    popup = click, group = "Parcelles"
  ) %>%

  addScaleBar(position = "bottomleft", options = scaleBarOptions(metric = TRUE, imperial = FALSE)) %>%
  addLayersControl(baseGroups = c("Positron", "Satellite", "Cadastre"), overlayGroups = c("Parcelles", "Géologie", "ZNIEFF", 'Aires AOC'), options = layersControlOptions(collapsed = FALSE)) %>%
  addMeasure(
    position = "topright",
    primaryLengthUnit = "meters",
    primaryAreaUnit = "hectares",
    localization = "fr",
    activeColor = "red",
    completedColor = "#7D4479"
  )%>%
    addLegend("bottomright",
    group = "ZNIEFF",
    colors = "#008A37",
    title = "ZNIEFF Type 1",
    labels = "",
    opacity = 0.8
  ) %>%
   addLegend("bottomright",
    group = "Aires AOC",
    colors = c("#F4D8D8","#EAF161","#45D21C"),
    title = "AOC",
    labels = c("Beaujolais","Côtes-de-Brouilly","Brouilly"),
    opacity = 0.8
  ) %>%
    hideGroup(c("Géologie","ZNIEFF", "Aires AOC"))
```


![](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/webmapping_avec_r/cartev4.png)



**Remarque** : si vous prévoyez un usage intensif de ce genre de cartes, il existe une limite à la version gratuite, avec un certain nombre de requêtes par mois. Au-delà de ce montant, il vous faudra payer pour assurer la continuité de service de ces données dans votre carte.




## Conclusion

On refait tourner notre script sur les 10 exploitations, et pour chacune d'entre elles nous avons une carte interactive avec ses parcelles, différents fonds de carte, la géologie, les aires AOC, les ZNIEFF, et on peut empiler facilement un certain nombre de couches sans monter bien haut en ce qui concerne la taille des fichiers (entre 6 et 20 Mo selon le nombre de polygones effectivement compris dans le fichier, ici les parcelles de l'exploitation). Il est possible de filtrer nos données, d'interagir avec dans le tableau qui peut être exporté, de réaliser des mesures sur la carte.

Le fichier peut ensuite être partagé, envoyé par mail, uploadé sur un site ou déposé sur une base de données documentaire.
Il est alors possible de créer à la chaîne et pour un grand nombre d'opérateurs (testé par votre humble serviteur pour 10'000 cartes différentes) ce type de petites cartes personnalisées très utiles et relativement faciles à mettre en place.

Bon courage !



----

## Auteur

Romain Lacroix
contact : @lacxrx sur Twitter
