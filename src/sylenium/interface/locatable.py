from typing import Tuple

from selenium.webdriver.common.by import By


class Locatable:
    def __init__(self, by: By, value: str) -> None:
        self.by = by
        self.value = value

    def locate(self) -> Tuple[By, str]:
        return self.by, self.value
