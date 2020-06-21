from dataclasses import dataclass
from dataclasses import field
from typing import Callable
from typing import Dict
from typing import Optional
from typing import Set
from typing import TypeVar

from webdriver_manager.chrome import ChromeDriverManager

from browzer.constants.strings import BROWSER_BINARY_PATH
from browzer.constants.strings import BROWSER_RESOLUTION as RESOLUTION
from browzer.constants.strings import BROWSER_VERSION as VERSION
from browzer.constants.strings import BROWZER_CONFIGURATION
from browzer.constants.strings import CHROME
from browzer.constants.strings import GRID_LOCALHOST
from browzer.helpers.importlib.importer import instantiate_class_from_path
from browzer.helpers.operating_system.environ import read_from_environ

ConfigTypeVar = TypeVar("ConfigTypeVar", bound="BrowzerConfiguration")


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
    IS_REMOTE: bool = False
    SELENIUM_GRID_URL: str = GRID_LOCALHOST
    SELENIUM_GRID_PORT: int = 4444
    BROWSER_RESOLUTION: str = RESOLUTION
    BROWSER_VERSION: str = VERSION
    DRIVER_BINARY_PATH: str = BROWSER_BINARY_PATH
    BROWSER_CAPABILITIES: Optional[Dict] = field(default_factory=dict)
    CHROME_OPTIONS: Optional[Set] = None
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


def load_browzer_config() -> ConfigTypeVar:
    """
    If the BROWZER_CONFIG environment variable has been setup, take its value and attempt to instantiate
    a custom user provided subclass of the config with their overridden values.
    :return: the default BrowzerConfiguration, or an instance of a user supplied subclass
    """
    has_custom = read_from_environ(BROWZER_CONFIGURATION, None)
    if not has_custom:
        return BrowzerConfiguration()
    else:
        return instantiate_class_from_path(has_custom)


class ConfigHelper:
    def __init__(self, config: BrowzerConfiguration):
        self.config = config

    def get_grid_info(self) -> str:
        """
        Resolves the selenium hub address for remote browsers.
        :return: String for the full hub address
        """
        if not self.config.IS_REMOTE:
            raise ValueError(
                "Using a selenium hub is not permitted unless IS_REMOTE is true"
            )
        return (
            f"{self.config.SELENIUM_GRID_URL}:{self.config.SELENIUM_GRID_PORT}/wd/hub"
        )

    def get_browser_info(self) -> tuple:
        """
        Fetches the driver binary and version specified by the users config
        :return: A tuple of browser meta data relating to versioning and binary data
        """
        return self.config.DRIVER_BINARY_PATH, self.config.BROWSER_VERSION

    def resolve_binary_path(self) -> str:
        """
        Decide if we need to:
        A) Acquire the driver binary binary path == 'acquire'
        B) Use a local path passed by the user if path is anything else
        :return: the path to the chrome-driver binary - downloaded or installed by the user
        """
        ver = self.config.BROWSER_VERSION
        path = self.config.DRIVER_BINARY_PATH
        return ChromeDriverManager(ver).install() if path.lower() == "acquire" else path
