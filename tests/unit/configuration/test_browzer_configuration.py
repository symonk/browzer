from assertpy import assert_that
from browzer import config
from browzer.configuration.browzer_configuration import BrowzerConfiguration


def test_browzer_config_load():
    assert_that(config).is_instance_of(BrowzerConfiguration)


def test_browzer_override(headless_config):
    config.headless = True
    assert_that(config.headless).is_equal_to(True)
