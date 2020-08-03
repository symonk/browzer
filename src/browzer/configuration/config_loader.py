import os
from dataclasses import dataclass
from dataclasses import field
from typing import Dict
from typing import List
from typing import Optional

from browzer.constants.strings import BROWSER_BINARY_PATH
from browzer.constants.strings import BROWSER_RESOLUTION as RESOLUTION
from browzer.constants.strings import BROWSER_VERSION as VERSION
from browzer.constants.strings import BROWZER_CONFIGURATION
from browzer.constants.strings import CHROME
from browzer.constants.strings import CSS
from browzer.constants.strings import GRID_LOCALHOST
from browzer.helpers.operating_system.environ import get_dictionary_from_yaml
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
    IS_REMOTE: bool = False
    SELENIUM_GRID_URL: str = GRID_LOCALHOST
    SELENIUM_GRID_PORT: int = 4444
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
    DEFAULT_SELECTOR: str = CSS


class ConfigLoader:
    def __init__(self):
        self.configuration_container = ConfigurationYamlContainer()
        self.browzer_config = None

    def build_config(self) -> BrowzerConfiguration:
        return BrowzerConfiguration(
            **self.configuration_container.get_config_merged_dictionary()
        )


class ConfigurationYamlContainer:
    def __init__(self):
        self.user_cfg_path: Optional[str] = read_from_environ(BROWZER_CONFIGURATION)
        self.browzer_cfg_path: str = os.path.join(
            os.path.dirname(__file__), "default_configuration.yaml"
        )

    def get_config_merged_dictionary(self) -> Dict:
        user_dict = get_dictionary_from_yaml(self.user_cfg_path)
        browzer_dict = get_dictionary_from_yaml(self.browzer_cfg_path)
        merged_dictionary = {**browzer_dict, **user_dict}
        return merged_dictionary
