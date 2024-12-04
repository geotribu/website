#! python3  # noqa: E265

"""Script permettant de lister les derniers contenus avec leurs propriétés
    dans un fichier YAML. Utilisé pour la page d'accueil et les pages
    d'index des derniers contenus publiés.
"""

# ############################################################################
# ########## Libraries #############
# ##################################

# standard library
import locale
import logging
from datetime import datetime
from pathlib import Path
from typing import Literal
from zoneinfo import ZoneInfo

# 3rd party
import yaml
from mkdocs.structure.pages import Page
from mkdocs.utils.meta import get_data

# ###########################################################################
# ########## Global ################
# ##################################

# journalisation
logger = logging.getLogger("mkdocs")

# gestion des dates
config_tz = ZoneInfo("Europe/Paris")
locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")

# ###########################################################################
# ########## Functions #############
# ##################################


def format_datetime(in_datetime_string: str, out_format: str = "long") -> str:
    """Formatte un datetime au format textuel standard (isocalendar) en version textuelle.
        Proche du fonctionnement de 'babel.format_date'.

    :param str in_datetime_string: chaîne de caractères en entrée. Doit être au format ISO.
    :param str out_format: format de sortie, defaults to "long"

    :return str: chaîne de caractères formatée
    """
    dt = datetime.fromisoformat(in_datetime_string).replace(tzinfo=config_tz)
    if out_format == "long":
        return dt.strftime("%A %d %B %Y")


def get_latest_content(
    content_type: Literal["articles", "rdp"], count: int = 10
) -> list[dict]:
    """Liste les X (défini par 'count') derniers contenus d'un certain type
        en retournant les métadonnées de chaque contenu, ainsi que quelques
        attributs personnalisés.

    :param Literal[&quot;articles&quot;, &quot;rdp&quot;] content_type: type de contenu à lister
    :param int count: nombre de contenus à lister, defaults to 10

    :return list[dict]: liste des contenus avec leurs attributs
    """
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
        # markdown, meta = get_data(source)

        # ajout attributs personnalisés
        output_contents_list.append(
            # ajout URL relative
            get_data(source)[1]
            | {"url_rel": str(content.relative_to("content/"))[:-3]}
            # ajoute la date au format textuel
            | {
                "date_txt_full": format_datetime(
                    in_datetime_string=get_data(source)[1].get("date"),
                    out_format="long",
                )
            }
        )

    return output_contents_list


# ###########################################################################
# ########## Main ##################
# ##################################

output_dict = {"latest": {"articles": [], "rdp": []}}
# print(get_latest_content(content_type="articles"))
for k in output_dict.get("latest"):
    output_dict["latest"][k] = get_latest_content(content_type=k)

# écrit le fichier final
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
