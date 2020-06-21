__version__ = "0.0.1"

import atexit
from typing import Type

from browzer.configuration.configuration import BrowzerConfiguration  # noqa: F401
from browzer.configuration.configuration import load_browzer_config
from browzer.core.pages.base_page import BrowzerPage  # noqa: F401
from browzer.core.webdriver.driver_factory import BrowzerDriverFactory
from browzer.core.webelement.browzer_element import BrowzerElement  # noqa: F401

browzer_config: Type[BrowzerConfiguration] = load_browzer_config()
driver_factory = BrowzerDriverFactory(browzer_config)


@atexit.register
def clean_up_drivers():
    for driver in driver_factory.drivers.values():
        driver.quit()


__all__ = [browzer_config]
