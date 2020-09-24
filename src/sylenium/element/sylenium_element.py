from __future__ import annotations

from typing import TYPE_CHECKING

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement as RemoteWebElement

from sylenium.element.locatable import Locatable

if TYPE_CHECKING:
    from sylenium import SyleniumDriver


class SyleniumElement:
    def __init__(
        self,
        locatable: Locatable,
        wrapped_element: RemoteWebElement,
        driver: SyleniumDriver,
    ):
        self._wrapped_element = wrapped_element
        self.locator = locatable
        self.driver = driver

    @property
    def wrapped_element(self) -> RemoteWebElement:
        return self._wrapped_element

    def _refind(self) -> RemoteWebElement:
        self._wrapped_element = self.driver.find(self.locator).wrapped_element
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
        self._refind()
        try:
            self.wrapped_element.click()
        except WebDriverException:
            ...

    def set_text(self, text: str) -> SyleniumElement:
        self._refind()
        self.wrapped_element.send_keys(text)
        return self

    def clear(self) -> SyleniumElement:
        self._refind()
        self.wrapped_element.clear()
        return self

    def press_enter(self) -> SyleniumElement:
        self._refind()
        self.set_text(Keys.ENTER)
        return self
