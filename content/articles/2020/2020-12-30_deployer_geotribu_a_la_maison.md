---
title: Geotribu à la maison
authors:
    - Julien MOURA
categories:
    - article
    - tutoriel
comments: true
date: 2020-12-30
description: A l'instar de nombreux autres sites web, celui de Geotribu est un site statique. So what ? Pour comprendre, le mieux c'est encore de le déployer à la maison.
image: https://cdn.geotribu.fr/img/articles-blog-rdp/divers/fernand_leger_constructeurs.jpg
tags:
    - Geotribu
    - GitHub
    - serveur
    - site web
---

# Toi aussi, déploie le site Geotribu chez toi

:calendar: Date de publication initiale : 30 décembre 2020

Pré-requis : une connexion internet.

!!! info "Trop tard !"
    La méthode présentée ici ne fonctionne plus depuis cette [PR de mai 2023](https://github.com/geotribu/website/pull/923) qui a basculé le déploiement du site sur les GitHub Pages hors de la branche `gh-pages`.

## Intro

![icône matière](https://cdn.geotribu.fr/img/internal/icons-rdp-news/matiere.png "matière"){: .img-thumbnail-left }

A l'instar de nombreux sites webs, Geotribu est un site statique, cela signifie :

* qu'il n'y a pas de base de données,
* que les appels au serveur web ne sont que des `GET`
* que ce dernier ne fait que retourner des fichiers HTML, CSS, JavaScript et les éventuels contenus binaires (images...).

C'est un gage de plein de mots-clés : légèreté, réactivité, faible maintenance, bonne résilience et sécurité.

Mais c'est surtout un bon moyen de jouer avec un site web sans se casser la tête !

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

Pour mieux se rendre compte de la légèreté et de la facilité des sites statiques, faisons un exercice simple de mise en pratique : **déployons le site actuel de Geotribu sur notre ordinateur en 2 étapes**.

## 1. Télécharger le site de production

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

On peut déjà observer que le site ne pèse que ~25 Mo compressé et ~110 Mo décompressé, pour un contenu de presque 600 pages (articles, revues de presse, guides de contribution, pages d'équipe, etc.). Et encore, le fichier d'index de la recherche (`search/search_index.json`) pèse à lui seul près de 50 Mo.

```bash
jmo@jmoslandia:/tmp/website-gh-pages$ ls -al .
total 496
drwxrwxr-x 14 jmo  jmo    4096 déc.  29 19:39 .
drwxrwxrwt 30 root root  12288 déc.  30 13:06 ..
-rw-rw-r--  1 jmo  jmo  143384 déc.  29 19:39 404.html
drwxrwxr-x  2 jmo  jmo    4096 déc.  29 19:39 acknowledgements
drwxrwxr-x 12 jmo  jmo    4096 déc.  29 19:39 articles
drwxrwxr-x  5 jmo  jmo    4096 déc.  29 19:39 assets
-rw-rw-r--  1 jmo  jmo      19 déc.  29 19:39 CNAME
drwxrwxr-x  9 jmo  jmo    4096 déc.  29 19:39 contribuer
drwxrwxr-x  2 jmo  jmo    4096 déc.  29 19:39 dicogis
-rw-rw-r--  1 jmo  jmo   42105 déc.  29 19:39 feed_rss_created.xml
-rw-rw-r--  1 jmo  jmo   40284 déc.  29 19:39 feed_rss_updated.xml
-rw-rw-r--  1 jmo  jmo  102918 déc.  29 19:39 index.html
drwxrwxr-x  2 jmo  jmo    4096 déc.  29 19:39 install_webapp
-rw-rw-r--  1 jmo  jmo     442 déc.  29 19:39 manifest.webmanifest
drwxrwxr-x 14 jmo  jmo    4096 déc.  29 19:39 node
-rw-rw-r--  1 jmo  jmo       0 déc.  29 19:39 .nojekyll
drwxrwxr-x 13 jmo  jmo    4096 déc.  29 19:39 rdp
-rw-rw-r--  1 jmo  jmo      97 déc.  29 19:39 robots.txt
drwxrwxr-x  2 jmo  jmo    4096 déc.  29 19:39 rss
-rw-rw-r--  1 jmo  jmo     116 déc.  29 19:39 rss.xml
drwxrwxr-x  2 jmo  jmo    4096 déc.  29 19:39 search
-rw-rw-r--  1 jmo  jmo   81602 déc.  29 19:39 sitemap.xml
-rw-rw-r--  1 jmo  jmo    2656 déc.  29 19:39 sitemap.xml.gz
drwxrwxr-x 16 jmo  jmo    4096 déc.  29 19:39 team
drwxrwxr-x  3 jmo  jmo    4096 déc.  29 19:39 theme
jmo@jmoslandia:/tmp/website-gh-pages$ du -sh .
112M    .
jmo@jmoslandia:/tmp/website-gh-pages$ du -sh search/
47M search/
```

Evidemment, ce dossier ne contient pas les images, hébergées sur un [serveur à part]({{ config.extra.url_contribuer }}guides/cdn-images-hebergement/) et sauvegardées mensuellement en tant que release sur GitHub. A titre d'exemple, [la sauvegarde de novembre pèse 422 Mo](https://github.com/geotribu/website/releases/download/2020.11/bkp_cdn_2020-11-11.tar.gz).

![Fernand Léger - Les constructeurs](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/fernand_leger_constructeurs.jpg "Quand je vous disais que c'est Léger !"){: loading=lazy }
{: align=middle }

## 2. Servir le site

En ouvrant simplement le fichier `index.html`, on voit déjà apparaître la page d'accueil dans son navigateur par défaut. Mais le site étant configuré pour avoir des URLs correspondant au titre de la page sans l'extension `.html`, la navigation n'est donc pas fonctionnelle, le [navigateur se comportant davantage comme un explorateur de fichiers](https://developer.mozilla.org/fr/docs/Apprendre/Ouvrir_un_fichier_dans_un_navigateur_web#Ouvrir_un_fichier_local).

![Le site sans serveur web](https://cdn.geotribu.fr/img/tuto/static_web/static_web_browser_as_file_explorer.webp "Consulter le site sur Firefox sans serveur web"){: loading=lazy }
{: align=middle }

Si on veut avoir le site pleinement fonctionnel, il suffit donc de "servir" le dossier par un... serveur web :clap:. Parce-que déployer un serveur web n'est pas du tout le sujet, utilisons les outils minimalistes intégrés à de nombreux langages :

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

Et voilà, vous avez le site Geotribu sur votre ordinateur :smile: !

----

<!-- geotribu:authors-block -->
