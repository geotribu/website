# standard
import logging
from datetime import date, datetime
from pathlib import Path

import yaml
from mkdocs.utils import write_file
from yaml import SafeDumper

IS_BUILD = False
dt_format = "%Y-%m-%d %H:%M"


# define a custom representer for strings
def quoted_presenter(dumper, data):
    return dumper.represent_scalar("tag:yaml.org,2002:str", data, style='"')


class MyDumper(SafeDumper):

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)

    # def represent_data(self, data):
    #     if isinstance(data, str) and data.isdigit():
    #         return self.represent_scalar("tag:yaml.org,2002:str", data, style="'")

    #     return super(CustomDumper, self).represent_data(data)


MyDumper.add_representer(
    type(None),
    lambda dumper, value: dumper.represent_scalar("tag:yaml.org,2002:null", ""),
)
# MyDumper.add_representer(str, quoted_presenter)


def on_startup(command, dirty):
    global IS_BUILD
    IS_BUILD = command == "build"


def on_page_markdown(markdown, page, config, files):

    if not page.meta.get("date"):
        print(f"no date, skipping {page}")
        return

    content_date = page.meta.get("date")
    target_dir = Path(config["docs_dir"]).parent / "dates"

    if type(content_date) == date:
        logging.debug(
            f"File {page.file.abs_src_path} has already a proper date defined in YAML "
            "frontmatters."
        )
        return
    elif isinstance(content_date, str):
        # parse date from str
        try:
            page.meta["date"] = datetime.strptime(content_date, dt_format).date()
        except ValueError:
            logging.error(
                f"File {page.file.abs_src_path} has a date in YAML frontmatters but it does "
                f"not comply with expected format ({dt_format}): {content_date}"
            )

        # write new version
        target_path = page.file.abs_src_path.replace(
            config["docs_dir"], str(target_dir)
        )
        output_bytes = f"---\n{yaml.dump(page.meta, allow_unicode=True, width=1000, indent=4, Dumper=MyDumper, sort_keys=False).strip()}\n---\n\n{markdown}".encode()
        write_file(output_bytes, target_path)
