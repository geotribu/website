#! python3  # noqa: E265

"""Script joué au chargement du contenu markdown de chaque page (hook).

Contexte :

    Le thème Material for Mkdocs intègre un plugin (social) qui permet de générer
    automatiquement une image pour chaque page en croisant différents éléments
    (métadonnées de la page et éléments graphiques de base).
    Mais le fonctionnement est très générique (normal) et entre en conflit avec la gestion
    des en-têtes du site Geotribu.

Objectifs :

    - quand une image n'est pas définie sur une page, patcher l'en-tête pour
        y insérer la configuration du plugin social de sorte qu'il génère une image
        et qu'on la référence
    - quand une image est définie manuellement, patcher l'en-tête pour
        y insérer la configuration du plugin social de sorte qu'il utilise l'image sans rien toucher

"""

# ############################################################################
# ########## Libraries #############
# ##################################

# standard library
import logging
from typing import Optional

# Mkdocs
import mkdocs.plugins
from material.plugins.social.plugin import SocialPlugin
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

# ###########################################################################
# ########## Global ################
# ##################################

logger = logging.getLogger("mkdocs")

# ###########################################################################
# ########## Functions #############
# ##################################


@mkdocs.plugins.event_priority(50)
def on_page_markdown(
    markdown: str, *, page: Page, config: MkDocsConfig, files: Files
) -> Optional[str]:
    """
    The `page_markdown` event is called after the page's markdown is loaded
    from file and can be used to alter the Markdown source text. The meta-
    data has been stripped off and is available as `page.meta` at this point.

    Parameters:
        markdown: Markdown source text of page as string
        page: `mkdocs.structure.pages.Page` instance
        config: global configuration object
        files: global files collection

    Returns:
        Markdown source text of page as string
    """
    if not config.plugins.get("material/social"):
        logger.warning("Le plugin social du thème Material n'est pas présent")
        return

    social_plugin: SocialPlugin = config.plugins.get("material/social")

    if page.meta.get("image") is None or page.meta.get("image") == "":
        social_card_url = (
            f"{config.site_url}assets/images/social{page.abs_url[:-1]}.png"
        )
        logger.info(
            f"{page.abs_url} n'a pas d'image. Une 'social card' sera automatiquement générée : {social_card_url}"
        )
        page.meta["image"] = social_card_url
        page.meta["social"] = {
            "cards": True,
            "cards_layout_options": {
                "background_color": social_plugin.config.cards_layout_options.get(
                    "background_color"
                ),
                "background_image": social_plugin.config.cards_layout_options.get(
                    "background_image",
                    "content/theme/assets/images/geotribu/background_geotribu.png",
                ),
                "color": social_plugin.config.cards_layout_options.get("color"),
                "font_family": social_plugin.config.cards_layout_options.get(
                    "font_family"
                ),
            },
        }
