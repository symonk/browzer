__version__ = "0.0.1"

import atexit

from browzer.configuration.config_loader import BrowzerConfiguration
from browzer.configuration.config_loader import ConfigLoader
from browzer.core.pages.base_page import BrowzerPage  # noqa: F401
from browzer.core.webdriver.driver_factory import BrowzerDriverFactory
from browzer.core.webelement.browzer_element import BrowzerElement  # noqa: F401

browzer_config: BrowzerConfiguration = ConfigLoader().build_config()


driver_factory = BrowzerDriverFactory()


@atexit.register
def clean_up_drivers():
    for driver in driver_factory.drivers.values():
        driver.quit()


__all__ = [browzer_config]
