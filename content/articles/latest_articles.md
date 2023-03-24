# Derniers articles publiés

{% if config.extra.latest %}
{% for article in config.extra.latest.articles %}
{{ article.title }}
{% endfor %}
{% endif %}
