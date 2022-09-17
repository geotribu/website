import argparse
from pathlib import Path

import yaml
from yaml_env_tag import construct_env_tag

# GLOBALS
yaml.Loader.add_constructor("!ENV", construct_env_tag)

# CLI
parser = argparse.ArgumentParser(
    prog="MkDocsConfigMerger", description="Merge configuration files."
)
parser.add_argument(
    "-o",
    "--output-file",
    dest="output_config_file",
    type=Path,
    help="Path to the output configuration file.",
    default="mkdocs.yml",
)
args = parser.parse_args()

output_config_file = args.output_config_file

# check files exist
if not output_config_file.is_file():
    raise FileNotFoundError(output_config_file)

# list files to append
configs_to_merge = Path("config/").glob("*.yml")

# load final config
with output_config_file.open(mode="r") as in_yaml:
    config_to_complete = yaml.load(in_yaml, Loader=yaml.Loader)

for cfg_file in configs_to_merge:
    dest_section = cfg_file.stem.split("_")[0]
    with cfg_file.open(mode="r") as part_config:
        cfg_data = yaml.safe_load(part_config)

    out_section = config_to_complete.get(dest_section)
    if isinstance(out_section, list):
        out_section.append(cfg_data)

# write merged final config file
with Path("mkdocs-merged.yaml").open("w") as out_file:
    yaml.dump(config_to_complete, out_file, sort_keys=True, default_flow_style=False)
