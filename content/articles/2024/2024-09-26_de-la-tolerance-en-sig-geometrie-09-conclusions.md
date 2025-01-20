---
title: "5 conseils pour bien vivre géométriquement"
subtitle: "Série : De la tolérance en SIG - chapitre 9"
authors:
    - Loïc Bartoletti
categories:
    - article
comments: true
date: 2024-09-26
description: "Neuvième et dernière partie du tour d'horizon des SIG sur les dessous des calculs géométriques : 5 conseils pour vivre votre meilleure vie géométrique."
icon: material/meditation
image: https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_09_conclusion.png
license: beerware
robots: index, follow
tags:
    - géométrie
    - lifestyle
    - open source
    - topologie
---

# 5 conseils pour arrêter de trop penser et vivre une vie meilleure !

:calendar: Date de publication initiale : {{ page.meta.date | date_localized }}

![Globe cerveau](https://cdn.geotribu.fr/img/internal/icons-rdp-news/mentale.png){: .img-thumbnail-left }

On a souvent ces interrogations sur les « irrégularités » rencontrées lors des opérations courantes dans les SIG : pourquoi les accrochages dans QGIS ne se positionnent-ils pas toujours exactement sur la géométrie ? Pourquoi les calculs de superposition manquent-ils de précision ? Et pourquoi les résultats peuvent-ils être incohérents ?

Plutôt que de se perdre dans une quête de surprécision, voici les 5 conseils pour améliorer votre expérience SIG et vivre une vie meilleure.

Derrière cette expression « incitaclic », voici en réalité quelques conseils ou expériences que j'ai pu rencontrer sur différents projets.

![Série d'été 2024 de Loïc Bartoletti - Les Géométries et les SIG : conclusions - Crédits : Sylvain Beorchia](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/splash_serie_geometrie_09_conclusion.png){: .img-center loading=lazy }

Cet article est la neuvième et dernière partie de la série d'été sur la gestion de la géométrie dans les SIG.

[Le dossier :octicons-move-to-start-16:](./2024-07-16_de-la-tolerance-en-sig-geometrie-00-annonce.md "De la tolérance en SIG : le dossier"){: .md-button }
[8 : Algorithmes géométriques et code :fontawesome-solid-backward-step:](./2024-09-05_de-la-tolerance-en-sig-geometrie-08-algorithmes-code.md "Algorithmes géométriques et code : comment cela fonctionne-t-il ?"){: .md-button }
{: align=middle }

[Commenter cet article :fontawesome-solid-comments:](#__comments "Aller aux commentaires"){: .md-button }
{: align=middle }

----

## Arrêtez de chercher la surprécision

!!! quote "Conseil n°1 : Le prix de la rigueur"
    La rigueur à tout prix peut devenir une source de frustration. Acceptez qu’une légère imprécision est inévitable et concentrez-vous sur l’essentiel.

On est dans un monde infini, mais avec des ressources finies. Quelques arrondis ne font pas de mal. De combien de chiffres après la virgule avez-vous réellement besoin ? Votre précision c'est le décimètre, le centimètre, le millimètre, au-delà  ? Vous avez besoin de combien de chiffres pour [Pi](https://www.jpl.nasa.gov/edu/news/2016/3/16/how-many-decimals-of-pi-do-we-really-need/). Combien d'approximations réalisez-vous au quotidien, tout en étant précis ? Il est actuellement 21 h 02 ou simplement 21 h ? Quand vous réalisez un trajet de chez vous aux rencontres QGIS, vous êtes précis à la seconde, à la minute, au quart d'heure ? Bref, la précision dépend de votre contexte et il y a fort à parier que vous allez rarement être en dessous de 10^-3 sur du cartésien et 10^-8 en géodésique.

![xkcd 2170 - Credits : Randall Monroe](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/xkcd_coordinate_precision.webp){: .img-center loading=lazy }

----

## Gérez la tolérance

!!! quote "Conseil n°2 : À chaque calcul, sa tolérance"
    Utilisez des tolérances appropriées dans vos calculs pour minimiser les effets des erreurs d'arrondi. Définissez des tolérances adaptées à l’échelle et aux objectifs de votre projet.

En lien avec le nombre de chiffres après la virgule, vous pouvez également ajouter une tolérance. En France, les gestionnaires de réseaux savent qu'on les caractérise suivant 3 classes : A, B ou C. 10 cm, 40 cm, etc. Une bonne pratique est de se demander si le point n'est pas à une distance d'environ X cm. Sur PostGIS, cela va se caractériser par l'utilisation de `ST_DWithin` plutôt qu'un `ST_Intersects`.

----

## Utilisez la topologie

!!! quote "Conseil n°3 : faut-il vraiment vous faire un topo ?"
    La topologie permet de gérer les relations spatiales et de corriger les erreurs géométriques. Les outils topologiques garantissent que les entités spatiales respectent certaines règles, améliorant ainsi la cohérence des données.

Si vraiment, vous souhaitez que les nœuds soient identiques, la topologie est là pour vous. Mais, attention, vous avez vu, cela transforme légèrement la donnée en entrée. Par ailleurs, suivant les outils que vous utilisez, elle peut ne pas être respectée lors d'éditions dans d'autres outils que ceux sur lesquels vous allez travailler. D'où l'idée de déporter l'intelligence en base : [Thick database (base épaisse)](https://img1.lemondeinformatique.fr/fichiers/telechargement/plaidoyer-de-frederic-brouard-sur-le-concept-de-bases-de-donnees-epaisses.pdf).

----

## Connaissez les autres nombres

!!! quote "Conseil n°4 : comptez-vous !"
    Comprenez comment les nombres sont représentés dans les ordinateurs. Cela aide à anticiper et à gérer les erreurs de calcul, notamment les différences entre les nombres en virgule flottante et les autres.

Tout est de la faute des nombres en virgule flottante ! Vous pouvez utiliser d'autres outils, mais attention, la conversion peut engendrer des erreurs. Sans aller jusqu'au détail de ces nombres, il faudrait retenir que 0.1 + 0.2 != 0.3.

----

## Investissez dans l'évolution des outils

!!! quote "Conseil n°5 : calculez sur le temps long."
    Soutenez le développement et l'amélioration des outils SIG, surtout les projets open source comme ceux de l'OSGeo !

On ne le dira jamais assez, mais si un fonctionnement ou un bug vous dérange donnez-vous les moyens de le corriger. **Investissez dans vos outils SIG !** Du temps et/ou de l'argent pour consolider les bases techniques sur lesquelles votre travail ou vos missions reposent. Rappelez-vous que même les logiciels propriétaires s'inspirent voire s'appuient sur les briques libres, ouvertes et gratuites (à l'usage) que sont GEOS, GDAL, SFCGAL, QGIS, SAGA, GRASS et d'autres encore. Ça vaut également pour les demandes de fonctionnalités.

----

## Conclusion finale

!!! quote "Comprendre > penser"
    La quête de la perfection numérique dans les SIG peut être frustrante. En adoptant une approche pragmatique et en comprenant les limites des calculs numériques, vous pouvez réduire le stress et améliorer votre efficacité. En acceptant ces réalités, vous pourrez arrêter de trop penser et commencer à vivre une vie meilleure, plus sereine et productive dans vos projets géospatiaux.

C'est beau, hein ?

En réalité, vivez vos SIG comme vous le voulez, mais ayez connaissance de leurs fonctionnements. Oui, leurs, car chacun peut vous donner des résultats plus ou moins différents.

![Bannière 5 conseils pour bien vivre géométriquement](https://cdn.geotribu.fr/img/articles-blog-rdp/articles/2024/geometrie_tolerance_sig/bien_vivre_geometriquement.webp){: .img-center loading=lazy }

J'espère que cette série d'articles vous a intéressé. D'autres sur la comparaison entre les outils devraient venir.

Et pour finir, merci à mes relecteurs de Geotribu ([Michaël](../../team/michael-galien.md "Michaël Galien"), [Florian](../../team/florian-boret.md "Florian Boret"), [Guilhem](../../team/guilhem-allaman.md "Guilhem"), [Arnaud](../../team/arnaud-vandecasteele.md) et Julien), à [Sandro Santilli](https://www.osgeo.org/member/sandro-santilli/) (correction d'une erreur dans un code), [Martin Davis](https://wiki.osgeo.org/wiki/User:Mdavis) aka Dr. [JTS](https://www.osgeo.org/projects/jts/) (pour ses apports sur les « concurrents ») et tout ce qu'il a pu faire pour nos outils ! Et, enfin, merci à [Julien Moura](../../team/julien-moura.md "Julien Moura") qui a su être patient avant de voir la première phrase :grin:.

<!-- geotribu:authors-block -->

{% include "licenses/beerware.md" %}
