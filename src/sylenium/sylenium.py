import atexit
import threading
from typing import Dict
from typing import List
from typing import Type

from sylenium.core.core import Session
from sylenium.core.elements.locators import SyleniumElement
from sylenium.core.elements.locators import SyleniumLocator
from sylenium.core.pages.pageobjects import PageObject
from sylenium.exceptions.exceptions import SessionException

SESSIONS: Dict[int, Session] = {}


def print_session_information():
    for session in SESSIONS.values():
        print(session)


def register_session(session: Session):
    SESSIONS[session.session_id] = session


def load(url: str, page_class: Type[PageObject]) -> PageObject:
    ...


def find(locator: SyleniumLocator) -> SyleniumElement:
    ...


def find_all(locator: SyleniumLocator) -> List[SyleniumElement]:
    ...


def _fetch_appropriate_driver():
    driver = SESSIONS.get(threading.get_ident())
    if not driver:
        raise SessionException(
            "Please configure a session for this thread before attempting driver or element actions"
        )
    return driver


atexit.register(print_session_information)
