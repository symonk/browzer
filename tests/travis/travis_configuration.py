from dataclasses import field
from typing import Optional
from typing import Set

from browzer import BrowzerConfiguration


class TravisConfiguration(BrowzerConfiguration):
    CHROME_OPTIONS: Optional[Set] = field(
        default_factory=lambda: {"no-sandbox", "--disable-extensions", "--headless"}
    )
