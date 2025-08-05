# standard library
import datetime
import logging

# 3rd party
import mkdocs.plugins
from babel.dates import format_date
from geotribu_cli.utils.slugger import sluggy
from jinja2 import Environment
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files

# globals
logger = logging.getLogger("mkdocs")
log_prefix = f"[{__name__}] "


def date_localized(in_date: datetime.date):
    "Localize a date using babel."
    return format_date(date=in_date, format="long", locale="fr_FR")


@mkdocs.plugins.event_priority(-50)
def on_env(env: Environment, config: MkDocsConfig, files: Files) -> Environment:
    """Ajoute des fonctionnalités (filtres et tests) à l'environnement Jinja utilisé
    par Mkdocs pour générer les pages à partir des templates.

    Note importante : ces filtres ne sont pas accessibles dans les pages Markdown, mais
    dans les templates HTML. Pour les filtres accessibles dans le Markdown, c'est via le
    plugin mkdocs-macros et le fichier lié 'hooks/macors/custom_jinja.py'.

    Args:
        env (Environment): global Jinja Environment
        config (MkDocsConfig): global configuration object
        files (Files): global files collection

    Returns:
        Environment: global Jinja Environment
    """
    env.filters["date_localized"] = date_localized
    env.filters["slugger"] = sluggy

    logger.info(
        log_prefix
        + "Jinja2 filters added for templates: slugger (handy filter to slugify a string)"
    )

    return env
