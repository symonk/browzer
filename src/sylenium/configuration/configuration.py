from __future__ import annotations

from typing import Dict
from typing import List
from typing import Optional

from sylenium.exceptions.exceptions import syleniumConfigValueError
from sylenium.helpers.object_validator import enforce_type_of
from sylenium.helpers.object_validator import enforce_value_is_in
from sylenium.mixins.simple_eq_mixin import SimpleEQMixing
from sylenium.mixins.simple_repr_mixin import SimpleReprMixin


class Configuration(SimpleReprMixin, SimpleEQMixing):
    """
    This is the core configuration class for sylenium.
    This should be configured prior to instantiating any drivers; it assumes sensible defaults.
    :param browser: The browser type to instantiate downstream. choices are: (chrome|firefox)
    :param headless: If the browsers instantiated will run headlessly. choices are: (True|False)
    :param remote: If the browser will be running using a seleniuim grid, likely in the cloud. choices are: (True|False)
    """

    def __init__(
        self,
        browser: str = "chrome",
        headless: bool = False,
        remote: bool = False,
        page_loading_strategy: str = "fast",
        selenium_grid_url: str = "http://127.0.0.1",
        selenium_grid_port: int = 4444,
        browser_resolution: str = "1280x1024",
        browser_version: str = "latest",
        browser_position: Optional[str] = None,
        driver_binary_path: Optional[str] = None,
        browser_capabilities: Dict[str, str] = None,
        chrome_options: Optional[List[str]] = None,
        base_url: Optional[str] = None,
        explicit_waiting: float = 30.00,
        polling_interval: float = 00.25,
        page_source_capturing: bool = False,
        page_screenshot_capturing: bool = False,
        stack_trace_capturing: bool = False,
        javascript_clicks: bool = False,
        javascript_sendkeys: bool = False,
        driver_listener_module_class_path: str = None,
        default_selector: str = "css",
    ):
        self._browser: str = browser
        self._headless: bool = headless
        self._remote: bool = remote
        self._selenium_grid_url: str = selenium_grid_url
        self._selenium_grid_port: int = selenium_grid_port
        self._browser_resolution: str = browser_resolution
        self._browser_version: str = browser_version
        self._browser_position: Optional[str] = browser_position
        self._driver_binary_path: str = driver_binary_path
        self._browser_capabilities: Dict[str, str] = browser_capabilities
        self._chrome_options: List[str] = chrome_options
        self._base_url: str = base_url
        self._explicit_waiting: float = explicit_waiting
        self._polling_interval: float = polling_interval
        self._page_source_capturing: bool = page_source_capturing
        self._page_screenshot_capturing: bool = page_screenshot_capturing
        self._stack_trace_capturing: bool = stack_trace_capturing
        self._javascript_clicks: bool = javascript_clicks
        self._javascript_sendkeys: bool = javascript_sendkeys
        self._driver_listener_module_class_path: str = driver_listener_module_class_path
        self._page_loading_strategy: str = page_loading_strategy
        self._default_selector: str = default_selector

    @property
    def browser(self) -> str:
        """
        Getter for the browser attribute
        :return: The browser attribute (string)
        """
        return self._browser

    @browser.setter
    def browser(self, browser: str) -> None:
        """
        Setter for the browser attribute.
        :param value: The browser to configure
        """
        supported = {"chrome", "firefox"}
        enforce_value_is_in(
            iterable=supported, value=browser.lower(), exc=syleniumConfigValueError
        )
        self._browser = browser.lower()

    @property
    def headless(self) -> bool:
        """
        The getter for the headless attribute
        :return: The headless attribute (boolean)
        """
        return self._headless

    @headless.setter
    def headless(self, headless: bool) -> None:
        """
        The setter for the headless attribute
        """
        message = f"Only boolean types are supported for headless, you provided: {type(headless)}"
        enforce_type_of(
            expected=bool, value=headless, exc=syleniumConfigValueError, msg=message
        )
        self._headless = headless

    @property
    def remote(self) -> bool:
        """
        The getter for the remote attribute
        :return: The remote attribute (boolean)
        """
        return self._remote

    @remote.setter
    def remote(self, remote: bool) -> None:
        """
        The setter for the remote attribute
        """
        message = (
            f"Only boolean types are supported for remote, you provided: {type(remote)}"
        )
        enforce_type_of(
            expected=bool, value=remote, exc=syleniumConfigValueError, msg=message
        )
        self._remote = remote

    @property
    def selenium_grid_url(self) -> str:
        """
        The getter for the selenium grid url attribute
        :return: The selenium grid hub url (str)
        """
        return self._selenium_grid_url

    @selenium_grid_url.setter
    def selenium_grid_url(self, selenium_grid_url: str) -> None:
        """
        The setter for the selenium_grid_url attribute
        """
        # TODO -> Better validation, do not end with /wd/hub we append it etc
        message = f"selenium grid url must be a string, but you provided: {type(selenium_grid_url)}"
        enforce_type_of(
            expected=str,
            value=selenium_grid_url,
            exc=syleniumConfigValueError,
            msg=message,
        )
        self._selenium_grid_url = selenium_grid_url

    @property
    def selenium_grid_port(self) -> int:
        """
        The getter for the selenium grid port attribute
        :return: The selenium grid hub port (int)
        """
        return self._selenium_grid_port

    @selenium_grid_port.setter
    def selenium_grid_port(self, selenium_grid_port: int) -> None:
        """
        The setter for the selenium_grid_port attribute
        """
        message = f"selenium grid url must be an integer, but you provided: {type(selenium_grid_port)}"
        enforce_type_of(
            expected=int,
            value=selenium_grid_port,
            exc=syleniumConfigValueError,
            msg=message,
        )
        self._selenium_grid_port = selenium_grid_port

    @property
    def browser_resolution(self) -> str:
        """
        The getter for the browser_resolution attribute
        """
        return self._browser_resolution

    @browser_resolution.setter
    def browser_resolution(self, browser_resolution: str) -> None:
        """
        The setter for the browser_resolution attribute
        """
        # TODO -> Better validation on a intXint
        message = f"browser_resolution must be a string, but you provided: {type(browser_resolution)}"
        enforce_type_of(
            expected=str,
            value=browser_resolution,
            exc=syleniumConfigValueError,
            msg=message,
        )
        self._selenium_grid_url = browser_resolution

    @property
    def browser_version(self) -> str:
        """
        Getter for the browser_version attribute
        """
        return self._browser_version

    @browser_version.setter
    def browser_version(self, version: str) -> None:
        """
        Setter for the browser_version attribute
        """
        message = f"browser_version must be a string, but you provided: {type(version)}"
        enforce_type_of(
            expected=str, value=version, exc=syleniumConfigValueError, msg=message
        )
        self._browser_version = version


    @property
    def browser_position(self) -> str:
        """
        Getter for the browser_position attribute
        """
        return self._browser_version

    @browser_version.setter
    def browser_position(self, browser_position: str) -> None:
        """
        Setter for the browser_position attribute
        """
        self._browser_version = browser_position

    @property
    def driver_binary_path(self) -> str:
        """
        Getter for the driver_binary_path
        """
        return self._driver_binary_path

    @driver_binary_path.setter
    def driver_binary_path(self, binary_path: str) -> None:
        """
        Setter for the driver_binary_path
        This is used to determine which version of the binaries to automatically acquire.
        If this value is 'latest', we will automatically acquire the latest version for the given binary.
        """
        self._driver_binary_path = binary_path

    @property
    def browser_capabilities(self) -> Dict[str, str]:
        """
        Getter for the browser_capabilities attribute
        """
        return self._browser_capabilities

    @browser_capabilities.setter
    def browser_capabilities(self, capabilities: Dict[str, str]) -> None:
        """
        Setter for the browser_capabilities attribute
        """
        message = f"browser_capabilities must be a dictionary, but you provided: {type(capabilities)}"
        enforce_type_of(
            expected=Dict, value=capabilities, exc=syleniumConfigValueError, msg=message
        )
        self._browser_capabilities = capabilities

    @property
    def chrome_options(self) -> List[str]:
        """
        Getter for the chrome_options attribute
        """
        return self._chrome_options

    @chrome_options.setter
    def chrome_options(self, chrome_options: List[str]) -> None:
        """
        Setter for the chrome_options attribute
        """
        message = (
            f"chrome_options must be a list, but you provided: {type(chrome_options)})"
        )
        enforce_type_of(
            expected=List,
            value=chrome_options,
            exc=syleniumConfigValueError,
            msg=message,
        )
        self._chrome_options = chrome_options

    @property
    def base_url(self) -> str:
        """
        Getter for the base_url attribute
        """
        return self._base_url

    @base_url.setter
    def base_url(self, base_url: str) -> None:
        """
        Setter for the base_url attribute
        """
        self._base_url = base_url

    @property
    def explicit_waiting(self) -> float:
        """
        Getter for the explicit_waiting attribute
        """
        return self._explicit_waiting

    @explicit_waiting.setter
    def explicit_waiting(self, explicit_waiting: float) -> None:
        """
        Setter for the explicit_waiting attribute
        """
        self._explicit_waiting = explicit_waiting

    @property
    def polling_interval(self) -> float:
        """
        Getter for the polling_interval attribute
        """
        return self.polling_interval

    @polling_interval.setter
    def polling_interval(self, polling_interval: float) -> None:
        """
        Setter for the polling_interval attribute
        """
        self._polling_interval = polling_interval

    @property
    def page_source_capturing(self) -> bool:
        """
        Getter for the page_source_capturing attribute
        """
        return self._page_source_capturing

    @page_source_capturing.setter
    def page_source_capturing(self, page_source_capturing: bool) -> None:
        """
        Setter for the page_source_capturing attribute
        """
        self._page_source_capturing = page_source_capturing

    @property
    def page_screenshot_capturing(self) -> bool:
        """
        Getter for the page_screenshot_capturing attribute
        """
        return self._page_source_capturing

    @page_screenshot_capturing.setter
    def page_screenshot_capturing(self, page_screenshot_capturing: bool) -> None:
        """
        Setter for the page_screenshot_capturing attribute
        """
        self._page_screenshot_capturing = page_screenshot_capturing

    @property
    def stack_trace_capturing(self) -> bool:
        """
        Getter for the stack_trace_capturing attribute
        """
        return self._stack_trace_capturing

    @stack_trace_capturing.setter
    def stack_trace_capturing(self, stack_trace_capturing: bool) -> None:
        """
        Setter for the stack_trace_capturing attribute
        """
        self._stack_trace_capturing = stack_trace_capturing

    @property
    def javascript_clicks(self) -> bool:
        """
        Getter for the javascript_clicks attribute
        """
        return self._javascript_clicks

    @javascript_clicks.setter
    def javascript_clicks(self, javascript_clicks: bool) -> None:
        """
        Setter for the javascript_clicks attribute
        """
        self._javascript_clicks = javascript_clicks

    @property
    def javascript_sendkeys(self) -> bool:
        """
        Getter for the javascript_sendkeys attribute
        """
        return self._javascript_sendkeys

    @javascript_sendkeys.setter
    def javascript_sendkeys(self, javascript_sendkeys: bool) -> None:
        """
        Setter for the javascript_sendkeys attribute
        """
        self._javascript_sendkeys = javascript_sendkeys

    @property
    def driver_listener_module_class_path(self) -> str:
        """
        Getter for the driver_listener_module_class_path attribute
        """
        return self._driver_listener_module_class_path

    @driver_listener_module_class_path.setter
    def driver_listener_module_class_path(
        self, driver_listener_module_class_path: str
    ) -> None:
        """
        Setter for the driver_listener_module_class_path attribute
        """
        self._driver_listener_module_class_path = driver_listener_module_class_path

    @property
    def default_selector(self) -> str:
        """
        Getter for the default_selector attribute
        """
        return self._default_selector

    @default_selector.setter
    def default_selector(self, default_selector: str) -> None:
        """
        Setter for the default_selector attribute
        """
        self._default_selector = default_selector

    def full_hub_endpoint(self) -> str:
        """
        The getter for the full hub endpoint that nodes are registered to and tests should be launched to.
        """
        # TODO -> Better validation, is it reachable? is it a url?
        return f"{self.selenium_grid_url}:{self.selenium_grid_port}/wd/hub"
