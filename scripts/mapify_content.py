"""

    refs
    https://towardsdatascience.com/how-to-draw-a-map-using-python-and-word2vec-e9627b4eae34
    https://en.wikipedia.org/wiki/Word_embedding
    https://medium.com/pythoneers/nlp-word2vec-with-python-example-3713e3157809
    https://en.wikipedia.org/wiki/Word2vec
"""
import string
from functools import lru_cache
from pathlib import Path

import frontmatter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stops = set(stopwords.words("french")).union(set(string.punctuation))
# print(sorted(stops))

start_folder = Path("content/")
name_exclusions = ("template",)


class Point(object):
    """A 3D point in the EPSG:4979"""

    def __init__(self, x, y, z):
        """
        Construct a point object given the x, y and z coordinates

        Parameters:
            x (float): x coordinate
            y (float): y coordinate
            z (float): z coordinate
        """
        self._x = x
        self._y = y
        self._y = z


def filter_phrase(input_phrase: str) -> tuple:
    return (
        word
        for word in word_tokenize(text=input_phrase, language="french")
        if word.lower() not in stops
    )


@lru_cache(maxsize=512)
def word2numbers(input_word: str) -> int:
    outnumber = 0
    for letter in input_word:
        outnumber += ord(letter) * (input_word.index(letter) + 1)

    return outnumber


content_properties = {}

for md in start_folder.glob("articles/**/*.md"):
    if "template" in md.name:
        continue
    md_frontmatter = frontmatter.load(str(md.resolve()))
    # print(md_frontmatter.get("title"))

    if not md_frontmatter.get("title"):
        print("En-tête incorrect dans le fichier : ", md.resolve())
        continue

    content_properties[md.relative_to(start_folder)] = {
        # "authors": [
        #     word2numbers(author_part)
        #     for title_word in md_frontmatter.get("title").split()
        # ],
        "title": [
            word2numbers(title_word)
            for title_word in md_frontmatter.get("title").split()
        ],
        "tags": [word2numbers(tag) for tag in md_frontmatter.get("tags")],
    }

print(word_tokenize(md_frontmatter.get("title"), language="french"))
print(tuple(filter_phrase(md_frontmatter.get("title"))))

# print(content_properties)

print(word2numbers("QGIS"), word2numbers("ArcGIS"), word2numbers(("Julien MOURA")))
