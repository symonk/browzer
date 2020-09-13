from threading import Thread

from assertpy import assert_that

from sylenium.sylenium import go


def test_default_driver(default_driver) -> None:
    default_driver.get("https://www.google.com")
    assert_that(default_driver.get_current_url()).is_equal_to("https://www.google.com/")


def test_loading(webserver) -> None:
    go(webserver.page_url("simple_element"))


def test_multiple(configuration, webserver, mocker) -> None:
    cfg = configuration(headless=False)
    mocker.patch("sylenium.configuration.configuration.DEFAULT_CONFIGURATION", cfg)
    t1 = Thread(target=go, args=(webserver.page_url("simple_element"),))
    t2 = Thread(target=go, args=(webserver.page_url("simple_element"),))
    t1.start()
    t2.start()
    t1.join()
    t2.join()


def test_single_but_same(configuration, mocker) -> None:
    cfg = configuration(headless=False)
    mocker.patch("sylenium.configuration.configuration.DEFAULT_CONFIGURATION", cfg)
    go("https://www.google.com")
    go("https://www.thesun.com")
