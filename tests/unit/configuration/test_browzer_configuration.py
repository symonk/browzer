from assertpy import assert_that
from browzer import browzer_config
from browzer.configuration.config_loader import BrowzerConfiguration
from browzer.constants.strings import BROWZER_CONFIGURATION


def test_browzer_config_load():
    assert_that(browzer_config).is_instance_of(BrowzerConfiguration)


def test_browzer_override(monkeypatch, yaml_headless_only_true):
    monkeypatch.setenv(BROWZER_CONFIGURATION, yaml_headless_only_true)
    browzer_config.reload()
    assert_that(browzer_config.headless).is_equal_to(True)
