__version__ = "0.0.0"

import atexit

from browzer.configuration.BrowzerConfig import BrowzerConfiguration  # noqa: F401
from browzer.configuration.BrowzerConfig import load_browzer_config
from browzer.core.webdriver.driver_factory import BrowzerDriverFactory

driver_manager = BrowzerDriverFactory(load_browzer_config())


@atexit.register
def clean_up_drivers():
    for driver in driver_manager.drivers.values():
        driver.quit()


__all__ = [driver_manager]
