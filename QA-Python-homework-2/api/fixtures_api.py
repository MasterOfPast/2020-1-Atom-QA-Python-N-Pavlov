import pytest
from api.api_client import Client
from some_data.authorization import Authorization_Data as AD
from random import randint


@pytest.fixture(scope='function')
def api_client():
    user = AD.email
    password = AD.password

    return Client(user, password)


@pytest.fixture(scope='function')
def auth_data():
    return (AD.email, AD.password)


@pytest.fixture(scope='function')
def random_data():
    return (randint(100, 100000), randint(100, 10000))


@pytest.fixture(scope='function')
def create_data(random_data):
    data = {
        'name': f'test_name {random_data[0]}',
        'pass_condition': 1,
        'relations': [
            {'object_type': "remarketing_player", 'params': {"type": "positive", "left": 365, "right": 0}}
        ],
        'logicType': "or"
    }
    return data
