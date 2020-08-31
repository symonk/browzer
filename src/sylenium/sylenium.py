import atexit
import threading
from typing import Mapping

from sylenium.core.core import Session

SESSIONS: Mapping[str, Session] = {}


def get_session_information():
    ...


def register_session(session: Session):
    global SESSIONS
    unique_id = threading.get_ident()
    session[unique_id] = session


atexit.register(get_session_information)
