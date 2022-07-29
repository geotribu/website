---
# theme customizations
search:
  exclude: true
---

# Guide de contribution pour la revue de presse

!!! warning
    Ce contenu est une archive. Son contenu n'est sûrement plus très frais...

## Introduction

La revue de presse (RDP pour les intimes), c'est le truc qu'on essaie de sortir tous les vendredis de l'année. Sans exception, jamais - ok sauf le 15 août de cette année où on a un peu foiré :wink: Même si il fait beau et qu'on a qu'une seule envie : aller à la plage ou à la montagne (au choix, on n'est pas sectaire). Bon bref ... pour la revue de presse y'a quelques impératifs à suivre et quelques bonnes méthodes à essayer d'appliquer. Allez, c'est partiiiiii pour le guide pratique du gentil contributeur à la RDP de GéoTribu !

Difficulté : [Facile](http://geotribu.net/taxonomy/term/7)

## La RDP : WTF historique

La revue de presse, c'est l'article qu'on sort tous les vendredis en début d'aprem - dans l'idéal évidemment. A l'époque nous écrivions des articles un peu comme les news venaient. Un truc nous plaisait, on en faisait une news. Mais il a commencé à devenir impossible de tout diffuser : les nouvelles versions de bibliothèques, la super dataviz glânée sur Twitter, bref tout ce qui fait la revue de presse actuelle.

Je crois que l'idée est venue d'Arnaud et Thomas : on l'a vite adoptée - une bonne idée on la garde et on en fait quelque chose. Il fallait regrouper toutes ces news dans un seul article qui sorte à date fixe pour fidéliser nos lecteurs :slightly_smiling_face: c'est un peu comme la dope, le but étant de fournir une dose de news toutes les semaines. Après les lecteurs deviennent accro et là ... là rien ! Bref, la revue de presse était née.

## Fonctionnement général

Une revue de presse, c'est comme le bon vin - ça s'ouvre avant de déguster. Souvent nous créons la RDP la semaine précédant sa diffusion.

### Création de la revue de presse

Là c'est tout facile. Grâce au travail d'Arnaud sur les templates de contenus, y'a quasiment rien à faire, hormis être un peu inspiré pour écrire les news. La création ça se passe comme ça : on se connecte sur le site avec son login et password et on clique sur Create content en haut de la barre d'administration :

![createrdp](https://cdn.geotribu.fr/img/internal/old_guide/createrdp.png "createrdp"){: .img-center loading=lazy }

Il faut alors lui donner un titre, renseigner un tag, écrire une introduction provisoire et écrire une première brève :

![createrdp2](https://cdn.geotribu.fr/img/internal/old_guide/createrdp2.png "createrdp2"){: .img-center loading=lazy }

![createrdp3](https://cdn.geotribu.fr/img/internal/old_guide/createrdp3.png "createrdp3"){: .img-center loading=lazy }

![createrdp4](https://cdn.geotribu.fr/img/internal/old_guide/createrdp4.png "createrdp4"){: .img-center loading=lazy }

Et hop la revue de presse est créée. Dans la liste des articles apparaît dorénavant la revue de presse :

![createrdp5](https://cdn.geotribu.fr/img/internal/old_guide/createrdp5.png "createrdp5"){: .img-center loading=lazy }

Cette création minimale permet à tous de pouvoir travailler sur la revue de presse sans trop de problèmes de co-édition : en gros on peut ajouter des brèves pour mettre un simple lien et y revenir plus tard pour la rédiger sans perturber l'édition globale.

### Métadonnées

Un truc que j'aime bien faire direct à la création c'est renseigner l'auteur et la date de publication - comme ça c'est fait :

![createrdp6](https://cdn.geotribu.fr/img/internal/old_guide/createrdp6.png "createrdp6"){: .img-center loading=lazy }

----

## Les brèves

Les brèves c'est le nom qu'on a donné au bloc relatif à une info. Dans l'interface d'administration c'est appelé `News` / `Elément` :

![createrdp3](https://cdn.geotribu.fr/img/internal/old_guide/createrdp3.png "createrdp3"){: .img-center loading=lazy }

Au début d'une revue de presse donc, une seule brève, obligatoire. Ensuite pour ajouter une brève, là c'est en mode 'faut pas traîner' pour pas faire chier les autres :slightly_smiling_face: En gros, nous n'avons pas trouvé de parade simple dans notre version de Drupal pour la création d'une brève : il faut éditer tout l'article, ajouter une brève minimale et sauver la revue de presse. Comme ça on peut l'éditer ensuite à loisir en laissant aux autres auteurs la possibilité de travailler aussi sur la rdp. Donc on créé une brève en éditant complétement la revue de presse.

Pour éditer une brève il suffit d'afficher la revue de presse, on y accède depuis la liste des contenus :

![createrdp5](https://cdn.geotribu.fr/img/internal/old_guide/createrdp5.png "createrdp5"){: .img-center loading=lazy }

Et on clique sur le bouton `Modifier` :

![createrdp13](https://cdn.geotribu.fr/img/internal/old_guide/createrdp13.png "createrdp13"){: .img-center loading=lazy }

On clique sur `Ajouter un autre élément` :

![createrdp14](https://cdn.geotribu.fr/img/internal/old_guide/createrdp14.png "createrdp14"){: .img-center loading=lazy }

On remplit quelques mots et on sauve la revue de presse. On pourra revenir sur cette news juste après la création sans perturber les autres :

![createrdp15](https://cdn.geotribu.fr/img/internal/old_guide/createrdp15.png "createrdp15"){: .img-center loading=lazy }

Puis clique sur `Enregistrer` :

![createrdp16](https://cdn.geotribu.fr/img/internal/old_guide/createrdp16.png "createrdp16"){: .img-center loading=lazy }

Voilà maintenant la brève créée, on pourra y revenir quand on aura plus d'inspiration :)

Pour l'éditer, il suffit de cliquer sur `Modifier` :

![createrdp12](https://cdn.geotribu.fr/img/internal/old_guide/createrdp12.png "createrdp12"){: .img-center loading=lazy }

Et là on n'édite que cette news sans bloquer les autres auteurs sur la revue de presse, c'est bien pratique cette fonctionnalité !

### Type

Une brève possède obligatoirement un type. Les types permettent de découper la revue de presse en blocs plus ou moins cohérents :

- Sorties de la semaine
- Client
- Serveur
- Logiciel
- OpenStreetMap
- Google
- Open Data
- Représentation Cartographique
- Divers
- En bref

Evidemment c'est pas fixe comme liste, on peut modifier / ajouter ces types. Pour demander rien de plus simple, hop on écrit un mail à tout le monde pour qu'on se mette d'accord sur le nom et hop Arnaud l'ajoute :wink: !

![createrdp7](https://cdn.geotribu.fr/img/internal/old_guide/createrdp7.png "createrdp7"){: .img-center loading=lazy }

### Icône

Ensuite une brève possède une icône. Par défaut l'icône c'est la fameuse icône connue de tous par son doux nom[world\_2.png](http://geotribu.net/sites/default/public/public_res/default_images/world_2.png). Deux choix du coup, soit on conserve celle-ci ou on en choisit une autre - élémentaire mon cher. Si on choisit d'en mettre une un peu plus en relation avec la news, on peut soit choisir une icône déjà existante - y'en a une bonne pelletée - ou soit on en ajoute une nouvelle. Dans les deux cas, on clique sur `Open file browser` au grand jamais nous ne cliquerons sur `Choisissez un fichier` ... ça bousille toute l'arborescence de stockage des images quand on l'utilise alors autant éviter :

![createrdp11](https://cdn.geotribu.fr/img/internal/old_guide/createrdp11.png "createrdp11"){: .img-center loading=lazy }

Le file browser c'est un peu l'espace de stockage pour nos images, dedans on a essayé d'organiser au mieux : y'a des répertoires et voilà en fonction de la news on pioche une image ou on en ajoute une à l'endroit le plus approprié.

![createrdp17](https://cdn.geotribu.fr/img/internal/old_guide/createrdp17.png "createrdp17"){: .img-center loading=lazy }

Il arrive parfois que l'arborescence ne s'affiche pas en entier, il faut pour cela cliquer sur les répertoires et ils se rafraîchissent. Donc les icônes c'est dans logos-icones, y'en a pas mal donc ne pas hésiter à jeter un coup d'œil dedans pour voir si y'en a pas une qui nous convienne :

![createrdp18](https://cdn.geotribu.fr/img/internal/old_guide/createrdp18.png "createrdp18"){: .img-center loading=lazy }

Une icône c'est **74 x 74 pixels**. On accepte aussi le 73 x 73 :slightly_smiling_face:. Sinon ça casse toute la mise en page. Un PNG ou un JPG fait l'affaire.

1. Icône existante, on la sélectionne :

  ![createrdp19](https://cdn.geotribu.fr/img/internal/old_guide/createrdp19.png "createrdp19"){: .img-center loading=lazy }

1. Upload d'une nouvelle icône, on crée une magnifique image 74 x 74, on la nomme comme on veut (éviter cependant les accents, les espaces, les caractères à la con, c'est quand même mieux), on choisit un répertoire plus ou moins approprié et enfin on upload la nouvelle icône :

  ![createrdp20](https://cdn.geotribu.fr/img/internal/old_guide/createrdp20.png "createrdp20"){: .img-center loading=lazy }

### Titre

Bah on saisit un titre. Essayer autant que faire ce peut de ne pas mettre un titre à rallonge, sur deux lignes c'est pas top avec la feuille de style.

![createrdp21](https://cdn.geotribu.fr/img/internal/old_guide/createrdp21.png "createrdp21"){: .img-center loading=lazy }

Un titre trop long :/

![createrdp22](https://cdn.geotribu.fr/img/internal/old_guide/createrdp22.png "createrdp22"){: .img-center loading=lazy }

### Contenu

Enfin le contenu de la news. Là on va faire connaissance avec un petit éditeur wysinrwyg What You See Is _Not Really_ What You Get - bah ouais on a imposé des règles fortes sur le style dans les css - histoire d'avoir une cohérence graphique dans nos contenus. Du coup ce qu'on saisit ne représente pas exacetement le résultat. Mais l'édition en devient simple en suivant quelques petites règles : pas besoin de trop s'emmerder avec tout ça.

![createrdp23](https://cdn.geotribu.fr/img/internal/old_guide/createrdp23.png "createrdp23"){: .img-center loading=lazy }

Pas besoin de définir des styles d'indentation, de décalage à droite ou à gauche, **on conserve tout le temps le style `Paragraphe` et on laisse tel quel `Font Size`**. Après on peut faire des listes à loisir et des tableaux aussi - bien que je ne crois pas en avoir vu une fois. Le dernier bouton, aucune idée de ce que ça peut être :/

Donc on saisit le texte, quand on veut aller à la ligne on clique sur `Entrée` ça créé automatiquement un nouveau paragraphe.

#### Lien

Quand on veut insérer un lien, on sélectionne le bout de texte sur lequel on veut faire le lien et on clique sur le bouton de lien :

![createrdp25](https://cdn.geotribu.fr/img/internal/old_guide/createrdp25.png "createrdp25"){: .img-center loading=lazy }

![createrdp26](https://cdn.geotribu.fr/img/internal/old_guide/createrdp26.png "createrdp26"){: .img-center loading=lazy }

Perso je mets souvent un `target=_blank` pour ouvrir le lien dans un nouvel onglet. C'est pas très HTML compliant mais bon, je trouve ça plus ergonomique. Au choix de chacun.

#### Image

Souvent on veut insérer une belle image dans la news - faut pas hésiter ! C'est bien une revue de presse avec plein d'illustrations.

Pour les images c'est pas super compliqué c'est pareil que pour les icônes sauf que là seule la largeur maximum d'affichage est imposée : c'est à peu près 600 pixels. Par contre dans la mesure du possible essayer d'éviter d'uploader une image qui pèse un âne mort. Si elle fait 3 Mo et 3500 pixels sur 1800 - bah c'est trop faut, il faut d'abord la réduire sur votre ordi avant de la transférer.

Donc l'image ; souvent c'est le seul moment où on a le droit de toucher au `text-align` : on centre le curseur et on upolad une image :

![createrdp27](https://cdn.geotribu.fr/img/internal/old_guide/createrdp27.png "createrdp27"){: .img-center loading=lazy }

![createrdp28](https://cdn.geotribu.fr/img/internal/old_guide/createrdp28.png "createrdp28"){: .img-center loading=lazy }

![createrdp29](https://cdn.geotribu.fr/img/internal/old_guide/createrdp29.png "createrdp29"){: .img-center loading=lazy }

![createrdp30](https://cdn.geotribu.fr/img/internal/old_guide/createrdp30.png "createrdp30"){: .img-center loading=lazy }

Il arrive bien souvent qu'on veuille faire un lien sur une image : rien de plus simple on sélectionne l'image et on ajoute le lien comme pour un texte.

#### Vidéos

Pour insérer une vidéo c'est un poil plus sioux :wink:.

Exemple pour une vidéo Youtube : [celle-là](https://www.youtube.com/watch?v=od_6M8cFdUA) par exemple :slightly_smiling_face:. On copie le lien d'insertion proposé par Youtube (pour les autres sites de vidéos, c'est pareil, juste faire gaffe à définir une largeur inférieure à 600 pixels.

On créé un nouveau paragraphe, on centre le curseur, on clique sur `Plain Text` et dans le dernier

On insère le code :

![createrdp31](https://cdn.geotribu.fr/img/internal/old_guide/createrdp31.png "createrdp31"){: .img-center loading=lazy }

![createrdp32](https://cdn.geotribu.fr/img/internal/old_guide/createrdp32.png "createrdp32"){: .img-center loading=lazy }

Puis on repasse en mode `Full HTML`. Et hop la vidéo est insérée :)

#### IFrames

Pour les IFrames, c'est un peu pareil que pour les vidéos.

Exemple pour une carto pleine page qu'on a trouvé[quelquepart](https://openlayers.org/dev/examples/fullScreen.html). On créé un nouveau paragraphe, on centre le curseur, on clique sur `Plain Text` et dans le dernier

on insère ce bout de code :

![createrdp33](https://cdn.geotribu.fr/img/internal/old_guide/createrdp33.png "createrdp33"){: .img-center loading=lazy }

On repasse en `Full HTML` et le tour est joué.

#### Radios

Ca nous arrive d'insérer un podcast d'une radio : idem que pour les vidéos ou les IFrames, curseur au centre, passage en `Plain Text`, insertion dans le dernier

d'un bout de code et switche vers `Full HTML`. Exemple pour une émission Radio France :

![createrdp34](https://cdn.geotribu.fr/img/internal/old_guide/createrdp34.png "createrdp34"){: .img-center loading=lazy }

### Cas particulier

Le type **En bref** se compose d'une liste de liens vers des trucs que nous ne jugeons pas utile de développer ou quand on n'a pas eu trop le temps. C'est une simple liste à puces.

----

## L'orthogaffe de la grand-mère

Bah voilà, on essaie de faire gaffe à l'orthographe, tout ça tout ça. Et aussi un peu à la ponctuation. J'y reviens lors de la relecture du vendredi avant publication.

----

## Introduire

L'intro... l'un d'entre-nous se lance, ouvre un éditeur de texte tout simple et on prose, on poème, on hurle, on recette un texte. On édite l'intégralité de la revue de presse et on copie colle notre prose.

![createrdp37](https://cdn.geotribu.fr/img/internal/old_guide/createrdp37.png "createrdp37"){: .img-center loading=lazy }

## L'image du slideshow

On met à chaque revue de presse une image qui ira se caller dans le slideshow de la page d'accueil. On l'intègre via ce petit bloc :

![createrdp38](https://cdn.geotribu.fr/img/internal/old_guide/createrdp38.png "createrdp38"){: .img-center loading=lazy }

On clique bien sur Open File Borwser et non sur Choisissez un fichier - qui est le mal absolu :)

La taille de cette image c'est 670 pixels par 180 pixels.

## L'icône de la revue de presse

On n'innove pas trop de ce côté-là - sauf celle d'[Halloween](http://geotribu.net/node/670). On peut quand la modifier si on veut :slightly_smiling_face: Mais cette fois-ci c'est 71 x 75 pixels.

----

## La relecture

Ca y est la revue de presse, il est jeudi aprem, le soleil brille - non je déconne, il est vendredi 13h30 - 30 minutes avant l'heure de publication - rrrraaahh, donc avant la publication on essaie de faire une relecture de toutes les news, si y'a des coquilles on corrige - même les coquilles des autres :slightly_smiling_face: - on vérifie un peu tout ce que je viens de dire au-dessus sur la mise en forme, les liens, les icpones, les images, tout ça.

Celui qui créé la revue de la presse est invité à lancer une discussion par email à tout le monde. Si on pouvait mettre le même titre tout le temps pour les revues de presse, ça nous permet d'organiser au mieux notre gestionnaire de mail :

![createrdp35](https://cdn.geotribu.fr/img/internal/old_guide/createrdp35.png "createrdp35"){: .img-center loading=lazy }

----

## Publication et diffusion

Une fois que tout est bon : pour ça quelqu'un lance un mail en disant un truc du style `Paré pour publication`, les autres répondent +1, dès qu'on en a deux ou trois, on publie.

Pour publier, bah on clique on édite la revue de presse, on refait gaffe à la date de publication renseignée au tout début de la création de la rdp :

![createrdp36](https://cdn.geotribu.fr/img/internal/old_guide/createrdp36.png "createrdp36"){: .img-center loading=lazy }

### Twitter

Une fois publiée la revue de presse se doit d'être un poil diffusée :smile:.

Un d'entre-nous tweete. Dans le tweet il faut veiller à mettre @geotribu et quelques #hashtag correspondant au contenu de la rdp. Le @geotribu permet à Arnaud de remercier les re-tweets. Ah si j'oubliais ... faut mettre le lien vers la revue de presse, je l'ai oublié une fois :/

### Google Plus

Aucune idée de comment ça marche ... hum hum hum

![createrdp_GooglePlus_01](https://cdn.geotribu.fr/img/internal/old_guide/createrdp_GooglePlus_01.jpg "createrdp_GooglePlus_01"){: .img-center loading=lazy }

![createrdp_GooglePlus_02](https://cdn.geotribu.fr/img/internal/old_guide/createrdp_GooglePlus_02.jpg "createrdp_GooglePlus_02"){: .img-center loading=lazy }

Voilà un petit guide de contribution. On a essayé de faire le plus complet possible pour faire de belles revues de presse.

Et surtout restez critique, impertinent, créatif... écrivez ce que vous voulez - tant que ça a un petit lien avec la carto, la géo, l'info, le web ou les données :wink:.

La GeoTribu Team

Fabien
