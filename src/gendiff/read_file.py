import json
from pathlib import Path

import yaml


def read_json(file_path):
    with open(file_path) as file:
        return json.load(file)


def read_yaml(file_path):
    with open(file_path) as file:
        return yaml.load(file, Loader=yaml.FullLoader)


def read_file(file_path):
    extension = Path(file_path).suffix

    match extension:
        case ".json":
            return read_json(file_path)
        case ".yml" | ".yaml":
            return read_yaml(file_path)

    return None
