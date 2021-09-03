---
ltitle: "Open Data Kit pour la collecte de données géographiques dans PostGIS (3/3)"
authors: ["Mathieu BOSSAERT"]
categories: ["article"]
date: "2021-09-14 10:20"
description: "Troisième et dernier article de présentation de la suite Open Data Kit (ODK) et son intégration au SI du CEN d'Occitanie et dans les processus métiers."
image: "https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/odk_and_postgresql.png"
tags: "ODK,Open Data Kit,PostgreSQL,PostGIS,collecte,Android"
---


# ODK pour la collecte de données géo dans PostGIS (3/3)

:calendar: Date de publication initiale : 14 septembre 2021

**Mots-clés :** ODK | PostgresSQL | PostGIS | PL/pgSQL | Android

![ODK PostGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/Central2PG.png "ODK + PostGIS"){: .img-rdp-news-thumb }

## Troisième partie - Récupération des données dans notre SI

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

[1ère partie : Introduction à ODK :fontawesome-solid-fast-backward:](https://static.geotribu.fr/articles/2021/2021-06-08_odk_postgis_1/){: .md-button }
[2ème partie : Exemple de mise en œuvre au CEN :fontawesome-solid-step-backward:](https://static.geotribu.fr/articles/2021/2021-06-22_odk_postgis_2/){: .md-button }

## Différents silos possibles

Les données collectées avec les formulaires peuvent être envoyées à différents outils :

* Aggregate (EOL)
* Central (détaillé plus bas)
* [Google sheet](https://docs.getodk.org/collect-connect-google/)

ou récupérées directement sur le téléphone connecté à un ordinateur avec

* https://docs.getodk.org/briefcase-intro/

## Exploitation des données

Différentes solutions d'exploitation, d'analyse et de visualisation de données sont disponibles.

### Outils opensource

* R / [RuODK](https://github.com/ropensci/ruODK)
* QGIS -> [QRealtime](https://shivareddyiirs.github.io/QRealTime/)
* Redash : via l'API : https://forum.getodk.org/t/first-use-of-a-central-web-form-and-basic-restitution-with-redash/30334/4 ou à travers une BDD PostgreSQL intermédiaire
* PostgreSQL/PostGIS -> [Central2PG](https://forum.getodk.org/t/postgresql-set-of-functions-to-get-data-from-central/33350)

### Outils propriétaires

* Excel via l'API Odata
* Tableau
* Power BI
* [Google Data Studio](https://github.com/UDub-Impact/OData-Connector/issues)

## ODK Central
C'est la composante "seveur" de la suite ODK. Il remplace Aggregate, arrivé en fin de vie au printemps 2021.

ODK Central reçoit les données des téléphones sous forme de fichiers xml tout à fait lisibles, et de fichiers binaires pour les éventuels médias collectés.

Il les stocke et en assure la diffusion via une [API REST (OData)](https://odkcentral.docs.apiary.io/#).

Il assure en outre la gestion des formulaires (ébauches et versions successives) et des utilisateurs mobiles. Ces derniers ont accès à des *projets*, qui regroupent différents formulaires.
Lorsque le téléphone interroge le serveur pour savoir quels formulaires sont diponibles à la saisie ou quels formulaires ont été mis à jour, *Central* sait à quelle ressource l'utilisateur configuré sur ce téléphone a accès.
La configuration des téléphones des utilisateurs se fait simplement en scannant avec ODK Collect le QRCode proposé par Central pour cet utilisateur.
Les versions récentes de Central et d'ODK Collect permettent à un utilisateur de participer à plusieurs projets qui peuvent être hébergés sur différentes serveurs.

Voir la liste des fonctionnalités de Central dans la [documentation](https://docs.getodk.org/central-intro/#odk-central-features).

Comme Aggregate, Central s'appuie sur une base de données PostgreSQL.

## Intégration des données au SI(G) du CEN (BDD PostGIS)

Aggregate, qui était le serveur proposé avant Central, créait pour chaque formulaire qu'il servait des tables dédiées pour accueillir les données.
Une table pour les paramètres communs à chaque session et des tables filles pour chaque répétition. Cela se traduisait dans notre cas par une table **sicen_core**, une table **sicen_emplacments** et une table **sicen_observations** . Chaque enregistrement de la table des observations faisait référence à un enregistrement de la table des emplacements, et chaque emplacement faisait référence à un enregistrement de la table "racine".

Il était ainsi très facile d'exploiter les données consolidées dans Aggregate dans notre système d'information construit sur PostgreSQL, en utilisant les outils fournis par la base de données :
* triggers,
* vues,
* "Foreign Data Wrapper".

Central a quelque peu bouleversé nos habitudes car les formulaires ne sont plus "transposés" en tables dans la base de données, mais uniquement stockés en XML (comme le faisait aussi aggregate).

Diverses pistes d'exploitation des données ont été explorées pour conserver la fluidité que nous connaissions dans le cheminement de l'information, depuis ODK Collect vers nos outils métiers.
Elles ont été présentées [ici](https://forum.getodk.org/t/sql-first-try-to-get-central-data-into-internal-postgis-database/30102?u=mathieubossaert) sur le forum d'ODK.
Voici un petit résumé de ces essais et une présentation plus détaillée de la solution générique finalement mise en oeuvre.

### Utilisation des fonctions XML de PostgreSQL

La première idée explorée a consisté à exploiter les données XML de la table submission_defs avec les fonctions intégrées de PostgreSQL.
Cette méthode a été concluante puisque la vue suivante, présentée en détail [sur le forum d'ODK](https://forum.getodk.org/t/sql-first-try-to-get-central-data-into-internal-postgis-database/30102?u=mathieubossaert) peut être affichée dans QGIS :-)

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
            ....

```

Cette méthode d'accès aux données n'est cependant [pas conseillée, à juste titre, par l'équipe de développement](https://forum.getodk.org/t/sql-first-try-to-get-central-data-into-internal-postgis-database/30102/2?u=mathieubossaert) qui ne guarantit pas que le modèle de données n'évoluera pas dans le temps, contrairement à l'API qui est stable et normalisée.

Par ailleurs, l'exploitation du XML, bien que très efficace dans PostgreSQL n'est pas si "évidente que ça" pour qui, comme moi, n'exploite traditionnellement en SQL que des types de données non complexes.

### Utilisation de l'extension pgsql_http

Ne souhaitant pas passer par un outil tiers, de type ETL (Extract Transform and Load, [voir le travail décrit par Dave Henry avec Kettle](https://forum.getodk.org/t/automating-data-delivery-using-the-odata-endpoint-in-odk-central/22010)) pour réaliser cette tâche, une seconde voie a consisté à utiliser l'extension [pgsql_http](https://github.com/pramsey/pgsql-http) développée par Paul Ramsey. Cela m'a conforté dans l'idée que l'exploitation du json dans postgreSQL est beaucoup plus aisée que celle du xml.

Cette méthode est présentée [ici](https://forum.getodk.org/t/sql-first-try-to-get-central-data-into-internal-postgis-database/30102/6?u=mathieubossaert) .

L'extension permet de faire des appels à des ressources web et donc à l'API de Central. Le resultat de l'appel est un document Json.

On réalise un appel à l'API pour chaque "table" du formulaire et le tour est presque joué. Il ne reste qu'à exploiter le JSON avec les [fonctions JSON proposées par PostgreSQL](https://www.postgresql.org/docs/13/functions-json.html).

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
...
```

Cette voie est elle aussi concluante mais je vois avec le recul que je complexifiais la requête pour rien, par exemple en testant inutilement l'existence d'un élément avant de tenter d'y accéder.

### Utilisation de la commande COPY FROM...

Enfin au gré de mes recherches je me suis souvenu d'un article de [Leo Hsu et Regina Obe sur le "Postgres OnLine Journal"](https://www.postgresonline.com/journal/archives/325-Using-wget-directly-from-PostgreSQL-using-COPY-FROM-PROGRAM.html) au sujet d'une fonctionnalité de PostgreSQL 9.3 qui est de pouvoir passer à l'instruction COPY le résultat d'une commande système avec la syntaxe :

```sql
COPY FROM program...
```

Le programme dont le résultat sera utilisé par *COPY FROM* sera un appel [curl](https://curl.se) à l'API de Central.
Les données reçues seront toujours du JSON, que nous savons maintenant exploiter.

Restait à automatiser le tout pour ne pas devoir tout refaire à chaque nouveau formulaire.

L'idée générale était la suivante :

- Interroger l'API de Central au sujet d'un formualire donné pour connaitre les tables qui le composent
- Récupérer via l'API les données disponibles pour chacune de ces tables
- Créer **automatiquement** les tables de destination dans PostgreSQL
- Lancer cette tâche à intervalle régulier pour récupérer rapidement en base, les données du terrain (30' actuellement) et les mettre à disposition dans nos outils

Deux ressources ont été déterminantes :

- https://postgresql.verite.pro/blog/2018/06/19/crosstab-pivot.html par Daniel Verité
- https://stackoverflow.com/questions/50837548/insert-into-fetch-all-from-cant-be-compiled/52889381#52889381 par Evgeny Nozdrev

Quelques adaptations de ces travaux nous ont permis d'aboutir à une méthode générique et automatique et à la première version d'une "bibliothèque" de fonctions pl/pgsql nommée [central2pg](https://github.com/mathieubossaert/central2pg) présentée ici : https://forum.getodk.org/t/postgresql-set-of-functions-to-get-data-from-central/33350

Ce simple appel de function :

```sql
SELECT odk_central.odk_central_to_pg(
	'me@mydomain.org',			-- user
	'PassW0rd',				-- password
	'my_central_server.org',		-- central FQDN
	2, 					-- the project id,
	'my_form_about_birds',			-- form ID
	'odk_data',				-- schema where to creta tables and store data
	'point_auto,point,ligne,polygone'	-- columns to ignore in json transformation to database attributes (geojson fields of GeoWidgets)
);
```

réalise ceci :

* demande à Central la liste des tables qui constituent le formulaire "my_form_about_birds"
* récupère les données pour chaque table
* crée les tables dans le schéma odk_data de la base de données, un attribut par question de formulaire
* le dernier paramètre permet de mentionner les questions à ignorer lors de la transformation récursive des objets json en attributs SQL
* alimente les tables créées avec les données reçues

Et à l'appel suivant (tâche cron) :

* vérifie la présence de nouvelles questions dans le formulaire
* crée les attributs correspondants le cas échéant
* insert les nouvelles données

## Perspectives

### Concernant ODK Collect, les formulaires et les "workflow"

La gestion de campagne d'enquêtes complexes, non "linéaires" et l'amélioration des fonctionnalités cartographiques sont des sujets discutés actuellement au sein du TAB et de l'équipe.

Nous n'entrons pas dans les détails ici mais voici quelques discussions sur le forum d'ODK :

- [faciliter la collecte de données basée sur des entités (traduction litérale)](https://forum.getodk.org/t/entity-based-data-capture-workflow-site-based-survey-with-opportunistic-encounters/33353)
- [pouvoir interragir avec la couche vecteur utilisée en référence](https://forum.getodk.org/t/selecting-a-map-feature-to-collect-data-about/28466/15)
- et les [cas d'utilistaions listés par Daniel Joseph](https://docs.google.com/document/d/18ICz7gziV-8uiwy_lMDQ5PM_dD_fBmlcJKG_UJsMNUA/edit#heading=h.sil54e9hyeu) (aka [danbjoseph](https://forum.getodk.org/u/danbjoseph/summary) ), membre tu TAB qui déploie ODK à la Croix Rouge Internationale 

### Concernant Central

En mai est sortie la version 1.2 de Central, avec de nouvelles fonctionnalités de gestion des utilisateurs et des projets, des données reçues... mais aussi, coté API, la possibilité de récupérer les données "jointes" avec [l'option $expand](https://forum.getodk.org/t/extend-api-to-retrieve-plain-json/32204) et l'espoir de pouvoir ne demander à Central que les données récentes.
Cette amélioration, répond en théorie à notre envie de ne rapatrier que les données récemment acquises, mais il s'avère que le json reçu est beaucoup plus difficile à exploiter de manière générique.

La possibilité de filtrer les données par date de soumission ne s'applique pour l'instant qu'à la table "Submissions" et non aux tables sous-jacentes dont nous devons récupérer l'ensemble des données.
Cela ne pose pas de souci fonctionnel mais entraîne inutilement des flux de données au volume toujours croissant pour les tables secondaires (les emplacements et les observations dans notre exemple) qui sont en outre par définition les plus volumineuses.
Une [demande de fonctionnalité](https://forum.getodk.org/t/propagate-submission-date-to-child-tables/34349) a été faite pour que la date de soumission des données soit propagée aux tables filles et utilisable dans les filtres.

Les fonctionnalités futures d'ODK Central sont listées ici, ainsi que celles déjà supportées et celles qui ne le seront jamais : https://forum.getodk.org/t/whats-coming-in-central-over-the-next-few-years/19677proposées ou prévues pour les prochaines années 

## Conclusion
ODK est devenu un outil essentiel au sein de notre SI. Les raisons principales sont :

- la solution s'intègre très facilement dans notre SI bâti sur PostgreSQL, c'était le cas avec Aggregate et ça l'est toujours avec Central et son API OData,
- nous n'avons pas à développer d'application mobile dédiée à chaque protocole. Quand bien même nous le pourrions, quel sens cela aurait-il ?
- nous pouvons à la place prendre le temps de transposer nos protocoles de collecte de données dans XLSForm pour en faire des formulaires efficaces servis par une application robuste.
- une connaissance minimale est nécessaire pour créer un formulaire. Si vous connaissez votre protocole, vous pouvez le transposer en XLSform, dans les limites (régulièrement repoussées) des possibilités d'ODK.
- la faciliter d'adaptation de formulaires existant pour de nouveaux besoins
- la facilité de partage et d'adaptation de ces formulaires à d'autres protocoles
- et peut-être avant tout sa communauté d'utilisateurs et de développeurs

----

## Auteur

### Mathieu Bossaert

![Portrait Mathieu Bossaert](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/odk_postgis_collecte/mb.jpeg "Portrait Mathieu Bossaert"){: .img-rdp-news-thumb }

Aprés des études de biologie, d'écologie, et d'informatique, j'ai intégré le CEN en 2003 pour y occuper le poste de gestionnaire de bases de données, et suis devenu "géomaticien" par extension.

J'y suis désormais co-responsable de la "Geomateam" qui compte 5 personnes, pas toutes à temps plein sur la thématique, au sein d'une équipe "Occitane" de 80 salariés, répartis sur 14 sites.

PostgreSQL est le pilier structurant de notre SI depuis 2006. Les besoins de la structure ont évolué avec elle et chacun d'eux a trouvé une solution robuste dans le monde du libre et les communautés des différents outils, à travers [GeoRezo](https://georezo.net) notamment, n'ont jamais été avares de conseils.
J'ai intégré il y a quelques années l'équipe de GeoRezo et j'y assure la fonction de trésorier.

Enfin je contribue dans la mesure de mes compétences et de ma disponibilité aux forums techniques dédiés (principalement celui d'[ODK](https://forum.getodk.org))

Vous pouvez me contacter pour échanger sur le sujet via [twitter](https://twitter.com/MathieuBossaert) et [linkedin](https://www.linkedin.com/in/mathieu-bossaert-08b73a205/).

<!-- Hyperlinks reference -->

[Conservatoire d'Espaces Naturels d'Occitanie]: https://www.cen-occitanie.org
["blog" géomatique du CEN]: https://si.cen-occitanie.org
[GetODK]: https://getodk.org/
[XLSForm]: https://xlsform.org/en/

{% include "licenses/cc4_by-sa.md" %}
