import pytest
from browzer import driver_factory


@pytest.fixture(autouse=True)
def destroy_threaded_driver(request):
    request.addfinalizer(driver_factory.terminate_driver)


@pytest.fixture(autouse=True, scope="session")
def destroy_all_drivers(request):
    request.addfinalizer(driver_factory.terminate_all_drivers)
