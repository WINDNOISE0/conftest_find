import pytest


@pytest.fixture
def load_api_fixture():
    return 1

@pytest.fixture
def api_load_fixture_change():
    return 2