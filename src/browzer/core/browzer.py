from typing import List

from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.remote.webelement import By

from browzer.core.webelement.browzer_element import BrowzerElement


def find(by: By) -> BrowzerElement:
    return get_webdriver().get_driver().find_element(by)


def findall(by: By) -> List[BrowzerElement]:
    return get_webdriver().find_elements(by)


def get_webdriver() -> RemoteWebDriver:
    from browzer import driver_manager

    return driver_manager.get_driver()
