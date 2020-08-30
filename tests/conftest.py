import pytest

from sylenium import Configuration
from sylenium import Session


@pytest.fixture
def default_session():
    with Session() as session:
        yield session


@pytest.fixture
def sy_session():
    return Session


@pytest.fixture
def headless_session():
    with Session(configuration=Configuration(headless=True)) as session:
        yield session
