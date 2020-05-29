---
Title: Bienvenue sur Geotribu
Category: global
Date: 2020-03-20 10:20
tags: homepage,accueil,geotribu,bienvenue,global
---

# Accueil

Bienvenue sur Geotribu !

![Bannière Géotribu](https://cdn.geotribu.fr/images/internal/charte/geotribu_banner.jpg)

## Thème

<button data-md-color-scheme="default"><code>Thème clair (défault)</code></button>
<button data-md-color-scheme="slate"><code>Thème sombre</code></button>

<script>
  var buttons = document.querySelectorAll("button[data-md-color-scheme]")
  buttons.forEach(function(button) {
    var attr = "data-md-color-scheme"
    button.addEventListener("click", function() {
      document.body.setAttribute(attr, this.getAttribute(attr))
    })
  })
</script>
