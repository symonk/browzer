import pytest
from assertpy import assert_that
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener


def test_driver_event_firing_wrapper_default(configuration):
    assert_that(configuration().driver_event_firing_wrapper).is_none()


def test_driver_event_firing_wrapper_custom(configuration):
    class MyListener(AbstractEventListener):
        pass

    assert_that(
        configuration(
            driver_event_firing_wrapper=MyListener
        ).driver_event_firing_wrapper
    ).is_equal_to(MyListener)


def test_driver_event_firing_wrapper_unsupported_not_class(configuration):
    with pytest.raises(ValueError) as error:
        configuration(configuration(driver_event_firing_wrapper=15))
    assert_that(error.value.args[0]).is_equal_to(
        "driver_event_firing_wrapper= should be of type <class>"
    )


def test_driver_event_firing_wrapper_class_but_not_subclass(configuration):
    class Random:
        pass

    with pytest.raises(ValueError) as error:
        configuration(configuration(driver_event_firing_wrapper=Random))
    assert_that(error.value.args[0]).is_equal_to(
        "driver_event_firing_wrapper= should be of type: <class 'selenium.webdriver.support.abstract_event_listener.AbstractEventListener'>"
    )
