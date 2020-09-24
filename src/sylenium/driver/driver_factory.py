from abc import ABC
from abc import abstractmethod
from typing import Any
from typing import Dict
from typing import Type

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeWebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as GeckoWebDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver
from webdriver_manager.chrome import ChromeDriverManager

from sylenium.configuration.configuration import Configuration
from sylenium.constants import TRAVIS_ENV
from sylenium.driver.sylenium_driver import SyleniumDriver
from sylenium.exception.exceptions import DriverInstantiationException
from sylenium.helper._filesystem_helper import does_file_exist
from sylenium.helper._os_environ_helper import read_from_environ


class WebDriverCreator(ABC):
    def __init__(self, config: Configuration) -> None:
        self.config = config

    @abstractmethod
    def create_driver(self) -> RemoteWebDriver:
        ...


class ChromeDriverCreator(WebDriverCreator):
    def __init__(self, config: Configuration) -> None:
        super().__init__(config)

    def create_driver(self) -> ChromeWebDriver:
        chrome_options = self.resolve_options()
        driver_executable = self.resolve_binary_path()
        driver = ChromeWebDriver(
            executable_path=driver_executable,
            port=0,
            options=chrome_options,
            service_args=None,
            desired_capabilities=self.config.browser_capabilities,
            service_log_path=self.config.chrome_service_log_path,
            keep_alive=True,
        )
        if self.config.driver_event_firing_wrapper:
            driver = EventFiringWebDriver(
                driver, self.config.driver_event_firing_wrapper()
            )
        return driver

    def resolve_options(self) -> ChromeOptions:
        """
        Handles (gracefully) multiple chrome based options in-line with what the user provided configuration
        has set.
        """
        chrome_options: ChromeOptions = self.config.chrome_options or ChromeOptions()
        is_travis = read_from_environ(key=TRAVIS_ENV, default=False)
        if self.config.headless or is_travis:
            chrome_options.headless = True
        if self.config.maximized:
            if "--maximized" not in chrome_options.arguments:
                chrome_options.add_argument("--start-maximized")
        else:
            if self.config.browser_resolution:
                if "--window-size" not in chrome_options.arguments:
                    width, height = self.config.browser_resolution.split("x")
                    chrome_options.add_argument(f"--window-size={width},{height}")
            if self.config.browser_position:
                if "--window-position" not in chrome_options.arguments:
                    x, y = self.config.browser_position.split("x")
                    chrome_options.add_argument(f"--window-position={x},{y}")
        if self.config.download_directory:
            if "download.default_directory" not in chrome_options.arguments:
                chrome_options.add_experimental_option(
                    "prefs",
                    {"download.default_directory": f"{self.config.download_directory}"},
                )
        return chrome_options

    def resolve_binary_path(self) -> Any:
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
    def __init__(self, config: Configuration) -> None:
        super().__init__(config)

    def create_driver(self) -> GeckoWebDriver:
        raise NotImplementedError


class RemoteDriverCreator(WebDriverCreator):
    def __init__(self, config: Configuration) -> None:
        super().__init__(config)

    def create_driver(self) -> RemoteWebDriver:
        desired_capabilities = self.config.browser_capabilities
        return RemoteWebDriver(
            command_executor=self.config.full_grid_endpoint,
            desired_capabilities=desired_capabilities,
            browser_profile=None,
            proxy=None,
            keep_alive=False,
            file_detector=None,
            options=None,
        )


def create_sylenium_driver(config: Configuration) -> SyleniumDriver:
    """
    Factory method responsible for determining which driver to instantiate at runtime
    based on how sylenium has been configured by the client.
    """
    driver_mapping: Dict[str, Type[WebDriverCreator]] = {
        "chrome": ChromeDriverCreator,
        "firefox": GeckoDriverCreator,
        "remote": RemoteDriverCreator,
    }
    lookup = config.browser if not config.remote else "remote"
    driver_creator_class = driver_mapping.get(lookup)
    if not driver_creator_class:
        raise ValueError(
            f"Unsupported driver instantiation was attempted for: {lookup}"
        )
    return SyleniumDriver(driver_creator_class(config).create_driver(), config)
