from __future__ import annotations

import os
from inspect import isclass
from typing import Any
from typing import Dict
from typing import Iterable
from typing import Optional
from typing import Set
from typing import Tuple
from typing import Type
from typing import Union
from urllib.parse import urlparse

from selenium.webdriver.chrome.webdriver import Options as ChromeOptions
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener

from sylenium.constants import SUPPORTED_BROWSERS
from sylenium.constants import SUPPORTED_PAGE_LOADING_STRATEGIES


class Configuration:
    """
    This is the core configuration class for sylenium.
    This is the core instance that is required to create a new session, fully customisable by the client.
    """

    def __init__(
        self,
        browser: str = "chrome",
        headless: bool = True,
        remote: bool = False,
        page_loading_strategy: str = "fast",
        selenium_grid_url: str = "http://localhost",
        selenium_grid_port: int = 4444,
        browser_resolution: Optional[str] = None,
        browser_version: str = "latest",
        browser_position: Optional[str] = None,
        download_directory: Optional[str] = None,
        proxy_enabled: bool = False,
        driver_binary_path: str = "acquire",
        browser_capabilities: Optional[Dict[str, str]] = None,
        chrome_options: Union[Optional[Set[str]], Optional[ChromeOptions]] = None,
        base_url: Optional[str] = None,
        explicit_waiting: float = 30.00,
        polling_interval: float = 01.50,
        page_source_capturing: bool = False,
        page_screenshot_capturing: bool = False,
        stack_trace_capturing: bool = False,
        javascript_clicks: bool = False,
        javascript_sendkeys: bool = False,
        driver_event_firing_wrapper: Optional[Type[AbstractEventListener]] = None,
        default_selector: str = "css",
        chrome_service_log_path: Optional[str] = None,
        maximized: bool = True,
    ):
        self.browser = browser
        self.headless = headless
        self.remote = remote
        self.page_loading_strategy = page_loading_strategy
        self.selenium_grid_url = selenium_grid_url
        self.selenium_grid_port = selenium_grid_port
        self.browser_resolution = browser_resolution
        self.browser_version = browser_version
        self.browser_position = browser_position
        self.download_directory = download_directory
        self.proxy_enabled = proxy_enabled
        self.driver_binary_path = driver_binary_path
        self.chrome_options = chrome_options
        self.browser_capabilities = browser_capabilities
        self.base_url = base_url
        self.explicit_waiting = explicit_waiting
        self.polling_interval = polling_interval
        self.page_source_capturing = page_source_capturing
        self.page_screenshot_capturing = page_screenshot_capturing
        self.stack_trace_capturing = stack_trace_capturing
        self.javascript_clicks = javascript_clicks
        self.javascript_sendkeys = javascript_sendkeys
        self.driver_event_firing_wrapper = driver_event_firing_wrapper
        self.default_selector = default_selector
        self.chrome_service_log_path = chrome_service_log_path
        self.maximized = maximized

    @property
    def browser(self) -> str:
        return self._browser

    @browser.setter
    def browser(self, browser: str) -> None:
        self._type_check("browser", browser, (str,))
        browser = browser.lower()
        self._validate_is_in(browser, SUPPORTED_BROWSERS)
        self._browser = browser.lower()

    @property
    def headless(self) -> bool:
        return self._headless

    @headless.setter
    def headless(self, headless: bool) -> None:
        self._type_check("headless", headless, (bool,))
        self._headless = headless

    @property
    def remote(self) -> bool:
        return self._remote

    @remote.setter
    def remote(self, remote: bool) -> None:
        self._type_check("remote", remote, (bool,))
        self._remote = remote

    @property
    def page_loading_strategy(self) -> str:
        return self._page_loading_strategy

    @page_loading_strategy.setter
    def page_loading_strategy(self, page_loading_strategy: str) -> None:
        self._type_check("page_loading_strategy", page_loading_strategy, (str,))
        page_loading_strategy = page_loading_strategy.lower()
        self._validate_is_in(page_loading_strategy, SUPPORTED_PAGE_LOADING_STRATEGIES)
        self._page_loading_strategy = page_loading_strategy

    @property
    def selenium_grid_url(self) -> str:
        return self._selenium_grid_url

    @selenium_grid_url.setter
    def selenium_grid_url(self, selenium_grid_url: str) -> None:
        self._type_check("selenium_grid_url", selenium_grid_url, (str,))
        self._selenium_grid_url = selenium_grid_url

    @property
    def selenium_grid_port(self) -> int:
        return self._selenium_grid_port

    @selenium_grid_port.setter
    def selenium_grid_port(self, selenium_grid_port: int) -> None:
        self._type_check("selenium_grid_port", selenium_grid_port, (int,))
        self._selenium_grid_port = selenium_grid_port

    @property
    def browser_resolution(self) -> Optional[str]:
        return self._browser_resolution

    @browser_resolution.setter
    def browser_resolution(self, browser_resolution: str) -> None:
        if browser_resolution is not None:
            self._type_check("browser_resolution", browser_resolution, (str,))
            self._validate_contains_x(browser_resolution)
        self._browser_resolution = browser_resolution

    @property
    def browser_version(self) -> str:
        return self._browser_version

    @browser_version.setter
    def browser_version(self, browser_version: str) -> None:
        self._type_check("browser_version", browser_version, (str,))
        self._browser_version = browser_version

    @property
    def browser_position(self) -> Optional[str]:
        return self._browser_position

    @browser_position.setter
    def browser_position(self, browser_position: str) -> None:
        if browser_position is not None:
            self._type_check("browser_position", browser_position, (str,))
            self._validate_contains_x(browser_position)
        self._browser_position = browser_position

    @property
    def download_directory(self) -> Optional[str]:
        return self._download_directory

    @download_directory.setter
    def download_directory(self, download_directory: Optional[str]) -> None:
        if download_directory is not None:
            self._type_check("download_directory", download_directory, (str,))
            self.is_valid_directory(download_directory)
        self._download_directory = download_directory

    @property
    def proxy_enabled(self) -> bool:
        return self._proxy_enabled

    @proxy_enabled.setter
    def proxy_enabled(self, proxy_enabled: bool) -> None:
        self._type_check("proxy_enabled", proxy_enabled, (bool,))
        self._proxy_enabled = proxy_enabled

    @property
    def driver_binary_path(self) -> str:
        return self._driver_binary_path

    @driver_binary_path.setter
    def driver_binary_path(self, driver_binary_path: str) -> None:
        self._type_check("driver_binary_path", driver_binary_path, (str,))
        self._driver_binary_path = driver_binary_path

    @property
    def chrome_options(self) -> ChromeOptions:
        return self._chrome_options

    @chrome_options.setter
    def chrome_options(self, chrome_options: Set[str]) -> None:
        if isinstance(chrome_options, ChromeOptions) or chrome_options is None:
            self._chrome_options = chrome_options
            return
        self._type_check("chrome_options", chrome_options, (set, ChromeOptions))
        options = ChromeOptions()
        for option in chrome_options:
            options.add_argument(option)
        self._chrome_options = options

    @property
    def browser_capabilities(self) -> Optional[Dict[str, str]]:
        return self._browser_capabilities

    @browser_capabilities.setter
    def browser_capabilities(
        self, browser_capabilities: Optional[Dict[str, str]]
    ) -> None:
        if browser_capabilities is not None:
            self._type_check("browser_capabilities", browser_capabilities, (dict,))
        self._browser_capabilities = browser_capabilities

    @property
    def chrome_service_log_path(self) -> str:
        return self._chrome_service_log_path

    @chrome_service_log_path.setter
    def chrome_service_log_path(self, chrome_service_log_path: Optional[str]) -> None:
        if chrome_service_log_path:
            self._type_check("chrome_service_log_path", chrome_service_log_path, (str,))
        self._chrome_service_log_path = chrome_service_log_path

    @property
    def maximized(self) -> bool:
        return self._maximized

    @maximized.setter
    def maximized(self, maximized: bool) -> None:
        self._type_check("maximized", maximized, (bool,))
        self._maximized = maximized

    @property
    def driver_event_firing_wrapper(self) -> Optional[Type[AbstractEventListener]]:
        return self._driver_event_firing_wrapper

    @driver_event_firing_wrapper.setter
    def driver_event_firing_wrapper(
        self, driver_event_firing_wrapper: Optional[Type[AbstractEventListener]]
    ) -> None:
        if driver_event_firing_wrapper:
            if not isclass(driver_event_firing_wrapper):
                raise TypeError(
                    "driver_event_firing_wrapper= should be of type <class>"
                )
            self._type_check(
                "driver_event_firing_wrapper",
                driver_event_firing_wrapper,
                (AbstractEventListener,),
                True,
            )
        self._driver_event_firing_wrapper = driver_event_firing_wrapper

    @property
    def base_url(self) -> Optional[str]:
        return self._base_url

    @base_url.setter
    def base_url(self, base_url: Optional[str]) -> None:
        if base_url is not None:
            self._type_check("base_url", base_url, (str,))
            self._validate_is_url(base_url)
        self._base_url = base_url

    @property
    def explicit_waiting(self) -> float:
        return self._explicit_waiting

    @explicit_waiting.setter
    def explicit_waiting(self, explicit_waiting: Union[float, int]) -> None:
        if isinstance(explicit_waiting, int):
            explicit_waiting = float(explicit_waiting)
        self._type_check("explicit_waiting", explicit_waiting, (float,))
        self._explicit_waiting = explicit_waiting

    @property
    def polling_interval(self) -> float:
        return self._polling_interval

    @polling_interval.setter
    def polling_interval(self, polling_interval: float) -> None:
        if isinstance(polling_interval, int):
            polling_interval = float(polling_interval)
        self._type_check("polling_interval", polling_interval, (float,))
        self._polling_interval = polling_interval

    @property
    def page_source_capturing(self) -> bool:
        return self._page_source_capturing

    @page_source_capturing.setter
    def page_source_capturing(self, page_source_capturing: bool) -> None:
        self._type_check("page_source_capturing", page_source_capturing, (bool,))
        self._page_source_capturing = page_source_capturing

    @property
    def page_screenshot_capturing(self) -> bool:
        return self._page_screenshot_capturing

    @page_screenshot_capturing.setter
    def page_screenshot_capturing(self, page_screenshot_capturing: bool) -> None:
        self._type_check(
            "page_screenshot_capturing", page_screenshot_capturing, (bool,)
        )
        self._page_screenshot_capturing = page_screenshot_capturing

    @property
    def stack_trace_capturing(self) -> bool:
        return self._stack_trace_capturing

    @stack_trace_capturing.setter
    def stack_trace_capturing(self, stack_trace_capturing: bool) -> None:
        self._type_check("stack_trace_capturing", stack_trace_capturing, (bool,))
        self._stack_trace_capturing = stack_trace_capturing

    @property
    def default_selector(self) -> str:
        return self._default_selector

    @default_selector.setter
    def default_selector(self, default_selector: str) -> None:
        self._type_check("default_selector", default_selector, (str,))
        self._default_selector = default_selector

    @property
    def javascript_clicks(self) -> bool:
        return self._javascript_clicks

    @javascript_clicks.setter
    def javascript_clicks(self, javascript_clicks: bool) -> None:
        self._type_check("javascript_clicks", javascript_clicks, (bool,))
        self._javascript_clicks = javascript_clicks

    @property
    def javascript_sendkeys(self) -> bool:
        return self._javascript_sendkeys

    @javascript_sendkeys.setter
    def javascript_sendkeys(self, javascript_sendkeys: bool) -> None:
        self._type_check("javascript_sendkeys", javascript_sendkeys, (bool,))
        self._javascript_sendkeys = javascript_sendkeys

    # non attr functions -----------------------------------------------------------------------------

    @property
    def selenium_grid(self) -> str:
        """
        Retrieve the full hub endpoint to points remote browsers at for running tests in the cloud
        """
        return f"{self.selenium_grid_url}:{self.selenium_grid_port}/wd/hub"

    @staticmethod
    def _type_check(
        attr: str, value: Any, expected_type: Tuple, expected_subclass: bool = False
    ) -> None:
        """
        Validate types passed into the config.
        """
        function = isinstance if not expected_subclass else issubclass
        if not function(value, expected_type):
            raise TypeError(
                f"{attr}= should be of type: {' '.join(str(t) for t in expected_type)}"
            )

    @staticmethod
    def _validate_is_in(data: str, supported: Iterable[str]) -> None:
        """
        Validate a piece of data is in a particular iterable
        """
        if data not in supported:
            raise ValueError(
                f"value: {data} was not in the supported values: {supported}"
            )

    @staticmethod
    def _validate_contains_x(data: str) -> None:
        """
        For resolution or position based attrs, validate 'x' is in the value
        This is because 'x' is required to split for deciphering things like width vs height
        """
        if "x" not in data:
            raise ValueError(
                f"value: {data} was resolution or position based and did not include 'x'"
            )

    @staticmethod
    def _validate_is_url(data: str) -> None:
        result = urlparse(data)
        if not result.netloc or not result.scheme:
            raise ValueError(f"url: {data} is not considered a valid url")

    @staticmethod
    def is_valid_directory(path: str) -> None:
        if not os.path.isdir(path):
            raise FileExistsError(f"Directory: {path} was not found on the file system")
