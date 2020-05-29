import pytest
from api_client.api_client import Client


@pytest.fixture()
def norm_auth(auth_data, config):
    return Client(auth_data['user'], auth_data['password'], config)


@pytest.fixture()
def special_auth(config):
    return Client('test_name', 'ad', config)
