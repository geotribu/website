---
title: "Initiation à MapServer"
authors:
    - Arnaud Vandecasteele
categories:
    - article
comments: true
date: 2008-08-22
description: "Initiation à MapServer"
tags:
    - MapServer
---

# Initiation à MapServer

:calendar: Date de publication initiale : 22 août 2008

## Introduction

![logo MapServer](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/mapserver.png "logo MapServer"){: .img-thumbnail-left }

Dans ce tutoriel vous apprendrez dans un premier temps à construire votre MapFile, nous verrons ensuite comment afficher une carte grâce au langage PhpMapScript, enfin nous verrons les nouveautés apportées par la version de MapServer.

- Qu'est ce que MapServer
- Intégrer MapServer
- Définir un MapFile
- Afficher une carte avec PhpMapScript

## Qu'est ce que MapServer

MapServer, est un environnement de développement permettant la réalisation d'applications web à composante cartographique. Il ne peut pas être considéré comme un SIG complet, mais il permet d'afficher des données géographique sous forme vectorielle ou cartographique. Pour plus d'informations vous pouvez consulter le site de MapServer.

## Comment intégrer MapServer

MapServer est multi-plateforme (Windows, Linux, Solaris, Mac Osx...). Dans ce tutoriel, nous ne verrons que l'installation sous Windows. Pour cela, il est nécessaire de télécharger le package MS4W, celui-ci contient entre autre un serveur apache, PHP, MapServer, PhpMapScript...

Après avoir télécharger et dezipper le package MS4W, il faudra le placer à la racine de votre disque dur. Puis lancer le fichier bat apache-install.bat. Et voilà, c'est fini ! Si vous ouvrez votre navigateur préféré (firefox bien sûr) avec localhost comme adresse vous devriez alors voir apparaitre la page de démarrage de votre serveur local.

## Définir son MapFile

Pour notre exemple, nous avons utilisé des données libres téléchargeable sur le site internet : <http://www.grida.no/> (link is external). Afin d'éviter d'avoir un fichier trop volumineux nous avons extrait la zone géographique correspondant à l'Indonésie. Un fichier zip des données utilisées est disponible ici.

Nous allons maintenant passer à la création de notre MapFile. C'est la pièce maîtresse de notre application, c'est lui qui est à la source de tous les échanges. Un MapFile se compose de plusieurs blocs. Il est important de comprendre et de bien former chacun d'eux. Sinon cela générera obligatoirement une erreur à l'exécution.

Notre fichier map sera composé de quatre blocs principaux. Chacun d'entre eux ont un rôle spécifique.

Le premier bloc va définir le MapFile d'une manière générale, un peu comme l'en-tête d'un fichier HTML. La balise MAP en haut du MapFile indique le début du fichier. Ensuite vient le nom du fichier, la taille de l'image qui va être générée, l'étendue géographique des données, l'unité utilisée et enfin le répertoire ou sont situées les données.

```conf
MAP
NAME "tutorial"
SIZE 1000 500
EXTENT 94.0000 -9.0048 131.000 4
UNITS METERS
IMAGECOLOR 255 255 255
SHAPEPATH "C:/ms4w/apps/cartoweb3/htdocs/phpMapScript/data"
```  

Ensuite vient le bloc Web, c'est lui qui va gérer où vont être entreposées les images générées par MapServer. Nous ne le verrons pas ici, mais c'est dans ce bloc qu'il va être possible de rajouter des éléments permettant d'enrichir l'interface générale de la page. Cela se passe grâce aux balises header et footer.

```conf
WEB
   IMAGEPATH "C:/ms4w/apps/cartoweb3/htdocs/phpMapScript/tmp"
   IMAGEURL "tmp/"
END
```

Maitenant nous allons spécifier à MapServer le type de fichier attendu en sortie. Dans notre cas cela sera une image de type png, il est bien sûr possible de définir d'autre type (jpg, gif etc.).

```conf
  OUTPUTFORMAT
  NAME png
  DRIVER "GD/PNG"
  MIMETYPE "image/png"
  IMAGEMODE PC256
  EXTENSION "png"
END
```

Pour finir nous allons maintenant lister les données à utiliser. Cela se passe grâce au bloc Layer. Il sera nécessaire de créer un bloc par données. A l'intérieur de ce bloc, il existe d'autres sous blocs tel que class, style, metadata etc.

```conf
LAYER
  NAME Admin_Indonesie
  STATUS ON
  CONNECTIONTYPE OGR
  CONNECTION "data/indonesie_surface.tab"
  TYPE LINE
    CLASS
      STYLE
          COLOR 0 0 0
          OUTLINECOLOR 255 255 255
      END
    END
END
```

Voilà nous sommes maintenant en mesure d'afficher une carte. Le fichier complet est disponible ici. Il est d'ailleurs possible de le faire directement en CGI grâce à la commande suivante :

[http://localhost/cgi-bin/mapserv.exe?map=C:/ms4w/apps/tutorial.map&mode=map](http://localhost/cgi-bin/mapserv.exe?map=C:/ms4w/apps/tutorial.map&mode=map)

Il est très important de bien indenter son code dans le MapFile. Une erreur arrive très rapidement, de plus vérifiez bien que tous vos blocs soient fermés par un END.

## Afficher une carte avec PhpMapScript

PhpMapScript est un module Php permettant la manipulation des objets, classes et méthodes relatifs au MapFile. Il sera ainsi possible d'activer ou de désactiver un layer, afficher la carte dynamiquement etc.

Dans ce tutoriel nous verrons simplement l'affichage d'une carte grâce au PhpMapScript. Cela vous permettra de vous familiariser un peu avec ce langage. Une liste complète des classes et méthodes est disponible sur cette page.

Pour cela nous aurons besoin tout d'abord d'instancier un nouvel objet Map, cela se fait grâce au constructeur ms_newMapObj auquel nous passons l'adresse où est situé notre MapFile. Ensuite, nous allons lui demander de dessiner la carte correspondante et enfin de la sauvegarder dans le dossier définit dans le bloc Web du MapFile.

```php
<?php
   // Éclaration de la bibliothèque PHPMAPSCRIPT
   dl('php_mapscript.dll')
   $map_file = "./tutorial.map";
   $map = ms_newMapObj($map_file);
   $image=$map->draw();
   $image_url=$image->saveWebImage(MS_PNG,1,1,0);
?>

<HTML>
    <HEAD>
      <TITLE?>Tutorial MapServer</TITLE?>
         </HEAD>
         <BODY>
             <IMG SRC= <?php echo $image_url; ?> >
          </BODY>
</HTML>
```

Si vous avez tout bien suivi, et que je ne me suis pas trompé (j'espère... :) ), une carte des contours de l'Indonésie devrait s'être dessinée. Une carte comme celle-ci :

![Indonésie](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2008/indonesie.png "Indonésie"){: .img-center loading=lazy }

----

<!-- geotribu:authors-block -->
