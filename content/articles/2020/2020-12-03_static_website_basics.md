---
title: "Le retour du web statique"
authors: ["Julien MOURA"]
categories: ["article", "tutoriel"]
date: 2020-12-03 11:11
description: "A l'instar de nombreux autres sites web, celui de Geotribu est un site statique. Mais c'est quoi exactement ?"
image: ""
tags: geotribu,site statique,static website,mkdocs,hugo,markdown
---

# Publier un site web : l'avènement des sites statiques

:calendar: Date de publication initiale : 3 décembre 2020

**Mots-clés :** web | Geotribu | contribution

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

## Toi aussi, déploie le site Geotribu chez toi

Pour mieux se rendre compte de la légèreté et de la facilité des sites statiques, faisons un exercice simple de mise en pratique : **déployons le site actuel de Geotribu en 2 étapes**.

### Télécharger le site de production

Commençons par télécharger [la dernière version du site en production](https://github.com/geotribu/website/archive/gh-pages.zip) et dézipper le tout.

Pour les personnes facturées au clic sur les interfaces graphiques, voici la petite commande qui va bien :

<!-- markdownlint-disable MD046 -->
=== "Bash"

    ```bash
    cd /tmp \
        && wget -N -c https://github.com/geotribu/website/archive/gh-pages.zip -O geotribu_website_prod.zip \
        && unzip -o -q geotribu_website_prod.zip \
        && cd website-gh-pages \
        && nautilus .
    ```

=== "Powershell"

    ```powershell
    Set-Location -Path "$env:TEMP"; `
    Invoke-WebRequest -Uri "https://github.com/geotribu/website/archive/gh-pages.zip" -OutFile geotribu_website_prod.zip ;`
    Expand-Archive -Path geotribu_website_prod.zip -DestinationPath . -Force ;`
    cd website-gh-pages ;
    explorer .
    ```
<!-- markdownlint-enable MD046 -->

On peut déjà observer que le site ne pèse que ~25 Mo compressé et ~110 Mo décompressé, pour un contenu de presque 600 pages (articles, revues de presse, guides de contribution pages d'équipe, etc.). Et encore, le fichier d'index de la recherche (`search/search_index.json`) pèse à lui seul près de 50 Mo.

Evidemment, ce dossier ne contient pas les images, hébergées sur un [serveur à part](/contribuer/guides/image/#heberger-une-image-sur-le-cdn-de-geotribu) et sauvegardées mensuellement en tant que release sur GitHub. A titre d'exemple, [la sauvegarde de novembre pèse 422 Mo](https://github.com/geotribu/website/releases/download/2020.11/bkp_cdn_2020-11-11.tar.gz).

[![Fernand Léger - Les constructeurs](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/fernand_leger_constructeurs.jpg "Quand je vous disais que c'est Léger !"){: loading=lazy }](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/fernand_leger_constructeurs.jpg){: data-mediabox="lightbox-gallery" data-title="Quand je vous disais que c'est Léger !"}
{: align=middle }

### Servir le site

En ouvrant simplement le fichier `index.html`, on voit déjà apparaître la page d'accueil dans son navigateur par défaut. Mais le site étant configuré pour avoir des URLs correspondant au titre de la page sans l'extension `.html`, la navigation n'est donc pas fonctionnelle, le [navigateur se comportant davantage comme un explorateur de fichiers](https://developer.mozilla.org/fr/docs/Apprendre/Ouvrir_un_fichier_dans_un_navigateur_web#Ouvrir_un_fichier_local).

![Le site sans serveur web](https://cdn.geotribu.fr/img/tuto/static_web/static_web_browser_as_file_explorer.png "Le site sans serveur web"){: .img-center  loading=lazy }

Si on veut avoir le site pleinement fonctionnel, il suffit donc de "servir" le dossier par un... serveur web. Parce-que déployer un serveur web n'est pas du tout le sujet, on peut utiliser les outils minimalistes intégrés à de nombreux langages :

<!-- markdownlint-disable MD046 -->
=== "Python 3+"
    Avec bash :

    ```bash
    $ python3 -m http.server 8085
    Serving HTTP on 0.0.0.0 port 8085 (http://0.0.0.0:8085/) ...
    ```

    Avec Powershell :
    ```powershell
    PS > py -3 -m http.server 8085
    Serving HTTP on 0.0.0.0 port 8085 (http://0.0.0.0:8085/) ...
    ```

=== "Node 12+"

    ```bash
    $ npx serve -l 8085
    npx : 78 installé(s) en 3.27s

    ┌──────────────────────────────────────────────────┐
    │                                                  │
    │   Serving!                                       │
    │                                                  │
    │   - Local:            http://localhost:8085      │
    │   - On Your Network:  http://192.168.1.25:8085   │
    │                                                  │
    │   Copied local address to clipboard!             │
    │                                                  │
    └──────────────────────────────────────────────────┘
    ```
<!-- markdownlint-enable MD046 -->

Ouvrir le navigateur sur l'adresse <http://localhost:8085> et vous devriez avoir le site en local, pleinement fonctionnel. Si les images n'apparaissent pas, c'est que vous n'accédez pas à <https://cdn.geotribu.fr>.

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
