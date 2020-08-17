---
authors: "Julien Moura"
categories: ["tutoriel"]
date: 2020-08-14 11:11
description: "A l'instar de nombreux autres sites web, celui de Geotribu est un site statique. Mais c'est quoi exactement ?"
hero: "Publier facilement sur internet : l'ère des sites statiques."
tags: site web,geotribu,site statique,static website,mkdocs,hugo,markdown
title: "Publier un site web statique"
---

# Publier un site web : l'avènement des sites statiques

:calendar: Date de publication initiale : 14 août 2020

**Mots-clés :** web | astuces | Geotribu | contribution

## Intro

Dans le cadre de mon intervention dans le [CQP GEOM](https://www.idgeo.fr/formation/cqp-geom-geomaticien-developpeur-dapplications-spatiales/) propulsé par [IDGEO](https://www.idgeo.fr/) le mois dernier, on m'a demandé de faire un retour d'expérience sur Geotribu et plus largement d'initier les participant/es à la contribution à l'écosystème, notamment sous la forme de blogs ou autre.

Après de grandes envolées théoriques mais non moins lyriques sur l'intérêt de partager, celui d'apporter ~~sa pierre~~ son caillou à l'édifice de son écosystème professionnel au risque/bénéfice de s'exposer "publiquement", les enjeux du délicat équilibre à trouver en termes d'investissement personnel bénévole, les dangers de faire des phrases trop longues, nous sommes passés aux travaux pratiques : comment publier un blog.

Dès lors, des étudiants

Avez-vous besoin d'un service d'authentification intégré (gestion des utilisateurs et des accès) ?
Avez-vous besoin d'une interface d'édition très complète ?

Exemples : documentations techniques, *landing pages*, événements (FOSS4G-FR), présentation de logiciel (GRASS)...

## C'est quoi un site statique

### Historique

En entendant "site statique", on peut avoir l'impression de revenir en arrière. Après tout, n'avons-nous pas passé ces deux dernières décennies à contextualiser, à dynamiser tout ce qui avait trait au web (Ajax, API, WebSocket...) ?

Mais attention,

rst -> markdown
sphinx

### Définition

Pas de base de données, pas de requêtes externes (même si...).
En résumé, ce que l'on appelle un site statique, ça n'est ni plus ni moins qu'un dossier avec du HTML, du CSS et du JS, accessible depuis un serveur de type HTTP (web). Le tout s'ouvre sur n'importe quel serveur web ou même un  navigateur.

Principaux intérêts :

- légèreté et donc performant
- interopérable
- portabilité du contenu
- sécurisation peu stressante

### Toi aussi, déploie le site Geotribu chez toi

Pour mieux se rendre compte de la légèreté et de la facilité qu'occasionnent les sites statiques, déployons le site actuel de Geotribu en 3 étapes.

1. Télécharger [la dernière version du site en production](https://github.com/geotribu/website/archive/gh-pages.zip)
2. Dézipper, lancer le fichier `website-gh-pages/index.html` et voir apparaître la page d'accueil dans son navigateur par défaut.

Mais le site ayant été configuré pour avoir des URL correspondant au titre sans l'extension `.html`, la navigation n'est donc pas fonctionnelle, le [navigateur se comportant davantage comme un explorateur de fichiers](https://developer.mozilla.org/fr/docs/Apprendre/Ouvrir_un_fichier_dans_un_navigateur_web#Ouvrir_un_fichier_local).

Si on veut avoir le site pleinement fonctionnel, il suffit de servir le dossier par un serveur web. On peut aussi utiliser les serveurs webs minimalistes intégrés à de nombreux langages :

=== "Python (3)"

    ```bash
    # se placer dans le dossier où vous avez téléchargé le site. Exemple :
    cd ~/downloads/website-gh-pages

    # lancer un serveur web minimaliste. Exemple avec Python 3 :
    python -m http.server 8085
    ```

=== "Node (12)"

    ```bash
    # se placer dans le dossier où vous avez téléchargé le site. Exemple :
    cd ~/downloads/website-gh-pages

    # lancer un serveur web minimaliste. Exemple avec Python 3 :
    npx serve -l 8085
    ```

Ouvrir le navigateur sur l'adresse <http://localhost:8085> et vous devriez avoir le site en local, pleinement fonctionnel.

### Les 90, c'est so 2020

![Vintage, pas vieux](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/pas_vieux_mais_vintage.png "Je ne suis pas vieux, je suis vintage"){: .img-rdp-news-thumb loading=lazy }

A l'instar du goût éternellement renouvelé pour le vintage, le site statique est de nouveau _hype_ aujourd'hui. Un truc de hipster en somme.

A chaque langage ou framework de développement, son ou ses moteur/s de génération de site statique :

- Go : Hugo - la star, le hit de l'été qui "tue" le game (en ce moment)
- JavaScript : NextJS (et son pendant now.sh), Gatsby, Vue Press, Gitbook
- PHP : Jigsaw
- Python : Sphinx, MkDocs, Pelican

Pour mieux vous rendre compte ou faire votre propre choix, je vous recommande le site [StaticGen](https://www.staticgen.com/) qui classe les différentes technologies selon leur "popularité" ou taux d'utilisation dans les dépôts de code ouverts :

![StaticGen capture](https://cdn.geotribu.fr/img/tuto/static_web/static_gen_picker.png "StaticGen - Sélecteur de générateur de site statique"){: loading=lazy }

Autre signe que tout cela a le vent en poupe, c'est qu'au-delà des moteurs, l'écosystème s'épaissit rapidement, des briques ou services proposant de s'affranchir facilement des limitations du site statique... en promettant d'y inclure facilement du dynamique :zany_face:.

Quelques exemples parmi les plus connus :

- [Netlify](https://www.netlify.com/) : la plateforme complète de services dédiés aux sites statiques : test, pré-déploiement, déploiement, optimisation des images, vérification des liens, formulaires de contact, etc.
- [Forestry](https://forestry.io/) : un CMS dédié aux sites statiques et basé sur les git workflows
- [StaticMan](https://staticman.net/) : ajoute un micro-service sous forme d'API intermédiaire pour, par exemple, ajouter un système de commentaires.
- [_Object Storage as a Static Web Server as a Service_ ou _OSaaSWSaaS_](https://en.wikipedia.org/wiki/Object_storage) : tous les services de cloud permettent d'utiliser leurs services de stockage objet sous forme d'un mini serveur web de fichiers statiques : Amazon, Azure, CloudFlare, Google, Scaleway (qui vient de racheter OpenIO), etc. Oh et pour l'acronyme, c'est une blague, je viens de l'inventer :grin: !

### La joie de la configuration

Si les sites statiques épargnent 75% l'effort de développement, de maintenance et de sécurisation du site web, il reste trois principaux postes de dépense :

- la rédaction bien sûr :
- le design : même si la plupart des templates sont suffisamment bien
- la configuration :




<https://html5up.net/>



----

## Le cas Geotribu

### Enjeu : la séparation des pouvoirs

> TO COMPLETE


### Jouer avec les thèmes de MkDocs

Le contenu étant décorrelé du style  thème à appliquer, on peut alors

> TO COMPLETE

#### Read the Docs

Intégré par défaut dans MkDocs, on peut par exemple rendre le contenu dans le style du site Read The Docs qui est une plateforme d'hébergement de documentations techniques (QGIS, GDAL...), historiquement axé sur Sphinx (qu'il est d'ailleurs toujours possible d'utiliser)

```powershell
mkdocs serve -t readthedocs
```

![Geotribu - Read the Docs](https://cdn.geotribu.fr/img/tuto/static_web/static_theming_geotribu_rtd.png "Geotribu avec le thème Read the Docs"){: loading=lazy }

#### Terminal

On peut aussi trouver des thèmes plus loufoques. Par exemple, si on souhaite s'adresser aux geeks nostalgiques, on optera pour le thème [bootstrap386](https://gitlab.com/lramage/mkdocs-bootstrap386) :

```powershell
pip install mkdocs-bootstrap386
mkdocs serve -t bootstrap386
```

![Geotribu - Vintage terminal](https://cdn.geotribu.fr/img/tuto/static_web/static_theming_geotribu_dos386.png "Geotribu avec le thème DOS i386"){: loading=lazy }

Il y a même le curseur qui parcourt les lignes, donnant un petit côté Minitel !

### Jouer avec d'autres générateurs

#### Hugo

Parmi les générateurs de sites statiques les plus utilisés, Hugo est l'un des plus côtés récemment. Développé en Go, les performances

```powershell
hugo new site geotribu_hugo
cd geotribu_hugo
git init
git submodule add https://github.com/jpescador/hugo-future-imperfect.git themes/hugo-future-imperfect
```

![Geotribu - Hugo](https://cdn.geotribu.fr/img/tuto/static_web/static_theming_geotribu_hugo_future_imperfect.png "Geotribu avec le thème Future Imperfect du moteur Hugo"){: loading=lazy }


----

## Déployer

## Localement

> TO COMPLETE

## Sur internet : mettre à profit les

> TO COMPLETE

![Déploiement sur GitHub](https://cdn.geotribu.fr/img/tuto/static_web/static_deploy_ci-cd_github.png "Notification GitHub confirmant le déploiement"){: loading=lazy }

----

## Auteur

--8<--
content/team/jmou.md
--8<--

<!-- Hyperlinks reference -->
[Git]: https://git-scm.com/
[ISE]: https://docs.microsoft.com/fr-fr/powershell/scripting/windows-powershell/ise/introducing-the-windows-powershell-ise
[OSGeo4W]: https://trac.osgeo.org/osgeo4w/wiki/OSGeo4W_fr
