---
title: Afficher des graphiques sur une carte - OpenLayers/Artichow
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-10-29
description: Afficher des graphiques sur une carte - OpenLayers/Artichow
image: ''
license: default
robots: index, follow
tags:
    - artichow
    - graphique
    - OpenLayers
---

# Afficher des graphiques sur une carte - OpenLayers/Artichow

:calendar: Date de publication initiale : 29 octobre 2008

## Introduction

Une carte n'est qu'un des nombreux moyens existants (graphique, tableaux....) permettant l'affichage et la mise en forme de données. Pourtant la plupart des librairies cartographiques actuelles se résument à un affichage "simple" de données géographiques. Or la plus value d'une donnée est justement sa mise la possibilité de la faire parler, de dégager une tendance, bref de l'utiliser...

C'est pourquoi après avoir consulté le [blog de Bjørn Sandvik](http://blog.thematicmapping.org/) et notamment son [article sur le couplage d'OpenLayers et google Chart](http://blog.thematicmapping.org/2008/04/openlayers-and-google-chart-mashup.html) je me suis lancé le projet d'arriver à un résultat similaire mais en utilisant uniquement des librairies OpenSource : [OpenLayers](http://openlayers.org/) et [Artichow](http://www.artichow.org/).

## Logique du script

La logique du script se base sur trois éléments majeurs :

- Un serveur WFS (ou tout autre format permettant l'affichage d'objet vecteur)
- Une librairie permettant de générer des graphiques (dans notre cas Artichow)
- La propriété `externalGraphic` de l'objet `Style` associé à ma couche vecteur

Concrétement, lors de l'appel de ma couche WFS j'ai spécifié dans mon protocole d'utiliser une image dont l'URL pointe vers mon script générant à la demande une image (grâce à Artichow). Ainsi pour chaque nouvel objet vecteur ajouté, un graphique est généré.

## Mise en application

### Côté client : la partie JavaScript (openLayers)

Comme souligné précédemment, c'est une propriété particulière de l'objet style,externalGraphic , qui nous permet d'afficher une image. La portion de script ci-dessous présente succintement la logique utilisée :

```javascript
function featureStyle() {  
  styleCircle = new OpenLayers.Style(  
    {  
      fillOpacity: 0.7,  
      pointRadius: "${radius}",  
      externalGraphic: "${getChartURL}"  
    },{  
      context: {  
        radius: function(feature) {  
          var minV = 28196;  
          var maxV = 1336317;  
          var minR = 2;  
          var maxR = 30;  
          surf = Math.round(minR+( (maxR-minR)*( (feature.attributes.POP_TOTAL-minV)/(maxV-minV) )));  
          surf = surf* Math.pow(2,map.getZoom()-1)  
          console.log(surf);  
          return surf;  
        },  
        getChartURL: function(feature) {  
          var charturl = './php_graph/graphCircle.php?value='+feature.attributes.POP_TOTAL/2000+'&surf='+styleCircle.context.radius(feature)*2+'&urban='+feature.attributes.URBAN+'&rural='+feature.attributes.RURAL;  
          return charturl;  
        } // End of function getChartURL  
      } // End of obj context  
    }  
  ); // End of obj OpenLayers.Style  
  styleMap = new OpenLayers.StyleMap({'default':styleCircle, 'select': {fillOpacity: 1}});  
  return styleMap;  
}
```

Concrétement, ma propriété `externalGraphic` pointe vers la fonction `getChartURL`. Dans celle-ci j'ai défini une variable `charturl` dans laquelle est spécifiée le chemin d'accès à mon script générant l'image ainsi que les informations dont j'ai besoin pour le graphique.

### Côté serveur : la partie PHP (Artichow)

Pour chaque objet vecteur dessiné sur la carte, mon navigateur fait appel à un script php qui retourne ensuite le graphique désiré sous forme d'image. Le script utilisé est le suivant :

```javascript
getValueUrban = $_GET["urban"];  
getValueRural = $_GET["rural"];  
require_once "../lib/php/Artichow/Pie.class.php";  

//NewGraph Obj  
$graph = new Graph(300, 300);

//Value  
$values = array(getValueUrban,getValueRural);  
$aThemeColor = array(  
  new Color(255,0,0,80),  
  new Color(0,0,255,80)  
);

//Type of graph  
$plot = new Pie($values,$aThemeColor);  
$plot->set3D(20);  
$plot->explode(array(0 => 15));  
$plot->legend->hide(TRUE);  
$plot->label->hide(TRUE);  
$plot->setStartAngle(90);

//Background Transparent  
$plot->setBackgroundColor(new Color(255,255,255));  
$color_gd = imagecolorallocate($graph->getDriver()->resource, 255,255,255);  
imagecolortransparent($graph->getDriver()->resource, $color_gd);

//Border  
$border = new Border();  
$graph->add($plot);  
$graph->border->hide(true);  
return $graph->draw();  
```

Dans mes variables globales GET je récupère les informations envoyées par mon navigateur que j'inclut ensuite au graphique final.

## Exemple de carte

Les données utilisées proviennent de : [geodata](http://geodata.grid.unep.ch/#)

![Exemple 1](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2008/Capture.png "Exemple 1"){: .img-center loading=lazy }

![Exemple 2](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2008/graph_bar.png "Exemple 2"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->
