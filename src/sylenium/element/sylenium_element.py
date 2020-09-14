from __future__ import annotations

from typing import TYPE_CHECKING

from selenium.webdriver.remote.webelement import WebElement as RemoteWebElement

from sylenium.command import command_invoker
from sylenium.interface.locatable import Locatable

if TYPE_CHECKING:
    from sylenium import SyleniumDriver


class SyleniumElement:
    def __init__(
        self,
        delegated_element: RemoteWebElement,
        locatable: Locatable,
        driver: SyleniumDriver,
    ):
        self.wrapped_element = delegated_element
        self.locatable = locatable
        self.driver = driver

    def refind(self) -> SyleniumElement:
        """
        Before calling any actions on the SyleniumElement, it should be refound.  This always happens and is a little
        price to pay for stability and dealing with StaleElements.
        """
        self.wrapped_element = self.driver.find(self.locatable).wrapped_element
        return self

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
