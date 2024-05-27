---
title: "Modélisation d'une base de données avec SQL Power Architect"
authors:
    - Arnaud VANDECASTEELE
categories:
    - article
comments: true
date: 2010-07-15
description: "Modélisation d'une base de données avec SQL Power Architect"
tags:
    - database
    - modélisation
    - open source
---

# Modélisation d'une base de données avec SQL Power Architect

:calendar: Date de publication initiale : 15 juillet 2010

![icone database](https://cdn.geotribu.fr/img/logos-icones/programmation/database.png "icone database"){: .img-thumbnail-left }

Dans le cadre de mon activité professionnelle, j'avais besoin de modéliser une base de données et d'importer des données d'une base access ([base gaspar](http://macommune.prim.net/gaspar/)) vers une base PostgreSQL. Plutôt que de faire tout cela à la main, j'ai cherché à optimiser et surtout automatiser au maximum les différentes opérations. Je me suis donc penché sur les différentes solutions existantes et je vous livre mes impressions. Il existe très certainement des équivalents propriétaires aux différentes applications que nous allons présenter ci-dessous, mais nous avons fait le choix de privilégier au maximum (intégralement) les logiciels OpenSource.

----

## Modélisation de la base

Durant cette étape, la problématique était double. Tout d'abord, faire de la [rétro-ingénierie](https://fr.wikipedia.org/wiki/R%C3%A9tro-ing%C3%A9nierie) à partir de la base Gaspar existante et ainsi m'éviter de créer manuellement toutes les tables et les relations. Ensuite, trouver un logiciel qui me permette de modéliser efficacement ma base de données et qui soit également capable de se connecter à un [SGBD](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_gestion_de_base_de_donn%C3%A9es) afin d'intégrer directement mon schéma.

### Rétro-ingénierie

Petit aparté avant d'entrer dans le vif du sujet. Comme je l'ai précisé en introduction, mon format de données en entrée était au format DBF (access). Impossible donc pour moi de le lire directement. Il me fallait donc trouver une solution afin de m'éviter le fastidieux travail de recopie de la base Access. Mon objectif était de trouver un applicatif me permettant d'extraire automatiquement le schéma de ma base Access et qui en plus fonctionne sur Linux. Mission impossible me direz-vous ? En fait non, il existe une suite d'utilitaires[^1] regroupés sous le nom de [MDBTools](http://sourceforge.net/projects/mdbtools/) qui vous permet de manipuler et d'exporter vos données stockées au format Access. Quelques lignes de commandes plus tard, je me retrouve avec un fichier SQL que je peux directement importer dans un SGBD et avoir ainsi toute la structure de la base. Passons maintenant à la modélisation de la base.

Pour les amoureux du python, vous pouvez utiliser ce [script](http://code.activestate.com/recipes/52267-reverse-engineer-ms-accessjet-databases/) qui vous permettra de passer d'une base Access à un fichier SQL intégrable dans votre SGBD. Néanmoins, celui-ci ne gère pas (encore) les index ainsi que les clés primaires.

### Modélisation

Il existe de nombreux logiciels permettant de modéliser une base de données. Néanmoins, très peu sont Open Source et surtout rares sont ceux qui sont réellement complets au niveau fonctionnalités.

Pour cela, quatre logiciels ont été passés au banc d'essai :

- [Dia](http://projects.gnome.org/dia/) et l'extension [tedia2sql](http://tedia2sql.tigris.org/)
- [Druid](http://druid.sourceforge.net/)
- [DBDesigner4](http://www.fabforce.net/dbdesigner4/index.php)
- [Architect](http://www.sqlpower.ca/page/architect)

Afin de compléter cette liste nous indiquons également d'autres logiciels que nous avons trouvé mais que nous n'avons pas essayé :

- [ERDesigner](http://mogwai.sourceforge.net/?Welcome:ERDesigner_NG)
- [MySQL GUI Tools](http://dev.mysql.com/downloads/gui-tools/5.0.html) et [MySQL Workbench](http://dev.mysql.com/downloads/workbench/)
- [SchemaSpy](http://schemaspy.sourceforge.net/)

Tous ont leurs avantages, mais c'est Architect qui a eu ma préférence. J'avais commencé à travailler avec dia mais si ce logiciel est idéal pour des schémas UML, il faut avouer qu'il y a encore du travail pour la modélisation de bases de données. En plus, il ne permettait pas l'import automatique du schéma généré dans le SGBD de mon choix.

Edité par la compagnie québécoise SQL Power, Architect fait partie de leur gamme de logiciels orientés Buisness Intelligence (BI). Comme nous l'avons déjà souligné, celui-ci permet de modéliser votre base et de générer automatiquement le schéma dans le SGBD de votre choix (MySQL, PostgreSQL, Oracle...). Mais ce n'est pas tout, car vous pouvez aussi créer les métadonnées pour les outils d'extraction, de transformation et de chargement (ETL) ou encore de "designer" votre cube au format Mondrian.

Passons maintenant au design proprement dit. Si vous avez bien suivi ce billet, vous vous rappelez que nous avions préalablement créé un schéma de la base Access. Je n'ai plus alors qu'à créer une connexion vers ce schéma et à glisser/déposer les tables qui m'intéressent pour créer l'organisation que je souhaite. Enfin, reste l'étape de l'import vers le SGBD de mon choix. Une fois ma connexion créée, il me suffit de la sélectionner et mon modèle est alors automatiquement généré vers la base cible. Magique non ?

![SQL Power Architect](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2010/power_architect.png "SQL Power Architect"){: .img-center loading=lazy }

Comme vous l'avez surement constaté, nous avons été emballés par Architect. Pour toutes les personnes travaillant de près ou de loin dans le milieu des bases de données, ce logiciel fait partie de ceux qu'il est obligatoire de posséder. C'est un vrai plaisir de pouvoir créer graphiquement son schéma sans se soucier des particularités de tel ou tel SGBD.

[^1]: mdb-export, mdb-schema, mdb-tables

----

<!-- geotribu:authors-block -->
