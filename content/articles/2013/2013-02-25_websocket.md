---
title: "Du web, des socquettes et de la carto"
authors:
    - Fabien GOBLET
categories:
    - article
    - tutoriel
comments: true
date: 2013-02-25
description: "Du web, des socquettes et de la carto"
tags:
    - Leaflet
    - PHP
    - Ratchet
    - WebSocket
---

# Du web, des socquettes et de la carto

:calendar: Date de publication initiale : 25 février 2013

![logo websocket](https://cdn.geotribu.fr/img/logos-icones/divers/websocket.png "logo websocket"){: .img-thumbnail-left }

Avec un titre pareil je suis pas prêt de me faire référencer... tant pis ce sera pour les initiés :wink:. J'entends souvent parler du temps réel ; la tendance actuelle vers les objects connectés et autres interactions possibles avec des smartphones et/ou des sites web m'a fait (re)découvrir une partie du web que j'avais mise de côté. Et donc l'envie de mettre les mains dans le cambouis et regarder d'un peu plus près comment ça marche ! Et ouais on ne se refait pas.

## Introduction - légère l'intro, pas d'inquiétude :)

### Au début il y avait le web

Je me rappelle des premiers sites web que j'ai pu visiter avec ma connexion [RTC](https://fr.wikipedia.org/wiki/R%C3%A9seau_t%C3%A9l%C3%A9phonique_commut%C3%A9) : c'était un peu lent à la connexion (en fait ça mettait une plombe à s'initialiser, le modem faisait un bruit horrible ...), c'était un poil statique, les sites comportaient des gif animés et il n'y avait pas énormément de sites en ligne (dans les 25 000, je vous laisse calculer mon âge, j'étais en seconde :). Bon d'accord y'en a des [jolis](http://obsession.nouvelobs.com/mode/20110428.OBS1990/la-revanche-du-gif-anime.html) des gif animés.

### ...puis on a entendu parler du web 2.0

Là le [web](https://fr.wikipedia.org/wiki/Web_2.0) s'est un peu accéléré, je suis toujours impressionné par les technologies actuelles : ça va vite, ça interagit, ça bouge sans trop ramer, bref c'est chouette ! L'internaute est devenu un acteur du web, il pouvait influer sur le contenu d'une page ou d'une application et voir quasiment en temps réel les modifications qu'il avait apportées - selon moi l'émergence des réseaux sociaux en est l'un des exemples les plus parlant.

### ...et maintenant l'HTML5

L'[HTML5](http://www.siteduzero.com/informatique/tutoriels/apprenez-a-creer-votre-site-web-avec-html5-et-css3/technologies-liees-a-html5-canvas-svg-web-sockets) est un ensemble de technologies - il n'y a pas que le HTML ou le CSS - mais aussi les canvas, le svg, la géolocalisation, le web storage et j'en passe.

Le sujet qui nous intéresse aujourd'hui est les [websocket](https://fr.wikipedia.org/wiki/Websocket) et donc la notion de vrai temps réel (une sorte de super Ajax). [On prend sa respiration ...] Il s'agit donc d'un protocole de communication entre un client et un serveur par la mise en place d'un canal bidirectionnel entre ces deux entités : ça permet de pousser des données du serveur vers le client. Je ne suis pas trop penché sur la question du système de notifications d'Apple avec iOS mais ça semble un peu similaire (dans le principe s'entend, je ne suis pas certain du tout qu'ils utilisent ce protocole).

## C'est bien gentil tout ça, mais c'est quoi le sujet de ton tuto ?

### T'inquiète paupiette on y vient

En brut de forme : installer un serveur de websocket sans trop se galérer avec l'installation d'un serveur type [node.js](http://nodejs.org/) ou [APE](http://www.ape-project.org/). On va faire ça simple avec une bibliothèque en PHP qui implémente les websockets. Comme ça hop pas trop de souci sur le serveur de développement et on bousille pas toute la configuration qui nous a pris des années à stabiliser (y'en a un peu de vrai, c'est peut-être pas des années mais un certain temps quand même). Côté performance, aucune idée de savoir si c'est une bonne solution, mais pour une première, ça ira, on fera comme si. Mais j'ai bon espoir :) Puis nous couplerons tout ça avec Leaflet et voir si tout fonctionne.

### Ratchet

Et tiens bim, encore un truc nouveau :smile: !

En cherchant une bibliothèque PHP qui supportait les websockets je suis tombé inévitablement sur [phpwebsocket](https://code.google.com/p/phpwebsocket/) mais bon ça n'a pas l'air d'être trop mis à jour. Y'a peut-être quelque chose d'autre ? Et oui, c'est [Ratchet](http://socketo.me/) ! Allez c'est parti on va partir sur cette bibliothèque.

#### Installation

Donc facile on se rend sur le site web et hop direct à la page d'[installation](http://socketo.me/docs/install)... tiens pas de bouton 'Download'... hum... il faut utiliser [composer](http://getcomposer.org/)... que de trucs nouveaux dans ce tuto :) Donc composer est un installeur de bibliothèques qui gère les dépendances et y'en a besoin pour Ratchet. On ouvre un terminal, on se place à la racine du projet web que l'on vient de créer et hop on attaque :

```bash
toto$ curl -s <https://getcomposer.org/installer> | php -d detect_unicode=Off
```

!!! note
    J'ai ajouté `detect_unicode=Off` ne voulant pas changer cette configuration dans mon `php.ini`.

On a donc le fichier `composer.phar` téléchargé à la racine. Il faut maintenant écrire un fichier de configuration dans lequel nous ajoutons Ratchet comme dépendance. Il faut éditer un nouveau fichier `composer.json` à la racine du projet et écrire dedans :

```json
{
    "autoload": {
        "psr-0": {
            "MyApp": "src"
        }
    },
    "require": {
        "cboden/Ratchet": "0.2.*"
    }
}
```

Et maintenant on installe Ratchet en lançant la commande suivante :

```bash
toto$ ./composer.phar install
```

On se retrouve avec un nouveau fichier `composer.lock` et un répertoire `vendor` qui contient les dépendances de Ratchet pour notre projet.

----

#### Du code du code du code

C'est parti ! On crée une nouvelle classe en PHP qui va s'appeler Truc et qui écoutera les 4 événements suivants :

- `onOpen` qui est appelé quand un nouveau client se connecte ;
- `onMessage` appelé quand un message arrive ;
- `onClose` appelé quand une connexion se ferme ;
- `onError` appelé quand y'a un blème.

On édite donc un fichier PHP que l'on enregistre ici `/src/MyApp/Truc.php` - qui utilise la classe de [connexion](http://socketo.me/api/class-Ratchet.ConnectionInterface.html) et celle des [messages](http://socketo.me/api/class-Ratchet.MessageComponentInterface.html) :

```php
<?php
namespace MyApp;
use Ratchet\MessageComponentInterface;
use Ratchet\ConnectionInterface;

class Truc implements MessageComponentInterface {
    public function onOpen(ConnectionInterface $conn) {
    }

    public function onMessage(ConnectionInterface $from, $msg) {
    }

    public function onClose(ConnectionInterface $conn) {
    }

    public function onError(ConnectionInterface $conn, \Exception $e) {
    }
}>
```

Evidemment il faudra mettre deux trois trucs dans les fonctions... là en l'état ça ne fait pas grand'chose.

Maintenant il faut créer le serveur d'entrées/sorties que l'on va appeler `/bin/truc-server.php` :

```php
<<?php
use Ratchet\Server\IoServer;
use MyApp\Truc;

    require dirname(__DIR__) . '/vendor/autoload.php';

    $server = IoServer::factory(
        new Truc(),
        8080
    );

    $server->run();
?>
```

On peut d'ores-et-déjà démarrer le serveur comme ça dans un terminal juste pour voir :

```bash
toto$ php bin/truc-server.php
```

Bon en fait on voit rien... hum hum... le script a juste pris possession du terminal - on verra comment écrire des logs dans ce terminal pour voir les connexions entrantes et les actions des clients. Pour quitter c'est Ctrl+C :wink:.

On continue en éditant notre classe Truc pour remplir un peu les fonctions des 4 événements déclarés :

```php
<?php
namespace MyApp;
use Ratchet\MessageComponentInterface;
use Ratchet\ConnectionInterface;

class Truc implements MessageComponentInterface {
    protected $clients;

    public function __construct() {
        $this->clients = new \SplObjectStorage;
    }

    public function onOpen(ConnectionInterface $conn) {
        // Store the new connection to send messages to later
        $this->clients->attach($conn);

        echo "New connection! ({$conn->resourceId})\n";
    }

    public function onMessage(ConnectionInterface $from, $msg) {
        $numRecv = count($this->clients) - 1;
        echo sprintf('Connection %d sending message "%s" to %d other connection%s' . "\n"
            , $from->resourceId, $msg, $numRecv, $numRecv == 1 ? '' : 's');

        foreach ($this->clients as $client) {
            if ($from !== $client) {
                // The sender is not the receiver, send to each client connected
                $client->send($msg);
            }
        }
    }

    public function onClose(ConnectionInterface $conn) {
        // The connection is closed, remove it, as we can no longer send it messages
        $this->clients->detach($conn);

        echo "Connection {$conn->resourceId} has disconnected\n";
    }

    public function onError(ConnectionInterface $conn, \Exception $e) {
        echo "An error has occurred: {$e->getMessage()}\n";

        $conn->close();
    }
}
```

En simplifié dans l'ordre du code, on a créé un constructeur de notre Truc, à chaque nouvelle connexion on enregistre le client et on écrit un log, à chaque message qui arrive on écrit un log et on envoie le message à tous les autres clients, à chaque déconnexion on supprime le client de notre objet de stockage, et enfin à chaque erreur on écrit dans le terminal que bah y'a eu un problème.

Lançons le serveur dans un premier terminal et lançons Telnet dans 3 autres :

```bash
toto$ php bin/truc-server.php
toto$ telnet localhost 8080
toto$ telnet localhost 8080
toto$ telnet localhost 8080
```

Et tapez des insultes dans un des telnet, vous les verrez dans les autres. Et dans le log (ie. le terminal où l'on a lancé le serveur) vous pouvez fliquer les clients ;)

Cool, ça marche, on a un serveur de websockets en PHP et plusieurs clients via le protocole TCP/IP peuvent s'envoyer des messages. Maintenant il faut mettre tout ça dans le web et coupler tout ceci dans une jolie carto :)

### Un peu d'HTML/Javascript avec de la carto dedans et hop ça touche à sa fin

Il nous reste à écrire une page HTML où nos clients se connecteront. On fait donc une carte où l'on donne la possibilité à l'internaute de cliquer pour ajouter des marqueurs à l'endroit justement où il a cliqué et qui enverra un message aux autres clients qui interpréteront cela comme un marqueur d'un gars extérieur - vous allez voir c'est un poil intrusif :)

C'est parti !

A la racine du projet on édite un fichier - genre `maptruc.html` - on aura pris soin de télécharger la bibliothèque [Leaflet](http://leafletjs.com/) dans le répertoire `lib/js/leaflet/`.

Carto Truc Websocket Leaflet :)

```javascript
var stamenUrlToner = 'http://{s}.tile.stamen.com/toner/{z}/{x}/{y}.png', subDomainsStamen = ['a', 'b', 'c', 'd'], stamenAttrib = '<span style="color: #E6A21C;">GeoTribu Truc</span> - Map tiles by <a href="http://stamen.com">Stamen Design</a>, under <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a>. Data by <a href="http://openstreetmap.org">OpenStreetMap</a>, under <a href="http://creativecommons.org/licenses/by-sa/3.0">CC BY SA</a>.';

var stamenToner = new L.TileLayer(stamenUrlToner, { minZoom: 0, maxZoom: 20, attribution: stamenAttrib, subdomains: subDomainsStamen });
var map = L.map('map', { center: new L.LatLng(43.594993, 1.435489), zoom: 14, zoomControl: true, zoomAnimation: true, scrollWheelZoom: true, layers: [stamenToner] });
```

On a la carto simple (avec un joli fond de carte de chez [Stamen Design](http://stamen.com/)), maintenant il faut se connecter au serveur de websocket et ajouter des marqueurs.

On ajoute des petits marqueurs dans le répertoire `img` et on en affiche un des deux chaque fois que l'on clique sur la carte :

```javascript
var iconGeoTribu2 = L.icon({ iconUrl: 'img/icn16x28.png', shadowUrl: 'img/shadow-icn16x28.png', iconSize: [16, 28], shadowSize: [31, 28], iconAnchor: [8, 28], shadowAnchor: [8, 28], popupAnchor: [-0, -45] }); var iconGeoTribu = L.icon({ iconUrl: 'img/icn16x28-2.png', shadowUrl: 'img/shadow-icn16x28.png', iconSize: [16, 28], shadowSize: [31, 28], iconAnchor: [8, 28], shadowAnchor: [8, 28], popupAnchor: [-0, -45] }); var map =... map.on('click', function(e) { L.marker(e.latlng,{icon: iconGeoTribu}).addTo(map); });
```

Les entrées / sorties fonctionnent, reste à charger les fonctionnalités des websocket dans `/bin/truc-server.php` pour que ça fonctionne dans les navigateurs un poil récent :

```php
<?php
use Ratchet\Server\IoServer;
use Ratchet\WebSocket\WsServer;
use MyApp\Truc;

require dirname(__DIR__) . '/vendor/autoload.php';

$server = IoServer::factory( new WsServer( new Truc() ) , 8080 );
$server-run();

?>
```

Encore 8 lignes et c'est fini ! On se connecte sur le serveur de websocket et on code quelques fonctionnalités :

1. quand on clique sur la carte - ça ajoute un marqueur sur la sienne et ça envoie un message (ie. on envoie que les coordonnées du marqueur) aux autres clients
2. et quand on reçoit un message on récupère le message (des coordonnées donc, vous suivez ?) et on ajoute un marqueur d'une autre couleur sur la carte :

```javascript
var conn = new WebSocket('ws://192.168.1.184:8080'); conn.onopen = function(e) { console.log("Connection established!"); }; conn.onmessage = function(e) { var temp = e.data; var tab = temp.split(","); L.marker(new L.LatLng(tab[0],tab[1]),{icon: iconGeoTribu2}).addTo(map); }; [...] map.on('click', function(e) { L.marker(e.latlng,{icon: iconGeoTribu}).addTo(map); conn.send(e.latlng.lat+','+e.latlng.lng); });
```

Modifiez l'adresse IP à la première ligne par la votre. Et c'est tout bon !

## Et les navigateurs dans tout ça ?

Bonne nouvelle, tous les navigateurs supportent les websocket même sur smartphone :) Bon ok il en manque un... je vous le donne dans le mille... IE c'est seulement à partir de la version 10 :/ Aux 11% qui lisent GeoTribu avec IE, essayez de changer, juste comme ça pour voir, les autres navigateurs sont pas mal franchement :wink:

## La démo

!!! info
    Le serveur hébergeant la démonstration n'étant plus disponible depuis de nombreuses années, la démonstration, autre fois intégrée en iFrame est désactivée.  
    `<iframe src="http://88.191.142.86/labs/websocket/maptruc.html" width="640" height="480" frameborder="0"></iframe>`

!!! tip
    Bon c'est sûr, il faut que plusieurs visiteurs soient sur le tuto en même temps pour voir quelque chose... Au pire ouvrez deux onglets et jouez avec vous-même.

Pour la pleine page c'est par [ici](http://88.191.142.86/labs/websocket/maptruc.html).

Si vous êtes seul sur ce tuto mais que vous avez un smartphone sous la main - testez la démo avec ! Flashouillez le code et hop cliquez sur la carte.

![Flashouillez le code](https://cdn.geotribu.fr/img/articles-blog-rdp/divers/qrcode_test-websocket.png "Flashouillez le code"){: .img-center loading=lazy }

Bon il se peut que le serveur de websocket ne fonctionne pas tout le temps - et ouais c'est une démo ! Et il se peut que vous ayez à modifier le port 8080 par autre chose. Souvent il est pris par Tomcat ce port. Et il faut avoir installé `php5-curl`, ça marchera mieux.

## Tips

Si vous voulez lancer le script de manière un peu durable il convient de rediriger les logs vers un fichier ad-hoc :

```bash
php ./bin/truc-server.php 1> ./script.log 2>&1 &
```

## Conclusion

Bon évidemment c'est un petit tuto pour voir comment tout ça fonctionne, mais de mon côté je suis enchanté, ça ouvre pas mal de perspectives et je compte m'y coller plus franchement : pourquoi pas installer `nodejs` (qui contient la bibliothèque Javascript socket.io qui gère le protocole des websockets) et une base de données NoSQL qui délivre du json en natif (surtout vrai pour [CouchDB](http://couchdb.apache.org/)) et du coup n'avoir que du Javascript partout. Imaginez ce que l'on pourrait faire avec le plugin [Draw](http://www.geotribu.net/node/573#news14) de Leaflet ! De la co-édition d'objets géographiques en temps réel par exemple ! Wahou !

----

<!-- geotribu:authors-block -->
