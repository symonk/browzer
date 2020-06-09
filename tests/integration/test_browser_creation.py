import threading
import time

from assertpy import assert_that

from browzer import BrowzerPage
from browzer import driver_manager


def test_browzer_config_helper():
    one = driver_manager.get_driver()
    two = driver_manager.get_driver()
    assert_that(id(one)).is_equal_to(id(two))


def test_two_browsers_on_seperate_threads_can_be_created():
    driver_manager.get_driver()
    threading.Thread(target=driver_manager.get_driver).start()
    time.sleep(5)
    assert len(driver_manager.drivers) == 2


def test_meta_class_pages():
    class LoginPage(metaclass=BrowzerPage):
        pass

    assert_that(LoginPage().current_url).is_equal_to("data:,")
