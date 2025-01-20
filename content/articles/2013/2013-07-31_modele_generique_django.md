---
title: "Modèle générique avec Django"
authors:
    - Arnaud VANDECASTEELE
categories:
    - article
comments: true
date: 2013-07-31
description: "Modèle générique avec Django"
tags:
    - Django
    - Python
---

# Modèle générique avec Django

:calendar: Date de publication initiale : 31 juillet 2013

Dans un des projets sur lequel je travaille, j'ai plusieurs modèles dont la structure est similaire mais dont seule la table change. En fait, il s'agit d'une grille géographique couvrant le monde et dont la résolution change en fonction du zoom. Plutôt que de répéter la même structure pour chacune des classes, il est bien plus simple de s'appuyer sur un modèle générique qui servira aux autres. Avec Django, rien de plus simple ! Voyons cela immédiatement.

----

Première étape, il faut bien évidemment créer votre modèle générique ([classe abstraite](https://docs.djangoproject.com/en/dev/topics/db/models/#abstract-base-classes)). Celle-ci dépend de votre usage et son implémentation ne change pas de ce qui se fait habituellement mise à part l'utilisation de la combinaison `abstract = True`. Comme son nom l'indique, cette combinaison spécifie que notre classe est abstraite ce qui signifie qu'elle pourra être utilisée par d'autres classes mais aussi qu'elle ne fait référence à aucune table de notre base et donc qu'aucune table ne sera créée lors de l'utilisation de [syncdb](https://docs.djangoproject.com/en/dev/ref/django-admin/#django-admin-syncdb). Par exemple, ma classe générique ressemble à cela :

```javascript
class gridGenericView(models.Model):
    id = models.IntegerField(primary_key=True)
    bbox = models.PolygonField()  
    generalvalue = models.IntegerField(null=True, blank=True)
    thematicaccuracy = models.IntegerField(null=True, blank=True)
    positionalaccuracy = models.IntegerField(null=True, blank=True)
    completeness = models.IntegerField(null=True, blank=True)
    objects = models.GeoManager()
    class Meta:
        abstract = True
```

Toutes les autres classes de mon application ont exactement la même structure, seul change le nom de la table. Il me suffit alors de simplement écrire mes nouvelles classes de la manière suivante :

```javascript
class osmqualitygridxlargevalues(gridGenericView):
    class Meta:
        db_table = 'osmqualitygridxlargevalues'

class osmqualitygridlargevalues(gridGenericView):
    class Meta:
        db_table = 'osmqualitygridlargevalues'
```

Plutôt simple non ? Vous noterez que contrairement à `gridGenericView` qui hérite de `models.Model`, mes deux autres classes héritent de `gridGenericView`. Dans mon cas, je souhaitais simplement changer la table à laquelle ses classes font référence. Mais rien ne vous empêche d'ajouter des champs en fonction de vos besoins. C'est ça que j'aime avec Django, c'est simple et bien pensé :)

----

<!-- geotribu:authors-block -->
