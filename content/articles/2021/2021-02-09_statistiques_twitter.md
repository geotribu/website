---
title: Impact de Twitter sur la fréquentation du site GeoTribu
authors:
    - Aurélien CHAUMET
categories:
    - article
comments: true
date: 2021-02-09
description: "Récupérer des données sociales de Twitter, les préparer et les représenter est assez simple, grâce à trois bibliothèques Python : Twint, Pandas et Plolty. L'exemple développé ici s'appuie sur les statistiques autour des GeoRDP et articles parus dans GeoTribu en 2020"
icon: material/twitter
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/stats_twitter/geotribu_stats_twitter.png
tags:
    - Geotribu
    - Pandas
    - Plotly
    - scraping
    - statistiques
    - Twint
    - Twitter
---

# Impact de Twitter sur la fréquentation du site GeoTribu

:calendar: Date de publication initiale : 9 février 2021

Prérequis :

- un interpréteur Python > 3.5
- quelques notions de Python

## Introduction

Nous avions déjà parlé statistiques GeoTribu dans [l'article rétrospectivo-bonne-annesque 2021](2021-01-04_bilan_2020_perspectives_2021.md).

Pas que les statistiques de fréquentation soient un objectif en soi, mais nous souhaitions creuser un peu plus certaines de ces statistiques et principalement celles provenant de Twitter, dans un principe d'exploration et de compréhension.

Et puis c'est aussi l'occasion de faire un article sur le forage de données ([une fois n'est pas coutume](../2020/2020-09-08_web-scraping_scrapy_geotribu.md) :smile:), avec des metadonnées autour de l'activité GeoTribu !

![banner geotribu stats twitter](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/stats_twitter/geotribu_stats_twitter.png "Geotribu stats Twitter"){: .img-center loading=lazy }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

## Récupérer les données de Twitter grâce à Twint

### Pourquoi Twint ?

Avant d'analyser quoi que ce soit, il faut disposer de données. Et ça tombe bien, nous en avons énormément autour de nous !

Twitter est une mine d'or de données sociales et leur récupération n'est réellement pas compliquée, notamment grâce à [Twint](https://github.com/twintproject/twint).

D'autres bibliothèques existent, comme [Tweepy](https://www.tweepy.org/) par exemple, mais à ma connaissance Twint est la seule à ne pas passer par l'API officielle Twitter et donc à pouvoir s'affranchir de ses limitations, comme le nombre de tweets maximal récupérés.

De plus, c'était une nouvelle occasion d'utiliser Twint, sur le même principe que [le scraping de données sur le 30DayMapChallenge](https://aurelienchaumet.github.io/articles/30daymapchallenge_scraping_twitter/), que j'avais déjà réalisé.

### Installation

L’installation est ultra simple, il suffit d'entrer dans un terminal de commande :

```bash
pip3 install twint
```

Et logiquement, c’est réglé !

Si vous souhaitez avoir d’autres manières de l’installer, vous les trouverez dans [le wiki de Twint](https://github.com/twintproject/twint/wiki/Setup).

### Principes de fonctionnement

Une fois installé, il existe 2 manières d'utiliser Twint :

#### Utilisation de la ligne de commande

Pour les cas d’usage les plus simples, vous pouvez passer par une commande CLI.  
Par exemple, pour récupérer l’ensemble des tweets de `username` :

```bash
twint -u username
```

Ce deuxième exemple ramènera l’ensemble des tweets contenant `pineapple`.

```bash
twint -s pineapple
```

#### Utilisation en tant que module Python

Pour les cas un peu plus poussés, il faudra passer par l’usage du module. La documentation de Twint donne un exemple pour récupérer l’ensemble des tweets de Donald Trump contenant `great`.  

```python
import twint

# Configure
c = twint.Config()
c.Username = "realDonaldTrump"
c.Search = "great"

# Run
twint.run.Search(c)
```

L’avantage de cette deuxième méthode réside dans le fait de pouvoir utiliser des fonctions pythoniques et vous pourrez ainsi vous en servir dans un script plus élaboré.

Vous trouverez plus d'informations sur [les fonctions utilisables ici](https://github.com/twintproject/twint/wiki/Configuration), ainsi que [plusieurs exemples ici](https://github.com/twintproject/twint/wiki/Scraping-functions).

!!! info
    Si vous souhaitez utiliser Twint via un [Jupyter Notebook](https://jupyter.org), il est important d'installer et d'importer la bibliothèque [`nest_asyncio`](https://github.com/erdewit/nest_asyncio).  

    <!-- markdownlint-disable MD046 -->
    ```python
    # Pour l'installer
    pip3 install nest_asyncio

    # Pour l'importer et l'utiliser
    import nest_asyncio
    nest_asyncio.apply()
    ```
    <!-- markdownlint-enable MD046 -->

----

## Scraping et préparation des données twitter GeoTribu

Maintenant que les bases sont posées, nous pouvons rentrer dans le vif du sujet.

Nous cherchons ici à objectiver les tendances observées via les statistiques d'utilisation du site GeoTribu provenant de Google Analytics. La problématique est donc la suivante : à quel point Twitter influence-t-il le trafic du site ?

Nous allons récupérer pour cela 2 types de données : les tweets liés aux GeoRDP et ceux liés aux articles.

!!! info
    Le cas d'usage étant simple ici, le choix aurait pu se porter sur les commandes directes en CLI. Mais pour l'exemple, nous passerons par le module de Twint, qui ouvre plus de possibilités.

### Données des GeoRDP

Voici le code que j'ai utilisé pour obtenir les tweets depuis le 30 avril 2020, qui contiennent le mot `geordp` :

```python
c = twint.Config()
c.Search = "geordp"
c.Since = "2020-04-30"
c.Store_csv = True
c.Output = "geordp-tweets.csv"

twint.run.Search(c)
```

Détail des paramètres :

- `c` est la variable dans laquelle on stocke une instance Twint
- `.Search` dit à Twint qu'il va devoir récupérer les données sur les tweets contenant le terme qui nous intéresse
- `.Since` indique à partir de quand il doit chercher
- `.Store_csv` lui dit de stocker le résultat dans un fichier csv
- `.Output` sous quel nom et où doit-il le faire

Si vous avez installé Twint et que vous faites tourner ce bout de code chez vous, vous pourrez bien sûr récupérer les mêmes données que moi. Tout ceci est réalisé sans trucage et ne nécessite pas de quelconque compétences de cascadeur.

![pouf cascadeur](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/stats_twitter/cascadeur_pouf.gif "Pouf le cascadeur"){: .img-center loading=lazy }

La pédagogie passe par la répétition, donc l'adage suivant ne sera sans doute pas répété assez souvent : toute dataviz est basée sur une bonne préparation de la donnée.

Ce n'est donc pas parce que nous venons de récupérer des données (aussi intéressantes soient-elles) qu'il faut se précipiter à vouloir les représenter. Un peu de patience que diable !

Afin de pouvoir utiliser ses données, il va encore falloir travailler un peu.  
En effet, en l'état, Twint a renvoyé l'ensemble des tweets contenant `geordp`, donc sans doute les tweets originels de partage des GeoRDP, mais également les retweets cités, ainsi que tout tweet mentionnant ce mot, et n'ayant pas forcément à voir avec une GeoRDP directement.

Il va donc falloir identifier les tweets originels, et ici, à part faire le boulot à la main, je n'ai pas trouvé d'autres méthodes, mais pour une grosse dizaine de lignes, ça devrait aller.

On ajoute un champ dans le csv `geordp`, peuplé avec des 'oui' lorsqu'ils correspondent au premier partage.  
On ajoute également la date de publication de la GeoRDP, car il peut arriver que les GeoRDP soient partagées après leur publication sur le site de GeoTribu.

### Données des articles

Pour les articles, le code est sensiblement le même :

```python hl_lines="2 5"
c = twint.Config()
c.Search = "geotribu"
c.Since = "2020-04-30"
c.Store_csv = True
c.Output = "geotribu-tweets.csv"

twint.run.Search(c)
```

Les seules différences se situent sur le `.Search` et le `.Output`.

Concernant la préparation de ce fichier, tout comme le précédent, il faut identifier les tweets originels de partage des articles.  
Un champ `article` est ajouté en le peuplant de 'oui' lorsque cela est nécessaire.

[:page_facing_up: Accéder au script Twint :page_facing_up:](https://github.com/geotribu/stats-twitter-geotribu/blob/main/scripts/scrap-twint.py){: .md-button }
{: align=middle }

### Données du site GeoTribu

Afin de tenter de comprendre si le partage des GeoRDP et articles sur Twitter ont une influence sur l'affluence du site GeoTribu, nous avons besoin de données d'utilisation du site.

Pour ce faire, on utilise Google Analytics [comme précédemment expliqué ici](2021-01-04_bilan_2020_perspectives_2021.md#frequentation).

En exportant les données du nombre d'utilisateurs quotidiens, on devrait avoir de quoi représenter un peu les choses.

### Twint vous informe

Pour être un peu plus complet sur Twint, il faut savoir que les résultats des tweets ressemblent à un fichier csv avec pas mal de champs et notamment :

- id du tweet
- date de création
- id et nom du twittos
- le texte du tweet en entier
- les hashtags
- l'url du tweet
- les nombres de likes, retweets et réponses

Vous trouverez [sur le wiki l'ensemble des champs produits](https://github.com/twintproject/twint/wiki/Tweet-attributes).

----

## Visualisation des différentes données récupérées

Il y a un peu de travail complémentaire sur la donnée pour pouvoir comparer les différentes sources, en passant par exemple les données du site Geotribu en format quinzomadaire, étant donné que les GeoRDP influencent très clairement les statistiques du site.

Pour celles et ceux qui seraient intéressés, le code de la fin de la préparation des données est disponible dans un dépôt Github sous deux scripts, un premier permettant de visualiser les données provenant exclusivement des GeoRDP et un deuxième prenant également en compte les articles parus sur GeoTribu.

Concernant la visualisation des données, c'est [Plotly](https://plotly.com/python/) qui a été utilisé ici. Les 2 scripts évoqués plus haut contiennent également le code permettant de reproduire les deux graphiques présents dans la suite de l'article.

[:page_facing_up: Accéder au dépôt Github :page_facing_up:](https://github.com/geotribu/stats-twitter-geotribu){: .md-button }
{: align=middle }

### Représentation des données des GeoRDP

Le graphique ci-dessous représente en bleu le nombre de likes et en rouge le nombre de retweets des tweets originels de partage, plus les statistiques des retweets cités (qui ne rentrent pas en compte dans les statistiques des tweets originaux, à l'inverse des retweets classiques, étant considérés comme un nouveau contenu original par Twitter). Les données de likes et retweets ont été placées à la date de partage originelle de chaque GeoRDP.  
La courbe verte représente le nombe d'utilisateurs du site GeoTribu par quinzaine.  
Les pointillés orange verticaux correspondent aux dates de publication des GeoRDP.

<iframe width="100%" height="500px" src="https://geotribu.github.io/stats-twitter-geotribu/geordp.html" frameborder="0" allowfullscreen></iframe>

[:chart_with_upwards_trend: Voir le graphique en plein écran :chart_with_upwards_trend:](https://geotribu.github.io/stats-twitter-geotribu/geordp.html){: .md-button } [:page_facing_up: Accéder au script :page_facing_up:](https://github.com/geotribu/stats-twitter-geotribu/blob/main/scripts/prepa-visu-geordp-ga.py){: .md-button }
{: align=middle }

On remarque une certaine corrélation (comme déjà évoqué précédemment) entre la publication des GeoRDP et l'affluence sur le site GeoTribu.  
Les périodes de vacances scolaires n'ont pas l'air très propices à la géo-lecture, étant donné qu'en août et en fin d'année on observe des baisses de fréquentation, alors que des GeoRDP ont bien été publiées.

En revanche, le lien entre publication de GeoRDP et partage Twitter n'est pas toujours très évident. Certains pics (dernière quinzaine de mai et fin juillet par exemple) ont l'air d'être associés à Twitter, en revanche on observe une baisse du nombre de likes et retweets à partir du 13 novembre , alors que la fréquentation du site continue d'augmenter jusqu'au 13 décembre.

2 hypothèses principales :

- L'apport du partage des GeoRDP sur Linkedin est assez important (17% du trafic provenant des réseaux sociaux) et donc, non pris en compte ici. De plus, Linkedin affiche parfois du contenu datant de plusieurs semaines sur les fils d'actualité, décalant donc potentiellement son impact sur la fréquentation du site
- D'autres contenus ont été partagés en plus des GeoRDP (des articles) et ne sont pas comptabilisés dans les statistiques twitteriennes présentées plus haut.

Nom de Zeus ! Marty, regardons de suite ce que cela implique si on rajoute les tweets de publication des articles ! :rocket:

### Ajout des données des articles

Ce nouveau graphique représente les mêmes champs, avec les données provenant des tweets sur les articles en plus de celles des GeoRDP.  
Les données de partage des articles ont été ramenées à l'échelle de celles des GeoRDP, c'est-à-dire au minimum toutes les 2 semaines (comme les données utilisateurs du site GeoTribu), afin de pouvoir comparer l'ensemble des données.

<iframe width="100%" height="500px" src="https://geotribu.github.io/stats-twitter-geotribu/articles.html" frameborder="0" allowfullscreen></iframe>

[:chart_with_upwards_trend: Voir le graphique en plein écran :chart_with_upwards_trend:](https://geotribu.github.io/stats-twitter-geotribu/articles.html){: .md-button } [:page_facing_up: Accéder au script :page_facing_up:](https://github.com/geotribu/stats-twitter-geotribu/blob/main/scripts/prepa-visu-geordp-articles-ga.py){: .md-button }
{: align=middle }

Bingo, comme disent les amateurs de loto !

On voit bien que la hausse de fréquentation observée mi-octobre et de manière continue jusqu'aux vacances de Noël est sans doute liée aux articles et à leur partage.  
Le pic de fin juin peut également s'expliquer grâce au partage [d'un article](../2020/2020-07-03_deploy_qgis_windows.md).

## Conclusion

Clairement, Twint est très simple d'utilisation et en 3 coups de cuillères à Python, il est possible d'arriver à représenter et analyser quelques phénomènes provenant de Twitter.

N'hésitez pas à nous faire des retours dans les commentaires, si vous avez également des cas d'usage de Twint !

----

<!-- geotribu:authors-block -->
