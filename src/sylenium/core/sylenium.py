from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from sylenium import config
from sylenium.core.webdriver.driver_factories import WebDriverFactory


def get_driver() -> RemoteWebDriver:
    """
    Sylenium entry point for fetching a thread local scoped web driver instance.  Before invoking this function
    to retrieve your customised driver, you should invoke initialize()
    """
    return WebDriverFactory(config=config).create_driver()
