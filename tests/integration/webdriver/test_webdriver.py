from threading import Thread

import pytest
from assertpy import assert_that
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver

from sylenium import SyleniumDriver
from sylenium import SyleniumElement
from sylenium.element import ById
from sylenium.sylenium import find
from sylenium.sylenium import go


def test_default_driver(default_driver) -> None:
    default_driver.get("https://www.google.com")
    assert_that(default_driver.get_current_url()).is_equal_to("https://www.google.com/")


def test_loading(webserver) -> None:
    go(webserver.page_url("simple_element"))
    element = find(ById("button1"))
    element.click()
    assert_that(element).is_instance_of(SyleniumElement)


def test_hello_world(webserver) -> None:
    go(webserver.page_url("simple_textarea"))
    sylenium_element = find(ById("textarea"))
    sylenium_element.set_text("Hello world!").clear().set_text("New Version")


def test_multiple(configuration, webserver) -> None:
    t1 = Thread(target=go, args=(webserver.page_url("simple_element"),))
    t2 = Thread(target=go, args=(webserver.page_url("simple_element"),))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def test_single_but_same(configuration) -> None:
    go("https://www.google.com")
    go("https://www.thesun.com")


@pytest.mark.skip(reason="unsupported yet")
def test_remote_browser(driver_creator, configuration) -> None:
    with driver_creator(
        config=configuration(
            remote=True, browser_capabilities={"BrowserName": "chrome"}
        )
    ) as my_driver:
        assert_that(my_driver).is_instance_of(SyleniumDriver)
        assert_that(my_driver.wrapped_driver).is_instance_of(RemoteWebDriver)
