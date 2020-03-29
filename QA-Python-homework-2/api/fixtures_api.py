import pytest
from api.api_client import Client
from some_data.authorization import Authorization_Data as AD


@pytest.fixture(scope='function')
def api_client():
    user = AD.email
    password = AD.password

    return Client(user, password)
