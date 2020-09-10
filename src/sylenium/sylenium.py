from sylenium import Configuration
from sylenium import session_manager

DEFAULT_CONFIGURATION = Configuration()


def go(url: str) -> None:
    driver = session_manager.fetch().get_driver()
    driver.get(url)


def register_configuration(config: Configuration) -> None:
    global DEFAULT_CONFIGURATION
    DEFAULT_CONFIGURATION = config
