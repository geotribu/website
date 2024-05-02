---
title: Afficher une carte dans une application Android
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-11-20
description: Afficher une carte dans une application Android
tags:
    - Android
---

# Afficher une carte dans une application Android

:calendar: Date de publication initiale : 20 novembre 2009

## Introduction

Nous allons ici apprendre à insérer une carte Google Maps dans une application Android (OS Google pour les téléphones portables).  

Ce tutoriel précise les étapes indispensables de configuration de votre atelier de développement pour y parvenir.

### Créer une cible typée cartographie pour l'émulateur

Allez dans le répertoire tools de votre sdk 1.5, et tapez la commande :  

`android list targets`  

Vous devriez avoir un résultat semblable à ceci :  

```sh
Available Android targets:
id:1
    Name: Android 1.1
    Type: platform
    API level: 2
    Skins: HVGA (default), HVGA-L, HVGA-P, QVGA-L, QVGA-P
id:2
    Name: Android 1.5
    Type: platform
    API level: 3
    Skins: HVGA (default), HVGA-L, HVGA-P, QVGA-L, QVGA-P
id:3
    Name: Google APIs
    Type: add-on
    Vendor: Google Inc.
    Description: Android + Google APIs
    Based on Android 1.5 (API level 3)
    Libraries:
    * com.google.android.maps (maps.jar)
        API for Google Maps
    Skins: HVGA (default), HVGA-L, QVGA-P, HVGA-P, QVGA-L
```  

Vous pouvez alors créer un nouvel AVD (Android Virtual Device)  

```sh
android create avd -n  -t
```

Par exemple :

```sh
android create avd -n avd3 -t 3
```  

Ensuite vous pouvez vérifier la création de votre AVD ciblé pour la cartographie en tapant  

```sh
android list avds

résultat :

Available Android Virtual Devices:
    Name: avd1
    Path: C:\Users\Loic\.android\avd\avd11.avd
  Target: Android 1.1 (API level 2)
    Skin: HVGA
---------
    Name: avd2
    Path: C:\Users\Loic\.android\avd\avd12.avd
  Target: Android 1.5 (API level 3)
    Skin: HVGA
---------
    Name: avd3
    Path: C:\Users\Loic\.android\avd\avd13.avd
  Target: Google APIs (Google Inc.)
          Based on Android 1.5 (API level 3)
    Skin: HVGA
```

Votre émulateur pouvant afficher des cartes est maintenant créé.

## Créer l'application dans Eclipse

### Nouveau projet avec cible spécifique

Dans Eclipse, créez un nouveau projet Android, et veillez bien à sélectionner Google APIs comme cible :

![Eclipse](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/android_tuto_1_newproject.png "Eclipse"){: .img-center loading=lazy }

### Adaptation du manifest

La librairie Google APIs ne fait pas parti du socle standard Android, il faut spécifier cette utilisation dans le manifest AndroidManifest.xml.  

Ajoutez sous la balise `<application>`

```xml
<uses-library android:name="com.google.android.maps" />
```

Les tuiles Google Maps sont téléchargées dynamiquement via Internet, il faut donc donner l'autorisation d'accés à Internet à votre d'application.  

Ajoutez sous la balise `<manifest>`  

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

### Quel Layout pour une carte

Il faut maintenant declarer une MapView dans vote Layout principal.  

Dans `/res/layout/main.xml`, insérer ce code qui déclare qu'une carte cliquable va occuper toute la fenêtre.  

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:id="@+id/mainlayout"
    android:orientation="vertical"
    android:layout_width="fill_parent"
    android:layout_height="fill_parent" >

    <com.google.android.maps.MapView
        android:id="@+id/mapview"
        android:layout_width="fill_parent"
        android:layout_height="fill_parent"
        android:clickable="true"
        android:apiKey="Your Maps API Key"
    />

</RelativeLayout>
```

Il manque donc ici votre Maps API Key qui prouve que vous êtes enregistré auprés de Google pour utiliser son service. Voyons maintenant comment la récupérer.

### Obtenir une Maps API Key

Il faut d'abord obtenir votre empreinte du certificat (MD5) pour votre atelier de développement.  

Pour cela, il suffit de taper la commande suivante (keytool est disponible dans votre JDK) :  

`keytool -list -alias androiddebugkey -keystore <path_to_debug_keystore>\debug.keystore -storepass android -keypass android`  

Le fichier `debug.keystore` est stocké dans un répertoire dépendant de votre OS :  

```conf
Windows Vista: C:\Users\<user>\.android\debug.keystore
Windows XP: C:\Documents and Settings\<user>\.android\debug.keystore
OS X and Linux: ~/.android/debug.keystore
```

Vous devriez obtenir ceci :  

```sh
androiddebugkey, 14 mai 2009, PrivateKeyEntry,
Empreinte du certificat (MD5) : 32:39:0C:F0:2D:48:32:A5:7C:3D:6A:xx:xx:xx:xx:xx
```

Muni de cette empreinte, allez sur le site <http://code.google.com/android/maps-api-signup.html> .  

Si vous n'avez pas de compte Google , c'est le moment d'en créer un.  

Acceptez les conditions et entrez votre empreinte. Vous obtiendrez votre clé Maps API, qu'il suffit de mettre dans votre fichier de Layout.

### Un peu de java, enfin

Voici le code le plus simple pour afficher une carte dans votre application.  

```javascript
package com.test;

import com.google.android.maps.MapActivity;
import android.os.Bundle;

public class MainActivity extends MapActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
    }

    protected boolean isRouteDisplayed() {
        return false;
    }

}
```

Votre activité est une MapActivity et non une Activity simple. Il faut donc implémenter la méthode isRouteDispayed().  

Lancez l'émulateur, vous devriez voir ceci :

![Google Maps - Carte](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2009/android_tuto_1_run.png "Google Maps - Carte"){: .img-center loading=lazy }

## Remarques

Liens utiles :  

- Eclipse : <http://www.eclipse.org/downloads/>  
- Android Developers : <http://developer.android.com/intl/fr/index.html>  
- Android SDK : <http://developer.android.com/intl/fr/sdk/index.html>

## Conclusion

Ce premier tutoriel à propos d'Android peut sembler un peu technique, mais il s'agit surtout de bien configurer son atelier de développement. Pour insérer des cartes Google Maps dans Android, vous ne pouvez pas simplement développer des pages html/javascript avec l'API Google Maps, il faut penser 'application' et non 'client léger', même si, je vous l'accorde les clients légers ne sont plus légers que par leur nom. Ici vous allez pouvoir profiter de toute l'API Android qui peut récupérer beaucoup d'informations intéressantes (localisation GPS ,accéleromètre, ...). D'autres tutoriels viendront pour éclairer ces points.

----

<!-- geotribu:authors-block -->
