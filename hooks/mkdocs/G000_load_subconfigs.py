#! python3  # noqa: E265

# ############################################################################
# ########## Libraries #############
# ##################################

# standard library
import logging
from pathlib import Path
from typing import Literal, Optional

# 3rd party
import mkdocs.plugins
from material import __version__ as material_version
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page
from mkdocs.utils import yaml_load
from mkdocs.utils.meta import get_data

# ###########################################################################
# ########## Global ################
# ##################################


logger = logging.getLogger("mkdocs")
log_prefix = f"[{__name__}] "

# ###########################################################################
# ########## Functions #############
# ##################################


def get_latest_content(
    content_type: Literal["articles", "rdp"],
    count: int = 10,
    social_card_image_base: str = "https://geotribu.fr/assets/images/social/",
):
    output_contents_list: list[Page] = []

    if content_type == "articles":
        glob_pattern = "202*/202*.md"
    elif content_type == "rdp":
        glob_pattern = "202*/rdp_202*.md"

    for content in sorted(
        Path(f"content/{content_type}/").glob(glob_pattern), reverse=True
    )[:count]:
        with content.open(encoding="utf-8-sig", errors="strict") as f:
            source = f.read()

        page_meta = get_data(source)[1]

        page_rel = str(content.relative_to("content/"))[:-3]

        if page_meta.get("image") is None or page_meta.get("image") == "":
            social_card_url = f"{social_card_image_base}{page_rel}.png"
            output_contents_list.append(
                get_data(source)[1] | {"url_rel": page_rel} | {"image": social_card_url}
            )
        else:
            output_contents_list.append(get_data(source)[1] | {"url_rel": page_rel})

    return output_contents_list


def is_mkdocs_theme_material_insiders() -> Optional[bool]:
    """Check if the material theme is community or insiders edition.

    Returns:
        bool: True if the theme is Insiders edition. False if community.
    """
    if material_version is not None and "insiders" in material_version:
        logger.debug(log_prefix + "Material theme edition INSIDERS")
        return True
    else:
        logger.debug(log_prefix + "Material theme edition COMMUNITY")
        return False


# ###########################################################################
# ########## Hooks #################
# ##################################


@mkdocs.plugins.event_priority(10)
def on_config(config: MkDocsConfig) -> MkDocsConfig:
    """The config event is the first event called on build and
    is run immediately after the user configuration is loaded and validated.
    Any alterations to the config should be made here.

    See: https://www.mkdocs.org/user-guide/plugins/#on_config

    Args:
        config (config_options.Config): global configuration object

    Returns:
        MkDocsConfig: global configuration object
    """
    # determine the website flavor
    config_filename = Path(config.get("config_file_path")).name
    if config_filename == "mkdocs.yml":
        config["extra"]["website_flavor"] = "insiders"
    elif config_filename == "mkdocs-free.yml":
        config["extra"]["website_flavor"] = "community"
    else:
        config["extra"]["website_flavor"] = "minimal"

    # check if insiders version is installed
    if (
        config["extra"]["website_flavor"] == "insiders"
        and not is_mkdocs_theme_material_insiders()
    ):
        logger.warning(
            log_prefix
            + f"Le fichier {config.get('config_file_path')} contient des paramètres ou "
            "plugins uniquement disponibles dans la version Insiders (payante) du thème "
            "Material. Or c'est la version community (gratuite) qui est installée "
            f"({material_version}). La génération va probablement échouer. Deux solutions :"
            "A. Installer la version Insiders (requiert un jeton GitHub). "
            "B. Utiliser la configuration basée sur la version communautaire (gratuite), "
            "par exemple : 'mkdocs build -f mkdocs-free.yml'"
        )
        config["extra"]["website_flavor"] = "community"

    logger.info(
        log_prefix + f"Génération du site {config.get('site_name')} "
        f"en version {config.get('extra').get('website_flavor').upper()}"
    )

    # latest contents
    latest_contents: dict = {"articles": [], "rdp": []}
    for k in latest_contents:
        latest_contents[k] = get_latest_content(
            content_type=k,
            social_card_image_base=f"{config.get('site_url')}assets/images/social/",
        )

    config["extra"]["latest"] = latest_contents
    logger.info(
        log_prefix + "Contenus récents ajoutés à la configuration globale du site."
    )

    # -- LOAD SUBCONFIGS --

    # list files to append
    configs_to_merge = Path("config").glob("*.yml")

    # load final config
    for cfg_file in configs_to_merge:
        logger.info(log_prefix + f"Chargement de la sous-configuration : {cfg_file}")
        dest_section = cfg_file.stem.split("_")[0]
        # print(dest_section)
        with cfg_file.open(mode="r") as part_config:
            cfg_data = yaml_load(part_config)
        out_section = config.get(dest_section)
        print(
            # out_section,
            type(out_section),
            isinstance(out_section, (dict, list)),
        )
        if isinstance(out_section, list):
            out_section.append(cfg_data)
        elif isinstance(out_section, dict):
            out_section.update(cfg_data)
        else:
            print("toto")
            logging.info(
                log_prefix
                + f"La section '{cfg_file.stem}' n'existe pas et va donc être ajoutée."
            )
            config[cfg_file.stem] = cfg_data
        break

    return config

    # # write merged final config file
    # with Path("mkdocs-generated-configuration.yml").open(
    #     "w", encoding="UTF-8"
    # ) as out_file:
    #     yaml.dump(
    #         config.__dict__,
    #         out_file,
    #         sort_keys=False,
    #         default_flow_style=False,
    #         encoding="UTF8",
    #     )

    return config
