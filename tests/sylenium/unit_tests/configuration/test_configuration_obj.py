from assertpy import assert_that

from sylenium.configuration import Configuration
from sylenium.configuration import configuration


def test_sylenium_config_load():
    assert_that(configuration).is_instance_of(Configuration)


def test_sylenium_override(headless_config):
    configuration.headless = True
    assert_that(configuration.headless).is_equal_to(True)
