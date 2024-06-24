---
title: "Créer ses propres plugins pour QGIS"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2010-09-23
description: "Créer ses propres plugins pour QGIS"
tags:
    - plugin builder
    - plugin QGIS
    - PyQGIS
    - QGIS
---

# Créer ses propres plugins pour QGIS

:calendar: Date de publication initiale : 23 septembre 2010

![logo QGIS](https://cdn.geotribu.fr/img/logos-icones/logiciels_librairies/qgis.png "logo QGIS"){: .img-thumbnail-left }

Ce billet s'inspire de l'article [a simple qgis python tutorial](http://linfiniti.com/2010/08/a-simple-qgis-python-tutorial/) paru sur le blog [linfinite](http://linfiniti.com/). En effet, [QGIS](https://www.qgis.org/) offre, depuis la version 1.0, la possibilité de réaliser vos propres extensions en utilisant l'[API](http://qgis.org/api/2.4/modules.html) du logiciel. Mais avant de pouvoir réaliser cela, il est nécessaire de comprendre le rôle des différents éléments.

C'est pourquoi, nous détaillerons les étapes nécessaires afin que vous puissiez ensuite réaliser vos propres applications. Mais, comparativement au blog [linfiniti](http://linfiniti.com/), notre exemple sera beaucoup plus simple ceci afin d'aller uniquement à l'essentiel.

----

## Préparatifs

### Génération de la structure du plugin

La création d'un plugin QGIS se fait en langage python. Plutôt que de créer l'ensemble des fichiers nécessaires manuellement, nous allons le faire grâce à un plugin QGIS qui génère un "squelette" de plugin QGIS !
Pour cela :

1. allez dans "Extensions"
2. puis "Installer/Gérer les extensions"
3. Ensuite dans le menu "Paramètres" cochez "Affichez les extensions expérimentales"
4. Enfin, une fois la liste des extensions mises à jour, le "Plugin Builder" devrait être disponible.

Installons-le et utilisons le immédiatement : `menu Extension -> Plugin Builder`.

![plugin_builder_v3.jpg](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/plugin_builder_v3.jpg){: .img-center loading=lazy }

Une fois le formulaire validé, il vous sera alors proposé d'enregistrer l'architecture de votre plugin avec les différents fichiers.
Choisissez le répertoire le répertoire "plugins" qui se trouve dans `/home/user/.qgis2/python/plugins/` pour Linux et `C:\Users\Nom_Utilisateur\.qgis2\python\plugins` pour Windows.

QGIS, au démarrage, scanne le dossier "plugins" et charge alors les différents plugins. Il est donc nécessaire de redémarrer QGIS pour qu'il soit pris en compte la première fois.

Pendant le redémarrage de QGIS, regardons les fichiers de notre plugin :

```bash
[etienne:/home/etienne/.qgis2/python/plugins/ShowActiveLayer] $ lshelp i18n icon.png __init__.py Makefile metadata.txt plugin_upload.py pylintrc README.html README.txt resources.qrc scripts show_active_layer_dialog_base.ui show_active_layer_dialog.py show_active_layer.py test
```

Regardons immédiatement ce que fait le nôtre :

1. Démarrez QGIS
2. Cliquez sur extensions puis Gestionnaire des extensions.
3. Maintenant après avoir tapé "layer" dans le champ de recherche, vous devriez voir le plugin s'afficher.
4. Une fois sélectionné, une nouvelle icône sera automatiquement placée dans votre barre d'outils.

Si vous passez votre souris sur le bouton, une infobulle contenant la description de votre plugin s'affichera alors. Pour le moment notre plugin ne fait absolument rien d'autre qu'afficher une fenêtre contenant le bouton "ok" et "cancel". Rien de très extraordinaire !

Néanmoins, avant de commencer à coder, nous allons installer le plugin "reloader". Celui-ci permet de ne pas avoir à fermer puis ouvrir à nouveau QGIS quand vous modifierez votre plugin.

----

### Installation du plugin Reloader

En phase de développement, vous allez effectuer (je l'espère) de nombreuses modifications.
Pour éviter d'avoir à redémarrer QGIS à chaque fois nous allons installer le plugin Reloader :

1. Allez dans "extensions"
2. puis "Récupérateur des extensions python"
3. Ensuite dans l'onglet "options" cochez "Affichez toutes les extensions, mêmes celles encore expérimentales".
4. Enfin, une fois la liste des extensions mises à jour, le plugin reloader devrait être disponible.

Installons-le immédiatement et commençons à le paramétrer.

Si vous tapez la combinaison de touches `alt+F5`, une fenêtre vous demandant de sélectionner le plugin que vous souhaitez recharger automatiquement apparaît. Sélectionnez `showactivelayer`.

Maintenant, à chaque fois que vous appuierez sur la touche `F5`, celui-ci se rechargera automatiquement. Faisons le test immédiatement et modifions le texte qui s'affiche au passage de la souris.

1. Ouvrez le fichier `showActiveLayer.py` dans `.qgis/python/plugins/`
2. Ensuite, ajoutez par exemple un point d'exclamation à la fin de la phrase "Show Active Layer".
3. Retournez maintenant à QGIS et appuyez sur F5. Le texte est alors automatiquement mis à jour.

Maintenant, que nous disposons des bases nécessaires, explorons un peu l'API de QGIS et surtout commençons concrètement à créer notre plugin.

----

### A la découverte de l'API de QGIS

L'[API](http://doc.qgis.org/) de QGIS est riche, vous pourrez, à travers les [différentes classes](http://doc.qgis.org/stable/classes.html) (plus d'une centaine), accéder à la totalité des composants du logiciel. Avant de commencer concrètement à créer notre plugin attardons-nous un peu sur celle-ci. Vous verrez ce n'est pas du temps perdu car vous aurez très souvent recours à l'API. C'est en quelque sorte votre encyclopédie des méthodes et des attributs du logiciel.

Pour commencer, nous allons utiliser la console python disponible dans QGIS. Pour cela, une fois votre logiciel démarré et une couche chargée, allez dans extensions et sélectionnez Console python. Une nouvelle fenêtre devrait alors s'ouvrir. Nous allons maintenant effectuer quelques opérations de bases afin de nous familiariser avec l'API :

```python
>>> mapCan = qgis.utils.iface.mapCanvas()
>>> mapCan.layerCount()
1
>>> lay = mapCan.layer(0)
>>> print lay.name()
TM_WORLD_BORDERS-0.3
>>> lay.setLayerName("World Border")
>>> print lay.name()
World Border
```

La classe principale que vous manipulerez le plus souvent est [mapCanvas](http://doc.qgis.org/stable/classQgsMapCanvas.html). Celle-ci est votre porte d'entrée vers les différents composants relatifs à la carte. Je vous conseille de vous y attarder, elle vous sera certainement très utile plus tard.

Mais bon, trêve de bavardage passons maintenant à notre plugin.

----

## Création du plugin

Allez, vous devez avoir les doigts qui vous démangent non ? Alors commençons sans plus attendre ! La création d'un plugin se divise en deux niveaux. Le premier qui peut être accessoire, est le design de l'interface graphique. Le second consiste à implémenter concrètement ce que devra réaliser notre future application.

### Création de l'interface

Deux solutions s'offrent à vous :

- Soit modifier le fichier `UI_NomDuPlugin.py` en y ajoutant les différents que vous souhaitez,
- ou utiliser le programme QT Designer.Ce dernier permet de dessiner vos éléments puis de générer ensuite le code correspondant.

C'est cette seconde alternative que nous choisirons, pour des raisons évidentes de simplicité. La démarche de création est facilitée du fait qu'à l'intérieur de votre répertoire se trouve un fichier `Ui_NomDuPlugin.ui`. C'est ce format qui est utilisé par QT Designer. Ainsi, une fois ce dernier démarré, sélectionner le fichier portant l'extension `.ui`.

![list_view_new.png](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/list_view_new.png){: .img-center loading=lazy }

Voilà une fois nos différents éléments placés comme nous le souhaitons, il va falloir compiler notre fichier xml `Ui_NomDuPlugin.ui`. Cela se passe en ligne de commande de la manière suivante :

```bash
pyuic4 -o tmp.py -x Ui_showActiveLayer.ui
```

Par sécurité j'ai préféré créer un fichier temporaire nommé `tmp.py` plutôt que d'écraser `UI_NomDuPlugin.py`.  
J'ouvre maintenant ces deux fichiers dans mon éditeur de texte et je remplace les éléments de `UI_NomDuPlugin.py` par les éléments de `tmp.py`.

J'obtiens maintenant le code suivant :

```python
from PyQt4 import QtCore, QtGui

class Ui_showActiveLayer(object):
    def setupUi(self, showActiveLayer):
        showActiveLayer.setObjectName("showActiveLayer")
        showActiveLayer.resize(389, 279)
        self.buttonBox = QtGui.QDialogButtonBox(showActiveLayer)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.plainTextEdit = QtGui.QPlainTextEdit(showActiveLayer)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 30, 361, 201))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtGui.QLabel(showActiveLayer)
        self.label.setGeometry(QtCore.QRect(10, 10, 181, 17))
        self.label.setObjectName("label")
        self.retranslateUi(showActiveLayer)
        QtCore.QObject.connect(
            self.buttonBox,
            QtCore.SIGNAL("accepted()"),
            showActiveLayer.accept
            )
        QtCore.QObject.connect(
            self.buttonBox,
            QtCore.SIGNAL("rejected()"),
            showActiveLayer.reject
            )
        QtCore.QMetaObject.connectSlotsByName(showActiveLayer)

    def retranslateUi(self, showActiveLayer):
        showActiveLayer.setWindowTitle(
            QtGui.QApplication.translate(
                "showActiveLayer",
                "showActiveLayer",
                None,
                QtGui.QApplication.UnicodeUTF8
                )
            )
        self.label.setText(
            QtGui.QApplication.translate(
                "showActiveLayer",
                "Les couches actives sont :",
                None,
                QtGui.QApplication.UnicodeUTF8
                )
            )

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    showActiveLayer = QtGui.QDialog()
    ui = Ui_showActiveLayer()
    ui.setupUi(showActiveLayer)
    showActiveLayer.show()
    sys.exit(app.exec_())
```

Et voilà, si vous mettez à jour, dans QGIS, votre plugin (F5), vous verrez que l'interface a été modifiée :

![qgis_plugin_show.png](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/qgis_plugin_show.png){: .img-center loading=lazy }

Pour le moment la liste est vide. En effet, notre plugin ne fait absolument rien. Réalisons immédiatement les modifications nécessaires. Cela nous permettra de comprendre concrètement comment fonctionne un plugin, mais cette fois côté code !

#### Implémentation du code

Dans le dossier `showactivelayer` vous devez avoir un fichier nommé `showActiveLayer.py`. C'est celui-ci que nous utiliserons pour spécifier à QGIS ce qu'il est nécessaire de faire.

Laissons les premières méthodes (`__init__`, `initGui` et `unload`) et intéressons-nous à `run()`. C'est au sein de celle-ci que se passera l'essentiel de nos actions. Rappelez-vous, nous souhaitons afficher dans notre zone de texte la liste des couches actives. Pour cela nous avons besoin d'un connecteur vers la carte. Cela se fait de la manière suivante :

```python
mapCanvas = self.iface.mapCanvas()
```

Ensuite, il me suffit de faire une boucle sur les différentes couches de la carte ce qui me permet de créer ma chaîne de caractère que j'incorporerai ensuite à ma zone de texte :

```python
layerName = ""
for i in range(mapCanvas.layerCount()-1,-1,-1):
    layer = mapCanvas.layer(i)
    layerName += layer.name()+"\n"
```

Et enfin, comme nous l'avons déjà précisé, nous allons ajouter notre chaîne de caractère à notre zone de texte :

```python
dlg = showActiveLayerDialog()
dlg.ui.plainTextEdit.appendPlainText(layerName)
```

Et voilà le code complet :

```python
# run method that performs all the real work
def run(self):
    mapCanvas = self.iface.mapCanvas()
    if mapCanvas.layerCount() == 0:
        QMessageBox.warning(
            self.iface.mainWindow(),
            "Show Active Layer Plugin",
            ("No active layer found"),
            QMessageBox.Ok
            )
        return

    layerName = ""
    for i in range(mapCanvas.layerCount()-1,-1,-1):
        layer = mapCanvas.layer(i)
        layerName += layer.name()+"\n"

    # create and show the dialog
    dlg = showActiveLayerDialog()
    dlg.ui.plainTextEdit.appendPlainText(layerName)
    dlg.show()
    result = dlg.exec_()
    # See if OK was pressed
    if result == 1:
        QMessageBox.warning(
            self.iface.mainWindow(),
            "Show Active Layer Plugin",
            ("Voulez allez quitter le plugin !"),
            QMessageBox.Ok
            )
```

Ce qui nous donne donc :

![plugin_final.png](https://cdn.geotribu.fr/img/articles-blog-rdp/logiciels/qgis/plugin_final.png){: .img-center loading=lazy }

----

## Conclusion

L'intérêt technique de ce plugin est très limité. Mais l'objectif était de vous fournir les bases nécessaires ainsi que les différentes ressources disponibles afin que vous puissiez ensuite réaliser vos propres applications. J'espère ainsi que ce billet vous aura permis de vous familiariser avec cet environnement de développement. L'API de QGIS, riche et complète, offre tous les éléments nécessaires afin que vous puissiez laisser libre cours à votre imagination alors n'hésitez pas à la découvrir vous même et à réaliser vos propres applications.

### Ressources

- l'inévitable [Bible](http://docs.python.org/index.html) de Python ;
- les [classes](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/html/classes.html) de PyQt ;
- et également une [introduction](http://www.riverbankcomputing.co.uk/static/Docs/PyQt4/pyqt4ref.html) à Pyqt ainsi que [celui-ci](http://zetcode.com/tutorials/pyqt4/) ;
- la [documentation](http://mapserver.sk/~wonder/qgis/html/index.html) (non officielle ?) de PyQGIS ;
- les différentes [classes](http://doc.qgis.org/stable/classes.html) de PyQGIS ;
- la création d'un plugin QGIS sur le site [Soft Libre](http://softlibre.gloobe.org/qgis/workshop/plugin).

----

<!-- geotribu:authors-block -->
