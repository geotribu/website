---
authors:
- GeoTribu
categories:
- article
date: 2009-12-31 10:20
description: '...'
image: ''
license: default
robots: index, follow
tags:
- SIG
title: Une machine virtuelle orientée SIG
---

# Une machine virtuelle orientée SIG


:calendar: Date de publication initiale : 31 décembre 2009


----

![logo_color.png](http://geotribu.net//sites/default/files/Tuto/img/Blog/virtual_gis/logo_color.png) Le Père Noël ne vous a pas suffisamment gâté pour les fêtes? Vous rêviez de recevoir un ordinateur pour geek géomaticien mais là sous le sapin rien...  

Si c'est le cas, je vous conseille d'aller faire un tour du côté de [Gisvm](http://gisvm.com/) qui propose en téléchargement une machine virtuelle complètement orientée SIG. Celle-ci, en fonction de vos besoins, se décline en deux versions, une serveur l'autre desktop. Les principales caractéristiques sont présentées dans le tableau ci-dessous :




| GISVM **Desktop** | GISVM **Server** |
| * S.O. Linux Ubuntu 8.04 Desktop
* Samba
* PostgreSQL/PostGIS
* Java/Tomcat/GeoServer
* Apache/PHP/MapServer
* Quantum GIS
* gvSIG
* KOSMO
* uDIG
* FWTools: OpenEV, GDAL/OGR, Proj4, OGDI
* OpenOffice
* Ainsi que toutes les applications standards d'Ubuntu
| * S.O. Linux Ubuntu 9.04 Server Edition
* Pacote LAMP Server (Linux, Apache, MySQL and PHP)
* Samba
* Tomcat Java Server
* PostgreSQL/PostGIS, ZigGIS and FDO ready!
* Mapserver
* Geoserver
* Deegree
* Webmin
|


Au delà d'avoir déjà une grande quantité de programmes préinstallés, les avantages de la virtualisation sont nombreux. En effet et par expérience, je sais qu'il est parfois hasardeux de vouloir faire cohabiter sur une même machine un environnement de travail et un environnement de test. Il m'est déjà arrivé en effet de devoir refaire une installation complète de ma machine suite à des dépendances corrompues. Avec la virtualisation, ce problème ne se pose plus. Vous avez sur une même machine deux environnements complètement séparés.


Essayons d'expliquer le principe de la virtualisation. Pour cela, imaginez que l'on vous fournisse un nouvel environnement déjà installé et paramétré et que vous n'avez plus qu'à appuyer sur start. Eh oui c'est aussi simple que cela et cela fonctionne quel que soit votre système d'exploitation. Vous pouvez ainsi, par exemple, faire fonctionner Ubuntu sur Windows ou inversement Windows sur Ubuntu (*ça me donne des boutons d'écrire cela ...*). De plus, vous pouvez bien évidemment réaliser des modifications, créer ou supprimer des fichiers dans votre environnement virtualisé... Tout fonctionne comme un système d'exploitation normal sauf que celui-ci s'exécute à partir d'un autre système d'exploitation.


![vmware_server.gif](/sites/default/files/Tuto/img/Blog/virtual_gis/vmware_server.gif)  

*source : [GISVM Blog](http://www.gisvm.com/blog/?p=207)*



Passons maintenant à la mise en application. Pour cela, deux étapes préalables sont nécessaires :


* Télécharger [VM Ware player](http://www.vmware.com/download/player/)
* Télécharger la machine virtuelle [GISVM](http://gisvm.com/download.html)


Une fois VM Ware player d'installé, il ne vous reste plus alors qu'à sélectionner votre machine virtuelle GISVM (*.vmx) qui une fois lancée affichera un environnement semblable à celui de l'image ci-dessous :


![739px-Gisvm_startup.jpg](/sites/default/files/Tuto/img/Blog/virtual_gis/739px-Gisvm_startup.jpg)  

*source : [GISVM Wiki](http://gisvm.com/wiki/index.php?title=GISVM_Desktop)*


Et voilà, il ne vous reste plus qu'à faire joujou !


-----------------------  

Source : [GISVM Blog](http://www.gisvm.com/blog/?p=207)




----

## Auteur

--8<-- "content/toc_nav_ignored/snippets/authors/geotribu.md"
