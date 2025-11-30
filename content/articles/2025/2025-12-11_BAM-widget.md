---
title: "BAM (Biodiversité Autour de Moi)"
subtitle: Les données ouvertes de biodiversité accessibles facilement à tous, partout !
authors:
    - Camille MONCHICOURT
categories:
    - article
comments: true
date: 2025-12-11
description: "Un nouveau widget de biodiversité pour afficher les espèces observées autour d'un lieu."
icon: "material/bee-flower"
image: "https://geonature.fr/documents/autres/BAM/BAM-widget-thumb.png"
license: cc4_by-sa
robots: index, follow
tags:
    - Biodiversité
    - OpenSource
    - Widget
---

# BAM (Biodiversité Autour de Moi), les données ouvertes de biodiversité accessibles facilement à tous, partout !

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![BAM widget](https://geonature.fr/documents/autres/BAM/BAM-logo.png "BAM widget"){: .img-thumbnail-left }

**Un nouveau widget de biodiversité, libre, développé par les parcs nationaux français et reconnu internationalement, pour afficher les espèces observées autour d'un lieu.**

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

Au Parc national des Écrins et au Parc national des Cévennes, on aime la géomatique open source, les bases de données 🐘 et l'open data !
Ces 10 dernières années, nous avons notamment développé 2 systèmes d'information open source :

- [Geotrek](https://geotrek.fr) pour gérer et valoriser les sentiers,
- [GeoNature](https://geonature.fr) pour collecter, gérer et diffuser des données de biodiversité.

Ces deux outils sont désormais utilisés par plus de 250 structures en France. Et plusieurs membres de leurs communautés souhaitaient pouvoir connecter GeoNature et Geotrek en faisant remonter les espèces observées autour d'une rando.

Plutôt que de développer un composant ou un module spécifique à nos outils, nous avons réfléchi à une solution plus globale et générique. Ainsi, avec Amandine Sahl du Parc national des Cévennes, nous avons envisagé une approche pouvant s’adapter à différents contextes et à diverses sources de données.

Ces dernières années, les données ouvertes sur la biodiversité se sont en effet multipliées grâce aux programmes participatifs internationaux
([iNaturalist](https://www.inaturalist.org/), [Pl@ntNet](https://plantnet.org/), [eBird](https://ebird.org/)…), aux naturalistes professionnels ou amateurs,
et aux plateformes nationales comme l'[INPN](https://inpn.mnhn.fr/). Mais, elles ne sont pas facilement accessibles au plus grand nombre.

Nous voulions donc que n'importe qui puisse afficher et intégrer dans son site, en quelques clics, la liste des espèces observées autour d’un gîte, d’un sentier, d'un événement ou encore d'une école.

C’est ainsi qu'est né l'outil [BAM – Biodiversité Autour de Moi](https://si.ecrins-parcnational.com/blog/2025-08-BAM-widget.html), dont nous avons initié le développement lors d'un workshop, fin 2024, avec plusieurs parcs nationaux français, coordonné par Amandine Sahl (Parc national des Cévennes) et Jacques Fize (Parc national des Écrins).

![BAM screenshot](https://github.com/user-attachments/assets/39ae6276-c95e-469d-8247-5ba781f76159)

## Comment fonctionne BAM ?

BAM se présente désormais comme un widget, prêt à être intégré sur une page web ou une application.

Il suffit de lui indiquer un lieu ou une zone de recherche pour que le widget affiche :

- le nom des espèces observées,
- leur dernière date d’observation,
- une photo,
- parfois même un enregistrement sonore.

Toutes ces informations viennent directement de grandes bases de données mondiales et ouvertes comme le [GBIF](https://www.gbif.org/fr/)  ou [Wikidata](https://www.wikidata.org/).
Elles peuvent également provenir de sources plus locales comme [GeoNature](https://geonature.fr/), avec une logique de connecteurs que l'on peut enrichir si l'on souhaite ajouter de nouvelles sources de données.

![Architecture BAM](https://github.com/user-attachments/assets/0adf126e-0219-49de-a8c0-7ef6c9b9e8c7)

L'outil n'a besoin d’aucune installation, ni de serveur, ni de base de données : Il récupère les observations collectées à jour en interrogeant les services exposés par des API.
Il fonctionne partout dans le monde, et est multilingue (Français 🇫🇷, Anglais 🇬🇧, Espagnol 🇪🇸, Italien 🇮🇹, Allemand 🇩🇪, et même Tchèque 🇨🇿 depuis la [contribution récente de Jiří Podhorecký](https://github.com/PnX-SI/BAM-widget/pull/83)).

Voici un exemple d'intégration du widget BAM, avec les espèces observées, dans un rayon de 200 m, autour de l'école forestière dans le Parc national du Banco à Abidjan  :

<iframe
        title="BAM - Parc national du Banco"
        width="100%" height="640" allow="geolocation"
        src="https://pnx-si.github.io/BAM-widget/#/?widgetType=mapList&nbTaxonPerLine=4&primaryColor=009485&switchModeAvailable=true&showFilters=true&lang=fr&buffer=200&x=-4.05224&y=5.38471"></iframe>

```html title="Code source du widget à intégrer pour cet exemple"
<iframe
   title="BAM - Parc national du Banco"
   width="100%" height="640" allow="geolocation"
   src="https://pnx-si.github.io/BAM-widget/#/?widgetType=mapList&nbTaxonPerLine=4&primaryColor=009485&switchModeAvailable=true&showFilters=true&lang=fr&buffer=200&x=-4.05224&y=5.38471">
</iframe>
```

⚙️ Un [configurateur du widget](https://pnx-si.github.io/BAM-widget/#/config) est disponible pour faciliter le paramétrage du widget et son intégration. Définissez le lieu, le mode d'affichage et les options (carte et liste ou liste uniquement, mode galerie ou détaillé, nombre de résultats par ligne, affichage des filtres ou non, zone de recherche, source de données, couleur...) et BAM ! Vous n'avez plus qu'à copier-coller dans votre site les quelques lignes de l'iframe que vous retourne le configurateur.

Des parcs naturels et sentiers aux écoles, refuges de montagne, sites d'escalade, événements ou hébergements, nous espérons voir le widget BAM intégré dans un large éventail de sites,
éveillant curiosité et sensibilisation à la nature auprès de nouveaux publics.

Le Parc national des Cévennes l'a déjà intégré sur les fiches des randonnées de son portail [Geotrek-rando](https://destination.cevennes-parcnational.fr/trek/37990-Arboretum-de-l-Hort-de-Dieu) et différents exemples d'utilisation sont proposés dans le [Github de l'outil](https://github.com/PnX-SI/BAM-widget/tree/main/docs/examples).

🔍 BAM peut aussi être utilisé comme un explorateur de données de biodiversité autonome, adapté à un usage mobile et installable sous forme de PWA,
en se rendant directement sur <https://pnx-si.github.io/BAM-widget/>.

## Une reconnaissance internationale

Le 24 octobre 2025, à Bogota (Colombie), BAM a reçu un prix lors du [défi international Ebbe Nielsen](https://www.gbif.org/fr/news/2LugQxJfG2kCzjiJocXzVZ/des-laureats-de-norvege-et-daustralie-partagent-la-premiere-place-du-defi-ebbe-nielsen-2025),
organisé par le GBIF, qui récompense chaque année les meilleures applications utilisant les données ouvertes sur la biodiversité.

![L'équipe des parcs nationaux à l'origine de la réalisation du widget BAM](https://github.com/user-attachments/assets/caf93b35-e20b-4174-9448-2b072b062bae)

Une belle reconnaissance pour ce projet porté par nos équipes des parcs nationaux des Cévennes et des Écrins, déjà lauréates de ce défi en 2019 pour l’outil GeoNature-atlas.

Avec ce nouveau projet, nos 2 parcs nationaux continuent leur démarche commune de développement d’outils libres pour répondre à des besoins locaux et spécifiques de manière générique et globale,
initiée depuis un peu plus de 10 ans avec les projets mutualisés Geotrek et GeoNature.

## Pour aller plus loin

- [Tester l’outil BAM](https://pnx-si.github.io/BAM-widget/)
- [Accéder au configurateur de widget BAM](https://pnx-si.github.io/BAM-widget/#/config)
- [Documentation complète de BAM](https://pnx-si.github.io/BAM-widget/docs/#/)
- [Présentation générale de BAM](https://si.ecrins-parcnational.com/blog/2025-08-BAM-widget.html)
- [Code source de BAM](https://github.com/PnX-SI/BAM-widget)
- [Résultats du défi Ebbe Nielsen 2025](https://www.gbif.org/fr/news/2LugQxJfG2kCzjiJocXzVZ/des-laureats-de-norvege-et-daustralie-partagent-la-premiere-place-du-defi-ebbe-nielsen-2025)

----

<!-- geotribu:authors-block -->

{% include "licenses/cc4_by-sa.md" %}
