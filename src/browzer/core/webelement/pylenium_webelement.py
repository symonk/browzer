from selenium.webdriver.remote.webelement import WebElement


class BrowzerElement(WebElement):
    """
    Browzers own custom webelement subclass, all driver calls will return an instance of one.
    BrowzerElement is much more robust and test friendly that seleniums default.
    """

    def __init__(self, parent, id_, w3c=False):
        super().__init__(parent, id_, w3c)
