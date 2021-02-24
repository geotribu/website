<!-- Modèle pour créer une nouvelle revue de presse. Ignorer ou adapter pour les autres types de contenus -->

# Amorcer une nouvelle revue de presse

- [ ] nommer cette _Pull Request_ de façon claire et lisible. Exemple : `GeoRDP du JJ MM AAAA`
- [ ] partir du modèle disponible (copier/coller) : [brut](https://raw.githubusercontent.com/geotribu/website/master/content/rdp/templates/template_rdp.md) - [rendu Github](https://github.com/geotribu/website/blob/master/content/rdp/templates/template_rdp.md)
- [ ] changer la date dans les métadonnées :
  - [ ] `date` : au format `AAAA-MM-JJ HH-MM` - mais laisser l'heure sur 14h20 c'est historique
  - [ ] `title` : correspond à ce qui est affiché dans le menu de navigation, l'onglet du navigateur et le SEO. Bien **indiquer l'année** pour améliorer le référencement et en prévision d'une refonte du moteur de rendu.
- [ ] changer la date du titre principal (en début de contenu). Idem, **indiquer l'année**.

## Encourager les contributions spontanées sur Twitter

Pour encourager les contributions extérieures, il est sympa de tweeter le lien du fichier de la RDP. Voici ci-dessous un modèle dans lequel :

- remplacer `XXXXXXXXXX` par le lien vers le fichier de la GeoRDP dans la branche créée (par exemple : <https://github.com/geotribu/website/blob/rdp/2021-02-26/content/rdp/2021/rdp_2021-02-26.md>)
- insérer l'image dans le tweet <https://cdn.geotribu.fr/img/internal/contribution/geotribu_contribuer_rdp_github_edit.png>

```txt
Ce vendredi c'est #GeoRDP !

💡 Une idée de news ? Une envie de parler de #carte ? d'outil #SIG ? de relayer un article, un tutoriel  sur la #géographie ou la #géomatique ?

C'est par ici 👉 XXXXXXXXXX 👈
(icône 🖍️)

Modèle de news ici : https://github.com/geotribu/website/blob/master/content/rdp/templates/template_rdp_news.md
```

Exemple tweet : <https://twitter.com/geotribu/status/1364625815099613185>

----

## Check-list de publication

### Qualité

- [ ] les news sont bien réparties dans les bonnes sections
- [ ] les sections vides sont supprimées
- [ ] vérifier le rendu de la syntaxe markdown
- [ ] chasse aux coquilles orthographiques et dyslexiques

### Images

- [ ] les images téléversées sur le CDN n'ont pas de caractère spécial dans leur nom de fichier (espace, accent, etc.)
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

## Diffuser sur Twitter

Une fois le déploiement effectué (~ 5 minutes), diffuser a minima sur Twitter avec le hashtag `#GeoRDP`, en citant les contributeur/ices avec leur compte. Attention le compte Twitter `@geotribu` est en fait le compte personnel d'Arnaud.
