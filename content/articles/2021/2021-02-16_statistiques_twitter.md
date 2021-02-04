---
title: "Impact de Twitter sur la fréquentation du site GeoTribu"
authors: ["Aurélien CHAUMEt"]
categories: ["article"]
date: "2021-02-16 10:20"
description: "Description pour le SEO."
image: "Image d'illustration de l'article qui sert ensuite dans la mise en avant : réseaux sociaux, flux RSS..."
tags: "twitter,scraping,twint,statistiques,geotribu,plotly"

---

# Impact de Twitter sur la fréquentation du site GeoTribu

:calendar: Date de publication initiale : 16 février 2021

**Mots-clés :** Mot-clé 1 | Mot-clé 2

## Introduction

Nous avions déjà parlé statistiques GeoTribu dans [l'article rétrospectivo-bonne-annesque 2021](https://static.geotribu.fr/articles/2021/2021-01-04_bilan_2020_perspectives_2021/).

Pas que les statistiques de fréquentation soient un objectif en soit, nous souhaitions creuser un peu plus certaines de ses statistiques et principalement celles provenant de Twitter, dans un principe d'exploration et de compréhension.

Et puis c'est aussi l'occasion de faire un article sur le forage de données ([une fois n'est pas coutume](https://static.geotribu.fr/articles/2020/2020-09-08_web-scraping_scrapy_geotribu/) :smile:), avec des données meta autour de l'activité GeoTribu !

[Commenter cet article :fontawesome-solid-comments:](#__comments){: .md-button }
{: align=middle }

## Récupérer les données de Twitter grâce à Twint

### Pourquoi Twint ?

Avant d'analyser quoi que ce soit, il faut disposer de données. Et ça tombe bien, nous en avons énormément autour de nous !

Twitter est une mine d'or de données sociales, et leur récupération n'est réellement pas compliquée, notamment grâce à [Twint](https://github.com/twintproject/twint).

D'autres bibliothèques existent, notamment Tweepy par exemple, mais 1 ma connaissance Twint est la seule à ne passer par l'API officielle Twitter et donc à pouvoir s'affranchir d'un certain nombre de limitations comme le nombre de tweets maximal récupérés par exemple.

### Installation

L’installation est ultra simple, il suffit de taper dans un terminal de commande :

```python
pip3 install twint
```

Et logiquement, c’est réglé !

Si vous souhaitez avoir d’autres manières de l’installer, vous les trouverez dans [le wiki de Twint](https://github.com/twintproject/twint/wiki/Setup).

### Principes de fonctionnement

Une fois installé, il existe 2 manières d'utiliser Twint :

- Pour les cas d’usage les plus simples, vous pouvez passer par une commande CLI

    ```python
    twint -u username
    ```

    Par exemple, récupèrera l’ensemble des tweets de `username`.

    ```python
    twint -s pineapple
    ```

    Ce deuxième exemple ramènera l’ensemble des tweets contenant `pineapple`.

- Pour les cas un peu plus poussés, il faudra passer par l’usage du Module

    ```python
    import twint

    # Configure
    c = twint.Config()
    c.Username = "realDonaldTrump"
    c.Search = "great"

    # Run
    twint.run.Search(c)
    ```

    Ici, vous récupèrerez l’ensemble des tweets de Donald Trump contenant `great`.  
    *L’exemple cité provient de la documentation de Twint et ne réflète en aucun cas un quelconque intérêt pour le fond*

L’avantage de cette deuxième méthode réside dans le fait de pouvoir utiliser des fonctions pythoniques, et vous pourrez ainsi vous en servir dans un script plus élaboré.

Vous trouverez plus d'informations sur [les fonctions utilisables ici](https://github.com/twintproject/twint/wiki/Configuration), ainsi que [plusieurs exemples ici](https://github.com/twintproject/twint/wiki/Scraping-functions).

### Scraping des données twitter GeoTribu

Maintenant que les bases sont posées,nous pouvons rentrer dans le vif du sujet.

Nous cherchons ici à objectiver les tendances observées via les statistiques d'utilisation du site GeoTribu provenant de Google Analytics. La problématique est donc la suivante : à quel point Twitter  influence le trafic du site ?

Nous allons récupérer pour cela 2 types de données : les tweets liées aux GeoRDP et ceux liés aux articles.

Le cas d'usage étant simple ici, le choix aurait pu se porter sur les commandes directs en CLI. Mais pour l'exemple, nous allons passer par le Module de Twint, qui ouvre plus de possibilités.

#### Données des GeoRDP

#### Données des articles

La pédagogie passe par la répétition, donc l'adage suivant ne sera sans doute pas répété asez souvent : toute dataviz est basée sur une bonne préparation de la donnée.

Ce n'est donc pas parce que nous venons de récupérer des données (aussi intéressantes soient-elles) qu'il faut se précipiter à vouloir les représenter. Un peu de patience que diable !

----

## Auteur

--8<-- "content/team/acha.md"
