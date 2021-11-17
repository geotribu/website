---
name: Suggestion de news pour une revue de presse
about: Formulaire pour soumettre une contribution de news à une revue de presse.
title: "[News GeoRDP]"
labels: contribution externe, rdp
assignees: aurelienchaumet, Guts, igeofr

---

# News

L'auteur/e a un lien avec le contenu proposé :

- [ ] Oui (développeur, intégrateur, vendeur, distributeur...)
- [ ] Non

## Section cible

Un seul choix possible :

- [ ] Sorties de la semaine
- [ ] Client
- [ ] Serveur
- [ ] Logiciel
- [ ] Représentation Cartographique
- [ ] OpenStreetMap
- [ ] Google
- [ ] Open Data
- [ ] Geo-event
- [ ] Divers
- [ ] En bref

----

## Titre

Le titre accrocheur de la news.
Longeur maximale indicative : 100/120 caractères

## Image de la vignette

- Texte de remplacement :
- Légende de l'image :
- URL :

## Contenu

Prose.

## Medias d'illustration (images, vidéos, tweets, etc.)

<!-- Liens bruts. -->

----

## Texte final à copier/coller

```markdown
## {{ news.section }}

### {{ news.title }}

![{{ news.thumbnail.replace_txt }}]({{ news.thumbnail.url }} "{{ news.thumbnail.caption }}"){: .img-rdp-news-thumb loading=lazy }

{{ news.body }}
```
