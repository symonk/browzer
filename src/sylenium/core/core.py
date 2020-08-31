from __future__ import annotations

import threading
from types import TracebackType
from typing import Optional
from typing import Type

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from sylenium.configuration import Configuration
from sylenium.core.webdriver.driver_factories import WebDriverFactory
from sylenium.mixins.simple_repr_mixin import SimpleReprMixin


class Session(SimpleReprMixin):
    def __init__(self, configuration: Configuration = None):
        """
        Sylenium session; This is the entry point to sylenium in general, a client should create a session
        which in turn manage(s) all the thread local scoped driver instances.
        Sessions are available as context managers and will automatically tear down all of its webdrivers.
        """
        self.config: Configuration = configuration or Configuration()
        self.session_id: int = threading.get_ident()
        self.driver: Optional[RemoteWebDriver] = None
        self.driver_factory: WebDriverFactory = WebDriverFactory(self.config)
        from sylenium.sylenium import register_session

        register_session(self)

    def get_driver(self) -> RemoteWebDriver:
        """
        Fetching a driver at runtime; Highly configurable via the session configuration provided by the user.
        """
        if self.driver:
            return self.driver
        self.driver = self.driver_factory.create_driver()
        return self.driver

    def __enter__(self) -> Session:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ):
        if self.driver:
            self.driver.quit()
            del self.driver
        return False

    def __del__(self):
        # Clean up when not used as a ctx manager
        ...
