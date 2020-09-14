import os

from assertpy import assert_that
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver

from sylenium import Configuration


def test_chrome_options_headless_standalone(headless_driver):
    assert_that(headless_driver)


def test_service_options_log(driver_creator, tmpdir):
    driver_creator(
        config=Configuration(
            chrome_service_log_path=f"{tmpdir}{os.path.sep}sylenium.log", headless=False
        )
    )


def test_event_wrapper(driver_creator):
    class MyListener(AbstractEventListener):
        pass

    driver = driver_creator(Configuration(driver_event_firing_wrapper=MyListener))
    assert_that(driver.wrapped_driver).is_instance_of(EventFiringWebDriver)
