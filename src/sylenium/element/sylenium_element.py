from __future__ import annotations

from selenium.webdriver.remote.webelement import WebElement as RemoteWebElement

from sylenium.interface.locatable import Locatable


class SyleniumElement:
    def __init__(self, delegated_element: RemoteWebElement, locatable: Locatable):
        self.element = delegated_element
        self.locatable = locatable

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
