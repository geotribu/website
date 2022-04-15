---
authors:
- Arnaud Vandecasteele
categories:
- article
date: 2008-10-16 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- OpenLayers
- WMS
- OGC
- SLD
title: Utiliser un SLD pour filtrer un flux WMS depuis OpenLayers
---

# Utiliser un SLD pour filtrer un flux WMS depuis OpenLayers


:calendar: Date de publication initiale : 16 octobre 2008


----

### Utiliser un SLD pour filtrer un flux WMS depuis OpenLayers




---


Définit par l'OGC, le [**S**tyled **L**ayer **D**escriptor](http://www.opengeospatial.org/standards/sld "Spécifications OGC SLD") (SLD) est un format de description (en [XML](http://fr.wikipedia.org/wiki/Extensible_Markup_Language "Wikipedia XML")) permettant la mise en forme de données géographique provenant d'un flux WMS. Pour simplifier il joue le même rôle qu'un fichier CSS pour une page HTML, le but étant de séparer complètement le style de la donnée. 


Concrètement, lors de la réception d'un flux WMS un style définit lui est rattaché. La particularité, étant que ce fichier n'est pas physiquement lié au moteur carto. En effet, il est tout à fait possible d'interroger un serveur cartographique distant, de réceptionner le flux WMS et de lui appliquer un style que vous aurez vous même défini.


### A quoi ressemble un SLD et comment cela fonctionne ?




---


Un SLD est un fichier XML contenant une liste de balises définie. On y retrouve par exemple la version du SLD utilisé, le nom de la données, le style à appliquer... Ci-dessous vous trouverez un exemple succinct de SLD : 


`xml version="1.0" encoding="UTF-8"?`




world

A style for World Population



#FF7171


#FF7171
2.0






Le fonctionnement en lui même n'a rien de bien compliqué, il suffit simplement de bien comprendre les différentes interactions ci-dessous :


* Un client effectue une requête WMS vers un serveur cartographique en spécifiant un SLD
* Le moteur cartographique analyse la validité de la requête et le cas échéant envoie le flux correspondant
* Le client récupère ce flux et peut ensuite l'afficher


### OpenLayers et SLD




---


Il existe en natif dans la librairie OpenLayers un objet [WMS](http://dev.openlayers.org/releases/OpenLayers-2.6/doc/apidocs/files/OpenLayers/Layer/WMS-js.html "API OpenLayers") dont l'une des propriétés est SLD. Il suffit alors de spécifier l'URL où est stocker votre fichier XML (valide) pour que celui-ci soit automatiquement appliqué à votre flux WMS.


Ce qui donne le code suivant :


`var worldWMS = new OpenLayers.Layer.WMS(  

"WORLD", "http: //localhost/cgi-bin/mapserv?map=/var/www/html/wms_wfs/world.map&",  

{  

layers: 'world',  

transparent:'true',  

SLD :'http://localhost/wms_wfs/styleSLD.xml'  

},  

{isBaseLayer:true,}  

);`


La carte ci-dessous, est une représentation mondiale du nombre d'habitant par Km² par pays. Le flux WMS étant généré par MapServer.



[![density_0.png](/sites/default/files/Tuto/img/SLD/density_0.png)](http://ks356007.kimsufi.com/arno/geotribu/applications/tutoriaux/tuto_wms_wfs/wms_wfs/filter_world.html)





----

## Auteur

--8<-- "content/team/avdc.md"
