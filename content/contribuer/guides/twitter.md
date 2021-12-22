---
title: Intégrer un tweet
categories:
    - article
    - contribution
    - tutoriel
date: 2020-04-20 10:20
description: "Guide de contribution à Geotribu : comment intégrer un tweet dans un contenu en Markdown."
image: "https://cdn.geotribu.fr/img/internal/contribution/twitter/embed_tweet_publish_website.png"
tags:
    - contribuer
    - guide
    - intégration
    - Markdown
    - Twitter
# theme customizations
search:
  exclude: true
---

<!-- markdownlint-disable MD046 -->

# Intégrer un tweet

## Pas à pas

Prenons ce tweet pour exemple : <https://twitter.com/geojulien/status/1169878346693369856>

1. Cliquer sur le menu déroulant et sélectionner **Intégrer le tweet** :

    ![Menu Intégrer le tweet](https://cdn.geotribu.fr/img/internal/contribution/twitter/embed_tweet_menu.png){: loading=lazy }

2. On est alors dirigé vers [le site dédié à l'intégration Twitter Publish](https://publish.twitter.com/) :

    !!! info
        Le scénario peut varier dans certains cas. Par exemple, il est possible que le mini-formulaire d'intégration apparaisse directement au-dessus du tweet. Pas de panique, ça revient au même à partir du point 4.

    ![Outil de publication des tweets dans des sites tiers](https://cdn.geotribu.fr/img/internal/contribution/twitter/embed_tweet_publish_website.png){: loading=lazy }

3. Pour bien faire les choses, notamment pour respecter les utilisateurs de Geotribu qui ne souhaitent pas être traqués par le marketing de Twitter, il est de bon ton de prendre le temps de changer les options de personnalisation. Cliquer sur `set customization options`, faire les réglages et cliquer sur `Update` :

    ![Personnaliser l'intégration du tweet](https://cdn.geotribu.fr/img/internal/contribution/twitter/embed_tweet_publish_custom.png){: loading=lazy }

4. Cliquer sur `Copy code` pour récupérer le bout de HTML à coller dans le markdown :

    === "Mis en forme"

        ```html linenums="1"
        <blockquote class="twitter-tweet" data-lang="fr" data-dnt="true">
        <p lang="fr" dir="ltr">Tjs une excellente base pour découvrir et expérimenter. Ce projet est juste fabuleux alors
            j&#39;imagine même pas les gens derrière ! <a href="https://t.co/27GwU4l54J">https://t.co/27GwU4l54J</a></p>
        &mdash; Julien Moura (@geojulien) <a
            href="https://twitter.com/geojulien/status/1169878346693369856?ref_src=twsrc%5Etfw">6 septembre 2019</a>
        </blockquote>
        <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ```

    === "Brut"

        ```html
        <blockquote class="twitter-tweet" data-lang="fr" data-dnt="true"><p lang="fr" dir="ltr">Tjs une excellente base pour découvrir et expérimenter. Ce projet est juste fabuleux alors j&#39;imagine même pas les gens derrière ! <a href="https://t.co/27GwU4l54J">https://t.co/27GwU4l54J</a></p>&mdash; Julien Moura (@geojulien) <a href="https://twitter.com/geojulien/status/1169878346693369856?ref_src=twsrc%5Etfw">6 septembre 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
        ```

5. Le site intègre déjà le Javascript de Twitter. Pour des raisons de performances et que le tweet soit rendu dans les meilleures conditions, il faut **supprimer** la balise `script` qui est ajoutée à la suite du `blockquote` :

    ```html hl_lines="7" linenums="1"
    <blockquote class="twitter-tweet" data-lang="fr" data-dnt="true">
    <p lang="fr" dir="ltr">Tjs une excellente base pour découvrir et expérimenter. Ce projet est juste fabuleux alors
        j&#39;imagine même pas les gens derrière ! <a href="https://t.co/27GwU4l54J">https://t.co/27GwU4l54J</a></p>
    &mdash; Julien Moura (@geojulien) <a
        href="https://twitter.com/geojulien/status/1169878346693369856?ref_src=twsrc%5Etfw">6 septembre 2019</a>
    </blockquote>
    <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    ```

:bellhop_bell: Voilà, c'est prêt ! :tada:

Coller le HTML dans le markdown et il s'affichera ainsi :

<blockquote class="twitter-tweet" data-lang="fr" data-dnt="true">
<p lang="fr" dir="ltr">Tjs une excellente base pour découvrir et expérimenter. Ce projet est juste fabuleux alors
    j&#39;imagine même pas les gens derrière ! <a href="https://t.co/27GwU4l54J">https://t.co/27GwU4l54J</a></p>
&mdash; Julien Moura (@geojulien) <a
    href="https://twitter.com/geojulien/status/1169878346693369856?ref_src=twsrc%5Etfw">6 septembre 2019</a>
</blockquote>

----

## Précisions et options

### Centrer le tweet

Bizarrement, l'option n'est pas proposée dans le formulaire de Twitter alors qu'il existe bien une classe CSS. Il faut donc ajouter manuellement `tw-align-center` aux côtés de `twitter-tweet` :

```css hl_lines="1" linenums="1"
<blockquote class="twitter-tweet tw-align-center" data-lang="fr" data-dnt="true">
<p lang="fr" dir="ltr">Tjs une excellente base pour découvrir et expérimenter. Ce projet est juste fabuleux alors
    j&#39;imagine même pas les gens derrière ! <a href="https://t.co/27GwU4l54J">https://t.co/27GwU4l54J</a></p>
&mdash; Julien Moura (@geojulien) <a
    href="https://twitter.com/geojulien/status/1169878346693369856?ref_src=twsrc%5Etfw">6 septembre 2019</a>
</blockquote>
```

### Pistage, blocage et fallback

Si un utilisateur utilise une protection renforcée contre le pistage et toute forme de tracking publicitaire, Twitter renvoie les tweets dans une forme dégradée (notamment sans les médias). Les tweets intégrés apparaissent alors dans une forme simplifiée avec uniquement le texte :

[![Tweet - Tracking enabled](https://cdn.geotribu.fr/img/internal/contribution/twitter/embed_tweet_tracking_enabled.png "Tweet - Tracking enabled"){: loading=lazy width=350px }](https://cdn.geotribu.fr/img/internal/contribution/twitter/embed_tweet_tracking_enabled.png){: data-mediabox="lightbox-twitter" data-title="Tweet correctement intégré quand la protection contre le pistage est désactivée"}
[![Tweet - Tracking enabled](https://cdn.geotribu.fr/img/internal/contribution/twitter/embed_tweet_tracking_fallback.png "Tweet - Tracking enabled"){: loading=lazy width=350px }](https://cdn.geotribu.fr/img/internal/contribution/twitter/embed_tweet_tracking_fallback.png){: data-mediabox="lightbox-twitter" data-title="Rendu dégradé quand la protection contre le pistage est active"}
{: align=middle }

Consulter :

- [l'article de Mozilla sur la protection contre le pistage](https://developer.mozilla.org/fr/docs/Mozilla/Firefox/Privacy/protection_contre_le_pistage)
- Firefox : [comment activer/désactiver la protection pour un site](https://support.mozilla.org/fr/kb/protection-renforcee-contre-pistage-firefox-ordinateur?as=u&utm_source=inproduct#w_que-faire-si-un-site-semble-dysfonctionner)

### Aspects techniques

Techniquement, l'intégration des tweets repose sur l'intégration d'une balise HTML `blockquote` en dur directement au sein du texte en markdown. La balise ainsi intégrée est transformée à la volée au chargement de la page via un script Javascript hébergé sur les serveurs de Twitter qui modifie directement le DOM pour en faire une balise `twitter-widget` complète dont le rendu est contrôlé par Twitter.

Conformément aux [recommandations de Twitter](https://developer.twitter.com/en/docs/twitter-for-websites/javascript-api/guides/set-up-twitter-for-websites), le code Javascript est intégré au chargement du site et n'est donc chargé qu'une seule fois par les visiteurs de Geotribu.

Pour plus d'infos, [consulter la Pull Request](https://github.com/geotribu/website/pull/54) qui a permis l'intégration propre des tweets.

----

## Exemples déjà publiés

Voici quelques exemples de syntaxe markdown qui ont été publiés sur Geotribu :

- [intégration du tweet de Sylvain Latarget annonçant l'ouverture des données de l'IGN](https://github.com/geotribu/website/blob/master/content/rdp/2020/rdp_2020-12-11.md?plain=1#L197)
