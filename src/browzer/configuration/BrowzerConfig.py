from dataclasses import dataclass
from dataclasses import field
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional

from browzer.constants.strings import BROWSER_BINARY_PATH
from browzer.constants.strings import BROWSER_RESOLUTION as RESOLUTION
from browzer.constants.strings import BROWSER_VERSION as VERSION
from browzer.constants.strings import BROWZER_CONFIG
from browzer.constants.strings import CHROME
from browzer.constants.strings import GRID_LOCALHOST
from browzer.helpers.importlib.importer import instantiate_class_from_path
from browzer.helpers.operating_system.environ import read_from_environ


@dataclass
class BrowzerConfiguration:
    """
    The Browzer config assumes sensible defaults, however to implement your own config you should
    subclass this object and register the full path to your subclass through the ENV_BROWZER_CONFIG
    environment variable.  Upon loading Browzer will detect the env and instantiate your config with the
    overridden values.
    """

    BROWSER: str = CHROME
    HEADLESS: bool = False
    SELENIUM_GRID_URL: str = GRID_LOCALHOST
    BROWSER_RESOLUTION: str = RESOLUTION
    BROWSER_VERSION: str = VERSION
    DRIVER_BINARY_PATH: str = BROWSER_BINARY_PATH
    BROWSER_CAPABILITIES: Optional[Dict] = field(default_factory=dict)
    CHROME_OPTIONS: Optional[List] = None
    BASE_URL: str = None
    EXPLICIT_WAIT: float = 30.00
    POLLING_INTERVAL: float = 0.25
    PAGE_SOURCE_CAPTURE: bool = False
    SCREENSHOT_CAPTURE: bool = False
    STACK_TRACE_CAPTURE: bool = False
    JAVASCRIPT_CLICK: bool = False
    JAVASCRIPT_SENDKEYS: bool = False
    DEFAULT_SELECTOR: str = "css"
    DRIVER_LISTENER: Optional[Callable] = None
    MAXIMIZED: bool = True


def load_browzer_config() -> BrowzerConfiguration:
    """
    If the BROWZER_CONFIG environment variable has been setup, take its value and attempt to instantiate
    a custom user provided subclass of the config with their overridden values.
    :return: the default BrowzerConfiguration, or an instance of a user supplied subclass
    """
    has_custom = read_from_environ(BROWZER_CONFIG, None)
    if not has_custom:
        return BrowzerConfiguration()
    else:
        return instantiate_class_from_path(has_custom)
