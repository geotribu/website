#! python3  # noqa: E265

# ############################################################################
# ########## Libraries #############
# ##################################

# standard lib
import logging
from collections import Counter
from pathlib import Path

# 3rd party
import matplotlib.pyplot as plt
from mkdocs.utils.meta import get_data
from wordcloud import WordCloud

# ###########################################################################
# ########## Global ################
# ##################################


logger = logging.getLogger("mkdocs")
content_types: tuple[str] = ("articles", "rdp")
content_tags: list[str] = []

# ###########################################################################
# ########## Main ##################
# ##################################


for content_type in content_types:
    for content in Path(f"content/{content_type}/").glob("**/*.md"):
        if content.parent.is_dir() and content.parent.name == "templates":
            continue

        with content.open(encoding="utf-8-sig", errors="strict") as f:
            source = f.read()

        page_meta = get_data(source)[1]
        if page_tags := page_meta.get("tags"):
            content_tags.extend(page_tags)


tags_freq = Counter(content_tags)


wordcloud = WordCloud(width=1000, height=500).generate_from_frequencies(tags_freq)

plt.figure(figsize=(15, 8))

# display and show "wc"
plt.imshow(wordcloud, interpolation="bilinear")

plt.axis("off")
plt.title("Mots-clés sur Geotribu", fontsize=13)
plt.show()
