from __future__ import annotations

from typing import Any
from typing import Type

from sylenium.constants import SUPPORTED_BROWSERS
from sylenium.mixins import SimpleEQMixin
from sylenium.mixins import SimpleReprMixin


class Configuration(SimpleReprMixin, SimpleEQMixin):
    """
    This is the core configuration class for sylenium.
    This is the core instance that is required to create a new session, fully customisable by the client.
    """

    def __init__(
        self, browser: str = "chrome", headless: bool = True, remote: bool = False
    ):
        self.browser = browser
        self.headless = headless
        self.remote = remote

    @property
    def browser(self) -> str:
        return self._browser

    @browser.setter
    def browser(self, browser: str) -> None:
        self._validate_types("browser", browser, str)
        browser = browser.lower()
        if browser not in SUPPORTED_BROWSERS:
            raise ValueError(
                f"browser={browser} is not supported, choose either: {SUPPORTED_BROWSERS}"
            )
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

    @staticmethod
    def _validate_types(attr: str, value: Any, expected_type: Type) -> None:
        """
        Validate types passed into the config.
        """
        if not isinstance(value, expected_type):
            raise ValueError(f"{attr}= should be of type: {str(expected_type)}")

    def full_hub_endpoint(self) -> str:
        """
        The getter for the full hub endpoint that nodes are registered to and tests should be launched to.
        """
        return f"{self.selenium_grid_url}:{self.selenium_grid_port}/wd/hub"
