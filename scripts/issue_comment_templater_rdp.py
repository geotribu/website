# standard
import json
import logging
from os import getenv
from pathlib import Path

# 3rd party
from jinja2 import Environment, FileSystemLoader, select_autoescape

# variables
submitted_form_data: Path = Path("rdp_news_submitted.json")
issue_comment_template: Path = Path("issue_comment_rdp_template.jinja")
logging.basicConfig(encoding="utf-8", level=logging.INFO)

# load JSON from issue form
with submitted_form_data.open("r", encoding="UTF8") as in_json:
    data = json.load(in_json)

# complete data with environment vars
data["issue_author"] = getenv("ISSUE_AUTHOR", "Inconnu(e)")
data["issue_id"] = getenv("ISSUE_ID", "99999")

# handle legacy form keys id (- not supported)
new_keys = [k.replace("-", "_") for k in data.keys()]
data = dict(zip(new_keys, data.values()))

# ensure image description and replacement text
img_thumbnail_url = data.get("in_news_icon")
if img_thumbnail_url.startswith("http"):
    try:
        img_thumbnail_path = Path(img_thumbnail_url)
        img_thumbnail_name = img_thumbnail_path.stem
        img_description = f"vignette {img_thumbnail_name}"
    except Exception as exc:
        logging.error(
            f"Failed to extract image name from URL: {img_thumbnail_url}. Trace: {exc}"
        )
        img_description = "vignette news"
else:
    img_description = data.get("in_news_icon")
data["in_icon_description"] = img_description

# improve tags
if isinstance(data.get("in_news_tags"), str) and len(data.get("in_news_tags")):
    data["in_news_tags"] = sorted(data.get("in_news_tags").split(","))
else:
    data["in_news_tags"] = []

# fill the comment template
env = Environment(
    autoescape=select_autoescape(["html", "xml"]),
    loader=FileSystemLoader(Path(__file__).parent),
)

template = env.get_template(issue_comment_template.name)

# write to the output
with Path("rdp_news_submitted_comment_output.md").open(
    "w", encoding="UTF8"
) as out_file:
    out_file.write(template.render(data))
