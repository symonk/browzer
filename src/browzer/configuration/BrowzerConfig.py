from dataclasses import dataclass
from dataclasses import field
from typing import Dict, Callable, List
from typing import Optional

from browzer.constants.strings import CHROME
from browzer.constants.strings import GRID_LOCALHOST
from browzer.constants.strings import BROWSER_RESOLUTION as RESOLUTION
from browzer.constants.strings import BROWSER_BINARY_PATH
from browzer.constants.strings import BROWSER_VERSION as VERSION


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
