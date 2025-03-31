---
title: Open Data Kit pour la collecte de données géographiques dans PostGIS (3/3)
authors:
    - Mathieu BOSSAERT
categories:
    - article
comments: true
date: 2021-09-22
description: Troisième et dernier article de présentation de la suite Open Data Kit (ODK) et son intégration au SI du CEN d'Occitanie et dans les processus métiers.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/open_data_kit_postgresql.png
license: CC-BY-SA
tags:
    - Android
    - collecte terrain
    - JSON
    - ODK
    - Open Data Kit
    - PostGIS
    - PostgreSQL
    - SQL
    - XML
---

# ODK pour la collecte de données géo dans PostGIS (3/3)

:calendar: Date de publication initiale : 22 septembre 2021

## Troisième partie - Récupération des données dans notre SI

![ODK PostGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/Central2PG.png "ODK + PostGIS"){: .img-thumbnail-left }

Les données collectées avec les formulaires peuvent être envoyées à différents outils :

* Aggregate ([EOL](https://en.wikipedia.org/wiki/End-of-life_product) : n'est plus maintenu)
* Central (détaillé plus bas)
* [Google Sheets](https://docs.getodk.org/collect-connect-google/)

ou récupérées directement sur le poste de travail avec [Briefcase](https://docs.getodk.org/briefcase-intro/).

Une fois les données centralisés, différentes solutions d'exploitation, d'analyse et de visualisation de données sont disponibles :

### Outils opensource

* R / [RuODK](https://github.com/ropensci/ruODK)
* ArqGIS -> [QRealtime](https://shivareddyiirs.github.io/QRealTime/)
* Redash : via [l'API](https://forum.getodk.org/t/first-use-of-a-central-web-form-and-basic-restitution-with-redash/30334/4) ou à travers une base de données PostgreSQL intermédiaire
* PostgreSQL/PostGIS -> [Central2PG](https://forum.getodk.org/t/postgresql-set-of-functions-to-get-data-from-central/33350) est la solution qui sera présentée plus en détail dans cet article

### Outils propriétaires

* Microsoft Excel via [l'API OData](https://www.odata.org/)
* [Microsoft Power BI](https://powerbi.microsoft.com/)
* [Google Data Studio](https://github.com/UDub-Impact/OData-Connector/issues)
* Tableau

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

*Previously on ODK PostGIS* :

[1 : Introduction à ODK](2021-06-08_odk_postgis_1.md){: .md-button } [2 : Exemple de mise en œuvre au CEN](2021-06-22_odk_postgis_2.md){: .md-button }
{: align=middle }

----

## ODK Central

C'est la composante "serveur" de la suite ODK. Il remplace Aggregate, arrivé en fin de vie au printemps 2021.

ODK Central reçoit les données des téléphones sous forme de fichiers [XML](https://fr.wikipedia.org/wiki/Extensible_Markup_Language) tout à fait lisibles et de fichiers binaires pour les éventuels médias collectés.

Il les stocke et en assure la diffusion via une [API REST (OData)](https://odkcentral.docs.apiary.io/#).

Il assure en outre la gestion des formulaires (ébauches et versions successives) et des utilisateurs mobiles. Ces derniers ont accès à des *projets*, qui regroupent différents formulaires.
Lorsque le téléphone interroge le serveur pour savoir quels formulaires sont diponibles à la saisie ou quels formulaires ont été mis à jour, *Central* sait à quelle ressource l'utilisateur configuré sur ce téléphone a accès.
La configuration des téléphones des utilisateurs se fait simplement en scannant avec ODK Collect le QRCode proposé par Central pour cet utilisateur.
Les versions récentes de Central et d'ODK Collect permettent à un utilisateur de participer à plusieurs projets qui peuvent être hébergés sur différentes serveurs.

Les fonctionnalités de Central sont décrites dans la [documentation](https://docs.getodk.org/central-intro/#odk-central-features).

Comme Aggregate, Central s'appuie sur une base de données PostgreSQL, mais il stocke les données sous forme de documents xml, quand Aggregate créait des tables de base de données pour chaque formulaire (une table de base et des tables filles pour les boucles de questions).
L'accès aux données stockées dans Central nécessite donc de revoir notre approche quant à l'intégration des données collectées dans notre SI "métier".

----

## Intégration des données au SI(G) du CEN (BDD PostGIS)

![logo PostGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/postgis.jpg "logo PostGIS"){: .img-thumbnail-left }

Diverses pistes d'exploitation des données ont été explorées pour conserver la fluidité que nous connaissions dans le cheminement de l'information, depuis ODK Collect vers nos outils métiers.  
Elles ont été présentées [ici](https://forum.getodk.org/t/sql-first-try-to-get-central-data-into-internal-postgis-database/30102?u=mathieubossaert) sur le forum d'ODK.
Voici un petit résumé de ces essais et une présentation plus détaillée de la solution générique finalement mise en oeuvre.

Ne souhaitant pas passer par un outil tiers, de type ETL (*Extract, Transform and Load*, [voir le travail décrit par Dave Henry avec Kettle](https://forum.getodk.org/t/automating-data-delivery-using-the-odata-endpoint-in-odk-central/22010)) pour réaliser cette tâche, nous avons exploré diverses pistes.

### Utilisation des fonctions XML de PostgreSQL

![icône XML](https://cdn.geotribu.fr/img/logos-icones/divers/xml.png "icône XML - XML File by Eucalyp from the Noun Project"){: .img-thumbnail-left }

La première idée explorée a consisté à exploiter les données XML de la table submission_defs avec les fonctions intégrées de PostgreSQL.

Cette méthode a été concluante puisque la vue suivante, présentée en détail [sur le forum d'ODK](https://forum.getodk.org/t/sql-first-try-to-get-central-data-into-internal-postgis-database/30102?u=mathieubossaert) peut être affichée dans ArqGIS :partying_face: :

```sql
CREATE VIEW odk_central.obs_sicen2020 AS
 WITH xmldata AS (
         SELECT submission_defs.xml::xml AS xml
           FROM odk_central.submission_defs
        ), core AS (
         SELECT "xmltable".phonenumber,
            "xmltable".custom_setting,
            "xmltable".astuce,
            "xmltable".email_utilisateur,
            "xmltable".username,
            "xmltable".nom_observateur,
            "xmltable".mail_observateur,
            [...]
```

Cette interrogation directe de la base de données n'est cependant [pas conseillée, à juste titre, par l'équipe de développement](https://forum.getodk.org/t/sql-first-try-to-get-central-data-into-internal-postgis-database/30102/2?u=mathieubossaert) qui ne garantit pas que le modèle de données n'évoluera pas dans le temps, contrairement à l'API qui est stable et normalisée.

Par ailleurs, l'exploitation du XML, bien que très efficace dans PostgreSQL n'est pas si "évidente que ça" pour qui, comme moi, n'exploite traditionnellement en SQL que des types de données non complexes.

### Utilisation de l'extension `pgsql_http`

Une seconde voie a consisté à utiliser l'extension [pgsql_http](https://github.com/pramsey/pgsql-http) développée par Paul Ramsey.

Cette méthode est présentée [ici](https://forum.getodk.org/t/sql-first-try-to-get-central-data-into-internal-postgis-database/30102/6?u=mathieubossaert).

L'extension permet de faire des appels à des ressources web et donc à l'API de Central. Le resultat de l'appel est un document JSON.

On réalise un appel à l'API pour chaque "table" du formulaire et le tour est presque joué.

![icône JSON](https://cdn.geotribu.fr/img/logos-icones/programmation/json.png "icône JSON"){: .img-thumbnail-left }

Il ne reste qu'à exploiter le JSON avec les [fonctions JSON proposées par PostgreSQL](https://www.postgresql.org/docs/13/functions-json.html). Avec le recul, la requête pourrait être simplifiée. Il est en effet inutile de tester l'existence d'un élément avant de tenter d'y accéder. S'il n'existe pas, une valeur nulle est renvoyée.

```sql
WITH submissions AS (
         SELECT json_array_elements(http.content::json -> 'value'::text) AS data
           FROM http(ROW('GET'::text::http_method, 'https://central.myserver.fr/v1/projects/1/forms/Sicen2020.svc/Submissions'::character varying, ARRAY[http_header('Authorization'::character varying, 'Basic bASDlldfdsfdf5d6f5ds65f6dsAD5f6ds5fds5f44dsdYi9P7zIw'::character varying)], NULL::character varying, NULL::character varying)::http_request) http(status, content_type, headers, content)
        )
 SELECT submissions.data ->> '__id'::text AS id,
    submissions.data ->> '__Submissions-id'::text AS "__Submissions-id",
        CASE
            WHEN (submissions.data #> '{phonenumber}'::text[]) IS NOT NULL THEN submissions.data -> 'phonenumber'::text
            ELSE NULL::json
        END AS phonenumber,
        CASE
            WHEN (submissions.data #> '{custom_setting}'::text[]) IS NOT NULL THEN submissions.data -> 'custom_setting'::text
            ELSE NULL::json
        END AS custom_setting,
        CASE
            WHEN (submissions.data #> '{utilisateur}'::text[]) IS NOT NULL THEN submissions.data -> 'utilisateur'::text
            ELSE NULL::json
        END AS utilisateur,
        CASE
            WHEN (submissions.data #> '{__system}'::text[]) IS NOT NULL THEN (submissions.data -> '__system'::text) ->> 'submissionDate'::text
            ELSE NULL::text
        END AS "submissionDate",
[...]
```

Cette voie est elle aussi concluante et elle m'a conforté dans l'idée que l'exploitation du JSON dans PostgreSQL me sera plus aisée que celle du XML.

### Utilisation de la commande `COPY FROM`

Enfin un article de [Leo Hsu et Regina Obe sur le "Postgres OnLine Journal"](https://www.postgresonline.com/journal/archives/325-Using-wget-directly-from-PostgreSQL-using-COPY-FROM-PROGRAM.html) m'est revenu à l'esprit... Il décrit une fonctionnalité de PostgreSQL 9.3 qui permet de passer à l'instruction COPY le résultat d'une commande système,
La syntaxe est la suivante :

```sql
COPY FROM program...
```

Le programme dont le résultat sera utilisé par *COPY FROM* sera [curl](https://curl.se) et un appel à l'API de Central.
Les données reçues seront toujours du JSON, que nous savons maintenant exploiter.

Restait à automatiser le tout pour ne pas devoir tout refaire à chaque nouveau formulaire.

Voici les étapes du processus imaginé :

* Interroger l'API de Central au sujet d'un formulaire donné pour connaitre les tables qui le composent
* Récupérer via l'API les données disponibles pour chacune de ces tables
* Créer **automatiquement** les tables de destination dans PostgreSQL
* Lancer cette tâche à intervalle régulier pour récupérer rapidement en base, les données du terrain (30' actuellement) et les mettre à disposition dans nos outils

Deux ressources ont été déterminantes :

* [Static and dynamic pivots](https://postgresql.verite.pro/blog/2018/06/19/crosstab-pivot.html) par Daniel Verité
* [INSERT INTO from refcursor](https://stackoverflow.com/questions/50837548/insert-into-fetch-all-from-cant-be-compiled/52889381#52889381) par Evgeny Nozdrev

Quelques adaptations de ces travaux nous ont permis d'aboutir à une méthode générique et automatique et à la première version d'une "bibliothèque" de fonctions pl/pgsql nommée [central2pg](https://github.com/mathieubossaert/central2pg) présentée ici : <https://forum.getodk.org/t/postgresql-set-of-functions-to-get-data-from-central/33350>.

Ce simple appel de fonction :

```sql
SELECT odk_central.odk_central_to_pg(
 'me@mydomain.org',   -- user
 'PassW0rd',    -- password
 'my_central_server.org',  -- central FQDN
 2,      -- the project id,
 'my_form_about_birds',   -- form ID
 'odk_data',    -- schema where to create tables and store data
 'point_auto,point,ligne,polygone' -- columns to ignore in json transformation to database attributes (like geojson fields of GeoWidgets)
);
```

réalise ceci :

* demande à Central la liste des tables qui constituent le formulaire "my_form_about_birds"
* récupère les données pour chaque table
* crée les tables dans le schéma odk_data de la base de données, un attribut par question de formulaire
* le dernier paramètre permet de mentionner les questions à ignorer lors de la transformation récursive des objets json en attributs SQL (par exemple les champs geojson que l'on souhaite conserver en l'état)
* alimente les tables créées avec les données reçues

Et à l'appel suivant (tâche planifiée avec cron) :

* vérifie la présence de nouvelles questions dans le formulaire
* crée les attributs correspondants le cas échéant
* insère les nouvelles données (celles non encore intégrées)

----

## Perspectives

### Concernant [central2pg](https://github.com/mathieubossaert/central2pg)

Toutes les données colléctées depuis ce printemps à travers une dizaine de formulaires ont été moissonnées automatiquement grâce aux fonctions décrites ici.

Les premiers retours de la communauté sur [central2pg](https://github.com/mathieubossaert/central2pg) sont encourageants et l'utilisation des fonctions développées dans d'autres contextes permettront sans doute de trouver et corriger des bugs, ainsi que d'améliorer la généricité des fonctions (url du serveur, colonne à utiliser en clé primaire)

### Concernant ODK Collect, les formulaires et les "workflow"

La gestion de campagnes d'enquêtes complexes, non "linéaires" et l'amélioration des fonctionnalités cartographiques sont des sujets discutés actuellement au sein du [TAB et de l'équipe](2021-06-08_odk_postgis_1.md#gouvernance-et-communaute).

Nous n'entrons pas dans les détails ici mais voici quelques discussions sur le forum d'ODK :

* [faciliter la collecte de données basée sur des entités (traduction litérale)](https://forum.getodk.org/t/entity-based-data-capture-workflow-site-based-survey-with-opportunistic-encounters/33353)
* [pouvoir interagir avec la couche vecteur utilisée en référence](https://forum.getodk.org/t/selecting-a-map-feature-to-collect-data-about/28466/15)
* et les [cas d'utilisations listés par Daniel Joseph](https://docs.google.com/document/d/18ICz7gziV-8uiwy_lMDQ5PM_dD_fBmlcJKG_UJsMNUA/edit#heading=h.sil54e9hyeu) (aka [danbjoseph](https://forum.getodk.org/u/danbjoseph/summary) ), membre tu TAB qui déploie ODK à la Croix Rouge Internationale

Depuis cet été, ODK Collect peut se connecter à différents projets hébergés sur différents serveurs, ce qui permet par exemple à un salarié du CEN de participer à une étude portée et hébergée par une autre structure.

### Concernant Central

En mai est sortie la version 1.2 de Central, avec de nouvelles fonctionnalités de gestion des utilisateurs et des projets, des données reçues... mais aussi, coté API, la possibilité de récupérer les données "jointes" avec l'option [$expand](https://forum.getodk.org/t/extend-api-to-retrieve-plain-json/32204) de l'API et l'espoir de pouvoir ne demander à Central que les données récentes.
Cette amélioration, répond en théorie à notre envie de ne rapatrier que les données récemment acquises, mais il s'avère que le json reçu est beaucoup plus difficile à exploiter de manière générique.

La possibilité de filtrer les données par date de soumission ne s'applique pour l'instant qu'à la table "Submissions" et non aux tables sous-jacentes dont nous devons récupérer l'ensemble des données.
Cela ne pose pas de souci fonctionnel mais entraîne inutilement des flux de données toujours croissant, contenant des données déjà intégrées.
Une [demande de fonctionnalité](https://forum.getodk.org/t/propagate-submission-date-to-child-tables/34349) a été faite pour que la date de soumission des données soit propagée aux tables filles et utilisable dans les filtres.

Les fonctionnalités futures d'ODK Central sont listées ici, ainsi que celles déjà supportées et celles qui ne le seront jamais : <https://forum.getodk.org/t/whats-coming-in-central-over-the-next-few-years/19677proposées> ou prévues pour les prochaines années.

----

## Conclusion

ODK est devenu un outil essentiel au sein de notre SI. Les raisons principales sont les suivantes :

* la solution s'intègre très facilement dans notre SI bâti sur PostgreSQL, c'était le cas avec Aggregate et ça l'est toujours avec Central et son API OData,
* nous n'avons pas à développer d'application mobile dédiée à chaque protocole. Quand bien même nous le pourrions, quel sens cela aurait-il ?
* nous pouvons à la place prendre le temps de transposer nos protocoles de collecte de données dans [XLSForm] pour en faire des formulaires efficaces servis par une application robuste.
* une connaissance minimale est nécessaire pour créer un formulaire. Si vous connaissez votre protocole, vous pouvez le transposer en [XLSform], dans les limites (régulièrement repoussées) des possibilités d'ODK.
* la facilité d'adaptation de formulaires existant pour de nouveaux besoins
* la facilité de partage et d'adaptation de ces formulaires à d'autres protocoles
* et peut-être avant tout sa communauté d'utilisateurs et de développeurs

----

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-sa.md" %}

## Crédits

* icône [XML](https://thenounproject.com/term/xml/3148395) de Eucalyp from the Noun Project
* icône [JSON](https://openclipart.org/detail/188447/developers-openclipart-has-a-json-api)

<!-- Hyperlinks reference -->
[XLSForm]: https://xlsform.org/en/
