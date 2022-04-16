---
authors:
- Arnaud Vandecasteele
categories:
- article
date: 2009-04-26 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- GeoExt
- OpenLayers
- WMS
title: Créer une liste déroulante de couches issue d'un serveur WMS avec GeoExt
---

# Créer une liste déroulante de couches issue d'un serveur WMS avec GeoExt


:calendar: Date de publication initiale : 26 avril 2009


----

### introduction




---


![attention_light.jpg](/sites/default/files/Tuto/img/attention_light.jpg) Ce tutoriel utilise la dernière version de GeoEXT qui possède la particularité de disposer d'une nouvelle classe WMSCapabilitiesReader.


### Créer la liste déroulante




---


Pour implémenter la liste déroulante, vous avez juste à télécharger ce fichier [ComboBoxWMS](http://ks356007.kimsufi.com/arno/lib/js/geoext/geoext/lib/GeoExt/form/ComboBoxWMS.js) ([ou sa version packagée](http://ks356007.kimsufi.com/arno/lib/js/geoext/geoext/lib/GeoExt/form/ComboBoxWMS_minify.js)). Il vous faut ensuite déclarer ce script ainsi que les autres librairies (GeoExt, Ext, openLayers) de la manière suivante :








Ensuite créez une page qui sera chargé au démarrage et ajoutez l'objet ComboBoxWMS :


`ProxyHost = "/cgi-bin/proxy.cgi?url=";  

combo = new GeoExt.form.ComboBoxWMS({  

renderTo : 'formCombo',  

WMSurl : 'http://labs.metacarta.com/wms/vmap0',  

layerFilter : 'pop',  

triggerAction : 'all',  

ProxyHost : "/cgi-bin/proxy.cgi?url=",  

listeners: {  

select: function(combo, record, index) {  

var layers = record.data.name;  

layers = new OpenLayers.Layer.WMS(layers, this.WMSurl,  

{layers: layers, transparent:true},  

{buffer: 0, isBaseLayer:false});  

map.addLayer(layers);  

}//EOF select  

}//EOF listeners  

});//EOF combo`


![attention_light.jpg](/sites/default/files/Tuto/img/attention_light.jpg) N'oubliez de spécifier le paramètre "**ProxyHost**". En effet c'est un flux texte qui va transiter et votre navigateur, sans ce proxyHost, va donc le bloquer.


Les deux paramètres importants à préciser sont :


* WMSurl : l'URl à interroger
* ProxyHost : Spécifie le proxy à utiliser. A utiliser en cas d'appel à une serveur distant


### Exemple




---


[![comboBow_WMS.png](/sites/default/files/Tuto/img/geoext/comboBow_WMS.png)](http://geotribu.net/applications/tutoriaux/GeoExt/Combobox/geoExt_ComboBox.html)




----

## Auteur

--8<-- "content/team/avdc.md"
