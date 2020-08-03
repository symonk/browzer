from __future__ import annotations
import os
from typing import Dict
from typing import List
from typing import Optional

from webdriver_manager.chrome import ChromeDriverManager

from browzer.constants.strings import BROWZER_CONFIGURATION
from browzer.exceptions.exceptions import BrowzerConfigValueError
from browzer.helpers.operating_system.environ import get_dictionary_from_yaml
from browzer.helpers.operating_system.environ import read_from_environ
from browzer.mixins.simple_eq_mixin import SimpleEQMixing
from browzer.mixins.simple_repr_mixin import SimpleReprMixin


class BrowzerConfiguration(SimpleReprMixin, SimpleEQMixing):
    """
    This is the core configuration class for browzer.  User provided yaml is merged into the defaults to provide
    an instance of this class.
    :param browser: The browser type to instantiate downstream. choices are: (chrome|firefox)
    :param headless: If the browsers instantiated will run headlessly. choices are: (True|False)
    :param remote: If the browser will be running using a seleniuim grid, likely in the cloud. choices are: (True|False)
    """

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
        self._headless: bool = headless
        self._remote: bool = remote
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
        """
        Getter for the browser attribute
        :return: The browser attribute (string)
        """
        return self._browser

    @browser.setter
    def browser(self, value: str) -> None:
        """
        Setter for the browser attribute.
        :param value: The browser to configure
        """
        supported = {"chrome", "firefox"}
        if value not in supported:
            raise BrowzerConfigValueError(
                f"Browser provided: {value} is not supported by Browzer.  Please select"
                f"Something from: {supported}"
            )
        self._browser = value.lower()

    @property
    def headless(self) -> bool:
        """
        The getter for the headless attribute
        :return: The headless attribute (boolean)
        """
        return self._headless

    @headless.setter
    def headless(self, value: bool) -> None:
        if isinstance(value, bool):
            self._headless = value
        else:
            raise BrowzerConfigValueError(
                f"Only boolean types are supported for headless, you provided: {type(value)}"
            )

    @property
    def remote(self) -> bool:
        """
        The getter for the remote attribute
        :return: The remote attribute (boolean)
        """
        return self._remote

    @remote.setter
    def remote(self, value: bool) -> None:
        if isinstance(value, bool):
            self._remote = value
        else:
            raise BrowzerConfigValueError(
                f"Only boolean types are supported for remote, you provided: {type(value)}"
            )

    def get_grid_info(self) -> str:
        """
        Resolves the selenium hub address for remote browsers.
        :return: String for the full hub address
        """
        if not self.remote:
            raise ValueError(
                "Using a selenium hub is not permitted unless remote is true"
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
