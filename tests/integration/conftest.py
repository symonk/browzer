import pytest
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


@pytest.fixture
def default_driver(headless_session) -> RemoteWebDriver:
    return headless_session.get_driver()
