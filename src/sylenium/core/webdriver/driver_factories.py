from abc import ABC
from abc import abstractmethod

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as GeckoWebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from webdriver_manager.chrome import ChromeDriverManager

from sylenium.configuration.configuration import Configuration


class WebDriverCreator(ABC):
    def __init__(self, config: Configuration):
        self.config = config

    @abstractmethod
    def create_driver(self) -> RemoteWebDriver:
        raise NotImplementedError()


class ChromeDriverCreator(WebDriverCreator):
    def create_driver(self) -> ChromeWebDriver:
        travis_opts = ChromeOptions()
        travis_opts.add_argument("--headless")
        travis_opts.add_argument("--no-sandbox")
        travis_opts.add_argument("--disable-gpu")
        return ChromeWebDriver(
            executable_path=ChromeDriverManager().install(), options=travis_opts
        )


class GeckoDriverCreator(WebDriverCreator):
    def create_driver(self) -> GeckoWebDriver:
        ...


class WebDriverFactory:
    def __init__(self, config: Configuration):
        self.config = config
        self.driver_mapping = {
            "Chrome": ChromeDriverCreator,
            "Firefox": GeckoDriverCreator,
        }

    def create_driver(self) -> RemoteWebDriver:
        """
        Factory method responsible for determining which driver to instantiate at runtime
        based on how sylenium has been configured by the client.
        """
        browser = self.config.browser
        web_driver = self.driver_mapping.get(browser.title())(
            self.config
        ).create_driver()
        return web_driver
