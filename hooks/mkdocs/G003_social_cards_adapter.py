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
from pathlib import Path
from typing import Optional

# Mkdocs
from material import __version__ as material_version
from material.plugins.social.plugin import SocialPlugin
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.plugins import event_priority
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

# ###########################################################################
# ########## Global ################
# ##################################

logger = logging.getLogger("mkdocs")
hook_name = Path(__file__).stem

# ###########################################################################
# ########## Functions #############
# ##################################


@event_priority(50)
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
    # vérifie que le plugin social est bien installé et configuré
    if not config.plugins.get("material/social"):
        logger.warning(
            f"[{hook_name}] Le plugin social du thème Material n'est pas présent. Ce hook est donc inutile."
        )
        return

    social_plugin: SocialPlugin = config.plugins.get("material/social")

    # vérifie que le plugin est activé
    if not social_plugin.config.enabled or not social_plugin.config.cards:
        logger.debug(
            f"[{hook_name}] Le plugin social du thème Material est présent mais désactivé. Ce hook est donc inutile."
        )
        return

    # Cas de figure où une image n'est pas définie
    if page.meta.get("image") is None or page.meta.get("image") == "":
        if not page.is_index:
            social_card_url = (
                f"{config.site_url}assets/images/social{page.abs_url[:-1]}.png"
            )
        else:
            social_card_url = (
                f"{config.site_url}assets/images/social{page.abs_url[:-1]}/index.png"
            )

        logger.debug(
            f"{page.file.abs_src_path} n'a pas d'image. Une 'social card' sera automatiquement générée : {social_card_url}"
        )

        # si la page a une icône, on adapte le template de l'image
        # ref : https://squidfunk.github.io/mkdocs-material/reference#setting-the-page-icon
        if page.meta.get("icon"):
            cards_layout = "default/variant"
            logger.info(
                f"[{hook_name}] La page {page.abs_url} a une icône définie "
                f"({page.meta.get('icon')}). Dans ce cas, le modèle de social "
                f"card est : {cards_layout}"
            )
        else:
            cards_layout = social_plugin.config.cards_layout

        # définit les paramètres pour les social cards au niveau de la page
        page.meta["social"] = {
            "cards": True,
            "cards_layout": cards_layout,
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
    else:
        logger.debug(
            f"[{hook_name}] {page.abs_url} a une image paramétrée. "
            "Désactivation du plugin social sur la page."
        )
        page.meta["social"] = {
            "cards": False,
            # TODO: les lignes suivantes pourront être réactivées quand le plugin social gèrera les images distantes
            # "cards_layout": "default/only/image",
            # "cards_layout_options": {
            #     "background_image": page.meta.get("image"),
            # },
        }
