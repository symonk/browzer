import pytest
from assertpy import assert_that

from browzer.helpers.importlib.importer import instantiate_class_from_path
from browzer import BrowzerConfiguration


def test_importer_returns_instance_successfully(monkey_test_files_on_path):
    path = "tests.test_files.custom_config.CustomConfig"
    clazz = instantiate_class_from_path(path, BrowzerConfiguration)
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
