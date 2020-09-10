from os import environ
from typing import Any


def read_from_environ(key: str, default: Any = None) -> Any:
    """
    Wrapper around os environ lookups, can return any default value specified if the lookup was unsuccessful
    :param key: a str to lookup in os.environ
    :param default: the default value to return if os.environ did not contain the key
    :return: a string if successful of the keys value, else default
    """
    return environ.get(key, default)
