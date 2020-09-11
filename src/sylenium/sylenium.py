from __future__ import annotations

import typing
from typing import Optional

from sylenium import Configuration

if typing.TYPE_CHECKING:
    from sylenium import SyleniumDriver

DEFAULT_CONFIGURATION = Configuration()


def go(url: str) -> None:
    driver = get_driver()
    driver.get(url)


def register_configuration(config: Configuration) -> None:
    global DEFAULT_CONFIGURATION
    DEFAULT_CONFIGURATION = config


def get_default_configuration() -> Configuration:
    """
    Return the currently registered default configuration instance of sylenium.
    This is overridable using the register_configuration function, which should be invoked by the client
    in the instance where you want newly made drivers without explicit configuration to use your own settings.
    """
    return DEFAULT_CONFIGURATION


def get_driver(config: Optional[Configuration] = None) -> SyleniumDriver:
    from sylenium.driver.driver_factory import create_sylenium_driver

    config = config or get_default_configuration()
    return create_sylenium_driver(config)
