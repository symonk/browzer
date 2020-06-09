from browzer.core.browzer import find
from browzer.core.browzer import findall
from browzer.core.browzer import get_webdriver


class BrowzerPage(type):
    """
    Custom meta class to bolt on a thread scoped driver to your page(s).  This removes the need for explicit
    subclass hierarchies that require drivers being instantiated upfront and passed into a page object as a
    dependency.

    Also attaches the find & findall functionality to browzer based page(s) to ease with element management.
    """

    def __new__(mcs, name, basis, dct):
        dct["driver"] = get_webdriver()
        dct["find"] = find
        dct["findall"] = findall
        return super().__new__(mcs, name, basis, dct)
