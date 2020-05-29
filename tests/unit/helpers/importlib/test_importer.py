import pytest
from assertpy import assert_that

from browzer import BrowzerConfiguration
from browzer.helpers.importlib.importer import instantiate_class_from_path


def test_importer_returns_instance_successfully(test_files_config_classes):
    clazz = instantiate_class_from_path(test_files_config_classes, BrowzerConfiguration)
    assert_that(clazz).is_instance_of(BrowzerConfiguration)


def test_failing_instance_of():
    path = "tests.test_files.custom_config.NoInheritance"
    with pytest.raises(ValueError) as err:
        instantiate_class_from_path(path, BrowzerConfiguration)
    assert_that(err.value.args[0]).is_equal_to(
        f"Unable to load a class of: {type(BrowzerConfiguration)} from: {path}"
    )


def test_importer_valid_module_no_class():
    path = "tests.test_files.custom_config.DoesNotExist"
    with pytest.raises(AttributeError):
        instantiate_class_from_path(path)


def test_importer_no_such_module():
    with pytest.raises(ModuleNotFoundError):
        instantiate_class_from_path("a.b.c.MadeUp")
