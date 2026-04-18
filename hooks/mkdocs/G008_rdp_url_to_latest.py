#! python3  # noqa: E265

import logging
from pathlib import Path

import mkdocs.plugins
from mkdocs.config.defaults import MkDocsConfig

logger = logging.getLogger("mkdocs")
log_prefix = f"[{__name__}] "


@mkdocs.plugins.event_priority(5)
def on_config(config: MkDocsConfig) -> MkDocsConfig:
    """
    Configure une redirection de /rdp/ vers la dernière RDP publiée,
    à l'aide du plugin mkdocs-redirects.
    """

    rdp_files = sorted(Path("content/rdp/").glob("20*/rdp_20*.md"), reverse=True)

    if not rdp_files:
        return config

    latest_rdp = str(rdp_files[0].relative_to("content/"))

    config.plugins["redirects"].config["redirect_maps"]["rdp/index.md"] = latest_rdp
    logger.info(log_prefix + f"Redirection de /rdp/ vers {latest_rdp} ajoutée.")

    return config
