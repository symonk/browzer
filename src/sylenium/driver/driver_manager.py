import threading
from threading import Lock
from typing import Dict
from typing import Mapping
from typing import Optional

from sylenium.configuration import Configuration
from sylenium.configuration import get_global_configuration

from .driver_factory import create_sylenium_driver
from .sylenium_driver import SyleniumDriver

THREAD_LOCK = Lock()
_DRIVERS: Dict[int, SyleniumDriver] = {}


def get_threaded_driver(config: Optional[Configuration]) -> SyleniumDriver:
    with THREAD_LOCK:
        thread = threading.get_ident()
        driver = _DRIVERS.get(thread)
        if driver is None:
            # No registered driver for this thread. Create one:
            _DRIVERS[thread] = create_sylenium_driver(
                config or get_global_configuration()
            )
            return _DRIVERS[thread]
        # Driver is already in existence, for the asking thread, use it
        return driver


def get_all_active_drivers() -> Mapping[int, SyleniumDriver]:
    return _DRIVERS


def terminate_all() -> None:
    for driver in get_all_active_drivers().values():
        driver.quit()
    _DRIVERS.clear()
