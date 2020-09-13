import threading
from threading import Lock
from typing import Dict
from typing import Mapping
from typing import Optional

from sylenium.configuration import Configuration
from sylenium.configuration import get_global_configuration
from sylenium.driver.driver_factory import create_sylenium_driver
from sylenium.driver.sylenium_driver import SyleniumDriver

THREAD_LOCK = Lock()


class DriverManager:
    _drivers: Dict[int, SyleniumDriver] = {}

    def __init__(self) -> None:
        ...

    def get_threaded_driver(self, config: Optional[Configuration]) -> SyleniumDriver:
        with THREAD_LOCK:
            thread = threading.get_ident()
            driver = self._drivers.get(thread)
            if driver is None:
                # No registered driver for this thread. Create one:
                self._drivers[thread] = create_sylenium_driver(
                    config or get_global_configuration()
                )
                return self._drivers[thread]
            # Driver is already in existence, for the asking thread, use it
            return driver

    def get_all_active_drivers(self) -> Mapping[int, SyleniumDriver]:
        return self._drivers

    def terminate_all(self) -> None:
        for driver in self.get_all_active_drivers().values():
            driver.quit()
        self._drivers.clear()
