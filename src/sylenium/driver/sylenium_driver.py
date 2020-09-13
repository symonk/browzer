from __future__ import annotations

from types import TracebackType
from typing import Any
from typing import List
from typing import Optional
from typing import Type

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from sylenium import Configuration
from sylenium.element.sylenium_element import SyleniumElement


class SyleniumDriver:
    def __init__(self, delegated_driver: RemoteWebDriver, config: Configuration):
        self.config = config
        self.driver = delegated_driver

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
        self.driver.close()

    def quit(self) -> None:
        """
        Terminates the driver and closes all of its associated windows
        """
        self.driver.quit()

    def get(self, url: str) -> None:
        """
        Loads the url provided in the current browser session
        """
        self.driver.get(url)

    def get_current_url(self) -> Any:
        """
        Retrieve the current url from the current page
        """
        return self.driver.current_url

    def find(self, locatable) -> SyleniumElement:
        return SyleniumElement(self.driver.find_element(*locatable.locate()), locatable)

    def find_all(self, locatable) -> List[SyleniumElement]:
        return [
            SyleniumElement(ele, locatable)
            for ele in self.driver.find_elements(*locatable.locate())
        ]
