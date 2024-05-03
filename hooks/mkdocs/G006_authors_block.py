#! python3  # noqa: E265

# ############################################################################
# ########## Libraries #############
# ##################################

# standard library
import logging
import re
from pathlib import Path

# 3rd party
from geotribu_cli.utils.slugger import sluggy
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.files import Files
from mkdocs.structure.pages import Page

# Mkdocs


# ###########################################################################
# ########## Global ################
# ##################################


logger = logging.getLogger("mkdocs")

dico_contributors = {}
exclude_files = [
    "confidentialite.md",
    "contributors.md",
    "credits.md",
    "index.md",
    "sponsoring.md",
]

author_block = """{% for author in page.meta.authors %}

### {{ author }}

--8<-- "content/team/julien-moura.md:author-sign-block"

{% endfor %}"""

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
            dico_contributors[Path(f.abs_src_path).stem] = None


# @mkdocs.plugins.event_priority(-100)
def on_page_markdown(
    markdown: str,
    page: Page,
    config: MkDocsConfig,
    files: Files,
):
    if "article" in page.file.abs_src_path:
        page_authors = page.meta.get("authors")
        if not isinstance(page_authors, list):
            logger.warning(
                f"L'entrée 'authors' de l'en-tête de la page '{page.file.abs_src_path}' est incorrecte."
            )
            continue

        if len(page_authors) > 1:
            author_block = "\n## Auteur·ices {: data-search-exclude }\n"
        else:
            author_block = "\n## Auteur·ice {: data-search-exclude }\n"

        for author in page_authors:
            if author == "Geotribu":
                author_block += '### L\'équipe Geotribu\n\n--8<-- "content/toc_nav_ignored/snippets/authors/geotribu.md:author-sign-block"\n\n'
            else:
                author_block += f'### [{author}](../../team/{sluggy(author)}.md)\n\n--8<-- "content/team/{sluggy(author)}.md:author-sign-block"\n\n'

        # Find and replace all external asset URLs in current page
        return re.sub(
            r"<!-- geotribu:authors-block -->",
            author_block,
            markdown,
            flags=re.I | re.M,
        )
