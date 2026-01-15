#! python3  # noqa: E265

"""
Description: Merge different mkdocs configuration files from a directory.
Author: Julien Moura (@Guts@github.com)

Requires: MkDocs installed (it uses its YAML loader)
"""

# -- IMPORTS --

# standard lib
import argparse
import logging
from pathlib import Path

# 3rd party
import yaml
from mkdocs.utils.yaml import yaml_load

# -- GLOBALS --
logging.basicConfig(level=logging.INFO)

# -- CLI --
parser = argparse.ArgumentParser(
    prog="MkDocsConfigMerger", description="Merge configuration files.", add_help=True
)
parser.add_argument(
    "-c",
    "--config-file",
    dest="output_config_file",
    type=Path,
    help="Path to the configuration file to complete. Must exist.",
    default="mkdocs.yml",
)
parser.add_argument(
    "-i",
    "--input-folder",
    dest="input_config_folder",
    type=Path,
    help="Path to the folder where to load configurations files to merge. Must exist.",
    default="./config",
)

args = parser.parse_args()

output_config_file = args.output_config_file
input_config_folder = args.input_config_folder

# -- CHECKS --

if not output_config_file.is_file():
    raise FileNotFoundError(output_config_file)
if not input_config_folder.is_dir():
    raise FileNotFoundError(input_config_folder)

# -- MAIN --

# list files to append
configs_to_merge = input_config_folder.glob("*.yml")

# load final config
with output_config_file.open(mode="r", encoding="UTF8") as in_yaml:
    config_to_complete = yaml_load(in_yaml)

for cfg_file in configs_to_merge:
    dest_section = cfg_file.stem.split("_")[0]
    with cfg_file.open(mode="r") as part_config:
        cfg_data = yaml_load(part_config)
    out_section = config_to_complete.get(dest_section)
    if isinstance(out_section, list):
        out_section.append(cfg_data)
    elif isinstance(out_section, dict):
        out_section.update(cfg_data)
    else:
        logging.info(
            f"La section '{cfg_file.stem}' n'existe pas et va donc être ajoutée."
        )
        config_to_complete[cfg_file.stem] = cfg_data


# write merged final config file
with output_config_file.open("w", encoding="UTF-8") as out_file:
    yaml.dump(
        config_to_complete,
        out_file,
        sort_keys=False,
        default_flow_style=False,
        encoding="UTF8",
    )
