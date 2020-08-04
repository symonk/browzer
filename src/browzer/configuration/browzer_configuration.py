from __future__ import annotations
import os
from typing import Dict
from typing import List
from typing import Optional

from webdriver_manager.chrome import ChromeDriverManager

from browzer.helpers.object_validator import enforce_type_of
from browzer.helpers.object_validator import enforce_value_is_in
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
        self._selenium_grid_url: str = selenium_grid_url
        self._selenium_grid_port: int = selenium_grid_port
        self._browser_resolution: str = browser_resolution
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
        enforce_value_is_in(
            iterable=supported, value=value, exc=BrowzerConfigValueError
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
        """
        The setter for the headless attribute
        """
        message = f"Only boolean types are supported for headless, you provided: {type(value)}"
        enforce_type_of(
            expected=bool, value=value, exc=BrowzerConfigValueError, msg=message
        )
        self._headless = value

    @property
    def remote(self) -> bool:
        """
        The getter for the remote attribute
        :return: The remote attribute (boolean)
        """
        return self._remote

    @remote.setter
    def remote(self, value: bool) -> None:
        """
        The setter for the remote attribute
        """
        message = (
            f"Only boolean types are supported for remote, you provided: {type(value)}"
        )
        enforce_type_of(
            expected=bool, value=value, exc=BrowzerConfigValueError, msg=message
        )
        self._remote = value

    @property
    def selenium_grid_url(self) -> str:
        """
        The getter for the selenium grid url attribute
        :return: The selenium grid hub url (str)
        """
        return self._selenium_grid_url

    @selenium_grid_url.setter
    def selenium_grid_url(self, value: str) -> None:
        """
        The setter for the selenium_grid_url attribute
        """
        # TODO -> Better validation, do not end with /wd/hub we append it etc
        message = f"selenium grid url must be a string, but you provided: {type(value)}"
        enforce_type_of(
            expected=str, value=value, exc=BrowzerConfigValueError, msg=message
        )
        self._selenium_grid_url = value

    @property
    def selenium_grid_port(self) -> int:
        """
        The getter for the selenium grid port attribute
        :return: The selenium grid hub port (int)
        """
        return self._selenium_grid_port

    @selenium_grid_port.setter
    def selenium_grid_port(self, value: int) -> None:
        """
        The setter for the selenium_grid_port attribute
        """
        message = (
            f"selenium grid url must be an integer, but you provided: {type(value)}"
        )
        enforce_type_of(
            expected=int, value=value, exc=BrowzerConfigValueError, msg=message
        )
        self._selenium_grid_port = value

    @property
    def browser_resolution(self) -> str:
        """
        The getter for the browser_resolution attribute
        """
        return self._browser_resolution

    @browser_resolution.setter
    def browser_resolution(self, value: str) -> None:
        """
        The setter for the browser_resolution attribute
        """
        # TODO -> Better validation on a intXint
        message = (
            f"browser_resolution must be a string, but you provided: {type(value)}"
        )
        enforce_type_of(
            expected=str, value=value, exc=BrowzerConfigValueError, msg=message
        )
        self._selenium_grid_url = value

    @property
    def full_hub_endpoint(self) -> str:
        """
        The getter for the full hub endpoint that nodes are registered to and tests should be launched to.
        """
        # TODO -> Better validation, is it reachable? is it a url?
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
