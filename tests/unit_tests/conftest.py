import pytest

from sylenium import session_manager


@pytest.fixture(autouse=True)
def clean_up_sessions():
    yield
    session_manager.deactivate()
