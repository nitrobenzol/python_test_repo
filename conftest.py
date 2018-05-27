import pytest
from fixture.application_group import Application


@pytest.fixture (scope = "session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
