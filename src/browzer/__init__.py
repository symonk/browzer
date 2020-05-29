__version__ = "0.0.0"

from browzer.configuration.BrowzerConfig import load_browzer_config
from browzer.configuration.BrowzerConfig import BrowzerConfiguration  # noqa: F401

browzer_config = load_browzer_config()

__all__ = [browzer_config]
