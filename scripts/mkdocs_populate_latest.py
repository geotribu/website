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
from mkdocs.utils.meta import get_data

# ###########################################################################
# ########## Global ################
# ##################################


logger = logging.getLogger("mkdocs")

# ###########################################################################
# ########## Functions #############
# ##################################


def get_latest_content(content_type: Literal["articles", "rdp"], count: int = 10):
    output_contents_list: list[Page] = []

    for content in sorted(
        Path(f"content/{content_type}/").glob("202*/202*.md"), reverse=True
    )[:count]:
        with content.open(encoding="utf-8-sig", errors="strict") as f:
            source = f.read()
        # markdown, meta = get_data(source)
        output_contents_list.append(get_data(source)[1])

    return output_contents_list


output_dict = {"latest": {"articles": [], "rdp": []}}
# print(get_latest_content(content_type="articles"))
for k in output_dict.get("latest"):
    output_dict["latest"][k] = get_latest_content(content_type=k)

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
