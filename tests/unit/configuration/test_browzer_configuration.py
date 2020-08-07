from assertpy import assert_that
from sylenium import config
from sylenium.configuration.sylenium_configuration import syleniumConfiguration


def test_sylenium_config_load():
    assert_that(config).is_instance_of(syleniumConfiguration)


def test_sylenium_override(headless_config):
    config.headless = True
    assert_that(config.headless).is_equal_to(True)
