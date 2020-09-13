import string
from random import choice
from typing import Type

import pytest

from sylenium import Configuration
from sylenium import get_driver


@pytest.fixture
def driver_creator():
    return get_driver


@pytest.fixture
def default_driver():
    with get_driver() as driver:
        yield driver


@pytest.fixture
def headless_driver():
    with get_driver(config=Configuration(headless=True)) as driver:
        yield driver


@pytest.fixture()
def configuration() -> Type[Configuration]:
    return Configuration


@pytest.fixture
def random_string() -> str:
    characters = string.ascii_letters
    return "".join(choice(characters) for x in range(15))
