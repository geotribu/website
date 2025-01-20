---
title: "O3D, ou comment intégrer de la 3D dans votre navigateur grâce à Google"
authors:
    - Geotribu
categories:
    - article
comments: true
date: 2009-04-22
description: "O3D, ou comment intégrer de la 3D dans votre navigateur grâce à Google"
tags:
    - Google
    - O3D
---

# O3D, ou comment intégrer de la 3D dans votre navigateur grâce à Google

:calendar: Date de publication initiale : 22 avril 2009

![globe news](https://cdn.geotribu.fr/img/internal/icons-rdp-news/world.png){: .img-thumbnail-left }

Google vient juste de finaliser [O3D](http://code.google.com/apis/o3d/), à la fois plugin (en C++) et [API javascript](http://code.google.com/apis/o3d/docs/utilitylist.html) permettant la création d'environnement 3D au sein d'un navigateur. Les exemples et vidéos disponibles en [démo](http://code.google.com/apis/o3d/docs/samplesdirectory.html) sont des plus intéressantes Il est facile d'imaginer les applications WEB et SIG/WEB qu'il serait possible de réaliser.

Côté développeur, tout s'effectue en JavaScript (vivement une généralisation de [TraceMonkey](http://3liz.com/blog/rldhont/index.php/2008/08/23/174-tracemonkey-une-bonne-nouvelle-pour-le-sig-en-javascript)).

Des objets provenant des logiciels 3D Studio Max, Maya, et Google SketchUp peuvent également être importés. De plus les fonctionnalités de base sont également très riches (création de [textures](http://code.google.com/apis/o3d/docs/samplesdirectory.html#textures), [shaders](http://code.google.com/apis/o3d/docs/samplesdirectory.html#shaders)...). Voici quelques lignes de code "hello world" à la sauce O3D permettant d'afficher un cube. Du code javascript ni plus ni moins :  

```javascript
<script type="text/javascript">
o3djs.require('o3djs.util');
o3djs.require('o3djs.math');
o3djs.require('o3djs.rendergraph');

// Create a Shape object for the mesh.
var cubeShape = g_pack.createObject('Shape');

// Create the Primitive that will contain the geometry data for
// the cube.
var cubePrimitive = g_pack.createObject('Primitive');

// Create a StreamBank to hold the streams of vertex data.
var streamBank = g_pack.createObject('StreamBank');
</script>
```

L'architecture d'O3D est présentée ci-dessous :

![Google O3D](https://cdn.geotribu.fr/img/articles-blog-rdp/capture-ecran/google_o3d_schema_software_stack.png "Google O3D"){: .img-center loading=lazy }

Google avec O3D a pour objectif de créer un nouveau standard Web. Mais, avec l'arrivée prochaine du HTML 5 et le développement de [Canvas 3D](https://wiki.mozilla.org/Canvas:3D) (et également [3D Canvas JS Library](http://www.c3dl.org/)), lequel de ces standards restera ?

----

<!-- geotribu:authors-block -->
