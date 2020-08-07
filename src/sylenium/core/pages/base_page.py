from sylenium.core.sylenium import find
from sylenium.core.sylenium import findall
from sylenium.core.sylenium import get_webdriver


class syleniumPage:
    def __init__(self) -> None:
        self.driver = get_webdriver()
        self.find = find
        self.findall = findall
