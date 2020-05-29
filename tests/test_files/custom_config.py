from dataclasses import dataclass

from browzer import BrowzerConfiguration


@dataclass
class CustomConfig(BrowzerConfiguration):
    HEADLESS: bool = True


@dataclass
class NoInheritance:
    pass
