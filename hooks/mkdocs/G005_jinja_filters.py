# standard library
import logging

# 3rd party
import mkdocs.plugins
from geotribu_cli.utils.slugger import sluggy
from jinja2 import Environment
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files

# globals
logger = logging.getLogger("mkdocs")


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
    env.filters["slugger"] = sluggy

    logger.info(
        "Jinja2 filters added for templates: slugger (handy filter to slugify a string)"
    )

    return env
