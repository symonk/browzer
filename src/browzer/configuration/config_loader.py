from __future__ import annotations
import os
from typing import Dict
from typing import List
from typing import Optional

from webdriver_manager.chrome import ChromeDriverManager

from browzer.constants.strings import BROWZER_CONFIGURATION
from browzer.exceptions.exceptions import BrowzerConfigurationException
from browzer.helpers.operating_system.environ import get_dictionary_from_yaml
from browzer.helpers.operating_system.environ import read_from_environ


class BrowzerConfiguration:
    def __init__(
        self,
        browser: str,
        headless: bool,
        remote: bool,
        page_loading_strategy: str,
        selenium_grid_url: str,
        selenium_grid_port: int,
        browser_resolution: str,
        browser_version: str,
        driver_binary_path: Optional[str],
        browser_capabilities: Dict[str, str],
        chrome_options: List[str],
        base_url: str,
        explicit_waiting: float,
        polling_interval: float,
        page_source_capturing: bool,
        page_screenshot_capturing: bool,
        stack_trace_capturing: bool,
        javascript_clicks: bool,
        javascript_sendkeys: bool,
        driver_listener_module_class_path: str,
        default_selector: str,
    ):
        self._browser: str = browser
        self.headless: bool = headless
        self.remote: bool = remote
        self.selenium_grid_url: str = selenium_grid_url
        self.selenium_grid_port: int = selenium_grid_port
        self.browser_resolution: str = browser_resolution
        self.browser_version: str = browser_version
        self.driver_binary_path: str = driver_binary_path
        self.browser_capabilities: Dict[str, str] = browser_capabilities
        self.chrome_options: List[str] = chrome_options
        self.base_url: str = base_url
        self.explicit_waiting: float = explicit_waiting
        self.polling_interval: float = polling_interval
        self.page_source_capturing: bool = page_source_capturing
        self.page_screenshot_capturing: bool = page_screenshot_capturing
        self.stack_trace_capturing: bool = stack_trace_capturing
        self.javascript_clicks: bool = javascript_clicks
        self.javascript_sendkeys: bool = javascript_sendkeys
        self.driver_listener_module_class_path: str = driver_listener_module_class_path
        self.page_loading_strategy: str = page_loading_strategy
        self.default_selector: str = default_selector

    @property
    def browser(self) -> str:
        return self._browser

    @browser.setter
    def browser(self, value: str) -> None:
        supported = {"chrome", "firefox"}
        if value not in supported:
            raise BrowzerConfigurationException(
                f"Browser provided: {value} is not supported by Browzer.  Please select"
                f"Something from: {supported}"
            )
        self._browser = value.lower()

    def get_grid_info(self) -> str:
        """
        Resolves the selenium hub address for remote browsers.
        :return: String for the full hub address
        """
        if not self.remote:
            raise ValueError(
                "Using a selenium hub is not permitted unless IS_REMOTE is true"
            )
        return f"{self.selenium_grid_url}:{self.selenium_grid_port}/wd/hub"

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

    @classmethod
    def reload(cls) -> BrowzerConfiguration:
        return ConfigLoader().build_config()


class ConfigLoader:
    def __init__(self):
        self.configuration_container = ConfigurationYamlContainer()

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
        default_dict = get_dictionary_from_yaml(self.browzer_cfg_path)
        user_dict = get_dictionary_from_yaml(self.user_cfg_path)
        merged_dict = {}
        for d in [default_dict, user_dict]:
            for key, value in d.items():
                merged_dict.setdefault(key, {}).update(value)
        return merged_dict["browzer"]
