import pytest
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver


@pytest.fixture
def default_driver(default_session) -> RemoteWebDriver:
    return default_session.get_driver()
