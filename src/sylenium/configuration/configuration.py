from __future__ import annotations

import os
from typing import Any
from typing import Iterable
from typing import Optional
from typing import Type

from sylenium.constants import SUPPORTED_BROWSERS
from sylenium.constants import SUPPORTED_PAGE_LOADING_STRATEGIES
from sylenium.mixins import SimpleEQMixin
from sylenium.mixins import SimpleReprMixin


class Configuration(SimpleReprMixin, SimpleEQMixin):
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
        browser_position: Optional[str] = None,
        browser_version: str = "latest",
        download_directory: Optional[str] = None,
        proxy_enabled: bool = False,
        driver_binary_path: str = "acquire",
    ):
        self.browser = browser
        self.headless = headless
        self.remote = remote
        self.page_loading_strategy = page_loading_strategy
        self.selenium_grid_url = selenium_grid_url
        self.selenium_grid_port = selenium_grid_port
        self.browser_resolution = browser_resolution
        self.browser_position = browser_position
        self.browser_version = browser_version
        self.download_directory = download_directory
        self.proxy_enabled = proxy_enabled
        self.driver_binary_path = driver_binary_path

    @property
    def browser(self) -> str:
        return self._browser

    @browser.setter
    def browser(self, browser: str) -> None:
        self._validate_types("browser", browser, str)
        browser = browser.lower()
        self._validate_is_in(browser, SUPPORTED_BROWSERS)
        self._browser = browser.lower()

    @property
    def headless(self) -> bool:
        return self._headless

    @headless.setter
    def headless(self, headless: bool) -> None:
        self._validate_types("headless", headless, bool)
        self._headless = headless

    @property
    def remote(self) -> bool:
        return self._remote

    @remote.setter
    def remote(self, remote: bool) -> None:
        self._validate_types("remote", remote, bool)
        self._remote = remote

    @property
    def page_loading_strategy(self) -> str:
        return self._page_loading_strategy

    @page_loading_strategy.setter
    def page_loading_strategy(self, page_loading_strategy: str) -> None:
        self._validate_types("page_loading_strategy", page_loading_strategy, str)
        page_loading_strategy = page_loading_strategy.lower()
        self._validate_is_in(page_loading_strategy, SUPPORTED_PAGE_LOADING_STRATEGIES)
        self._page_loading_strategy = page_loading_strategy

    @property
    def selenium_grid_url(self) -> str:
        return self._selenium_grid_url

    @selenium_grid_url.setter
    def selenium_grid_url(self, selenium_grid_url: str) -> None:
        self._validate_types("selenium_grid_url", selenium_grid_url, str)
        self._selenium_grid_url = selenium_grid_url

    @property
    def selenium_grid_port(self) -> int:
        return self._selenium_grid_port

    @selenium_grid_port.setter
    def selenium_grid_port(self, selenium_grid_port: int) -> None:
        self._validate_types("selenium_grid_port", selenium_grid_port, int)
        self._selenium_grid_port = selenium_grid_port

    @property
    def browser_resolution(self) -> Optional[str]:
        return self._browser_resolution

    @browser_resolution.setter
    def browser_resolution(self, browser_resolution: str) -> None:
        if browser_resolution:
            self._validate_types("browser_resolution", browser_resolution, str)
            self._validate_contains_x(browser_resolution)
        self._browser_resolution = browser_resolution

    @property
    def browser_position(self) -> Optional[str]:
        return self._browser_position

    @browser_position.setter
    def browser_position(self, browser_position: str) -> None:
        if browser_position:
            self._validate_types("browser_position", browser_position, str)
            self._validate_contains_x(browser_position)
        self._browser_position = browser_position

    @property
    def browser_version(self) -> str:
        return self._browser_version

    @browser_version.setter
    def browser_version(self, browser_version: str) -> None:
        self._validate_types("browser_version", browser_version, str)
        self._browser_version = browser_version

    @property
    def download_directory(self) -> Optional[str]:
        return self._download_directory

    @download_directory.setter
    def download_directory(self, download_directory: Optional[str]) -> None:
        if download_directory:
            self._validate_types("download_directory", download_directory, str)
            self.is_valid_directory(download_directory)
        self._download_directory = download_directory

    @property
    def proxy_enabled(self) -> bool:
        return self._proxy_enabled

    @proxy_enabled.setter
    def proxy_enabled(self, proxy_enabled: bool) -> None:
        self._validate_types("proxy_enabled", proxy_enabled, bool)
        self._proxy_enabled = proxy_enabled

    @property
    def driver_binary_path(self) -> str:
        return self._driver_binary_path

    @driver_binary_path.setter
    def driver_binary_path(self, driver_binary_path: str) -> None:
        self._validate_types("driver_binary_path", driver_binary_path, str)
        self._driver_binary_path = driver_binary_path

    # non attr functions

    @property
    def selenium_grid(self) -> str:
        """
        Retrieve the full hub endpoint to points remote browsers at for running tests in the cloud
        """
        return f"{self.selenium_grid_url}:{self.selenium_grid_port}/wd/hub"

    @staticmethod
    def _validate_types(attr: str, value: Any, expected_type: Type) -> None:
        """
        Validate types passed into the config.
        """
        if not isinstance(value, expected_type):
            raise ValueError(f"{attr}= should be of type: {str(expected_type)}")

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
    def is_valid_directory(path: str) -> None:
        if not os.path.isdir(path):
            raise FileExistsError(f"Directory: {path} was not found on the file system")
