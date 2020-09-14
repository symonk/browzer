from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Optional

from selenium.webdriver.remote.webelement import WebElement as RemoteWebElement

from sylenium.command import command_invoker
from sylenium.interface.locatable import Locatable

if TYPE_CHECKING:
    from sylenium import SyleniumDriver


class SyleniumElement:
    def __init__(self, locatable: Locatable, driver: SyleniumDriver):
        self._wrapped_element: Optional[RemoteWebElement] = None
        self.locatable = locatable
        self.driver = driver

    @property
    def wrapped_element(self) -> RemoteWebElement:
        """
        Upon access, re-acquire the RemoteWebElement.  This is useful to avoid StaleElements and provides
        a high level of stability.
        """
        self._wrapped_element = self.driver.wrapped_driver.find_element(
            *self.locatable.locate()
        )
        return self._wrapped_element

    def should_be(self) -> SyleniumElement:
        ...

    def should_have(self) -> SyleniumElement:
        ...

    def should_not_be(self) -> SyleniumElement:
        ...

    def should_not_have(self) -> SyleniumElement:
        ...

    def wait_until(self) -> SyleniumElement:
        ...

    def wait_while(self) -> SyleniumElement:
        ...

    def click(self) -> None:
        command_invoker.execute("click", self)
