from selenium.webdriver.common.by import By

from sylenium.interfaces.locatable import Locatable


class ById(Locatable):
    def __init__(self, value: str) -> None:
        super().__init__(By.ID, value)


class ByXpath(Locatable):
    def __init__(self, value: str) -> None:
        super().__init__(By.XPATH, value)


class ByLinkText(Locatable):
    def __init__(self, value: str) -> None:
        super().__init__(By.LINK_TEXT, value)


class ByPartialLinkText(Locatable):
    def __init__(self, value: str) -> None:
        super().__init__(By.PARTIAL_LINK_TEXT, value)


class ByName(Locatable):
    def __init__(self, value: str) -> None:
        super().__init__(By.NAME, value)


class ByTagName(Locatable):
    def __init__(self, value: str) -> None:
        super().__init__(By.NAME, value)


class ByClassName(Locatable):
    def __init__(self, value: str) -> None:
        super().__init__(By.CLASS_NAME, value)


class ByCssSelector(Locatable):
    def __init__(self, value: str) -> None:
        super().__init__(By.CSS_SELECTOR, value)
