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

# balises pour éviter de dupliquer la section "Liste de mes articles" autogénérée
authors_with_existing_autolist: set[str] = set()
AUTHOR_ARTICLES_AUTOLIST_START = "<!-- --8<-- [start:author-articles-autolist] -->"
AUTHOR_ARTICLES_AUTOLIST_END = "<!-- --8<-- [end:author-articles-autolist] -->"

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

            # Si y'a déjà le marqueur de début, on met la page auteur dans une liste à
            # ignorer au prochain build.
            content = filepath.read_text(encoding="UTF-8")
            if AUTHOR_ARTICLES_AUTOLIST_START in content:
                authors_with_existing_autolist.add(filepath.stem)
                logger.debug(
                    log_prefix
                    + f"[G006] Liste auto-générée déjà présente pour : {filepath.stem}"
                )


# @mkdocs.plugins.event_priority(-100)
def on_page_markdown(
    markdown: str,
    page: Page,
    config: MkDocsConfig,
    files: Files,
):
    if (
        "articles" in page.file.abs_src_path
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
            author_slug = sluggy(author)

            if author == "Geotribu":
                author_block += '### L\'équipe Geotribu\n\n--8<-- "content/toc_nav_ignored/snippets/authors/geotribu.md:author-sign-block"\n\n'
            else:
                if author_slug not in dico_contributors:
                    logger.error(
                        log_prefix
                        + f"L'auteur/ice '{author}' du contenu '{page.file.abs_src_path}' "
                        f"n'a pas de page correspondante : {author_slug}"
                    )
                    continue
                author_block += f'### [{author}](../../team/{author_slug}.md "Voir la page complète de l\'auteur·ice avec la liste de ses articles")\n\n--8<-- "content/team/{author_slug}.md:author-sign-block"\n\n'

                if author_slug in authors_with_existing_autolist:
                    # liste autogénérée déjà présente dans le fichier, probablement via
                    # un précédent build (rebuild)
                    dico_contributors[author_slug] = (
                        dico_contributors.get(author_slug) + 1
                    )
                    logger.debug(
                        log_prefix
                        + f"[G006] La liste des articles existe déjà pour '{author_slug}'."
                    )
                else:

                    # -- Ajoute la page à la liste des articles dans la page auteur
                    articles_headers = ""

                    if dico_contributors.get(author_slug) == 0:
                        # intère une balise pour éviter de dupliquer cette section quand
                        # plusieurs builds sont successivement lancés
                        articles_headers += f"\n{AUTHOR_ARTICLES_AUTOLIST_START}"
                        articles_headers += "\n## Liste de mes articles\n"

                    dico_contributors[author_slug] = (
                        dico_contributors.get(author_slug) + 1
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

                    with Path(f"content/team/{author_slug}.md").open(
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


def on_post_build(config: MkDocsConfig):
    for author_slug, count in dico_contributors.items():
        # auteuricess ayant au moins 1 article ET dont la liste a été
        # créée durant ce build.
        if count == 0 or author_slug in authors_with_existing_autolist:
            continue

        author_file_path = Path(f"content/team/{author_slug}.md")
        if not author_file_path.exists():
            continue

        content = author_file_path.read_text(encoding="UTF-8")

        # on ajoute le marqueur de fin que si le marqueur de début
        # est présent mais que la fin est absente
        if (
            AUTHOR_ARTICLES_AUTOLIST_START in content
            and AUTHOR_ARTICLES_AUTOLIST_END not in content
        ):
            with author_file_path.open("a", encoding="UTF-8") as f:
                f.write(f"\n\n{AUTHOR_ARTICLES_AUTOLIST_END}\n")
            logger.debug(
                log_prefix
                + "Balise de fin de liste autogénérée des articles ajoutée à la "
                f"page '{author_slug}' ({count} article(s))."
            )
