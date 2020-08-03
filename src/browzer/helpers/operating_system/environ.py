from os import environ
from typing import Any
from typing import Dict
from typing import Optional

import yaml


def read_from_environ(key: str, default: Any = None) -> Any:
    """
    Wrapper around os environ lookups, can return any default value specified if the lookup was unsuccessful
    :param key: a str to lookup in os.environ
    :param default: the default value to return if os.environ did not contain the key
    :return: a string if successful of the keys value, else default
    """
    return environ.get(key, default)


def get_dictionary_from_yaml(path: Optional[str]) -> Dict:
    """
    :return: Given a yaml file path, return the dictionary of the yaml file safely parsed.
    """
    if path and path.endswith(".yaml"):
        with open(path) as file_stream:
            return yaml.safe_load(file_stream)
    return {}
