from typing import Type

import pytest

from sylenium import Configuration


@pytest.fixture()
def configuration() -> Type[Configuration]:
    return Configuration
