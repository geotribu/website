#! python3  # noqa: E265

# ############################################################################
# ########## Libraries #############
# ##################################

# standard library
import logging
from pathlib import Path
from typing import Literal

# 3rd party
import mkdocs.plugins
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page
from mkdocs.utils.meta import get_data

# ###########################################################################
# ########## Global ################
# ##################################


logger = logging.getLogger("mkdocs")
log_prefix = f"[{__name__}] "
witness_output = Path("./latest_content.yml")

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
    else:
        config["extra"]["website_flavor"] = "minimal"

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
    print(
        latest_contents,
        file=witness_output.open(mode="w", encoding="UTF-8"),
    )
    logger.info(
        log_prefix + "Contenus récents ajoutés à la configuration globale du site. "
        f"Également écrits dans le fichier témoin : {witness_output.resolve()}"
    )
