import os
from dataclasses import dataclass
from dataclasses import field
from typing import Dict, Callable
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
from webdriver_manager.chrome import ChromeDriverManager


class BrowzerConfiguration:
    """
    The Browzer config assumes sensible defaults, however to implement your own config you should
    subclass this object and register the full path to your subclass through the ENV_BROWZER_CONFIG
    environment variable.  Upon loading Browzer will detect the env and instantiate your config with the
    overridden values.
    """
    def __init__(self, *args, **kwargs):
        self.browser: str = kwargs.pop('browser').lower()
        self.headless: bool = kwargs.pop('headless')
        self.remote: bool = kwargs.pop('remote')
        self.selenium_grid_url: str = kwargs.pop('selenium_grid_url').lower()
        self.selenium_grid_port: int = kwargs.pop('selenium_grid_port')
        self.browser_resolution: str = kwargs.pop('browser_resolution').lower()
        self.browser_version: str = kwargs.pop('browser_version').lower()
        self.driver_binary_path: str = kwargs.pop('driver_binary_path').lower()
        self.browser_capabilities: Dict = kwargs.pop('browser_capabilities')
        self.chrome_options: List = kwargs.pop('chrome_options')
        self.base_url: str = kwargs.pop('base_url')
        self.explicit_waiting: float = kwargs.pop('explicit_waiting')
        self.polling_interval: float = kwargs.pop('polling_interval')
        self.page_source_capturing: bool = kwargs.pop('page_source_capturing')
        self.page_screenshot_capturing: bool = kwargs.pop('page_screenshot_capturing')
        self.stack_trace_capturing: bool = kwargs.pop('stack_trace_capturing')
        self.javascript_clicks: bool = kwargs.pop('javascript_clicks')
        self.javascript_sendkeys: bool = kwargs.pop('javascript_sendkeys')
        self.default_selector: str = kwargs.pop('default_selector').lower()
        self.driver_listener: str = kwargs.pop('driver_listener').lower()

    def get_grid_info(self) -> str:
        """
        Resolves the selenium hub address for remote browsers.
        :return: String for the full hub address
        """
        if not self.remote:
            raise ValueError(
                "Using a selenium hub is not permitted unless IS_REMOTE is true"
            )
        return (
            f"{self.selenium_grid_url}:{self.selenium_grid_port}/wd/hub"
        )

    def get_browser_info(self) -> tuple:
        """
        Fetches the driver binary and version specified by the users config
        :return: A tuple of browser meta data relating to versioning and binary data
        """
        return self.driver_binary_path, self.browser_version

    def resolve_binary_path(self) -> str:
        """
        Decide if we need to:
        A) Acquire the driver binary binary path == 'acquire'
        B) Use a local path passed by the user if path is anything else
        :return: the path to the chrome-driver binary - downloaded or installed by the user
        """
        ver = self.browser_version
        path = self.driver_binary_path
        return ChromeDriverManager(ver).install() if path.lower() == "acquire" else path


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
        return merged_dictionary['browzer']
