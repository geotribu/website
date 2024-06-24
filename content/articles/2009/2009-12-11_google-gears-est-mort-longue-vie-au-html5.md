---
title: "Google Gears est mort longue vie au HTML5"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-12-11
description: "Google Gears est mort longue vie au HTML5"
tags:
    - HTML5
    - Google
    - web
---

# Google Gears est mort longue vie au HTML5

:calendar: Date de publication initiale : 11 décembre 2009

![icône globe world](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png "icône globe générique"){: .img-thumbnail-left }

N'enterrons pas trop vite Google Gears (que nous abrégerons par GGears) mais il semble bien que la firme du même nom ait décidé de lui préférer le futur standard HTML 5. Cette information abondamment relayée ([clubic](http://www.clubic.com/actualite-313674-google-abandonne-gears-html.html), [01net](http://pro.01net.com/editorial/509349/google-delaisse-gears-au-profit-d-html-5/)... ) s'explique logiquement du fait que la plupart des fonctionnalités apportées par le plugin GGears seront fournies nativement par le nouveau moteur HTML 5 (gestion du Drag & Drop, du mode déconnectée...). Ce choix est une décision importante pour l' interopérabilité et pour le respect des standards.

Mais revenons au HTML 5 et aux bouleversements qu'il risque d'entrainer. **Bouleversements?** Oui et encore le terme me semble à peine suffisant. En effet, après plus de 10 ans sans nouvelle version majeure, le format HTML s'offre une véritable cure de jouvence. Les améliorations sont nombreuses, on y trouve notamment :

* une structuration orientée contenu (balises Article, Dialog, Figure)
* le support audio et vidéo
* l'intégration de la balise canvas
* la gestion Web Workers
* ...

Les futures fonctionnalités sont présentées en détail sur les sites [alsa créations](http://www.alsacreations.com/article/lire/750-HTML5-nouveautes.html) et [life hacker](http://lifehacker.com/5416100/how-html5-will-change-the-way-you-use-the-web?skyline=true&s=x). Je vous invite également à consulter le site [labnol](http://www.labnol.org/internet/html5-presentations/10587/) qui référence les meilleures présentations liées au HTML 5 et tout particulièrement celle de [Brad Neuberg](http://www.youtube.com/watch?v=siOHh0uzcuY) qui, pendant 20 minutes, expose magistralement le futur web de demain.

Pour le côté pratique quelques démos commencent à être disponibles. Le site [hml 5 demos](http://html5demos.com/) a ainsi réalisé toute une série d'exemples. Enfin, preuve que le HTML 5 n'est pas qu'une simple utopie quelque acteurs importants du Web ont dors et déjà commencé à réaliser des prototypes d'interface à l'exemple de [You Tube](http://www.youtube.com/html5) ou de Google Wave

Bon ok, le html 5 c'est bien beau mais quel rapport avec la cartographie me direz-vous ! Ce à quoi je réponds **TOUT**. En effet, cette nouvelle version risque de bousculer nos habitudes du web et surtout elle ouvre la porte à une multitude de nouveaux usages. Intéressons-nous aux quatre améliorations majeures qui vont je pense bouleverser notre approche du WebMapping :

* **Web Workers** : Il vous est déjà arrivé je pense d'être sur une page et que celle-ci tout à coup se ralentisse ou pire se fige à cause d'un script consommateur de ressource. Pour pallier à cela, le concept de Web Workers permettra de s'affranchir de cette contrainte en exécutant les processus consommateur de ressources en tache de fond. Comme un exemple vaut mieux qu'un long discours, je vous invite à consulter l'[exemple](http://people.mozilla.com/~prouget/demos/simulatedAnnealing/index.xhtml) de Mozilla ou encore ces deux exemples de calculs de nombres premiers un utilisant les [webworkers](http://htmlfive.appspot.com/static/primes-good.html) alors que l'[autre](http://htmlfive.appspot.com/static/primes-bad.html) non.
* **Canvas** : Imaginez que vous souhaitiez créer dynamiquement un vecteur directement depuis votre interface graphique, c'est ce que permet la balise canvas. Pour ma part, j'avais du mal à comprendre la différence entre le SVG et le canvas. Si vous êtes dans le même cas que moi, je vous conseille la lecture du [billet](http://ljouanneau.com/blog/post/2009/03/26/Differences-entre-documents-et-API) de Laurent Jouanneau. En fait comme il le spécifie dans son titre c'est avant tout des "Différences entre documents et API".
* **Geolocalisation** : Attention [Big Brother](https://fr.wikipedia.org/wiki/1984_(roman)) vous regarde ! Même si cela peut portait à sourire nous n'en sommes pas très loin. En effet il est maintenant possible, depuis votre navigateur et avec votre autorisation, d'être automatiquement localisé.
* **Exploitation en mode déconnecté** : Cette fonctionnalité permettra de créer un cache afin de sauvegarder les données en local et pouvoir ainsi travailler en offline.
Je pense qu'il n'est pas très difficile d'entrevoir les exemples d'applications cartographiques qu'il est possible de réaliser. [Cartagen](http://cartagen.org/) dont l'interface cartographique est uniquement construite à base de canvas est un exemple des possibilités offertes. Le développeur va même un peu plus loin car il a lui-même inventé son propre langage CSS cartographique baptisé GSS pour Geographic Style Sheets. Mais bon ceci fera surement l'objet d'un autre billet.

Allé pour finir un petit gout de CSS 3 et notamment de la propriété transition qui risque bien de rendre toutes nos belles bibliothèques javascript obsolètes. L'explication se passe toujours sur le blog de [Laurent Jouanneau](http://ljouanneau.com/blog/post/2009/10/16/Transitions-CSS) et pour l'exemple c'est [ici](http://ljouanneau.com/lab/css3/transitions/zmtransitions.html).

----

<!-- geotribu:authors-block -->
