#! python3  # noqa: E265

"""Insert social share buttons in content.

Related resources:

- https://squidfunk.github.io/mkdocs-material/tutorials/blogs/engage/
- https://stackoverflow.com/questions/10713542/how-to-make-a-custom-linkedin-share-button
- https://stackoverflow.com/questions/24823114/post-to-reddit-via-url
- https://docs.bsky.app/docs/advanced-guides/intent-links
"""

# ############################################################################
# ########## Libraries #############
# ##################################

# standard library
import logging
import re
import urllib.parse
from textwrap import dedent

# Mkdocs
import mkdocs.plugins
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.structure.pages import Page

# ###########################################################################
# ########## Global ################
# ##################################


logger = logging.getLogger("mkdocs")

regex_pattern_include = re.compile(r"^(rdp|articles)/.*\.md$")

share_url_base_bluesky = "https://bsky.app/intent/compose"
share_url_base_mastodon = "https://mastodonshare.com/share"
share_url_base_linkedin = "https://www.linkedin.com/shareArticle"
share_url_base_reddit = "http://www.reddit.com/submit"

# Marker to prevent duplicate injections
SHARE_MARKER = "<!-- geotribu:social-share-buttons -->"

# ###########################################################################
# ########## Functions #############
# ##################################


@mkdocs.plugins.event_priority(-100)
def on_page_markdown(markdown: str, page: Page, config: MkDocsConfig, **kwargs) -> str:
    """Add social share buttons to the page content.

    Args:
        markdown (str): page content in markdown format
        page (Page): Mkdocs page object
        config (MkDocsConfig): Mkdocs configuration object

    Returns:
        str: markdown content with social share buttons appended
    """

    if not regex_pattern_include.match(page.file.src_uri):
        return markdown

    # Skip if marker already exists (prevent duplicate injections)
    if SHARE_MARKER in markdown:
        return markdown

    # prepare data
    page_authors = urllib.parse.quote(
        ", ".join(page.meta.get("authors", ["L'équipe Geotribu"]))
    )
    page_description = urllib.parse.quote(page.meta.get("description", "") + "\n")
    page_tags = "%20".join(
        [
            urllib.parse.quote(f"#{tag.replace(' ', '')}")
            for tag in page.meta.get("tags", [])
        ]
    )

    page_title = urllib.parse.quote(page.title + "\n")
    page_url = config.site_url + page.url

    # urls
    share_url_bluesky = (
        f"{share_url_base_bluesky}?text="
        f"{page_title}%0A%0A{page_description}"
        f"%0Apar%20{page_authors}.%20%0A%0A%0A%23Geotribu%0A"
        f"%0A%0ALire%20sur%20@geotribu.bsky.social%20:%20{page_url}"
        f"%0A%23Geotribu%20{page_tags}"
    )
    share_url_linkedin = (
        f"{share_url_base_linkedin}?url={page_url}"
        "&mini=true"
        # f"&title={page_title}"
        # f"&summary={page_description}"
        f"&source=Geotribu"
        f"&text={page_title}%20par%20{page_authors}%20sur%20%40Geotribu"
        f"%0A%0A{page_description}"
        f"%0A%0A👉 {page_url} 👈"
        f"%0A%0A%23Geotribu%20{page_tags}"
    )
    share_url_mastodon = (
        f"{share_url_base_mastodon}?url={page_url}"
        f"&text={page_title}%20par%20{page_authors}%20"
        "sur%20%40geotribu%40mapstodon.space%20"
        f"%0A%0A{page_description}%0A"
        f"%0A%23GISTribe%20{page_tags}"
    )
    share_url_reddit = f"{share_url_base_reddit}?title={page_title}%20par%20{page_authors}&url={page_url}"

    return markdown + dedent(
        f"""\n{SHARE_MARKER}\n\nPartager sur :
        [:fontawesome-brands-bluesky:]({share_url_bluesky} "Partager sur BlueSky"){{: rel="noopener" }}
        [:fontawesome-brands-linkedin:]({share_url_linkedin} "Partager sur LinkedIn"){{: rel="noopener" }}
        [:fontawesome-brands-mastodon:]({share_url_mastodon} "Partager sur Mastodon"){{: rel="noopener" }}
        [:fontawesome-brands-reddit:]({share_url_reddit} "Partager sur Reddit"){{: rel="noopener" }}
        {{: align=middle }}
    """
    )
