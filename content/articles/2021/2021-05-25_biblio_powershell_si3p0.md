---
title: Aperçu de la bibliothèque PowerShell SI3P0
authors:
    - Michaël GALIEN
categories:
    - article
comments: true
date: 2021-05-25
description: Petit aperçu de la bibliothèque PowerShell SI3P0 développée par le département du Gard pour la gestion de son SIg routes et bâtiments.
icon: material/powershell
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/api_powershell_si3p0/apercu_SI3P0-logo.png
tags:
    - adresse
    - BAN
    - open source
    - PostGIS
    - PostgreSQL
    - PowerShell
    - SIG
    - SQL
---

# Aperçu de la bibliothèque PowerShell SI3P0

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

Pré-requis :

- une base de données PostgreSQL/PostGIS (v10.5/v.2.4)
- un client Windows qui :
    - permet l'exécution de scripts [PowerShell] (v.5.1)
    - dispose des outils clients PostgreSQL dont psql.exe
    - dispose de ogr2ogr.exe (GDAL v.2.4.1)

Les versions mentionnées sont celles que nous utilisons au [département du Gard]. Les versions antérieures ou ultérieures n'ont pas été testées, mais devraient fonctionner.

## Introduction

![Logo du département du Gard](https://cdn.geotribu.fr/img/logos-icones/entreprises_association/gard.jpg "Logo du département du Gard"){: .img-thumbnail-left }

Le [département du Gard] gère environ 4600 km de routes. Auparavant, le référentiel géographique de ces routes était tenu à jour manuellement sur la base de plans de récolement mais plus souvent suite à des remontées d'informations du terrain. De fait, la qualité du tracé, dépendante d'une ortho parfois ancienne, n'était pas toujours au rendez-vous.

Pour disposer d'un référentiel à jour, l'idée a été d'automatiser sa génération à partir de la BD TOPO® et de faire en sorte que cette génération soit facilement rejouable à chaque nouvelle livraison de l'[IGN](https://www.ign.fr/).

Les géo-traitements nécessaires à cette réalisation ont été faits avec PostgreSQL/PostGIS. Cependant, plusieurs étapes étaient requises et pour séquencer les différentes opérations nous avons commencé à rédiger des scripts [PowerShell]. Au fil du temps, les scripts sont devenus des fonctions, les fonctions sont devenues une bibliothèque plutôt “bancale” et, après pas mal d'efforts de renommage, redécoupage, refactoring, etc., la bibliothèque s'est transformée en quelque chose de propre et réutilisable (du moins, c'est ce qu'on croit :thinking:).

Pour faire la promotion de ces travaux au sein de la collectivité, nous avons décidé de "personnifier" le SIg que nous développons. Le nom retenu est SI3P0 (pour Système d'Information 3 Point 0) pour le côté "geek" de sa consonance et en lien avec le logo 3.0 du Gard qui fait référence au code officiel géographique du département.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Utilisation de la bibliothèque

![logo PowerShell](https://cdn.geotribu.fr/img/logos-icones/programmation/powershell.png "logo PowerShell"){: .img-thumbnail-left }

La bibliothèque est constituée de fichiers de scripts (extension `.ps1`). Autrement dit, nous n'avons pas construit de module PowerShell (extension `.psm1`).

Pour utiliser la bibliothèque, il te faut donc télécharger les différents scripts et définir plusieurs constantes propres à ton contexte de travail. Il suffit ensuite d'inclure la bibliothèque au script en cours de rédaction suivant [le principe du Dot-Sourcing](https://mcpmag.com/articles/2017/02/02/exploring-dot-sourcing-in-powershell.aspx).

Les étapes sont détaillées sur [les pages GitHub du projet](https://cd30-devil.github.io/SI3P0/) mais, avant de t'y rendre, tu trouveras ci-dessous un petit aperçu.

----

## Les fonctions

La bibliothèque propose plusieurs fonctions classiquement nécessaires pour gérer un SIg construit sur PostgreSQL/PostGIS. Nous l'utilisons pour traiter différentes thématiques (BAN, Cadastre, 3V - Véloroutes et Voies Vertes, etc.) et l'enrichissons chaque fois que de nouveaux besoins apparaissent. Le MindMap ci-dessous liste les fonctions disponibles au moment de la rédaction de cet article.

![Liste des fonctions de la bibliothèque SI3P0](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/api_powershell_si3p0/apercu_SI3P0-MindMap_fonctions.png "Liste des fonctions de la bibliothèque SI3P0"){: loading=lazy }
{: align=middle }

----

## Cas d'usage : traitement automatisé de la BAN

En guise de démo, le script qui suit te montre comment télécharger la BAN[^ban] au format CSV d'un département et la transformer en un fichier GeoJSON + SHP par commune.

### Détails sur le fonctionnement du script

Le script débute par l'import de la bibliothèque par Dot-Sourcing du fichier [api_complète.ps1](https://github.com/CD30-Devil/SI3P0/blob/main/API/PowerShell/api_compl%C3%A8te.ps1). Quelques variables, utiles dans la suite du script, sont également déclarées.

```powershell
# import de la bibliothèque SI3P0
. ("$PSScriptRoot\..\API\PowerShell\api_complète.ps1")

# le COG du département à traiter
$departement = '30'

# chemins de travail
$dossierDonnees = "$PSScriptRoot\Données"
$dossierRapports = "$PSScriptRoot\Rapports"
```

Vient ensuite une phase de nettoyage préalable qui permet de remettre le contexte au propre. Il y est notamment question de supprimer des tables grâce à la fonction `SIg-Effacer-Table` (cf. fichier [sig_défaut.ps1](https://github.com/CD30-Devil/SI3P0/blob/main/API/PowerShell/sig_d%C3%A9faut.ps1)) qui envoie à la base une commande `drop table if exists`.

```powershell
# effacement des rapports
Remove-Item "$dossierRapports\*.txt"
Remove-Item "$dossierRapports\*.err"

# effacement des données
Remove-Item "$dossierDonnees\*" -Recurse -Force

# effacement des tables
SIg-Effacer-Table `
    -table 'BAN_CSV' `
    -sortie "$dossierRapports\$(Get-Date -Format 'yyyy-MM-dd HH-mm-ss') - effacement BAN_CSV.txt"

SIg-Effacer-Table `
    -table 'BAN_Geo' `
    -sortie "$dossierRapports\$(Get-Date -Format 'yyyy-MM-dd HH-mm-ss') - effacement BAN_Geo.txt"
```

Le téléchargement du fichier BAN[^ban] du département depuis <https://adresse.data.gouv.fr> et son extraction sont faits respectivement grâce aux fonctions `Telecharger` (cf. fichier [fonctions_web.ps1](https://github.com/CD30-Devil/SI3P0/blob/main/API/PowerShell/fonctions_web.ps1)) et `DeGZipper` (cf. fichier [fonctions_archives.ps1](https://github.com/CD30-Devil/SI3P0/blob/main/API/PowerShell/fonctions_archives.ps1)).

```powershell
# téléchargement...
Telecharger `
    -url "https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-$departement.csv.gz" `
    -enregistrerSous "$dossierDonnees\adresses-$departement.csv.gz"

#  ...et extraction de la BAN
DeGZipper `
    -archive "$dossierDonnees\adresses-$departement.csv.gz" `
    -extraireVers $dossierDonnees
```

Il est alors question d'importer le fichier BAN dans la base de données.

Pour cela, une table, dont les colonnes correspondent à celles du fichier CSV, est construite grâce à la fonction `SIg-Creer-Table-Temp` (cf. fichier [sig_défaut.ps1](https://github.com/CD30-Devil/SI3P0/blob/main/API/PowerShell/sig_d%C3%A9faut.ps1)). Cette dernière crée une table non tracée (`unlogged`) constituée de colonnes de type `text`.

Le CSV y est importé par appel à la fonction `SIg-Importer-CSV` (cf. fichier [sig_défaut.ps1](https://github.com/CD30-Devil/SI3P0/blob/main/API/PowerShell/sig_d%C3%A9faut.ps1)).

```powershell
# création d'une table temporaire pour l'import du CSV
SIg-Creer-Table-Temp `
    -table 'BAN_CSV' `
    -colonnes `
        'id', `
        'id_fantoir', `
        'numero', `
        'rep', `
        'nom_voie', `
        'code_postal', `
        'code_insee', `
        'nom_commune', `
        'code_insee_ancienne_commune', `
        'nom_ancienne_commune', `
        'x', `
        'y', `
        'lon', `
        'lat', `
        'alias', `
        'nom_ld', `
        'libelle_acheminement', `
        'nom_afnor', `
        'source_position', `
        'source_nom_voie' `
    -sortie "$dossierRapports\$(Get-Date -Format 'yyyy-MM-dd HH-mm-ss') - création BAN_CSV.txt"

# import du CSV
SIg-Importer-CSV `
    -table 'BAN_CSV' `
    -csv "$dossierDonnees\adresses-$departement.csv" `
    -sortie "$dossierRapports\$(Get-Date -Format 'yyyy-MM-dd HH-mm-ss') - import adresses-$departement.csv.txt"
```

La conversion de la table temporaire en table géographique est faite par exécution d'une requête SQL de typage et de transformation. Cette requête est envoyée à PostgreSQL/PostGIS via la fonction `SIg-Executer-Commande` (cf. fichier [sig_défaut.ps1](https://github.com/CD30-Devil/SI3P0/blob/main/API/PowerShell/sig_d%C3%A9faut.ps1)).

```powershell
# transformation de la table "CSV" en table géographique
SIg-Executer-Commande -commande @'
create table BAN_Geo as
select
    id::varchar,
    id_fantoir::varchar,
    numero::integer,
    rep::varchar,
    nom_voie::varchar,
    code_postal::varchar,
    code_insee::varchar,
    nom_commune::varchar,
    code_insee_ancienne_commune::varchar,
    nom_ancienne_commune::varchar,
    libelle_acheminement::varchar,
    nom_afnor::varchar,
    source_position::varchar,
    source_nom_voie::varchar,
    ST_SetSRID(ST_MakePoint(x::numeric, y::numeric), 2154) as geom
from BAN_CSV;
'@
```

A ce stade, la base de données stocke la table géographique Lambert-93 de l'ensemble des adresses du département.

Pour la phase d'extraction, la liste des communes est déterminée par requête SQL et est sauvegardée dans un fichier. Le résultat est parcouru pour paramétrer deux processus d'extraction par commune (1 pour le GeoJSON + 1 pour le SHP) grâce aux fonctions `Parametrer-Job-SIg-Exporter-GeoJSON` et `Parametrer-Job-SIg-Exporter-SHP` (cf. fichier [sig_défaut.ps1](https://github.com/CD30-Devil/SI3P0/blob/main/API/PowerShell/sig_d%C3%A9faut.ps1)).

Les extractions sont enfin lancées grâce à la fonction `Executer-Jobs` (cf. fichier [fonctions_jobs.ps1](https://github.com/CD30-Devil/SI3P0/blob/main/API/PowerShell/fonctions_jobs.ps1)) qui, par défaut, exécute en parallèle un nombre de processus égal au nombre de cœurs de la machine - 1.

```powershell
# recherche de la liste des communes
# passage par un fichier intermédiaire (pas mieux pour l'instant via la bibliothèque)
SIg-Executer-Commande `
    -commande 'select distinct code_insee from BAN_Geo' `
    -sortie "$dossierRapports\cog_communes.txt" `
    -erreur $false `
    -autresParams '--tuples-only', '--no-align'


# paramétrage des jobs d'export (1 GeoJSON + 1 SHP par commune)
$parametresJobs = [System.Collections.ArrayList]::new()

foreach ($cog_commune in (Get-Content "$dossierRapports\cog_communes.txt")) {

    # job d'export GeoJSON
    [void]$parametresJobs.Add(
        (Parametrer-Job-SIg-Exporter-GeoJSON `
            -requete "select * from BAN_Geo where code_insee = '$cog_commune'" `
            -geoJSON "$dossierDonnees\GeoJSON\BAN_$cog_commune.geojson")
    )

    # job d'export SHP
    [void]$parametresJobs.Add(
        (Parametrer-Job-SIg-Exporter-SHP `
            -requete "select * from BAN_Geo where code_insee = '$cog_commune'" `
            -shp "$dossierDonnees\SHP\BAN_$cog_commune.shp" `
            -compresser $true)
    )

}

# exécution des jobs
# s'il n'est pas spécifié, le nombre de jobs en // est égal au nombre de coeurs da la machine - 1
Executer-Jobs -parametresJobs $parametresJobs
```

A l'issue de l'export, la table temporaire est supprimée. La version géographique est quant à elle conservée dans la base PostgreSQL/PostGIS.

```powershell
# effacement de la table temporaire
SIg-Effacer-Table -table 'BAN_CSV' -sortie "$dossierRapports\$(Get-Date -Format 'yyyy-MM-dd HH-mm-ss') - effacement BAN_CSV.txt"
```

[Voir le script complet :fontawesome-regular-file-code:](https://github.com/CD30-Devil/SI3P0/blob/main/docs/Ressources/GeoTribu/2021-05-25_biblio_powershell_si3p0.ps1){: .md-button }
{: align=middle }

### Résultats obtenus

Après exécution du script, la table `BAN_Geo` est disponible dans la base SIg et les versions GeoJSON et SHP par commune sont accessibles dans le dossier de sortie.

Les données peuvent être visualisées dans ArqGIS :

![Visualisation du résultat d'exécution du script sous ArqGIS](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/api_powershell_si3p0/apercu_SI3P0-resultat_script.png "Visualisation du résultat d'exécution du script sous ArqGIS"){: loading=lazy }

----

## Pour aller plus loin

Comme indiqué plus haut, si tu souhaites récupérer les sources (sous licence [BSD-3](https://opensource.org/licenses/BSD-3-Clause)) et en savoir plus sur le paramétrage et le fonctionnement de la bibliothèque, il te faut aller sur [les pages GitHub du projet](https://cd30-devil.github.io/SI3P0/) à l'adresse suivante : [https://cd30-devil.github.io/SI3P0/](https://cd30-devil.github.io/SI3P0/)

----

<!-- geotribu:authors-block -->

!!! note "Pourquoi est-ce que j'écris SIg et pas SIG ?"
    Je traite au quotidien différentes données dont une partie est géographique. A ce titre, je considère que je participe à la construction du SI de la collectivité. Ce "G", s'il précise la composante géographique des travaux, apporte je trouve, un côté réducteur à la matière. J'ai donc opté pour ce compromis d'écriture.

<!-- Hyperlinks reference -->
[département du Gard]: https://www.gard.fr
[PowerShell]: https://fr.wikipedia.org/wiki/Windows_PowerShell

[^ban]: Base Adresse Nationale (voir <https://adresse.data.gouv.fr/>)
