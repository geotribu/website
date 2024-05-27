---
title: "Un peu de websocket avec Django"
authors:
    - Arnaud VANDECASTEELE
categories:
    - article
comments: true
date: 2013-11-19
description: "Un peu de websocket avec Django"
tags:
    - Python
    - Django
    - WebSocket
---

# Un peu de websocket avec Django

:calendar: Date de publication initiale : 19 novembre 2013

Dans son billet intitulé ["Du web, des socquettes et de la carto](2013-02-25_websocket.md)", Fabien nous avait gratifié d'un super tuto sur les potentialités du Web "temps réel". Par temps réel, j'entends le fait d'avoir une communication bi-directionnelle persistante entre le client et le serveur. En effet, à l'heure actuelle, la grande majorité du web fonctionne en mode pull. C'est-à-dire que c'est le client qui va interroger le serveur à intervalle régulier. En plus d’être une approximation d'un fonctionnement temps-réel, cette approche entraine une utilisation inutile de ressources informatiques d'autant plus qu'il peut arriver qu'il n'y ait eu aucun changement.

C'est pourquoi il serait beaucoup plus intéressant que cela soit le serveur qui contacte directement le client en cas de changement. C'est ce que l'on nomme le mode push. Jusqu'à l'arrivée du HTML 5, cela n'était pas nativement prévu. Il était donc nécessaire de passer par [différentes alternatives](https://en.wikipedia.org/wiki/Comet_%28programming%29) comme le long polling, le Ajax Push, les forever iframes ou encore les [adobe Flash socket](http://help.adobe.com/en_US/as3/dev/WSb2ba3b1aad8a27b0-181c51321220efd9d1c-8000.html). Ne rentrons pas dans les détails de ces alternatives, l'important est de retenir que si techniquement cela était possible ce n'était tout d'abord pas standardisé et pas toujours très propre. En gros chacun faisait un peu à sa sauce dans son coin, on fait mieux en terme de réutilisabilité !

Du coup l'arrivée du HTML 5 et surtout de son [API websockets](https://html.spec.whatwg.org/multipage/web-sockets.html) (voir aussi sur [l'article de wikipedia](https://fr.wikipedia.org/wiki/WebSocket)) arrive à point nommé. Celle-ci permet bien évidemment de créer cette fameuse communication bi-directionnelle persistante entre le client et le serveur mais surtout offre un moyen standardisé de le faire. Plus de bidouilles on part enfin sur des bases solides. Mais (oui y'a toujours un mais), même si c'est de moins en moins le cas il n'en reste pas moins que tous les navigateurs ne sont pas encore compatibles HTML 5. Comment faire alors ? Vous avez bien évidemment le choix de vous appuyer uniquement sur cette API, mais cela signifie alors que votre service ne sera visible que par quelques privilégiés. Un peu embêtant tout de même. C'est là qu'arrive la fameuse bibliothèque [Socket.IO](https://socket.io/) dont le but est d'unifier l'utilisation des web socket au travers d'une seule interface. Ainsi, en fonction des caractéristiques de votre navigateur, Socket.IO va définir automatiquement la solution la plus adaptée (Websocket, Ajax long polling, Multipart XHR, etc.).

Bon c'est bien beau tout ce blabla, mais on en fait quoi de tout ça ? Ok, je vois vous avez envie de mettre les mains dans le cambouis ! Commençons donc immédiatement notre tour d'horizon. Tout d'abord, pourquoi utiliser Django (python) alors que Fabien l'avait déjà fait avec PHP. Réponse courte pour le fun et le challenge, réponse de troll parce que PHP ça pue. Surtout, je n'ai pas trouvé sur internet de tutoriel, genre le websocket avec Django pour les nuls.

----

Dans ce tuto, nous allons nous concentrer sur l'intégration des websockets dans Django. C'est pourquoi notre exemple sera volontairement le plus simple possible. Exemple que vous pouvez d'ailleurs télécharger sur ce [dépôt Git](https://github.com/arno974/django-socketio-example). Pas de carto, pas de trucs de sioux, juste un formulaire et une liste à puce. À chaque fois que quelqu'un valide le formulaire, le contenu de celui-ci est automatiquement et immédiatement répercuté sur les autres navigateurs qui seraient sur la même page. Je ne l'ai pas précisé, mais cela suppose que vous avez déjà créé un projet Django. Si ce n'est pas le cas, c'est le moment de lancer un petit 'startproject'.

Si vous avez bien suivi l'intro, les websockets ça se passe côté client mais aussi côté serveur. Nous allons devoir écrire du code pour chacun d'eux.

## Côté serveur

Côté serveur, nous avons bien évidemment besoin d'un système qui autorise et qui permet de garder cette connexion communication bi-directionnelle persistante. [Différentes solutions existent](http://stackoverflow.com/questions/1253683/what-browsers-support-html5-websocket-api/2700609#2700609), et cela dans différents langages. Certaines sont de "simples" bibliothèques qui vont implémenter le protocole websockets. C'est le cas notamment de [pywebsocket](http://code.google.com/p/pywebsocket/) et [gevent-websocket](https://bitbucket.org/Jeffrey/gevent-websocket/) en python, [Ratchet](http://socketo.me/) en PHP ou encore [jWebsocket](http://jwebsocket.org/) en Java. D'autres solutions sont des systèmes complets spécifiquement conçes pour ce mode d'utilisation. C'est le cas notamment de [Node.js](http://nodejs.org/), [Tornado](https://github.com/facebook/tornado) ou encore [APE](http://ape-project.org/).

Dans le cadre de notre exemple, nous allons volontairement rester le plus simple possible et utiliser les potentialités offertes par la bibliothèque `django-socketio`. Celle-ci se base sur la bibliothèque [gevent](https://www.gevent.org/) et permet permet une intégration facile et rapide des websockets directement dans Django. Néanmoins, comme cela est précisé sur la page du projet, cette bibliothèque n'est plus à jour avec les dernières versions de socket.io et du coup celle-ci n'implémente pas les dernières spécifications des websockets. Il peut donc arriver que sur certains navigateurs cela ne fonctionne pas.

Passons immédiatement au code. Tout d'abord, nous allons créer une application (*commande django startapp*) et l'ajouter, ainsi que l'application django_socketio, à la liste des applications (*INSTALLED_APPS*) de notre fichier settins.py.

Une fois réalisé, mettons les mains dans le cambouis. Enfin, en réalité nous n'allons pas beaucoup nous salir, car les modifications sont minimes. Tout d'abord nous allons modifier notre fichier **urls.py** et y ajouter la ligne "*url("", include('django_socketio.urls'))*".

Puis nous allons créer (dans le dossier de notre application) un fichier **events.py** qui contiendra à peine une quinzaine de lignes. Pourquoi events.py ? En réalité, vous pouvez créer le fichier que vous voulez du moment que celui-ci est chargé au démarrage de Django. Mais par défaut, django-socketio, cherche un fichier events.py nous allons donc lui faciliter le travail en gardant cette configuration. Détaillons immédiatement ce fichier :

```python
from django_socketio import events

@events.on_connect()
def connect(request, socket, context):
    message = {"action" : "system-info", "text" : "connexion ok"}
    socket.send(message)

@events.on_subscribe(channel="^room-")
def connect(request, socket, context, channel):
    message = {"action" : "system-info", "text" : " - on subscribe ok"}
    socket.send(message)

@events.on_message(channel="^room-")
def message(request, socket, context, message):
    socket.send_and_broadcast_channel(message)
```

Celui-ci n'est pas bien compliqué à comprendre. En effet, nous avons spécifié trois types [d'événements](https://github.com/stephenmcd/django-socketio#events) (message, subscribe et connect) auquel notre serveur va réagir.

`Connect` et `subscribe` vont retourner des informations générales spécifiant que notre connexion est valide. Ces informations ne devant être vues uniquement que par l'utilisateur connecté, nous utilisons la méthode `send()`. Par contre, le dernier événement message est plus intéressant car c'est lui qui va envoyer le message à l'ensemble des utilisateurs connectés. Cela se fait à l'aide de la méthode `send_and_broadcast_channel()`.

Et voilà, c'est tout ! Nous avons notre serveur prêt à répondre aux requêtes. Passons maintenant au code à écrire côté client.

## Côté client

Comme je le soulignais, le code et la structure de la page vont être volontairement très simples. Ci-dessous est présentée l'organisation générale de notre page (sans le code). Vous remarquerez la présence des balises 'socketio_tags' et 'socketio'. Celles-ci ajoutent automatiquement les scripts javascripts nécessaires à l'utilisation de socket.io.

```html
<html xmlns="<http://www.w3.org/1999/xhtml>">

<head>
    <title>Mon gabarit de page</title> <!-- [1] Appel du JS et du CSS -->
    <link rel="stylesheet" href="../../lib/OpenLayers-2.10/theme/default/style.css" type="text/css" />
    <script src="../../lib/OpenLayers-2.10/OpenLayers.js"></script> <!-- [2] Notre futur code JS -->
    <script type="text/javascript"> function init() { //Futur emplacement de notre code } </script>
</head> <!-- [3] Appel de la fonction init au chargement de la page -->

<body onload="init()">
    <!-- [4] Notre balise qui contiendra la map -->
    <div id="map_div"></div>
</body>

</html>
```

Le corps de cette page est constitué de trois principaux éléments. Un indicateur de connexion (`id=status`), notre formulaire et enfin une liste (`id=messages`) qui est vide pour le moment. Concentrons-nous maintenant sur le code javascript. Afin d'en faciliter sa compréhension, celui-ci sera décrit étape par étape.

Dans un premier temps, il est nécessaire de créer notre web socket. Cela se fait en faisant appel au constructeur `new io.Socket()`. Puis, avec la méthode `connect()`, nous spécifions. Ensuite, nous définissons [différents événements](https://github.com/LearnBoost/socket.io/wiki/Exposed-events#client) qui déclencheront des actions spécifiques.

Bien qu'en théorie, vous pouvez même définir vos propres événements, il ne me semble pas que la [classe events](https://github.com/stephenmcd/django-socketio/blob/master/django_socketio/events.py) de django-socketio chargée d'interpréter ces événements côté serveur prenne cela en charge. C'est pourquoi nous n'utiliserons que les événements les plus courants tels que `connect`, `message`, `disconnect` ou encore `error`.
De toute façon, pour notre application, ces événements par défaut sont bien suffisants et il est toujours possible de faire, côté serveur, des *switch case* sur l'événement message.

Revenons à notre code, dans celui-ci nous avons défini deux types d'événements : `connect` et `message`. Le premier se déclenchera lorsque la connexion entre notre client et notre serveur sera établie. Le second sera déclenché lorsqu'un message sera émis par le serveur. Chacun d'eux prend en argument une fonction (`connected` et `messaged`) qui sera appelée lors de la réalisation de cet événément.

```javascript
$(function () {
    var socket;
    var start = function () {
        socket = new io.connect(); //création de la websocket
        socket.connect('<http://localhost:9000>');//connexion à notre serveur local
        socket.on('connect', connected);//définition d'une action à la connexion
        socket.on('message', messaged);//définition d'une action lors de la réception d'un message
    };
    start();
});
```

Spécifions donc immédiatement chacune de ces fonctions. La première (`connected`) spécifie simplement le canal (`room-1`) sur lequel nous sommes connectés. Dans notre exemple, cela n'est pas utile, mais sachez que cela existe et que cela vous permet de disposer de plusieurs interfaces de communication. La seconde fonction fait un peu plus de choses. Tout d'abord, nous avons spécifié une structure conditionnelle (`switch`) en fonction du type de message retourné par le serveur. Deux conditions (`message` et `system-info`) ont été définies. La première est celle qui nous permettra d'afficher les messages des utilisateurs. Nous ne faisons pas grand chose à part, récupérer le message initial et ajouter juste avant le moment où il a été reçu. La seconde condition est surtout là à titre indicatif afin de vérifier que notre connexion s'est correctement déroulée. En fonction du résultat de cette condition, le texte de notre balise `system-info` sera modifié.

```javascript
$(function () {
    var socket;
    var connected = function () {
        socket.subscribe('room-1');
    };
    var messaged = function (msg) {
        switch (msg.action) {

            case 'message': var d = new Date();
            var win = $(window), doc = $(window.document);
            var bottom = win.scrollTop() + win.height() == doc.height();
            msg.time = $.map([d.getHours(), d.getMinutes(), d.getSeconds()], function (s) { s = String(s);
                return (s.length == 1 ? '0' : '') + s;
            }).join(':');
            $('#messages').append($('#messages').append(msg.time + " - " + msg.text));
            if (bottom) {
                window.scrollBy(0, 10000);
            }
            break;

            case 'system-info': if ($('#system-info').html() === "En attente de la connexion.") {
                $('#system-info').html(msg.text);
            } else {
                $('#system-info').append(msg.text);
            } break;
        }
    };
    var start = function () { socket = new io.connect(); //création de la websocket
        socket.connect('<http://localhost:9000>');//connexion à notre serveur local
        socket.on('connect', connected);//définition d'une action à la connexion
        socket.on('message', messaged);//définition d'une action lors de la réception d'un message
    };
    start();
});
```

Maintenant que nous avons spécifié le comportement de notre application lors d'un événement provenant de notre serveur, il nous reste à interagir avec lui. En effet, ce que je souhaite c'est que lorsqu'un utilisateur poste un message à partir du formulaire, celui-ci soit automatiquement transmis à l'ensemble des utilisateurs connecté à notre canal. Pour cela, nous spécifions qu'à la soumission du formulaire, il est nécessaire de récupérer le texte écrit dans notre balise '#message' et d'envoyer cela à notre serveur grâce à la méthode `send()`. Afin d'éviter que la page ne se recharge nous avons également précisé que le résultat de cette soumission renverra toujours false.

```javascript
$(function () {
    [...]
    $('form').submit(function () {
        var value = $('#message').val();
        if (value) {
            data = { action: 'message', text: value
        };
        socket.send(data);
    }
    $('#message').val('').focus();
    return false;
});
[...]
});
```

Et voilà, notre puzzle est maintenant complet et notre système devrait réagir comme il faut. Il ne nous reste plus qu'à vérifier cela en lançant notre serveur de test en utilisant la commande `python manage.py runserver_socketio localhost:9002`.

Et voilà, le tour est joué. Pour un simple test vous pouvez ouvrir deux navigateurs et vous amuser à écrire n'importe quoi. Il ne vous reste plus maintenant qu'à faire de vraies applications :celebration:

----

## Conclusion

La prise en main de ce concept de websockets bien que pas très compliqué m'a tout de même pris du temps. Le problème étant surtout lié à la compréhension de la bibliothèque django-socketio. Au final, ça fonctionne, mais c'est presque trop magique. La question que je me pose est combien de connexions est capable de supporter cette architecture ? Au départ, je souhaitais aller au plus simple et tout intégrer dans django, mais après réflexion, je me demande s'il ne vaut pas mieux utiliser un serveur dédié type [APE](http://ape-project.org/) ou [node.js](http://nodejs.org/).

Chacun s'occupe de ce dans quoi il est bon. Si vous avez plus d'infos concernant ces technos ou si vous voyez des erreurs, n'hésitez pas à m'en faire part dans vos commentaires.

## Ressources complémentaires

* [Démo d'un module de tchat](http://html5demos.com/web-socket) utilisant WebSocket en html5 (motorisé sur nodejs)
* Tutoriel pour [comprendre et commencer avec WebSocket](http://www.html5rocks.com/en/tutorials/websockets/basics/) (en anglais)
* Tutoriels sur [HTML5 Professor](http://html5professor.com/tutoriels-7.html) (en français malgré le nom)
* [Site officiel de Web Socket](http://www.websocket.org/)

----

<!-- geotribu:authors-block -->
