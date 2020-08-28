from abc import ABC
from abc import abstractmethod
from typing import Type

from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as GeckoWebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from sylenium.configuration.configuration import Configuration


class WebDriverCreator(ABC):

    def __init__(self, config: Configuration):
        self.config = config

    @abstractmethod
    def create_driver(self) -> RemoteWebDriver:
        raise NotImplementedError()


class ChromeDriverCreator(WebDriverCreator):

    def create_driver(self) -> ChromeWebDriver:
        ...


class GeckoDriverCreator(WebDriverCreator):

    def create_driver(self) -> GeckoWebDriver:
        ...


class WebDriverFactory:
    def __init__(self, config: Configuration):
        self.config = config
        self.driver_mapping = {'Chrome': ChromeDriverCreator, 'Firefox': GeckoDriverCreator}

    def create_driver(self) -> RemoteWebDriver:
        """
        Factory method responsible for determining which driver to instantiate at runtime
        based on how sylenium has been configured by the client.
        """
        browser = self.config.browser
        web_driver = self.driver_mapping.get(browser)(self.config).create_driver()
        return web_driver


