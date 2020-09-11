from ._version import __version__
from .configuration import Configuration
from .driver.sylenium_driver import SyleniumDriver
from .sylenium import get_driver

__all__ = ["__version__", "Configuration", "SyleniumDriver", "get_driver"]
