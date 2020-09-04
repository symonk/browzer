from __future__ import annotations

import threading
from types import TracebackType
from typing import Dict
from typing import Optional
from typing import Type

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from sylenium import Configuration
from sylenium.core.webdriver.driver_factories import WebDriverFactory
from sylenium.exceptions import SessionException
from sylenium.mixins import SimpleReprMixin


class SessionManager:
    def __init__(self):
        self.sessions: Dict[int, Session] = {}

    def register(self, session: Session):
        """
        Responsible for registering new sessions.  Sessions should only be registered once
        and are not considered 'reusable' once deactivated.  Currently a single session is coupled to a
        single browser instance and each session has a unique ID.
        """
        if session.unique_id in self.sessions:
            raise SessionException(f"Session: {session} already registered")
        self.sessions[session.unique_id] = session

    def fetch(self):
        fetched_session = self.sessions.get(threading.get_ident())
        if fetched_session is None:
            raise SessionException(
                f"No such session registered for the thread: {threading.get_ident()}"
            )
        return fetched_session

    def deactivate(self) -> None:
        try:
            del self.sessions[threading.get_ident()]
        except KeyError:
            ...


session_manager = SessionManager()


class Session(SimpleReprMixin):
    def __init__(self, configuration: Configuration = None):
        """
        Sylenium session; This is the entry point to sylenium in general, a client should create a session
        which in turn manage(s) all the thread local scoped driver instances.
        Sessions are available as context managers and will automatically tear down all of its webdrivers.
        """
        self.config: Configuration = configuration or Configuration()
        self.unique_id: int = threading.get_ident()
        self._driver: Optional[RemoteWebDriver] = None
        self.driver_factory: WebDriverFactory = WebDriverFactory(self.config)
        session_manager.register(self)

    def get_driver(self) -> RemoteWebDriver:
        """
        Fetching a driver at runtime; Highly configurable via the session configuration provided by the user.
        """
        if self._driver:
            return self._driver
        self._driver = self.driver_factory.create_driver()
        return self._driver

    def __enter__(self) -> Session:
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ):
        if self._driver:
            self._driver.quit()
            del self._driver
        return False

    def __del__(self):
        # Clean up when not used as a ctx manager
        session_manager.deactivate()
