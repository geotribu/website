---
title: "Documenter vos bases de données : exemple avec OpenStreetMap"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2011-01-19
description: "Documenter vos bases de données : exemple avec OpenStreetMap"
tags:
    - database
    - OpenStreetMap
    - PostgreSQL
---

# Documenter vos bases de données : exemple avec OpenStreetMap

:calendar: Date de publication initiale : 19 janvier 2011

![logo OpenStreetMap](https://cdn.geotribu.fr/img/logos-icones/OpenStreetMap/Openstreetmap.png "logo OpenStreetMap"){: .img-thumbnail-left }

Dans un précédent tutoriel portant sur OpenStreetMap [Créez votre propre serveur OpenStreetMap sous Ubuntu 10.04 Lucid Lynx](http://www.geotribu.net/node/262), nous vous faisions importer des données dans la base de données PostgreSQL mais sans vous apprendre à les explorer rapidement.  

Nous vous proposons pour cela de découvrir comment être rapidement en mesure de comprendre la structure d'une base de données existantes en la modélisant par l'intermédiaire d'un outil tiers.  
L'outil retenu pour cela est SchemaSpy. Vous allez nous dire alors d'arrêter car vous avez déjà lu le tutoriel [Modélisation d'une base de données avec SQL Power Architect](http://www.geotribu.net/node/248)  
Il n'en est rien car cet outil n'a pas pour but de modéliser une base de données mais plutôt de la documenter en analysant les tables les relations, en créant un dictionnaire des données et en vous fournissant des conseils d'optimisation.  

Ainsi, vous pourrez produire un rapport consultable/partageable sur Internet en quelques minutes.  
Evidemment, cette méthode bien qu'appliquée à la base de OpenStreetMap est applicable à l'ensemble des bases de données que vous rencontrerez à partir du moment où elles possèdent un pilote JDBC (basé sur Java).

Après cette longue introduction, commençons!!

## Installer l'outil

L'outil étant basé sur Java et Graphviz (une bibliothèque graphique), il faut les installer.

### Sous Windows

1. Installez GraphViz en allant sur <http://www.graphviz.org/> et en allant dans la section `Download`.  
Double-cliquez sur le fichier et faites des "suivant-suivant" pour installer  
Si vous êtes sous Vista, même en étant administrateur, il est conseillé d'ouvrir la fenêtre de commandes, de vous déplacer dans le répertoire contenant votre fichier et faire un `3msiexec /a graphviz-x.xx.msi`
2. Vérifiez que vous n'avez pas déjà Java en allant sur `Démarrer > Tous les Programmes > Accessoires > Invite de commande`, Tapez : `java -version`
Si vous avez un retour mentionnant java version 1.6.x.x ou 1.5.x.x, vous pouvez sautez l'étape suivante
3. Installez Java en allant le récupérer sur <http://www.java.com/fr/download/manual.jsp>  
Comme pour GraphViz, double-cliquez sur le fichier reçu, suivez les instructions et c'est OK
4. En introduction, nous avions fait référence à des drivers JDBC, il faut les récupérer sur <http://jdbc.postgresql.org/download.html>  
Il faut si votre version de java est 1.5.x.x prendre des pilotes de la colonnes JDBC3 correspondant à votre version de PostgreSQL.  
Si vous avez une version 1.6.x.x (ce qui est le cas avec l'installation de l'étape 3 si vous n'aviez pas déjà java antérieurement), il faudra choisir un pilote JDBC4 correspondant à PostgreSQL
5. Récupérez enfin SchemaSpy en allant sur <http://schemaspy.sourceforge.net/> ou par le [lien direct](http://sourceforge.net/projects/schemaspy/files/schemaspy/SchemaSpy%205.0.0/schemaSpy_5.0.0.jar/download)
6. Rajouter à la fin de la variable d'environnement PATH, le chemin vers dot.exe, c'est à dire `C:\Program Files\Graphviz2.26.3\bin` (ou `C:\Program Files (x86)\Graphviz2.26.3\bin` pour une machine avec un windows 64 bits) précédé d'un point virgule qui joue le rôle de séparateur.

### Sous Ubuntu Linux 10.04

Attention, inutile de faire les étapes 1 et 2 si vous venez du tutoriel de OpenStreetMap (vous avez déjà fait ces manipulations pour installer Osmosis)

1. Testez la présence de Java : `java -version`
2. Sinon, faire :

    ```bash
    sudo nano /etc/apt/sources.list
    ```

    puis coller à la fin :  

    ```txt
    ###########################################################################  

    ## Commercial  

    deb <http://archive.canonical.com/ubuntu> lucid partner

    ## Sources  

    # deb-src <http://archive.canonical.com/ubuntu> lucid partner  

    ###########################################################################  
    ```

    Puis fermer avec `ctrl + O`.  
    Ensuite, rechargez le gestionnaire de package et installer Java avec :

    ```bash
    sudo apt-get update  
    sudo apt-get upgrade  
    sudo apt-get install sun-java6-jre  
    ```

3. Installez GraphViz

    ```bash
    sudo apt-get install graphviz
    ```

4. En introduction, nous avions fait référence à des drivers JDBC, il faut les récupérer sur <http://jdbc.postgresql.org/download.html> . Il faut si votre version de java est 1.5.x.x prendre des pilotes de la colonnes JDBC3 correspondant à votre version de PostgreSQL. Si vous avez une version 1.6.x.x (ce qui est le cas avec l'installation de l'étape 3 si vous n'aviez pas déjà java antérieurement), il faudra choisir un pilote JDBC4 correspondant à PostgreSQL
5. Récupérez enfin `SchemaSpy` en allant sur <http://schemaspy.sourceforge.net/> ou par le [lien direct](http://sourceforge.net/projects/schemaspy/files/schemaspy/SchemaSpy%205.0.0/schemaSpy_5.0.0.jar/download)

## Utilisez l'outil pour faire votre "beau schéma"

Le plus long était l'installation.  

Il vous suffit de suivre le modèle ci-dessous et de remplacer les variables encadrées par <...> par vos propres paramètres :...

```bash
java -jar -cp -t pgsql -db  -host  -u  -p  
-s  -o  
```

Un cas concret avec l'utilisateur de base de données "utilisateurbase" avec son mot de passe "motdepasse" connécté en local sur une base osm et envoyant le résultat dans le répertoire `osm_psql_doc`.

<!-- markdownlint-disable MD046 -->
=== ":window: Windows"

    ```cmd
    java -jar C:/downloads/schemaSpy_5.0.0.jar -cp C:/download/postgresql-9.0-801.jdbc4.jar -t pgsql -db osm -host localhost -u utilisateurbase -p motdepasse -s public -o osm_psql_doc
    ```

=== ":fontawesome-brands-linux: Linux et assimilés"

    ```bash
    java -jar /home/monutilisateur/download/schemaSpy_5.0.0.jar -cp /home/monutilisateur/download/postgresql-9.0-801.jdbc4.jar -t pgsql -db osm -host localhost -u utilisateurbase -p motdepasse -s public -o osm_psql_doc  
    ```
<!-- markdownlint-enable MD046 -->

Ouvrir avec votre navigateur le fichier index.html du répertoire `osm_psql_doc` et vous avez ainsi documenté la structure de la base OSM importée dans PostgreSQL.  

Une version hébergée datant du 13 janvier 2010 est disponible en suivant le [lien](http://osm.analysesig.net/osm2pgsql_schema).  

Vous avez vu ainsi comment documenter votre base de données postgreSQL OpenStreetMap mais vous auriez pu faire de même avec un autre base postgreSQL ou une base MySql ou sqlite. Vous pouvez aussi installer une interface graphique plutôt que de faire de la ligne de commande.  

Allez sur le [site officiel pour découvrir comment](http://schemaspy.sourceforge.net/) !

## Exercices complémentaires

Nous vous proposons d'appliquer la même méthode à l'exemple de la base obtenue dans le tutoriel [Modélisation d'une base de données avec SQL Power Architect](http://www.geotribu.net/node/248) très intéressant car il y a beaucoup de relations entre les tables.  

Nous vous conseillons aussi croiser le nom des colonnes dans le schéma obtenu, avec la liste des objets qui constituent la carte [https://wiki.openstreetmap.org/wiki/FR:Map_Features](https://wiki.openstreetmap.org/wiki/FR:Map_Features)  
Vous trouverez une correspondance flagrante entre les clés et les noms des champs dans certaines tables de la base de donnée.  

Ce dernier exercice complémentaire met d'ailleurs en évidence un manque en terme d'analyse depuis un modèle de base de données , on ne voit que la structure et on oublie les occurrences pour les champs. Il y a donc un grand intérêt à explorer la donnée et sa documentation lorsqu'elle existe.

----

<!-- geotribu:authors-block -->
