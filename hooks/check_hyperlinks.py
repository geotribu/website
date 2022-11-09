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

pattern = re.compile(r"\[([^][]+)\](\(((?:[^()]+|(\?2))+)\))")
# Anything that isn't a square closing bracket
name_regex = "[^]]+"
# http:// or https:// followed by anything but a closing paren
url_regex = "http[s]?://[^)]+"

pattern = "\[({0})]\(\s*({1})\s*\)".format(name_regex, url_regex)

# ###########################################################################
# ########## Functions #############
# ##################################


@mkdocs.plugins.event_priority(-50)
def on_page_markdown(markdown, page, **kwargs):
    path = page.file.src_uri
    # for m in re.finditer(r"\bhttps://static.geotribu.fr/[^) ]+", markdown):
    # for match in pattern.finditer(markdown):
    for match in re.findall(pattern, markdown):
        # print(path, match)
        if match[1].startswith("https://static.geotribu.fr"):
            logger.warning(
                f"G001 || Les liens internes doivent etre relatifs par rapport à la racine du site. || '{path}' contient un lien interne absolu : {match[1]}"
            )
