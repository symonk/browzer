from abc import ABC
from abc import abstractmethod

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as GeckoWebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from webdriver_manager.chrome import ChromeDriverManager

from sylenium.configuration.configuration import Configuration
from sylenium.exceptions.exceptions import DriverInstantiationException
from sylenium.helpers.operating_system.filesystem import does_file_exist


class WebDriverCreator(ABC):
    def __init__(self, config: Configuration):
        self.config = config

    @abstractmethod
    def create_driver(self) -> RemoteWebDriver:
        raise NotImplementedError()


class ChromeDriverCreator(WebDriverCreator):
    def create_driver(self) -> ChromeWebDriver:
        chrome_options = self.resolve_options()
        driver_executable = (
            self.config.driver_binary_path or ChromeDriverManager().install()
        )

        return ChromeWebDriver(
            executable_path=driver_executable, options=chrome_options
        )

    def resolve_options(self) -> ChromeOptions:
        """
        Resolves headless and user provided chrome options to ensure they play together gracefully.
        """
        chrome_options = self.config.chrome_options or ChromeOptions()
        if self.config.headless:
            missing = {"--headless", "--no-sandbox", "--no-display"}
            for expected in missing:
                if missing not in chrome_options.arguments:
                    chrome_options.arguments.append(expected)
        return chrome_options

    def resolve_binary_path(self) -> str:
        """
        Resolves the binary driver path, using the following mechanism:
        Priority A) Has the user said to use WDM explicitly
        Priority B) Has the user provided a custom driver_binary_path in their session configuration
        Note: Sylenium does something special with the unique 'acquire' value, it is the mechanism to use the
        auto acquired webdriver binary.
        Note: Such binaries are only applicable when running locally, CI based RemoteWebDriver instances often use
        a node machines binary, e.g a docker setup for hub/nodes in AWS etc.
        """
        binary_path = self.config.driver_binary_path
        if binary_path == "acquire":
            # wdm has been set, lets resolve and acquire the binary based on browser_version
            # version is 'latest' by default, unless a specific version has been specified by the client
            return ChromeDriverManager(version=self.config.browser_version).install()
        if does_file_exist(binary_path):
            # use has provided a binary path to a valid file, we will try and use it
            return binary_path
        raise DriverInstantiationException(
            "Unable to instantiate a driver, use a valid path for driver_binary_path"
            "or use the auto acquiring functionality (provided by default)"
        )


class GeckoDriverCreator(WebDriverCreator):
    def create_driver(self) -> GeckoWebDriver:
        ...


class RemoteDriverCreator(WebDriverCreator):
    def create_driver(self) -> RemoteWebDriver:
        ...


class WebDriverFactory:
    def __init__(self, config: Configuration):
        self.config = config
        self.driver_mapping = {
            "chrome": ChromeDriverCreator,
            "firefox": GeckoDriverCreator,
            "remote": RemoteDriverCreator,
        }

    def create_driver(self) -> RemoteWebDriver:
        """
        Factory method responsible for determining which driver to instantiate at runtime
        based on how sylenium has been configured by the client.
        """
        lookup = self.config.browser if not self.config.remote else "remote"
        driver = self.driver_mapping.get(lookup)(self.config).create_driver()
        return driver
