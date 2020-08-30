from __future__ import annotations

import uuid
from typing import List

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from sylenium.configuration import Configuration
from sylenium.core.webdriver.driver_factories import WebDriverFactory


class Session:
    def __init__(self, configuration: Configuration = None):
        """
        Sylenium session; This is the entry point to sylenium in general, a client should create a session
        which in turn manage(s) all the thread local scoped driver instances.
        Sessions are available as context managers and will automatically tear down all of its webdrivers.
        """
        self.config = configuration or Configuration()
        self.session_id = uuid.uuid4()
        self.drivers: List[RemoteWebDriver] = []
        self.driver_factory = WebDriverFactory(self.config)

    def get_driver(self) -> RemoteWebDriver:
        """
        Fetching a driver at runtime; Highly configurable via the session configuration provided by the user.
        """
        driver = self.driver_factory.create_driver()
        self.drivers.append(driver)
        return driver

    def __enter__(self) -> Session:
        return self

    def __exit__(self, type, value, traceback):
        for driver in self.drivers:
            driver.quit()
        return False

    def __del__(self):
        # Clean up when not used as a ctx manager
        ...
