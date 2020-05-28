from browzer import BrowzerConfiguration
from dataclasses import dataclass


@dataclass
class CustomConfig(BrowzerConfiguration):
    HEADLESS: bool = True


@dataclass
class NoInheritance:
    pass
