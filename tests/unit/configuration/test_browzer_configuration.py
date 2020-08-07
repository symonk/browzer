from assertpy import assert_that

from sylenium import configuration
from sylenium.configuration.configuration import Configuration


def test_sylenium_config_load():
    assert_that(configuration).is_instance_of(Configuration)


def test_sylenium_override(headless_config):
    configuration.headless = True
    assert_that(configuration.headless).is_equal_to(True)
