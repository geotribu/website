#! python3  # noqa: E265

# ############################################################################
# ########## Libraries #############
# ##################################

# standard library
import logging
import re
import ssl
from functools import lru_cache
from urllib import request
from urllib.error import HTTPError, URLError

# Mkdocs
import mkdocs.plugins
from geotribu_cli.utils.formatters import convert_octets

# ###########################################################################
# ########## Global ################
# ##################################


logger = logging.getLogger("mkdocs")

base_url: str = "https://static.geotribu.fr/"

REMOTE_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
}

regex_pattern = (
    r"(?:[!]\[(?P<caption>.*?)\])\((?P<image>.*?)(?P<description>\".*?\")?\s*\)"
)

exclude_list = [
    "articles/2008/2008-08-22_ajouter-des-shp-dans-geoserver.md",
    "toc_nav_ignored/qgis_resources_preview_table.md",
]

max_size: float = 2097152.0

# ###########################################################################
# ########## Functions #############
# ##################################


@lru_cache(maxsize=512)
def get_remote_image_length(
    image_url: str,
    http_method: str = "HEAD",
    attempt: int = 0,
    ssl_context: ssl.SSLContext = None,
) -> int:
    """Retrieve length for remote images (starting with 'http' \
        in meta.image or meta.illustration). \
        It tries to perform a HEAD request and get the length from the headers. \
        If it fails, it tries again with a GET and disabling SSL verification.

    :param image_url: remote image URL
    :type image_url: str
    :param http_method: HTTP method used to perform request, defaults to "HEAD"
    :type http_method: str, optional
    :param attempt: request tries counter, defaults to 0
    :type attempt: int, optional
    :param ssl_context: SSL context, defaults to None
    :type ssl_context: ssl.SSLContext, optional

    :return: image length as str or None
    :rtype: int
    """
    # prepare request
    req = request.Request(
        image_url,
        method=http_method,
        headers=REMOTE_REQUEST_HEADERS,
    )
    # first, try HEAD request to avoid downloading the image
    try:
        attempt += 1
        remote_img = request.urlopen(url=req, context=ssl_context, timeout=3)
        img_length = remote_img.getheader("content-length")
    except (HTTPError, URLError) as err:
        logger.debug(
            f"Image inacessible avec un HEAD: {image_url}. "
            "Trying again with GET and disabling SSL verification. "
            f"Attempt: {attempt}. "
            f"Trace: {err}"
        )
        if attempt < 2:
            return get_remote_image_length(
                image_url,
                http_method="GET",
                attempt=attempt,
                ssl_context=ssl._create_unverified_context(),
            )
        else:
            logger.warning(
                f"L'image {image_url} est inaccessible après {attempt} essais. "
                f"Trace: {err}"
            )
            return None

    except Exception as err:
        logger.error(
            f"Erreur fatale. Cause possible : URL d'image mal formatée. Trace: {err}"
        )
        return None

    return int(img_length)


@mkdocs.plugins.event_priority(-40)
def on_page_markdown(markdown, page, **kwargs):
    path = page.file.src_uri
    if path in exclude_list:
        logger.debug("Fichier ignoré car dans la liste d'exclusion.")
        return

    for match in re.findall(regex_pattern, markdown):
        img_url = match[1].strip()

        if img_url.startswith("http"):
            img_length = get_remote_image_length(image_url=img_url)
            if img_length and img_length > max_size:
                logger.error(
                    f"G002 || Poids des images maximum : {convert_octets(max_size)}. || "
                    f"'{path}' contient une image {img_url} "
                    f"de {convert_octets(img_length)}."
                )
            else:
                logger.debug(
                    "Impossible d'accéder à l'image {img_url} présente dans le fichier {path}"
                )
        else:
            logger.debug("Image locale ignorée")
