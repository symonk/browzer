from typing import Optional

from sylenium.concurrency.driver_thread_local import SyleniumThreadLocal
from sylenium.configuration import Configuration
from sylenium.configuration import get_global_configuration
from sylenium.driver.driver_factory import create_sylenium_driver
from sylenium.driver.sylenium_driver import SyleniumDriver


class DriverManager:
    _drivers = SyleniumThreadLocal()

    def __init__(self) -> None:
        ...

    def get_threaded_driver(
        self, config: Optional[Configuration] = None
    ) -> SyleniumDriver:
        driver: Optional[SyleniumDriver] = self._drivers.driver
        if driver is not None:
            return driver
        else:
            return create_sylenium_driver(config or get_global_configuration())

    def flush_driver_for_thread(self) -> None:
        self._drivers.driver = None
