from threading import Thread

from assertpy import assert_that

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
