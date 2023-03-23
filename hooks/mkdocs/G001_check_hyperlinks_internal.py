#! python3  # noqa: E265

# ############################################################################
# ########## Libraries #############
# ##################################

# standard library

import logging
import re

# Mkdocs
import mkdocs.plugins

# ###########################################################################
# ########## Global ################
# ##################################

logger = logging.getLogger("mkdocs")

base_url: str = "https://static.geotribu.fr/"

pattern = re.compile(r"\[([^][]+)\](\(((?:[^()]+|(\?2))+)\))")
# Anything that isn't a square closing bracket
name_regex = "[^]]+"
# http:// or https:// followed by anything but a closing parenthesis
url_regex = "http[s]?://[^)]+"
pattern = rf"\[({name_regex})]\(\s*({url_regex})\s*\)"


exclude_list = [
    "contribuer/guides/markdown_quality.md",
]

# ###########################################################################
# ########## Functions #############
# ##################################


@mkdocs.plugins.event_priority(-50)
def on_page_markdown(markdown, page, **kwargs):
    path = page.file.src_uri
    if path in exclude_list:
        return
    # for m in re.finditer(r"\bhttps://static.geotribu.fr/[^) ]+", markdown):
    # for match in pattern.finditer(markdown):
    for match in re.findall(pattern, markdown):
        # print(path, match)
        if match[1].startswith(base_url) and len(match[1]) > len(base_url):
            logger.error(
                f"G001 || Les liens internes doivent etre relatifs par rapport à la racine du site. || '{path}' contient un lien interne absolu : {match[1]}"
            )
