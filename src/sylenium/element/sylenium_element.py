from selenium.webdriver.remote.webelement import WebElement as RemoteWebElement

from sylenium.interface.locatable import Locatable


class SyleniumElement:
    def __init__(self, delegated_element: RemoteWebElement, locatable: Locatable):
        self.element = delegated_element
        self.locatable = locatable
