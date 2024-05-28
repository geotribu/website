---
title: 'Les commentaires sur Geotribu : de Disqus à Isso'
authors:
    - Julien MOURA
categories:
    - article
comments: true
date: 2021-05-14
description: 'Rien à voir avec la Géo, mais tout à voir avec la Tribu : nous avons migré notre système de commentaires de Disqus vers Isso. Partage d''expérience et contribution open source.'
image: https://cdn.geotribu.fr/img/articles-blog-rdp/geotribu/disqus_to_isso/geotribu_comments_isso_backend.png
tags:
    - commentaire
    - Geotribu
    - Isso
    - open source
---

# Les commentaires sur Geotribu : de Disqus à Isso, via une contribution open-source

:calendar: Date de publication initiale : 14 mai 2021

## Introduction

![icône commentaire](https://cdn.geotribu.fr/img/logos-icones/astuce.png "icône commentaire"){: .img-thumbnail-left }

Lorsque nous avons remis Geotribu en route l'an dernier en optant pour un site statique et que la question des commentaires s'est posée, je suis allé au plus simple : [Disqus], notammant parce-que son intégration est mise en avant dans [la documentation](https://squidfunk.github.io/mkdocs-material/setup/adding-a-comment-system/#disqus) du thème retenu.

Mais avec la montée en puissance de [la fréquentation du site](2021-01-04_bilan_2020_perspectives_2021.md#frequentation), notamment suite à [ign2map], Disqus a considéré que Geotribu était éligible pour les publicités.

![Disqus - Mail de notification](https://cdn.geotribu.fr/img/articles-blog-rdp/geotribu/disqus_to_isso/disqus_publicites_mail_notification.webp "Disqus - Mail de notification"){: loading=lazy align=left clear=right width=150px }

On peut comprendre qu'un service n'est jamais gratuit et que la publicité est l'un des moyens de le viabiliser (modèle freemium dans le cas de [Disqus](https://fr.wikipedia.org/wiki/Disqus)). Mais le prix est trop élevé pour un site bénévole comme Geotribu et les publicités (que je ne voyais pas moi-même, utilisant entre autres [le mode strict de Firefox](https://support.mozilla.org/fr/kb/protection-renforcee-contre-pistage-firefox-ordinateur?cache=no&redirectslug=activer-desactiver-cookies&redirectlocale=fr#w_reglage-stricte-de-la-protection-renforcee-contre-le-pistage) et [uBlock Origin](https://github.com/gorhill/uBlock#ublock-origin)) affichées vraiment mal ciblées voire gênantes :

![Disqus - Publicités affichées](https://cdn.geotribu.fr/img/articles-blog-rdp/geotribu/disqus_to_isso/disqus_publicites_activees.webp "Disqus - Publicités affichées"){: loading=lazy align=right clear=left width=150px }

D'après la [FAQ](https://help.disqus.com/en/articles/1717307-subscription-payments-faq), nous aurions pu prétendre à un forfait gratuit exempt de publicité mais c'était l'occasion de s'affranchir d'un service propriétaire et qui, même gratuit, ajoute des éléments de tracking non désirés.

Comme évoqué dans l'introduction de [la GeoRDP du 12 mars](../../rdp/2021/rdp_2021-03-12.md), nous avons donc décidé de couper le service en attendant de trouver mieux... ou de ne pas mettre de système de commentaires du tout.

Finalement, on a mis en place [Isso] et après un mois d'utilisation, il est temps de faire un retour d'expérience.

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Isso

![logo Isso](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/isso.svg "logo Isso"){: .img-thumbnail-left }

Les systèmes de commentaires sont nombreux : [Juvia](https://phusion.github.io/juvia/), [GitMent](https://imsun.github.io/gitment/), [GitTalk](https://gitalk.github.io/), [Schnack](https://github.com/schn4ck/schnack), etc.

Mais même si une intégration via GitHub (où le site est déjà stocké, généré, hébergé et sauvegardé) était tentante, on s'est dit qu'on ne voulait pas qu'un compte sur une plateforme tierce soit un pré-requis pour commenter sur Geotribu.

On a finalement opté pour [Isso] pour plusieurs raisons  :

- très bien packagé/distribué et plutôt bien maintenu
- pas de publicités, ni de tracking
- auto-hébergeable facilement
- compatible avec le socle technique de l'équipe et du site (Python, Flask)
- pas de SGBD, juste une base SQLite, qu'il est donc facile d'intégrer à notre mécanisme de sauvegarde des fichiers statiques
- capacité d'import de Disqus, qui fournit un export XML des commentaires
- une API minimaliste pour éventuellement d'autres usages (exemple [les 10 derniers commentaires](https://comments.geotribu.fr/latest?limit=10&asc=true))

### Installation du serveur

![logo Python](https://cdn.geotribu.fr/img/logos-icones/programmation/python.png "logo Python"){: .img-thumbnail-left }

Vu que GeoRezo nous autorise gracieusement à utiliser le serveur d'[El Géo Paso](https://elgeopaso.georezo.net/) et qu'il s'agit d'une application légère, j'ai décidé de l'installer à côté de [notre pseudo-CDN]({{ config.extra.url_contribuer }}guides/cdn-images-hebergement/).

L'occasion de rappeler que soutenir GeoRezo c'est une bonne idée pour l'écosystème et c'est aussi soutenir GeoTribu :hugging_face: :

[Faire un don à GeoRezo :fontawesome-solid-hand-holding-heart:](https://www.helloasso.com/associations/georezo-le-portail-geomatique/){: .md-button }
{: align=middle }

Voici dans les grandes lignes les étapes de l'installation, la configuration et du déploiement :

- Du côté de notre gestionnaire de domaine (Gandi) :
    - créer un sous-domaine et le faire pointer sur l'adresse IP du serveur
    - créer une adresse email afin d'envoyer des notifications : `facteur@geotribu.fr`
- Du côté du serveur :
    - on crée un environnement virtuel Python dans lequel on installe Isso et ses copains ([gevent](https://www.gevent.org/) par exemple)
    - on s'assure que le serveur web parle couramment [WSGI](https://wsgi.readthedocs.io/). Dans notre cas, c'est Apache donc ça passe par [mod_wsgi](https://modwsgi.readthedocs.io/)
    - on configure le site dans le serveur web
    - on crée un certificat SSL grâce au [certbot de l'EFF](https://certbot.eff.org/)
    - on fait quelques optimisations : compression et cache

En grand amateur de la théorie du camion (ou [facteur autobus](https://fr.wikipedia.org/wiki/Facteur_d%27autobus)), pour celles et ceux que le détail intéresse, les fichiers de configuration et étapes d'installation sont documentés sur notre compte GitHub :

[Fichiers de configuration et documentation :fontawesome-brands-github:](https://github.com/geotribu/comments/){: .md-button }
{: align=middle }

En peu de temps, nous voici avec l'interface d'administration et les commentaires importés depuis Disqus :

![Isso, interface d'administration](https://cdn.geotribu.fr/img/articles-blog-rdp/geotribu/disqus_to_isso/geotribu_comments_isso_backend.png "Isso, interface d'administration"){: .img-center loading=lazy }

### Intégration au site

![logo HTML5](https://cdn.geotribu.fr/img/logos-icones/programmation/html5.png "logo HTML5"){: .img-thumbnail-left }

Comme indiqué (voir la [doc](https://squidfunk.github.io/mkdocs-material/setup/adding-a-comment-system/) et [ticket GitHub](https://github.com/squidfunk/mkdocs-material/issues/1466#issuecomment-588049898)) par l'auteur du thème Material pour MkDocs que l'on utilise pour le site, si Disqus bénéficie d'une facilité d'intégration, il reste possible d'intégrer n'importe quel système.  
Saluons une fois de plus la qualité de ce thème, dont le développement prévoit des personnalisations totales ou partielles de chaque partie du site.

Pour intégrer le bloc de commentaires, j'ai donc ajouté l'URL dans [la section `extra` du fichier de configuration `mkdocs.yml`](https://github.com/geotribu/website/blob/957583a04cf04f3adcad9ab18d660ca3a874d6ac/mkdocs.yml#L115), de façon à ne pas stocker d'URL en dur dans le template HTML :

```yaml
extra:
  comments_url: https://comments.geotribu.fr/
```

:shinto_shrine: Puis, on personnalise le template Jinja qui sert de base à toutes les pages du site [`main.html`](https://github.com/geotribu/website/blob/957583a04cf04f3adcad9ab18d660ca3a874d6ac/content/theme/main.html#L105-L138) en passant nos [options Isso](https://posativ.org/isso/docs/configuration/client/) et l'URL de la configuration :

```jinja
[...]
{% block disqus %}

{# Comment system (Isso) #}
<div id="__comments">
  <script
    data-isso="{{ config.extra.comments_url }}/"
    data-isso-require-author="true"
    data-isso-require-email="true"
    data-isso-reply-to-self="false"
    data-isso-vote="true"
    src="{{ config.extra.comments_url }}/js/embed.min.js">
  </script>
  <hr><section id="isso-thread"><h2>Comments</h2></section>
  <noscript>Please enable JavaScript to view the comments.</noscript>
</div>
{% endblock %}
[...]
```

Et voilà tout !

![Isso, bloc commentaires Geotribu](https://cdn.geotribu.fr/img/articles-blog-rdp/geotribu/disqus_to_isso/geotribu_commentaires_bloc.webp "Isso, bloc commentaires Geotribu"){: .img-center  loading=lazy }

----

## Contribuer au cercle vertueux de l'open-source

![logo open source](https://cdn.geotribu.fr/img/logos-icones/opensource.png "logo open source"){: .img-thumbnail-left }

Le service rendu est à la hauteur des attentes et voilà la Geotribu dotée d'un nouveau module de commentaires :partying_face:.

Mais [Isso] ne sait notifier des nouveaux commentaires que par email. C'est déjà bien et pour éviter que tout ne repose que sur une personne, on met en place une [chaîne de transfert emails à l'ancienne](https://www.franceculture.fr/societe/partagez-cinq-fois-ce-message-ou-le-retour-des-chaines-de-mails/) !

Ça marche, mais on peut faire mieux : pourquoi ne pas envoyer une notification sur Slack, l'outil (propriétaire hum... :person_facepalming_tone2:) que l'on utilise pour la communication interne à la GéoTribu.

Le souci c'est que Slack, en mode gratuit, ne permet pas le transfert d'email vers un canal. En revanche, les [webhooks](https://fr.wikipedia.org/wiki/Webhook) sont très bien gérés et intégrés.

Alors, puisque c'est open source, pourquoi ne pas mettre à profit les nuits écourtées pour contribuer à [Isso] ?

![Mème Bruce tout Puissant clavier](https://cdn.geotribu.fr/img/articles-blog-rdp/geotribu/disqus_to_isso/meme_bruce_tout_puissant_clavier.webp "Toujours cherché une occasion d'insérer ce mème !"){: .img-center loading=lazy }

Paupières relevées, manches retroussées et c'est parti pour contribuer au projet Isso en proposant d'ajouter la possibilité d'envoyer des notifications à un webhook pour chaque nouveau commentaire posté, avec en prime la possibilité de définir un modèle JSON personalisé.

[Voir la pull request :fontawesome-brands-github:](https://github.com/posativ/isso/pull/724/){: .md-button }
{: align=middle }

En attendant que ce soit éventuellement accepté, on utilise déjà cette version sur Geotribu :

![Geotribot - Notification Slack](https://cdn.geotribu.fr/img/articles-blog-rdp/geotribu/disqus_to_isso/geotribu_comments_geotribot_slack_notification.png "Geotribot - Notification Slack"){: .img-center  loading=lazy }

C'est beau l'open source :smiling_face_with_3_hearts:.

----

<!-- geotribu:authors-block -->

<!-- Hyperlinks reference -->
[Disqus]: https://disqus.com/
[ign2map]: 2021-02-15_ignfr2map_carte_liens_IGN_open-data_7_etapes.md
[Isso]: https://posativ.org/isso/
