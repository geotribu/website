#! python3  # noqa: E265

# ############################################################################
# ########## Libraries #############
# ##################################

# standard library
import logging
from pathlib import Path
from typing import Literal

# 3rd party
import yaml
from mkdocs.structure.pages import Page
from mkdocs.utils import yaml_load
from mkdocs.utils.meta import get_data

# ###########################################################################
# ########## Global ################
# ##################################


logger = logging.getLogger("mkdocs")


# ###########################################################################
# ########## Functions #############
# ##################################


def get_latest_content(
    content_type: Literal["articles", "rdp"],
    count: int = 10,
    social_card_image_base: str = "https://static.geotribu.fr/assets/images/social/",
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


# charge la configuration
with Path("mkdocs.yml").open(mode="r", encoding="UTF8") as in_yaml:
    mkdocs_config = yaml_load(in_yaml)

output_dict = {"latest": {"articles": [], "rdp": []}}

# print(get_latest_content(content_type="articles"))

for k in output_dict.get("latest"):
    output_dict["latest"][k] = get_latest_content(
        content_type=k,
        social_card_image_base=f"{mkdocs_config.get('site_url')}assets/images/social/",
    )

with Path("config/extra_latest.yml").open("w", encoding="UTF-8") as out_file:
    yaml.safe_dump(
        output_dict,
        out_file,
        allow_unicode=True,
        default_flow_style=False,
        encoding="UTF8",
        # indent=4,
        sort_keys=True,
    )
