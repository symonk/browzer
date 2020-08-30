import pytest

from sylenium.core.sylenium import Session


@pytest.fixture
def default_session():
    with Session() as session:
        yield session


@pytest.fixture
def sy_session():
    return Session
