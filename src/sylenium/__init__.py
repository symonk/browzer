from ._version import __version__
from .concurrency.driver_monitor_thread import DriverMonitorThread
from .configuration import Configuration
from .configuration import configure
from .configuration import get_global_configuration
from .driver import DriverManager
from .driver import SyleniumDriver
from .sylenium import get_driver

__all__ = [
    "__version__",
    "Configuration",
    "SyleniumDriver",
    "configure",
    "get_global_configuration",
    "DriverMonitorThread",
    "DriverManager",
    "get_driver",
]
