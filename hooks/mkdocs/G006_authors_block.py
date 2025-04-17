#! python3  # noqa: E265

# ############################################################################
# ########## Libraries #############
# ##################################

# standard library
import logging
import re
from html import escape
from pathlib import Path

# 3rd party
from babel.dates import format_date
from geotribu_cli.utils.slugger import sluggy
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

# ###########################################################################
# ########## Global ################
# ##################################


logger = logging.getLogger("mkdocs")
log_prefix = f"[{__name__}] "
dico_contributors = {}
exclude_files = [
    "confidentialite.md",
    "contributors.md",
    "credits.md",
    "index.md",
    "sponsoring.md",
]

regex_pattern = re.compile(
    pattern="<!-- geotribu:authors-block -->",
    flags=re.I | re.M,
)

# ###########################################################################
# ########## Functions #############
# ##################################


def on_files(files: Files, config: MkDocsConfig):
    for f in files:
        filepath = Path(f.abs_src_path)
        if (
            "team" in f.abs_src_path
            and "archives" not in f.abs_src_path
            and filepath.suffix == ".md"
            and Path(f.abs_src_path).name not in exclude_files
        ):
            dico_contributors[Path(f.abs_src_path).stem] = 0


# @mkdocs.plugins.event_priority(-100)
def on_page_markdown(
    markdown: str,
    page: Page,
    config: MkDocsConfig,
    files: Files,
):
    if (
        "articles" in page.file.abs_src_path
        and "index" not in page.file.name
        and "templates" not in page.file.abs_src_path
    ):
        page_authors = page.meta.get("authors")
        if not isinstance(page_authors, list):
            logger.warning(
                log_prefix
                + f"L'entrée 'authors' de l'en-tête de la page '{page.file.abs_src_path}' est incorrecte."
            )
            return

        if len(page_authors) > 1:
            author_block = "\n## Auteur·ices {: data-search-exclude }\n"
        else:
            author_block = "\n## Auteur·ice {: data-search-exclude }\n"

        for author in page_authors:
            if author == "Geotribu":
                author_block += '### L\'équipe Geotribu\n\n--8<-- "content/toc_nav_ignored/snippets/authors/geotribu.md:author-sign-block"\n\n'
            else:
                if sluggy(author) not in dico_contributors:
                    logger.warning(
                        f"L'auteur/ice '{author}' du contenu '{page.file.abs_src_path}' "
                        f"n'a pas de page correspondante : {sluggy(author)}"
                    )
                    continue
                author_block += f'### [{author}](../../team/{sluggy(author)}.md "Voir la page complète de l\'auteur·ice avec la liste de ses articles")\n\n--8<-- "content/team/{sluggy(author)}.md:author-sign-block"\n\n'

                # -- Ajoute la page à la liste des articles dans la page auteur
                articles_headers = ""
                if dico_contributors.get(sluggy(author)) == 0:
                    articles_headers = "\n\n## Liste de mes articles\n"
                dico_contributors[sluggy(author)] = (
                    dico_contributors.get(sluggy(author)) + 1
                )

                # date
                item_date = format_date(
                    date=page.meta.get("date"), format="long", locale="fr_FR"
                )

                # icône
                item_icon = ""
                if page.meta.get("icon"):
                    item_icon = f" :{page.meta.get('icon').replace('/', '-')}:"

                # hyperlink data
                list_item_link_data = ""
                if (
                    page.meta.get("description")
                    and page.meta.get("description") != page.title
                ):
                    list_item_link_data += escape(
                        page.meta.get("description"), quote=True
                    )
                if page.meta.get("tags"):
                    if (
                        page.meta.get("description")
                        and page.meta.get("description") != page.title
                    ):
                        list_item_link_data += "<br/><br/>"
                    list_item_link_data += (
                        "<i>Mots-clés : "
                        f"{escape(', ', quote=True).join(page.meta.get('tags'))}</i>"
                    )

                with Path(f"content/team/{sluggy(author)}.md").open(
                    "a", encoding="UTF-8"
                ) as author_file:
                    author_file.write(articles_headers)
                    author_file.write(
                        f"\n-{item_icon} [{escape(page.title, quote=True)}](../{page.file.src_uri} '{list_item_link_data}') - _publié le {item_date}_"
                    )

        # on cherche et remplace la balise de bloc de signature en ignorant la casse
        # (re.I) et en gérant le multi-ligne (re.M)
        return regex_pattern.sub(
            author_block,
            markdown,
        )
