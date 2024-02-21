#! python3  # noqa: E265

"""Script meant to be used as one-shot to convert YAML fonrtmatter 'date' value from
    str into date.

See: https://github.com/mkdocs/mkdocs/discussions/3576

"""

# -- IMPORTS --

# standard
import logging
from datetime import date, datetime
from pathlib import Path

# 3rd party
import frontmatter

# -- MAIN --

dt_format = "%Y-%m-%d %H:%M"
logging.basicConfig(level=logging.INFO)

# match = re.search(
#     r"^---\s*\n.*?date: (\d{4}-\d{2}-\d{2}).*?\n---",
#     content,
#     re.DOTALL | re.MULTILINE,
# )

for md_filepath in Path("content").glob("**/*.md"):
    # read and load content
    with md_filepath.open(mode="r", encoding="UTF-8") as in_file:
        content = frontmatter.load(in_file)

    # manipulate date in YAML frontmatter
    if content_date := content.metadata.get("date"):
        if type(content_date) == date:
            logging.debug(
                f"File {md_filepath} has already a proper date defined in YAML "
                "frontmatters."
            )
            continue
        elif isinstance(content_date, str):
            # parse date from str
            try:
                content.metadata["date"] = datetime.strptime(
                    content_date, dt_format
                ).date()
            except ValueError:
                logging.error(
                    f"File {md_filepath} has a date in YAML frontmatters but it does "
                    f"not comply with expected format ({dt_format}): {content_date}"
                )

            # write new version
            with md_filepath.open(mode="w", encoding="UTF-8") as out_file:
                # frontmatter.dump(content, out_file) # not working
                out_file.write(
                    frontmatter.dumps(content, sort_keys=False, **{"indent": 4})
                )
        else:
            logging.warning(
                f"File {md_filepath} has a date in YAML frontmatters but it's not a "
                f"str: {content_date}"
            )

        continue

    logging.info(f"File has no date defined in YAML frontmatters: {md_filepath}")
