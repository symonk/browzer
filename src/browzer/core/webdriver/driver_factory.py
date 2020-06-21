from __future__ import annotations

import threading
from abc import ABC
from abc import abstractmethod
from typing import Optional
from typing import Type
from typing import Union

from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from browzer import BrowzerConfiguration
from browzer.configuration.configuration import ConfigHelper
from browzer.constants.strings import CHROME
from browzer.constants.strings import FIREFOX
from browzer.core.webelement.browzer_element import BrowzerElement


class ICreator(ABC):
    """
    Interface for browser creation, each subclass guarantees it can create a browser of its type.
    """

    @abstractmethod
    def create(self) -> RemoteWebDriver:
        pass


class ChromeCreator(ICreator):
    def __init__(self, config: BrowzerConfiguration):
        self.config = config
        self.config_helper = ConfigHelper(self.config)

    def create(self) -> RemoteWebDriver:
        """
        Chrome driver instantiation
        :return: Return the instantiated version of the chrome driver (Remote or local)
        """
        chrome_opts = ChromeOptions()
        cfg_chrome_opts = self.config.CHROME_OPTIONS
        if cfg_chrome_opts:
            for option in cfg_chrome_opts:
                chrome_opts.add_argument(option)
        capabilities = self.config.BROWSER_CAPABILITIES
        binary = self.config_helper.resolve_binary_path()
        driver = ChromeDriver(
            executable_path=binary,
            options=chrome_opts,
            desired_capabilities=capabilities,
        )
        driver._web_element_cls = BrowzerElement
        driver = self._load_base_url_if_specified(driver)
        driver = self._wrap_driver_if_necessary(driver)
        return driver

    def _load_base_url_if_specified(self, driver: RemoteWebDriver) -> RemoteWebDriver:
        """
        Checks config BASE_URL for a loadable url and loads it prior to returning the driver
        :param driver: the driver instances; recently instantiated
        :return: the creator for fluency
        """
        url = self.config.BASE_URL
        if url:
            driver.get(url)
        return driver

    def _wrap_driver_if_necessary(
        self, driver: RemoteWebDriver
    ) -> Union[RemoteWebDriver, EventFiringWebDriver]:
        """
         Given the --driver-listener CLI arg, wrap the driver into an EventFiringWebDriver using the class passed
         by the user; note their module should be discoverable by python and if it is not, we cannot possibly get here.
         parser will raise a ValueError alerting them about the issue
         :param driver: the webdriver instance to 'potentially' wrap
         """
        event_firing = self.config.DRIVER_LISTENER
        return EventFiringWebDriver(driver, event_firing()) if event_firing else driver


class FireFoxCreator(ICreator):
    def __init__(self, config):
        self.config = config

    def create(self) -> RemoteWebDriver:
        pass


class BrowzerDriverFactory:
    """
    The Browzer factory is responsible for tracking instantiating browsers.
    If an interaction occurs without a driver, such interaction will create and register a new browser.
    These browsers are thread local scoped to help with parallel testing on test frameworks that can support it.
    """

    def __init__(self, config: Type[BrowzerConfiguration]):
        self.config = config
        self.supported = {CHROME: ChromeCreator, FIREFOX: FireFoxCreator}
        self.drivers = {}

    def get_driver(self) -> RemoteWebDriver:
        """
        Retrieve a browser instance, returns the thread bound driver if one exists, else creates one.
        :return: A subclass of RemoteWebDriver depending on the configuration overrides.
        """
        bound_driver = self._check_and_fetch()
        if not bound_driver:
            return self._register_new()
        return bound_driver

    def _register_new(self) -> RemoteWebDriver:
        """
        Registers a new driver object into the active drivers space and returns it to the caller.
        :return: An instance of a RemoteWebDriver subclass.
        """
        new_driver = self.supported.get(self.config.BROWSER)(self.config).create()
        self.drivers[threading.get_ident()] = new_driver
        return new_driver

    def _check_and_fetch(self) -> Optional[RemoteWebDriver]:
        """
        Simple lookup if a driver has been already registered based on the thread id.
        :return: An instance of a RemoteWebDriver subclass, or None if one has never been created (yet).
        """
        if threading.get_ident() in self.drivers:
            return self.drivers[threading.get_ident()]

    def terminate_driver(self) -> None:
        """
        Looks up a given driver from the dictionary and terminate(s) it if so.
        Note: Browzer does not support persistent browsers across tests at present.
        :return:
        """
        driver = self._check_and_fetch()
        if driver:
            driver.quit()
            del self.drivers[threading.get_ident()]
