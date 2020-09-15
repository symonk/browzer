from __future__ import annotations

from types import TracebackType
from typing import Any
from typing import Optional
from typing import Type

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from sylenium.configuration.configuration import Configuration
from sylenium.element.sylenium_element import SyleniumElement


class SyleniumDriver:
    """
    Serves as a wrapper around an arbitrary RemoteWebDriver subclass.  Similar to how EventFiringWebDriver wraps
    RemoteWebDriver when used.
    """

    def __init__(self, delegated_driver: RemoteWebDriver, config: Configuration):
        self.config: Configuration = config
        self.wrapped_driver: RemoteWebDriver = delegated_driver

    def _wrap_value(self, *args) -> Any:
        """
        Unsure of an implementation for now...
        """
        ...

    def __enter__(self) -> SyleniumDriver:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        self.quit()

    def close(self) -> None:
        """
        Closes the current driver window
        Note: Not to be confused with the entire driver instance, .quit() should be used for that.
        """
        self.wrapped_driver.close()

    def quit(self) -> None:
        """
        Terminates the driver and closes all of its associated windows
        """
        self.wrapped_driver.quit()

    def get(self, url: str) -> None:
        """
        Loads the url provided in the current browser session
        """
        self.wrapped_driver.get(url)

    def get_current_url(self) -> Any:
        """
        Retrieve the current url from the current page
        """
        return self.wrapped_driver.current_url

    def find(self, locatable) -> SyleniumElement:
        return SyleniumElement(locatable, self)
