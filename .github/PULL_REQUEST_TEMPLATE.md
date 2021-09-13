<!-- Modèle pour créer une nouvelle revue de presse.

MERCI DE SUPPRIMER OU ADAPTER POUR LES AUTRES TYPES DE CONTENUS (principe du `benevol time fair-use`).

Pour les articles, voir : https://static.geotribu.fr/contribuer/workflow_article/#soumettre

 -->

# Amorcer une nouvelle revue de presse

- [ ] nommer cette _Pull Request_ de façon claire et lisible. Exemple : `GeoRDP du JJ MM AAAA`
- [ ] partir du modèle disponible (copier/coller) [sur Github](https://github.com/geotribu/website/blob/master/content/rdp/templates/template_rdp.md?plain=1) ou [sur le pad](https://geotripad.herokuapp.com/DCBQirjYSp6sqxPd5JYqLg?both)
- [ ] changer la date dans les métadonnées :
  - [ ] `date` : au format `AAAA-MM-JJ HH-MM` - mais laisser l'heure sur 14h20 c'est historique
  - [ ] `title` : correspond à ce qui est affiché dans le menu de navigation, l'onglet du navigateur et le SEO. Bien **indiquer l'année** pour améliorer le référencement et en prévision d'une refonte du moteur de rendu.
- [ ] changer la date du titre principal (en début de contenu). Idem, **indiquer l'année**.

## Encourager les contributions

- [ ] informer l'équipe que la prochaine RDP a été initiée en publiant le lien de la PR sur [le canal `#revues-de-presse` de Slack](https://geotribu.slack.com/archives/C010DD7FMEX)
- [ ] tweeter le lien du fichier de la RDP. Voici ci-dessous un modèle dans lequel :

- remplacer `XXXXXXXXXX` par le lien vers le fichier de la GeoRDP dans la branche créée (par exemple : <https://github.com/geotribu/website/blob/rdp/2021-02-26/content/rdp/2021/rdp_2021-02-26.md?plain=1>)
- insérer cette image dans le tweet <https://cdn.geotribu.fr/img/internal/contribution/geotribu_contribuer_rdp_github_edit.png>

```txt
Ce vendredi c'est #GeoRDP !

💡 Une idée de news ? Une envie de parler de #carte ? d'outil #SIG ? de relayer un article, un tutoriel  sur la #géographie ou la #géomatique ?

C'est par ici 👉 XXXXXXXXXX 👈
(icône 🖍️)

Modèle de news ici : https://github.com/geotribu/website/blob/master/content/rdp/templates/template_rdp_news.md
```

Exemple de [tweet](https://twitter.com/geotribu/status/1364625815099613185) :

![tweet geordp](https://cdn.geotribu.fr/img/internal/contribution/geotribu_rdp_tweet_incitation.png "exemple de tweet geordp")

----

## Check-list de publication

### Qualité

- [ ] les news sont bien réparties dans les bonnes sections
- [ ] les sections vides sont supprimées
- [ ] vérifier le rendu de la syntaxe markdown (cf. linter)
- [ ] chasse aux coquilles orthographiques et dyslexiques

### Images

- [ ] les images téléversées sur le CDN n'ont pas de caractère spécial dans leur nom de fichier (espace, accent, etc.) et n'excédent pas 1000px de largeur
- [ ] les images sont hébergées sur des sites sécurisés (HTTPS)
- [ ] chaque news a une vignette
- [ ] les images (sauf les vignettes) ont l'attribut `loading` défini sur `lazy` (cf. [MDN](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img#attr-loading) et [guide material-mkdocs](https://squidfunk.github.io/mkdocs-material/reference/images/#image-lazy-loading))
- [ ] accessibilité : chaque image a un texte de remplacement (entre les crochets) et un titre lisible par les outils d'assistance. Bref, qui respecte la [syntaxe générale](https://static.geotribu.fr/contribuer/guides/image/#syntaxe-generale)

### SEO

- [ ] `image` pointe vers l'URL d'une des images de la revue de presse
- [ ] `description` contient les mots-clés et grandes lignes du contenu (par exemple, la reprise de l'intro)

----

## Publier

1. S'assurer que la branche soit à jour par rapport à la branche principale. Le cas échéant, utiliser le bouton `Update branch` en bas.
2. S'assurer que les éléments de la check-list ci-dessus soient tous remplis
3. Fusionner (_merge_) en utilisant un _merge commit_ ou un _rebase_, mais **surtout pas un squash**.

----

## Diffuser sur Twitter

Une fois le déploiement effectué (~ 5 minutes), diffuser a minima sur Twitter :

- avec le hashtag `#GeoRDP`, en citant les contributeur/ices avec leur éventuel compte
- si possible en intégrant quelques hastags des personne, organisations ou logiciels cités dans la revue de presse
- de préférence via le compte `@geotribu` en utilisant Tweetdeck.
