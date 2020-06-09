from browzer.core.browzer import find
from browzer.core.browzer import findall
from browzer.core.browzer import get_webdriver


class BrowzerPage:
    def __init__(self) -> None:
        self.driver = get_webdriver()
        self.find = find
        self.findall = findall
