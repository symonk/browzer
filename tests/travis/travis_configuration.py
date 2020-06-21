from dataclasses import dataclass
from dataclasses import field
from typing import Optional
from typing import Set

from browzer import BrowzerConfiguration


@dataclass
class TravisConfiguration(BrowzerConfiguration):
    CHROME_OPTIONS: Optional[Set] = field(
        default_factory=lambda: {"no-sandbox", "--disable-extensions", "--headless"}
    )
