from pathlib import Path

import yaml
from yaml_env_tag import construct_env_tag

yaml.Loader.add_constructor("!ENV", construct_env_tag)

cfg_final = Path("mkdocs.yml")

# check files exist
if not cfg_final.is_file():
    raise FileNotFoundError(cfg_final)

# list files to append
configs_to_merge = Path("config/").glob("*.yml")

# load final config
with cfg_final.open(mode="r") as in_yaml:
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
